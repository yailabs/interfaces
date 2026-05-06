#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/case-evidence-binding.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures/case-evidence-binding"
EXPECTED_FIXTURES = {
    "manual-note-evidence.json",
    "job-output-evidence.json",
    "provider-call-evidence.json",
    "gate-decision-evidence.json",
    "detached-job-evidence.json",
}


def fail(message: str) -> None:
    print(f"case-evidence-binding: FAIL: {message}")
    raise SystemExit(1)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        fail(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
    raise AssertionError("unreachable")


def require_object(obj: object, label: str, path: Path) -> dict:
    if not isinstance(obj, dict):
        fail(f"{path.relative_to(ROOT)} {label} must be an object")
    return obj


def require_keys(obj: dict, keys: list[str], label: str, path: Path) -> None:
    for key in keys:
        if key not in obj:
            fail(f"{path.relative_to(ROOT)} {label} missing required key: {key}")


def require_enum(value: object, allowed: set[str], field: str, path: Path) -> None:
    if value not in allowed:
        fail(f"{path.relative_to(ROOT)} field '{field}' has unknown value: {value!r}")


def require_string_array(value: object, field: str, path: Path) -> None:
    if not isinstance(value, list):
        fail(f"{path.relative_to(ROOT)} field '{field}' must be an array")
    for item in value:
        if not isinstance(item, str):
            fail(f"{path.relative_to(ROOT)} field '{field}' must contain only strings")


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

    evidence_required = defs["evidence"]["required"]
    evidence_kinds = set(defs["evidenceKind"]["enum"])
    visibility_values = set(defs["visibility"]["enum"])
    retention_values = set(defs["retentionPosture"]["enum"])

    for fixture_path in sorted(FIXTURE_DIR.glob("*.json")):
        fixture = require_object(load_json(fixture_path), "fixture", fixture_path)
        require_keys(fixture, ["evidence"], "fixture", fixture_path)
        evidence = require_object(fixture["evidence"], "evidence", fixture_path)
        require_keys(evidence, evidence_required, "evidence", fixture_path)

        if not evidence.get("case_ref"):
            fail(f"{fixture_path.relative_to(ROOT)} evidence.case_ref is required")

        require_enum(evidence["evidence_kind"], evidence_kinds, "evidence_kind", fixture_path)
        require_enum(evidence["visibility"], visibility_values, "visibility", fixture_path)
        require_enum(
            evidence["retention_posture"],
            retention_values,
            "retention_posture",
            fixture_path,
        )

        for array_field in ("artifact_refs", "lineage_refs"):
            if array_field in evidence:
                require_string_array(evidence[array_field], array_field, fixture_path)

    print("case-evidence-binding: ok")


if __name__ == "__main__":
    main()
