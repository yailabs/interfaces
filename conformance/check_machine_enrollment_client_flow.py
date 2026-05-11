#!/usr/bin/env python3
"""Dependency-free conformance checks for V41 machine enrollment client flow."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "machine-enrollment-client-flow.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "machine-enrollment-client-flow"

EXPECTED_FIXTURES = {
    "local-client-enrollment-request.json",
    "browser-confirmation-required.json",
    "device-code-pending.json",
    "enrollment-blocked-missing-auth.json",
    "enrollment-blocked-privacy-review.json",
    "enrollment-completed-with-authorization-ref.json",
}

REQUIRED_STRING_FIELDS = (
    "machine_enrollment_request_ref",
    "local_machine_identity_ref",
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
    "motherboard_serial",
    "disk_serial",
    "cpu_serial",
    "device_serial",
}

SECRET_KEYS = {
    "api_key",
    "token",
    "secret",
    "password",
    "private_key",
    "signing_key",
    "salt",
    "raw_salt",
}


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_enums(schema: dict) -> dict[str, set[str]]:
    defs = schema["$defs"]
    return {
        "enrollment_intent": set(defs["enrollmentIntent"]["enum"]),
        "enrollment_channel": set(defs["enrollmentChannel"]["enum"]),
        "enrollment_status": set(defs["enrollmentStatus"]["enum"]),
        "account_confirmation_posture": set(defs["accountConfirmationPosture"]["enum"]),
        "browser_handoff_posture": set(defs["browserHandoffPosture"]["enum"]),
        "device_code_posture": set(defs["deviceCodePosture"]["enum"]),
        "privacy_posture": set(defs["privacyPosture"]["enum"]),
        "consent_posture": set(defs["consentPosture"]["enum"]),
        "machine_authorization_status": set(defs["machineAuthorizationStatus"]["enum"]),
        "blocked_reason": set(defs["blockedReason"]["enum"]),
        "next_actions": set(defs["nextAction"]["enum"]),
        "warning_codes": set(defs["warningCode"]["enum"]),
    }


def walk_keys(node: object, errors: list[str], path: str = "$") -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key in FORBIDDEN_KEYS:
                errors.append(f"{path}.{key}: forbidden raw hardware key")
            if key in SECRET_KEYS:
                errors.append(f"{path}.{key}: forbidden secret-like key")
            walk_keys(value, errors, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            walk_keys(value, errors, f"{path}[{index}]")


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_fixture(name: str, payload: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(payload, dict), f"{name}: top-level JSON must be an object", errors)
    if not isinstance(payload, dict):
        return

    require("machine_enrollment_request" in payload, f"{name}: missing machine_enrollment_request", errors)
    request = payload.get("machine_enrollment_request")
    require(isinstance(request, dict), f"{name}: machine_enrollment_request must be an object", errors)
    if not isinstance(request, dict):
        return

    for field in REQUIRED_STRING_FIELDS:
        value = request.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field} must be a non-empty string", errors)

    for field in (
        "enrollment_intent",
        "enrollment_channel",
        "enrollment_status",
        "account_confirmation_posture",
        "browser_handoff_posture",
        "device_code_posture",
        "privacy_posture",
        "consent_posture",
    ):
        value = request.get(field)
        require(value in enums[field], f"{name}: unknown {field} {value!r}", errors)

    if "machine_authorization_status" in request:
        value = request["machine_authorization_status"]
        require(
            value in enums["machine_authorization_status"],
            f"{name}: unknown machine_authorization_status {value!r}",
            errors,
        )

    if "blocked_reason" in request:
        value = request["blocked_reason"]
        require(value in enums["blocked_reason"], f"{name}: unknown blocked_reason {value!r}", errors)

    if "next_actions" in request:
        require(isinstance(request["next_actions"], list), f"{name}: next_actions must be a list", errors)
        if isinstance(request["next_actions"], list):
            for action in request["next_actions"]:
                require(action in enums["next_actions"], f"{name}: unknown next action {action!r}", errors)

    if "warning_codes" in request:
        require(isinstance(request["warning_codes"], list), f"{name}: warning_codes must be a list", errors)
        if isinstance(request["warning_codes"], list):
            for code in request["warning_codes"]:
                require(code in enums["warning_codes"], f"{name}: unknown warning code {code!r}", errors)

    walk_keys(payload, errors)

    if request.get("enrollment_status") == "blocked":
        require("blocked_reason" in request, f"{name}: blocked status requires blocked_reason", errors)

    if name == "browser-confirmation-required.json":
        require(
            request.get("browser_handoff_posture") in {"required", "ready_to_open", "opened"},
            f"{name}: browser fixture must use browser handoff posture required/ready/opened",
            errors,
        )

    if name == "device-code-pending.json":
        require(
            request.get("device_code_posture") in {"required", "generated", "pending_poll"},
            f"{name}: device-code fixture must use required/generated/pending_poll posture",
            errors,
        )


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

    print("machine-enrollment-client-flow: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
