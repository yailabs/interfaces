#!/usr/bin/env python3
"""Dependency-free conformance checks for V43 license lease consumption."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "license-lease-consumption.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "license-lease-consumption"

EXPECTED_FIXTURES = {
    "valid-lease-consumed.json",
    "expired-lease-blocked.json",
    "revoked-lease-blocked.json",
    "stale-lease-grace.json",
    "missing-machine-authorization.json",
    "safe-lease-projection.json",
}

REQUIRED_STRING_FIELDS = (
    "license_lease_consumption_ref",
    "license_lease_ref",
)

FORBIDDEN_KEYS = {
    "billing_customer",
    "stripe_customer",
    "subscription",
    "invoice",
    "price",
    "plan_object",
    "supabase_user",
    "provider_user",
}

SECRET_KEYS = {
    "api_key",
    "token",
    "secret",
    "password",
    "private_key",
}

SAFE_PROJECTION_KEYS = {
    "license_lease_ref",
    "lease_status",
    "consumption_status",
    "scope",
    "grace_posture",
    "stale_posture",
    "refresh_posture",
    "diagnostic_posture",
    "sealed_posture",
    "expires_at",
    "warning_codes",
}


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_enums(schema: dict) -> dict[str, set[str]]:
    defs = schema["$defs"]
    return {
        "lease_status": set(defs["leaseStatus"]["enum"]),
        "consumption_status": set(defs["consumptionStatus"]["enum"]),
        "scope": set(defs["leaseScope"]["enum"]),
        "lease_source": set(defs["leaseSource"]["enum"]),
        "grace_posture": set(defs["gracePosture"]["enum"]),
        "stale_posture": set(defs["stalePosture"]["enum"]),
        "refresh_posture": set(defs["refreshPosture"]["enum"]),
        "revocation_posture": set(defs["revocationPosture"]["enum"]),
        "diagnostic_posture": set(defs["diagnosticPosture"]["enum"]),
        "sealed_posture": set(defs["sealedPosture"]["enum"]),
        "blocked_reason": set(defs["blockedReason"]["enum"]),
        "warning_codes": set(defs["warningCode"]["enum"]),
    }


def walk_keys(node: object, errors: list[str], path: str = "$") -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key in FORBIDDEN_KEYS:
                errors.append(f"{path}.{key}: forbidden billing/private/provider field")
            if key in SECRET_KEYS:
                errors.append(f"{path}.{key}: forbidden secret-like key")
            walk_keys(value, errors, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            walk_keys(value, errors, f"{path}[{index}]")


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_safe_projection(name: str, projection: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(projection, dict), f"{name}: safe_lease_projection must be an object", errors)
    if not isinstance(projection, dict):
        return

    extra = set(projection.keys()) - SAFE_PROJECTION_KEYS
    require(not extra, f"{name}: safe_lease_projection has unsafe keys {sorted(extra)}", errors)

    value = projection.get("license_lease_ref")
    require(
        isinstance(value, str) and value.strip(),
        f"{name}: safe_lease_projection.license_lease_ref must be non-empty",
        errors,
    )

    for field in (
        "lease_status",
        "consumption_status",
        "scope",
        "grace_posture",
        "stale_posture",
        "refresh_posture",
        "diagnostic_posture",
        "sealed_posture",
    ):
        value = projection.get(field)
        require(value in enums[field], f"{name}: unknown safe_lease_projection {field} {value!r}", errors)

    if "warning_codes" in projection:
        require(isinstance(projection["warning_codes"], list), f"{name}: safe_lease_projection.warning_codes must be a list", errors)
        if isinstance(projection["warning_codes"], list):
            for code in projection["warning_codes"]:
                require(code in enums["warning_codes"], f"{name}: unknown safe_lease_projection warning code {code!r}", errors)


def validate_fixture(name: str, payload: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(payload, dict), f"{name}: top-level JSON must be an object", errors)
    if not isinstance(payload, dict):
        return

    require(
        "license_lease_consumption" in payload,
        f"{name}: missing license_lease_consumption",
        errors,
    )
    consumption = payload.get("license_lease_consumption")
    require(isinstance(consumption, dict), f"{name}: license_lease_consumption must be an object", errors)
    if not isinstance(consumption, dict):
        return

    for field in REQUIRED_STRING_FIELDS:
        value = consumption.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field} must be a non-empty string", errors)

    for field in (
        "lease_status",
        "consumption_status",
        "scope",
        "lease_source",
        "grace_posture",
        "stale_posture",
        "refresh_posture",
        "revocation_posture",
        "diagnostic_posture",
        "sealed_posture",
    ):
        value = consumption.get(field)
        require(value in enums[field], f"{name}: unknown {field} {value!r}", errors)

    if "blocked_reason" in consumption:
        value = consumption["blocked_reason"]
        require(value in enums["blocked_reason"], f"{name}: unknown blocked_reason {value!r}", errors)

    if "warning_codes" in consumption:
        require(isinstance(consumption["warning_codes"], list), f"{name}: warning_codes must be a list", errors)
        if isinstance(consumption["warning_codes"], list):
            for code in consumption["warning_codes"]:
                require(code in enums["warning_codes"], f"{name}: unknown warning code {code!r}", errors)

    if "safe_lease_projection" in consumption:
        validate_safe_projection(name, consumption["safe_lease_projection"], enums, errors)

    walk_keys(payload, errors)

    if consumption.get("consumption_status") in {"blocked", "stale_rejected"} or consumption.get("lease_status") in {"expired", "revoked", "blocked"}:
        require("blocked_reason" in consumption, f"{name}: blocked or unusable posture requires blocked_reason", errors)


def main() -> int:
    errors: list[str] = []

    schema = load_json(SCHEMA_PATH)
    require(isinstance(schema, dict), "schema: must be a JSON object", errors)
    if not isinstance(schema, dict):
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    enums = schema_enums(schema)

    fixture_paths = sorted(FIXTURE_DIR.glob("*.json"))
    names = {path.name for path in fixture_paths}
    require(names == EXPECTED_FIXTURES, f"fixtures: expected {sorted(EXPECTED_FIXTURES)}, found {sorted(names)}", errors)

    for path in fixture_paths:
        payload = load_json(path)
        validate_fixture(path.name, payload, enums, errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("license-lease-consumption: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
