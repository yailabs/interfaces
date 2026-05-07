#!/usr/bin/env python3
"""Dependency-free conformance checks for V40 machine fingerprint evidence builder."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "machine-fingerprint-evidence-builder.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "machine-fingerprint-evidence-builder"

EXPECTED_FIXTURES = {
    "minimized-local-evidence.json",
    "enrollment-ready-evidence.json",
    "consent-required-evidence.json",
    "rotated-identity-evidence.json",
    "raw-hardware-rejected-evidence.json",
    "low-confidence-evidence.json",
}

REQUIRED_STRING_FIELDS = (
    "machine_fingerprint_evidence_ref",
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
        "evidence_kind": set(defs["evidenceKind"]["enum"]),
        "evidence_status": set(defs["evidenceStatus"]["enum"]),
        "evidence_source_policy": set(defs["evidenceSourcePolicy"]["enum"]),
        "privacy_posture": set(defs["privacyPosture"]["enum"]),
        "minimization_posture": set(defs["minimizationPosture"]["enum"]),
        "consent_posture": set(defs["consentPosture"]["enum"]),
        "confidence_posture": set(defs["confidencePosture"]["enum"]),
        "rotation_posture": set(defs["rotationPosture"]["enum"]),
        "enrollment_use": set(defs["enrollmentUse"]["enum"]),
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

    require(
        "machine_fingerprint_evidence" in payload,
        f"{name}: missing machine_fingerprint_evidence",
        errors,
    )
    evidence = payload.get("machine_fingerprint_evidence")
    require(isinstance(evidence, dict), f"{name}: machine_fingerprint_evidence must be an object", errors)
    if not isinstance(evidence, dict):
        return

    for field in REQUIRED_STRING_FIELDS:
        value = evidence.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field} must be a non-empty string", errors)

    for field in (
        "evidence_kind",
        "evidence_status",
        "evidence_source_policy",
        "privacy_posture",
        "minimization_posture",
        "consent_posture",
        "confidence_posture",
        "rotation_posture",
        "enrollment_use",
    ):
        value = evidence.get(field)
        require(value in enums[field], f"{name}: unknown {field} {value!r}", errors)

    if "machine_authorization_status" in evidence:
        value = evidence["machine_authorization_status"]
        require(
            value in enums["machine_authorization_status"],
            f"{name}: unknown machine_authorization_status {value!r}",
            errors,
        )

    if "warning_codes" in evidence:
        require(isinstance(evidence["warning_codes"], list), f"{name}: warning_codes must be a list", errors)
        if isinstance(evidence["warning_codes"], list):
            for code in evidence["warning_codes"]:
                require(code in enums["warning_codes"], f"{name}: unknown warning code {code!r}", errors)

    walk_keys(payload, errors)

    if name == "raw-hardware-rejected-evidence.json":
        require(
            evidence.get("privacy_posture") in {"blocked", "raw_hardware_forbidden", "requires_review"},
            f"{name}: raw hardware rejection must carry blocked/review privacy posture",
            errors,
        )
        require(
            evidence.get("evidence_status") in {"blocked", "requires_privacy_review"},
            f"{name}: raw hardware rejection must not look like built safe evidence",
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

    print("machine-fingerprint-evidence-builder: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
