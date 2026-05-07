#!/usr/bin/env python3
"""Dependency-free conformance checks for V39 local machine identity store."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "local-machine-identity-store.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "local-machine-identity-store"

EXPECTED_FIXTURES = {
    "new-local-identity.json",
    "existing-local-identity.json",
    "rotated-local-identity.json",
    "revoked-local-identity.json",
    "no-raw-hardware-fields.json",
    "reboot-continuity-posture.json",
}

REQUIRED_STRING_FIELDS = (
    "local_machine_identity_ref",
    "local_machine_ref",
    "machine_identity_store_ref",
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
}

SECRET_KEYS = {
    "api_key",
    "token",
    "secret",
    "password",
    "private_key",
}


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_enums(schema: dict) -> dict[str, set[str]]:
    defs = schema["$defs"]
    return {
        "store_status": set(defs["storeStatus"]["enum"]),
        "identity_status": set(defs["identityStatus"]["enum"]),
        "storage_posture": set(defs["storagePosture"]["enum"]),
        "rotation_posture": set(defs["rotationPosture"]["enum"]),
        "privacy_posture": set(defs["privacyPosture"]["enum"]),
        "evidence_builder_status": set(defs["evidenceBuilderStatus"]["enum"]),
        "enrollment_readiness": set(defs["enrollmentReadiness"]["enum"]),
        "machine_authorization_status": set(defs["machineAuthorizationStatus"]["enum"]),
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

    require("local_machine_identity" in payload, f"{name}: missing local_machine_identity", errors)
    identity = payload.get("local_machine_identity")
    require(isinstance(identity, dict), f"{name}: local_machine_identity must be an object", errors)
    if not isinstance(identity, dict):
        return

    for field in REQUIRED_STRING_FIELDS:
        value = identity.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field} must be a non-empty string", errors)

    for field in (
        "store_status",
        "identity_status",
        "storage_posture",
        "rotation_posture",
        "privacy_posture",
        "evidence_builder_status",
        "enrollment_readiness",
    ):
        value = identity.get(field)
        require(value in enums[field], f"{name}: unknown {field} {value!r}", errors)

    if "machine_authorization_status" in identity:
        value = identity["machine_authorization_status"]
        require(
            value in enums["machine_authorization_status"],
            f"{name}: unknown machine_authorization_status {value!r}",
            errors,
        )

    if "warning_codes" in identity:
        require(isinstance(identity["warning_codes"], list), f"{name}: warning_codes must be a list", errors)
        if isinstance(identity["warning_codes"], list):
            for code in identity["warning_codes"]:
                require(code in enums["warning_codes"], f"{name}: unknown warning code {code!r}", errors)

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

    print("local-machine-identity-store: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
