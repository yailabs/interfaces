#!/usr/bin/env python3
"""Dependency-free conformance checks for V49 offline grace / stale lease behavior."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "offline-grace-stale-lease-behavior.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "offline-grace-stale-lease-behavior"

EXPECTED_FIXTURES = {
    "grace-active-limited-operational.json",
    "grace-expired-sealed.json",
    "stale-lease-diagnostics-only.json",
    "offline-refresh-required.json",
    "online-refresh-recovers.json",
    "safe-grace-projection.json",
}

REQUIRED_STRING_FIELDS = ("offline_grace_state_ref",)

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

SAFE_GRACE_KEYS = {
    "grace_status",
    "stale_lease_status",
    "offline_status",
    "operational_readiness",
    "diagnostic_posture",
    "allowed_surface_posture",
    "blocked_surface_posture",
    "refresh_posture",
    "next_action",
    "grace_expires_at",
    "warning_codes",
}


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_enums(schema: dict) -> dict[str, set[str]]:
    defs = schema["$defs"]
    return {
        "grace_status": set(defs["graceStatus"]["enum"]),
        "stale_lease_status": set(defs["staleLeaseStatus"]["enum"]),
        "offline_status": set(defs["offlineStatus"]["enum"]),
        "connectivity_posture": set(defs["connectivityPosture"]["enum"]),
        "operational_readiness": set(defs["operationalReadiness"]["enum"]),
        "diagnostic_posture": set(defs["diagnosticPosture"]["enum"]),
        "allowed_surface_posture": set(defs["allowedSurfacePosture"]["enum"]),
        "blocked_surface_posture": set(defs["blockedSurfacePosture"]["enum"]),
        "refresh_posture": set(defs["refreshPosture"]["enum"]),
        "recovery_posture": set(defs["recoveryPosture"]["enum"]),
        "next_action": set(defs["nextAction"]["enum"]),
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


def validate_safe_grace_projection(name: str, projection: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(projection, dict), f"{name}: safe_grace_projection must be an object", errors)
    if not isinstance(projection, dict):
        return

    extra = set(projection.keys()) - SAFE_GRACE_KEYS
    require(not extra, f"{name}: safe_grace_projection has unsafe keys {sorted(extra)}", errors)

    for field in (
        "grace_status",
        "stale_lease_status",
        "offline_status",
        "operational_readiness",
        "diagnostic_posture",
        "allowed_surface_posture",
        "blocked_surface_posture",
        "refresh_posture",
        "next_action",
    ):
        value = projection.get(field)
        require(value in enums[field], f"{name}: unknown safe_grace_projection {field} {value!r}", errors)

    if "warning_codes" in projection:
        validate_warning_codes(name, projection["warning_codes"], enums, "safe_grace_projection.warning_codes", errors)


def validate_fixture(name: str, payload: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(payload, dict), f"{name}: top-level JSON must be an object", errors)
    if not isinstance(payload, dict):
        return

    require("offline_grace_state" in payload, f"{name}: missing offline_grace_state", errors)
    state = payload.get("offline_grace_state")
    require(isinstance(state, dict), f"{name}: offline_grace_state must be an object", errors)
    if not isinstance(state, dict):
        return

    for field in REQUIRED_STRING_FIELDS:
        value = state.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field} must be a non-empty string", errors)

    for field in (
        "grace_status",
        "stale_lease_status",
        "offline_status",
        "connectivity_posture",
        "operational_readiness",
        "diagnostic_posture",
        "allowed_surface_posture",
        "blocked_surface_posture",
        "refresh_posture",
        "recovery_posture",
        "next_action",
    ):
        value = state.get(field)
        require(value in enums[field], f"{name}: unknown {field} {value!r}", errors)

    if "warning_codes" in state:
        validate_warning_codes(name, state["warning_codes"], enums, "warning_codes", errors)

    if "safe_grace_projection" in state:
        validate_safe_grace_projection(name, state["safe_grace_projection"], enums, errors)

    if name == "grace-expired-sealed.json":
        require(
            state.get("operational_readiness") != "ready",
            f"{name}: grace_expired fixture must not mark operational_readiness as ready",
            errors,
        )

    if name == "stale-lease-diagnostics-only.json":
        require(
            state.get("operational_readiness") == "diagnostics_only",
            f"{name}: stale diagnostics fixture must use operational_readiness diagnostics_only",
            errors,
        )
        require(
            state.get("allowed_surface_posture") == "diagnostics_only",
            f"{name}: stale diagnostics fixture must use allowed_surface_posture diagnostics_only",
            errors,
        )

    if name == "grace-active-limited-operational.json":
        require(state.get("grace_status") == "grace_active", f"{name}: grace active fixture must use grace_active", errors)
        require(
            state.get("allowed_surface_posture") == "limited_operational",
            f"{name}: grace active fixture must remain bounded to limited_operational",
            errors,
        )
        require(
            state.get("allowed_surface_posture") != "operational_allowed",
            f"{name}: grace active fixture must not imply full operational_allowed access",
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

    print("offline-grace-stale-lease-behavior: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
