#!/usr/bin/env python3
"""Dependency-free conformance checks for V42 machine authorization consumption."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "machine-authorization-consumption.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "machine-authorization-consumption"

EXPECTED_FIXTURES = {
    "authorized-machine-consumed.json",
    "revoked-machine-blocked.json",
    "expired-machine-blocked.json",
    "pending-machine-diagnostics-only.json",
    "missing-license-lease-required.json",
    "safe-status-projection.json",
}

REQUIRED_STRING_FIELDS = (
    "machine_authorization_consumption_ref",
    "machine_authorization_ref",
    "local_machine_ref",
)

FORBIDDEN_KEYS = {
    "serial_number",
    "serial",
    "mac_address",
    "mac",
    "hardware_uuid",
    "hardware_id",
    "raw_fingerprint",
    "raw_hardware_fingerprint",
    "provider_user",
    "supabase_user",
    "billing_customer",
}

SECRET_KEYS = {
    "api_key",
    "token",
    "secret",
    "password",
    "private_key",
}

SAFE_PROJECTION_KEYS = {
    "machine_authorization_ref",
    "local_machine_ref",
    "authorization_status",
    "consumption_status",
    "authorization_scope",
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
        "authorization_status": set(defs["authorizationStatus"]["enum"]),
        "consumption_status": set(defs["consumptionStatus"]["enum"]),
        "authorization_scope": set(defs["authorizationScope"]["enum"]),
        "authorization_source": set(defs["authorizationSource"]["enum"]),
        "lease_requirement_posture": set(defs["leaseRequirementPosture"]["enum"]),
        "diagnostic_posture": set(defs["diagnosticPosture"]["enum"]),
        "sealed_posture": set(defs["sealedPosture"]["enum"]),
        "blocked_reason": set(defs["blockedReason"]["enum"]),
        "warning_codes": set(defs["warningCode"]["enum"]),
    }


def walk_keys(node: object, errors: list[str], path: str = "$") -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key in FORBIDDEN_KEYS:
                errors.append(f"{path}.{key}: forbidden private/raw field")
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
    require(isinstance(projection, dict), f"{name}: safe_status_projection must be an object", errors)
    if not isinstance(projection, dict):
        return

    extra = set(projection.keys()) - SAFE_PROJECTION_KEYS
    require(not extra, f"{name}: safe_status_projection has unsafe keys {sorted(extra)}", errors)

    for field in (
        "machine_authorization_ref",
        "local_machine_ref",
    ):
        value = projection.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: safe_status_projection.{field} must be non-empty", errors)

    for field in (
        "authorization_status",
        "consumption_status",
        "authorization_scope",
        "diagnostic_posture",
        "sealed_posture",
    ):
        value = projection.get(field)
        require(value in enums[field], f"{name}: unknown safe_status_projection {field} {value!r}", errors)

    if "warning_codes" in projection:
        require(isinstance(projection["warning_codes"], list), f"{name}: safe_status_projection.warning_codes must be a list", errors)
        if isinstance(projection["warning_codes"], list):
            for code in projection["warning_codes"]:
                require(code in enums["warning_codes"], f"{name}: unknown safe_status_projection warning code {code!r}", errors)


def validate_fixture(name: str, payload: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(payload, dict), f"{name}: top-level JSON must be an object", errors)
    if not isinstance(payload, dict):
        return

    require(
        "machine_authorization_consumption" in payload,
        f"{name}: missing machine_authorization_consumption",
        errors,
    )
    consumption = payload.get("machine_authorization_consumption")
    require(isinstance(consumption, dict), f"{name}: machine_authorization_consumption must be an object", errors)
    if not isinstance(consumption, dict):
        return

    for field in REQUIRED_STRING_FIELDS:
        value = consumption.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field} must be a non-empty string", errors)

    for field in (
        "authorization_status",
        "consumption_status",
        "authorization_scope",
        "authorization_source",
        "lease_requirement_posture",
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

    if "safe_status_projection" in consumption:
        validate_safe_projection(name, consumption["safe_status_projection"], enums, errors)

    walk_keys(payload, errors)

    if consumption.get("consumption_status") == "blocked" or consumption.get("authorization_status") in {"revoked", "expired", "blocked"}:
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

    print("machine-authorization-consumption: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
