#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
registry = root / "registry"
schemas = root / "schemas"
openapi_file = root / "openapi/yai-api.v1.yaml"

# parse json files
for p in list(registry.glob("*.json")) + list(schemas.glob("*.schema.json")):
    json.loads(p.read_text())

ops = json.loads((registry / "api-operations.v1.json").read_text())["operations"]
families = {f["id"] for f in json.loads((registry / "api-families.v1.json").read_text())["families"]}
errors = set(json.loads((registry / "api-errors.v1.json").read_text())["errors"])
subset = set(json.loads((registry / "api-operations.v1.json").read_text()).get("openapi_vertical_subset", []))

# yaml parsing with fallback
raw = openapi_file.read_text()
paths = set()
opids = set()
tags = set()
try:
    import yaml  # type: ignore
    doc = yaml.safe_load(raw)
    for t in doc.get("tags", []):
        if isinstance(t, dict) and "name" in t:
            tags.add(t["name"])
    for p, methods in doc.get("paths", {}).items():
        paths.add(p)
        if isinstance(methods, dict):
            for _, op in methods.items():
                if isinstance(op, dict):
                    if "operationId" in op:
                        opids.add(op["operationId"])
                    for tg in op.get("tags", []):
                        tags.add(tg)
except Exception:
    for line in raw.splitlines():
        s=line.strip()
        if s.startswith('/v1/') and s.endswith(':'):
            paths.add(s[:-1])
        if s.startswith('operationId:'):
            opids.add(s.split(':',1)[1].strip())
        if s.startswith('- name:'):
            tags.add(s.split(':',1)[1].strip())

errors_out=[]
for op in ops:
    if op["operation_id"].startswith("policy."):
        errors_out.append(f"forbidden root policy op: {op['operation_id']}")
    if op["operation_id"] in {"runtime.start","runtime.stop","runtime.restart","system.start","system.stop","system.restart","system.service.start","system.service.stop"}:
        errors_out.append(f"forbidden lifecycle op: {op['operation_id']}")
    if op["family"] == "supervisor":
        errors_out.append(f"forbidden family supervisor in {op['operation_id']}")
    for key in ("input_schema","output_schema"):
        ref = op.get(key,"")
        if ref.startswith("schemas/"):
            schema_name = ref.split('#',1)[0].split('/',1)[1]
            if not (schemas / schema_name).exists():
                errors_out.append(f"missing schema ref for {op['operation_id']}: {ref}")
    for e in op.get("errors", []):
        if e not in errors:
            errors_out.append(f"unknown error '{e}' in {op['operation_id']}")

for so in subset:
    if so not in opids:
        errors_out.append(f"openapi subset missing operationId: {so}")

for tg in tags:
    if tg not in families and tg != 'system':
        errors_out.append(f"openapi tag not mapped to family: {tg}")

if '/v1/operations/{operation_id}' not in paths:
    errors_out.append("missing /v1/operations/{operation_id} path")
if '/v1/operations' not in paths:
    errors_out.append("missing /v1/operations path")

if errors_out:
    print('api-contracts: FAIL')
    for e in errors_out:
        print('-', e)
    raise SystemExit(1)
print('api-contracts: ok')
