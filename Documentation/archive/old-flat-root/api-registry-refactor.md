# API Registry Refactor

## Status

* Delivery: V51
* Branch: `refoundation/phase-01`
* Registry source: `api/registry`
* Action source: `api/registry/yai-actions.v1.json`

## Purpose

V51 aligns the API registry with the action_id command system so the registry
stops preserving stale command families as canonical truth and instead becomes
the canonical operation/projection layer for CLI, TUI, SDK, and runtime-facing
work.

## Non-goals

* no CLI implementation
* no SDK generation
* no runtime behavior
* no endpoint/server implementation
* no protocol cutover

## Registry Principles

```text
API registry is operation/projection canon.
API registry is not runtime truth.
API registry must not preserve session as canonical domain.
API registry must distinguish API family names from CLI/TUI projection names.
API registry must expose legacy/deprecated/forbidden status explicitly.
```

## Family Decisions

| Concept | Canonical API family | CLI/TUI projection | Legacy alias | Decision |
| ------- | -------------------- | ------------------ | ------------ | -------- |
| `session` | `session` | `session-legacy` | `session` | Kept only as legacy/deprecated compatibility family. |
| `flow/workflow` | `workflow` | `workflow` | `flow` | `workflow` is canonical; `flow` is legacy alias only. |
| `records/state.records` | `state` with `state.records.*` | `records` or `state records` | root `records.*` | Root `records` is not canonical; `state.records.*` is canonical. |
| `providers/provider` | `providers` | `provider` | none | API remains plural; CLI/TUI may stay singular. |
| `models/model` | `models` | `model` | CLI plural `models.*` | API remains plural; CLI/TUI may project singular while plural CLI remains compatibility. |
| `agents/agent` | `agents` | `agent` | none | API remains plural; CLI/TUI may stay singular. |
| `policy_pack/policy-pack` | `policy_pack` | `policy-pack` | root `policy` forbidden | Canonical API family uses underscore; root `policy` is forbidden. |
| `materialization/materialize` | `materialization` | `materialize` | none | Canonical API family is noun-based; CLI/TUI may use verb projection. |
| `intake` | `intake` | `intake` | none | New first-class family in V51. |
| `lineage` | `lineage` | `lineage` | `knowledge.lineage.*` | Lineage becomes first-class; nested knowledge lineage remains compatibility-only where retained. |
| `evidence` | `evidence` | `evidence` | `control.evidence.*` | Evidence becomes first-class; control-owned evidence projection remains compatibility-only where retained. |
| `query` | no root family | scoped query/recall | `query.root` | Root query is forbidden; use `recall.query` or family-local query surfaces. |
| `inspect` | no root family | family-local inspect | `inspect.root` | Root inspect is forbidden; use family-local inspect operations only. |
| `logs` | `logs` | `logs` | generic root logs owner forbidden | Logs is scoped only to runtime/job/workflow/agent/provider. |
| runtime control | no runtime lifecycle family | none | `runtime.start/stop/restart` | Runtime lifecycle remains forbidden as a canonical domain API surface. |

## Operation Additions / Changes

| Operation | Source action_id | Registry status | Notes |
| --------- | ---------------- | --------------- | ----- |
| `system.readiness` | `system.readiness` | added | Adds explicit readiness projection without creating runtime lifecycle control. |
| `workflow.status`, `workflow.inspect`, `workflow.plan`, `workflow.runs.stop`, `workflow.outputs.show`, `workflow.evidence.show`, `workflow.lineage.trace` | `workflow.status`, `workflow.inspect`, `workflow.run`, `workflow.stop`, `workflow.outputs`, `workflow.evidence`, `workflow.lineage` | added | Keeps `workflow` canonical and deepens lifecycle beyond list/watch only. |
| `policy_pack.list`, `policy_pack.inspect`, `policy_pack.validate`, `policy_pack.explain` | `policy_pack.*` | added | Restores explicit policy-pack family and blocks root `policy`. |
| `intake.plan`, `intake.run`, `intake.status`, `intake.inspect`, `intake.validate`, `intake.outputs.show`, `intake.lineage.trace` | `intake.*` | added | Makes intake first-class instead of burying it under knowledge or query. |
| `materialization.plan`, `materialization.run`, `materialization.status`, `materialization.inspect`, `materialization.validate`, `materialization.outputs.show`, `materialization.evidence.show`, `materialization.lineage.trace` | `materialize.*` | added | Canonical API family uses `materialization` while CLI/TUI may project `materialize`. |
| `excerpt.list`, `excerpt.show`, `excerpt.inspect`, `excerpt.lineage.trace` | `excerpt.*` | added | Restores excerpt as a governed case-bound output family. |
| `evidence.list`, `evidence.show`, `evidence.inspect`, `evidence.lineage.trace` | `evidence.*` | added | Promotes evidence to first-class API family. |
| `lineage.trace`, `lineage.show`, `lineage.explain`, `lineage.graph.show` | `lineage.*` | added | Promotes lineage to first-class API family. |
| `recall.query`, `recall.explain`, `recall.inspect` | `recall.*` | added | Restores governed recall as distinct from root query. |
| `knowledge.status`, `knowledge.list`, `knowledge.show`, `knowledge.inspect`, `knowledge.rebuild.plan`, `knowledge.rebuild` | `knowledge.*` | added | Deepens knowledge lifecycle without making knowledge the only owner of lineage/recall. |
| `state.status`, `state.list`, `state.inspect`, `state.projections.show`, `state.materialized.show`, `state.substrate.status`, `state.substrate.inspect.*` | `state.*` | added | Makes state richer while keeping substrate inspection diagnostic and scoped. |
| `providers.inspect`, `providers.capabilities.show`, `providers.config.status`, `providers.routes.explain`, `providers.calls.*` | `provider.*` | added | Keeps plural API family while restoring lifecycle depth for provider capability work. |
| `models.status`, `models.inspect`, `models.check`, `models.routes.explain`, `models.runs.*` | `model.*` | added | Keeps plural API family while restoring lifecycle depth for models. |
| `agents.status`, `agents.inspect`, `agents.cancel`, `agents.logs.watch`, `agents.outputs.show`, `agents.evidence.show`, `agents.lineage.trace` | `agent.*` | added | Keeps plural API family while restoring agent lifecycle depth. |
| `job.list`, `job.status`, `job.inspect`, `job.plan`, `job.start`, `job.cancel`, `job.logs.watch`, `job.outputs.show`, `job.evidence.show`, `job.lineage.trace` | `job.*` | added | Promotes jobs from under-modeled runtime concept to first-class API family. |
| `license.status`, `license.lease.status`, `license.check`, `license.cache.status` | `license.*` | added | Creates explicit license posture family distinct from billing or session meaning. |
| `machine.status`, `machine.identity.status`, `machine.evidence.status`, `machine.authorization.status`, `machine.enroll` | `machine.*` | added | Creates explicit machine posture family without exposing raw machine identity. |
| `limits.status`, `limits.explain` | `limits.*` | added | Adds safe limits projection family. |
| `logs.runtime.watch`, `logs.job.watch`, `logs.workflow.watch`, `logs.agent.watch`, `logs.provider.watch` | `logs.*` | added | Makes logs scoped and explicit instead of generic root ownership. |

## Deprecated / Legacy Operations

| Operation | Status | Replacement | Notes |
| --------- | ------ | ----------- | ----- |
| `session.attach` | legacy | none single | Replacement meaning is split across auth, case/context, client/shell, and system surfaces. |
| `session.current` | legacy | none single | Session is not canonical domain truth after V51. |
| `session.detach` | legacy | none single | Session detach remains compatibility only. |
| `session.status` | legacy | `system.status` and `auth.status` split | Retained only as compatibility surface. |
| `knowledge.lineage.trace` | legacy | `lineage.trace` | Retained while lineage becomes first-class. |
| `control.evidence.show` | legacy | `evidence.show` | Retained while evidence becomes first-class. |

## Forbidden Operations

| Operation or root | Status | Replacement |
| ----------------- | ------ | ----------- |
| `runtime.start` | forbidden | none |
| `runtime.stop` | forbidden | none |
| `runtime.restart` | forbidden | none |
| `query.root` | forbidden | `recall.query` or family-local query surfaces |
| `inspect.root` | forbidden | family-local inspect operations |
| `policy.root` | forbidden | `policy_pack.*` or `governance.policy.resolve` |
| `substrate.inspect.raw` | forbidden | `state.substrate.inspect.*` diagnostic projections only |

## Projection Alignment

V51 keeps the projection chain explicit:

```text
action_id
  -> API family / operation
  -> CLI/TUI projection name
  -> SDK surface candidate
  -> runtime action key candidate
```

Alignment rules in V51:

* `yai-actions.v1.json` remains the seeded action source.
* `api-operation-projections.v1.json` now records family projection rules, legacy alias mappings, and forbidden action locks.
* API family names may differ from CLI/TUI names:
  * `providers` -> `provider`
  * `models` -> `model`
  * `agents` -> `agent`
  * `policy_pack` -> `policy-pack`
  * `materialization` -> `materialize`
* V51 does not try to fully resync every `none verified` action metadata row in `yai-actions.v1.json`; that drift is now explicit instead of hidden.

## V52+ Handoff

* V52 — API Case Expansion
* V53 — API Auth Surfaces
* V54 — API Operator Context
* V55 — Entitlement
* V56 — Machine Authorization
* V57 — Runtime Gate Decision

V51 deliberately stops at registry canon and conformance. It does not implement
CLI, SDK, runtime, endpoint, or protocol cutover behavior.
