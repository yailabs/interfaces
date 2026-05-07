#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/knowledge-binding.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures/knowledge-binding"
EXPECTED_FIXTURES = {
    "manual-summary-knowledge.json",
    "evidence-derived-knowledge.json",
    "job-derived-knowledge.json",
    "provider-derived-knowledge.json",
    "detached-case-knowledge.json",
}


def fail(message: str) -> None:
    print(f"knowledge-binding: FAIL: {message}")
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

    knowledge_required = defs["knowledge"]["required"]
    knowledge_kinds = set(defs["knowledgeKind"]["enum"])
    visibility_values = set(defs["visibility"]["enum"])
    recall_values = set(defs["recallPolicy"]["enum"])
    write_values = set(defs["writePolicy"]["enum"])
    derivation_values = set(defs["derivationStatus"]["enum"])

    for fixture_path in sorted(FIXTURE_DIR.glob("*.json")):
        fixture = require_object(load_json(fixture_path), "fixture", fixture_path)
        require_keys(fixture, ["knowledge"], "fixture", fixture_path)
        knowledge = require_object(fixture["knowledge"], "knowledge", fixture_path)
        require_keys(knowledge, knowledge_required, "knowledge", fixture_path)

        if not knowledge.get("case_ref"):
            fail(f"{display_path(fixture_path)} knowledge.case_ref is required")

        require_enum(
            knowledge["knowledge_kind"],
            knowledge_kinds,
            "knowledge_kind",
            fixture_path,
        )
        require_enum(knowledge["visibility"], visibility_values, "visibility", fixture_path)
        require_enum(
            knowledge["recall_policy"],
            recall_values,
            "recall_policy",
            fixture_path,
        )
        require_enum(
            knowledge["write_policy"],
            write_values,
            "write_policy",
            fixture_path,
        )
        require_enum(
            knowledge["derivation_status"],
            derivation_values,
            "derivation_status",
            fixture_path,
        )

        for array_field in (
            "source_evidence_refs",
            "source_record_refs",
            "source_job_refs",
            "source_provider_call_refs",
            "source_artifact_refs",
            "lineage_refs",
        ):
            if array_field in knowledge:
                require_string_array(knowledge[array_field], array_field, fixture_path)

    print("knowledge-binding: ok")


if __name__ == "__main__":
    main()
