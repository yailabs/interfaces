#!/usr/bin/env python3
"""Dependency-free checks for the V37 local model/provider access boundary."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "local-model-provider-access-boundary.v1.schema.json"
FIXTURES_DIR = ROOT / "fixtures" / "local-model-provider-access-boundary"

EXPECTED_FIXTURES = {
    "local-model-allowed.json",
    "provider-blocked-missing-entitlement.json",
    "provider-blocked-budget.json",
    "hosted-model-requires-cloud-gate.json",
    "custom-model-not-implemented.json",
    "user-owned-provider-credentials-boundary.json",
}

ACCESS_TARGETS = {
    "local_model",
    "external_provider",
    "hosted_model",
    "custom_model",
    "fine_tuned_model",
    "provider_status",
    "model_status",
}

ACCESS_MODES = {
    "local_runtime",
    "user_owned_provider",
    "platform_managed_provider",
    "hosted_platform",
    "offline_cached",
    "diagnostic_status",
}

REQUESTED_ACTIONS = {
    "inspect_status",
    "load_local_model",
    "invoke_local_model",
    "invoke_external_provider",
    "invoke_hosted_model",
    "invoke_custom_model",
    "embed",
    "rerank",
    "summarize",
    "classify",
    "extract",
    "tool_call",
}

DECISIONS = {
    "allowed",
    "blocked",
    "degraded",
    "diagnostic_allowed",
    "requires_auth",
    "requires_case",
    "requires_entitlement",
    "requires_machine_authorization",
    "requires_license_lease",
    "requires_runtime_gate",
    "requires_limit_capacity",
    "requires_provider_budget",
    "requires_credentials",
    "requires_manual_review",
    "not_implemented",
    "unknown",
}

BLOCKED_REASONS = {
    "missing_auth_context",
    "missing_case_ref",
    "missing_entitlement",
    "machine_not_authorized",
    "license_lease_expired",
    "runtime_gate_blocked",
    "limit_exceeded",
    "provider_budget_exceeded",
    "provider_not_configured",
    "credentials_missing",
    "credentials_forbidden",
    "model_not_available",
    "model_not_allowed",
    "hosted_model_not_enabled",
    "custom_model_not_implemented",
    "cloud_capacity_unavailable",
    "manual_review_required",
    "unsafe_request",
    "unknown",
}

OUTPUT_POSTURES = {
    "no_output",
    "output_not_persisted",
    "output_as_evidence_candidate",
    "output_as_knowledge_candidate",
    "output_redacted",
    "output_blocked",
    "diagnostic_only",
}

CREDENTIAL_BOUNDARIES = {
    "no_credentials_required",
    "user_owned_credentials_required",
    "platform_managed_credentials_required",
    "credentials_present_but_not_exposed",
    "credentials_missing",
    "credentials_forbidden",
    "not_applicable",
}

REQUIRED_FIELDS = {
    "model_access_decision_ref",
    "access_target",
    "access_mode",
    "requested_action",
    "requested_at",
    "decision",
    "reason",
    "output_posture",
    "credential_boundary",
}

CASE_SCOPED_ACTIONS = {
    "load_local_model",
    "invoke_local_model",
    "invoke_external_provider",
    "invoke_hosted_model",
    "invoke_custom_model",
    "embed",
    "rerank",
    "summarize",
    "classify",
    "extract",
    "tool_call",
}

REQUIRES_REASON_DECISIONS = {
    "blocked",
    "requires_auth",
    "requires_case",
    "requires_entitlement",
    "requires_machine_authorization",
    "requires_license_lease",
    "requires_runtime_gate",
    "requires_limit_capacity",
    "requires_provider_budget",
    "requires_credentials",
    "requires_manual_review",
    "not_implemented",
}

SECRET_FIELD_TOKENS = {"api_key", "token", "secret", "password"}


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> object:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        fail(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid json in {path}: {exc}")


def require_enum(value: object, allowed: set[str], field_name: str, fixture_path: Path) -> None:
    if value not in allowed:
        fail(f"{fixture_path}: invalid {field_name}: {value!r}")


def ensure_no_secret_fields(node: object, fixture_path: Path) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            lowered = key.lower()
            if lowered in SECRET_FIELD_TOKENS:
                fail(f"{fixture_path}: forbidden secret field {key!r}")
            ensure_no_secret_fields(value, fixture_path)
    elif isinstance(node, list):
        for value in node:
            ensure_no_secret_fields(value, fixture_path)


def validate_fixture(fixture_path: Path) -> None:
    payload = load_json(fixture_path)
    ensure_no_secret_fields(payload, fixture_path)

    if not isinstance(payload, dict):
        fail(f"{fixture_path}: top-level value must be an object")
    if "model_access_decision" not in payload:
        fail(f"{fixture_path}: missing top-level model_access_decision")

    decision_obj = payload["model_access_decision"]
    if not isinstance(decision_obj, dict):
        fail(f"{fixture_path}: model_access_decision must be an object")

    missing = sorted(REQUIRED_FIELDS - decision_obj.keys())
    if missing:
        fail(f"{fixture_path}: missing required fields: {', '.join(missing)}")

    require_enum(decision_obj["access_target"], ACCESS_TARGETS, "access_target", fixture_path)
    require_enum(decision_obj["access_mode"], ACCESS_MODES, "access_mode", fixture_path)
    require_enum(decision_obj["requested_action"], REQUESTED_ACTIONS, "requested_action", fixture_path)
    require_enum(decision_obj["decision"], DECISIONS, "decision", fixture_path)
    require_enum(decision_obj["output_posture"], OUTPUT_POSTURES, "output_posture", fixture_path)
    require_enum(
        decision_obj["credential_boundary"],
        CREDENTIAL_BOUNDARIES,
        "credential_boundary",
        fixture_path,
    )

    if "blocked_reason" in decision_obj:
        require_enum(decision_obj["blocked_reason"], BLOCKED_REASONS, "blocked_reason", fixture_path)

    if not isinstance(decision_obj["model_access_decision_ref"], str) or not decision_obj["model_access_decision_ref"]:
        fail(f"{fixture_path}: model_access_decision_ref must be a non-empty string")
    if not isinstance(decision_obj["requested_at"], str) or not decision_obj["requested_at"]:
        fail(f"{fixture_path}: requested_at must be a non-empty string")
    if not isinstance(decision_obj["reason"], str) or not decision_obj["reason"]:
        fail(f"{fixture_path}: reason must be a non-empty string")

    if decision_obj["requested_action"] in CASE_SCOPED_ACTIONS and decision_obj["decision"] != "requires_case":
        case_ref = decision_obj.get("case_ref")
        if not isinstance(case_ref, str) or not case_ref:
            fail(f"{fixture_path}: case-scoped operational access requires non-empty case_ref")

    if decision_obj["decision"] in REQUIRES_REASON_DECISIONS and "blocked_reason" not in decision_obj:
        fail(f"{fixture_path}: {decision_obj['decision']} decisions require blocked_reason")


def main() -> None:
    if not SCHEMA_PATH.is_file():
        fail(f"missing schema: {SCHEMA_PATH}")
    load_json(SCHEMA_PATH)

    if not FIXTURES_DIR.is_dir():
        fail(f"missing fixtures directory: {FIXTURES_DIR}")

    fixture_paths = sorted(FIXTURES_DIR.glob("*.json"))
    fixture_names = {path.name for path in fixture_paths}
    missing = sorted(EXPECTED_FIXTURES - fixture_names)
    if missing:
        fail(f"missing fixtures: {', '.join(missing)}")

    for fixture_path in fixture_paths:
        validate_fixture(fixture_path)

    print("local-model-provider-access-boundary: ok")


if __name__ == "__main__":
    main()
