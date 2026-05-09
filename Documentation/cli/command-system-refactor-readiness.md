# Command System Refactor Readiness

## Status

* Delivery: V50.10
* Track: V — CLI/API/SDK/runtime/TUI action canon
* Branch: `refoundation/phase-01`
* Depends on:
  - `canonical-yai-command-system.md`
  - `cli-tui-command-projection-contract.md`
  - `capability-command-recovery.md`
  - `canonical-action-descriptor-registry.md`
  - `registry/yai-actions.v1.json`
* Next wave: V51 — API Registry Refactor

## Purpose

Prepare the exact cross-repo refactor path for canonical actions before V51.

V50.10 converts the V50.6-V50.9 command-system work into a verified readiness
map across `api`, `cli`, `sdk`, `yai`, and `loom`. The output is not another
theory wave. It is the wiring map for what V51+ must normalize, deprecate,
expose, hide, reconnect, or leave unavailable.

The V50.9 seed currently contains `203` canonical `action_id` descriptors. This
document consumes that seed and classifies each action against real repo
surfaces.

## Non-goals

* not implementation
* not API registry refactor
* not CLI parser change
* not TUI/Loom UI change
* not SDK generation
* not runtime behavior
* not storage behavior
* not command deletion

## Readiness Model

```text
ready_for_v51_registry_refactor
needs_api_operation
needs_sdk_surface
needs_cli_projection
needs_tui_projection
needs_runtime_action_key
needs_backend_reconnection
needs_storage_projection
needs_materialization_path
needs_governance_policy_path
needs_lineage_path
needs_deprecation_path
forbidden_locked
legacy_locked
unknown_needs_source_audit
```

Readiness interpretation:

* `ready_for_v51_registry_refactor`: API family and near-term action mapping are already grounded enough that V51 can normalize names and projections without new domain discovery.
* `needs_api_operation`: the registry seed points at `none verified` or at a compatibility-only op that still needs a canonical family/resource/verb entry.
* `needs_sdk_surface`: API candidate exists, but one or more typed SDK surfaces are absent, partial, or compatibility-only.
* `needs_cli_projection`: action is canonical in seed/API/SDK but missing or drifted in the Rust CLI parser/help/output/tests.
* `needs_tui_projection`: action should exist in Loom as a palette entry, panel action, or unavailable placeholder but is not yet mapped there.
* `needs_runtime_action_key`: command/API shape exists but runtime-aligned action-key naming is still unverified.
* `needs_backend_reconnection`: repo evidence shows backend/runtime pieces exist, but public action wiring was flattened or lost.
* `needs_storage_projection`: read-model, state, logs, or analytics projection work is still missing or only partially exposed.
* `needs_materialization_path`: intake/materialization actions need a first-class path through policy, case, state, evidence, and outputs.
* `needs_governance_policy_path`: policy/govern/control slices need canonical registry ownership or clearer action family mapping.
* `needs_lineage_path`: lineage is still partially buried under knowledge or lacks first-class output/graph actions.
* `needs_deprecation_path`: compatibility action still exists and must be marked legacy, hidden, or replaced in later waves.
* `forbidden_locked`: action stays explicitly forbidden.
* `legacy_locked`: action stays available only as compatibility or migration bridge.
* `unknown_needs_source_audit`: current source/doc reality is divergent enough that later implementation must re-audit before wiring.

## Refactor Target Layers

```text
api_registry
api_schema
api_fixture
api_conformance
sdk_typescript
sdk_rust
sdk_python
sdk_c
cli_parser
cli_output
cli_tests
loom_action_registry
loom_palette
loom_panel
yai_runtime_core
yai_state_substrate
yai_materialization
yai_lineage
yai_governance
yai_provider_model_backend
yai_logs_projection
docs_only
```

Target-layer interpretation:

* `api_registry`, `api_schema`, `api_fixture`, `api_conformance` are the V51-V57 normalization band.
* `sdk_typescript`, `sdk_rust`, `sdk_python`, `sdk_c` are the V58-V60 typed client alignment band.
* `cli_parser`, `cli_output`, `cli_tests` are the V61-V67 migration band.
* `loom_action_registry`, `loom_palette`, `loom_panel` are the TUI alignment band.
* `yai_runtime_core`, `yai_state_substrate`, `yai_materialization`, `yai_lineage`, `yai_governance`, `yai_provider_model_backend`, `yai_logs_projection` are the backend reconnection band.
* `docs_only` records actions that should stay unavailable or diagnostic until later product/platform work exists.

## Cross-Repo Readiness Matrix

Rows below may cluster multiple `action_id` values when the current repo
evidence and next-wave path are identical. Every `action_id` from
`registry/yai-actions.v1.json` appears exactly once.

### System, Auth, Case, and Governance

| action_id | family | current_registry_status | api_gap | sdk_gap | cli_gap | tui_gap | runtime_gap | storage_or_projection_gap | backend_reconnection_gap | legacy_alias_gap | test_gap | refactor_class | next_wave | notes |
| --------- | ------ | ----------------------- | ------- | ------- | ------- | ------- | ----------- | ------------------------- | ------------------------ | ---------------- | -------- | -------------- | --------- | ----- |
| `system.status`, `system.readiness` | `system` | `canonical_target` | no new API family; keep `system.status` as canonical anchor | TS and Rust already have `system.status`; Python/C not action-model aligned | add `yai system status` and `yai system readiness`; current CLI still exposes `yai runtime status` | Loom has `/status` and `/runtime`, but not `action_id`-backed `system_panel` entries | no major runtime gap for inspect path | none | none | `runtime.status -> system.status` | add CLI snapshots, sealed/no-auth checks, Loom palette/panel checks | `ready_for_v51_registry_refactor`, `needs_cli_projection`, `needs_tui_projection` | `V51 + V61-V67 + Band D` | `cli/src/commands/runtime.rs` already calls `system.status`, so this is mainly a projection normalization task. |
| `system.info`, `system.doctor` | `system` | `planned` | no new family; keep `system.runtime.inspect` and `system.check` candidates | TS has both candidates; Rust exposes `check()` but not a public `runtimeInspect()` surface | add parser/help/output for `yai system info` and `yai system doctor` | Loom needs visible info/doctor entries in `system_panel` and palette | none major | none | none | root `yai doctor` stays convenience alias only | add diagnostic snapshots and unavailable-path tests | `ready_for_v51_registry_refactor`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection` | `V51 + V58-V60 + V61-V67 + Band D` | Verified Rust ops constants include `system.runtime.inspect`, but the public Rust surface still centers on `status()` and `check()`. |
| `auth.login`, `auth.status`, `auth.logout` | `auth` | `implemented_current`, `implemented_current`, `implemented_current` | canonical API operations still unverified | no typed SDK auth surface verified | current CLI exists and is truthful; no parser gap | Loom auth panel can show posture, but canonical `action_id` mapping is still missing | no runtime action-key verification | none | local CLI path exists; production/backend path missing | none | add CLI JSON output coverage, local-dev/unauth/sealed tests, future Loom placeholders | `needs_api_operation`, `needs_sdk_surface`, `needs_tui_projection` | `V51 + V58-V60 + Band D` | `cli/src/commands/auth.rs` proves truthful local posture and logout boundary, but not canonical API/SDK ownership yet. |
| `auth.login.local_dev` | `auth` | `legacy_compat` | keep outside canonical production auth family | SDK not needed beyond compatibility docs | CLI path already exists | Loom should stay hidden or developer-only | none | none | none | compatibility-only local-dev bootstrap | add legacy tests and explicit compatibility docs | `legacy_locked`, `needs_deprecation_path` | `V51 + V61-V67` | Remains useful for local development, but must not become the production auth story. |
| `account.status`, `account.access`, `account.open` | `account` | `planned` | add canonical account posture family or explicit identity/account projections | all SDK surfaces missing | no current CLI parser | Loom needs `account_panel` placeholders only | runtime truth unverified | none | none | none | later platform tests only | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection` | `Band F` | Keep billing/profile internals out of scope. |
| `machine.status`, `machine.identity.status`, `machine.evidence.status`, `machine.enroll`, `machine.authorization.status` | `machine` | `planned` | add canonical machine posture family | all SDK surfaces missing | no current CLI parser | Loom should show blocked/planned states in `machine_panel` | runtime posture contracts exist from V42/V50 but no verified action-key map | none | none | none | add future machine/license posture tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_runtime_action_key` | `V51 + V58-V60 + Band D + Band F` | Must never expose raw hardware or fingerprint data. |
| `license.status`, `license.lease.status`, `license.check`, `license.cache.status` | `license` | `planned` | add canonical license posture family | all SDK surfaces missing | no current CLI parser | Loom should expose read-only/unavailable `license_panel` states | runtime/license posture docs exist, but public action keys are unverified | cache and safe projection contracts exist; action outputs still missing | none | none | add lease invalidation/offline-grace output tests later | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_runtime_action_key` | `V51 + V58-V60 + Band D + Band F` | Safe projection only; no billing/subscription object leakage. |
| `entitlement.status` | `entitlement` | `planned` | add explicit entitlement projection | all SDK surfaces missing | no current CLI parser | Loom should show `limits_panel` or `account_panel` placeholder | runtime truth unverified | none | none | none | later read-only tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection` | `Band F` | Keep entitlement posture separate from billing truth. |
| `limits.status`, `limits.explain` | `limits` | `planned` | add canonical limit/read-model family | all SDK surfaces missing | no current CLI parser | Loom should expose disabled `limits_panel` entries | runtime truth unverified | needs safe derived projection rather than direct ledger ownership | none | none | later projection and envelope tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection` | `Band F` | Limits must remain safe projection only. |
| `case.root`, `case.list`, `case.open`, `case.enter`, `case.leave`, `case.status` | `case` | `implemented_current` | case API exists only partially; `case.current`, `case.list`, `case.show` verified, but the full action family is incomplete | Rust/TS case surfaces are partial; current local CLI behavior is ahead of SDK/API | no immediate parser gap; later canonical output normalization still needed | Loom currently shows case posture text, not action-mapped `case_tree` and `case_panel` flows | runtime action keys remain mostly unverified because current CLI owns local state directly | no major substrate gap for local tree; later case read models may help | none | `case.current` remains compatibility wording | add P0 CLI snapshot tests for root/list/open/enter/leave/status and future Loom case-tree tests | `needs_api_operation`, `needs_sdk_surface`, `needs_tui_projection`, `needs_runtime_action_key` | `V51 + V58-V60 + Band D + V61-V67` | `cli/src/commands/case.rs` verifies real local case behavior and operator-context ownership without session revival. |
| `case.close` | `case` | `planned` | registry metadata should be corrected to reflect current local CLI reality | SDK/API still incomplete | no parser gap; current local close path already exists | Loom still missing case-close placeholder | runtime action keys unverified | none | none | none | add close-path tests and seed correction note | `ready_for_v51_registry_refactor`, `needs_api_operation`, `needs_sdk_surface`, `needs_tui_projection` | `V51 + V58-V60 + Band D + V61-V67` | Verified drift: `cli/src/commands/case.rs` already implements `case.close.local`, but the V50.9 seed still marked `case.close` as `planned`. |
| `context.status`, `context.current`, `context.switch`, `context.clear` | `context` | `unknown_needs_audit` | add explicit operator-context API family or formally hide under `case.*` | all SDK surfaces missing | no current CLI parser | Loom can surface operator-context state text, but not canonical context actions | runtime/backend truth likely overlaps operator-context markers, but public keys are unverified | none | none | none | audit-first before tests | `unknown_needs_source_audit`, `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection` | `V51 + later source audit` | Current repo surfaces favor `case enter/leave/status` over a separate `context` grammar. |
| `control.status`, `control.gates`, `control.explain` | `control` | `canonical_target` | verified control ops already exist for gates/explain; `control.status` still needs explicit mapping | TS already exposes control surfaces; Rust surface missing | no current CLI parser | Loom needs `control_panel` actions and disabled placeholders | runtime action keys still unverified | none | governance/control backend exists, but CLI/TUI wiring is absent | none | add read-only control explanation tests | `ready_for_v51_registry_refactor`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_runtime_action_key` | `V51 + V58-V60 + Band D + V61-V67` | Control should be one of the earliest canonical read-only families after registry normalization. |
| `control.decision`, `control.plan` | `control` | `planned` | add explicit `control.decision` and `control.plan` registry coverage | TS/Rust surfaces missing | no current CLI parser | Loom should expose unavailable/blocked entries in `control_panel` | runtime/control backend likely exists conceptually but not as verified public action keys | none | none | none | later plan/explanation tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_runtime_action_key` | `V51 + V58-V60 + Band D` | Keep these plan/explanation surfaces declarative, not mutating. |
| `govern.status`, `govern.policy.list`, `govern.policy.inspect`, `govern.policy.explain`, `govern.decision.explain` | `govern` | `canonical_target` | keep API family pluralized as `governance.*`; add action projections, not a new domain | TS governance surface exists; Rust surface missing | no current CLI parser | Loom needs a real `governance_panel` registry instead of generic status text only | runtime/governance action keys still unverified | none | governance backend exists | `govern` is a CLI projection over `governance.*` | add policy-resolution and decision-explain tests | `ready_for_v51_registry_refactor`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_governance_policy_path` | `V51 + V58-V60 + Band D + V61-V67` | Governance is closer to registry readiness than to CLI readiness. |
| `policy_pack.list`, `policy_pack.inspect`, `policy_pack.validate`, `policy_pack.explain` | `policy_pack` | `canonical_target` | add missing family and operations | all SDK surfaces missing | no current CLI parser | Loom needs disabled `policy_pack_panel` entries | no verified runtime action keys | none | needs governed catalog/policy-pack path rather than greenfield naming | root `policy` must not absorb this family | add P1 validation and explain tests after registry work | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_governance_policy_path` | `V51 + V58-V60 + Band D + V61-V67` | Policy-pack is one of the most important missing registry families for V51. |
| `policy.root` | `policy_pack` | `forbidden` | lock as forbidden | no SDK surface | no CLI parser should be added | Loom should hide or show developer-only forbidden placeholder | none | none | none | replace with `policy_pack.*` or `govern.policy.*` | no test beyond lock | `forbidden_locked` | `V51` | Root `policy` is too vague and must stay locked. |

### Intake, Materialization, State, Knowledge, and Lineage

| action_id | family | current_registry_status | api_gap | sdk_gap | cli_gap | tui_gap | runtime_gap | storage_or_projection_gap | backend_reconnection_gap | legacy_alias_gap | test_gap | refactor_class | next_wave | notes |
| --------- | ------ | ----------------------- | ------- | ------- | ------- | ------- | ----------- | ------------------------- | ------------------------ | ---------------- | -------- | -------------- | --------- | ----- |
| `intake.plan`, `intake.run`, `intake.status`, `intake.inspect`, `intake.validate` | `intake` | `canonical_target`, `planned` | add explicit intake family and operations | all SDK surfaces missing | no current CLI parser | Loom needs `intake_panel` forms and unavailable placeholders | no verified public runtime action keys | later outputs/evidence/state read models needed | evidence suggests reconnection, not pure greenfield | none | add P1 plan/validate tests and P2 run/status tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_materialization_path`, `needs_backend_reconnection` | `V51 + V58-V60 + Band D + Band E + V61-V67` | Intake was flattened during older CLI/source removal and must return as a first-class family. |
| `intake.outputs`, `intake.lineage` | `intake` | `planned` | add explicit output/lineage slices | all SDK surfaces missing | no current CLI parser | Loom needs output/detail placeholders | runtime action keys unverified | requires state/evidence/lineage projections | backend path should reconnect to state/lineage rather than stop at dry-run | none | add later output/lineage tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection`, `needs_lineage_path`, `needs_backend_reconnection` | `V51 + Band E + Band D + V61-V67` | Intake should not end at plan/run; outputs and lineage are part of the lifecycle. |
| `materialize.plan`, `materialize.run`, `materialize.status`, `materialize.inspect`, `materialize.validate` | `materialize` | `canonical_target`, `planned` | add explicit materialization family and operations | all SDK surfaces missing | no current CLI parser | Loom needs `materialization_panel` forms and blocked placeholders | public runtime action keys unverified | requires state outputs and evidence projection | strong backend evidence exists in `yai/state/materialization/materialize_runtime.c` | none | add P1 plan tests and P2 run/status tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_materialization_path`, `needs_backend_reconnection` | `V51 + V58-V60 + Band D + Band E + V61-V67` | Materialization is one of the clearest backend reconnection families, not a blank-slate feature. |
| `materialize.outputs`, `materialize.evidence`, `materialize.lineage` | `materialize` | `planned` | add explicit output/evidence/lineage ops | all SDK surfaces missing | no current CLI parser | Loom needs output/detail placeholders in `materialization_panel`, `evidence_panel`, `lineage_panel` | runtime action keys unverified | needs state, evidence, and lineage projection outputs | backend path exists conceptually but public wiring is absent | none | add later outputs/evidence/lineage tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection`, `needs_lineage_path`, `needs_backend_reconnection` | `V51 + Band E + Band D + V61-V67` | Materialization is incomplete until its outputs are inspectable. |
| `excerpt.list`, `excerpt.show`, `excerpt.inspect`, `excerpt.lineage` | `excerpt` | `planned` | add excerpt family or state-adjacent projections | all SDK surfaces missing | no current CLI parser | Loom needs detail placeholders in `records_panel` or `evidence_panel` | runtime action keys unverified | needs state/lineage projection | likely reconnect to materialization/state rather than greenfield | none | later excerpt and lineage tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection`, `needs_lineage_path`, `needs_backend_reconnection` | `V51 + Band E + Band D` | Excerpts are a lifecycle surface, not a free-floating object class. |
| `state.status`, `state.inspect`, `state.list`, `state.projections`, `state.materialized` | `state` | `canonical_target`, `planned` | add missing first-class state operations beyond record query/tail | TS state surface exists; Rust/Python/C are missing | no current CLI parser | Loom needs `state_panel` entries and unavailable placeholders | runtime action keys unverified | explicit state and projection reads still need public envelopes | backend evidence already exists in LMDB/DuckDB/state roots | root `records` currently obscures canonical state ownership | add P1 state status tests and later projection tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection`, `needs_backend_reconnection` | `V51 + V58-V60 + Band D + Band E + V61-V67` | State is one of the biggest registry holes because the repo already has real substrate ownership. |
| `state.records.list`, `state.records.tail`, `state.records.query` | `state` | `canonical_target`, `planned` | `state.records.query` and `state.records.tail` already exist; `state.records.list` still needs explicit op | TS and Rust already expose query/tail candidates; list remains absent | no current CLI parser | Loom needs `records_panel` search/tail placeholders | runtime action keys unverified | needs stable read-model and record projection envelopes | backend exists in state substrate | `records.* -> state.records.*` | add P1 query/tail tests and CLI JSON output tests | `ready_for_v51_registry_refactor`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection`, `needs_deprecation_path` | `V51 + V58-V60 + Band D + V61-V67` | This family is a high-confidence V51 normalization target because API and SDK already expose part of it. |
| `state.substrate.status`, `state.substrate.inspect.shm`, `state.substrate.inspect.lmdb`, `state.substrate.inspect.duckdb`, `state.substrate.inspect.ladybug` | `state` | `diagnostic_only`, `planned` | add diagnostic projection ops only if they stay read-only | no public SDK surfaces verified | no current CLI parser | Loom should expose diagnostic-only placeholders, not raw mutation | runtime action keys unverified | strong storage-layer read-model work needed; `LMDB` and `DuckDB` are real, `Ladybug` is still conceptual | backend evidence exists for `LMDB` and `DuckDB`; `Ladybug` remains future inspection boundary | none | later diagnostic-only tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection`, `needs_backend_reconnection` | `V51 + Band E + Band D` | `yai` currently has real substrate code for LMDB and DuckDB, but public action wiring must stay read-only. |
| `records.list`, `records.show`, `records.inspect`, `records.tail` | `records` | `legacy_compat` | keep out of new canonical API families | SDK should point callers to `state.records.*` | CLI alias may exist later, but should not remain primary | Loom should not promote root `records` as the owner | runtime/public ownership belongs under `state` | same projection work as `state.records.*` | none | `records.* -> state.records.*` | add deprecation and alias tests only | `legacy_locked`, `needs_deprecation_path` | `V51 + V61-V67` | Root `records` is transitional and should be treated as a migration shim. |
| `knowledge.status`, `knowledge.list`, `knowledge.show`, `knowledge.inspect`, `knowledge.query` | `knowledge` | `canonical_target` | only `knowledge.query` and `knowledge.lineage.trace` are verified today; the rest need explicit ops or projections | TS knowledge surface exists for query/lineage; Rust/Python/C are missing | no current CLI parser | Loom needs `knowledge_panel` entries and blocked placeholders | runtime action keys still unverified | needs knowledge read-models and safe view envelopes | backend exists, but knowledge ownership is mid-refactor in `yai` | none | add query/explain/read-only tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection`, `needs_backend_reconnection` | `V51 + V58-V60 + Band D + Band E` | `yai` currently shows pre-existing drift where knowledge surfaces are being split and re-homed; V50.10 records that drift rather than hiding it. |
| `knowledge.rebuild.plan`, `knowledge.rebuild` | `knowledge` | `planned` | add explicit rebuild ops only as gated diagnostics | all SDK surfaces missing | no current CLI parser | Loom should show unavailable placeholders only | runtime action keys unverified | depends on rebuildable projection contracts | backend path likely touches state/lineage/materialization | none | later gated rebuild tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection`, `needs_backend_reconnection` | `Band E + Band D` | Must remain gated and non-default. |
| `lineage.trace`, `lineage.show`, `lineage.explain`, `lineage.graph` | `lineage` | `canonical_target`, `planned` | `knowledge.lineage.trace` exists; first-class `lineage.*` family still missing | TS exposes `knowledge.lineageTrace()`; Rust/Python/C missing | no current CLI parser | Loom needs `lineage_panel` detail and graph placeholders | runtime action keys unverified | needs lineage graph/read projection | strong backend evidence exists in `include/orchestration/flow.h`, controlled-act docs, and graph/materialization anchors | lineage is still partially buried under `knowledge.*` | add P1 trace tests and later graph tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_lineage_path`, `needs_backend_reconnection` | `V51 + V58-V60 + Band D + Band E` | Lineage should become first-class instead of staying as `knowledge.lineage.*` only. |
| `recall.query`, `recall.explain`, `recall.inspect` | `recall` | `planned` | add explicit recall family or map clearly onto `knowledge.query` | all public SDK recall surfaces missing | no current CLI parser | Loom needs governed `recall_panel` placeholders | runtime action keys unverified | depends on knowledge/lineage/state projections | backend path depends on later memory/recall work | none | later governed recall tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_lineage_path`, `unknown_needs_source_audit` | `later source audit + Band D` | V50.6 already blocked premature memory/recall CLI flattening; this stays a later family. |
| `evidence.list`, `evidence.show`, `evidence.inspect`, `evidence.lineage` | `evidence` | `canonical_target` | add explicit evidence family or control/state adjacencies | all SDK surfaces missing | no current CLI parser | Loom needs `evidence_panel` placeholders | runtime action keys unverified | needs evidence projection and lineage joins | backend evidence exists through state/control records | none | later evidence/lineage tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection`, `needs_lineage_path`, `needs_backend_reconnection` | `V51 + Band E + Band D` | Evidence is present in the backend model, but not yet recovered as a public action family. |

### Providers, Models, Skills, Agents, Workflow, and Jobs

| action_id | family | current_registry_status | api_gap | sdk_gap | cli_gap | tui_gap | runtime_gap | storage_or_projection_gap | backend_reconnection_gap | legacy_alias_gap | test_gap | refactor_class | next_wave | notes |
| --------- | ------ | ----------------------- | ------- | ------- | ------- | ------- | ----------- | ------------------------- | ------------------------ | ---------------- | -------- | -------------- | --------- | ----- |
| `provider.list`, `provider.status`, `provider.inspect`, `provider.check`, `provider.capabilities`, `provider.config.status`, `provider.route.explain` | `provider` | `canonical_target`, `planned` | `providers.list` and `providers.probe` are verified; other provider lifecycle ops need canonical additions | TS and Rust expose list/probe only; Python/C action surfaces missing | current CLI only exposes shallow `yai provider list` | Loom needs `provider_panel` lifecycle placeholders, not just generic text | public runtime action keys still mostly unverified | later outputs/evidence/log projections needed | backend path is partial, not absent | singular CLI must keep mapping to plural API family `providers.*` | add P1 list/check tests and later inspect/route tests | `ready_for_v51_registry_refactor`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_backend_reconnection` | `V51 + V58-V60 + Band D + Band E + V61-V67` | `cli/src/commands/provider.rs` proves current CLI is shallow; readiness work must restore the full lifecycle. |
| `provider.call.plan`, `provider.call.run`, `provider.call.inspect`, `provider.call.logs`, `provider.call.evidence`, `provider.call.lineage` | `provider` | `planned`, `runtime_internal` | add execution and observation ops | all public SDK surfaces missing | no current CLI parser | Loom needs disabled lifecycle placeholders in `provider_panel` and `logs_panel` | strong runtime reconnection needed | needs logs, evidence, and lineage projections | backend pieces likely exist but were flattened during older CLI/source removal | none | later execution, logs, evidence, and lineage tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_runtime_action_key`, `needs_storage_projection`, `needs_backend_reconnection`, `needs_lineage_path` | `V51 + Band E + Band D + V58-V60 + V61-V67` | Provider readiness/list alone is explicitly not enough after V50.8. |
| `model.list`, `model.status`, `model.inspect`, `model.check`, `model.capabilities`, `model.route.explain` | `model` | `canonical_target`, `planned` | `models.list` and `models.capabilities.show` are verified; other lifecycle ops still missing | TS and Rust expose list/capabilities only; Python/C missing | current CLI only exposes plural `yai models list` | Loom needs `model_panel` placeholders | runtime action keys still mostly unverified | later outputs/evidence projections needed | backend path is partial | plural CLI alias must map to singular canonical `model.*` | add P1 list/inspect tests and later route tests | `ready_for_v51_registry_refactor`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_backend_reconnection` | `V51 + V58-V60 + Band D + Band E + V61-V67` | Public CLI should normalize to singular `model` while API/SDK stay pluralized as `models.*`. |
| `model.run.plan`, `model.run`, `model.run.inspect`, `model.run.evidence`, `model.run.lineage` | `model` | `planned`, `runtime_internal` | add explicit execution ops | all public SDK surfaces missing | no current CLI parser | Loom needs disabled lifecycle placeholders in `model_panel` | strong runtime reconnection needed | needs evidence and lineage projection | backend pieces exist in model/provider/runtime planes, but public path is missing | none | later execution/evidence/lineage tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_runtime_action_key`, `needs_storage_projection`, `needs_backend_reconnection`, `needs_lineage_path` | `V51 + Band E + Band D + V58-V60 + V61-V67` | No free model invocation path should be implied. |
| `skills.list`, `skills.status`, `skills.inspect`, `skills.check`, `skills.route.explain` | `skills` | `planned`, `api_only` | add explicit skill family ops and action projections | all public SDK surfaces missing | no current CLI parser | Loom needs `skills` placeholders later, probably under developer/capability panels | runtime action keys unverified | minimal projection work for read-only skill registry | backend capability plane exists in `yai`, but surface is not public | none | later registry/admissibility tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_backend_reconnection` | `V51 + Band E + Band D + V58-V60` | Skills are a real family and should not stay list-only or hidden forever. |
| `skills.run.plan`, `skills.run` | `skills` | `planned` | add explicit run ops | all SDK surfaces missing | no current CLI parser | Loom should show unavailable placeholders only | runtime action keys unverified | later outputs/evidence storage work | backend exists conceptually but is not surfaced | none | later run-path tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_runtime_action_key`, `needs_backend_reconnection` | `Band E + V58-V60 + Band D` | Keep governed admission boundaries explicit. |
| `agent.list`, `agent.status`, `agent.inspect` | `agent` | `canonical_target`, `planned` | `agents.list` and `agents.trace` are the nearest verified ops; public inspect/status map still needs cleanup | TS exposes plural `agents` surfaces; Rust/Python/C missing | no current CLI parser | Loom needs `agent_panel` placeholders | runtime action keys unverified | later outputs/evidence/logs projection work | backend capability plane exists in `yai` | singular CLI must map to plural API family `agents.*` | add list/status/inspect tests later | `ready_for_v51_registry_refactor`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_backend_reconnection` | `V51 + V58-V60 + Band D + Band E` | Agent should not stay frozen at spawn-only language. |
| `agent.spawn.plan`, `agent.spawn`, `agent.stop`, `agent.logs`, `agent.outputs`, `agent.evidence`, `agent.lineage` | `agent` | `canonical_target`, `planned` | add full lifecycle ops | all public SDK surfaces missing beyond plural list/trace | no current CLI parser | Loom needs disabled lifecycle placeholders in `agent_panel` and `logs_panel` | strong runtime reconnection needed | needs logs/evidence/lineage/output projections | backend path likely exists in partial form | none | later execution/log/output/evidence tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_runtime_action_key`, `needs_storage_projection`, `needs_backend_reconnection`, `needs_lineage_path` | `V51 + Band E + Band D + V58-V60 + V61-V67` | Backend recovery should reconnect to case/control/runtime, not invent an agent-owned truth plane. |
| `workflow.list`, `workflow.status`, `workflow.inspect`, `workflow.plan` | `workflow` | `canonical_target`, `planned` | `workflow.list`, `workflow.show`, and `workflow.steps.pending` already exist; `workflow.plan` still needs explicit op | TS already exposes workflow list/show/stepsPending; Rust/Python/C missing | no current CLI parser; current docs still carry `flow` compatibility | Loom needs `workflow_panel` placeholders | runtime action keys still unverified | later outputs/logs/evidence projections needed | strong backend evidence exists in `sdk` ops and `yai/include/orchestration/flow.h` | `flow.* -> workflow.*` | add P1 workflow list/status/watch tests | `ready_for_v51_registry_refactor`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_backend_reconnection`, `needs_deprecation_path` | `V51 + V58-V60 + Band D + Band E + V61-V67` | Workflow is a major V51 target because the repo already has real backend and API anchors. |
| `workflow.run`, `workflow.stop`, `workflow.watch`, `workflow.outputs`, `workflow.evidence`, `workflow.lineage` | `workflow` | `canonical_target`, `planned` | `workflow.runs.watch` is verified; other run/stop/output/evidence ops are missing | TS exposes watch only; Rust/Python/C missing | no current CLI parser | Loom needs lifecycle placeholders in `workflow_panel` and `logs_panel` | runtime action keys still unverified | needs outputs/evidence/lineage projections | strong backend reconnection needed | `flow.* -> workflow.*` | later execution/watch/output/evidence tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_runtime_action_key`, `needs_storage_projection`, `needs_backend_reconnection`, `needs_lineage_path`, `needs_deprecation_path` | `V51 + Band E + Band D + V58-V60 + V61-V67` | Watch is ahead of run/stop in the current API/SDK surfaces. |
| `job.list`, `job.status`, `job.inspect`, `job.start.plan`, `job.start`, `job.cancel`, `job.logs`, `job.outputs`, `job.evidence`, `job.lineage` | `job` | `planned`, `runtime_internal` | add explicit job family | all SDK surfaces missing | no current CLI parser | Loom needs `job_panel` placeholders | runtime/public action keys unverified | needs logs/evidence/output projections | likely reconnects to workflow/runtime rather than starting greenfield | none | later job lifecycle tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_runtime_action_key`, `needs_storage_projection`, `needs_backend_reconnection`, `needs_lineage_path` | `Band E + V51 + Band D + V58-V60` | Job is one of the most under-modeled families today. |
| `lease.execution.list`, `lease.execution.status`, `lease.execution.inspect` | `lease` | `runtime_internal` | leave API exposure undecided until execution-lease ownership is clearer | no SDK surface | no CLI parser | Loom should keep this hidden or developer-only | runtime/private path likely exists conceptually | may need cache/lease diagnostics later | none | none | low-priority diagnostic tests only | `unknown_needs_source_audit`, `needs_runtime_action_key`, `needs_tui_projection` | `later source audit` | Execution lease remains one of the least mature public families. |

### Runtime, Diagnostics, Logs, Analytics, Release, Shell, Client, Session, and Forbidden Roots

| action_id | family | current_registry_status | api_gap | sdk_gap | cli_gap | tui_gap | runtime_gap | storage_or_projection_gap | backend_reconnection_gap | legacy_alias_gap | test_gap | refactor_class | next_wave | notes |
| --------- | ------ | ----------------------- | ------- | ------- | ------- | ------- | ----------- | ------------------------- | ------------------------ | ---------------- | -------- | -------------- | --------- | ----- |
| `analytics.status`, `analytics.summary`, `analytics.inspect` | `analytics` | `planned` | add analytics family or explicit derived views | no SDK surfaces verified | no current CLI parser | Loom needs `analytics_panel` placeholders | runtime action keys unverified | strong projection work required | likely later backend work, not immediate | none | later analytics tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection` | `Band F` | Analytics stays derived and non-authoritative. |
| `logs.runtime`, `logs.job`, `logs.workflow`, `logs.agent`, `logs.provider` | `logs` | `diagnostic_only` | add scoped log/read operations | no SDK surfaces verified | no current CLI parser | Loom needs `logs_panel` placeholders and palette entries | runtime action keys unverified | strong logs/read-model projection work needed | partial backend evidence only | none | later log-tail and diagnostics tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection`, `needs_backend_reconnection` | `Band E + Band D + V51` | Root logs were intentionally rejected; scoped logs still need real projections. |
| `runtime.status` | `runtime` | `legacy_compat` | keep as compatibility projection over `system.status` | Rust runtime compat surface exists; TS/Python/C action model incomplete | current CLI already exposes `yai runtime status` | Loom already exposes `/runtime` and `/status`, but not as `action_id`-backed aliases | none major | none | none | `runtime.status -> system.status` | add alias and parity tests | `legacy_locked`, `needs_deprecation_path` | `V51 + V61-V67 + Band D` | `cli/src/commands/runtime.rs` already uses operation id `system.status`, so the legacy surface is a projection issue, not a backend issue. |
| `runtime.diagnostics` | `runtime` | `diagnostic_only` | add explicit diagnostic operation or keep as doc-only | no SDK surface verified | no current CLI parser | Loom should likely absorb this into `runtime_panel` rather than a new root command | runtime action keys unverified | may need runtime/log projection | partial backend evidence only | none | later diagnostic tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection` | `V51 + Band D` | Keep runtime root diagnostic-only. |
| `runtime.start`, `runtime.stop`, `runtime.restart` | `runtime` | `forbidden` | lock out at registry level | no SDK surfaces | no CLI parser should be added | Loom must hide these or show forbidden placeholders only | do not assign public runtime action keys | none | none | replace with service/bootstrap tooling only | no test beyond lock | `forbidden_locked` | `V51` | Domain CLI/TUI must not own runtime lifecycle. |
| `storage_substrate.status` | `storage_substrate` | `diagnostic_only` | add only if a read-only substrate summary is needed | no SDK surfaces verified | no current CLI parser | Loom may show developer-only placeholder | runtime action keys unverified | storage summary projection required | backend exists in `yai/state/substrate/*` | root substrate grammar should not overshadow nested `state.substrate.*` | later diagnostic-only tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_storage_projection` | `Band E + Band D` | Prefer nested `state.substrate.*` over root `substrate`. |
| `substrate.inspect.raw` | `storage_substrate` | `forbidden` | lock out at registry level | no SDK surfaces | no CLI parser should be added | Loom must hide it | none | raw substrate mutation/exposure stays forbidden | none | replace with `state.substrate.inspect.*` read-only projections | no test beyond lock | `forbidden_locked` | `V51` | Raw substrate inspection/mutation must never become public domain UX. |
| `release.status` | `release` | `planned` | add only if product/distribution boundary is formalized | no SDK surfaces | no current CLI parser | Loom settings/developer placeholder only | none | none | none | none | low-priority later tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection` | `Band F` | No fake artifact claims. |
| `update.status`, `update.check` | `update` | `planned` | add only if release/update policy becomes formal | no SDK surfaces | no current CLI parser | Loom settings/developer placeholder only | none | none | none | none | low-priority later tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection` | `Band F` | Keep update semantics separate from runtime lifecycle. |
| `download.status` | `download` | `planned` | add only if artifact/download boundary becomes formal | no SDK surfaces | no current CLI parser | Loom settings/developer placeholder only | none | none | none | none | low-priority later tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection` | `Band F` | No fake download behavior. |
| `shell.open`, `shell.list`, `shell.attach`, `shell.detach` | `shell` | `implemented_current` | canonical API operation candidates still unverified | no typed SDK shell surface verified | CLI already exposes truthful unavailable/current UX | Loom already has client-shell UX but not action-registry mapping | no runtime gap is required for truthful unavailable UX | none | real shell backend remains absent | none | add P0 CLI text/JSON tests and Loom palette mapping tests | `needs_api_operation`, `needs_sdk_surface`, `needs_tui_projection` | `V51 + V58-V60 + Band D` | `cli/src/commands/shell.rs` is already the model for truthful unavailable projection. |
| `client.list`, `client.status`, `client.attach`, `client.detach` | `client` | `diagnostic_only` | add explicit client family only if needed | no SDK surfaces verified as canonical client actions | no current CLI parser | Loom already models connection posture internally, but not as canonical `client.*` actions | runtime connection action keys unverified | none | partial client/connection backend exists in Loom posture logic | none | later connection posture tests | `needs_api_operation`, `needs_sdk_surface`, `needs_cli_projection`, `needs_tui_projection`, `needs_runtime_action_key` | `V51 + Band D + V58-V60 + V61-V67` | Client is secondary to shell in user-facing CLI, but Loom may need it as an internal action family. |
| `session.status` | `session_legacy` | `deprecated` | keep compatibility op only; mark deprecated | Rust SDK and CLI still expose it | no parser change required now; later hide or demote | Loom should keep it hidden or developer-only | none major | none | none | split toward `auth.*`, `case.*`, `shell.*`, and `client.*` | add legacy-only tests | `legacy_locked`, `needs_deprecation_path` | `V51 + V61-V67 + Band D` | `cli/src/commands/session.rs` already prints guidance to prefer auth/case/shell. |
| `session.attach`, `session.detach` | `session_legacy` | `deprecated` | no new API work; keep deprecated or remove from public docs later | no canonical SDK work | no CLI parser should be promoted | Loom should not surface them | none | none | none | replace with `shell.attach`, `shell.detach`, `client.attach`, `client.detach` | low-priority deprecation tests only | `legacy_locked`, `needs_deprecation_path` | `V51 + V61-V67` | Session attach/detach must not re-emerge as the ownership model. |
| `dev_wrapper.make.yai`, `dev_wrapper.make.info`, `dev_wrapper.install_service`, `dev_wrapper.cargo.run` | `dev_wrapper` | `diagnostic_only` | no API work | no SDK work | no CLI parser work; stay outside domain CLI | Loom should hide these | none | none | none | none | no domain tests | `legacy_locked` | `docs_only` | These are bootstrap/developer entrypoints, not domain actions. |
| `query.root` | `query` | `forbidden` | lock out | no SDK work | no CLI parser should be added | Loom must hide it | none | none | none | replace with `recall.query`, `knowledge.query`, or `state.records.query` | no test beyond lock | `forbidden_locked` | `V51` | Root query stays too vague. |
| `inspect.root` | `query` | `forbidden` | lock out | no SDK work | no CLI parser should be added | Loom must hide it | none | none | none | replace with family-local `inspect` verbs | no test beyond lock | `forbidden_locked` | `V51` | Root inspect stays too vague. |

## Priority Bands

```text
Band A — must fix in V51-V57
  API registry/surface correctness.

Band B — must fix in V58-V60
  SDK typed clients and generated/handwritten surface alignment.

Band C — must fix in V61-V67
  CLI command migration, docs, parser/output/test alignment.

Band D — TUI/Loom alignment
  action registry, palette, panels, unavailable placeholders.

Band E — runtime/backend reconnection
  provider/model/materialization/state/lineage/backend paths.

Band F — later product/platform
  account, billing-adjacent, release/download, cloud, admin/support.
```

Band consequences:

* Band A is about naming, family ownership, compatibility flags, and forbidden locks.
* Band B is where the action model becomes typed and transport-safe across SDKs.
* Band C is where user-visible CLI migration happens after the registry is stable.
* Band D is where Loom stops being a small slash-command registry and becomes an action projection consumer.
* Band E is where existing backend/runtime pieces are reconnected to the public action model.
* Band F stays intentionally later because it depends on product/platform surfaces that do not exist yet.

## V51 API Registry Refactor Readiness

V51 should answer the registry problem, not the implementation problem.

Required V51 registry work:

* Add missing families or first-class slices for `policy_pack`, `intake`, `materialize`, `state`, `lineage`, `skills`, `job`, `analytics`, `logs`, `machine`, `license`, `entitlement`, and `limits`.
* Normalize old or compatibility-facing registry families:
  - `flow.* -> workflow.*`
  - root `records.* -> state.records.*`
  - `runtime.status -> system.status` compatibility projection
  - singular CLI projections such as `provider`, `model`, `agent`, and `govern` should remain projections over plural or canonical API families `providers`, `models`, `agents`, and `governance`
* Mark session entries deprecated:
  - `session.status`
  - `session.attach`
  - `session.detach`
* Keep provider/model/agent API family names plural where already canonical in SDK/API.
* Add missing `materialize`, `intake`, `policy_pack`, and `lineage` actions instead of burying them under older families.
* Promote lineage actions to first-class family coverage instead of leaving them only under `knowledge.lineage.*`.
* Mark forbidden actions explicitly:
  - `runtime.start`
  - `runtime.stop`
  - `runtime.restart`
  - `query.root`
  - `inspect.root`
  - `policy.root`
  - `substrate.inspect.raw`

V51 registry readiness by family:

| Registry question | V50.10 answer |
| ----------------- | ------------- |
| Which families must be added? | `policy_pack`, `intake`, `materialize`, `state` first-class slices, `lineage`, `skills`, `job`, `analytics`, `logs`, and posture families around `machine`, `license`, `entitlement`, `limits`. |
| Which old families must be renamed or remapped? | `flow -> workflow`, root `records -> state.records`, CLI singular projections must stay projections over plural API families. |
| Which families must be marked legacy? | `session.*`, `runtime.status` as compatibility-only root, root `records.*`. |
| Which entries must stay forbidden? | root `query`, root `inspect`, root `policy`, raw substrate inspect, and runtime lifecycle verbs. |
| Which families are closest to V51 readiness? | `system`, `workflow`, `provider`, `model`, `state.records`, `control`, and `governance` because real API/SDK anchors already exist. |

## SDK Readiness

Verified current SDK posture:

* TypeScript already exposes meaningful slices for `system`, `workflow`, `governance`, `control`, `state`, `records`, `knowledge`, `providers`, `models`, `agents`, and compatibility `flow`.
* Rust already exposes meaningful slices for `system`, `case`, compatibility `runtime`, legacy `session`, `providers`, compatibility `provider`, and `models`.
* Python package exists in the repo, but this audit did not verify action-family surfaces there. `rg` over `sdk/packages/python/src` and `tests` returned no matching public operation families from the V50.10 target list.
* C package exists and contains runtime/control model helpers, but it is not yet aligned to the V50.9 action registry as a family-by-family typed client.

SDK actions closest to typed readiness:

* `system.status`
* `system.doctor`
* `workflow.list`
* `workflow.inspect`
* `workflow.watch`
* `control.explain`
* `control.gates`
* `govern.policy.explain`
* `state.records.query`
* `state.records.tail`
* `knowledge.query`
* `lineage.trace`
* `provider.list`
* `provider.check`
* `model.list`
* `model.capabilities`
* `agent.list`

SDK actions that still need surface creation in V58-V60:

* `policy_pack.*`
* `intake.*`
* `materialize.*`
* `state.status`, `state.inspect`, `state.projections`, `state.materialized`
* `knowledge.status`, `knowledge.inspect`, `knowledge.rebuild.*`
* `evidence.*`
* `job.*`
* `analytics.*`
* `logs.*`
* `machine.*`, `license.*`, `entitlement.*`, `limits.*`
* all `shell.*` and `client.*` actions if they ever get typed SDK ownership

Old naming still visible in SDK surfaces:

* `session.*` remains present in Rust and README compatibility guidance.
* `flow` remains present in TypeScript client compatibility surfaces.
* `records` remains a top-level TypeScript surface even though canonical ownership should converge under `state.records`.
* singular `provider` remains a Rust compatibility alias over plural `providers`.

## CLI Readiness

Current CLI state is no longer purely theoretical. The Rust CLI already proves
several truthful posture patterns.

Verified current behavior:

* `yai case status`
  - verified in `cli/src/commands/case.rs`
  - shows auth posture, case posture, root case, active case, and session posture separation
* `yai shell`
  - verified in `cli/src/commands/shell.rs`
  - exists and truthfully reports that shell is canonical UX vocabulary but not implemented in this build
* `yai runtime status`
  - verified in `cli/src/commands/runtime.rs`
  - currently uses operation id `system.status`, so it is already a compatibility projection over the future canonical `system` family
* `yai auth status`
  - verified in `cli/src/commands/auth.rs`
  - returns truthful local-dev or unauthenticated posture without reviving session as auth truth
* `yai provider list`
  - verified in `cli/src/commands/provider.rs`
  - is a shallow `providers.list` projection today
* `yai models list`
  - verified in `cli/src/commands/models.rs`
  - is a shallow plural compatibility projection today
* `yai session status`
  - verified in `cli/src/commands/session.rs`
  - is explicitly legacy-oriented and already nudges users toward `auth`, `case`, and `shell`

Current canonical CLI posture:

| Category | Actions |
| -------- | ------- |
| canonical now | `yai auth login --local-dev`, `yai auth status`, `yai auth logout`, `yai case root`, `yai case list`, `yai case open`, `yai case enter`, `yai case leave`, `yai case status`, `yai case close`, `yai shell`, `yai shell list`, `yai shell attach`, `yai shell detach` |
| compatibility alias now | `yai runtime status`, `yai case current`, `yai models list`, `yai session status` |
| truthful unavailable placeholder now | `yai shell`, `yai shell list`, `yai shell attach`, `yai shell detach`, plus any runtime/provider/models path blocked by missing SDK/API transport |
| missing parser entries | `system.*`, `control.*`, `govern.*`, `policy_pack.*`, `intake.*`, `materialize.*`, `state.*`, `lineage.*`, `knowledge.*`, `evidence.*`, `workflow.*`, `agent.*`, `job.*`, `analytics.*`, `logs.*`, `machine.*`, `license.*`, `limits.*` |

CLI output and test readiness:

* JSON output contracts still need explicit normalization for many seeded actions, even where the parser already exists.
* Snapshot tests are needed for:
  - `auth.*`
  - `case.*`
  - `shell.*`
  - `runtime.status`
  - `session.status`
* sealed/no-auth/local-dev/future-licensed test coverage is still shallow outside `auth` and `case`.
* `provider.list` and `models.list` need tests that lock in their current shallow/truthful behavior before deeper lifecycle work lands.

## Loom / TUI Readiness

Current Loom evidence is real but intentionally narrow.

Verified current Loom action registry:

* `loom/src/command/registry.rs` currently exposes only:
  - `/help`
  - `/status`
  - `/runtime`
  - `/runtime-ipc`
  - `/attach`
  - `/detach`
* `Ctrl+P` opens a palette, but the palette still consumes that small local command registry rather than the V50.9 `action_id` registry seed.

Panels and action families that should be explicit in Loom:

| Loom surface | Needed action posture |
| ------------ | --------------------- |
| `provider_panel` | show `provider.list`, `provider.check`, `provider.inspect`, and disabled provider-call lifecycle placeholders |
| `model_panel` | show `model.list`, `model.inspect`, `model.capabilities`, and disabled model-run lifecycle placeholders |
| `agent_panel` | show disabled `agent.list`, `agent.inspect`, `agent.spawn`, `agent.logs`, `agent.outputs` placeholders |
| `workflow_panel` | show `workflow.list`, `workflow.inspect`, `workflow.watch`, and disabled `workflow.run/stop/outputs` placeholders |
| `materialization_panel` | show disabled `materialize.plan`, `materialize.run`, `materialize.outputs`, `materialize.lineage` placeholders |
| `state_panel` | show `state.status`, `state.projections`, and nested substrate diagnostics placeholders |
| `lineage_panel` | show `lineage.trace` and disabled `lineage.graph` placeholder |
| `knowledge_panel` | show `knowledge.query`, `knowledge.inspect`, and blocked `knowledge.rebuild` placeholder |
| `evidence_panel` | show disabled `evidence.list` and `evidence.inspect` placeholders |
| `records_panel` | show `state.records.query`, `state.records.tail`, and root `records` should not be primary |
| `control_panel` | show `control.explain`, `control.gates`, and blocked `control.plan` placeholder |
| `governance_panel` | show `govern.status`, `govern.policy.inspect`, `govern.decision.explain` |
| `case_tree` | show `case.list`, `case.enter`, `case.leave`, `case.status` |
| `runtime_panel` | keep `runtime.status` compatibility and explicit `/runtime-ipc` probe |
| `system_panel` | show canonical `system.status`, `system.info`, `system.doctor`, `system.readiness` |
| `license_panel` | show unavailable/read-only license posture placeholders |
| `machine_panel` | show unavailable/read-only machine posture placeholders |
| `limits_panel` | show unavailable/read-only limit posture placeholders |

Loom visibility rules for V50.10:

* show canonical or planned actions as disabled/unavailable placeholders when the family matters to the domain
* hide forbidden actions entirely or show them only in developer docs
* require selection/ref context for:
  - `lineage.trace`
  - `evidence.inspect`
  - `records.inspect`
  - `workflow.inspect`
  - `agent.inspect`
  - `job.inspect`
* use richer lifecycle placeholders for:
  - provider/model/agent/workflow/materialization/state/lineage panels

## Runtime / Backend Reconnection Readiness

This band is where V50.10 is most important. Several actions do not need
greenfield backend work. They need reconnection to existing runtime/state
pieces.

Verified backend evidence:

| Family | Repo evidence | Recovery posture |
| ------ | ------------- | ---------------- |
| `provider` | `yai/README.md` capability-plane ownership plus provider/model transport boundaries in SDK and runtime docs | reconnect public action lifecycle to existing capability plane; do not stop at list/probe |
| `model` | `yai/README.md` capability-plane ownership plus model/runtime/backend language | reconnect lifecycle beyond list/capabilities |
| `agent` | `yai/README.md` and SDK `agents.*` surfaces | reconnect lifecycle through controlled-act/runtime boundaries rather than spawn-only language |
| `workflow` | `sdk/packages/rust/src/operations.rs` plus `yai/include/orchestration/flow.h` | rename/normalize `flow -> workflow` and reconnect run/watch/output/evidence/lineage |
| `job` | runtime/orchestration language exists, but public family is under-modeled | likely reconnect through workflow/runtime records rather than build isolated job truth |
| `intake` | docs and architecture narrative already imply governed intake | restore public lifecycle and connect to policy/materialization/state |
| `materialize` | `yai/state/materialization/materialize_runtime.c` plus related include fragments | reconnect to public action lifecycle; do not treat as missing backend |
| `policy_pack` | governance/catalog docs exist, but public family is missing | add registry family first, then reconnect to governance/catalog runtime path |
| `state` | `yai/state/substrate/lmdb_store.c`, `yai/state/substrate/duckdb_store.c`, `yai/state/README.md` | add public state/status/records/projection actions over real substrate ownership |
| `lineage` | `yai/Documentation/architecture/controlled-act-lifecycle.md`, graph/materialization anchors, and `knowledge.lineage.trace` API op | make first-class instead of leaving lineage buried under knowledge |
| `knowledge` | `knowledge.query` API op plus ongoing `yai` working-tree split between knowledge/read/recall surfaces | reconnect carefully; source audit still needed because working tree is mid-restructure |
| `records` | `state.records.query`, `state.records.tail`, `case.records.tail`, and state substrate | converge root records aliases onto state ownership |
| `evidence` | control/state record language and materialization/action evidence expectations | expose evidence as a first-class read family over real backend records |
| `logs` | Loom runtime feedback, CLI diagnostics, and runtime/readiness envelopes | build scoped logs projection rather than root logs catch-all |
| `analytics` | derived/inspection language exists in docs | likely later projection-only work; less ready than state/lineage/materialization |

Known source drift that V50.10 records explicitly:

* `yai` working tree currently shows pre-existing movement from `state/records/materialize_*` into `state/materialization/`.
* `yai` working tree also shows pre-existing knowledge/lineage/query/memory/session splits and deletions.
* V50.10 does not resolve that drift. It records that `materialize`, `knowledge`, `lineage`, and related actions will need a fresh source audit during implementation waves so V51-V67 do not normalize the wrong path.

## Forbidden / Legacy Lock

Locked decisions:

```text
runtime.start -> forbidden
runtime.stop -> forbidden
runtime.restart -> forbidden
query.root -> forbidden
inspect.root -> forbidden
policy.root -> forbidden
substrate.inspect.raw -> forbidden
session.attach -> deprecated
session.detach -> deprecated
session.status -> legacy_compat only
flow.* -> legacy alias to workflow.*
models.* CLI plural -> compatibility alias to model.*
records.* root -> transitional alias to state.records.*
```

Lock consequences:

* forbidden actions must exist only as explicit registry locks or hidden placeholders
* legacy actions may remain for migration, but they must not keep narrative ownership
* `flow`, `records`, `runtime`, `session`, and plural `models` compatibility language must not block canonical action-family cleanup

## Test Readiness Matrix

| action_id | CLI test needed | TUI test needed | SDK test needed | API conformance needed | runtime/backend test needed | priority | notes |
| --------- | --------------- | --------------- | --------------- | ---------------------- | --------------------------- | -------- | ----- |
| `system.status` | yes | yes | yes | yes | light inspect parity | `P0` | lock alias parity with `runtime.status` |
| `auth.login` | yes | later placeholder | yes when SDK exists | yes when API exists | no new runtime work yet | `P0` | production path still unavailable, but truthfulness matters |
| `auth.login.local_dev` | yes | no | no | no | no | `P0` | compatibility-only local-dev path |
| `auth.status` | yes | yes | yes when SDK exists | yes when API exists | no | `P0` | lock posture semantics and session separation |
| `auth.logout` | yes | later placeholder | yes when SDK exists | yes when API exists | no | `P0` | lock non-destructive logout boundaries |
| `case.root` | yes | later case-tree test | yes when SDK exists | yes when API exists | no | `P0` | current local CLI truth already exists |
| `case.list` | yes | yes | yes when SDK exists | yes when API exists | no | `P0` | active-case marker behavior matters |
| `case.open` | yes | later | yes when SDK exists | yes when API exists | no | `P0` | must stay non-selecting |
| `case.enter` | yes | yes | yes when SDK exists | yes when API exists | no | `P0` | operator-context ownership is critical |
| `case.leave` | yes | yes | yes when SDK exists | yes when API exists | no | `P0` | must not mutate session |
| `case.status` | yes | yes | yes when SDK exists | yes when API exists | no | `P0` | must remain available while sealed |
| `case.close` | yes | later | yes when SDK exists | yes when API exists | no | `P0` | registry seed status must be corrected |
| `shell.open` | yes | yes | no | no | no | `P0` | truthful unavailable UX pattern |
| `shell.list` | yes | later | no | no | no | `P0` | truthful unavailable UX pattern |
| `shell.attach` | yes | yes | no | no | no | `P0` | must not imply auth/case/session mutation |
| `shell.detach` | yes | yes | no | no | no | `P0` | must not imply logout/runtime stop |
| `runtime.status` | yes | yes | yes | yes | light inspect parity | `P0` | compatibility alias over `system.status` |
| `session.status` | yes | hidden/legacy | yes | yes | no | `P0` | legacy-only path |
| `provider.list` | yes | yes | yes | yes | no | `P1` | shallow current surface must stay truthful |
| `provider.check` | later | yes | yes | yes | maybe | `P1` | nearest verified op is `providers.probe` |
| `model.list` | yes | yes | yes | yes | no | `P1` | plural alias needs lock |
| `model.inspect` | later | yes | yes | yes | maybe | `P1` | capabilities and inspect drift still exist |
| `machine.status` | later | yes | later | later | later | `P1` | placeholder and posture contract only |
| `license.status` | later | yes | later | later | later | `P1` | safe projection only |
| `limits.status` | later | yes | later | later | later | `P1` | derived projection only |
| `control.explain` | later | yes | yes | yes | later | `P1` | high-value read-only posture surface |
| `policy_pack.validate` | later | yes | later | later | later | `P1` | key V51 addition |
| `intake.plan` | later | yes | later | later | later | `P1` | must be dry-run and governed |
| `materialize.plan` | later | yes | later | later | yes | `P1` | key backend reconnection family |
| `lineage.trace` | later | yes | yes | yes | yes | `P1` | first-class lineage readiness anchor |
| `state.status` | later | yes | later | later | yes | `P1` | first-class state readiness anchor |

## Final Handoff to V51

Concrete V51 recommendation:

```text
V51 should not try to implement commands.
V51 should refactor API registry around action families and legacy mapping.

V51 should:
  - add/normalize action family names;
  - mark session legacy/deprecated;
  - map flow -> workflow;
  - map records -> state.records;
  - keep provider/model/agent API plural while CLI projection may be singular;
  - add missing materialize/intake/policy_pack/lineage/state actions;
  - add forbidden-action markers;
  - align operation projections with yai-actions.v1.json.
```

V51 stop rule:

* if a task tries to implement CLI/TUI/runtime behavior during V51, it is out of scope
* if a task tries to normalize family names, compatibility mappings, forbidden locks, or action projections in the API registry, it is in scope

V50.10 exit condition:

* the canonical action registry is seeded
* every action family now has a verified refactor path
* V51 can start on registry normalization without needing another meta-wave
