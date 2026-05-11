#!/usr/bin/env python3
"""Dependency-free conformance checks for V47 runtime license check response."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "runtime-license-check-response.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "runtime-license-check-response"

EXPECTED_FIXTURES = {
    "allowed-response.json",
    "blocked-missing-machine-authorization.json",
    "blocked-expired-lease.json",
    "blocked-limit-exceeded.json",
    "grace-response.json",
    "safe-response-projection.json",
}

REQUIRED_STRING_FIELDS = (
    "runtime_license_check_response_ref",
    "runtime_license_check_request_ref",
    "reason",
    "responded_at",
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

REQUEST_ONLY_KEYS = {
    "request_kind",
    "check_scope",
    "request_context",
    "request_freshness",
    "connectivity_posture",
    "privacy_posture",
    "requested_at",
    "requested_actions",
    "next_expected_response",
}

SAFE_LEASE_KEYS = {
    "license_lease_ref",
    "lease_posture",
    "expires_at",
    "warning_codes",
}

SAFE_MACHINE_KEYS = {
    "machine_authorization_ref",
    "machine_authorization_posture",
    "expires_at",
    "warning_codes",
}

SAFE_LIMIT_KEYS = {
    "limit_projection_ref",
    "limit_posture",
    "warning_codes",
}

SAFE_GATE_KEYS = {
    "runtime_gate_decision_ref",
    "runtime_gate_posture",
    "warning_codes",
}


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_enums(schema: dict) -> dict[str, set[str]]:
    defs = schema["$defs"]
    return {
        "decision": set(defs["decision"]["enum"]),
        "blocked_reason": set(defs["blockedReason"]["enum"]),
        "next_action": set(defs["nextAction"]["enum"]),
        "response_freshness": set(defs["responseFreshness"]["enum"]),
        "lease_posture": set(defs["leasePosture"]["enum"]),
        "machine_authorization_posture": set(defs["machineAuthorizationPosture"]["enum"]),
        "entitlement_posture": set(defs["entitlementPosture"]["enum"]),
        "limit_posture": set(defs["limitPosture"]["enum"]),
        "runtime_gate_posture": set(defs["runtimeGatePosture"]["enum"]),
        "offline_grace_posture": set(defs["offlineGracePosture"]["enum"]),
        "cache_update_posture": set(defs["cacheUpdatePosture"]["enum"]),
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
            if key in REQUEST_ONLY_KEYS:
                errors.append(f"{path}.{key}: forbidden request-only field")
            walk_keys(value, errors, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            walk_keys(value, errors, f"{path}[{index}]")


def validate_warning_codes(name: str, value: object, enums: dict[str, set[str]], field_name: str, errors: list[str]) -> None:
    require(isinstance(value, list), f"{name}: {field_name} must be a list", errors)
    if isinstance(value, list):
        for code in value:
            require(code in enums["warning_codes"], f"{name}: unknown warning code {code!r}", errors)


def validate_safe_projection(
    name: str,
    field_name: str,
    projection: object,
    allowed_keys: set[str],
    required_fields: tuple[str, ...],
    enum_fields: dict[str, str],
    enums: dict[str, set[str]],
    errors: list[str],
) -> None:
    require(isinstance(projection, dict), f"{name}: {field_name} must be an object", errors)
    if not isinstance(projection, dict):
        return

    extra = set(projection.keys()) - allowed_keys
    require(not extra, f"{name}: {field_name} has unsafe keys {sorted(extra)}", errors)

    for required_field in required_fields:
        value = projection.get(required_field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field_name}.{required_field} must be non-empty", errors)

    for field, enum_name in enum_fields.items():
        value = projection.get(field)
        require(value in enums[enum_name], f"{name}: unknown {field_name} {field} {value!r}", errors)

    if "warning_codes" in projection:
        validate_warning_codes(name, projection["warning_codes"], enums, f"{field_name}.warning_codes", errors)


def validate_fixture(name: str, payload: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(payload, dict), f"{name}: top-level JSON must be an object", errors)
    if not isinstance(payload, dict):
        return

    require("runtime_license_check_response" in payload, f"{name}: missing runtime_license_check_response", errors)
    response = payload.get("runtime_license_check_response")
    require(isinstance(response, dict), f"{name}: runtime_license_check_response must be an object", errors)
    if not isinstance(response, dict):
        return

    for field in REQUIRED_STRING_FIELDS:
        value = response.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field} must be a non-empty string", errors)

    for field in (
        "decision",
        "next_action",
        "response_freshness",
        "lease_posture",
        "machine_authorization_posture",
        "entitlement_posture",
        "limit_posture",
        "runtime_gate_posture",
        "offline_grace_posture",
        "cache_update_posture",
    ):
        value = response.get(field)
        require(value in enums[field], f"{name}: unknown {field} {value!r}", errors)

    if "blocked_reason" in response:
        require(response["blocked_reason"] in enums["blocked_reason"], f"{name}: unknown blocked_reason {response['blocked_reason']!r}", errors)

    if "warning_codes" in response:
        validate_warning_codes(name, response["warning_codes"], enums, "warning_codes", errors)

    if "safe_license_lease_projection" in response:
        validate_safe_projection(
            name,
            "safe_license_lease_projection",
            response["safe_license_lease_projection"],
            SAFE_LEASE_KEYS,
            ("license_lease_ref",),
            {"lease_posture": "lease_posture"},
            enums,
            errors,
        )

    if "safe_machine_authorization_projection" in response:
        validate_safe_projection(
            name,
            "safe_machine_authorization_projection",
            response["safe_machine_authorization_projection"],
            SAFE_MACHINE_KEYS,
            ("machine_authorization_ref",),
            {"machine_authorization_posture": "machine_authorization_posture"},
            enums,
            errors,
        )

    if "safe_limit_projection" in response:
        validate_safe_projection(
            name,
            "safe_limit_projection",
            response["safe_limit_projection"],
            SAFE_LIMIT_KEYS,
            ("limit_projection_ref",),
            {"limit_posture": "limit_posture"},
            enums,
            errors,
        )

    if "safe_runtime_gate_decision" in response:
        validate_safe_projection(
            name,
            "safe_runtime_gate_decision",
            response["safe_runtime_gate_decision"],
            SAFE_GATE_KEYS,
            ("runtime_gate_decision_ref",),
            {"runtime_gate_posture": "runtime_gate_posture"},
            enums,
            errors,
        )

    if response.get("decision") == "blocked":
        require("blocked_reason" in response, f"{name}: blocked decisions require blocked_reason", errors)

    if name == "allowed-response.json":
        require("blocked_reason" not in response, f"{name}: allowed response must not include blocked_reason", errors)

    walk_keys(payload, errors)


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

    print("runtime-license-check-response: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
