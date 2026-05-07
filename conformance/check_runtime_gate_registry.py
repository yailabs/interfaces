#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/runtime-gate-registry.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures/runtime-gate-registry"
EXPECTED_FIXTURES = {
    "diagnostic-runtime-status.json",
    "case-open-requires-auth.json",
    "job-start-requires-case-and-gate.json",
    "provider-call-requires-entitlement.json",
    "agent-spawn-requires-limit.json",
    "knowledge-write-requires-case.json",
}


def fail(message: str) -> None:
    print(f"runtime-gate-registry: FAIL: {message}")
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


def require_enum_array(value: object, allowed: set[str], field: str, path: Path) -> None:
    if not isinstance(value, list):
        fail(f"{display_path(path)} field '{field}' must be an array")
    for item in value:
        require_enum(item, allowed, field, path)


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

    action_required = defs["runtimeAction"]["required"]
    families = set(defs["runtimeActionFamily"]["enum"])
    categories = set(defs["actionCategory"]["enum"])
    gate_classes = set(defs["gateClassification"]["enum"])
    contexts = set(defs["requiredContext"]["enum"])
    refs = set(defs["requiredRef"]["enum"])
    decisions = set(defs["decisionStatus"]["enum"])
    blocked_reasons = set(defs["blockedReason"]["enum"])

    operational_categories = {
        "case_write",
        "operational",
        "execution",
        "provider_action",
        "agent_action",
        "flow_action",
        "evidence_write",
        "knowledge_write",
        "runtime_control",
        "release_update",
        "admin_control",
    }

    boolean_fields = (
        "allowed_during_sealed",
        "limit_sensitive",
        "metering_sensitive",
        "cloud_sensitive",
        "writes_state",
        "writes_evidence",
        "writes_knowledge",
        "controls_runtime",
    )

    for fixture_path in sorted(FIXTURE_DIR.glob("*.json")):
        fixture = require_object(load_json(fixture_path), "fixture", fixture_path)
        require_keys(fixture, ["runtime_gate_registry"], "fixture", fixture_path)
        registry = require_object(
            fixture["runtime_gate_registry"], "runtime_gate_registry", fixture_path
        )
        require_keys(
            registry,
            ["registry_version", "runtime_actions"],
            "runtime_gate_registry",
            fixture_path,
        )

        runtime_actions = registry["runtime_actions"]
        if not isinstance(runtime_actions, list) or not runtime_actions:
            fail(f"{display_path(fixture_path)} runtime_actions must be a non-empty array")

        for action in runtime_actions:
            if not isinstance(action, dict):
                fail(f"{display_path(fixture_path)} runtime_actions entries must be objects")
            require_keys(action, action_required, "runtime_action", fixture_path)

            require_enum(action["runtime_action_family"], families, "runtime_action_family", fixture_path)
            require_enum(action["action_category"], categories, "action_category", fixture_path)
            require_enum(action["gate_classification"], gate_classes, "gate_classification", fixture_path)

            if "required_context" in action:
                require_enum_array(action["required_context"], contexts, "required_context", fixture_path)
            if "required_refs" in action:
                require_enum_array(action["required_refs"], refs, "required_refs", fixture_path)
            if "required_postures" in action:
                require_string_array(action["required_postures"], "required_postures", fixture_path)
            if "blocked_reasons" in action:
                require_enum_array(action["blocked_reasons"], blocked_reasons, "blocked_reasons", fixture_path)

            require_enum_array(action["decision_outputs"], decisions, "decision_outputs", fixture_path)

            for field in boolean_fields:
                if not isinstance(action[field], bool):
                    fail(f"{display_path(fixture_path)} field '{field}' must be boolean")

            if action["gate_classification"] == "ungated_diagnostic":
                if not action["allowed_during_sealed"]:
                    fail(f"{display_path(fixture_path)} ungated_diagnostic actions must be allowed during sealed")
                if action["action_category"] != "diagnostic_read":
                    fail(f"{display_path(fixture_path)} ungated_diagnostic actions must use action_category 'diagnostic_read'")
                if action["writes_state"] or action["writes_evidence"] or action["writes_knowledge"] or action["controls_runtime"]:
                    fail(f"{display_path(fixture_path)} ungated_diagnostic actions must not mutate or control runtime")

            if action["action_category"] in operational_categories and action["gate_classification"] == "ungated_diagnostic":
                fail(f"{display_path(fixture_path)} operational/write actions must not be ungated_diagnostic")

    print("runtime-gate-registry: ok")


if __name__ == "__main__":
    main()
