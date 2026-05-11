#!/usr/bin/env python3
"""Dependency-free conformance checks for V48 runtime sealed-by-license behavior."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "runtime-sealed-by-license-behavior.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "runtime-sealed-by-license-behavior"

EXPECTED_FIXTURES = {
    "unsealed-valid-license.json",
    "sealed-missing-machine-authorization.json",
    "sealed-expired-license-lease.json",
    "sealed-limit-exceeded.json",
    "diagnostics-only-stale-response.json",
    "safe-seal-status-projection.json",
}

REQUIRED_STRING_FIELDS = ("runtime_license_seal_state_ref",)

FORBIDDEN_KEYS = {
    "billing_customer",
    "stripe_customer",
    "subscription",
    "invoice",
    "price",
    "plan_object",
    "supabase_user",
    "provider_user",
    "raw_fingerprint",
    "serial_number",
    "mac_address",
}

RAW_HARDWARE_KEYS = {
    "serial",
    "hardware_uuid",
    "uuid",
    "motherboard_serial",
    "disk_serial",
    "cpu_serial",
    "device_serial",
    "mac",
    "macs",
}

SECRET_KEYS = {
    "api_key",
    "token",
    "secret",
    "password",
    "private_key",
}

SAFE_STATUS_KEYS = {
    "seal_state",
    "seal_reason",
    "operational_readiness",
    "diagnostic_posture",
    "allowed_surface_posture",
    "blocked_surface_posture",
    "recovery_posture",
    "next_action",
    "response_freshness",
    "warning_codes",
}


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_enums(schema: dict) -> dict[str, set[str]]:
    defs = schema["$defs"]
    return {
        "seal_state": set(defs["sealState"]["enum"]),
        "seal_reason": set(defs["sealReason"]["enum"]),
        "operational_readiness": set(defs["operationalReadiness"]["enum"]),
        "diagnostic_posture": set(defs["diagnosticPosture"]["enum"]),
        "allowed_surface_posture": set(defs["allowedSurfacePosture"]["enum"]),
        "blocked_surface_posture": set(defs["blockedSurfacePosture"]["enum"]),
        "recovery_posture": set(defs["recoveryPosture"]["enum"]),
        "next_action": set(defs["nextAction"]["enum"]),
        "response_freshness": set(defs["responseFreshness"]["enum"]),
        "cache_posture": set(defs["cachePosture"]["enum"]),
        "offline_grace_posture": set(defs["offlineGracePosture"]["enum"]),
        "warning_codes": set(defs["warningCode"]["enum"]),
    }


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def walk_keys(node: object, errors: list[str], path: str = "$") -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key in FORBIDDEN_KEYS:
                errors.append(f"{path}.{key}: forbidden billing/private/provider/raw field")
            if key in RAW_HARDWARE_KEYS:
                errors.append(f"{path}.{key}: forbidden raw hardware key")
            if key in SECRET_KEYS:
                errors.append(f"{path}.{key}: forbidden secret-like key")
            walk_keys(value, errors, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            walk_keys(value, errors, f"{path}[{index}]")


def validate_warning_codes(name: str, value: object, enums: dict[str, set[str]], field_name: str, errors: list[str]) -> None:
    require(isinstance(value, list), f"{name}: {field_name} must be a list", errors)
    if isinstance(value, list):
        for code in value:
            require(code in enums["warning_codes"], f"{name}: unknown warning code {code!r}", errors)


def validate_safe_status_projection(name: str, projection: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(projection, dict), f"{name}: safe_status_projection must be an object", errors)
    if not isinstance(projection, dict):
        return

    extra = set(projection.keys()) - SAFE_STATUS_KEYS
    require(not extra, f"{name}: safe_status_projection has unsafe keys {sorted(extra)}", errors)

    for field in (
        "seal_state",
        "seal_reason",
        "operational_readiness",
        "diagnostic_posture",
        "allowed_surface_posture",
        "blocked_surface_posture",
        "recovery_posture",
        "next_action",
        "response_freshness",
    ):
        value = projection.get(field)
        require(value in enums[field], f"{name}: unknown safe_status_projection {field} {value!r}", errors)

    if "warning_codes" in projection:
        validate_warning_codes(name, projection["warning_codes"], enums, "safe_status_projection.warning_codes", errors)


def validate_fixture(name: str, payload: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(payload, dict), f"{name}: top-level JSON must be an object", errors)
    if not isinstance(payload, dict):
        return

    require("runtime_license_seal_state" in payload, f"{name}: missing runtime_license_seal_state", errors)
    state = payload.get("runtime_license_seal_state")
    require(isinstance(state, dict), f"{name}: runtime_license_seal_state must be an object", errors)
    if not isinstance(state, dict):
        return

    for field in REQUIRED_STRING_FIELDS:
        value = state.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field} must be a non-empty string", errors)

    for field in (
        "seal_state",
        "seal_reason",
        "operational_readiness",
        "diagnostic_posture",
        "allowed_surface_posture",
        "blocked_surface_posture",
        "recovery_posture",
        "next_action",
        "response_freshness",
    ):
        value = state.get(field)
        require(value in enums[field], f"{name}: unknown {field} {value!r}", errors)

    for field in ("cache_posture", "offline_grace_posture"):
        if field in state:
            require(state[field] in enums[field], f"{name}: unknown {field} {state[field]!r}", errors)

    if "warning_codes" in state:
        validate_warning_codes(name, state["warning_codes"], enums, "warning_codes", errors)

    if "safe_status_projection" in state:
        validate_safe_status_projection(name, state["safe_status_projection"], enums, errors)

    if name.startswith("sealed-"):
        require(
            state.get("operational_readiness") != "ready",
            f"{name}: sealed fixture must not mark operational_readiness as ready",
            errors,
        )

    if name == "unsealed-valid-license.json":
        require(state.get("seal_reason") == "none", f"{name}: unsealed fixture must use seal_reason none", errors)

    if name == "diagnostics-only-stale-response.json":
        require(
            state.get("operational_readiness") == "diagnostics_only",
            f"{name}: diagnostics-only fixture must use operational_readiness diagnostics_only",
            errors,
        )

    walk_keys(payload, errors)


def main() -> int:
    errors: list[str] = []

    schema = load_json(SCHEMA_PATH)
    require(isinstance(schema, dict), "schema: top-level JSON must be an object", errors)
    if not isinstance(schema, dict):
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    fixtures = sorted(FIXTURE_DIR.glob("*.json"))
    names = {fixture.name for fixture in fixtures}
    require(names == EXPECTED_FIXTURES, f"fixtures: expected {sorted(EXPECTED_FIXTURES)}, found {sorted(names)}", errors)

    enums = schema_enums(schema)
    for fixture in fixtures:
        validate_fixture(fixture.name, load_json(fixture), enums, errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("runtime-sealed-by-license-behavior: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
