#!/usr/bin/env python3
"""Dependency-free checks for the V38 cloud compute boundary."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "cloud-compute-boundary.v1.schema.json"
FIXTURES_DIR = ROOT / "fixtures" / "cloud-compute-boundary"

EXPECTED_FIXTURES = {
    "local-runtime-not-cloud.json",
    "cloud-compute-blocked-missing-entitlement.json",
    "cloud-compute-blocked-capacity.json",
    "priority-queue-required.json",
    "dedicated-capacity-not-implemented.json",
    "managed-remote-job-deferred.json",
}

COMPUTE_TARGETS = {
    "local_runtime",
    "local_model",
    "external_provider",
    "hosted_model",
    "cloud_job",
    "managed_remote_job",
    "priority_queue",
    "dedicated_capacity",
    "cloud_artifact_build",
    "cloud_evaluation",
}

COMPUTE_MODES = {
    "local_only",
    "cloud_optional",
    "cloud_required",
    "hosted_platform",
    "managed_execution",
    "diagnostic_status",
    "not_applicable",
}

REQUESTED_ACTIONS = {
    "inspect_status",
    "request_cloud_capacity",
    "submit_remote_job",
    "resume_remote_job",
    "cancel_remote_job",
    "invoke_hosted_model",
    "run_cloud_evaluation",
    "build_cloud_artifact",
    "enter_priority_queue",
    "use_dedicated_capacity",
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
    "requires_cloud_capacity",
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
    "cloud_compute_not_enabled",
    "cloud_capacity_unavailable",
    "priority_queue_required",
    "dedicated_capacity_required",
    "hosted_model_not_enabled",
    "managed_execution_not_available",
    "region_not_available",
    "billing_required_but_unavailable",
    "manual_review_required",
    "unsafe_request",
    "unknown",
}

OUTPUT_POSTURES = {
    "no_output",
    "output_not_persisted",
    "output_as_evidence_candidate",
    "output_as_knowledge_candidate",
    "cloud_artifact_ref_only",
    "output_redacted",
    "output_blocked",
    "diagnostic_only",
}

INFRASTRUCTURE_BOUNDARIES = {
    "no_cloud_infrastructure",
    "platform_managed_infrastructure",
    "customer_managed_infrastructure",
    "hybrid_local_cloud",
    "infrastructure_not_exposed_to_v",
    "not_applicable",
}

REQUIRED_FIELDS = {
    "cloud_compute_decision_ref",
    "compute_target",
    "compute_mode",
    "requested_action",
    "requested_at",
    "decision",
    "reason",
    "output_posture",
    "infrastructure_boundary",
}

CASE_SCOPED_ACTIONS = {
    "request_cloud_capacity",
    "submit_remote_job",
    "resume_remote_job",
    "cancel_remote_job",
    "invoke_hosted_model",
    "run_cloud_evaluation",
    "build_cloud_artifact",
    "enter_priority_queue",
    "use_dedicated_capacity",
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
    "requires_cloud_capacity",
    "requires_manual_review",
    "not_implemented",
}

SECRET_FIELD_TOKENS = {
    "api_key",
    "token",
    "secret",
    "password",
    "cloud_secret",
    "provider_secret",
}


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
            if key.lower() in SECRET_FIELD_TOKENS:
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
    if "cloud_compute_decision" not in payload:
        fail(f"{fixture_path}: missing top-level cloud_compute_decision")

    decision_obj = payload["cloud_compute_decision"]
    if not isinstance(decision_obj, dict):
        fail(f"{fixture_path}: cloud_compute_decision must be an object")

    missing = sorted(REQUIRED_FIELDS - decision_obj.keys())
    if missing:
        fail(f"{fixture_path}: missing required fields: {', '.join(missing)}")

    require_enum(decision_obj["compute_target"], COMPUTE_TARGETS, "compute_target", fixture_path)
    require_enum(decision_obj["compute_mode"], COMPUTE_MODES, "compute_mode", fixture_path)
    require_enum(decision_obj["requested_action"], REQUESTED_ACTIONS, "requested_action", fixture_path)
    require_enum(decision_obj["decision"], DECISIONS, "decision", fixture_path)
    require_enum(decision_obj["output_posture"], OUTPUT_POSTURES, "output_posture", fixture_path)
    require_enum(
        decision_obj["infrastructure_boundary"],
        INFRASTRUCTURE_BOUNDARIES,
        "infrastructure_boundary",
        fixture_path,
    )

    if "blocked_reason" in decision_obj:
        require_enum(decision_obj["blocked_reason"], BLOCKED_REASONS, "blocked_reason", fixture_path)

    if not isinstance(decision_obj["cloud_compute_decision_ref"], str) or not decision_obj["cloud_compute_decision_ref"]:
        fail(f"{fixture_path}: cloud_compute_decision_ref must be a non-empty string")
    if not isinstance(decision_obj["requested_at"], str) or not decision_obj["requested_at"]:
        fail(f"{fixture_path}: requested_at must be a non-empty string")
    if not isinstance(decision_obj["reason"], str) or not decision_obj["reason"]:
        fail(f"{fixture_path}: reason must be a non-empty string")

    if decision_obj["requested_action"] in CASE_SCOPED_ACTIONS and decision_obj["decision"] != "requires_case":
        case_ref = decision_obj.get("case_ref")
        if not isinstance(case_ref, str) or not case_ref:
            fail(f"{fixture_path}: case-scoped cloud access requires non-empty case_ref")

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

    print("cloud-compute-boundary: ok")


if __name__ == "__main__":
    main()
