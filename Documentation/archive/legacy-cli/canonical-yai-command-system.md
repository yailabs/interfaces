# Canonical YAI Command System

## Status

* Delivery: V50.6
* Track: V — CLI/API/SDK/runtime command canon
* Branch: `refoundation/phase-01`
* Source of truth: this document
* Supersedes: V50.5 flat command inventory

## Purpose

Define the canonical YAI command system across:

* user-facing CLI
* diagnostic CLI
* internal runtime actions
* API operations
* SDK surfaces
* storage/projection layers
* governance/control plane
* case materialization cycle

This document reconstructs the command model as a system. It does not treat the
current Rust CLI parser as the whole truth. It reads the command surface as a
projection over the governed operating cycle already described in `yai`,
contracted in `api`, partially surfaced in `sdk`, and only selectively rendered
in `cli` and `loom`.

## Non-goals

* not implementation
* not API registry refactor
* not SDK generation
* not runtime behavior
* not storage behavior
* not command deletion

## CLI / TUI Projection

The command system is not CLI-only.
User-visible CLI commands and TUI actions both project from canonical
`action_id` descriptors defined in:

* `api/Documentation/cli/cli-tui-command-projection-contract.md`

V50.6 defines the command families, ownership boundaries, storage/projection
layers, and operational cycle.

V50.7 defines the shared projection contract that CLI, Loom, SDK, API, and
runtime-aligned action registries must follow.

V50.8 restores lifecycle depth for capability families that had become too
shallow in public projection. Command families such as `provider`, `model`,
`agent`, `workflow`, `job`, `skills`, `materialize`, `state`, `knowledge`,
`lineage`, `records`, `evidence`, `query`, `logs`, and runtime/system
diagnostics must not be modeled as `list/status` only. Their recovered
lifecycle slices are defined in:

* `api/Documentation/cli/capability-command-recovery.md`

V50.9 seeds the first canonical `action_id` registry so the family and
lifecycle model can project consistently into CLI, Loom/TUI, SDK, API, and
runtime-aligned action registries. The registry seed is defined in:

* `api/Documentation/cli/canonical-action-descriptor-registry.md`
* `api/registry/yai-actions.v1.json`

## Command Projection Rules

```text
CLI is a client.
CLI does not own runtime truth.
CLI does not own auth truth.
CLI does not own case truth.
CLI does not own entitlement.
CLI does not own machine authorization.
CLI does not own license lease.
CLI does not own billing.
CLI does not own provider/model execution.
CLI must not revive session as canonical domain.
Command-like UX is a projection over canonical API operations where API exists.
Runtime remains the source of truth for runtime, case, governance, control,
records, knowledge, flow/workflow, and orchestration state.
```

Repository anchors:

* `api/Documentation/command-projection-model.md`
* `api/Documentation/api-to-core-plane-map.md`
* `yai/Documentation/architecture/runtime-session-client-api-boundary.md`
* `yai/README.md`

## Command System Layers

1. `Public CLI`
   Stable operator-facing commands such as `yai auth ...`, `yai case ...`, and
   the future canonical `yai system ...`. Public CLI is presentation and
   invocation grammar, not domain ownership.

2. `Diagnostic CLI`
   Truthful inspection surfaces such as `doctor`, runtime status/readiness,
   substrate inspection, and logs/read-model queries. Diagnostic CLI may stay
   available while operational surfaces are sealed.

3. `Dev-wrapper / bootstrap`
   Repository and host-ops wrappers such as `make yai`, `make info`,
   `cargo run`, and service install/remove helpers. These are not canonical
   domain commands.

4. `SDK surfaces`
   Typed clients over canonical API families. SDK surfaces already expose more
   future command-system shape than the current Rust CLI.

5. `API operation registry`
   Canonical family/resource/verb grammar under `api/registry/*.json`. Public
   commands should project from this grammar when the family exists.

6. `Runtime internal actions`
   Runtime admission, control mediation, case activation, provider/model
   routing, receipt emission, and execution bridges. These are not automatically
   public CLI.

7. `Storage substrate`
   Live/runtime-local and durable persistence mechanics, including SHM/live
   runtime state, LMDB substrate, filesystem fallback, and graph backends.

8. `Projection / analytics layer`
   Derived read models such as DuckDB projections, logs projections, lineage
   summaries, and analytics views. These are rebuildable and not primary truth.

9. `Governance / policy / control plane`
   Qualification, gates, obligations, decisions, supervision/control, and
   evidence boundaries. These planes decide posture; CLI only explains or
   requests.

10. `Materialization / intake cycle`
    Source intake, policy-pack resolution, materialization planning, run
    execution, excerpt/record/evidence creation, knowledge/state projection,
    lineage linking, and later recall/query reuse.

## Storage / State / Projection Layers

The audited repository already expresses a layered data-plane model:

```text
SHM (live runtime state)
  -> LMDB (durable record/event substrate)
  -> DuckDB (query/read model/analytics)
  -> Ladybug (graph/lineage inspection target)
```

Truthful reconstruction from repo anchors:

* `SHM` is documented as live runtime state in
  `yai/Documentation/system/architecture/yai-end-state-runtime.md`.
  This audit did not verify a standalone `shm/` root or a public CLI contract
  for raw SHM access.
* `LMDB` is the durable substrate for append/count/tail/retention mechanics
  under `yai/state/substrate/lmdb_store.c`. It is explicitly not the semantic
  owner of State or Control truth.
* `DuckDB` is a derived projection/read-model layer under
  `yai/state/projections/duckdb/` and `yai/state/substrate/duckdb_store.c`. It
  is rebuildable and must not be treated as canonical State.
* `Ladybug` is a future inspection/navigation/visualization boundary for
  lineage-like surfaces. `ladybug/` root does not exist today. Graph backends
  exist under `yai/state/substrate/graph_*`, but Ladybug itself is not an
  implemented public root.

Durable-state and inspection answers:

* durable state lives in State-backed records and substrate, currently anchored
  by LMDB and `state/records/`
* projection/query data lives in DuckDB and other derived read surfaces
* live runtime-only state is SHM/live runtime posture
* safe inspection can expose derived/read-only posture and projections, not raw
  semantic ownership
* raw SHM internals, raw LMDB keyspace details, and raw graph backend mechanics
  must not become a primary public CLI grammar

| Layer | Expected role | User-facing CLI? | Diagnostic CLI? | API? | SDK? | Runtime internal? | Notes |
| ----- | ------------- | ---------------- | --------------- | ---- | ---- | ----------------- | ----- |
| `SHM` | live runtime state and readiness posture | no | indirect only | indirect via `system`/runtime status projections | indirect only | yes | Documented as target live-runtime layer in `yai-end-state-runtime.md`; no standalone public command or audited standalone module path was verified. |
| `LMDB` | durable record/event substrate | no | yes, read-only via future state/substrate diagnostics | no raw public family | no raw public surface | yes | Anchors: `yai/state/substrate/lmdb_store.c`, `yai/state/substrate/lmdb-keyspace-inventory.md`; LMDB is substrate only, not semantic owner. |
| `DuckDB` | derived query/read-model/analytics projection | no as raw substrate | yes | partial future `state` / `analytics` reads | partial future `state` / `analytics` surfaces | yes | Anchors: `yai/state/projections/duckdb/README.md`, `yai/state/substrate/duckdb_store.c`; rebuildable and non-canonical. |
| `Ladybug` | future lineage/graph inspection and visualization boundary | no as raw public root | yes, later inspection only | not yet | not yet | partial graph-backend anchors only | Anchors: `yai/Documentation/architecture/ladybug-inspection-boundary.md`; `ladybug/` root absent; must not become causal truth or raw public CLI substrate. |

## Operational Cycle

Canonical YAI command grammar must align to the operational cycle already
described in `yai/README.md`, the controlled-act lifecycle, and the
catalog-governance materialization model:

```text
auth/account posture
  -> machine/license posture
  -> root case
  -> active case
  -> intake
  -> policy pack / governance decision
  -> materialization plan
  -> materialization run
  -> excerpts / records / evidence
  -> knowledge / state projection
  -> lineage trace
  -> recall / query
  -> agent / flow / job execution
  -> analytics / audit
  -> review / control / next action
```

This cycle is not loose UX vocabulary. It is the command projection of:

* `operation -> case_action -> controlled_act -> carrier_act -> evidence_event -> state_transition -> orchestration_outcome`
* `catalog -> governance resolution -> case binding -> supervisor/control posture -> state materialization`
* `State remembers -> Lineage connects -> Analytics observes`
* `User Root Case -> Specialized Cases -> Case Graphs -> Events -> Records -> State -> Lineage -> Memory Spine -> Recall -> Proposal -> Control -> Action -> New Experience`

Map-v3 consequence:

* data-plane commands must not collapse straight into `query`
* `case`, `state`, `lineage`, `recall`, and `control` are sequentially related
* `memory` is already a constitutional part of the system spine, but it is not
  yet a public CLI command group in V50.6 because current repo ownership still
  keeps memory inside knowledge/runtime surfaces and later waves (`29+`, `33+`,
  `39+`, `61+`) formalize public memory access separately

### Operational Cycle Mapping

| Cycle step | Command group | API family | SDK surface | Runtime/storage layer | Notes |
| ---------- | ------------- | ---------- | ----------- | --------------------- | ----- |
| auth/account posture | `auth`, `account` | `auth`, `identity` | partial Rust + Loom posture helpers | identity/runtime boundary | CLI may request or inspect posture; it does not own truth. |
| machine/license posture | `machine`, `license`, `entitlement`, `limits` | `identity` today; dedicated license/limit families remain future | no direct Rust surface yet; TS future-facing only | runtime license/machine boundary | Posture-only waves V42-V50 established safe projections, not billing/session truth. |
| root case | `case` | `case` | Rust `case` partial | case plane | `case root/list/open` are current CLI anchors. |
| active case | `case`, `context` | `case` plus operator-context boundary | Rust `case` partial | operator context | Active case belongs to operator context, not session. |
| intake | `intake` | future | none yet | case + governance + source + state records | Intake is not direct knowledge creation. It stages candidate material. |
| policy pack / governance decision | `policy-pack`, `govern`, `control` | `governance`, `control` | TS `governance`, `control`; Rust not yet | governance/control plane | Policy-pack was lost as public grammar and must be restored explicitly. |
| materialization plan | `materialize` | future | none yet | governance -> case -> state | Materialization turns governed candidate inputs into case-bound outputs. |
| materialization run | `materialize` | future | none yet | state/records/runtime bridge | Must not be confused with provider/model invocation alone. |
| excerpts / records / evidence | `excerpt`, `records`, `evidence` | `state`, `control` | TS `state`; evidence remains indirect | state/records/control evidence | Evidence is case-bound. Root `records` grammar is transitional. |
| knowledge / state projection | `knowledge`, `state`, `analytics` | `knowledge`, `state`, `analytics` | TS `knowledge`, `state` | LMDB -> DuckDB -> knowledge context | Derived views must stay derived. |
| lineage trace | `lineage` | currently `knowledge.lineage.*` candidate | TS `knowledge`; future dedicated lineage surface | records + graph backend + Ladybug candidate | Repo still nests lineage in knowledge, but CLI should expose lineage as first-class meaning. |
| recall / query | `recall`, `query` | `knowledge.query` today | TS `knowledge` | knowledge/retrieval/memory | Recall must be governed and case-bound. Root `query` remains unresolved. |
| agent / flow / job execution | `agent`, `workflow`, `job`, `lease`, `provider`, `model`, `skills`, `runtime` | `agents`, `workflow`, `providers`, `models`, `act` | TS rich; Rust partial for providers/models only | runtime/control/orchestration | Execution must remain controlled-act mediated, not session/client owned. |
| analytics / audit | `analytics`, `logs`, `state`, `lineage` | `analytics`, `state`, `knowledge` | TS partial | DuckDB, lineage summaries, logs projection | Analytics observes derived data and must not become limit or billing truth. |
| review / control / next action | `control`, `govern`, `system`, `runtime` | `control`, `governance`, `system` | TS `control`; Rust `system` partial | control/runtime observation | System/runtime/status surfaces explain posture; they do not own execution meaning. |

### Experiential Spine Alignment

The re-foundation map (`yai/Documentation/audits/refoundation-map-v3.md`) adds a
stronger interpretation rule for command design. The command system must
preserve the experiential spine instead of flattening everything into storage or
query verbs.

| Experiential spine step | Command consequence in V50.6 |
| ----------------------- | ---------------------------- |
| `User Root Case` | keep `case root` and future account/root continuity separate from session |
| `Specialized Cases` | keep `case open/enter/leave/status` as first-class command grammar |
| `Case Graphs` | keep graph/lineage meaning case-bound; do not hide it inside raw storage commands |
| `Events` / `Records` | preserve `records` as transitional and converge durable truth under `state` |
| `State` | make `state` a first-class command group rather than a hidden implementation detail |
| `Lineage` | make `lineage` first-class even while repo ownership is still nested under knowledge |
| `Memory Spine` | reserve as future public/access layer; do not prematurely expose raw memory commands in V50.6 |
| `Recall` | keep recall governed, case-bound, and downstream of state/lineage/memory rather than as a global query shortcut |
| `Proposal` | let knowledge/agent/workflow surfaces propose, never own truth |
| `Control` | keep `control` and `govern` explicit; memory and recall must return here for action-relevant use |
| `Action` | keep workflow/job/agent/provider/model execution under runtime/control boundaries |
| `New Experience` | route outcomes back into evidence/records/state/lineage rather than session or client-owned history |

## Canonical Command Groups

The definitive target command groups are:

```text
system
auth
account
machine
license
entitlement
limits
case
context
control
govern
policy-pack
intake
materialize
excerpt
records
evidence
knowledge
state
lineage
recall
query
job
lease
workflow
agent
provider
model
skills
runtime
storage/substrate
analytics
logs
release/update/download
shell
client
session-legacy
dev-wrapper
```

Map-v3 alignment note:

* `memory` is intentionally not promoted to a public top-level command group in
  V50.6
* this is not because memory is unimportant, but because the current repo and
  re-foundation map place public memory access later, after State, Lineage, and
  Recall contracts are cleaner
* until those later waves land, `memory` remains a future plane that must shape
  command design without becoming premature CLI grammar

### Command Group Ownership Table

| Group | Public CLI | API | SDK | Runtime internal | Storage layer | Status |
| ----- | ---------- | --- | --- | ---------------- | ------------- | ------ |
| `system` | yes | `system` | Rust + TS | yes | indirect | `canonical_cli` |
| `auth` | yes | `auth` | partial/local today | yes | no | `canonical_cli` |
| `account` | partial future | `identity`/future account boundary | Loom posture only today | yes | no | `planned_cli` |
| `machine` | partial future | `identity`/future machine boundary | not yet | yes | indirect | `planned_cli` |
| `license` | partial future | future dedicated family or runtime/license boundary | not yet | yes | indirect/cache | `planned_cli` |
| `entitlement` | partial future | `identity`/future entitlement family | TS direction only | yes | no | `planned_cli` |
| `limits` | partial future | future limit/read-model family | TS direction only | yes | derived | `planned_cli` |
| `case` | yes | `case` | Rust + TS partial | yes | indirect | `canonical_cli` |
| `context` | unresolved | none explicit | none explicit | yes | no | `unknown_needs_audit` |
| `control` | target yes | `control` | TS yes | yes | indirect | `canonical_cli` |
| `govern` | target yes | `governance` | TS yes | yes | indirect | `canonical_cli` |
| `policy-pack` | target yes | future governance/catalog family | none yet | yes | no | `canonical_cli` |
| `intake` | target yes | future | none yet | yes | yes | `canonical_cli` |
| `materialize` | target yes | future | none yet | yes | yes | `canonical_cli` |
| `excerpt` | target yes | future or `state` adjunct | none yet | yes | yes | `canonical_cli` |
| `records` | compatibility / maybe nested under `state` | `state` | TS `state` | yes | yes | `legacy_compat` |
| `evidence` | target yes | `control` evidence resources or future explicit family | indirect only | yes | yes | `canonical_cli` |
| `knowledge` | target yes | `knowledge` | TS yes | yes | derived | `canonical_cli` |
| `state` | target yes | `state` | TS yes | yes | yes | `canonical_cli` |
| `lineage` | target yes | currently `knowledge.lineage.*` candidate | TS `knowledge` today | yes | graph + records | `canonical_cli` |
| `recall` | target yes | future or `knowledge.query` projection | none direct | yes | derived | `planned_cli` |
| `query` | no as bare root | `knowledge.query`, `state.records.query` | TS partial | yes | derived | `forbidden` |
| `job` | target yes but unresolved | future `workflow`/`act`/job family | none | yes | records/evidence | `planned_cli` |
| `lease` | likely diagnostic/internal | none explicit public | none | yes | indirect/cache | `runtime_internal` |
| `workflow` | target yes | `workflow` | TS yes | yes | records/graph | `canonical_cli` |
| `agent` | target yes | `agents` | TS yes | yes | records/lineage | `canonical_cli` |
| `provider` | target yes | `providers` | Rust compat + TS yes | yes | runtime state only | `canonical_cli` |
| `model` | target yes | `models` | Rust + TS yes | yes | runtime state only | `canonical_cli` |
| `skills` | target yes | future or runtime/registry family | partial internal docs only | yes | no | `planned_cli` |
| `runtime` | compatibility diagnostics only | `system`/runtime inspect | Rust compat alias | yes | indirect | `diagnostic_cli` |
| `storage/substrate` | no as domain root | no raw public family | no raw public surface | yes | yes | `diagnostic_cli` |
| `analytics` | target yes | `analytics` | TS direction | yes | DuckDB/derived | `planned_cli` |
| `logs` | scoped diagnostics only | future output/read family | not yet | yes | records projection | `diagnostic_cli` |
| `release/update/download` | future only | none verified | none verified | no | no | `planned_cli` |
| `shell` | yes | `client`/`session`/runtime posture projection | CLI + Loom UX | yes | no | `canonical_cli` |
| `client` | partial diagnostics | `client` | partial via posture docs | yes | no | `diagnostic_cli` |
| `session-legacy` | compat only | `session` | Rust compat + TS compat | yes | no | `deprecated` |
| `dev-wrapper` | no | no | no | no | no | `dev_wrapper` |

## Definitive Command List

Required status vocabulary:

```text
canonical_cli
diagnostic_cli
planned_cli
api_only
sdk_only
runtime_internal
storage_internal
dev_wrapper
legacy_compat
deprecated
forbidden
unknown_needs_audit
```

Required posture vocabulary:

```text
no_auth_required
diagnostic_allowed
auth_required
account_required
case_required
active_case_required
operator_context_required
machine_authorization_required
license_lease_required
entitlement_required
limit_projection_required
runtime_gate_required
policy_required
manual_review_required
cloud_capacity_required
admin_required
not_implemented
forbidden
```

Required test priority:

```text
P0
P1
P2
P3
N/A
```

### System, Identity, Case, and Control

| group | command | status | layer | owner | implemented today | target command | API operation candidate | SDK surface candidate | runtime action candidate | required posture | test priority | notes |
| ----- | ------- | ------ | ----- | ----- | ----------------- | -------------- | ----------------------- | -------------------- | ------------------------ | ---------------- | ------------- | ----- |
| `system` | `yai system status` | `canonical_cli` | `Public CLI` | `cli` projecting `api/system` | no | yes | `system.status` | Rust `client.system().status()` | runtime service status/readiness inspect | `diagnostic_allowed` | `P0` | Canonical replacement for compatibility `yai runtime status`. |
| `system` | `yai system info` | `planned_cli` | `Diagnostic CLI` | `cli` projecting `api/system` | no | yes | `system.runtime.inspect` | Rust `client.system()` future detail view | runtime detail inspect | `diagnostic_allowed` | `P1` | Split between `status`, `info`, and `doctor` still needs cleanup. |
| `system` | `yai system doctor` | `planned_cli` | `Diagnostic CLI` | `cli` | no | yes | `system.check` | Rust `client.system().check()` candidate | runtime/service/environment diagnostic read | `diagnostic_allowed` | `P1` | Current root `yai doctor` remains truthful local diagnostic surface. |
| `status` | `yai status` | `diagnostic_cli` | `Public CLI` convenience wrapper | `cli` | no | yes | likely `system.status` wrapper | same as `system.status` | wrapper only | `diagnostic_allowed` | `P1` | Convenience alias only; must not own separate truth. |
| `auth` | `yai auth login` | `canonical_cli` | `Public CLI` | `cli` projecting `api/auth` | yes | yes | `auth.login` | local today; future SDK auth surface | auth posture request | `no_auth_required` | `P0` | Current production path is unavailable; `--local-dev` is compatibility/bootstrap. |
| `auth` | `yai auth status` | `canonical_cli` | `Public CLI` | `cli` | yes | yes | `auth.status` | future SDK auth surface | auth posture inspect | `diagnostic_allowed` | `P0` | Must stay distinct from session and client attachment. |
| `auth` | `yai auth logout` | `canonical_cli` | `Public CLI` | `cli` | yes | yes | `auth.logout` | future SDK auth surface | auth posture clear/invalidation request | `auth_required` | `P0` | Logout is not runtime stop and not case deletion. |
| `account` | `yai account status` | `planned_cli` | `Public CLI` | `cli` over identity/account posture | no | yes | future account or `identity` posture op | none yet | account posture inspect | `auth_required` | `P2` | Must not expose billing/account profile internals. |
| `machine` | `yai machine authorization status` | `planned_cli` | `Diagnostic CLI` | `cli` over machine posture | no | yes | future machine/identity operation | none yet | machine authorization posture inspect | `auth_required + machine_authorization_required` | `P1` | No raw hardware or fingerprint leakage. |
| `license` | `yai license lease status` | `planned_cli` | `Diagnostic CLI` | `cli` over runtime/license posture | no | yes | future license family | none yet | license lease posture inspect | `auth_required + license_lease_required` | `P1` | Safe request/response/cache posture only. |
| `entitlement` | `yai entitlement status` | `planned_cli` | `Diagnostic CLI` | `cli` | no | yes | future entitlement family or `identity` resource | none yet | entitlement posture inspect | `auth_required + entitlement_required` | `P1` | Safe projection only; no plan or billing object. |
| `limits` | `yai limits explain` | `planned_cli` | `Diagnostic CLI` | `cli` | no | yes | future limit/read-model family | none yet | limit reconciliation / projection explain | `auth_required + limit_projection_required` | `P1` | Shared-account limit posture only; not quota-ledger ownership. |
| `case` | `yai case root` | `canonical_cli` | `Public CLI` | `cli` | yes | yes | local case root / future `case.tree` adjunct | Rust local case helpers | root case discovery | `auth_required` | `P0` | Current local-manifest anchor. |
| `case` | `yai case enter <case>` | `canonical_cli` | `Public CLI` | `cli` projecting case/operator context | yes | yes | `case.use` / `case.current` adjunct | Rust `case` partial | `operator_context.active_case_ref` set | `auth_required + case_required + operator_context_required` | `P0` | Active case belongs to operator context, not session. |
| `case` | `yai case status` | `canonical_cli` | `Diagnostic CLI` | `cli` | yes | yes | `case.current` plus case posture projection | Rust `client.case().current()` partial | active-case posture inspect | `diagnostic_allowed` | `P0` | Must stay available even when operational work is sealed. |
| `context` | `yai context status` | `unknown_needs_audit` | `Public CLI` candidate | `cli` | no | unresolved | none explicit | none explicit | operator context inspect | `auth_required + operator_context_required` | `P2` | May remain hidden behind `case status/enter/leave`. |
| `control` | `yai control explain <action>` | `canonical_cli` | `Public CLI` | `cli` projecting `api/control` | no | yes | `control.decisions.explain` | TS `control`; Rust future | control decision explain | `auth_required + active_case_required + runtime_gate_required` | `P1` | Control explains posture; it does not execute provider/model/job/flow by itself. |
| `control` | `yai control gates` | `canonical_cli` | `Diagnostic CLI` | `cli` projecting `api/control` | no | yes | `control.gates.list` / `control.gates.show` | TS `control` | gate posture inspect | `auth_required + runtime_gate_required` | `P1` | Good replacement for vague `runtime gates`. |
| `govern` | `yai govern decision explain <decision>` | `canonical_cli` | `Public CLI` | `cli` projecting governance plane | no | yes | `governance.posture` / `governance.policy.resolve` / future decision op | TS `governance` | governance decision explain | `auth_required + case_required + policy_required` | `P1` | CLI spelling `govern` can project API/SDK family `governance`. |
| `policy-pack` | `yai policy-pack validate <pack>` | `canonical_cli` | `Public CLI` | `cli` + future API | no | yes | future governance/catalog operation | none yet | policy-pack validation | `auth_required + policy_required + not_implemented` | `P1` | Restores explicit governed pack vocabulary; root `yai policy` remains too vague. |

### Intake, Materialization, State, Knowledge, and Lineage

| group | command | status | layer | owner | implemented today | target command | API operation candidate | SDK surface candidate | runtime action candidate | required posture | test priority | notes |
| ----- | ------- | ------ | ----- | ----- | ----------------- | -------------- | ----------------------- | -------------------- | ------------------------ | ---------------- | ------------- | ----- |
| `intake` | `yai intake plan <source>` | `canonical_cli` | `Public CLI` | `cli` + future API/runtime | no | yes | future `intake.plan` | none yet | intake plan generation | `auth_required + case_required + policy_required + not_implemented` | `P1` | Intake stages candidate material; it does not directly become knowledge. |
| `intake` | `yai intake run <source>` | `canonical_cli` | `Public CLI` | `cli` + future API/runtime | no | yes | future `intake.run` | none yet | intake run | `auth_required + active_case_required + policy_required + runtime_gate_required + not_implemented` | `P2` | Conceptual options include `--case`, `--policy-pack`, `--dry-run`, `--format json`. |
| `materialize` | `yai materialize plan <input>` | `canonical_cli` | `Public CLI` | `cli` + future API/runtime | no | yes | future `materialization.plan` | none yet | materialization planning | `auth_required + case_required + policy_required + not_implemented` | `P1` | Central command family missing from current CLI and registry. |
| `materialize` | `yai materialize run <plan>` | `canonical_cli` | `Public CLI` | `cli` + future API/runtime | no | yes | future `materialization.run` | none yet | `state/records/materialize_runtime` anchor | `auth_required + active_case_required + runtime_gate_required + policy_required + not_implemented` | `P2` | Must bind source/intake, policy-pack, and case outputs. |
| `excerpt` | `yai excerpt lineage <excerpt>` | `canonical_cli` | `Diagnostic CLI` | `cli` + future API/runtime | no | yes | future excerpt or lineage op | none yet | excerpt lineage inspect | `auth_required + active_case_required + not_implemented` | `P2` | Excerpts are case-bound and not free-floating documents. |
| `records` | `yai records list` | `legacy_compat` | `Public CLI` compatibility | `cli` -> future `state` | no | no, prefer `state records` | `state.records.query` | TS `state.records` | records query/tail | `auth_required + active_case_required + not_implemented` | `P2` | Root `records` is transitional; canonical shape should move under `state`. |
| `evidence` | `yai evidence inspect <evidence>` | `canonical_cli` | `Diagnostic CLI` | `cli` + control/state | no | yes | future `control.evidence.*` or explicit evidence family | none direct | evidence inspect | `auth_required + active_case_required + not_implemented` | `P2` | Evidence is case-bound and does not belong to provider/model/agent ownership. |
| `knowledge` | `yai knowledge inspect <knowledge>` | `canonical_cli` | `Diagnostic CLI` | `cli` projecting `api/knowledge` | no | yes | `knowledge.query` adjunct / future `knowledge.inspect` | TS `knowledge` | knowledge inspect | `auth_required + active_case_required + not_implemented` | `P2` | Knowledge is case-bound projection, not raw logging. |
| `knowledge` | `yai knowledge rebuild` | `planned_cli` | `Diagnostic CLI` gated | `cli` + runtime/state | no | yes | future knowledge/state rebuild op | none yet | projection rebuild | `auth_required + active_case_required + runtime_gate_required + policy_required + not_implemented` | `P3` | Rebuild is future/gated and must not imply unsafe mutation by default. |
| `state` | `yai state status` | `canonical_cli` | `Diagnostic CLI` | `cli` projecting `api/state` | no | yes | `state.records.query` / future `state.status` | TS `state` | state posture inspect | `diagnostic_allowed` | `P1` | State is a first-class command group absent from current Rust CLI. |
| `state` | `yai state substrate inspect duckdb` | `diagnostic_cli` | `Diagnostic CLI` | `cli` over state substrate | no | yes | none raw public; diagnostic projection only | none raw | substrate inspect | `diagnostic_allowed + not_implemented` | `P2` | Preferred over raw root `substrate` command because it preserves State ownership. |
| `lineage` | `yai lineage trace <ref>` | `canonical_cli` | `Diagnostic CLI` | `cli` projecting current knowledge/lineage surfaces | no | yes | current best candidate `knowledge.lineage.trace` | TS `knowledge` today; future dedicated lineage surface | lineage trace | `auth_required + active_case_required + not_implemented` | `P1` | Repo still nests lineage inside knowledge, but CLI should expose lineage as first-class meaning. |
| `lineage` | `yai lineage graph <ref>` | `planned_cli` | `Diagnostic CLI` | `cli` + future Ladybug/lineage view | no | yes | future lineage graph operation | none yet | graph inspection | `auth_required + active_case_required + not_implemented` | `P3` | Graph output remains future and must preserve derived truth class. |
| `recall` | `yai recall query <query>` | `planned_cli` | `Public CLI` | `cli` over governed retrieval | no | yes | `knowledge.query` or future `recall.query` | TS `knowledge` partial | governed recall query | `auth_required + active_case_required + runtime_gate_required + not_implemented` | `P2` | Recall is governed and must not become global unscoped recall. |
| `query` | `yai query` | `forbidden` | `Public CLI` root | none | no | no | ambiguous between `knowledge.query`, `state.records.query`, and future scoped queries | none | none | `forbidden` | `N/A` | Too vague. Preferred replacements are `yai recall query ...`, `yai state ...`, or an explicit scoped `yai query case|knowledge|records|evidence ...`. |

### Execution, Capability, Observation, and Compatibility

| group | command | status | layer | owner | implemented today | target command | API operation candidate | SDK surface candidate | runtime action candidate | required posture | test priority | notes |
| ----- | ------- | ------ | ----- | ----- | ----------------- | -------------- | ----------------------- | -------------------- | ------------------------ | ---------------- | ------------- | ----- |
| `job` | `yai job start <spec>` | `planned_cli` | `Public CLI` | `cli` + future workflow/control/runtime | no | yes | future `job.*` or `act.run` / `workflow.*` composite | none direct | controlled-act admission + orchestration run | `auth_required + active_case_required + machine_authorization_required + license_lease_required + entitlement_required + limit_projection_required + runtime_gate_required + not_implemented` | `P2` | Job is case-bound and not session/client owned. |
| `lease` | `yai lease execution status <job>` | `runtime_internal` | `Diagnostic CLI` candidate | runtime/license boundary | no | unresolved | none explicit public | none | execution lease inspect | `auth_required + active_case_required + license_lease_required + not_implemented` | `P3` | Keep internal or diagnostic until API ownership is explicit. |
| `workflow` | `yai workflow run <workflow>` | `canonical_cli` | `Public CLI` | `cli` projecting `api/workflow` | no | yes | `workflow.*` | TS `workflow`; Rust future | workflow run / watch | `auth_required + active_case_required + runtime_gate_required + not_implemented` | `P2` | Canonical replacement for legacy `flow`. |
| `workflow` | `yai flow run <flow>` | `legacy_compat` | `Public CLI` compatibility | `cli` | no | no, compat only | maps to `workflow.*` | TS `workflow` | compatibility only | `auth_required + active_case_required + not_implemented` | `P3` | Keep only as migration bridge if needed. |
| `agent` | `yai agent spawn <role>` | `canonical_cli` | `Public CLI` | `cli` projecting `api/agents` | no | yes | `agents.run` / `agents.plan` | TS `agents`; Rust future | agent run/plan | `auth_required + active_case_required + entitlement_required + runtime_gate_required + not_implemented` | `P2` | Preferred public grammar is singular `agent`, even though API family is plural `agents`. |
| `provider` | `yai provider inspect <provider>` | `canonical_cli` | `Diagnostic CLI` | `cli` projecting provider plane | no | yes | `providers.list` / `providers.probe` | Rust compat + TS `providers` | provider inspect/probe | `diagnostic_allowed` | `P1` | Preferred public CLI is singular `provider`; API/SDK family stays plural `providers`. |
| `model` | `yai model inspect <model>` | `canonical_cli` | `Diagnostic CLI` | `cli` projecting model plane | no | yes | `models.list` / `models.capabilities.show` | Rust `models`; TS `models` | model inspect/capabilities | `diagnostic_allowed` | `P1` | Current `yai models list` may remain compatibility until grammar normalizes. |
| `skills` | `yai skills inspect <skill>` | `planned_cli` | `Diagnostic CLI` | `cli` + runtime/registry | no | yes | future skills/registry operation | none verified as SDK public today | skill registry inspect | `diagnostic_allowed + not_implemented` | `P2` | Plural `skills` is already well established in docs. |
| `runtime` | `yai runtime status` | `diagnostic_cli` | `Diagnostic CLI` compatibility | `cli` | yes | no as final public root | compatibility to `system.status` | Rust compat alias `client.runtime()` | runtime status inspect | `diagnostic_allowed` | `P0` | Keep truthful compatibility while `system` becomes canonical. |
| `runtime` | `yai runtime start` | `forbidden` | `Dev-wrapper / bootstrap` | service/bootstrap boundary | no | no | none | none | host/service manager only | `forbidden` | `N/A` | Canonical public runtime lifecycle commands are forbidden. |
| `storage/substrate` | `yai substrate inspect lmdb` | `diagnostic_cli` | `Diagnostic CLI` | `cli` over State diagnostics | no | alternative only | none raw public | none raw | substrate inspection | `diagnostic_allowed + not_implemented` | `P3` | Prefer `yai state substrate inspect lmdb` so State remains owner. |
| `analytics` | `yai analytics summary` | `planned_cli` | `Diagnostic CLI` | `cli` projecting derived analytics | no | yes | future `analytics.*`; registry currently seeds analytics-related ops | TS direction only | analytics read model inspect | `auth_required + active_case_required + not_implemented` | `P2` | Analytics is derived and must not become billing or limit truth. |
| `logs` | `yai logs runtime` | `diagnostic_cli` | `Diagnostic CLI` | `cli` over records projection | no | yes | future output/log projection | none | records/log projection tail | `diagnostic_allowed + not_implemented` | `P2` | Scoped logs are preferable to root `yai logs`. |
| `release/update/download` | `yai update check` | `planned_cli` | `Public CLI` future | `cli` + packaging/distribution boundary | no | yes | none verified | none verified | none yet | `no_auth_required + not_implemented` | `P3` | Must not claim live artifact access or fake download behavior. |
| `shell` | `yai shell attach <shell_id>` | `canonical_cli` | `Public CLI` | `cli` | yes | yes | `client` / compat `session` projection only | CLI UX only | shell attach/detach UX | `diagnostic_allowed` | `P0` | Shell is UX language, not auth, case, or runtime ownership. |
| `client` | `yai client list` | `diagnostic_cli` | `Diagnostic CLI` | `cli` / future API projection | no | yes | `client.list` / `client.status` family candidates | none explicit today | connected-client inspect | `diagnostic_allowed + not_implemented` | `P2` | Useful as a diagnostic/TUI/API surface; likely secondary to `shell` for everyday UX. |
| `session-legacy` | `yai session status` | `deprecated` | `Public CLI` compatibility | `cli` | yes | no | `session.status` | Rust compat + TS compat | legacy attach/status posture | `diagnostic_allowed` | `P1` | Session must not own auth, case, runtime, or work. Removal path belongs to later waves. |
| `dev-wrapper` | `make yai` | `dev_wrapper` | `Dev-wrapper / bootstrap` | repository/build tooling | yes | no | none | none | build/bootstrap only | `N/A` | `N/A` | Not a canonical domain CLI command. |

## Storage Layer Mapping

| Layer | Role | Commands | API/SDK exposure | Public? | Notes |
| ----- | ---- | -------- | ---------------- | ------- | ----- |
| `SHM` | live runtime state / readiness posture | no direct raw command; observe through `yai system status`, `yai runtime status`, and future `yai system readiness` | indirect only | no | Repo audit verified the concept and posture language, not a standalone public SHM command surface. |
| `LMDB` | durable record/event substrate | preferred diagnostic form `yai state substrate inspect lmdb` | no raw public API/SDK surface | no | Must stay substrate-only; raw DBI/keyspace is not public CLI. |
| `DuckDB` | derived read-model, query, analytics projection | `yai state substrate inspect duckdb`, future `yai analytics ...`, `yai state projections` | indirect future `state`/`analytics` | diagnostic only | Derived, rebuildable, provenance/freshness-sensitive. |
| `Ladybug` | future graph/lineage inspection target | future `yai lineage graph <ref>` or `yai state substrate inspect ladybug` if ever added | none verified today | no raw public root | `ladybug/` root absent; graph backends exist, but Ladybug remains an inspection-boundary concept. |

## Lost Legacy Capability Recovery Table

| old legacy concept | where it was found | whether it survived extraction | new canonical group | new target command | API/SDK/runtime owner | status |
| ------------------ | ------------------ | ----------------------------- | ------------------- | ------------------ | --------------------- | ------ |
| `intake` | old C era command expectations; `yai` docs on governance embedding/materialization | no clean public survival | `intake` | `yai intake plan <source>` | future API + runtime + CLI projection | `restored target` |
| `policy pack` | governance/catalog/materialization docs | not as public CLI grammar | `policy-pack` | `yai policy-pack validate <pack>` | governance/catalog owner | `restored target` |
| `materialization` | `catalog-governance-materialization-model.md`, state/materialize runtime anchors | survived as runtime/state concept, not CLI | `materialize` | `yai materialize run <plan>` | future API + runtime + CLI projection | `restored target` |
| `excerpt` | architecture and knowledge/materialization narratives | no clean public grammar | `excerpt` | `yai excerpt lineage <excerpt>` | future API + runtime | `restored target` |
| `knowledge` | API family, TS SDK, `yai` knowledge plane | yes | `knowledge` | `yai knowledge inspect <knowledge>` | API + SDK + runtime | `target` |
| `state` | API family, TS SDK, `yai/state/` | yes | `state` | `yai state status` | API + SDK + runtime | `target` |
| `lineage` | `yai` docs and internal surfaces, currently nested in knowledge | partial only | `lineage` | `yai lineage trace <ref>` | runtime + future API/SDK cleanup | `restored target` |
| `query` | CLI legacy, knowledge query docs, SDK constants | yes, but too vague as root | scoped query under `recall` / `state` / `knowledge` | replace bare `yai query` | API + SDK + runtime | `forbidden as root` |
| `inspect` | old CLI patterns, Loom and runtime inspect wording | partial only | family-local inspect verbs | replace bare `yai inspect` | family-specific owners | `forbidden as root` |
| `logs` | historic CLI and `yai-end-state-runtime.md` (`yai logs latest`) | yes as projection concept | `logs` and `state records` | `yai logs runtime` / `yai state records tail` | runtime/state owner | `diagnostic target` |
| `governance` | API family `governance`, TS SDK, CLI placeholder `governance` | yes | `govern` | `yai govern status` | API `governance` + SDK `governance` | `target with CLI rename` |
| `control` / `supervisor` | CLI placeholder `supervisor`, API `control`, TS `control` | partial | `control` | `yai control explain <action>` | API + SDK + runtime control plane | `target with rename` |
| `provider` | current Rust CLI and SDK compat, API `providers` | yes | `provider` | `yai provider inspect <provider>` | API `providers` + SDK `providers` | `target with singular CLI projection` |
| `model` / `models` | current Rust CLI `models`, API `models` | yes | `model` | `yai model inspect <model>` | API + SDK | `target with grammar normalization` |
| `agent` / `agents` | CLI placeholder `agent`, API `agents`, TS `agents` | partial | `agent` | `yai agent spawn <role>` | API + SDK + runtime | `target with singular CLI projection` |
| `flow` | CLI placeholder `flow`, many docs, old operator workflow docs | yes as compatibility | `workflow` | `yai workflow run <workflow>` | API `workflow` + TS SDK `workflow` | `legacy -> target` |
| `job` | execution/job semantics in lifecycle docs and waves, no clean public family | partial internal concept | `job` | `yai job status <job>` | future API/runtime | `planned target` |
| `case` | current Rust CLI, API family, SDK surfaces | yes | `case` | `yai case status` | API + SDK + runtime | `target` |

## Forbidden / Too Vague Commands

| Command | Why vague or forbidden | Preferred replacement |
| ------- | ---------------------- | --------------------- |
| `yai query` | Too ambiguous between recall, knowledge, state records, and evidence. | `yai recall query <query>` or a future scoped form such as `yai query knowledge ...` / `yai query records ...`. |
| `yai inspect` | `inspect` is a verb, not a domain family. Root ownership is unclear and encourages catch-all drift. | Family-local verbs such as `yai system info`, `yai lineage trace`, `yai evidence inspect`, `yai provider inspect`, `yai model inspect`. |
| `yai logs` | Root logs are too vague and risk collapsing storage, projection, runtime, and job logs into one unscoped surface. | `yai logs runtime`, `yai logs job <job>`, or `yai state records tail`. |
| `yai policy` | Root policy does not distinguish governance posture, policy-pack artifacts, or control decisions. | `yai policy-pack ...` for pack artifacts and `yai govern policy ...` for governance resolution/explanation. |
| `yai runtime start` / `stop` / `restart` | Runtime lifecycle control is a service/bootstrap boundary, not canonical domain CLI. | `make install-service`, host service manager, or future explicitly governed service-manager boundary. |

## P0/P1/P2 Test Plan

| command | expected exit class | sealed/no-auth behavior | local-dev behavior | active-case behavior | future licensed behavior | JSON output required yes/no | snapshot test required yes/no | integration test required yes/no |
| ------- | ------------------- | ----------------------- | ------------------ | -------------------- | ------------------------ | --------------------------- | ----------------------------- | -------------------------------- |
| `yai auth status` | `0 success` | truthful posture, no secret leakage | yes | n/a | posture only | yes | yes | no |
| `yai auth login --local-dev` | `0 success` | n/a | yes | root case bootstrap may follow | must remain dev-only | yes | yes | no |
| `yai case list` | `0 success` | should still explain auth/case posture | yes | lists available cases | later licensed gates may still allow read | yes | yes | no |
| `yai case enter <case>` | `0/1 truthful mutation` | blocked if posture forbids | yes | must set operator context, not session | should honor future gates | yes | yes | yes |
| `yai system status` | `0 success` | must remain available while sealed | yes | should report operator-context posture separately | must surface license/machine/limit posture safely | yes | yes | yes |
| `yai runtime status` | `0 success` | same truthful posture as compat alias | yes | same as `system status` | same | yes | yes | yes |
| `yai control explain <action>` | `0 success or truthful unavailable` | should explain gates rather than execute | partial future | needs active case for case-bound actions | must surface machine/license/limit gates | yes | yes | yes |
| `yai policy-pack validate <pack>` | `0 success or truthful unavailable` | diagnostic/read-only | future | may require case/policy context | future license posture may gate pack usage, not raw read | yes | yes | yes |
| `yai intake plan <source>` | `0 success or truthful unavailable` | may remain dry-run capable while sealed | future | case-bound | must surface policy-pack/materialization requirements | yes | yes | yes |
| `yai materialize run <plan>` | `0 success or truthful blocked` | blocked when sealed | future | active case required | license/machine/gates required | yes | yes | yes |
| `yai lineage trace <ref>` | `0 success or truthful unavailable` | diagnostics may remain allowed | future | case-bound scope required | should remain read-only under license posture | yes | yes | yes |
| `yai state substrate inspect duckdb` | `0 success or truthful unavailable` | diagnostic-only | future | may be scoped | no commercial truth leakage | yes | yes | yes |
| `yai provider inspect <provider>` | `0 success or truthful unavailable` | diagnostics allowed | yes | n/a | must never reveal credentials | yes | yes | yes |
| `yai workflow run <workflow>` | `0 success or truthful blocked` | blocked while sealed | future | active case required | license/machine/limit/gate posture required | yes | yes | yes |
| `yai session status` | `0 success` | must remain clearly compatibility-only | yes | must not claim active-case ownership | same | yes | yes | no |

## Final System Decisions

* V50.6 is the authoritative command-system document.
* V50.5 remains useful only as a preliminary flat inventory and cross-check.
* V50.8 is the authoritative lifecycle-depth recovery for operational
  capability families that were under-modeled in earlier CLI/TUI audits.
* `system` is the canonical public diagnostic root; `runtime` remains a
  compatibility/diagnostic surface.
* `policy-pack`, `intake`, `materialize`, `excerpt`, `state`, and `lineage`
  must be restored as first-class command groups even though current Rust CLI
  does not yet expose them.
* `workflow` is the canonical target grammar; `flow` is legacy compatibility.
* `provider`, `model`, and `agent` are accepted public CLI spellings even when
  the API/SDK family remains plural (`providers`, `models`, `agents`).
* readiness, status, and list are first slices only; they do not recover a
  capability family by themselves.
* `records` should converge under `state`, not remain a root semantic owner.
* `query`, `inspect`, `logs`, and root `policy` are too vague as public roots.
* raw substrate layers must stay diagnostic and read-only; they must not become
  semantic public CLI owners.
