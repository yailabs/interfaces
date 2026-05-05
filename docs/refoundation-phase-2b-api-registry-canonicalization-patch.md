# Refoundation Phase 2B — API Registry Canonicalization Patch

## Scope
Patched API registries/conformance to remove legacy public naming drift found in Phase 2A.

## Registry changes
- `registry/api-plane-surfaces.v1.json`
  - `runtime` -> `system`
  - removed root public `records` plane by canonicalizing to `state` with owner `../yai/state`
  - `flow` -> `workflow`
  - `orchestration` -> `orchestrator`
  - added canonical public planes `conversation`, `prompting`, `output` as scaffolded/planned metadata
- `registry/api-surfaces.v1.json`
  - replaced CLI-style keys (`ai`, `flow`, `runtime`, `govern`, `provider`, `agent`, `inspect`) with canonical public keys
  - retained operation-oriented suffixes (e.g. `state.records.query`, `workflow.runs.watch`)
- `registry/api-operations.v1.json`
  - corrected readiness metadata to `planned` for:
    - `case.records.tail`
    - `state.records.tail`
    - `workflow.runs.watch`
    - `control.gates.list`

## Conformance checks added
- fail on forbidden canonical public planes: `flow`, `records`, `orchestration`
- fail on forbidden canonical surface keys: `ai`, `flow`, `runtime`, `govern`, `provider`, `agent`, `inspect`
- fail on forbidden operation namespaces: `flow.*`, `records.*`, `orchestration.*`, `supervisor.*`, root `policy.*`

## Remaining allowed internal references
- implementation owner paths may still reference `../yai/flow` and `../yai/orchestration` where public plane is canonical (`workflow`, `orchestrator`)
- operation IDs under `state.records.*` and `governance.policy.*` remain allowed

## Not changed
- no operation IDs added/removed
- no schema expansion (no controlled-action API schema in this phase)
- no runtime implementation claims added
- no sibling repo changes

## Recommended next phase
- Phase 2C — API Controlled Action Contract Proposal (optional)
- Otherwise Phase 3A — SDK Typed Operation Gate Audit
