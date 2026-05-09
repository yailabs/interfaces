#!/usr/bin/env python3
"""Dependency-free conformance checks for V50 logout/revocation/lease invalidation."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "logout-revocation-lease-invalidation.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "logout-revocation-lease-invalidation"

EXPECTED_FIXTURES = {
    "logout-seals-operational.json",
    "machine-revoked-seals-runtime.json",
    "lease-revoked-invalidates-cache.json",
    "lease-expired-diagnostics-only.json",
    "case-evidence-knowledge-preserved.json",
    "safe-invalidation-projection.json",
}

REQUIRED_STRING_FIELDS = ("runtime_invalidation_event_ref",)

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

DESTRUCTIVE_KEYS = {
    "delete_case",
    "delete_evidence",
    "delete_knowledge",
    "delete_records",
    "purge_case_tree",
}

SAFE_PROJECTION_KEYS = {
    "invalidation_kind",
    "invalidation_reason",
    "seal_state",
    "operational_readiness",
    "diagnostic_posture",
    "cache_invalidation_posture",
    "lease_invalidation_posture",
    "machine_authorization_posture",
    "logout_posture",
    "preservation_posture",
    "recovery_posture",
    "next_action",
    "warning_codes",
}


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_enums(schema: dict) -> dict[str, set[str]]:
    defs = schema["$defs"]
    return {
        "invalidation_kind": set(defs["invalidationKind"]["enum"]),
        "invalidation_reason": set(defs["invalidationReason"]["enum"]),
        "seal_state": set(defs["sealState"]["enum"]),
        "operational_readiness": set(defs["operationalReadiness"]["enum"]),
        "diagnostic_posture": set(defs["diagnosticPosture"]["enum"]),
        "cache_invalidation_posture": set(defs["cacheInvalidationPosture"]["enum"]),
        "lease_invalidation_posture": set(defs["leaseInvalidationPosture"]["enum"]),
        "machine_authorization_posture": set(defs["machineAuthorizationPosture"]["enum"]),
        "logout_posture": set(defs["logoutPosture"]["enum"]),
        "preservation_posture": set(defs["preservationPosture"]["enum"]),
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
            if key in DESTRUCTIVE_KEYS:
                errors.append(f"{path}.{key}: forbidden destructive implementation field")
            walk_keys(value, errors, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            walk_keys(value, errors, f"{path}[{index}]")


def validate_warning_codes(name: str, value: object, enums: dict[str, set[str]], field_name: str, errors: list[str]) -> None:
    require(isinstance(value, list), f"{name}: {field_name} must be a list", errors)
    if isinstance(value, list):
        for code in value:
            require(code in enums["warning_codes"], f"{name}: unknown warning code {code!r}", errors)


def validate_safe_projection(name: str, projection: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(projection, dict), f"{name}: safe_invalidation_projection must be an object", errors)
    if not isinstance(projection, dict):
        return

    extra = set(projection.keys()) - SAFE_PROJECTION_KEYS
    require(not extra, f"{name}: safe_invalidation_projection has unsafe keys {sorted(extra)}", errors)

    for field in (
        "invalidation_kind",
        "invalidation_reason",
        "seal_state",
        "operational_readiness",
        "diagnostic_posture",
        "cache_invalidation_posture",
        "lease_invalidation_posture",
        "machine_authorization_posture",
        "logout_posture",
        "preservation_posture",
        "recovery_posture",
        "next_action",
    ):
        value = projection.get(field)
        require(value in enums[field], f"{name}: unknown safe_invalidation_projection {field} {value!r}", errors)

    if "warning_codes" in projection:
        validate_warning_codes(name, projection["warning_codes"], enums, "safe_invalidation_projection.warning_codes", errors)


def validate_fixture(name: str, payload: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(payload, dict), f"{name}: top-level JSON must be an object", errors)
    if not isinstance(payload, dict):
        return

    require("runtime_invalidation_event" in payload, f"{name}: missing runtime_invalidation_event", errors)
    event = payload.get("runtime_invalidation_event")
    require(isinstance(event, dict), f"{name}: runtime_invalidation_event must be an object", errors)
    if not isinstance(event, dict):
        return

    for field in REQUIRED_STRING_FIELDS:
        value = event.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field} must be a non-empty string", errors)

    require(isinstance(event.get("affected_refs"), list), f"{name}: affected_refs must be an array", errors)
    if isinstance(event.get("affected_refs"), list):
        for item in event["affected_refs"]:
            require(isinstance(item, str) and item.strip(), f"{name}: affected_refs items must be non-empty strings", errors)

    for field in (
        "invalidation_kind",
        "invalidation_reason",
        "seal_state",
        "operational_readiness",
        "diagnostic_posture",
        "cache_invalidation_posture",
        "lease_invalidation_posture",
        "machine_authorization_posture",
        "logout_posture",
        "preservation_posture",
        "recovery_posture",
        "next_action",
    ):
        value = event.get(field)
        require(value in enums[field], f"{name}: unknown {field} {value!r}", errors)

    if "warning_codes" in event:
        validate_warning_codes(name, event["warning_codes"], enums, "warning_codes", errors)

    if "safe_invalidation_projection" in event:
        validate_safe_projection(name, event["safe_invalidation_projection"], enums, errors)

    if name in {"logout-seals-operational.json", "machine-revoked-seals-runtime.json", "lease-revoked-invalidates-cache.json", "lease-expired-diagnostics-only.json"}:
        require(
            event.get("operational_readiness") != "ready",
            f"{name}: sealed/diagnostics-only fixture must not mark operational_readiness ready",
            errors,
        )

    if name == "case-evidence-knowledge-preserved.json":
        require(
            event.get("preservation_posture") == "preserve_cases_records_evidence_knowledge",
            f"{name}: preservation fixture must preserve cases/records/evidence/knowledge",
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

    print("logout-revocation-lease-invalidation: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
