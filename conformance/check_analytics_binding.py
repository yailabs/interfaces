#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/analytics-binding.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures/analytics-binding"
EXPECTED_FIXTURES = {
    "case-activity-analytics.json",
    "job-completion-analytics.json",
    "flow-progress-analytics.json",
    "provider-blocked-analytics.json",
    "evidence-growth-analytics.json",
}


def fail(message: str) -> None:
    print(f"analytics-binding: FAIL: {message}")
    raise SystemExit(1)


def display_path(path: Path) -> str:
    try:
        return f"api/{path.relative_to(ROOT)}"
    except ValueError:
        return str(path)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        fail(f"{display_path(path)} is not valid JSON: {exc}")
    raise AssertionError("unreachable")


def require_object(obj: object, label: str, path: Path) -> dict:
    if not isinstance(obj, dict):
        fail(f"{display_path(path)} {label} must be an object")
    return obj


def require_keys(obj: dict, keys: list[str], label: str, path: Path) -> None:
    for key in keys:
        if key not in obj:
            fail(f"{display_path(path)} {label} missing required key: {key}")


def require_enum(value: object, allowed: set[str], field: str, path: Path) -> None:
    if value not in allowed:
        fail(f"{display_path(path)} field '{field}' has unknown value: {value!r}")


def require_string_array(value: object, field: str, path: Path) -> None:
    if not isinstance(value, list):
        fail(f"{display_path(path)} field '{field}' must be an array")
    for item in value:
        if not isinstance(item, str):
            fail(f"{display_path(path)} field '{field}' must contain only strings")


def main() -> None:
    if not SCHEMA_PATH.exists():
        fail("schema file is missing")
    if not FIXTURE_DIR.exists():
        fail("fixture directory is missing")

    schema = require_object(load_json(SCHEMA_PATH), "schema", SCHEMA_PATH)
    require_keys(schema, ["$defs", "required"], "schema", SCHEMA_PATH)
    defs = require_object(schema["$defs"], "$defs", SCHEMA_PATH)

    fixture_names = {path.name for path in FIXTURE_DIR.glob("*.json")}
    missing = EXPECTED_FIXTURES - fixture_names
    if missing:
        fail(f"missing fixtures: {', '.join(sorted(missing))}")

    binding_required = defs["analyticsBinding"]["required"]
    kinds = set(defs["analyticsKind"]["enum"])
    scopes = set(defs["analyticsScope"]["enum"])
    decisions = set(defs["decisionStatus"]["enum"])
    reasons = set(defs["blockedReason"]["enum"])
    visibility_values = set(defs["visibility"]["enum"])
    retention_values = set(defs["retentionPosture"]["enum"])

    blocked_or_special = {"blocked", "requires_case", "requires_auth", "requires_gate", "redacted"}
    case_scopes = {"case", "case_tree"}

    for fixture_path in sorted(FIXTURE_DIR.glob("*.json")):
        fixture = require_object(load_json(fixture_path), "fixture", fixture_path)
        require_keys(fixture, ["analytics_binding"], "fixture", fixture_path)
        binding = require_object(
            fixture["analytics_binding"], "analytics_binding", fixture_path
        )
        require_keys(binding, binding_required, "analytics_binding", fixture_path)

        require_enum(binding["analytics_kind"], kinds, "analytics_kind", fixture_path)
        require_enum(binding["analytics_scope"], scopes, "analytics_scope", fixture_path)
        require_enum(binding["decision"], decisions, "decision", fixture_path)
        require_enum(binding["visibility"], visibility_values, "visibility", fixture_path)
        require_enum(
            binding["retention_posture"],
            retention_values,
            "retention_posture",
            fixture_path,
        )

        scope = binding["analytics_scope"]
        case_ref = binding.get("case_ref", "")
        if scope in case_scopes and not case_ref:
            fail(
                f"{display_path(fixture_path)} analytics_binding.case_ref is required for scope {scope!r}"
            )

        if binding["decision"] in blocked_or_special:
            if "blocked_reason" not in binding:
                fail(
                    f"{display_path(fixture_path)} blocked_reason is required for decision {binding['decision']!r}"
                )
            require_enum(binding["blocked_reason"], reasons, "blocked_reason", fixture_path)
        elif "blocked_reason" in binding:
            require_enum(binding["blocked_reason"], reasons, "blocked_reason", fixture_path)

        for array_field in (
            "source_record_refs",
            "source_evidence_refs",
            "source_knowledge_refs",
            "source_job_refs",
            "source_flow_refs",
            "source_agent_instance_refs",
            "source_provider_call_refs",
            "runtime_gate_decision_refs",
            "license_lease_refs",
            "machine_authorization_refs",
            "limit_projection_refs",
            "derived_from_refs",
        ):
            if array_field in binding:
                require_string_array(binding[array_field], array_field, fixture_path)

    print("analytics-binding: ok")


if __name__ == "__main__":
    main()
