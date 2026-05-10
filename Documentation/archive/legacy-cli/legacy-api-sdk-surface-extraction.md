# Legacy API/SDK Surface Extraction

## Status

* Delivery: V21.4
* Status: active extraction artifact
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Extract API/SDK-worthy surface candidates from quarantined `cli/source/`.

## Extraction Principle

```text
Do not preserve legacy C command implementation.
Preserve only useful API/SDK surface shapes in the correct architectural layer.
```

## Candidate Categories

* `api_operation_candidate`
* `api_schema_candidate`
* `api_read_model_candidate`
* `sdk_client_candidate`
* `sdk_type_candidate`
* `sdk_transport_candidate`
* `runtime_gate_candidate`
* `case_surface_candidate`
* `records_evidence_surface_candidate`
* `knowledge_surface_candidate`
* `provider_surface_candidate`
* `agent_surface_candidate`
* `flow_surface_candidate`
* `analytics_surface_candidate`
* `legacy_session_surface`
* `remove_without_extraction`
* `unknown_needs_followup`

## Source Areas Reviewed

| Source area | Legacy role |
| ----------- | ----------- |
| `source/cmd/runtime` | runtime status and legacy runtime family wrappers |
| `source/cmd/provider` | provider list/status/current/select/connect/probe/models/doctor wrappers |
| `source/cmd/agent` | agent entry grammar and runtime-layout seeding |
| `source/cmd/flow` | workflow/orchestration snapshot, pending, gate, blocker, and reconcile vocabulary |
| `source/cmd/govern` | governance intake/legal/authority/review/publication family |
| `source/cmd/knowledge` | knowledge query, lineage, context, memory, retrieval, topology, and records/read-model families |
| `source/cmd/analytics` | analytics summary/query/show wrapper family |
| `source/cmd/logs` | logs latest over canonical `operational_receipt` tails |
| `source/cmd/case` | case facts/runtime/watch/gui summaries and case-bound readiness/read-model surfaces |
| `source/cmd/session` | legacy session summary/status/welcome/substrate entry compatibility |
| `source/out` | output stubs for json/text/table/tsv/shell |
| `source/shared` | CLI passthrough/path/help helpers |

## Surface Candidate Table

| Legacy area | Candidate surfaces | Candidate category | Target owner | Future wave | Deletion readiness |
| ----------- | ------------------ | ------------------ | ------------ | ----------- | ------------------ |
| `source/cmd/runtime` | `runtime status` and `runtime overview` map to lifecycle/health/readiness status plus future case-bound runtime inspect/readiness reasons | `api_operation_candidate`, `api_read_model_candidate`, `sdk_client_candidate`, `sdk_type_candidate`, `runtime_gate_candidate` | `api` + `sdk` + `yai/core` | V41, V47, V58 | partial |
| `source/cmd/provider` | provider `list`, `status`, `current`, `select`, `view`, `connect`, `disconnect`, `probe`, `models`, `set`, `doctor` | `provider_surface_candidate`, `api_operation_candidate`, `sdk_client_candidate`, `sdk_type_candidate` | `api` + `sdk` + `yai/core` | V31, V37, V47, V50 | partial |
| `source/cmd/agent` | scope/actor/agent/provider/input run grammar, agent role vocabulary, agent trace/run posture | `agent_surface_candidate`, `api_operation_candidate`, `sdk_client_candidate`, `sdk_type_candidate` | `api` + `sdk` + `yai/core` | V32, V47, V58 | partial |
| `source/cmd/flow` | workflow snapshot, steps pending, runs watch, gate/blocker/explain/reconcile read models | `flow_surface_candidate`, `api_operation_candidate`, `api_read_model_candidate`, `sdk_client_candidate`, `sdk_type_candidate`, `runtime_gate_candidate` | `api` + `sdk` + `yai/core` | V33, V47, V58 | partial |
| `source/cmd/govern` | intake, legal, authority, review, publication, posture, dossier, gate explanation surfaces | `api_operation_candidate`, `api_read_model_candidate`, `sdk_client_candidate`, `sdk_type_candidate`, `runtime_gate_candidate` | `api` + `sdk` + `yai/core` | V44, V45, V47 | partial |
| `source/cmd/knowledge` | query, lineage, topology, context, memory, retrieval, inference, summarize, maintenance, records/read-model catalog families | `knowledge_surface_candidate`, `api_operation_candidate`, `api_read_model_candidate`, `sdk_client_candidate`, `sdk_type_candidate`, `records_evidence_surface_candidate` | `api` + `sdk` + `yai/core` | V29, V30, V49, V58 | partial |
| `source/cmd/analytics` | analytics `summary`, `query`, `show`, `emit-summary` | `analytics_surface_candidate`, `api_operation_candidate`, `sdk_client_candidate`, `sdk_type_candidate` | `api` + `sdk` + `yai/core` | V34, V58 | partial |
| `source/cmd/logs` | `logs latest` over canonical `operational_receipt` tails with `scope`, `limit`, `receipts_available`, `reason` | `records_evidence_surface_candidate`, `api_operation_candidate`, `api_read_model_candidate`, `sdk_client_candidate`, `sdk_type_candidate` | `api` + `sdk` + `yai/core` | V29, V47, V58 | partial |
| `source/cmd/case` | case `facts`, case-bound `runtime`, case-bound `watch`, gui summaries, process/evidence summaries, readiness snapshots | `case_surface_candidate`, `api_operation_candidate`, `api_read_model_candidate`, `sdk_client_candidate`, `sdk_type_candidate`, `runtime_gate_candidate`, `records_evidence_surface_candidate` | `api` + `sdk` + `cli` + `yai/core` | V42, V47, V49, V58 | partial |
| `source/cmd/session` | `session status`, `session summary`, `session attach`, substrate entry bootstrap, shell landing render hooks | `legacy_session_surface` | `api` + `Documentation/remove` + `cli` | V43, V51, V53, V54, V55 | partial |
| `source/out` | no durable domain model; stub emitter signatures only | `remove_without_extraction` | `cli` | V21.5 | partial |
| `source/shared` | no SDK transport canon; only legacy CLI passthrough/path/help glue | `remove_without_extraction` | `cli` | V21.5 | partial |

## API Candidate Summary

| Candidate | Source | Proposed API surface | Notes |
| --------- | ------ | -------------------- | ----- |
| runtime posture and inspect | `source/cmd/runtime/status.c`, `source/cmd/case/surface.c` | `system.status`, `system.runtime.inspect`, future `case.runtime.inspect` | Preserve lifecycle/health/readiness and case-bound runtime snapshot vocabulary without preserving legacy `start`/`stop` grammar |
| provider family | `source/cmd/provider/*.c`, `source/cmd/models/surface.c` | `providers.list`, `providers.probe`, future `providers.status`, `providers.current`, `providers.select`, `providers.connect`, `providers.models`, `models.list`, `models.capabilities.show` | Thin wrappers are disposable; operation names and request shapes are the useful artifact |
| agent family | `source/cmd/agent/root.c`, `source/cmd/flow/surface.c` | `agents.list`, `agents.trace`, future `agents.run` / `agents.invoke` | Legacy flags suggest a typed request with `scope`, `actor`, `agent`, `provider`, and `input` |
| workflow family | `source/cmd/flow/root.c`, `source/cmd/flow/surface.c` | `workflow.list`, `workflow.show`, `workflow.steps.pending`, `workflow.runs.watch`, future reconcile/blocker/gate summaries | The large legacy surface mainly contributes read-model and explain vocabulary |
| governance family | `source/cmd/govern/*.c`, `source/cmd/flow/surface.c` | `governance.posture`, `governance.policy.resolve`, future `governance.review.dossier`, `governance.intake.submit` | Keep posture/review/legal surface names, not session-gated CLI behavior |
| knowledge and records family | `source/cmd/knowledge/*.c`, `source/cmd/logs/root.c` | `knowledge.query`, `knowledge.lineage.trace`, `state.records.query`, `state.records.tail`, future `knowledge.context.show`, `knowledge.memory.show`, `records.operational_receipts.tail` | `records.c` is the strongest read-model catalog artifact in the legacy tree |
| case read models | `source/cmd/case/surface.c` | `case.current`, `case.list`, `case.show`, `case.records.tail`, future `case.facts.show`, `case.watch.show`, gui summary projections | Legacy case surface suggests transport-visible snapshots, not CLI-owned truth |
| analytics family | `source/cmd/analytics/query.c`, `source/cmd/knowledge/records.c` | `analytics.query`, future `analytics.show` and derived summaries | Analytics remains derived and must not become authority |

## SDK Candidate Summary

| Candidate | Source | Proposed SDK surface | Notes |
| --------- | ------ | -------------------- | ----- |
| runtime status and case-bound runtime inspect | `source/cmd/runtime/status.c`, `source/cmd/case/surface.c` | `client.system().status()`, `client.runtime().status_inspect()`, future typed `case.runtimeInspect()` | SDK owns the typed request/response and unavailable transport truth, not service execution |
| provider and model family | `source/cmd/provider/*.c`, `source/cmd/models/surface.c` | `client.providers().list()`, `probe()`, future `status()`, `current()`, `select()`, `connect()`, `models()` and `client.models().list()/capabilitiesShow()` | Useful extraction is family grouping and request naming, not wrapper code |
| agent client family | `source/cmd/agent/root.c` | future `client.agents()` / `client.agent()` typed run/trace methods | Preserve typed request fields for scope, actor, agent, provider, and input |
| workflow client family | `source/cmd/flow/surface.c` | `client.workflow().list()/show()/stepsPending()/runsWatch()`, future snapshot/blocker/reconcile helpers | Legacy flow surface mostly suggests typed envelopes and read models |
| governance and control family | `source/cmd/govern/*.c`, `source/cmd/flow/surface.c` | `client.governance()`, `client.control()` future dossier/posture/explain methods | Gate, review, and allowed/blocked reason types belong here, not in CLI |
| knowledge and records family | `source/cmd/knowledge/*.c`, `source/cmd/logs/root.c` | `client.knowledge()`, `client.records()`, `client.state()` future typed catalog/tail/query methods | Operational receipts and read-model families should be typed SDK projections |
| case watch/facts summaries | `source/cmd/case/surface.c` | future `client.case().watchSnapshot()/facts()/runtimeInspect()` typed methods | Session-like watch/session fields stay compatibility-only; case-bound summaries are the durable artifact |
| session compatibility only | `source/cmd/session/*.c` | compatibility/deprecation docs, not new canonical SDK family growth | `session` remains a removal/deprecation surface, not a destination for new typed clients |

## Session Candidate Treatment

```text
Session-like legacy surfaces are not API/SDK canon.
They may become compatibility/deprecation docs only, or be removed.
```

## Deletion Readiness

| Legacy area | Deletion readiness | Blocking reason |
| ----------- | ------------------ | --------------- |
| `source/cmd/runtime` | partial | runtime posture vocabulary is preserved, but broader build references and legacy `runtime` family wrappers still exist |
| `source/cmd/provider` | partial | operation names and typed request families are preserved, but wrappers remain until deletion pass |
| `source/cmd/agent` | partial | agent request grammar is preserved, but deletion still depends on broader build cleanup |
| `source/cmd/flow` | partial | read-model/gate/blocker/reconcile vocabulary is preserved, but the legacy surface is still large and broader build references remain |
| `source/cmd/govern` | partial | governance surface shapes are preserved, but session contamination and build cleanup remain |
| `source/cmd/knowledge` | partial | knowledge/read-model families are preserved in docs, but `records.c` still sits in the legacy tree until deletion |
| `source/cmd/analytics` | partial | thin query/show family preserved, but subtree still participates in broader legacy build references |
| `source/cmd/logs` | partial | `operational_receipt` tail semantics are preserved, but transport-facing record surfaces are not implemented here |
| `source/cmd/case` | partial | case facts/runtime/watch summaries are documented, but the large legacy case surface remains in place |
| `source/cmd/session` | partial | classified as legacy compatibility only, but explicit removal/deprecation waves still remain |
| `source/out` | partial | no preserved API/SDK semantics needed, but subtree still exists until deletion pass |
| `source/shared` | partial | no preserved API/SDK semantics needed, but subtree still exists until deletion pass |
