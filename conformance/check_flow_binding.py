#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/flow-binding.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures/flow-binding"
EXPECTED_FIXTURES = {
    "allowed-case-flow.json",
    "blocked-missing-case.json",
    "flow-with-agent-step.json",
    "flow-with-provider-step.json",
    "flow-output-to-evidence.json",
}


def fail(message: str) -> None:
    print(f"flow-binding: FAIL: {message}")
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

    binding_required = defs["flowBinding"]["required"]
    flow_kinds = set(defs["flowKind"]["enum"])
    actions = set(defs["requestedAction"]["enum"])
    decisions = set(defs["decisionStatus"]["enum"])
    blocked_reasons = set(defs["blockedReason"]["enum"])
    output_postures = set(defs["flowOutputPosture"]["enum"])

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
        require_keys(fixture, ["flow_binding"], "fixture", fixture_path)
        binding = require_object(fixture["flow_binding"], "flow_binding", fixture_path)
        require_keys(binding, binding_required, "flow_binding", fixture_path)

        require_enum(binding["flow_kind"], flow_kinds, "flow_kind", fixture_path)
        require_enum(binding["requested_action"], actions, "requested_action", fixture_path)
        require_enum(binding["decision"], decisions, "decision", fixture_path)
        require_enum(
            binding["flow_output_posture"],
            output_postures,
            "flow_output_posture",
            fixture_path,
        )

        decision = binding["decision"]
        case_ref = binding.get("case_ref", "")
        if decision != "requires_case" and not case_ref:
            fail(f"{display_path(fixture_path)} flow_binding.case_ref is required")

        if decision in blocked_or_requires:
            if "blocked_reason" not in binding:
                fail(
                    f"{display_path(fixture_path)} blocked_reason is required for decision {decision!r}"
                )
            require_enum(
                binding["blocked_reason"],
                blocked_reasons,
                "blocked_reason",
                fixture_path,
            )
        elif "blocked_reason" in binding:
            require_enum(
                binding["blocked_reason"],
                blocked_reasons,
                "blocked_reason",
                fixture_path,
            )

        for array_field in (
            "job_refs",
            "agent_instance_refs",
            "provider_call_refs",
            "execution_lease_refs",
            "evidence_refs",
            "knowledge_refs",
            "flow_step_refs",
        ):
            if array_field in binding:
                require_string_array(binding[array_field], array_field, fixture_path)

    print("flow-binding: ok")


if __name__ == "__main__":
    main()
