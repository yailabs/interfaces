# Refoundation Phase 2A — API Contract Reconciliation Audit

## 1. Executive verdict

Verdict: **partial alignment with material drift**.

- API grammar guardrails are present and enforced for key forbiddens (`supervisor`, root `policy.*`, runtime/system lifecycle start/stop/restart).
- API operation registry is broadly aligned with current `yai` runtime truth for the Wave/Phase partial slices.
- Plane/surface registries still expose legacy/compat drift (`flow`, root `records`, `orchestration`) and must be cleaned before SDK typed projection hardens.
- OpenAPI remains a subset projection; it is usable as a contract slice but still over-represents planned operations as callable without explicit readiness posture.

## 2. API grammar alignment

Evidence:
- `Documentation/operation-grammar.md`
- `Documentation/api-source-of-truth.md`
- `Documentation/api-plane-surface-model.md`
- `conformance/check_operation_registry.py`
- `conformance/check_api_contracts.py`

Status:
- Public grammar intent is mostly correct: `workflow`, `control`, `governance.policy.*`, `state.records`, `system`.
- Conformance checks correctly reject:
  - `policy.*` root operations
  - `runtime.start|stop|restart`
  - `system.start|stop|restart`
  - public `supervisor` family
- Drift remains in plane/surface metadata documents/registries (see sections 4 and 5).

## 3. Runtime readiness alignment table (API vs YAI)

Source of runtime truth:
- `../yai/runtime/registry/runtime/implementation/runtime-handler-readiness.v1.json`

| operation_id | api registry | family/resource/verb | api runtime_handler_readiness | yai readiness | mismatch | action needed |
|---|---|---|---|---|---|---|
| case.current | yes | case/case/current | partial | partial | no | none |
| case.list | yes | case/case/list | partial | partial | no | none |
| case.show | yes | case/case/show | partial | partial | no | none |
| state.records.query | yes | state/records/query | partial | partial | no | none |
| knowledge.lineage.trace | yes | knowledge/lineage/trace | partial | partial | no | none |
| workflow.list | yes | workflow/workflow/list | partial | partial | no | none |
| workflow.show | yes | workflow/workflow/show | partial | partial | no | none |
| workflow.steps.pending | yes | workflow/steps/pending | partial | partial | no | none |
| governance.posture | yes | governance/governance/posture | partial | partial | no | none |
| governance.policy.resolve | yes | governance/policy/resolve | partial | partial | no | none |
| control.decisions.explain | yes | control/decisions/explain | partial | partial | no | none |
| conversation.current | yes | conversation/conversation/current | partial | partial | no | none |
| conversation.messages.send | yes | conversation/messages/send | partial | partial | no | none |
| prompting.context.assemble | yes | prompting/context/assemble | partial | partial | no | none |
| case.records.tail | yes | case/records/tail | partial | planned | yes | set API readiness metadata to planned/compat note |
| state.records.tail | yes | state/records/tail | partial | planned | yes | set API readiness metadata to planned/compat note |
| workflow.runs.watch | yes | workflow/runs/watch | partial | planned | yes | set API readiness metadata to planned/compat note |
| control.gates.list | yes | control/gates/list | partial | planned | yes | set API readiness metadata to planned/compat note |
| control.gates.show | yes | control/gates/show | planned | planned | no | none |

Summary:
- Main vertical slices are aligned.
- Four operations currently over-claimed in API metadata (`partial` in API vs `planned` in runtime readiness).

## 4. Plane/surface drift

### Drift found

1. `registry/api-plane-surfaces.v1.json` includes legacy/internal planes as public-looking entries:
- `records` (root) with `coreOwnerPath: ../yai/records`
- `flow`
- `orchestration`

2. `registry/api-surfaces.v1.json` includes legacy naming:
- top-level `flow` surface

3. `registry/api-families.v1.json` still carries internal-plane hints including `flow` and `orchestration`; `records` appears as surface member in some family metadata.

### Classification

- `flow`: **P0** for Phase 2B cleanup in public plane/surface view (must map to public `workflow`).
- root `records`: **P0** for Phase 2B cleanup (must remain `state.records` publicly).
- `orchestration` naming drift vs public `orchestrator`: **P1**.

## 5. Operation registry gaps

- API operation set is broad and includes many planned ops beyond current runtime slices; this is acceptable only if readiness and projection status are explicit and truthful.
- Immediate gap: per-operation readiness metadata mismatch on the four operations listed in section 3.
- High-level projections in `registry/api-operation-projections.v1.json` reference operations that are still planned (expected), but should be clearly marked as non-execution compositions in Documentation/conformance notes.

## 6. Schema/envelope gaps

Audited:
- `schemas/operation-contract.v1.schema.json`
- `schemas/operation-ref.v1.schema.json`
- `schemas/request-envelope.v1.schema.json`
- `schemas/response-envelope.v1.schema.json`
- `schemas/readiness-envelope.v1.schema.json`
- `schemas/record-ref.v1.schema.json`
- `schemas/evidence-ref.v1.schema.json`
- `schemas/watch-event.v1.schema.json`

Findings:
- Core envelope/ref schemas are syntactically valid and coherent for current phases.
- No immediate schema blocker for existing operations.
- Controlled-action contract implications exist (section 9), but adding `controlled-action-*` schema now is premature for 2A.

## 7. OpenAPI projection gaps

- `openapi/yai-api.v1.yaml` is explicitly declared subset projection (`openapi/README.md` confirms this).
- Major operation IDs are present.
- Gap: subset includes operations still planned in runtime; without a linked readiness semantic, consumer interpretation may over-assume runtime availability.
- Recommendation: Phase 2B annotate/readiness-link operation subset entries (doc + conformance check), not full OpenAPI expansion.

## 8. Conformance gaps

Current checks catch major forbidden grammar, but do not yet enforce:
- no public `flow` or root `records` plane entries in plane/surface registries;
- no `orchestration` public naming drift where `orchestrator` is intended;
- readiness parity cross-check with `yai` runtime readiness source.

These are **P1** conformance enhancements for next phase.

## 9. Controlled-action future API contract implications

Current state:
- Controlled-action is internal runtime posture (`yai` Phase 1B/1D), not API contract.

Implications for API:
- Future API should likely introduce a minimal action posture ref/envelope only when runtime threading is stable and semantics are proven.
- Do not expose internal posture markers as durable refs.
- No schema addition in 2A; capture as proposal input for Phase 2C.

## 10. Recommended Phase 2B changes

1. Clean plane/surface registries to canonical public names:
- remove public `flow` plane/surface exposure (map to `workflow`)
- remove public root `records` exposure (map to `state.records` only)
- normalize `orchestration` -> `orchestrator` in public-facing registries/docs

2. Reconcile API `runtime_handler_readiness` metadata for:
- `case.records.tail`
- `state.records.tail`
- `workflow.runs.watch`
- `control.gates.list`

3. Add conformance checks for:
- forbidden public plane/surface drift (`flow`, root `records`, `orchestration` as public)
- readiness mismatch policy (at least an allowlist/exception file until automated cross-repo check exists)

4. Keep OpenAPI subset as projection and add explicit readiness interpretation notes.

## 11. Impact on SDK/CLI/Loom phases

- SDK Phase 3 typed gate should not hard-code legacy public `flow` or root `records` surfaces.
- CLI Phase 4 Rust migration should consume canonical API names only (`workflow`, `control`, `state.records`, `orchestrator`).
- Loom Phase 5 should treat planned operations as non-executable unless readiness confirms otherwise.

---

## Priority classification

### P0 blockers (before API can be reliable source-of-truth for public naming)
- Public plane/surface drift: `flow`, root `records`.

### P1 blockers (before SDK typed surface hardening)
- Readiness metadata mismatch (4 operations).
- Missing conformance checks for plane/surface canonical naming.
- `orchestration` vs `orchestrator` normalization in public registries/docs.

### P2 compat/transitional
- Broad planned-operation presence in registry/OpenAPI subset with partial implementation in runtime.

### P3 historical/docs only
- Legacy compatibility wording in older family/readme references where no public contract claim is made.
