#!/usr/bin/env python3
"""Dependency-free V52 conformance checks for canonical case operations."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
SCHEMA_PATH = ROOT / "schemas" / "case-operation.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "case-operation"

EXPECTED_FIXTURES = {
    "root-response.json",
    "list-response.json",
    "open-response.json",
    "enter-response.json",
    "leave-response.json",
    "status-response.json",
    "close-response.json",
}

REQUIRED_CANONICAL_OPS = {
    "case.root",
    "case.list",
    "case.open",
    "case.enter",
    "case.leave",
    "case.status",
    "case.close",
}

ACTION_TO_OPERATION = {
    "case.root": "case.root",
    "case.list": "case.list",
    "case.open": "case.open",
    "case.enter": "case.enter",
    "case.leave": "case.leave",
    "case.status": "case.status",
    "case.close": "case.close",
}

CASE_OPERATION_SCHEMA = "schemas/case-operation.v1.schema.json"


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_case_node(name: str, node: object, errors: list[str]) -> None:
    require(isinstance(node, dict), f"{name}: case node must be an object", errors)
    if not isinstance(node, dict):
      return
    for field in ("case_ref", "kind"):
        value = node.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: node {field} must be a non-empty string", errors)
    require(isinstance(node.get("path"), str), f"{name}: node path must be a string", errors)
    require("parent_case_ref" in node, f"{name}: node must carry parent_case_ref", errors)
    if "parent_case_ref" in node:
        parent = node.get("parent_case_ref")
        require(parent is None or (isinstance(parent, str) and parent.strip()), f"{name}: node parent_case_ref must be null or a non-empty string", errors)
    require(isinstance(node.get("active"), bool), f"{name}: node active must be boolean", errors)


def validate_fixture(name: str, payload: object, errors: list[str]) -> None:
    require(isinstance(payload, dict), f"{name}: top-level JSON must be an object", errors)
    if not isinstance(payload, dict):
        return

    require("case_operation" in payload, f"{name}: missing case_operation", errors)
    operation = payload.get("case_operation")
    require(isinstance(operation, dict), f"{name}: case_operation must be an object", errors)
    if not isinstance(operation, dict):
        return

    for field in (
        "operation_id",
        "outcome",
        "summary",
        "root_case_ref",
        "operator_context_owner",
    ):
        value = operation.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field} must be a non-empty string", errors)

    require(operation.get("operation_id") in REQUIRED_CANONICAL_OPS, f"{name}: unexpected operation_id {operation.get('operation_id')!r}", errors)
    require(operation.get("operator_context_owner") == "operator_context.active_case_ref", f"{name}: operator_context_owner must be operator_context.active_case_ref", errors)
    require(operation.get("session_mutated") is False, f"{name}: session_mutated must be false", errors)
    require(operation.get("evidence_deleted") is False, f"{name}: evidence_deleted must be false", errors)
    require(operation.get("knowledge_deleted") is False, f"{name}: knowledge_deleted must be false", errors)
    require(operation.get("records_deleted") is False, f"{name}: records_deleted must be false", errors)
    require(isinstance(operation.get("case_tree_mutated"), bool), f"{name}: case_tree_mutated must be boolean", errors)
    require(isinstance(operation.get("operator_context_mutated"), bool), f"{name}: operator_context_mutated must be boolean", errors)

    active = operation.get("active_case_ref")
    require(
        active is None or (isinstance(active, str) and active.strip()),
        f"{name}: active_case_ref must be null or a non-empty string",
        errors,
    )

    cases = operation.get("cases")
    require(isinstance(cases, list), f"{name}: cases must be a list", errors)
    if isinstance(cases, list):
        for index, node in enumerate(cases):
            validate_case_node(f"{name}: cases[{index}]", node, errors)

    warnings = operation.get("warnings")
    if warnings is not None:
        require(isinstance(warnings, list), f"{name}: warnings must be a list", errors)
    next_actions = operation.get("next_actions")
    if next_actions is not None:
        require(isinstance(next_actions, list), f"{name}: next_actions must be a list", errors)

    if name == "open-response.json":
        require(operation.get("case_tree_mutated") is True, f"{name}: open must mutate case tree", errors)
        opened = operation.get("opened_case_ref")
        require(isinstance(opened, str) and opened.strip(), f"{name}: opened_case_ref must be set", errors)
        require(operation.get("operator_context_mutated") is False, f"{name}: open must not mutate operator context", errors)
    elif name == "enter-response.json":
        require(operation.get("operator_context_mutated") is True, f"{name}: enter must mutate operator context", errors)
        entered = operation.get("entered_case_ref")
        require(isinstance(entered, str) and entered.strip(), f"{name}: entered_case_ref must be set", errors)
    elif name == "leave-response.json":
        require(operation.get("operator_context_mutated") is True, f"{name}: leave must mutate operator context", errors)
        require(operation.get("active_case_ref") is None, f"{name}: leave must clear active_case_ref", errors)
    elif name == "close-response.json":
        require(operation.get("case_tree_mutated") is True, f"{name}: close must mutate case tree", errors)
        require(operation.get("operator_context_mutated") is False, f"{name}: close must not mutate operator context", errors)
        closed = operation.get("closed_case_ref")
        require(isinstance(closed, str) and closed.strip(), f"{name}: closed_case_ref must be set", errors)


def main() -> int:
    errors: list[str] = []

    schema = load_json(SCHEMA_PATH)
    require(isinstance(schema, dict), "schema: top-level schema must be an object", errors)
    if isinstance(schema, dict):
        require(schema.get("$id") == "https://yai.dev/schemas/case-operation.v1.schema.json", "schema: unexpected $id", errors)
        require("case_operation" in schema.get("properties", {}), "schema: missing case_operation property", errors)

    fixtures = {path.name for path in FIXTURE_DIR.glob("*.json")}
    require(fixtures == EXPECTED_FIXTURES, f"fixtures: expected {sorted(EXPECTED_FIXTURES)}, found {sorted(fixtures)}", errors)

    operations_doc = load_json(REGISTRY / "api-operations.v1.json")
    surfaces_doc = load_json(REGISTRY / "api-surfaces.v1.json")
    projections_doc = load_json(REGISTRY / "api-operation-projections.v1.json")
    actions_doc = load_json(REGISTRY / "yai-actions.v1.json")

    if isinstance(operations_doc, dict):
        operation_rows = {
            row["operation_id"]: row for row in operations_doc.get("operations", [])
        }
        for opid in REQUIRED_CANONICAL_OPS:
            row = operation_rows.get(opid)
            require(row is not None, f"registry: missing canonical case operation {opid}", errors)
            if row is None:
                continue
            require(row.get("family") == "case", f"registry: {opid} must stay in case family", errors)
            require(row.get("output_schema") == CASE_OPERATION_SCHEMA, f"registry: {opid} must use {CASE_OPERATION_SCHEMA}", errors)
            require(row.get("status") == "seed", f"registry: {opid} must stay seed in V52", errors)

        for legacy_op in ("case.create", "case.use"):
            row = operation_rows.get(legacy_op)
            require(row is not None, f"registry: missing compatibility operation {legacy_op}", errors)
            if row is not None:
                require(row.get("status") in {"legacy", "deprecated"}, f"registry: {legacy_op} must be legacy/deprecated", errors)

    if isinstance(surfaces_doc, dict):
        case_surface = set(surfaces_doc.get("surfaces", {}).get("case", []))
        for projection in ("root", "list", "open", "enter", "leave", "status", "close"):
            require(projection in case_surface, f"surfaces: case surface missing {projection}", errors)

    if isinstance(projections_doc, dict):
        aliases = {row.get("alias"): row for row in projections_doc.get("legacy_alias_mappings", [])}
        require("case.create" in aliases, "projections: missing case.create legacy alias", errors)
        require("case.use" in aliases, "projections: missing case.use legacy alias", errors)
        if "case.create" in aliases:
            require(aliases["case.create"].get("canonical_operation_id") == "case.open", "projections: case.create must map to case.open", errors)
        if "case.use" in aliases:
            require(aliases["case.use"].get("canonical_operation_id") == "case.enter", "projections: case.use must map to case.enter", errors)

    if isinstance(actions_doc, dict):
        action_rows = {row["action_id"]: row for row in actions_doc.get("actions", [])}
        for action_id, opid in ACTION_TO_OPERATION.items():
            row = action_rows.get(action_id)
            require(row is not None, f"yai-actions: missing {action_id}", errors)
            if row is None:
                continue
            require(row.get("api_operation_candidate") == opid, f"yai-actions: {action_id} must map to {opid}", errors)

    for fixture_name in sorted(EXPECTED_FIXTURES):
        validate_fixture(fixture_name, load_json(FIXTURE_DIR / fixture_name), errors)

    if errors:
        print("case-operations: FAIL")
        for error in errors:
            print("-", error)
        return 1

    print("case-operations: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
