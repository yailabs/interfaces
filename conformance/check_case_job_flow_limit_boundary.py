#!/usr/bin/env python3
"""Dependency-free checks for the V36 case/job/flow limit boundary fixtures."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "case-job-flow-limit-boundary.v1.schema.json"
FIXTURES_DIR = ROOT / "fixtures" / "case-job-flow-limit-boundary"

EXPECTED_FIXTURES = {
    "case-limit-allowed.json",
    "job-limit-blocked.json",
    "flow-limit-warning.json",
    "agent-limit-blocked.json",
    "provider-call-limit-metering-sensitive.json",
    "account-global-limit-shared-across-machines.json",
}

LIMIT_FAMILIES = {
    "case",
    "job",
    "flow",
    "agent",
    "provider_call",
    "knowledge",
    "evidence",
    "runtime_action",
    "machine",
    "release_update",
    "cloud_compute",
    "admin",
}

LIMIT_SCOPES = {
    "account_global",
    "principal",
    "machine",
    "case_tree",
    "case",
    "runtime_instance",
    "team",
    "organization",
    "system_internal",
}

LIMIT_KEYS = {
    "max_open_cases",
    "max_active_cases",
    "max_nested_cases",
    "max_parallel_jobs",
    "max_active_flows",
    "max_concurrent_agents",
    "max_provider_calls",
    "max_knowledge_writes",
    "max_evidence_writes",
    "max_authorized_machines",
    "max_runtime_actions",
    "max_release_downloads",
    "cloud_compute_minutes",
}

WINDOWS = {
    "none",
    "minute",
    "hour",
    "day",
    "week",
    "month",
    "billing_period",
    "lease_period",
    "release_period",
    "custom",
}

DECISIONS = {
    "allowed",
    "warning",
    "blocked",
    "requires_entitlement",
    "requires_license_lease",
    "requires_machine_authorization",
    "requires_limit_projection",
    "requires_manual_review",
    "unknown",
}

BLOCKED_REASONS = {
    "limit_exceeded",
    "quota_exhausted",
    "missing_limit_projection",
    "missing_entitlement",
    "license_lease_expired",
    "machine_not_authorized",
    "manual_review_required",
    "plan_package_unavailable",
    "billing_required_but_unavailable",
    "unknown",
}

REQUIRED_FIELDS = {
    "limit_projection_ref",
    "limit_key",
    "limit_family",
    "scope",
    "subject_ref",
    "window",
    "decision",
    "observed_at",
}

NUMERIC_FIELDS = {
    "current_usage",
    "max_allowed",
    "remaining",
    "soft_limit",
    "hard_limit",
    "warning_threshold",
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


def require_number(value: object, field_name: str, fixture_path: Path) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        fail(f"{fixture_path}: {field_name} must be numeric")


def validate_fixture(fixture_path: Path) -> None:
    payload = load_json(fixture_path)
    if not isinstance(payload, dict):
        fail(f"{fixture_path}: top-level value must be an object")
    if "limit_projection" not in payload:
        fail(f"{fixture_path}: missing top-level limit_projection")

    projection = payload["limit_projection"]
    if not isinstance(projection, dict):
        fail(f"{fixture_path}: limit_projection must be an object")

    missing = sorted(REQUIRED_FIELDS - projection.keys())
    if missing:
        fail(f"{fixture_path}: missing required fields: {', '.join(missing)}")

    require_enum(projection["limit_family"], LIMIT_FAMILIES, "limit_family", fixture_path)
    require_enum(projection["scope"], LIMIT_SCOPES, "scope", fixture_path)
    require_enum(projection["limit_key"], LIMIT_KEYS, "limit_key", fixture_path)
    require_enum(projection["window"], WINDOWS, "window", fixture_path)
    require_enum(projection["decision"], DECISIONS, "decision", fixture_path)

    for field_name in NUMERIC_FIELDS:
        if field_name in projection:
            require_number(projection[field_name], field_name, fixture_path)

    if not isinstance(projection["limit_projection_ref"], str) or not projection["limit_projection_ref"]:
        fail(f"{fixture_path}: limit_projection_ref must be a non-empty string")
    if not isinstance(projection["subject_ref"], str) or not projection["subject_ref"]:
        fail(f"{fixture_path}: subject_ref must be a non-empty string")
    if not isinstance(projection["observed_at"], str) or not projection["observed_at"]:
        fail(f"{fixture_path}: observed_at must be a non-empty string")

    if projection["decision"] == "blocked" and "blocked_reason" not in projection:
        fail(f"{fixture_path}: blocked decisions require blocked_reason")

    if "blocked_reason" in projection:
        require_enum(projection["blocked_reason"], BLOCKED_REASONS, "blocked_reason", fixture_path)

    if projection["decision"] == "warning":
        if "warning_threshold" not in projection and "soft_limit" not in projection:
            fail(f"{fixture_path}: warning decisions require warning_threshold or soft_limit")

    if fixture_path.name == "account-global-limit-shared-across-machines.json":
        if projection["scope"] != "account_global":
            fail(f"{fixture_path}: shared account fixture must use scope account_global")


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

    print("case-job-flow-limit-boundary: ok")


if __name__ == "__main__":
    main()
