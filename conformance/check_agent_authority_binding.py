#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/agent-authority-binding.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures/agent-authority-binding"
EXPECTED_FIXTURES = {
    "allowed-agent-spawn.json",
    "blocked-missing-case.json",
    "blocked-agent-limit.json",
    "agent-provider-call-request.json",
    "agent-output-to-evidence.json",
}


def fail(message: str) -> None:
    print(f"agent-authority-binding: FAIL: {message}")
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

    authority_required = defs["agentAuthority"]["required"]
    roles = set(defs["agentRole"]["enum"])
    actions = set(defs["requestedAction"]["enum"])
    decisions = set(defs["decisionStatus"]["enum"])
    blocked_reasons = set(defs["blockedReason"]["enum"])
    output_postures = set(defs["agentOutputPosture"]["enum"])

    blocked_or_requires = {
        "blocked",
        "requires_auth",
        "requires_case",
        "requires_entitlement",
        "requires_machine_authorization",
        "requires_license_lease",
        "requires_runtime_gate",
        "requires_limit_capacity",
        "requires_manual_review",
    }

    for fixture_path in sorted(FIXTURE_DIR.glob("*.json")):
        fixture = require_object(load_json(fixture_path), "fixture", fixture_path)
        require_keys(fixture, ["agent_authority"], "fixture", fixture_path)
        authority = require_object(
            fixture["agent_authority"], "agent_authority", fixture_path
        )
        require_keys(authority, authority_required, "agent_authority", fixture_path)

        require_enum(authority["agent_role"], roles, "agent_role", fixture_path)
        require_enum(authority["requested_action"], actions, "requested_action", fixture_path)
        require_enum(authority["decision"], decisions, "decision", fixture_path)
        require_enum(
            authority["agent_output_posture"],
            output_postures,
            "agent_output_posture",
            fixture_path,
        )

        decision = authority["decision"]
        case_ref = authority.get("case_ref", "")
        if decision != "requires_case" and not case_ref:
            fail(f"{display_path(fixture_path)} agent_authority.case_ref is required")

        if decision in blocked_or_requires:
            if "blocked_reason" not in authority:
                fail(
                    f"{display_path(fixture_path)} blocked_reason is required for decision {decision!r}"
                )
            require_enum(
                authority["blocked_reason"],
                blocked_reasons,
                "blocked_reason",
                fixture_path,
            )
        elif "blocked_reason" in authority:
            require_enum(
                authority["blocked_reason"],
                blocked_reasons,
                "blocked_reason",
                fixture_path,
            )

        for array_field in (
            "allowed_provider_action_refs",
            "allowed_tool_action_refs",
            "output_evidence_refs",
            "output_knowledge_refs",
        ):
            if array_field in authority:
                require_string_array(authority[array_field], array_field, fixture_path)

    print("agent-authority-binding: ok")


if __name__ == "__main__":
    main()
