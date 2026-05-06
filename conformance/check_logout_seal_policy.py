#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/logout-seal-policy.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures/logout-seal-policy"
EXPECTED_FIXTURES = {
    "no-active-work.json",
    "active-case-no-job.json",
    "active-job-with-lease.json",
    "expired-license-lease.json",
    "force-request-requires-confirmation.json",
}


def fail(message: str) -> None:
    print(f"logout-seal-policy: FAIL: {message}")
    raise SystemExit(1)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        fail(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
    raise AssertionError("unreachable")


def require_keys(obj: object, keys: list[str], label: str, path: Path) -> dict:
    if not isinstance(obj, dict):
        fail(f"{path.relative_to(ROOT)} {label} must be an object")
    for key in keys:
        if key not in obj:
            fail(f"{path.relative_to(ROOT)} {label} missing required key: {key}")
    return obj


def require_string_array(value: object, field: str, path: Path) -> None:
    if not isinstance(value, list):
        fail(f"{path.relative_to(ROOT)} field '{field}' must be an array")
    for item in value:
        if not isinstance(item, str):
            fail(f"{path.relative_to(ROOT)} field '{field}' must contain only strings")


def require_enum(value: object, allowed: set[str], field: str, path: Path) -> None:
    if value not in allowed:
        fail(
            f"{path.relative_to(ROOT)} field '{field}' has unknown value: {value!r}"
        )


def main() -> None:
    if not SCHEMA_PATH.exists():
        fail("schema file is missing")
    if not FIXTURE_DIR.exists():
        fail("fixture directory is missing")

    schema = load_json(SCHEMA_PATH)
    schema_obj = require_keys(schema, ["$defs", "required"], "schema", SCHEMA_PATH)
    defs = require_keys(schema_obj["$defs"], [], "$defs", SCHEMA_PATH)

    fixture_names = {path.name for path in FIXTURE_DIR.glob("*.json")}
    missing_fixtures = EXPECTED_FIXTURES - fixture_names
    if missing_fixtures:
        fail(f"missing fixtures: {', '.join(sorted(missing_fixtures))}")

    request_required = defs["logoutRequest"]["required"]
    decision_required = defs["logoutPolicyDecision"]["required"]

    requested_modes = set(defs["requestedMode"]["enum"])
    decision_statuses = set(defs["decisionStatus"]["enum"])
    safe_reasons = set(defs["safeReason"]["enum"])
    auth_actions = set(defs["authContextAction"]["enum"])
    license_actions = set(defs["licenseLeaseAction"]["enum"])
    runtime_actions = set(defs["runtimeSealAction"]["enum"])
    records_actions = set(defs["recordsEvidenceAction"]["enum"])
    knowledge_actions = set(defs["knowledgeAction"]["enum"])

    for fixture_path in sorted(FIXTURE_DIR.glob("*.json")):
        fixture = load_json(fixture_path)
        fixture_obj = require_keys(
            fixture,
            ["logout_request", "logout_policy_decision"],
            "fixture",
            fixture_path,
        )
        request = require_keys(
            fixture_obj["logout_request"],
            request_required,
            "logout_request",
            fixture_path,
        )
        decision = require_keys(
            fixture_obj["logout_policy_decision"],
            decision_required,
            "logout_policy_decision",
            fixture_path,
        )

        require_enum(request["requested_mode"], requested_modes, "requested_mode", fixture_path)
        require_enum(decision["decision"], decision_statuses, "decision", fixture_path)
        require_enum(decision["reason"], safe_reasons, "reason", fixture_path)
        require_enum(
            decision["auth_context_action"],
            auth_actions,
            "auth_context_action",
            fixture_path,
        )
        require_enum(
            decision["license_lease_action"],
            license_actions,
            "license_lease_action",
            fixture_path,
        )
        require_enum(
            decision["runtime_seal_action"],
            runtime_actions,
            "runtime_seal_action",
            fixture_path,
        )
        require_enum(
            decision["records_evidence_action"],
            records_actions,
            "records_evidence_action",
            fixture_path,
        )
        require_enum(
            decision["knowledge_action"],
            knowledge_actions,
            "knowledge_action",
            fixture_path,
        )

        for array_field in (
            "observed_job_refs",
            "observed_execution_lease_refs",
        ):
            if array_field in request:
                require_string_array(request[array_field], array_field, fixture_path)

        for array_field in (
            "next_actions",
            "affected_case_refs",
            "affected_job_refs",
            "affected_execution_lease_refs",
        ):
            require_string_array(decision[array_field], array_field, fixture_path)

        if request["logout_request_ref"] != decision["logout_request_ref"]:
            fail(
                f"{fixture_path.relative_to(ROOT)} logout_request_ref mismatch between request and decision"
            )

    print("logout-seal-policy: ok")


if __name__ == "__main__":
    main()
