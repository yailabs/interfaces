#!/usr/bin/env python3
"""Dependency-free conformance checks for V46 runtime license check request."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "runtime-license-check-request.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "runtime-license-check-request"

EXPECTED_FIXTURES = {
    "full-online-check-request.json",
    "missing-machine-authorization-request.json",
    "cached-lease-refresh-request.json",
    "offline-stale-posture-request.json",
    "account-limit-reconciliation-request.json",
    "safe-request-projection.json",
}

REQUIRED_STRING_FIELDS = (
    "runtime_license_check_request_ref",
    "local_machine_ref",
    "requested_at",
)

LIST_FIELDS = {
    "limit_projection_refs",
    "requested_actions",
    "warning_codes",
}

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

FINAL_RESPONSE_KEYS = {
    "allowed",
    "denied",
    "final_decision",
    "response_status",
}


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_enums(schema: dict) -> dict[str, set[str]]:
    defs = schema["$defs"]
    return {
        "request_kind": set(defs["requestKind"]["enum"]),
        "check_scope": set(defs["checkScope"]["enum"]),
        "request_context": set(defs["requestContext"]["enum"]),
        "request_freshness": set(defs["requestFreshness"]["enum"]),
        "connectivity_posture": set(defs["connectivityPosture"]["enum"]),
        "privacy_posture": set(defs["privacyPosture"]["enum"]),
        "next_expected_response": set(defs["nextExpectedResponse"]["enum"]),
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
            if key in FINAL_RESPONSE_KEYS:
                errors.append(f"{path}.{key}: forbidden final response field")
            walk_keys(value, errors, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            walk_keys(value, errors, f"{path}[{index}]")


def validate_fixture(name: str, payload: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(payload, dict), f"{name}: top-level JSON must be an object", errors)
    if not isinstance(payload, dict):
        return

    require(
        "runtime_license_check_request" in payload,
        f"{name}: missing runtime_license_check_request",
        errors,
    )
    request = payload.get("runtime_license_check_request")
    require(
        isinstance(request, dict),
        f"{name}: runtime_license_check_request must be an object",
        errors,
    )
    if not isinstance(request, dict):
        return

    for field in REQUIRED_STRING_FIELDS:
        value = request.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field} must be a non-empty string", errors)

    for field in (
        "request_kind",
        "check_scope",
        "request_context",
        "request_freshness",
        "connectivity_posture",
        "privacy_posture",
        "next_expected_response",
    ):
        value = request.get(field)
        require(value in enums[field], f"{name}: unknown {field} {value!r}", errors)

    for field in LIST_FIELDS:
        if field in request:
            require(isinstance(request[field], list), f"{name}: {field} must be a list", errors)

    if "warning_codes" in request and isinstance(request["warning_codes"], list):
        for code in request["warning_codes"]:
            require(code in enums["warning_codes"], f"{name}: unknown warning code {code!r}", errors)

    if "limit_projection_refs" in request and isinstance(request["limit_projection_refs"], list):
        for value in request["limit_projection_refs"]:
            require(isinstance(value, str) and value.strip(), f"{name}: limit_projection_refs must contain non-empty strings", errors)

    if "requested_actions" in request and isinstance(request["requested_actions"], list):
        for value in request["requested_actions"]:
            require(isinstance(value, str) and value.strip(), f"{name}: requested_actions must contain non-empty strings", errors)

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
    require(
        names == EXPECTED_FIXTURES,
        f"fixtures: expected {sorted(EXPECTED_FIXTURES)}, found {sorted(names)}",
        errors,
    )

    for path in fixture_paths:
        payload = load_json(path)
        validate_fixture(path.name, payload, enums, errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("runtime-license-check-request: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
