#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
registry = root / "registry"

ops_doc = json.loads((registry / "api-operations.v1.json").read_text())
families_doc = json.loads((registry / "api-families.v1.json").read_text())
verbs_doc = json.loads((registry / "api-verbs.v1.json").read_text())
projections_doc = json.loads((registry / "api-operation-projections.v1.json").read_text())
surfaces_doc = json.loads((registry / "api-surfaces.v1.json").read_text())
actions_doc = json.loads((registry / "yai-actions.v1.json").read_text())

ops = ops_doc["operations"]
family_rows = families_doc["families"]
verbs = {v["id"] for v in verbs_doc["verbs"]}
projection_ids = {p["id"] for p in projections_doc.get("high_level_projections", [])}
surfaces = surfaces_doc.get("surfaces", {})
surface_status = surfaces_doc.get("surface_status", {})
actions = actions_doc["actions"]

family_status = {f["id"]: f.get("status") for f in family_rows}
family_ids = set(family_status)
operation_ids = []
operation_status = {}
required_fields = {
    "operation_id",
    "family",
    "resource",
    "verb",
    "scope",
    "mutation_class",
    "status",
}
allowed_statuses = {"seed", "seed-projection", "legacy", "deprecated"}
required_v51_families = {
    "policy_pack",
    "intake",
    "materialization",
    "excerpt",
    "evidence",
    "lineage",
    "recall",
    "job",
    "license",
    "machine",
    "limits",
    "logs",
}
required_v51_ops = {
    "policy_pack.inspect",
    "intake.plan",
    "materialization.plan",
    "evidence.show",
    "lineage.trace",
    "license.status",
    "machine.status",
    "limits.status",
    "logs.runtime.watch",
    "workflow.runs.stop",
    "state.records.query",
    "state.records.tail",
}
required_v52_case_ops = {
    "case.root",
    "case.list",
    "case.open",
    "case.enter",
    "case.leave",
    "case.status",
    "case.close",
}
required_v53_auth_ops = {
    "auth.login",
    "auth.login.local_dev",
    "auth.status",
    "auth.logout",
    "auth.context.inspect",
    "auth.provider.status",
    "auth.device_login.start",
    "auth.device_login.status",
    "auth.device_login.cancel",
}
required_v54_operator_context_ops = {
    "operator_context.status",
    "operator_context.current",
    "operator_context.active_case.set",
    "operator_context.active_case.clear",
}
case_schema_operation_ids = required_v52_case_ops | {
    "case.current",
    "case.show",
    "case.tree",
    "case.pending",
}
case_operation_schema = "schemas/case-operation.v1.schema.json"
auth_schema_operation_ids = required_v53_auth_ops | {
    "auth.whoami",
}
auth_operation_schema = "schemas/auth-operation.v1.schema.json"
operator_context_schema_operation_ids = required_v54_operator_context_ops
operator_context_operation_schema = "schemas/operator-context-operation.v1.schema.json"
forbidden_prefixes = (
    "flow.",
    "records.",
    "policy.",
    "query.",
    "inspect.",
    "runtime.",
)
forbidden_operation_ids = {
    "runtime.start",
    "runtime.stop",
    "runtime.restart",
    "system.start",
    "system.stop",
    "system.restart",
    "system.service.start",
    "system.service.stop",
}
required_legacy_aliases = {
    "auth.whoami",
    "case.create",
    "case.use",
    "flow.*",
    "knowledge.lineage.trace",
    "control.evidence.show",
    "session.*",
    "records.*",
    "runtime.status",
    "policy.root",
    "query.root",
    "inspect.root",
}
required_forbidden_actions = {
    "runtime.start",
    "runtime.stop",
    "runtime.restart",
    "query.root",
    "inspect.root",
    "policy.root",
    "substrate.inspect.raw",
}

errors = []

for family in required_v51_families:
    if family not in family_ids:
        errors.append(f"missing V51 canonical family: {family}")
if "operator_context" not in family_ids:
    errors.append("missing V54 canonical family: operator_context")

for forbidden_family in {"flow", "records", "policy", "query", "inspect", "runtime"}:
    if forbidden_family in family_ids:
        errors.append(f"forbidden canonical family present: {forbidden_family}")

for singular_family in {"provider", "model", "agent"}:
    if singular_family in family_ids:
        errors.append(f"singular API family should not exist: {singular_family}")

if family_status.get("session") not in {"legacy", "deprecated"}:
    errors.append("session family must be legacy/deprecated in V51")
if family_status.get("workflow") not in {"seed", "canonical"}:
    errors.append("workflow family must remain canonical/seed in V51")
if surface_status.get("session") not in {"legacy", "deprecated"}:
    errors.append("session surface must be marked legacy/deprecated")
if surface_status.get("case") not in {None, "seed", "canonical"}:
    errors.append("case surface must remain canonical/seed")
if surface_status.get("auth") not in {None, "seed", "canonical"}:
    errors.append("auth surface must remain canonical/seed")
if surface_status.get("operator_context") not in {None, "seed", "canonical"}:
    errors.append("operator_context surface must remain canonical/seed")

for key in {"policy_pack", "intake", "materialization", "excerpt", "evidence", "lineage", "recall", "job", "license", "machine", "limits", "logs"}:
    if key not in surfaces:
        errors.append(f"missing API surface for V51 family: {key}")
if "auth" not in surfaces:
    errors.append("missing API surface for V53 family: auth")
if "operator_context" not in surfaces:
    errors.append("missing API surface for V54 family: operator_context")

for forbidden_surface in {"flow", "records", "policy", "query", "inspect", "runtime", "provider", "model", "agent"}:
    if forbidden_surface in surfaces:
        errors.append(f"forbidden canonical surface key: {forbidden_surface}")
for surface_name in {"root", "list", "open", "enter", "leave", "status", "close"}:
    if surface_name not in set(surfaces.get("case", [])):
        errors.append(f"case surface missing V52 operation projection: {surface_name}")
for surface_name in {
    "login",
    "login.local_dev",
    "status",
    "logout",
    "context.inspect",
    "provider.status",
    "device_login.start",
    "device_login.status",
    "device_login.cancel",
}:
    if surface_name not in set(surfaces.get("auth", [])):
        errors.append(f"auth surface missing V53 operation projection: {surface_name}")
for surface_name in {"status", "current", "active_case.set", "active_case.clear"}:
    if surface_name not in set(surfaces.get("operator_context", [])):
        errors.append(
            f"operator_context surface missing V54 operation projection: {surface_name}"
        )

for op in ops:
    opid = op.get("operation_id", "<unknown>")
    operation_ids.append(opid)
    operation_status[opid] = op.get("status")

    missing = sorted(required_fields - set(op))
    if missing:
        errors.append(f"missing fields for {opid}: {','.join(missing)}")
        continue

    if op["status"] not in allowed_statuses:
        errors.append(f"unknown operation status '{op['status']}' in {opid}")
    if op["family"] not in family_ids and op["family"] not in projection_ids:
        errors.append(f"unknown family {op['family']} in {opid}")
    if op["verb"] not in verbs and "custom_verb_justification" not in op:
        errors.append(
            f"unknown verb {op['verb']} in {opid} (no custom_verb_justification)"
        )
    if opid in forbidden_operation_ids:
        errors.append(f"forbidden lifecycle operation present: {opid}")
    if opid.startswith(forbidden_prefixes):
        errors.append(f"forbidden operation namespace: {opid}")
    if op["family"] == "session" and op["status"] not in {"legacy", "deprecated"}:
        errors.append(f"session operation must be legacy/deprecated: {opid}")

if len(operation_ids) != len(set(operation_ids)):
    errors.append("duplicate operation_id entries detected")

for opid in required_v51_ops:
    if opid not in operation_status:
        errors.append(f"missing required V51 operation: {opid}")
for opid in required_v52_case_ops:
    if opid not in operation_status:
        errors.append(f"missing required V52 case operation: {opid}")
for opid in required_v53_auth_ops:
    if opid not in operation_status:
        errors.append(f"missing required V53 auth operation: {opid}")
for opid in required_v54_operator_context_ops:
    if opid not in operation_status:
        errors.append(f"missing required V54 operator_context operation: {opid}")

op_rows = {op["operation_id"]: op for op in ops}
for opid in case_schema_operation_ids:
    row = op_rows.get(opid)
    if row is None:
        continue
    if row.get("output_schema") != case_operation_schema:
        errors.append(f"{opid} must use {case_operation_schema}")
for opid in required_v52_case_ops:
    row = op_rows.get(opid)
    if row is None:
        continue
    if row.get("family") != "case":
        errors.append(f"{opid} must stay in case family")
    if row.get("status") not in {"seed", "seed-projection"}:
        errors.append(f"{opid} must remain canonical seed/seed-projection")
if operation_status.get("case.create") not in {"legacy", "deprecated"}:
    errors.append("case.create must be legacy/deprecated in V52")
if operation_status.get("case.use") not in {"legacy", "deprecated"}:
    errors.append("case.use must be legacy/deprecated in V52")

for opid in auth_schema_operation_ids:
    row = op_rows.get(opid)
    if row is None:
        continue
    if row.get("output_schema") != auth_operation_schema:
        errors.append(f"{opid} must use {auth_operation_schema}")
for opid in required_v53_auth_ops:
    row = op_rows.get(opid)
    if row is None:
        continue
    if row.get("family") != "auth":
        errors.append(f"{opid} must stay in auth family")
    if row.get("status") not in {"seed", "seed-projection"}:
        errors.append(f"{opid} must remain canonical seed/seed-projection")
    if row.get("governance_required") is not False:
        errors.append(f"{opid} must not require governance")
    if row.get("records_emitted") is not False:
        errors.append(f"{opid} must not emit records")
    if row.get("conversation_bound") is not False:
        errors.append(f"{opid} must not be conversation-bound")
if operation_status.get("auth.whoami") not in {"legacy", "deprecated"}:
    errors.append("auth.whoami must be legacy/deprecated in V53")

for opid in operator_context_schema_operation_ids:
    row = op_rows.get(opid)
    if row is None:
        continue
    if row.get("output_schema") != operator_context_operation_schema:
        errors.append(f"{opid} must use {operator_context_operation_schema}")
for opid in required_v54_operator_context_ops:
    row = op_rows.get(opid)
    if row is None:
        continue
    if row.get("family") != "operator_context":
        errors.append(f"{opid} must stay in operator_context family")
    if row.get("status") not in {"seed", "seed-projection"}:
        errors.append(f"{opid} must remain canonical seed/seed-projection")
    if row.get("governance_required") is not False:
        errors.append(f"{opid} must not require governance")
    if row.get("records_emitted") is not False:
        errors.append(f"{opid} must not emit records")
    if row.get("conversation_bound") is not False:
        errors.append(f"{opid} must not be conversation-bound")
for family_name in {"session", "client", "shell", "case"}:
    for opid, row in op_rows.items():
        if row.get("family") != family_name:
            continue
        serialized = json.dumps(row, sort_keys=True)
        if "active_case_ref" in serialized or '"active_case"' in serialized:
            errors.append(
                f"{family_name} operation must not own active-case semantics directly: {opid}"
            )

if operation_status.get("knowledge.lineage.trace") not in {"legacy", "deprecated"}:
    errors.append("knowledge.lineage.trace must be legacy/deprecated in V51")
if operation_status.get("control.evidence.show") not in {"legacy", "deprecated"}:
    errors.append("control.evidence.show must be legacy/deprecated in V51")

alias_rows = {
    row.get("alias"): row for row in projections_doc.get("legacy_alias_mappings", [])
}
for alias in required_legacy_aliases:
    if alias not in alias_rows:
        errors.append(f"missing required legacy alias mapping: {alias}")
for alias, row in alias_rows.items():
    target = row.get("canonical_operation_id")
    target_prefix = row.get("canonical_operation_prefix")
    if target and target not in operation_status:
        errors.append(f"legacy alias target missing operation: {alias} -> {target}")
    if target_prefix and not any(opid.startswith(target_prefix) for opid in operation_status):
        errors.append(
            f"legacy alias target prefix missing operations: {alias} -> {target_prefix}"
        )

forbidden_actions = {
    row.get("action_id") for row in projections_doc.get("forbidden_actions", [])
}
for action_id in required_forbidden_actions:
    if action_id not in forbidden_actions:
        errors.append(f"missing forbidden action projection lock: {action_id}")

action_rows = {row["action_id"]: row for row in actions}
for action_id in forbidden_actions:
    row = action_rows.get(action_id)
    if row is None:
        errors.append(f"forbidden action missing from yai-actions: {action_id}")
        continue
    if not row.get("forbidden"):
        errors.append(f"forbidden action not marked forbidden in yai-actions: {action_id}")

for action in actions:
    action_id = action["action_id"]
    candidate = action.get("api_operation_candidate")
    if candidate and candidate != "none verified" and candidate not in operation_status:
        errors.append(
            f"yai-actions api_operation_candidate missing from registry: {action_id} -> {candidate}"
        )
    if (
        action.get("implementation_status") in {"implemented_current", "canonical_target"}
        and candidate == "none verified"
        and not action.get("notes")
    ):
        errors.append(
            f"canonical action without API candidate must carry deferred note: {action_id}"
        )

for action_id, candidate in {
    "auth.login": "auth.login",
    "auth.login.local_dev": "auth.login.local_dev",
    "auth.status": "auth.status",
    "auth.logout": "auth.logout",
    "auth.context.inspect": "auth.context.inspect",
    "auth.provider.status": "auth.provider.status",
    "auth.device_login.start": "auth.device_login.start",
    "auth.device_login.status": "auth.device_login.status",
    "auth.device_login.cancel": "auth.device_login.cancel",
    "case.root": "case.root",
    "case.list": "case.list",
    "case.open": "case.open",
    "case.enter": "case.enter",
    "case.leave": "case.leave",
    "case.status": "case.status",
    "case.close": "case.close",
    "context.status": "operator_context.status",
    "context.current": "operator_context.current",
    "context.switch": "operator_context.active_case.set",
    "context.clear": "operator_context.active_case.clear",
}.items():
    row = action_rows.get(action_id)
    if row is None:
        errors.append(f"missing canonical action row in yai-actions: {action_id}")
        continue
    if row.get("api_operation_candidate") != candidate:
        errors.append(
            f"canonical action must map to expected registry operation: {action_id} -> {candidate}"
        )

projection_bridges = {
    row.get("source_action_or_command"): row.get("canonical_api_operation_id")
    for row in projections_doc.get("projection_bridges", [])
}
for action_id, target in {
    "case.enter": "operator_context.active_case.set",
    "case.leave": "operator_context.active_case.clear",
    "case.status": "operator_context.status",
    "context.switch": "operator_context.active_case.set",
    "context.clear": "operator_context.active_case.clear",
}.items():
    if projection_bridges.get(action_id) != target:
        errors.append(
            f"missing V54 projection bridge: {action_id} -> {target}"
        )

if errors:
    print("conformance: FAIL")
    for err in errors:
        print("-", err)
    raise SystemExit(1)

print("conformance: ok")
