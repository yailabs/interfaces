#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
ops = json.loads((root / "registry/api-operations.v1.json").read_text())
families = json.loads((root / "registry/api-families.v1.json").read_text())
verbs = json.loads((root / "registry/api-verbs.v1.json").read_text())
projections = json.loads((root / "registry/api-operation-projections.v1.json").read_text())

family_ids = {f["id"] for f in families["families"]}
verb_ids = {v["id"] for v in verbs["verbs"]}
projection_ids = {p["id"] for p in projections.get("high_level_projections", [])}
required = {"operation_id","family","resource","verb","scope","mutation_class","status"}
forbidden = {
    "runtime.start","runtime.stop","runtime.restart",
    "system.start","system.stop","system.restart",
    "system.service.start","system.service.stop",
}
errors = []
for op in ops["operations"]:
    miss = sorted(required - set(op.keys()))
    if miss:
        errors.append(f"missing fields for {op.get('operation_id','<unknown>')}: {','.join(miss)}")
        continue
    if op["family"] not in family_ids and op["family"] not in projection_ids:
        errors.append(f"unknown family {op['family']} in {op['operation_id']}")
    if op["verb"] not in verb_ids and "custom_verb_justification" not in op:
        errors.append(f"unknown verb {op['verb']} in {op['operation_id']} (no custom_verb_justification)")
    if op["operation_id"] in forbidden:
        errors.append(f"forbidden lifecycle operation present: {op['operation_id']}")
    if op["operation_id"].startswith("policy."):
        errors.append(f"forbidden root policy operation: {op['operation_id']}")
    if op["family"] == "supervisor":
        errors.append(f"forbidden public family supervisor in {op['operation_id']}")
for op in ops["operations"]:
    if op["family"] in projection_ids and op.get("projection_kind") != "high_level_composition":
        errors.append(f"projection family not marked composition: {op['operation_id']}")
if errors:
    print("conformance: FAIL")
    for e in errors:
        print("-", e)
    raise SystemExit(1)
print("conformance: ok")
