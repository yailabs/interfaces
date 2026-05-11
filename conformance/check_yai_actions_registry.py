#!/usr/bin/env python3
import json
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parents[1]
actions_doc = json.loads((root / "registry/yai-actions.v1.json").read_text())
actions = actions_doc["actions"]

required_fields = {
    "action_id",
    "family",
    "lifecycle_stage",
    "canonical_name",
    "description",
    "cli_projection",
    "tui_projection",
    "api_operation_candidate",
    "sdk_surface_candidate",
    "runtime_action_key_candidate",
    "required_posture",
    "availability",
    "implementation_status",
    "test_priority",
    "aliases",
    "forbidden",
    "replacement_action_id",
    "notes",
}
lifecycle_stages = {
    "catalog",
    "status",
    "inspect",
    "check",
    "configure",
    "plan",
    "run",
    "watch",
    "outputs",
    "evidence",
    "lineage",
    "cancel",
    "explain",
    "diagnostics",
    "compatibility",
    "forbidden",
}
implementation_statuses = {
    "implemented_current",
    "canonical_target",
    "planned",
    "diagnostic_only",
    "api_only",
    "sdk_only",
    "runtime_internal",
    "storage_internal",
    "legacy_compat",
    "deprecated",
    "forbidden",
    "unknown_needs_audit",
}
availability_values = {
    "available",
    "available_read_only",
    "available_diagnostic",
    "blocked_by_auth",
    "blocked_by_case",
    "blocked_by_active_case",
    "blocked_by_machine_authorization",
    "blocked_by_license_lease",
    "blocked_by_entitlement",
    "blocked_by_runtime_gate",
    "blocked_by_limit",
    "blocked_by_policy",
    "blocked_by_manual_review",
    "not_implemented",
    "legacy_only",
    "forbidden",
}
test_priorities = {"P0", "P1", "P2", "P3", "N/A"}
required_forbidden = {
    "runtime.start",
    "runtime.stop",
    "runtime.restart",
    "query.root",
    "inspect.root",
    "policy.root",
    "substrate.inspect.raw",
}
compat_statuses = {"legacy_compat", "deprecated", "forbidden"}

errors = []
ids = set()
cli_projection_map = defaultdict(list)

for action in actions:
    action_id = action.get("action_id", "<unknown>")
    missing = sorted(required_fields - set(action))
    if missing:
        errors.append(f"missing fields for {action_id}: {','.join(missing)}")
        continue

    if action_id in ids:
        errors.append(f"duplicate action_id: {action_id}")
    ids.add(action_id)

    if action["lifecycle_stage"] not in lifecycle_stages:
        errors.append(
            f"unknown lifecycle_stage '{action['lifecycle_stage']}' in {action_id}"
        )
    if action["implementation_status"] not in implementation_statuses:
        errors.append(
            f"unknown implementation_status '{action['implementation_status']}' in {action_id}"
        )
    if action["availability"] not in availability_values:
        errors.append(f"unknown availability '{action['availability']}' in {action_id}")
    if action["test_priority"] not in test_priorities:
        errors.append(f"unknown test_priority '{action['test_priority']}' in {action_id}")
    if not isinstance(action["forbidden"], bool):
        errors.append(f"forbidden must be boolean in {action_id}")

    cli_projection = action.get("cli_projection")
    if isinstance(cli_projection, str) and cli_projection:
        cli_projection_map[cli_projection].append(action)

    if action_id in required_forbidden:
        if not action["forbidden"]:
            errors.append(f"required forbidden action not marked forbidden: {action_id}")
        if action["availability"] != "forbidden":
            errors.append(f"forbidden action must have forbidden availability: {action_id}")
        if action["implementation_status"] != "forbidden":
            errors.append(
                f"forbidden action must have forbidden implementation status: {action_id}"
            )

    if action["implementation_status"] in {"legacy_compat", "deprecated"}:
        if not (action["aliases"] or action["replacement_action_id"] or action["notes"]):
            errors.append(
                f"legacy/deprecated action requires alias, replacement, or notes: {action_id}"
            )

for projection, rows in cli_projection_map.items():
    if len(rows) > 1:
        if not all(row["implementation_status"] in compat_statuses for row in rows):
            ids = ", ".join(row["action_id"] for row in rows)
            errors.append(
                f"duplicate canonical CLI projection without compat status: {projection} -> {ids}"
            )

if errors:
    print("yai-actions: FAIL")
    for err in errors:
        print("-", err)
    raise SystemExit(1)

print("yai-actions: ok")
