# Canonical Action Descriptor Registry

## Status

* Delivery: V50.9
* Track: V — CLI/API/SDK/runtime/TUI action canon
* Branch: `refoundation/phase-01`
* Source of truth: this document
* Optional machine-readable seed: `api/registry/yai-actions.v1.json`

## Purpose

Create the first canonical `action_id` registry seed so CLI, TUI/Loom, SDK,
API, and runtime-aligned action surfaces all project from the same primitive.

The primitive is not the CLI string, the TUI button, or the API operation name.
The primitive is `action_id`.

## Non-goals

* not implementation
* not API registry refactor
* not SDK generation
* not CLI/TUI behavior
* not runtime behavior

## Descriptor Schema

Every seeded descriptor uses the following fields.

| Field | Meaning |
| ----- | ------- |
| `action_id` | canonical primitive across CLI, TUI, SDK, API, and runtime-aligned action registries |
| `family` | canonical family from the V50.6 command-system model |
| `lifecycle_stage` | lifecycle slice such as `catalog`, `status`, `inspect`, `plan`, `run`, or `forbidden` |
| `canonical_name` | stable human-readable action name |
| `description` | concise governed meaning of the action |
| `cli_projection` | preferred CLI projection string when one exists |
| `tui_projection` | label, location, and interaction kind for Loom/TUI projection |
| `api_operation_candidate` | nearest verified API operation or `none verified` |
| `sdk_surface_candidate` | nearest verified SDK surface or `none verified` |
| `runtime_action_key_candidate` | nearest verified runtime action key or `none verified` |
| `required_posture` | required auth/case/license/gate posture array |
| `availability` | visible availability state such as `available_diagnostic` or `blocked_by_case` |
| `implementation_status` | maturity/status vocabulary from V50.7/V50.8 |
| `test_priority` | `P0`, `P1`, `P2`, `P3`, or `N/A` |
| `aliases` | compatibility CLI or legacy action aliases |
| `forbidden` | explicit boolean for forbidden actions |
| `replacement_action_id` | canonical successor when the action is deprecated or forbidden |
| `notes` | caveats, drift markers, or canonical replacement notes |

## Family Registry

The seed attaches every command family from V50.6 to at least one canonical
descriptor and uses lifecycle coverage instead of shallow readiness-only
classification.

| Family | Lifecycle coverage in seed | Seed posture |
| ------ | -------------------------- | ------------ |
| `system` | `status`, `inspect`, `check`, `diagnostics` | canonical |
| `auth` | `run`, `status`, `compatibility` | canonical |
| `account` | `status`, `inspect` | planned |
| `machine` | `status`, `inspect`, `run` | planned |
| `license` | `status`, `check`, `inspect` | planned |
| `entitlement` | `status` | planned |
| `limits` | `status`, `explain` | planned |
| `case` | `catalog`, `status`, `inspect`, `run`, `cancel` | canonical |
| `context` | `status`, `inspect`, `run`, `cancel` | unresolved but seeded |
| `control` | `status`, `inspect`, `explain`, `plan` | canonical |
| `govern` | `status`, `catalog`, `inspect`, `explain` | canonical |
| `policy_pack` | `catalog`, `inspect`, `check`, `explain` | canonical target |
| `intake` | `plan`, `run`, `status`, `inspect`, `check`, `outputs`, `lineage` | canonical target |
| `materialize` | `plan`, `run`, `status`, `inspect`, `outputs`, `evidence`, `lineage`, `check` | canonical target |
| `excerpt` | `catalog`, `inspect`, `lineage` | planned |
| `records` | `catalog`, `inspect`, `watch`, `compatibility` | compatibility-only root |
| `evidence` | `catalog`, `inspect`, `lineage` | canonical target |
| `knowledge` | `status`, `catalog`, `inspect`, `check`, `plan`, `run` | canonical target |
| `state` | `status`, `inspect`, `catalog`, `watch`, `diagnostics` | canonical target |
| `lineage` | `inspect`, `explain`, `lineage` | canonical target |
| `recall` | `run`, `explain`, `inspect` | planned canonical |
| `query` | `forbidden` | root remains forbidden |
| `job` | `catalog`, `status`, `inspect`, `plan`, `run`, `watch`, `outputs`, `evidence`, `lineage`, `cancel` | planned canonical |
| `lease` | `catalog`, `status`, `inspect` | runtime-internal/diagnostic |
| `workflow` | `catalog`, `status`, `inspect`, `plan`, `run`, `watch`, `outputs`, `evidence`, `lineage`, `cancel` | canonical target |
| `agent` | `catalog`, `status`, `inspect`, `plan`, `run`, `watch`, `outputs`, `evidence`, `lineage`, `cancel` | canonical target |
| `provider` | `catalog`, `status`, `inspect`, `check`, `configure`, `plan`, `run`, `watch`, `outputs`, `evidence`, `lineage`, `explain` | canonical target |
| `model` | `catalog`, `status`, `inspect`, `check`, `plan`, `run`, `outputs`, `evidence`, `lineage`, `explain` | canonical target |
| `skills` | `catalog`, `status`, `inspect`, `check`, `plan`, `run`, `explain` | planned canonical |
| `runtime` | `diagnostics`, `compatibility`, `forbidden` | compatibility/forbidden split |
| `storage_substrate` | `diagnostics`, `forbidden` | diagnostic-only / forbidden raw |
| `analytics` | `status`, `inspect` | planned diagnostic |
| `logs` | `watch`, `inspect` | diagnostic-only |
| `release`, `update`, `download` | `status`, `check` | planned |
| `shell` | `run`, `catalog`, `compatibility` | canonical |
| `client` | `catalog`, `status`, `run`, `cancel` | diagnostic target |
| `session_legacy` | `status`, `run`, `cancel`, `compatibility` | deprecated |
| `dev_wrapper` | `run`, `diagnostics`, `compatibility` | non-domain wrapper |

## Action Descriptor Matrix

The full exact per-action seed lives in `api/registry/yai-actions.v1.json`.
Tables below summarize the grouped seed rows by family and show how the exact
registry rows are organized.

### System

| action_id | lifecycle_stage | CLI projection | TUI projection | API operation candidate | SDK surface candidate | runtime_action_key candidate | required posture | availability | implementation status | test priority | aliases | replacement | notes |
| --------- | --------------- | -------------- | -------------- | ----------------------- | -------------------- | ---------------------------- | ---------------- | ------------ | --------------------- | ------------- | ------- | ----------- | ----- |
| `system.status`, `system.readiness` | `status`, `diagnostics` | `yai system status`, `yai system readiness` | `System status`, `System readiness` | `system.status` | `client.system().status()` | `system.status.inspect` | `diagnostic_allowed` | `available_diagnostic` | `canonical_target` | `P0` | `yai runtime status` | none | canonical diagnostic roots |
| `system.info` | `inspect` | `yai system info` | `System info` | `system.runtime.inspect` | `client.system().runtimeInspect()` | `none verified` | `diagnostic_allowed` | `available_diagnostic` | `planned` | `P1` | none | none | detail surface |
| `system.doctor` | `check` | `yai system doctor`, `yai doctor` | `System doctor` | `system.check` | `client.system().check()` | `none verified` | `diagnostic_allowed` | `available_diagnostic` | `planned` | `P1` | `yai doctor` | none | health/probe surface |

### Auth / Account / Machine / License / Entitlement / Limits

| action_id | lifecycle_stage | CLI projection | TUI projection | API operation candidate | SDK surface candidate | runtime_action_key candidate | required posture | availability | implementation status | test priority | aliases | replacement | notes |
| --------- | --------------- | -------------- | -------------- | ----------------------- | -------------------- | ---------------------------- | ---------------- | ------------ | --------------------- | ------------- | ------- | ----------- | ----- |
| `auth.login`, `auth.login.local_dev`, `auth.logout` | `run`, `compatibility` | `yai auth login`, `yai auth login --local-dev`, `yai auth logout` | auth form and logout action | `auth.login`, `auth.logout`, `none verified` for local-dev | `none verified` | `none verified` | `no_auth_required`, `auth_required` | `available`, `legacy_only` for local-dev | `implemented_current`, `legacy_compat` | `P0` | none | none | local-dev remains bootstrap compatibility |
| `auth.status` | `status` | `yai auth status` | `Auth status` | `auth.status` | `none verified` | `none verified` | `diagnostic_allowed` | `available_diagnostic` | `implemented_current` | `P0` | none | none | auth posture root |
| `account.status`, `account.access`, `account.open` | `status`, `inspect` | `yai account status`, `yai account access`, `yai account open` | account panel actions | `none verified` | `none verified` | `none verified` | `auth_required` | `not_implemented` | `planned` | `P2` | none | none | no billing/profile internals |
| `machine.status`, `machine.identity.status`, `machine.evidence.status`, `machine.enroll`, `machine.authorization.status` | `status`, `inspect`, `run` | machine commands | machine panel actions | `none verified` | `none verified` | `none verified` | `auth_required`, `machine_authorization_required` | `not_implemented` | `planned` | `P1` | none | none | no raw hardware or fingerprint leakage |
| `license.status`, `license.lease.status`, `license.check`, `license.cache.status` | `status`, `check`, `inspect` | license commands | license panel actions | `none verified` | `none verified` | `none verified` | `auth_required`, `license_lease_required` | `not_implemented` | `planned` | `P1` | none | none | safe projection only |
| `entitlement.status` | `status` | `yai entitlement status` | `Entitlement status` | `none verified` | `none verified` | `none verified` | `auth_required`, `entitlement_required` | `not_implemented` | `planned` | `P1` | none | none | no billing object exposure |
| `limits.status`, `limits.explain` | `status`, `explain` | `yai limits status`, `yai limits explain` | limits panel actions | `none verified` | `none verified` | `none verified` | `auth_required`, `limit_projection_required` | `not_implemented` | `planned` | `P1` | none | none | shared-account limit projection only |

### Case / Context / Control / Govern / Policy Pack

| action_id | lifecycle_stage | CLI projection | TUI projection | API operation candidate | SDK surface candidate | runtime_action_key candidate | required posture | availability | implementation status | test priority | aliases | replacement | notes |
| --------- | --------------- | -------------- | -------------- | ----------------------- | -------------------- | ---------------------------- | ---------------- | ------------ | --------------------- | ------------- | ------- | ----------- | ----- |
| `case.root`, `case.list`, `case.open`, `case.enter`, `case.leave`, `case.status`, `case.close` | `catalog`, `inspect`, `run`, `status`, `cancel` | canonical `case` commands | case tree, case panel, operator context bar | `case.list`, `case.current`, `case.show`, `none verified` for some verbs | `client.case().list()` and current-case surfaces where verified | `case.open` verified; others `none verified` unless explicit | `auth_required`, `case_required`, `operator_context_required` | `available`, `blocked_by_auth`, `blocked_by_case` | `implemented_current`, `canonical_target`, `planned` mixed | `P0` | none | none | active case belongs to operator context, not session |
| `context.status`, `context.current`, `context.switch`, `context.clear` | `status`, `inspect`, `run`, `cancel` | `yai context ...` | operator context bar actions | `none verified` | `none verified` | `none verified` | `auth_required`, `operator_context_required` | `not_implemented` | `unknown_needs_audit` | `P2` | none | none | may stay behind `case` |
| `control.status`, `control.gates`, `control.explain`, `control.decision`, `control.plan` | `status`, `inspect`, `explain`, `plan` | control commands | control panel actions | `control.gates.list`, `control.gates.show`, `control.decisions.explain`, `none verified` for `plan` | TS `control` surfaces where verified; otherwise `none verified` | `none verified` | `auth_required`, `active_case_required`, `runtime_gate_required` | `available_read_only`, `blocked_by_active_case`, `blocked_by_runtime_gate` | `canonical_target`, `planned` | `P1` | none | none | control explains posture; it does not execute by itself |
| `govern.status`, `govern.policy.list`, `govern.policy.inspect`, `govern.policy.explain`, `govern.decision.explain` | `status`, `catalog`, `inspect`, `explain` | govern commands | governance panel actions | `governance.posture`, `governance.policy.resolve` | TS `governance` surfaces | `none verified` | `auth_required`, `case_required`, `policy_required` | `available_read_only`, `blocked_by_policy` | `canonical_target` | `P1` | `yai governance ...` | none | CLI spelling `govern` projects API family `governance` |
| `policy_pack.list`, `policy_pack.inspect`, `policy_pack.validate`, `policy_pack.explain` | `catalog`, `inspect`, `check`, `explain` | policy-pack commands | policy-pack panel actions | `none verified` | `none verified` | `none verified` | `auth_required`, `policy_required` | `not_implemented` | `canonical_target` | `P1` | none | none | explicit governed pack vocabulary |

### Intake / Materialize / Excerpt

| action_id | lifecycle_stage | CLI projection | TUI projection | API operation candidate | SDK surface candidate | runtime_action_key candidate | required posture | availability | implementation status | test priority | aliases | replacement | notes |
| --------- | --------------- | -------------- | -------------- | ----------------------- | -------------------- | ---------------------------- | ---------------- | ------------ | --------------------- | ------------- | ------- | ----------- | ----- |
| `intake.plan`, `intake.run`, `intake.status`, `intake.inspect`, `intake.validate`, `intake.outputs`, `intake.lineage` | `plan`, `run`, `status`, `inspect`, `check`, `outputs`, `lineage` | intake commands | intake panel, detail, lineage | `none verified` | `none verified` | `none verified` | `auth_required`, `case_required`, `policy_required`, `runtime_gate_required` | `not_implemented`, `blocked_by_case`, `blocked_by_policy` | `canonical_target` | `P1`, `P2` | none | none | candidate material is not direct knowledge |
| `materialize.plan`, `materialize.run`, `materialize.status`, `materialize.inspect`, `materialize.outputs`, `materialize.evidence`, `materialize.lineage`, `materialize.validate` | `plan`, `run`, `status`, `inspect`, `outputs`, `evidence`, `lineage`, `check` | materialize commands | materialization panel actions | `none verified` | `none verified` | `none verified` | `auth_required`, `active_case_required`, `policy_required`, `runtime_gate_required` | `not_implemented`, `blocked_by_active_case`, `blocked_by_runtime_gate` | `canonical_target` | `P1`, `P2` | none | none | first-class materialization family |
| `excerpt.list`, `excerpt.show`, `excerpt.inspect`, `excerpt.lineage` | `catalog`, `inspect`, `lineage` | excerpt commands | records/evidence detail actions | `none verified` | `none verified` | `none verified` | `auth_required`, `active_case_required` | `not_implemented` | `planned` | `P2` | none | none | excerpts are case-bound, not free-floating documents |

### State / Records / Knowledge / Lineage / Recall / Evidence

| action_id | lifecycle_stage | CLI projection | TUI projection | API operation candidate | SDK surface candidate | runtime_action_key candidate | required posture | availability | implementation status | test priority | aliases | replacement | notes |
| --------- | --------------- | -------------- | -------------- | ----------------------- | -------------------- | ---------------------------- | ---------------- | ------------ | --------------------- | ------------- | ------- | ----------- | ----- |
| `state.status`, `state.inspect`, `state.list`, `state.projections`, `state.materialized` | `status`, `inspect`, `catalog` | state commands | state panel actions | `none verified` except record-related slices | TS `state` surface | `none verified` | `diagnostic_allowed`, `auth_required`, `active_case_required` | `available_diagnostic`, `blocked_by_active_case` | `canonical_target` | `P1` | none | none | state is first-class |
| `state.records.list`, `state.records.tail`, `state.records.query` | `catalog`, `watch`, `inspect` | nested state-record commands | records panel actions | `state.records.query`, `state.records.tail`, `none verified` for `list` | `client.state().recordsQuery()`, `client.state().recordsTail()` | `none verified` | `auth_required`, `active_case_required` | `available_read_only`, `blocked_by_active_case` | `canonical_target`, `planned` | `P1`, `P2` | root `records.*` compat | none | canonical record ownership is under `state` |
| `state.substrate.status`, `state.substrate.inspect.shm`, `state.substrate.inspect.lmdb`, `state.substrate.inspect.duckdb`, `state.substrate.inspect.ladybug` | `diagnostics`, `inspect` | nested substrate commands | diagnostics panel actions | `none verified` | `none verified` | `none verified` | `diagnostic_allowed` | `available_diagnostic`, `not_implemented` | `diagnostic_only`, `planned` | `P2`, `P3` | none | none | diagnostic-only; no raw mutation |
| `records.list`, `records.show`, `records.inspect`, `records.tail` | `catalog`, `inspect`, `watch`, `compatibility` | root records commands | compatibility only | `state.records.query`, `state.records.tail`, `none verified` | `client.state().recordsQuery()`, `client.state().recordsTail()` | `none verified` | `auth_required`, `active_case_required` | `legacy_only` | `legacy_compat` | `P2` | none | `state.records.list`, `state.inspect`, `state.records.query`, `state.records.tail` | root `records` is transitional |
| `knowledge.status`, `knowledge.list`, `knowledge.show`, `knowledge.inspect`, `knowledge.query`, `knowledge.rebuild.plan`, `knowledge.rebuild` | `status`, `catalog`, `inspect`, `check`, `plan`, `run` | knowledge commands | knowledge panel actions | `knowledge.query`, `none verified` for rebuild/list/show | TS `knowledge` surfaces including `query()` and `lineageTrace()` where relevant | `knowledge.write` verified for write path; others `none verified` | `auth_required`, `active_case_required`, `runtime_gate_required` | `available_read_only`, `blocked_by_active_case`, `not_implemented` | `canonical_target`, `planned` | `P1`, `P2`, `P3` | none | none | knowledge is case-bound and governed |
| `lineage.trace`, `lineage.show`, `lineage.explain`, `lineage.graph` | `lineage`, `inspect`, `explain` | lineage commands | lineage panel actions | `knowledge.lineage.trace`, `none verified` for graph/show | `client.knowledge().lineageTrace()` | `none verified` | `auth_required`, `active_case_required` | `available_read_only`, `not_implemented` | `canonical_target`, `planned` | `P1`, `P3` | none | none | first-class lineage meaning despite nested repo ownership |
| `recall.query`, `recall.explain`, `recall.inspect` | `run`, `explain`, `inspect` | recall commands | recall panel actions | `knowledge.query`, `none verified` for explain/inspect | `client.knowledge().query()` | `none verified` | `auth_required`, `active_case_required`, `runtime_gate_required` | `not_implemented`, `blocked_by_active_case`, `blocked_by_runtime_gate` | `planned` | `P2` | none | none | governed recall, not global query |
| `evidence.list`, `evidence.show`, `evidence.inspect`, `evidence.lineage` | `catalog`, `inspect`, `lineage` | evidence commands | evidence panel actions | `none verified` | `none verified` | `none verified` | `auth_required`, `active_case_required` | `not_implemented` | `canonical_target` | `P2` | none | none | evidence is case-bound |

### Provider / Model / Skills

| action_id | lifecycle_stage | CLI projection | TUI projection | API operation candidate | SDK surface candidate | runtime_action_key candidate | required posture | availability | implementation status | test priority | aliases | replacement | notes |
| --------- | --------------- | -------------- | -------------- | ----------------------- | -------------------- | ---------------------------- | ---------------- | ------------ | --------------------- | ------------- | ------- | ----------- | ----- |
| `provider.list`, `provider.status`, `provider.inspect`, `provider.check`, `provider.capabilities`, `provider.config.status`, `provider.route.explain` | `catalog`, `status`, `inspect`, `check`, `configure`, `explain` | provider commands | provider panel actions | `providers.list`, `providers.probe`, `none verified` otherwise | `client.providers().list()`, `client.providers().probe()` | `none verified` | `diagnostic_allowed`, `auth_required`, `runtime_gate_required` | `available_diagnostic`, `not_implemented` | `canonical_target`, `planned` | `P1`, `P2` | none | none | provider family is deeper than list/status |
| `provider.call.plan`, `provider.call.run`, `provider.call.inspect`, `provider.call.logs`, `provider.call.evidence`, `provider.call.lineage` | `plan`, `run`, `inspect`, `watch`, `evidence`, `lineage` | provider call commands | provider detail and logs actions | `none verified` | `none verified` | `provider.call`, `provider.call.request` verified for run path | `auth_required`, `active_case_required`, `runtime_gate_required`, `entitlement_required` | `not_implemented`, `blocked_by_runtime_gate`, `blocked_by_entitlement` | `planned`, `runtime_internal` | `P2` | none | none | execution stays governed |
| `model.list`, `model.status`, `model.inspect`, `model.check`, `model.capabilities`, `model.route.explain` | `catalog`, `status`, `inspect`, `check`, `explain` | model commands | model panel actions | `models.list`, `models.capabilities.show`, `none verified` for others | `client.models().list()`, `client.models().capabilitiesShow()` | `none verified` | `diagnostic_allowed` | `available_diagnostic`, `not_implemented` | `canonical_target`, `planned` | `P1`, `P2` | `yai models list` | none | singular public grammar, plural API family |
| `model.run.plan`, `model.run`, `model.run.inspect`, `model.run.evidence`, `model.run.lineage` | `plan`, `run`, `inspect`, `evidence`, `lineage` | model run commands | model detail actions | `none verified` | `none verified` | `model.local.invoke`, `model.custom.invoke`, `model.hosted.invoke` | `auth_required`, `active_case_required`, `runtime_gate_required` | `not_implemented`, `blocked_by_runtime_gate` | `planned`, `runtime_internal` | `P2` | none | none | no free model invocation claim |
| `skills.list`, `skills.status`, `skills.inspect`, `skills.check`, `skills.route.explain`, `skills.run.plan`, `skills.run` | `catalog`, `status`, `inspect`, `check`, `explain`, `plan`, `run` | skills commands | skills panel actions | `skills.list`, `skills.admissibility.check`, `skills.resolve`, `skills.run` | `none verified` | `none verified` | `diagnostic_allowed`, `auth_required`, `runtime_gate_required` | `available_read_only`, `not_implemented` | `planned`, `api_only` | `P2` | none | none | skills are real capability family, not list-only |

### Agent / Workflow / Job / Lease

| action_id | lifecycle_stage | CLI projection | TUI projection | API operation candidate | SDK surface candidate | runtime_action_key candidate | required posture | availability | implementation status | test priority | aliases | replacement | notes |
| --------- | --------------- | -------------- | -------------- | ----------------------- | -------------------- | ---------------------------- | ---------------- | ------------ | --------------------- | ------------- | ------- | ----------- | ----- |
| `agent.list`, `agent.status`, `agent.inspect` | `catalog`, `status`, `inspect` | agent commands | agent panel actions | `agents.list`, `agents.trace` nearest for inspect/trace | `none verified` | `none verified` | `auth_required`, `active_case_required` | `not_implemented`, `blocked_by_active_case` | `canonical_target`, `planned` | `P2` | none | none | agent is case-bound |
| `agent.spawn.plan`, `agent.spawn`, `agent.stop`, `agent.logs`, `agent.outputs`, `agent.evidence`, `agent.lineage` | `plan`, `run`, `cancel`, `watch`, `outputs`, `evidence`, `lineage` | agent execution commands | agent detail/logs actions | `agents.plan`, `agents.run`, `agents.trace` | `none verified` | `agent.spawn` | `auth_required`, `active_case_required`, `runtime_gate_required`, `entitlement_required` | `not_implemented`, `blocked_by_runtime_gate`, `blocked_by_entitlement` | `canonical_target`, `planned`, `runtime_internal` | `P2` | none | none | deeper than spawn-only wording |
| `workflow.list`, `workflow.status`, `workflow.inspect`, `workflow.plan` | `catalog`, `status`, `inspect`, `plan` | workflow commands | workflow panel actions | `workflow.list`, `workflow.show`, `workflow.steps.pending` | `client.workflow().list()`, `client.workflow().show()`, `client.workflow().stepsPending()` | `none verified` | `auth_required`, `active_case_required` | `available_read_only`, `not_implemented` | `canonical_target`, `planned` | `P1`, `P2` | `yai flow list`, `yai flow status` | none | workflow is canonical, flow is compat |
| `workflow.run`, `workflow.stop`, `workflow.watch`, `workflow.outputs`, `workflow.evidence`, `workflow.lineage` | `run`, `cancel`, `watch`, `outputs`, `evidence`, `lineage` | workflow execution commands | workflow detail/log actions | `workflow.runs.watch`, `none verified` for some run/stop/output ops | `client.workflow().runsWatch()` | `none verified` | `auth_required`, `active_case_required`, `runtime_gate_required` | `not_implemented`, `blocked_by_runtime_gate` | `canonical_target`, `planned` | `P2` | `yai flow run`, `yai flow stop` | none | real backend depth exists even when public wiring is partial |
| `job.list`, `job.status`, `job.inspect`, `job.start.plan`, `job.start`, `job.cancel`, `job.logs`, `job.outputs`, `job.evidence`, `job.lineage` | `catalog`, `status`, `inspect`, `plan`, `run`, `cancel`, `watch`, `outputs`, `evidence`, `lineage` | job commands | job panel actions | `none verified` | `none verified` | `job.start` | `auth_required`, `active_case_required`, `machine_authorization_required`, `license_lease_required`, `entitlement_required`, `limit_projection_required`, `runtime_gate_required` | `not_implemented`, `blocked_by_runtime_gate`, `blocked_by_license_lease`, `blocked_by_machine_authorization` | `planned`, `runtime_internal` | `P2` | none | none | job is case-bound and governed |
| `lease.execution.list`, `lease.execution.status`, `lease.execution.inspect` | `catalog`, `status`, `inspect` | lease execution diagnostics | diagnostics panel actions | `none verified` | `none verified` | `none verified` | `auth_required`, `active_case_required`, `license_lease_required` | `not_implemented` | `runtime_internal` | `P3` | none | none | likely diagnostic/API-only |

### Runtime / Storage / Analytics / Logs / Shell / Client / Session Legacy / Dev Wrapper / Forbidden Roots

| action_id | lifecycle_stage | CLI projection | TUI projection | API operation candidate | SDK surface candidate | runtime_action_key candidate | required posture | availability | implementation status | test priority | aliases | replacement | notes |
| --------- | --------------- | -------------- | -------------- | ----------------------- | -------------------- | ---------------------------- | ---------------- | ------------ | --------------------- | ------------- | ------- | ----------- | ----- |
| `runtime.status`, `runtime.diagnostics` | `compatibility`, `diagnostics` | `yai runtime status`, `yai runtime diagnostics` | runtime panel actions | `system.status`, `none verified` | `client.runtime().status()` compat, `none verified` otherwise | `system.status.inspect` for status; `none verified` for diagnostics | `diagnostic_allowed` | `available_diagnostic` | `legacy_compat`, `diagnostic_only` | `P0`, `P2` | none | `system.status`, `system.info` | runtime root remains compatibility/diagnostic only |
| `storage_substrate.status`, `substrate.inspect.raw` | `diagnostics`, `forbidden` | `yai substrate status`, none | diagnostics panel or hidden placeholder | `none verified` | `none verified` | `none verified` | `diagnostic_allowed`, `forbidden` | `not_implemented`, `forbidden` | `diagnostic_only`, `forbidden` | `P3`, `N/A` | none | `state.substrate.status`, `state.substrate.inspect.*` | raw substrate root must not become public |
| `analytics.status`, `analytics.summary`, `analytics.inspect` | `status`, `inspect` | analytics commands | analytics panel actions | `none verified` | `none verified` | `none verified` | `auth_required`, `active_case_required` | `not_implemented` | `planned` | `P2` | none | none | derived analytics only |
| `logs.runtime`, `logs.job`, `logs.workflow`, `logs.agent`, `logs.provider` | `watch`, `inspect` | scoped logs commands | logs panel actions | `none verified` | `none verified` | `none verified` | `diagnostic_allowed`, `active_case_required` | `available_diagnostic`, `not_implemented` | `diagnostic_only`, `planned` | `P2` | none | none | scoped logs only |
| `release.status`, `update.status`, `update.check`, `download.status` | `status`, `check` | release/update/download commands | settings/developer panel actions | `none verified` | `none verified` | `none verified` | `no_auth_required` | `not_implemented` | `planned` | `P3` | none | none | no fake artifact claims |
| `shell.open`, `shell.list`, `shell.attach`, `shell.detach` | `run`, `catalog`, `cancel` | shell commands | home/client-shell actions | `none verified` | `none verified` | `none verified` | `diagnostic_allowed` | `available`, `available_diagnostic` | `implemented_current`, `canonical_target` | `P0` | none | none | shell is UX language, not domain ownership |
| `client.list`, `client.status`, `client.attach`, `client.detach` | `catalog`, `status`, `run`, `cancel` | client commands | client panel actions | `none verified` | `none verified` | `none verified` | `diagnostic_allowed` | `not_implemented` | `diagnostic_only` | `P2` | none | none | likely secondary to shell |
| `session.status`, `session.attach`, `session.detach` | `status`, `run`, `cancel`, `compatibility` | session legacy commands | hidden or developer-only placeholders | `session.status`, `session.current`, `none verified` | `client.session().status()` | `none verified` | `diagnostic_allowed` | `legacy_only` | `deprecated` | `P1` | none | `shell.open`, `client.attach`, `auth.status`, `case.status` split | session is not canonical domain ownership |
| `dev_wrapper.make.yai`, `dev_wrapper.make.info`, `dev_wrapper.install_service`, `dev_wrapper.cargo.run` | `run`, `diagnostics`, `compatibility` | `make yai`, `make info`, `make install-service`, `cargo run ...` | hidden/developer panel only | `none verified` | `none verified` | `none verified` | `no_auth_required` | `available_diagnostic` | `dev_wrapper` | `N/A` | none | none | not domain CLI |
| `runtime.start`, `runtime.stop`, `runtime.restart`, `query.root`, `inspect.root`, `policy.root` | `forbidden` | none | hidden unavailable placeholders | `none verified` | `none verified` | `none verified` | `forbidden` | `forbidden` | `forbidden` | `N/A` | none | `system.status` or family-local replacements | forbidden roots or lifecycle control |

## Legacy Alias Mapping

| Legacy form | Canonical mapping | Registry rule |
| ----------- | ----------------- | ------------- |
| `flow.*` | `workflow.*` | keep only as compatibility aliases or deprecated descriptors |
| CLI `models.*` | `model.*` | public CLI normalizes to singular `model`; API/SDK family may remain plural |
| `session.*` | split into `shell.*`, `client.*`, `auth.*`, and `case.*` | no canonical session ownership revival |
| `runtime.status` | `system.status` | runtime root stays compatibility only |
| `records.*` | `state.records.*` | root `records` is transitional compatibility only |
| `query.root` | `recall.query` or scoped `knowledge` / `state.records` query | root query stays forbidden |
| `inspect.root` | family-local `inspect` verbs | root inspect stays forbidden |
| `policy.root` | `policy_pack.*` or `govern.policy.*` | root policy stays forbidden |

## TUI Projection Mapping

| action_id cluster | TUI location | Interaction kind |
| ----------------- | ------------ | ---------------- |
| `system.*`, `runtime.*` | `system_panel`, `runtime_panel`, `diagnostics_panel` | `status_badge`, `diagnostic_panel`, `read_only_view` |
| `auth.*`, `account.*`, `machine.*`, `license.*`, `entitlement.*`, `limits.*` | `auth_panel`, `account_panel`, `machine_panel`, `license_panel`, `limits_panel` | `form_action`, `detail_action`, `status_badge`, `read_only_view` |
| `case.*`, `context.*` | `case_panel`, `case_tree`, `operator_context_bar` | `context_action`, `panel_action`, `detail_action` |
| `control.*`, `govern.*`, `policy_pack.*` | `control_panel`, `governance_panel`, `policy_pack_panel` | `panel_action`, `detail_action`, `form_action`, `read_only_view` |
| `intake.*`, `materialize.*` | `intake_panel`, `materialization_panel` | `form_action`, `panel_action`, `detail_action`, `wizard_action` |
| `state.*`, `records.*`, `knowledge.*`, `lineage.*`, `recall.*`, `evidence.*`, `excerpt.*` | `state_panel`, `records_panel`, `knowledge_panel`, `lineage_panel`, `recall_panel`, `evidence_panel` | `read_only_view`, `detail_action`, `context_action`, `command_palette_action` |
| `provider.*`, `model.*`, `skills.*`, `agent.*`, `workflow.*`, `job.*`, `lease.*` | `provider_panel`, `model_panel`, `agent_panel`, `workflow_panel`, `job_panel`, `developer_panel` | `detail_action`, `panel_action`, `form_action`, `context_action`, `unavailable_placeholder` |
| `logs.*`, `analytics.*` | `logs_panel`, `analytics_panel`, `diagnostics_panel` | `diagnostic_panel`, `read_only_view`, `status_badge` |
| `shell.*`, `client.*`, `session.*` | `home`, `global_command_palette`, `developer_panel`, `hidden` | `command_palette_action`, `context_action`, `unavailable_placeholder` |
| forbidden roots | `hidden` | `unavailable_placeholder` |

## API / SDK Gap Summary

| action_id | missing API op | missing SDK surface | current nearest op/surface | V51/V58+ action needed |
| --------- | -------------- | ------------------- | -------------------------- | ---------------------- |
| `policy_pack.validate` | yes | yes | none verified | introduce governance/catalog pack ops and typed SDK surface |
| `intake.plan` | yes | yes | none verified | formalize intake family and request/response contracts |
| `materialize.run` | yes | yes | none verified; runtime/materialization anchors exist in `yai` only | formalize materialization registry family |
| `state.substrate.inspect.duckdb` | yes | yes | nested diagnostic concept only | decide public diagnostic contract |
| `knowledge.rebuild` | yes | yes | knowledge query exists; rebuild does not | decide guarded rebuild contract |
| `provider.call.run` | yes | yes | provider probe plus runtime gate docs only | formalize governed provider-call operation family |
| `model.run` | yes | yes | model capability ops plus runtime invoke keys | formalize governed model-run contract |
| `job.start` | yes | yes | case-bound job docs and runtime gate fixtures only | formalize job family |
| `lease.execution.status` | yes | yes | execution-lease docs only | decide whether lease stays internal or becomes diagnostic family |
| `analytics.summary` | yes | yes | analytics binding docs only | formalize analytics read-model family |

## Test Priority Summary

| Priority | Seed focus |
| -------- | ---------- |
| `P0` | `system.status`, `auth.status`, `auth.login`, `auth.logout`, `case.root`, `case.list`, `case.enter`, `case.status`, `shell.open`, `shell.attach`, `system`/`runtime` compatibility posture |
| `P1` | `control.*`, `govern.*`, `policy_pack.*`, `machine.authorization.status`, `license.*`, `limits.*`, `provider.*`, `model.*`, `state.*`, `lineage.trace` |
| `P2` | `intake.*`, `materialize.*`, `knowledge.*`, `recall.*`, `agent.*`, `workflow.*`, `job.*`, `analytics.*`, `logs.*`, `client.*` |
| `P3` | `state.substrate.*`, `lease.execution.*`, `release/update/download`, deep graph diagnostics, rebuild/watch slices not yet public |
| `N/A` | forbidden roots and dev-wrapper-only actions |
