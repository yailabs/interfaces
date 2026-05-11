#!/usr/bin/env python3
"""Dependency-free V54 conformance checks for canonical operator-context operations."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
SCHEMA_PATH = ROOT / "schemas" / "operator-context-operation.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "operator-context-operation"

EXPECTED_FIXTURES = {
    "operator-context-status.json",
    "operator-context-current.json",
    "active-case-set.json",
    "active-case-clear.json",
}

REQUIRED_OPERATOR_CONTEXT_OPS = {
    "operator_context.status",
    "operator_context.current",
    "operator_context.active_case.set",
    "operator_context.active_case.clear",
}

ACTION_TO_OPERATION = {
    "context.status": "operator_context.status",
    "context.current": "operator_context.current",
    "context.switch": "operator_context.active_case.set",
    "context.clear": "operator_context.active_case.clear",
}

REQUEST_KINDS = {
    "status",
    "current",
    "active_case_set",
    "active_case_clear",
}

OPERATION_STATUSES = {
    "allowed",
    "blocked",
    "unavailable",
    "not_implemented",
    "legacy_alias",
    "forbidden",
}

SAFE_PROJECTION_FIELDS = {
    "action_id",
    "operation_status",
    "root_case_ref",
    "active_case_ref",
    "operator_context_ref",
    "principal_ref",
    "auth_context_ref",
    "reason",
    "next_action",
}

FORBIDDEN_KEYS = {
    "session_ref",
    "session_id",
    "session_owner",
    "client_owner",
    "shell_owner",
    "runtime_owner",
    "job_ref",
    "workflow_ref",
    "agent_ref",
    "provider_call_ref",
    "evidence_ref",
    "record_ref",
    "knowledge_ref",
    "analytics_ref",
}

SCHEMA_REF = "schemas/operator-context-operation.v1.schema.json"


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def scan_forbidden_keys(name: str, node: object, errors: list[str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            require(key not in FORBIDDEN_KEYS, f"{name}: forbidden key present: {key}", errors)
            scan_forbidden_keys(name, value, errors)
    elif isinstance(node, list):
        for value in node:
            scan_forbidden_keys(name, value, errors)


def validate_fixture(name: str, payload: object, errors: list[str]) -> None:
    require(isinstance(payload, dict), f"{name}: top-level JSON must be an object", errors)
    if not isinstance(payload, dict):
        return

    scan_forbidden_keys(name, payload, errors)

    require("operator_context_operation" in payload, f"{name}: missing operator_context_operation", errors)
    operation = payload.get("operator_context_operation")
    require(isinstance(operation, dict), f"{name}: operator_context_operation must be an object", errors)
    if not isinstance(operation, dict):
        return

    for field in (
        "operation_id",
        "action_id",
        "request_kind",
        "operation_status",
        "root_case_ref",
        "active_case_ref",
        "operator_context_ref",
        "operator_context_owner",
        "selection_mutated",
        "session_mutated",
        "client_mutated",
        "shell_mutated",
        "runtime_mutated",
        "auth_mutated",
        "safe_projection",
    ):
        require(field in operation, f"{name}: missing {field}", errors)

    opid = operation.get("operation_id")
    action_id = operation.get("action_id")
    request_kind = operation.get("request_kind")
    operation_status = operation.get("operation_status")

    require(isinstance(opid, str) and opid.startswith("operator_context."), f"{name}: operation_id must start with operator_context.", errors)
    require(isinstance(action_id, str) and action_id.startswith("context."), f"{name}: action_id must start with context.", errors)
    require(request_kind in REQUEST_KINDS, f"{name}: unknown request_kind {request_kind!r}", errors)
    require(operation_status in OPERATION_STATUSES, f"{name}: unknown operation_status {operation_status!r}", errors)
    require(operation.get("operator_context_owner") == "operator_context.active_case_ref", f"{name}: operator_context_owner must be operator_context.active_case_ref", errors)
    for field in ("session_mutated", "client_mutated", "shell_mutated", "runtime_mutated", "auth_mutated"):
        require(operation.get(field) is False, f"{name}: {field} must be false", errors)
    require(isinstance(operation.get("selection_mutated"), bool), f"{name}: selection_mutated must be boolean", errors)

    active_case_ref = operation.get("active_case_ref")
    require(
        active_case_ref is None or (isinstance(active_case_ref, str) and active_case_ref.strip()),
        f"{name}: active_case_ref must be null or a non-empty string",
        errors,
    )

    safe_projection = operation.get("safe_projection")
    require(isinstance(safe_projection, dict), f"{name}: safe_projection must be an object", errors)
    if isinstance(safe_projection, dict):
        extra = sorted(set(safe_projection) - SAFE_PROJECTION_FIELDS)
        require(not extra, f"{name}: safe_projection contains unsupported fields: {extra}", errors)
        for field in ("action_id", "operation_status", "root_case_ref", "active_case_ref", "operator_context_ref"):
            require(field in safe_projection, f"{name}: safe_projection missing {field}", errors)
        if isinstance(action_id, str):
            require(safe_projection.get("action_id") == action_id, f"{name}: safe_projection.action_id must match action_id", errors)
        if operation_status in OPERATION_STATUSES:
            require(safe_projection.get("operation_status") == operation_status, f"{name}: safe_projection.operation_status must match operation_status", errors)

    if name == "active-case-set.json":
        require(request_kind == "active_case_set", f"{name}: set fixture must use active_case_set", errors)
        require(operation.get("selection_mutated") is True, f"{name}: set fixture must mutate selection", errors)
        selected = operation.get("selected_case_ref")
        require(isinstance(selected, str) and selected.strip(), f"{name}: selected_case_ref must be non-empty", errors)
    elif name == "active-case-clear.json":
        require(request_kind == "active_case_clear", f"{name}: clear fixture must use active_case_clear", errors)
        require(operation.get("selection_mutated") is True, f"{name}: clear fixture must mutate selection", errors)
        require(operation.get("active_case_ref") is None, f"{name}: clear fixture must clear active_case_ref", errors)
    else:
        require(operation.get("selection_mutated") is False, f"{name}: status/current fixtures must not mutate selection", errors)


def main() -> int:
    errors: list[str] = []

    schema = load_json(SCHEMA_PATH)
    require(isinstance(schema, dict), "schema: top-level schema must be an object", errors)
    if isinstance(schema, dict):
        require(schema.get("$id") == "https://yai.dev/schemas/operator-context-operation.v1.schema.json", "schema: unexpected $id", errors)
        require("operator_context_operation" in schema.get("properties", {}), "schema: missing operator_context_operation property", errors)

    fixtures = {path.name for path in FIXTURE_DIR.glob("*.json")}
    require(fixtures == EXPECTED_FIXTURES, f"fixtures: expected {sorted(EXPECTED_FIXTURES)}, found {sorted(fixtures)}", errors)

    operations_doc = load_json(REGISTRY / "api-operations.v1.json")
    surfaces_doc = load_json(REGISTRY / "api-surfaces.v1.json")
    projections_doc = load_json(REGISTRY / "api-operation-projections.v1.json")
    actions_doc = load_json(REGISTRY / "yai-actions.v1.json")

    if isinstance(operations_doc, dict):
        operation_rows = {row["operation_id"]: row for row in operations_doc.get("operations", [])}
        for opid in REQUIRED_OPERATOR_CONTEXT_OPS:
            row = operation_rows.get(opid)
            require(row is not None, f"registry: missing operator_context operation {opid}", errors)
            if row is None:
                continue
            require(row.get("family") == "operator_context", f"registry: {opid} must stay in operator_context family", errors)
            require(row.get("output_schema") == SCHEMA_REF, f"registry: {opid} must use {SCHEMA_REF}", errors)
            require(row.get("governance_required") is False, f"registry: {opid} must not require governance", errors)
            require(row.get("records_emitted") is False, f"registry: {opid} must not emit records", errors)
        for opid, row in operation_rows.items():
            if row.get("family") in {"session", "client"}:
                text = json.dumps(row, sort_keys=True)
                require("active_case" not in text, f"registry: {opid} must not own active_case semantics", errors)

    if isinstance(surfaces_doc, dict):
        surface = set(surfaces_doc.get("surfaces", {}).get("operator_context", []))
        for entry in ("status", "current", "active_case.set", "active_case.clear"):
            require(entry in surface, f"surfaces: operator_context surface missing {entry}", errors)

    if isinstance(projections_doc, dict):
        bridges = {row.get("source_action_or_command"): row for row in projections_doc.get("projection_bridges", [])}
        expected = {
            "case.enter": "operator_context.active_case.set",
            "case.leave": "operator_context.active_case.clear",
            "case.status": "operator_context.status",
            "context.switch": "operator_context.active_case.set",
            "context.clear": "operator_context.active_case.clear",
        }
        for source, target in expected.items():
            row = bridges.get(source)
            require(row is not None, f"projections: missing projection bridge for {source}", errors)
            if row is not None:
                require(row.get("canonical_api_operation_id") == target, f"projections: {source} must map to {target}", errors)

    if isinstance(actions_doc, dict):
        action_rows = {row["action_id"]: row for row in actions_doc.get("actions", [])}
        for action_id, opid in ACTION_TO_OPERATION.items():
            row = action_rows.get(action_id)
            require(row is not None, f"yai-actions: missing {action_id}", errors)
            if row is not None:
                require(row.get("api_operation_candidate") == opid, f"yai-actions: {action_id} must map to {opid}", errors)

    for fixture_name in sorted(EXPECTED_FIXTURES):
        validate_fixture(fixture_name, load_json(FIXTURE_DIR / fixture_name), errors)

    if errors:
        print("operator-context-operations: FAIL")
        for error in errors:
            print("-", error)
        return 1

    print("operator-context-operations: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
