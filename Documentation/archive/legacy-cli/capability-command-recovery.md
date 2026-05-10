# Capability Command Recovery

## Status

* Delivery: V50.8
* Track: V — CLI/API/SDK/runtime command canon
* Branch: `refoundation/phase-01`
* Depends on:
  - `canonical-yai-command-system.md`
  - `cli-tui-command-projection-contract.md`

## Purpose

Recover the full command lifecycle for operational capability families that
were flattened or under-modeled during the session/session-removal and
`cli/source` deletion work.

## Problem Statement

V50.5, V50.6, and V50.7 preserved the command-system boundary correctly, but
they left several operational families too shallow:

* `provider` reduced to list/status readiness language
* `model` reduced to list/status capability language
* `agent` reduced to placeholder or spawn wording
* `workflow` / `flow` reduced to naming cleanup and partial readiness
* `job` reduced to boundary-only ownership language
* `skills` reduced to list/inspect-only vocabulary
* `materialize` and `intake` only recently restored
* `knowledge`, `state`, `lineage`, `records`, and `evidence` not given full
  lifecycle depth
* `query`, `inspect`, and `logs` left too vague as root commands
* runtime/system diagnostics modeled mostly as readiness projection

Repo reality is richer than that shallow picture:

* `sdk/packages/typescript/src/operations.ts` already exposes
  `providers.probe`, `workflow.steps.pending`, `workflow.runs.watch`,
  `state.records.query`, `state.records.tail`, `knowledge.query`, and
  `knowledge.lineage.trace`.
* `yai/Documentation/architecture/controlled-act-lifecycle.md` already defines
  a governed execution spine from `operation` through `evidence_event`,
  `state_transition`, and `orchestration_outcome`.
* `yai/include/orchestration/flow.h` already models step, transition, review,
  gating, snapshot, composition, control, progress, and operation records.
* `yai/state/materialization/materialize_runtime.c` and
  `Documentation/audits/wave-13a-state-materialization-direct-cut.md` already
  establish `state/materialization` as a dedicated runtime/materialization
  owner separate from `state/records`.
* `cli/MIGRATION_MAP.md` and `cli/src/sdk/runtime.rs` confirm that the current
  Rust CLI only projects a narrow subset of the deeper API/SDK/runtime shape.

## Capability Lifecycle Vocabulary

| Stage | Meaning |
| ----- | ------- |
| `catalog` | list, enumerate, or discover the family surface or candidate set |
| `status` | summarize readiness, posture, or current high-level state |
| `inspect` | show detail, metadata, or record-level shape |
| `check` | probe, validate, or test availability/admissibility without full execution |
| `configure` | inspect or request configuration posture without exposing secrets or private substrate |
| `plan` | dry-run, explain, or construct an execution/materialization plan before side effects |
| `run` | request governed execution or materialization |
| `watch` | follow progress, streaming, logs, or evolving status |
| `outputs` | expose result posture or produced artifacts safely |
| `evidence` | surface case-bound evidence or record consequences |
| `lineage` | trace derivation, relationship, or provenance links |
| `cancel` | stop, cancel, pause, or revoke the running action where that makes sense |
| `explain` | explain gates, blocked posture, control decision, or runtime reason |

Lifecycle rules:

* `catalog` is not `inspect`.
* `inspect` is not `check`.
* `check` is not `run`.
* `plan` is not `run`.
* `watch` is not `outputs`.
* `outputs` are not ownership.
* `evidence` and `lineage` are first-class aftermath stages for governed work.
* `cancel` belongs only where a family actually governs continuity.
* `explain` belongs across families through `control`, runtime gates, and safe
  posture surfaces.

## Recovery Rules

```text
Readiness/status/list is not enough.
Every operational capability family must be classified across the full
lifecycle even if some stages remain planned, diagnostic-only, or
runtime-internal.
Public CLI is only one projection of that lifecycle.
TUI may show unavailable lifecycle stages, but it must not invent them.
API/SDK/runtime may own deeper stages before CLI/TUI expose them.
```

Practical consequence:

* a family may be canonically deep even when current Rust CLI exposes only one
  or two commands
* a lifecycle stage may be `runtime_internal` or `derived_via_other_family`
  rather than a public root command
* `query`, `inspect`, and `logs` must be recovered by scoping them, not by
  reviving them as vague catch-all roots
* V50.9 should carry these recovered lifecycle stages into the canonical
  `action_id` registry seed rather than leaving them as prose only

## Backend Surface Rehydration Findings

| Surface cluster | Verified repo anchors | Recovery consequence |
| --------------- | --------------------- | -------------------- |
| provider/model access | `api/Documentation/execution/provider-authority-binding.md`, `api/Documentation/execution/local-model-provider-access-boundary.md`, `sdk/packages/typescript/src/operations.ts` | provider/model families must include inspect/check/run/gate depth, not only list/status |
| agent/workflow/job governed execution | `api/Documentation/execution/agent-authority-binding.md`, `api/Documentation/execution/flow-binding.md`, `api/Documentation/execution/case-bound-jobs.md`, `api/Documentation/execution/execution-lease-model.md`, `yai/Documentation/architecture/controlled-act-lifecycle.md` | execution families must include run/watch/evidence/lineage/cancel/explain stages |
| workflow internal backing | `yai/include/orchestration/flow.h`, `yai/Documentation/architecture/workflow-readiness-pending-runs-wave-20D.md`, `sdk/packages/typescript/src/surfaces/workflow.ts` | public `workflow` grammar has real backend depth even where runtime watch is still planned |
| state/materialization/records | `yai/state/materialization/materialize_runtime.c`, `yai/Documentation/audits/wave-13a-state-materialization-direct-cut.md`, `sdk/packages/typescript/src/surfaces/state.ts` | `state`, `materialize`, and `records` require plan/run/watch/outputs separation |
| knowledge/lineage/evidence | `api/Documentation/execution/knowledge-binding.md`, `api/Documentation/execution/case-evidence-binding.md`, `sdk/packages/typescript/src/surfaces/knowledge.ts` | knowledge/evidence are not passive stores; they have inspect, recall/query, lineage, and write/materialization aftermath |
| analytics/logs/runtime gates | `api/Documentation/execution/analytics-binding.md`, `api/Documentation/execution/runtime-gate-registry.md`, `api/Documentation/runtime/runtime-readiness-projection.md` | diagnostics must distinguish status, inspect, watch/logs, evidence, and gate explanation |
| current Rust CLI shallowness | `cli/MIGRATION_MAP.md`, `cli/src/sdk/runtime.rs` | current CLI exposes only a thin slice and must not be mistaken for canonical lifecycle depth |

## Capability Lifecycle Recovery Matrix

### Provider / Model / Skills

| Family | catalog | status | inspect | check | configure | plan | run | watch | outputs | evidence | lineage | cancel | explain |
| ------ | ------- | ------ | ------- | ----- | --------- | ---- | --- | ----- | ------- | -------- | ------- | ------ | ------- |
| `provider` | `provider list` public target; current CLI only has `list` | `provider status` planned | `provider inspect <provider>` target | `providers.probe` verified in SDK/API direction | config posture only; no raw secrets or billing objects | via `control explain` and governed admission, not provider-root planning | `provider.call` is backend/runtime-governed, not a shallow root command | follow through `job`/`workflow`/scoped logs, not a provider-root watch loop | result posture only; provider output does not own truth | `provider_response` becomes case evidence | lineage via evidence/knowledge refs and `lineage` surfaces | stop/cancel lives under job/workflow/control, not provider root | gate/control explanation required for provider admission |
| `model` | `model list` public target | `model status` target | `model inspect <model>` target | `models.capabilities.show` verified; `model check` target | access-mode and credential posture only; no secret exposure | via control/materialize/workflow planning, not model-root ownership | local/hosted/custom invoke remains governed runtime action, not a free root shortcut | follow through `job`, `workflow`, or logs, not a model-root stream claim | output posture only; results become evidence/knowledge candidates | evidence via job/provider/runtime capture | lineage through evidence/knowledge/lineage refs | stop/cancel belongs to job/workflow/control | explain through control + machine/license/gate posture |
| `skills` | `skills list` target | `skills status` target | `skills inspect <skill>` target | admissibility/routing/registry check is diagnostic-only today | registry/routing posture only; not arbitrary mutation | route/selection planning belongs here conceptually | runtime skill execution remains governed/internal | watch through agent/job/workflow/log surfaces | outputs are governed downstream artifacts, not root skill ownership | skill results may emit evidence | lineage through controlled-act/state/lineage chain | cancel via agent/job/workflow, not root skill | explain via control/routing/admissibility posture |

### Agent / Workflow / Job

| Family | catalog | status | inspect | check | configure | plan | run | watch | outputs | evidence | lineage | cancel | explain |
| ------ | ------- | ------ | ------- | ----- | --------- | ---- | --- | ----- | ------- | -------- | ------- | ------ | ------- |
| `agent` | `agent list` target; SDK/API already expose `agents.list` | `agent status <agent>` target | `agent inspect <agent>` target | `agents.trace` proves deeper traceability than spawn-only wording | role/admission posture only | delegation and governed planning are part of the family | `agent spawn/resume/delegate` are target run actions | watch through agent/job/workflow state and logs | outputs become evidence/knowledge candidates, not agent-owned truth | evidence write is a governed downstream stage | lineage should trace agent -> provider/tool -> evidence/knowledge | `agent stop/pause` belongs here | explain via control decision and agent authority posture |
| `workflow` | `workflow list` canonical target; internal `flow/*` stays backend | `workflow status/show` canonical target | `workflow inspect <workflow>` target | `workflow.steps.pending` and `workflow.runs.watch` are verified lifecycle stages | definition/binding/gating posture exists in backend records | workflow planning and step planning are core to the family | `workflow run/start` is canonical run surface | `workflow.runs.watch` is verified as real target even where runtime wiring stays partial | outputs are coordinated case-bound outcomes, not workflow-owned truth | workflows may write evidence via governed steps | lineage must connect workflow, job, agent, provider, evidence, and knowledge | `workflow stop/cancel` belongs here | explain via flow/control/gating posture |
| `job` | `job list` target | `job status <job>` target | `job inspect <job>` target | `execution_lease` and admission posture make check a real slice | execution continuity/admission context belongs here | spec validation and dry-run planning belong here | `job start <spec>` target | `job logs <job>` and future watch loops belong here | results/outputs are first-class | `job_output` evidence is explicit in evidence binding | lineage must connect job -> evidence -> state -> knowledge | `job cancel <job>` belongs here | explain via case/gate/license/machine/limit posture |

### Intake / Materialize

| Family | catalog | status | inspect | check | configure | plan | run | watch | outputs | evidence | lineage | cancel | explain |
| ------ | ------- | ------ | ------- | ----- | --------- | ---- | --- | ----- | ------- | -------- | ------- | ------ | ------- |
| `intake` | `intake` must enumerate planned/running/known intake refs, not just exist as a noun | `intake status <intake>` target | `intake inspect <intake>` target | `intake validate <source>` target | `--case`, `--policy-pack`, and profile posture are part of intake setup | `intake plan <source>` is canonical | `intake run <source>` is canonical | watch/status/logs are part of long-running intake | outputs are candidate material, not direct knowledge | evidence/records may be produced during intake | lineage must connect source -> intake -> materialize | cancel belongs here if intake becomes long-running | explain via policy-pack/control/materialization prerequisites |
| `materialize` | enumerate plans/runs/known outputs as a first-class family | `materialize status <run>` target | `materialize inspect <run>` target | `materialize validate <plan>` target | profile/policy/runtime posture belongs here | `materialize plan <input>` is canonical | `materialize run <plan>` is canonical | status/logs/watch are part of the family | `materialize outputs <run>` is required | records/evidence are direct aftermath, not optional side notes | lineage must connect intake/policy pack -> records/evidence/knowledge/state | cancel/stop may route through job/workflow/runtime once implemented | explain via control, policy-pack, gate, and readiness posture |

### Knowledge / State / Lineage / Records / Evidence

| Family | catalog | status | inspect | check | configure | plan | run | watch | outputs | evidence | lineage | cancel | explain |
| ------ | ------- | ------ | ------- | ----- | --------- | ---- | --- | ----- | ------- | -------- | ------- | ------ | ------- |
| `knowledge` | `knowledge list` target | `knowledge status` target | `knowledge show/inspect` target | freshness/derivation/recall posture checks belong here | recall/write/visibility posture belongs here | knowledge proposal/materialization planning is real | writes/rebuilds are governed and not trivial root mutators | watch/rebuild progress is future but meaningful | outputs are readable knowledge items and governed query results | knowledge derives from evidence/records/jobs/provider calls | lineage is intrinsic; `knowledge.lineage.trace` already exists | cancel is only meaningful for rebuild/materialization flows | explain via recall/write policy and control posture |
| `state` | `state list/materialized/projections` target | `state status` target | `state inspect <ref>` target | substrate/projection health checks are real diagnostics | projection/substrate posture belongs here | state planning happens through materialization and records policy | writes are runtime/state internal, not raw public mutation | `state records tail` is already verified as a watch-class slice | outputs are materialized state and derived projections | records/evidence are source material for state | lineage should connect state transitions to upstream/downstream refs | cancel is not a root state concern | explain via state/control/readiness posture |
| `lineage` | lineage discovery/index surfaces are target diagnostic roots | lineage availability/status is diagnostic | `lineage show/explain/trace` are core | graph/backend diagnostic checks belong here | backend posture only; no raw graph mutation CLI | lineage rebuild planning is internal/future | lineage materialization is runtime/internal | graph/watch surfaces remain future diagnostics | outputs are traces, graphs, and explanations | lineage links evidence/records/knowledge/jobs/flows/agents/providers/models | lineage is the family itself | cancel is usually not a root concern | explain is a primary lineage function |
| `records` | root `records list` is compatibility only; canonical ownership converges under `state` | status is via `state` and record-tail posture | `records show/inspect` remains transitional | `state.records.query` and `state.records.tail` are verified slices | retention/projection posture belongs under `state` | planning belongs under `materialize`/`state` | writes are runtime/state internal | tail/watch is already a real lifecycle slice | outputs are record bodies and projections | records link directly into evidence and state transitions | lineage comes from linked refs | cancel is not a root records concern | explain via `state`/`control`, not root `records` |
| `evidence` | `evidence list` target | evidence posture/status is diagnostic-only | `evidence show/inspect` target | evidence lineage and visibility checks belong here | visibility/retention posture belongs here | planning belongs through control/materialize/workflow | `write_evidence` is governed runtime/internal | watch can surface evidence growth and log excerpts | outputs are evidence items | evidence is the family itself | lineage is first-class through `evidence lineage` and linked refs | cancel is not a root evidence concern | explain via control/runtime decision context |

### Query / Logs / Runtime-System Diagnostics

| Family | catalog | status | inspect | check | configure | plan | run | watch | outputs | evidence | lineage | cancel | explain |
| ------ | ------- | ------ | ------- | ----- | --------- | ---- | --- | ----- | ------- | -------- | ------- | ------ | ------- |
| `query` | bare root query has no safe catalog | no standalone root status | root inspect is forbidden | root check is forbidden | no root configure | no root plan | bare `yai query` remains forbidden | no root watch | outputs must come from scoped families only | evidence comes from scoped families only | lineage comes from scoped families only | n/a | recover query by splitting into `recall`, `knowledge`, `state records`, and `evidence` scopes |
| `logs` | scoped logs families should be enumerated | log-source availability is diagnostic | `logs runtime/job/workflow/agent/provider` are the right recovery shape | diagnostic source checks belong here | retention/source selection posture only | no separate planning owner | read-only tail/watch only | watch/tail is the core lifecycle slice | outputs are excerpts and log views | `log_excerpt` may become evidence | lineage should bind logs to related case/job/flow/agent/provider refs | cancel means stopping a tail/watch view only | explain via runtime/control/availability posture |
| `runtime/system diagnostics` | `system status/info/doctor` and compatibility `runtime status` are catalog roots | readiness/lifecycle/health remain core | `system info`, `runtime diagnostics`, and runtime gate inspection belong here | `system doctor` and gate checks are real lifecycle stages | transport/config posture belongs here | service-control planning is dev-wrapper or explicit control-plan only | start/stop/restart remain forbidden as canonical domain commands | watch/log tails and changing readiness are valid diagnostic slices | outputs are readiness/gate/posture envelopes | runtime decisions and observations may become evidence | lineage is indirect and should route through evidence/state/control, not raw runtime ownership | n/a as domain lifecycle control | explain is a first-class diagnostic/control function |

## Family Recovery Decisions

* `provider`, `model`, `agent`, `workflow`, and `job` are execution-capability
  families and must be modeled through run/watch/outputs/evidence/lineage, not
  only status/list.
* `skills` is a real capability family with registry, routing, and
  admissibility depth; it must not stay at list/inspect only.
* `materialize` and `intake` are first-class operational families with
  plan/run/status/outputs lifecycles.
* `knowledge`, `state`, `lineage`, `records`, and `evidence` are not passive
  data nouns; they each own meaningful inspect/query/tail/lineage or
  write/materialization aftermath slices.
* root `query` remains forbidden and must recover as scoped query families.
* root `logs` recovers only as scoped diagnostic surfaces.
* runtime/system diagnostics must distinguish inspect/check/explain/watch from
  forbidden lifecycle control.

## Implications For V50.6 And V50.7

* V50.6 remains the canonical system model, but family definitions are not
  complete when only readiness/list/status is described.
* V50.7 remains the canonical projection contract, but the projection contract
  becomes mechanically useful only when the lifecycle slices are seeded as
  explicit action descriptors.
* V50.9 is the first registry seed that turns the recovered lifecycle model
  into concrete `action_id` rows for CLI, TUI, SDK, API, and runtime-aligned
  projection work.
* V50.7 remains the canonical action-projection contract, but action matrices
  must be read as lifecycle slices, not as complete family recovery.
* CLI may keep a shallow implemented slice today.
* Loom/TUI may show richer unavailable actions and panels.
* SDK and API may already expose deeper lifecycle stages before CLI catches up.
* runtime action registries must not treat `list` or `status` as sufficient
  substitutes for run/evidence/lineage/cancel/explain stages.

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| API registry normalization of recovered lifecycle stages | V51 |
| typed SDK generation from recovered action families | V60+ |
| public memory-family commands after state/lineage/recall cleanup | later memory waves |
