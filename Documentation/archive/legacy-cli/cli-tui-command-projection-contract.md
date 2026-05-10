# CLI / TUI Command Projection Contract

## Status

* Delivery: V50.7
* Track: V — CLI/API/SDK/runtime/TUI command canon
* Branch: `refoundation/phase-01`
* Source of truth for projection: this document
* Depends on: `api/Documentation/cli/canonical-yai-command-system.md`

## Purpose

Define the shared projection contract used by:

* CLI command strings
* TUI / Loom actions, panels, menus, and palette entries
* SDK typed methods
* API operations
* runtime action registry alignment

CLI command strings are one projection. TUI actions are another projection. The
canonical primitive is the YAI action descriptor identified by `action_id`.

The command system reconstructed in V50.6 remains the domain/system model. V50.7
adds the missing projection layer so that CLI, Loom, SDK, API, and runtime do
not drift into separate action vocabularies.

Repository anchors used in this reconstruction:

* `api/Documentation/command-projection-model.md`
* `api/Documentation/api-operation-model.md`
* `api/schemas/operation-contract.v1.schema.json`
* `api/registry/api-operation-projections.v1.json`
* `api/Documentation/client/loom-client-alignment.md`
* `sdk/README.md`
* `sdk/packages/typescript/src/operations.ts`
* `sdk/Documentation/reports/refoundation-phase-3b-sdk-canonical-surface-cleanup.md`
* `cli/MIGRATION_MAP.md`
* `loom/src/command/registry.rs`
* `loom/src/tui/overlays/palette.rs`
* `loom/src/tui/screens/login.rs`
* `loom/src/tui/screens/client_shell.rs`
* `yai/Documentation/architecture/controlled-act-lifecycle.md`
* `yai/Documentation/audits/refoundation-map-v3.md`

## Non-goals

* not CLI implementation
* not TUI implementation
* not Loom UI redesign
* not registry refactor
* not SDK generation
* not runtime behavior

## Projection Rule

```text
Do not design CLI and TUI separately.
Do not let TUI invent actions that CLI/API/runtime cannot explain.
Do not let CLI command names become the only source of truth.
Every user-visible action should resolve to a canonical action_id.
```

Additional rule from V50.6 and the re-foundation map:

```text
Canonical action descriptors must preserve the governed operational cycle.
They must not flatten case/state/lineage/recall/control into vague UI verbs.
```

V50.8 extension:

```text
A capability family is not recovered when it only exposes list/status/readiness.
Every capability family should resolve to lifecycle-shaped action descriptors
where meaningful: catalog, status, inspect, check, configure, plan, run,
watch, outputs, evidence, lineage, cancel, and explain.
Some lifecycle stages may remain diagnostic_only, api_only, sdk_only,
runtime_internal, storage_internal, legacy_compat, or forbidden.
```

V50.9 extension:

```text
The projection contract is now seeded in a canonical action descriptor registry.
CLI strings, TUI actions, SDK method candidates, API operation candidates, and
runtime action key candidates should map back to the same `action_id`.
The first seed lives in `api/registry/yai-actions.v1.json`.
```

## Canonical Action Descriptor

Minimum descriptor fields in V50.7:

```text
action_id
action_family
action_name
canonical_description
cli_command
tui_label
tui_location
tui_interaction_kind
api_operation
sdk_surface
runtime_action_key
required_posture
input_contract
output_contract
confirmation_required
destructive
availability
test_priority
implementation_status
notes
```

Descriptor meaning:

| Field | Meaning |
| ----- | ------- |
| `action_id` | Canonical primitive. Stable identifier that every visible CLI/TUI action must resolve to. |
| `action_family` | Domain/action family from the V50.6 system model. |
| `action_name` | Action-local name under the family. |
| `canonical_description` | Human-readable statement of what the action means in governed YAI terms. |
| `cli_command` | Preferred CLI projection string when a CLI projection exists. |
| `tui_label` | Preferred TUI-visible label. |
| `tui_location` | Canonical panel, palette, bar, or hidden location for the TUI projection. |
| `tui_interaction_kind` | Menu item, form, detail action, badge, wizard, or placeholder behavior. |
| `api_operation` | Primary API operation when one exists; may be `none verified` if not yet stabilized. |
| `sdk_surface` | Typed SDK method or surface candidate when verified. |
| `runtime_action_key` | Runtime-local action identifier when verified by runtime/license/gate docs or fixtures. |
| `required_posture` | Auth/case/operator/gate/license/machine requirements. |
| `input_contract` | Required request shape or input form category. |
| `output_contract` | Shared envelope shape consumed by CLI and TUI. |
| `confirmation_required` | Whether the projection must ask for explicit confirmation. |
| `destructive` | Whether the action mutates or destroys user-visible state. |
| `availability` | How the action should present itself when gated or absent. |
| `test_priority` | P0/P1/P2/P3/N/A as shared validation expectation. |
| `implementation_status` | Projection/implementation maturity across repos. |
| `notes` | Drift, compatibility, composition, or caveat notes. |

Descriptor rules:

* `action_id` is the canonical primitive even when `cli_command` is absent.
* `action_id` does not need to equal `api_operation`.
* `api_operation` may be a primary operation inside a composed higher-level
  action.
* `runtime_action_key` should only be filled with a verified key or `none
  verified`.
* V50.9 adds a machine-readable seed in `api/registry/yai-actions.v1.json`.
* descriptors for the same family should collectively cover the family
  lifecycle, not only its shallow readiness slice.

Required status vocabulary:

```text
implemented_current
canonical_target
planned
diagnostic_only
api_only
sdk_only
runtime_internal
storage_internal
legacy_compat
deprecated
forbidden
unknown_needs_audit
```

Required TUI interaction kinds:

```text
menu_item
command_palette_action
panel_action
detail_action
form_action
wizard_action
context_action
status_badge
diagnostic_panel
read_only_view
destructive_action
unavailable_placeholder
```

Required TUI locations:

```text
global_command_palette
home
account_panel
auth_panel
case_panel
case_tree
operator_context_bar
runtime_panel
system_panel
control_panel
governance_panel
policy_pack_panel
intake_panel
materialization_panel
state_panel
knowledge_panel
lineage_panel
recall_panel
records_panel
evidence_panel
job_panel
workflow_panel
agent_panel
provider_panel
model_panel
machine_panel
license_panel
limits_panel
analytics_panel
logs_panel
settings_panel
diagnostics_panel
developer_panel
hidden
not_applicable
```

Required availability values:

```text
available
available_read_only
available_diagnostic
blocked_by_auth
blocked_by_case
blocked_by_active_case
blocked_by_machine_authorization
blocked_by_license_lease
blocked_by_entitlement
blocked_by_runtime_gate
blocked_by_limit
blocked_by_policy
blocked_by_manual_review
not_implemented
legacy_only
forbidden
```

## Projection Layers

| Layer | Projection | Owns domain truth? |
| ----- | ---------- | ------------------ |
| CLI | command string + flags | no |
| TUI / Loom | action/menu/panel/wizard | no |
| SDK | typed method | no, unless SDK wraps API operation |
| API | operation contract | no runtime truth; transport contract |
| runtime | action/gate/effect boundary | yes for runtime-local truth |
| storage/projection | substrate/read model | no semantic command ownership |

Repo-reality note:

* `api` already models `sdk`, `cli`, `tui`, and `agent` projections in
  `schemas/operation-contract.v1.schema.json`.
* `loom` already exposes palette and command-registry concepts with availability
  and confirmation policies.
* `sdk` already exposes richer typed families than the current Rust CLI.
* `yai` already expresses the deeper `operation -> case_action -> controlled_act`
  spine that action descriptors must respect.

## Capability Lifecycle Coverage

V50.7 now depends on the V50.8 recovery rule:

* `provider` must project more than `list/status`; the repo already exposes
  `providers.probe` and runtime/provider call authority boundaries.
* `model` must project more than `list/status`; the repo already exposes
  `models.capabilities.show` and governed provider/model access decisions.
* `workflow` must project more than `list/show`; the repo already exposes
  `workflow.steps.pending` and `workflow.runs.watch`.
* `state` must project more than root readiness; the repo already exposes
  `state.records.query` and `state.records.tail`.
* `knowledge` and `lineage` must project more than root inspection; the repo
  already exposes `knowledge.query` and `knowledge.lineage.trace`.
* `materialize` and `intake` must project plan/run/status/outputs lifecycles,
  even when public CLI/TUI projections remain planned.

Shared projection consequence:

```text
CLI may show only the actions it currently implements.
TUI may show richer unavailable placeholders and guided actions.
Neither CLI nor TUI may pretend that a family is canonically complete when only
its readiness/list slice exists.
```

See:

* `api/Documentation/cli/capability-command-recovery.md`

## Required Action Families

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

## Shared CLI / TUI Action Matrix

Posture vocabulary used in the matrix:

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

Test priority vocabulary:

```text
P0
P1
P2
P3
N/A
```

### System / Identity / Case / Context

| action_id | family | CLI projection | TUI projection | TUI location | TUI interaction kind | API operation candidate | SDK surface candidate | runtime_action_key candidate | required posture | availability | test priority | status | notes |
| --------- | ------ | -------------- | -------------- | ------------ | -------------------- | ----------------------- | -------------------- | ---------------------------- | ---------------- | ------------ | ------------- | ------ | ----- |
| `system.status` | `system` | `yai system status` | System status | `system_panel` | `status_badge` | `system.status` | `client.system().status()` | `system.status.inspect` | `diagnostic_allowed` | `available_diagnostic` | `P0` | `implemented_current` | Current CLI/runtime compatibility route is `yai runtime status`; Loom already has `/status` and `/runtime`. |
| `system.info` | `system` | `yai system info` | System info | `system_panel` | `detail_action` | `system.runtime.inspect` | `none verified` | `none verified` | `diagnostic_allowed` | `not_implemented` | `P1` | `canonical_target` | Split between status/info/readiness exists in docs but not yet in CLI/TUI. |
| `system.doctor` | `system` | `yai system doctor` | Run doctor | `diagnostics_panel` | `diagnostic_panel` | `system.check` | `none verified` | `none verified` | `diagnostic_allowed` | `available_diagnostic` | `P0` | `implemented_current` | Current projection is root `yai doctor`; future canonical nesting belongs under `system`. |
| `system.readiness` | `system` | `yai system readiness` | System readiness | `system_panel` | `status_badge` | `system.status` adjunct | `none verified` | `none verified` | `diagnostic_allowed` | `not_implemented` | `P1` | `canonical_target` | Should remain diagnostic and available while operational surfaces are sealed. |
| `auth.login` | `auth` | `yai auth login` | Log in | `auth_panel` | `form_action` | `auth.login` | `none verified` | `none verified` | `no_auth_required` | `available` | `P0` | `implemented_current` | Canonical CLI auth entrypoint. |
| `auth.login.local_dev` | `auth` | `yai auth login --local-dev` | Continue in local dev | `auth_panel` | `command_palette_action` | `auth.login` compat/local-dev mode | `none verified` | `none verified` | `no_auth_required` | `available` | `P0` | `implemented_current` | Development-only compatibility path; not account identity or entitlement. |
| `auth.status` | `auth` | `yai auth status` | Auth posture | `auth_panel` | `status_badge` | `auth.status` | `none verified` | `none verified` | `diagnostic_allowed` | `available_diagnostic` | `P0` | `implemented_current` | Must stay distinct from session/client attachment. |
| `auth.logout` | `auth` | `yai auth logout` | Log out | `account_panel` | `destructive_action` | `auth.logout` | `none verified` | `none verified` | `auth_required` | `available` | `P0` | `implemented_current` | Logout is not runtime stop and not case deletion. |
| `account.status` | `account` | `yai account status` | Account status | `account_panel` | `detail_action` | `identity.account.status` future | `none verified` | `none verified` | `auth_required` | `not_implemented` | `P2` | `planned` | Must not expose billing/account-profile internals. |
| `account.access` | `account` | `yai account access` | Access posture | `account_panel` | `detail_action` | `identity.account.access` future | `none verified` | `none verified` | `auth_required` | `not_implemented` | `P2` | `planned` | Safe posture only. |
| `account.open` | `account` | `yai account open` | Open account panel | `account_panel` | `panel_action` | `none verified` | `none verified` | `none verified` | `auth_required` | `not_implemented` | `P3` | `planned` | UI/navigation projection; not a billing surface. |
| `machine.status` | `machine` | `yai machine status` | Machine status | `machine_panel` | `detail_action` | `identity.machine.status` future | `none verified` | `none verified` | `auth_required` | `not_implemented` | `P1` | `planned` | No raw hardware or fingerprint output. |
| `machine.identity.status` | `machine` | `yai machine identity status` | Machine identity posture | `machine_panel` | `detail_action` | `identity.machine.identity.status` future | `none verified` | `none verified` | `auth_required` | `not_implemented` | `P1` | `planned` | Safe identity posture only. |
| `machine.evidence.status` | `machine` | `yai machine evidence status` | Machine evidence posture | `machine_panel` | `detail_action` | `identity.machine.evidence.status` future | `none verified` | `none verified` | `auth_required` | `not_implemented` | `P2` | `planned` | Safe evidence posture only. |
| `machine.enroll` | `machine` | `yai machine enroll` | Enroll machine | `machine_panel` | `wizard_action` | `identity.machine.enroll` future | `none verified` | `none verified` | `auth_required` | `not_implemented` | `P1` | `planned` | CLI/TUI may request enrollment; they do not issue authorization. |
| `machine.authorization.status` | `machine` | `yai machine authorization status` | Machine authorization | `machine_panel` | `status_badge` | `identity.machine.authorization.status` future | `none verified` | `none verified` | `auth_required + machine_authorization_required` | `not_implemented` | `P1` | `planned` | Consumes posture only. |
| `license.status` | `license` | `yai license status` | License posture | `license_panel` | `detail_action` | `license.status` future | `none verified` | `none verified` | `auth_required` | `not_implemented` | `P1` | `planned` | Must not leak billing/subscription objects. |
| `license.lease.status` | `license` | `yai license lease status` | Lease posture | `license_panel` | `status_badge` | `license.lease.status` future | `none verified` | `none verified` | `auth_required + license_lease_required` | `not_implemented` | `P1` | `planned` | Safe lease posture only. |
| `license.check` | `license` | `yai license check` | Check license posture | `license_panel` | `detail_action` | `license.check` future | `none verified` | `none verified` | `auth_required + license_lease_required` | `not_implemented` | `P1` | `planned` | Request/response posture only; not billing truth. |
| `license.cache.status` | `license` | `yai license cache status` | Lease cache posture | `license_panel` | `detail_action` | `license.cache.status` future | `none verified` | `none verified` | `auth_required + license_lease_required` | `not_implemented` | `P2` | `planned` | Reflects V44 cache posture boundary only. |
| `entitlement.status` | `entitlement` | `yai entitlement status` | Entitlement posture | `limits_panel` | `status_badge` | `identity.entitlement.status` future | `none verified` | `none verified` | `auth_required + entitlement_required` | `not_implemented` | `P1` | `planned` | Safe projection only. |
| `limits.status` | `limits` | `yai limits status` | Limits posture | `limits_panel` | `status_badge` | `limits.status` future | `none verified` | `none verified` | `auth_required + limit_projection_required` | `not_implemented` | `P1` | `planned` | Shared-account limit posture only. |
| `limits.explain` | `limits` | `yai limits explain` | Explain limits | `limits_panel` | `detail_action` | `limits.explain` future | `none verified` | `none verified` | `auth_required + limit_projection_required` | `not_implemented` | `P1` | `planned` | Explanation surface, not quota-ledger ownership. |
| `case.root` | `case` | `yai case root` | Root case | `case_panel` | `detail_action` | `case.root` future or local resolution | `none verified` | `none verified` | `auth_required` | `available` | `P0` | `implemented_current` | Current local-manifest anchor. |
| `case.list` | `case` | `yai case list` | Case list | `case_panel` | `read_only_view` | `case.list` | `client.case().list()` | `none verified` | `auth_required` | `available_read_only` | `P0` | `implemented_current` | Public case inventory projection. |
| `case.open` | `case` | `yai case open <path-or-uri>` | Open case | `case_panel` | `detail_action` | `case.show` plus local resolver | `none verified` | `case.open` | `auth_required + case_required` | `available` | `P0` | `implemented_current` | CLI path/URI opening is partly local, partly future API-backed. |
| `case.enter` | `case` | `yai case enter <case>` | Enter case | `case_tree` | `context_action` | `case.use` future | `none verified` | `none verified` | `auth_required + case_required + operator_context_required` | `available` | `P0` | `implemented_current` | Sets operator context; not session ownership. |
| `case.leave` | `case` | `yai case leave` | Leave case | `operator_context_bar` | `context_action` | `case.clear_current` future | `none verified` | `none verified` | `auth_required + operator_context_required` | `available` | `P1` | `implemented_current` | Clears active case posture, not auth/session. |
| `case.status` | `case` | `yai case status` | Case status | `operator_context_bar` | `status_badge` | `case.current` / `case.show` | `client.case().current()` | `none verified` | `diagnostic_allowed` | `available_diagnostic` | `P0` | `implemented_current` | Must remain available while operational work is sealed. |
| `case.close` | `case` | `yai case close <case>` | Close case | `case_panel` | `destructive_action` | `case.close` future | `none verified` | `none verified` | `auth_required + case_required` | `available` | `P1` | `implemented_current` | Closing case is not deleting evidence/knowledge by default. |
| `context.status` | `context` | `yai context status` | Context status | `operator_context_bar` | `status_badge` | `none verified` | `none verified` | `none verified` | `auth_required + operator_context_required` | `not_implemented` | `P2` | `unknown_needs_audit` | May remain hidden behind `case status`. |
| `context.current` | `context` | `yai context current` | Current context | `operator_context_bar` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + operator_context_required` | `not_implemented` | `P2` | `unknown_needs_audit` | Redundant with `case status` unless operator-context surface is extracted explicitly. |
| `context.switch` | `context` | `yai context switch <case>` | Switch context | `case_tree` | `context_action` | `none verified` | `none verified` | `none verified` | `auth_required + case_required + operator_context_required` | `not_implemented` | `P2` | `unknown_needs_audit` | If kept, should map to `case.enter` rather than invent a new domain. |
| `context.clear` | `context` | `yai context clear` | Clear context | `operator_context_bar` | `context_action` | `none verified` | `none verified` | `none verified` | `auth_required + operator_context_required` | `not_implemented` | `P2` | `unknown_needs_audit` | If kept, should map to `case.leave`. |

### Control / Governance / Policy Pack / Intake / Materialization

| action_id | family | CLI projection | TUI projection | TUI location | TUI interaction kind | API operation candidate | SDK surface candidate | runtime_action_key candidate | required posture | availability | test priority | status | notes |
| --------- | ------ | -------------- | -------------- | ------------ | -------------------- | ----------------------- | -------------------- | ---------------------------- | ---------------- | ------------ | ------------- | ------ | ----- |
| `control.status` | `control` | `yai control status` | Control status | `control_panel` | `status_badge` | `control.gates.show` / future `control.status` | `client.control` surface | `none verified` | `auth_required + runtime_gate_required` | `not_implemented` | `P1` | `canonical_target` | Control posture is explanatory, not execution by itself. |
| `control.gates` | `control` | `yai control gates` | Gates | `control_panel` | `detail_action` | `control.gates.list` | `client.control().gatesList()` candidate | `none verified` | `auth_required + runtime_gate_required` | `not_implemented` | `P1` | `canonical_target` | Preferred replacement for vague `runtime gates`. |
| `control.explain` | `control` | `yai control explain <action>` | Explain action | `control_panel` | `detail_action` | `control.decisions.explain` | `client.control().decisionsExplain()` candidate | `none verified` | `auth_required + active_case_required + runtime_gate_required` | `not_implemented` | `P1` | `canonical_target` | Should explain posture and denial reasons without side effects. |
| `control.decision` | `control` | `yai control decision <action>` | Decision posture | `control_panel` | `detail_action` | `control.decisions.explain` | `client.control().decisionsExplain()` candidate | `none verified` | `auth_required + active_case_required + runtime_gate_required` | `not_implemented` | `P2` | `planned` | May collapse into `control explain` depending later UX cleanup. |
| `control.plan` | `control` | `yai control plan` | Control plan | `control_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + runtime_gate_required` | `not_implemented` | `P2` | `planned` | Must stay declarative and not become runtime lifecycle control. |
| `govern.status` | `govern` | `yai govern status` | Governance status | `governance_panel` | `status_badge` | `governance.posture` | `client.governance().posture()` candidate | `none verified` | `auth_required + policy_required` | `not_implemented` | `P1` | `canonical_target` | CLI spelling `govern` projects API/SDK family `governance`. |
| `govern.policy.list` | `govern` | `yai govern policy list` | Policies | `governance_panel` | `read_only_view` | `governance.policy.resolve` adjunct / future list op | `client.governance` surface | `none verified` | `auth_required + policy_required` | `not_implemented` | `P2` | `planned` | List surface remains future. |
| `govern.policy.inspect` | `govern` | `yai govern policy inspect <policy>` | Inspect policy | `governance_panel` | `detail_action` | `governance.policy.resolve` adjunct | `client.governance` surface | `none verified` | `auth_required + policy_required` | `not_implemented` | `P2` | `planned` | Inspect must remain read-only. |
| `govern.policy.explain` | `govern` | `yai govern policy explain <policy>` | Explain policy | `governance_panel` | `detail_action` | `governance.policy.resolve` | `client.governance().policyResolve()` | `none verified` | `auth_required + policy_required` | `not_implemented` | `P1` | `canonical_target` | Explanation surface rather than raw registry dump. |
| `govern.decision.explain` | `govern` | `yai govern decision explain <decision>` | Explain governance decision | `governance_panel` | `detail_action` | `governance.posture` / future decision op | `client.governance` surface | `none verified` | `auth_required + case_required + policy_required` | `not_implemented` | `P1` | `canonical_target` | Should surface governance posture without inventing control truth. |
| `policy_pack.list` | `policy-pack` | `yai policy-pack list` | Policy packs | `policy_pack_panel` | `read_only_view` | `none verified` | `none verified` | `none verified` | `auth_required + policy_required` | `not_implemented` | `P2` | `canonical_target` | Restores explicit pack vocabulary. |
| `policy_pack.inspect` | `policy-pack` | `yai policy-pack inspect <pack>` | Inspect policy pack | `policy_pack_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + policy_required` | `not_implemented` | `P2` | `canonical_target` | Pack artifact view only. |
| `policy_pack.validate` | `policy-pack` | `yai policy-pack validate <pack>` | Validate policy pack | `policy_pack_panel` | `form_action` | `none verified` | `none verified` | `none verified` | `auth_required + policy_required + not_implemented` | `not_implemented` | `P1` | `canonical_target` | No policy execution without case/materialization context. |
| `policy_pack.explain` | `policy-pack` | `yai policy-pack explain <pack>` | Explain policy pack | `policy_pack_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + policy_required` | `not_implemented` | `P2` | `planned` | Separate from root `policy`, which remains too vague. |
| `intake.plan` | `intake` | `yai intake plan <source>` | Plan intake | `intake_panel` | `form_action` | `intake.plan` future | `none verified` | `none verified` | `auth_required + case_required + policy_required + not_implemented` | `not_implemented` | `P1` | `canonical_target` | Intake stages candidate material; it does not directly become knowledge. |
| `intake.run` | `intake` | `yai intake run <source>` | Run intake | `intake_panel` | `wizard_action` | `intake.run` future | `none verified` | `none verified` | `auth_required + active_case_required + policy_required + runtime_gate_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | Must remain policy-aware and case-bound. |
| `intake.status` | `intake` | `yai intake status <intake>` | Intake status | `intake_panel` | `status_badge` | `intake.status` future | `none verified` | `none verified` | `auth_required + case_required + not_implemented` | `not_implemented` | `P2` | `planned` | Run status should report governed posture, not raw worker state. |
| `intake.inspect` | `intake` | `yai intake inspect <intake>` | Inspect intake | `intake_panel` | `detail_action` | `intake.inspect` future | `none verified` | `none verified` | `auth_required + case_required + not_implemented` | `not_implemented` | `P2` | `planned` | Inspect candidate material and policy-pack binding safely. |
| `intake.validate` | `intake` | `yai intake validate <source>` | Validate intake source | `intake_panel` | `form_action` | `intake.validate` future | `none verified` | `none verified` | `auth_required + policy_required + not_implemented` | `not_implemented` | `P2` | `planned` | Read-only source/policy validation. |
| `materialize.plan` | `materialize` | `yai materialize plan <input>` | Plan materialization | `materialization_panel` | `form_action` | `materialization.plan` future | `none verified` | `none verified` | `auth_required + case_required + policy_required + not_implemented` | `not_implemented` | `P1` | `canonical_target` | Central missing family in current CLI. |
| `materialize.run` | `materialize` | `yai materialize run <plan>` | Run materialization | `materialization_panel` | `wizard_action` | `materialization.run` future | `none verified` | `none verified` | `auth_required + active_case_required + runtime_gate_required + policy_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | Must bind source/intake, policy-pack, and case outputs. |
| `materialize.status` | `materialize` | `yai materialize status <run>` | Materialization status | `materialization_panel` | `status_badge` | `materialization.status` future | `none verified` | `none verified` | `auth_required + case_required + not_implemented` | `not_implemented` | `P2` | `planned` | Status must explain governed/materialized posture. |
| `materialize.inspect` | `materialize` | `yai materialize inspect <run>` | Inspect materialization | `materialization_panel` | `detail_action` | `materialization.inspect` future | `none verified` | `none verified` | `auth_required + case_required + not_implemented` | `not_implemented` | `P2` | `planned` | Inspect plan/run bindings and outputs. |
| `materialize.outputs` | `materialize` | `yai materialize outputs <run>` | Materialization outputs | `materialization_panel` | `read_only_view` | `materialization.outputs` future | `none verified` | `none verified` | `auth_required + case_required + not_implemented` | `not_implemented` | `P2` | `planned` | Output view should link excerpts/records/evidence/knowledge/state. |
| `materialize.validate` | `materialize` | `yai materialize validate <plan>` | Validate materialization plan | `materialization_panel` | `form_action` | `materialization.validate` future | `none verified` | `none verified` | `auth_required + policy_required + not_implemented` | `not_implemented` | `P2` | `planned` | Validation is read-only. |

### Excerpt / Records / Evidence / Knowledge / State / Lineage / Recall / Query / Analytics / Logs

| action_id | family | CLI projection | TUI projection | TUI location | TUI interaction kind | API operation candidate | SDK surface candidate | runtime_action_key candidate | required posture | availability | test priority | status | notes |
| --------- | ------ | -------------- | -------------- | ------------ | -------------------- | ----------------------- | -------------------- | ---------------------------- | ---------------- | ------------ | ------------- | ------ | ----- |
| `excerpt.list` | `excerpt` | `yai excerpt list` | Excerpts | `records_panel` | `read_only_view` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | Excerpts are case-bound outputs, not free-floating documents. |
| `excerpt.show` | `excerpt` | `yai excerpt show <excerpt>` | Show excerpt | `records_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | |
| `excerpt.inspect` | `excerpt` | `yai excerpt inspect <excerpt>` | Inspect excerpt | `records_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `excerpt.lineage` | `excerpt` | `yai excerpt lineage <excerpt>` | Excerpt lineage | `lineage_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | Excerpt lineage should connect intake/materialization/state/evidence. |
| `records.list` | `records` | `yai records list` | Records | `records_panel` | `read_only_view` | `state.records.query` | `client.state().recordsQuery()` candidate | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `legacy_compat` | Transitional root; should converge under `state`. |
| `records.show` | `records` | `yai records show <record>` | Show record | `records_panel` | `detail_action` | `state.records.query` | `client.state().recordsQuery()` candidate | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `legacy_compat` | |
| `records.inspect` | `records` | `yai records inspect <record>` | Inspect record | `records_panel` | `detail_action` | `state.records.query` | `client.state().recordsQuery()` candidate | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `legacy_compat` | |
| `records.tail` | `records` | `yai records tail` | Tail records | `records_panel` | `read_only_view` | `state.records.tail` | `client.state().recordsTail()` candidate | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `legacy_compat` | Prefer eventual `state records tail`. |
| `evidence.list` | `evidence` | `yai evidence list` | Evidence | `evidence_panel` | `read_only_view` | `control.evidence.list` future | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | Evidence is case-bound and not provider/model-owned. |
| `evidence.show` | `evidence` | `yai evidence show <evidence>` | Show evidence | `evidence_panel` | `detail_action` | `control.evidence.show` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | |
| `evidence.inspect` | `evidence` | `yai evidence inspect <evidence>` | Inspect evidence | `evidence_panel` | `detail_action` | `control.evidence.show` / explicit future inspect op | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | |
| `evidence.lineage` | `evidence` | `yai evidence lineage <evidence>` | Evidence lineage | `lineage_panel` | `detail_action` | `knowledge.lineage.trace` adjunct / future evidence lineage op | `client.knowledge().lineageTrace()` candidate | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | Evidence lineage should remain case-bound and provenance-backed. |
| `knowledge.status` | `knowledge` | `yai knowledge status` | Knowledge status | `knowledge_panel` | `status_badge` | `knowledge.query` adjunct / future `knowledge.status` | `client.knowledge()` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | Knowledge is a case-bound derived plane. |
| `knowledge.list` | `knowledge` | `yai knowledge list` | Knowledge list | `knowledge_panel` | `read_only_view` | `knowledge.query` | `client.knowledge().query()` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | |
| `knowledge.show` | `knowledge` | `yai knowledge show <knowledge>` | Show knowledge | `knowledge_panel` | `detail_action` | `knowledge.query` / future `knowledge.show` | `client.knowledge().query()` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `knowledge.inspect` | `knowledge` | `yai knowledge inspect <knowledge>` | Inspect knowledge | `knowledge_panel` | `detail_action` | `knowledge.query` / future inspect op | `client.knowledge().query()` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | |
| `knowledge.rebuild` | `knowledge` | `yai knowledge rebuild` | Rebuild knowledge | `knowledge_panel` | `wizard_action` | `none verified` | `none verified` | `knowledge.write` not verified for rebuild | `auth_required + active_case_required + runtime_gate_required + policy_required + not_implemented` | `not_implemented` | `P3` | `planned` | Gated future maintenance action. |
| `state.status` | `state` | `yai state status` | State status | `state_panel` | `status_badge` | `state.records.query` / future `state.status` | `client.state()` | `none verified` | `diagnostic_allowed` | `not_implemented` | `P1` | `canonical_target` | State is first-class and should not stay hidden behind records. |
| `state.inspect` | `state` | `yai state inspect <ref>` | Inspect state | `state_panel` | `detail_action` | `state.records.query` | `client.state().recordsQuery()` candidate | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | |
| `state.list` | `state` | `yai state list` | State list | `state_panel` | `read_only_view` | `state.records.query` | `client.state().recordsQuery()` candidate | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | |
| `state.projections` | `state` | `yai state projections` | State projections | `state_panel` | `read_only_view` | `state.records.query` adjunct / future op | `client.state()` | `none verified` | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `canonical_target` | Projection list should distinguish canonical vs derived. |
| `state.materialized` | `state` | `yai state materialized` | Materialized state | `state_panel` | `read_only_view` | `state.records.query` adjunct / future op | `client.state()` | `none verified` | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `planned` | Maps to materialized outputs and read models. |
| `state.substrate.status` | `state` | `yai state substrate status` | Substrate status | `diagnostics_panel` | `diagnostic_panel` | `none verified` | `none verified` | `none verified` | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `diagnostic_only` | Summary only; no raw mutation. |
| `state.substrate.inspect.shm` | `state` | `yai state substrate inspect shm` | Inspect SHM posture | `diagnostics_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `diagnostic_only` | SHM is live runtime state, not public semantic truth. |
| `state.substrate.inspect.lmdb` | `state` | `yai state substrate inspect lmdb` | Inspect LMDB posture | `diagnostics_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `diagnostic_only` | LMDB is durable substrate only. |
| `state.substrate.inspect.duckdb` | `state` | `yai state substrate inspect duckdb` | Inspect DuckDB posture | `diagnostics_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `diagnostic_only` | DuckDB is derived/read-only projection. |
| `state.substrate.inspect.ladybug` | `state` | `yai state substrate inspect ladybug` | Inspect Ladybug posture | `diagnostics_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `diagnostic_allowed + not_implemented` | `not_implemented` | `P3` | `diagnostic_only` | Ladybug remains a future inspection boundary. |
| `lineage.trace` | `lineage` | `yai lineage trace <ref>` | Trace lineage | `lineage_panel` | `detail_action` | `knowledge.lineage.trace` | `client.knowledge().lineageTrace()` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P1` | `canonical_target` | Repo still nests lineage under knowledge, but CLI/TUI should expose first-class lineage meaning. |
| `lineage.show` | `lineage` | `yai lineage show <ref>` | Show lineage | `lineage_panel` | `detail_action` | `knowledge.lineage.trace` adjunct | `client.knowledge().lineageTrace()` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `lineage.explain` | `lineage` | `yai lineage explain <ref>` | Explain lineage | `lineage_panel` | `detail_action` | `knowledge.lineage.trace` adjunct | `client.knowledge().lineageTrace()` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `lineage.graph` | `lineage` | `yai lineage graph <ref>` | Lineage graph | `lineage_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P3` | `planned` | Later Ladybug-style graph inspection target. |
| `recall.query` | `recall` | `yai recall query <query>` | Recall query | `recall_panel` | `form_action` | `knowledge.query` / future `recall.query` | `client.knowledge().query()` | `none verified` | `auth_required + active_case_required + runtime_gate_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | Governed, case-bound recall only. |
| `recall.explain` | `recall` | `yai recall explain <query-or-result>` | Explain recall | `recall_panel` | `detail_action` | `knowledge.query` adjunct | `client.knowledge().query()` | `none verified` | `auth_required + active_case_required + runtime_gate_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `recall.inspect` | `recall` | `yai recall inspect <result>` | Inspect recall result | `recall_panel` | `detail_action` | `knowledge.query` adjunct | `client.knowledge().query()` | `none verified` | `auth_required + active_case_required + runtime_gate_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `query.root` | `query` | `yai query` | Query | `global_command_palette` | `unavailable_placeholder` | ambiguous | `none verified` | `none verified` | `forbidden` | `forbidden` | `N/A` | `forbidden` | Root query is too vague and should not become canonical truth. |
| `query.case` | `query` | `yai query case <query>` | Case query | `global_command_palette` | `command_palette_action` | `case.show` / `state.records.query` composite | `client.case` + `client.state` composite | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P3` | `planned` | Scoped replacement candidate if bare `query` is later revived. |
| `query.knowledge` | `query` | `yai query knowledge <query>` | Knowledge query | `knowledge_panel` | `form_action` | `knowledge.query` | `client.knowledge().query()` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P3` | `planned` | |
| `query.records` | `query` | `yai query records <query>` | Records query | `records_panel` | `form_action` | `state.records.query` | `client.state().recordsQuery()` candidate | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P3` | `planned` | |
| `query.evidence` | `query` | `yai query evidence <query>` | Evidence query | `evidence_panel` | `form_action` | `control.evidence.list` future / `state.records.query` composite | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P3` | `planned` | |
| `analytics.status` | `analytics` | `yai analytics status` | Analytics status | `analytics_panel` | `status_badge` | `analytics.status` future | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `planned` | Analytics is derived, not primary truth. |
| `analytics.summary` | `analytics` | `yai analytics summary` | Analytics summary | `analytics_panel` | `read_only_view` | `analytics.summary` future | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `analytics.inspect` | `analytics` | `yai analytics inspect <projection>` | Inspect analytics projection | `analytics_panel` | `detail_action` | `analytics.inspect` future | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `logs.runtime` | `logs` | `yai logs runtime` | Runtime logs | `logs_panel` | `diagnostic_panel` | `none verified` | `none verified` | `none verified` | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `diagnostic_only` | Scoped logs are preferable to bare `yai logs`. |
| `logs.job` | `logs` | `yai logs job <job>` | Job logs | `logs_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `diagnostic_only` | |
| `logs.workflow` | `logs` | `yai logs workflow <workflow>` | Workflow logs | `logs_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `diagnostic_only` | |
| `logs.agent` | `logs` | `yai logs agent <agent>` | Agent logs | `logs_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `diagnostic_only` | |
| `logs.provider` | `logs` | `yai logs provider <provider>` | Provider logs | `logs_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `diagnostic_only` | |

### Job / Lease / Workflow / Agent / Provider / Model / Skills / Runtime / Storage Root

| action_id | family | CLI projection | TUI projection | TUI location | TUI interaction kind | API operation candidate | SDK surface candidate | runtime_action_key candidate | required posture | availability | test priority | status | notes |
| --------- | ------ | -------------- | -------------- | ------------ | -------------------- | ----------------------- | -------------------- | ---------------------------- | ---------------- | ------------ | ------------- | ------ | ----- |
| `job.list` | `job` | `yai job list` | Jobs | `job_panel` | `read_only_view` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `planned` | Jobs are case-bound and not session/client owned. |
| `job.status` | `job` | `yai job status <job>` | Job status | `job_panel` | `status_badge` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `job.start` | `job` | `yai job start <spec>` | Start job | `job_panel` | `wizard_action` | `none verified` | `none verified` | `job.start` | `auth_required + active_case_required + machine_authorization_required + license_lease_required + entitlement_required + limit_projection_required + runtime_gate_required + not_implemented` | `not_implemented` | `P2` | `planned` | Verified runtime action key exists in V35/V36 fixtures. |
| `job.cancel` | `job` | `yai job cancel <job>` | Cancel job | `job_panel` | `destructive_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + runtime_gate_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `job.logs` | `job` | `yai job logs <job>` | Job logs | `job_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `job.lineage` | `job` | `yai job lineage <job>` | Job lineage | `lineage_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `lease.execution.status` | `lease` | `yai lease execution status <job>` | Execution lease status | `job_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + license_lease_required + not_implemented` | `not_implemented` | `P3` | `runtime_internal` | Keep internal/diagnostic until public ownership is explicit. |
| `lease.execution.list` | `lease` | `yai lease execution list` | Execution leases | `job_panel` | `read_only_view` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + license_lease_required + not_implemented` | `not_implemented` | `P3` | `runtime_internal` | |
| `lease.execution.inspect` | `lease` | `yai lease execution inspect <lease>` | Inspect execution lease | `job_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + license_lease_required + not_implemented` | `not_implemented` | `P3` | `runtime_internal` | |
| `workflow.list` | `workflow` | `yai workflow list` | Workflows | `workflow_panel` | `read_only_view` | `workflow.list` | `client.workflow().list()` | `none verified` | `auth_required + case_required` | `available_read_only` | `P1` | `implemented_current` | SDK/API family exists; CLI target still needs rename from legacy `flow`. |
| `workflow.status` | `workflow` | `yai workflow status <workflow>` | Workflow status | `workflow_panel` | `status_badge` | `workflow.show` | `client.workflow().show()` | `none verified` | `auth_required + active_case_required` | `available_read_only` | `P1` | `implemented_current` | Maps to workflow show/status projection. |
| `workflow.run` | `workflow` | `yai workflow run <workflow>` | Run workflow | `workflow_panel` | `wizard_action` | `workflow.runs.watch` composite / future run op | `client.workflow` surface | `none verified` | `auth_required + active_case_required + runtime_gate_required + not_implemented` | `not_implemented` | `P2` | `canonical_target` | Canonical replacement for legacy `flow run`. |
| `workflow.stop` | `workflow` | `yai workflow stop <workflow>` | Stop workflow | `workflow_panel` | `destructive_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + runtime_gate_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `workflow.inspect` | `workflow` | `yai workflow inspect <workflow>` | Inspect workflow | `workflow_panel` | `detail_action` | `workflow.show` | `client.workflow().show()` | `none verified` | `auth_required + active_case_required` | `available_read_only` | `P2` | `implemented_current` | |
| `workflow.lineage` | `workflow` | `yai workflow lineage <workflow>` | Workflow lineage | `lineage_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `agent.list` | `agent` | `yai agent list` | Agents | `agent_panel` | `read_only_view` | `agents.list` | `client.agents().list()` | `none verified` | `auth_required + active_case_required` | `available_read_only` | `P2` | `implemented_current` | SDK/API family exists; CLI projection is future. |
| `agent.status` | `agent` | `yai agent status <agent>` | Agent status | `agent_panel` | `status_badge` | `agents.trace` / future status op | `client.agents().trace()` | `none verified` | `auth_required + active_case_required` | `available_read_only` | `P2` | `implemented_current` | Trace currently stands in for richer inspect/status surfaces. |
| `agent.spawn` | `agent` | `yai agent spawn <role>` | Spawn agent | `agent_panel` | `wizard_action` | `agents.run` / future `agents.spawn` | `none verified` | `agent.spawn` | `auth_required + active_case_required + entitlement_required + runtime_gate_required + not_implemented` | `not_implemented` | `P2` | `planned` | Verified runtime action key exists in runtime-gate fixtures. |
| `agent.stop` | `agent` | `yai agent stop <agent>` | Stop agent | `agent_panel` | `destructive_action` | `none verified` | `none verified` | `none verified` | `auth_required + active_case_required + runtime_gate_required + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `agent.inspect` | `agent` | `yai agent inspect <agent>` | Inspect agent | `agent_panel` | `detail_action` | `agents.trace` | `client.agents().trace()` | `none verified` | `auth_required + active_case_required` | `available_read_only` | `P2` | `implemented_current` | Current SDK/API trace is the closest verified projection. |
| `agent.lineage` | `agent` | `yai agent lineage <agent>` | Agent lineage | `lineage_panel` | `detail_action` | `agents.trace` adjunct / future lineage op | `client.agents().trace()` | `none verified` | `auth_required + active_case_required` | `available_read_only` | `P2` | `implemented_current` | |
| `provider.list` | `provider` | `yai provider list` | Providers | `provider_panel` | `read_only_view` | `providers.list` | `client.providers().list()` | `none verified` | `diagnostic_allowed` | `available_read_only` | `P1` | `implemented_current` | Current CLI uses singular `provider`; API/SDK family stays plural. |
| `provider.status` | `provider` | `yai provider status` | Provider status | `provider_panel` | `status_badge` | `providers.list` adjunct / future status op | `client.providers()` | `none verified` | `diagnostic_allowed` | `not_implemented` | `P2` | `canonical_target` | |
| `provider.inspect` | `provider` | `yai provider inspect <provider>` | Inspect provider | `provider_panel` | `detail_action` | `providers.list` adjunct | `client.providers().list()` | `none verified` | `diagnostic_allowed` | `not_implemented` | `P2` | `canonical_target` | |
| `provider.check` | `provider` | `yai provider check <provider>` | Check provider | `provider_panel` | `detail_action` | `providers.probe` | `client.providers().probe()` | `none verified` | `diagnostic_allowed` | `available_diagnostic` | `P1` | `implemented_current` | No credentials/secrets output. |
| `model.list` | `model` | `yai model list` | Models | `model_panel` | `read_only_view` | `models.list` | `client.models().list()` | `none verified` | `diagnostic_allowed` | `available_read_only` | `P1` | `implemented_current` | Current CLI compatibility command is `yai models list`. |
| `model.status` | `model` | `yai model status` | Model status | `model_panel` | `status_badge` | `models.capabilities.show` adjunct / future status op | `client.models()` | `none verified` | `diagnostic_allowed` | `not_implemented` | `P2` | `canonical_target` | |
| `model.inspect` | `model` | `yai model inspect <model>` | Inspect model | `model_panel` | `detail_action` | `models.capabilities.show` | `client.models().capabilitiesShow()` | `none verified` | `diagnostic_allowed` | `available_diagnostic` | `P1` | `implemented_current` | Existing SDK/API surface is capabilities-oriented. |
| `model.check` | `model` | `yai model check <model>` | Check model | `model_panel` | `detail_action` | `models.capabilities.show` / future check op | `client.models().capabilitiesShow()` | `none verified` | `diagnostic_allowed` | `available_diagnostic` | `P1` | `implemented_current` | Must not imply live inference execution by default. |
| `skills.list` | `skills` | `yai skills list` | Skills | `developer_panel` | `read_only_view` | `none verified` | `none verified` | `none verified` | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `planned` | Plural `skills` remains the preferred public grammar. |
| `skills.inspect` | `skills` | `yai skills inspect <skill>` | Inspect skill | `developer_panel` | `detail_action` | `none verified` | `none verified` | `none verified` | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `skills.status` | `skills` | `yai skills status` | Skills status | `developer_panel` | `status_badge` | `none verified` | `none verified` | `none verified` | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `runtime.status` | `runtime` | `yai runtime status` | Runtime status | `runtime_panel` | `status_badge` | `system.status` compat projection | `client.runtime().statusInspect()` compat alias | `system.status.inspect` | `diagnostic_allowed` | `available_diagnostic` | `P0` | `legacy_compat` | Truthful compatibility alias while `system` becomes canonical. |
| `runtime.readiness` | `runtime` | `yai runtime readiness` | Runtime readiness | `runtime_panel` | `status_badge` | `system.status` / future readiness adjunct | `none verified` | `none verified` | `diagnostic_allowed` | `not_implemented` | `P1` | `diagnostic_only` | Compatibility/diagnostic family only. |
| `runtime.diagnostics` | `runtime` | `yai runtime diagnostics` | Runtime diagnostics | `runtime_panel` | `diagnostic_panel` | `system.runtime.inspect` / `system.check` composite | `none verified` | `none verified` | `diagnostic_allowed` | `not_implemented` | `P1` | `diagnostic_only` | |
| `runtime.gates` | `runtime` | `yai runtime gates` | Runtime gates | `runtime_panel` | `detail_action` | `control.gates.list` projection | `client.control().gatesList()` candidate | `none verified` | `auth_required + runtime_gate_required` | `not_implemented` | `P2` | `diagnostic_only` | Prefer `control.gates` as canonical family. |
| `runtime.start` | `runtime` | `yai runtime start` | Start runtime | `hidden` | `unavailable_placeholder` | excluded by API model | `none verified` | `none verified` | `forbidden` | `forbidden` | `N/A` | `forbidden` | Runtime lifecycle control is service/bootstrap territory, not canonical domain CLI/TUI. |
| `runtime.stop` | `runtime` | `yai runtime stop` | Stop runtime | `hidden` | `unavailable_placeholder` | excluded by API model | `none verified` | `none verified` | `forbidden` | `forbidden` | `N/A` | `forbidden` | |
| `runtime.restart` | `runtime` | `yai runtime restart` | Restart runtime | `hidden` | `unavailable_placeholder` | excluded by API model | `none verified` | `none verified` | `forbidden` | `forbidden` | `N/A` | `forbidden` | |
| `substrate.inspect.raw` | `storage/substrate` | `yai substrate inspect <layer>` | Raw substrate inspect | `diagnostics_panel` | `unavailable_placeholder` | none raw public | `none verified` | `none verified` | `forbidden` | `forbidden` | `N/A` | `forbidden` | Prefer `state.substrate.*` so State remains the owner. |

### Shell / Client / Session Legacy / Release / Update / Download / Dev Wrapper

| action_id | family | CLI projection | TUI projection | TUI location | TUI interaction kind | API operation candidate | SDK surface candidate | runtime_action_key candidate | required posture | availability | test priority | status | notes |
| --------- | ------ | -------------- | -------------- | ------------ | -------------------- | ----------------------- | -------------------- | ---------------------------- | ---------------- | ------------ | ------------- | ------ | ----- |
| `shell.open` | `shell` | `yai shell` | Shell home | `home` | `read_only_view` | none verified | none verified | none verified | `diagnostic_allowed` | `available` | `P0` | `implemented_current` | Shell is UX language, not auth/case/runtime ownership. |
| `shell.list` | `shell` | `yai shell list` | Shells | `global_command_palette` | `command_palette_action` | none verified | none verified | none verified | `diagnostic_allowed` | `available_diagnostic` | `P0` | `implemented_current` | Current CLI marks this as canonical shell inspection surface even before a real shell registry exists. |
| `shell.attach` | `shell` | `yai shell attach <shell_id>` | Attach shell | `global_command_palette` | `command_palette_action` | none verified | none verified | none verified | `diagnostic_allowed` | `available` | `P0` | `implemented_current` | UX connection command only. Must not be confused with auth/case/runtime lifecycle. |
| `shell.detach` | `shell` | `yai shell detach` | Detach shell | `global_command_palette` | `command_palette_action` | none verified | none verified | none verified | `diagnostic_allowed` | `available` | `P0` | `implemented_current` | UX connection command only. |
| `client.list` | `client` | `yai client list` | Clients | `runtime_panel` | `read_only_view` | `client.list` future | none verified | none verified | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `planned` | Secondary to shell for daily UX; useful for diagnostics/TUI. |
| `client.status` | `client` | `yai client status` | Client status | `runtime_panel` | `status_badge` | `client.status` future | none verified | none verified | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `client.attach` | `client` | `yai client attach <client_id>` | Attach client | `runtime_panel` | `context_action` | `client.attach` future | none verified | none verified | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `planned` | TUI may expose attach semantics, but client must not become case/auth owner. |
| `client.detach` | `client` | `yai client detach` | Detach client | `runtime_panel` | `context_action` | `client.detach` future | none verified | none verified | `diagnostic_allowed + not_implemented` | `not_implemented` | `P2` | `planned` | |
| `session.status` | `session-legacy` | `yai session status` | Session status | `hidden` | `unavailable_placeholder` | `session.status` | `client.session().statusInspect()` compat alias | `none verified` | `diagnostic_allowed` | `legacy_only` | `P1` | `deprecated` | Compatibility only; must not own auth, case, runtime, or work. |
| `session.attach` | `session-legacy` | `yai session attach` | Session attach | `hidden` | `unavailable_placeholder` | `session.attach` compat only | `none verified` | `none verified` | `forbidden` | `legacy_only` | `N/A` | `deprecated` | Documented only to prevent resurrection as canonical domain. |
| `session.detach` | `session-legacy` | `yai session detach` | Session detach | `hidden` | `unavailable_placeholder` | `session.detach` compat only | `none verified` | `none verified` | `forbidden` | `legacy_only` | `N/A` | `deprecated` | |
| `release.status` | `release/update/download` | `yai release status` | Release status | `settings_panel` | `detail_action` | none verified | none verified | none verified | `no_auth_required + not_implemented` | `not_implemented` | `P3` | `planned` | Must not claim live artifact state without a real release gate. |
| `update.status` | `release/update/download` | `yai update status` | Update status | `settings_panel` | `detail_action` | none verified | none verified | none verified | `no_auth_required + not_implemented` | `not_implemented` | `P3` | `planned` | |
| `update.check` | `release/update/download` | `yai update check` | Check updates | `settings_panel` | `detail_action` | none verified | none verified | none verified | `no_auth_required + not_implemented` | `not_implemented` | `P3` | `planned` | |
| `download.status` | `release/update/download` | `yai download status` | Download status | `settings_panel` | `detail_action` | none verified | none verified | none verified | `no_auth_required + not_implemented` | `not_implemented` | `P3` | `planned` | |
| `dev_wrapper.make_yai` | `dev-wrapper` | `make yai` | Run `make yai` | `not_applicable` | `unavailable_placeholder` | none | none | none | `forbidden` | `forbidden` | `N/A` | `forbidden` | Repository bootstrap wrapper, not canonical domain action. |
| `dev_wrapper.make_info` | `dev-wrapper` | `make info` | Run `make info` | `not_applicable` | `unavailable_placeholder` | none | none | none | `forbidden` | `forbidden` | `N/A` | `forbidden` | |
| `dev_wrapper.install_service` | `dev-wrapper` | `make install-service` | Install service | `not_applicable` | `unavailable_placeholder` | none | none | none | `forbidden` | `forbidden` | `N/A` | `forbidden` | Service/bootstrap boundary only. |
| `dev_wrapper.uninstall_service` | `dev-wrapper` | `make uninstall-service` | Uninstall service | `not_applicable` | `unavailable_placeholder` | none | none | none | `forbidden` | `forbidden` | `N/A` | `forbidden` | |

## TUI Projection Requirements

Every TUI projection must define:

```text
label
location
interaction_kind
visible_when
disabled_when
empty_state
blocked_state
confirmation_required
result_view
```

Field contract:

| Field | Meaning |
| ----- | ------- |
| `label` | Human-visible action label. |
| `location` | One of the canonical TUI locations in this document. |
| `interaction_kind` | How the user triggers the action. |
| `visible_when` | Whether the action should be shown even before it becomes available. |
| `disabled_when` | Canonical disabled-state rule using posture/gate vocabulary. |
| `empty_state` | What the panel/palette should say when there is no current data or selection. |
| `blocked_state` | What the panel/palette should say when the action is blocked by auth/case/gates. |
| `confirmation_required` | Whether the TUI must confirm before running it. |
| `result_view` | Which panel or detail overlay should render the shared output envelope. |

Examples:

| action_id | CLI | TUI label | TUI location | interaction | visible_when | disabled_when |
| --------- | --- | --------- | ------------ | ----------- | ------------ | ------------- |
| `case.enter` | `yai case enter <case>` | Enter case | `case_tree` | `context_action` | case exists in tree | auth missing or case selection invalid |
| `lineage.trace` | `yai lineage trace <ref>` | Trace lineage | `lineage_panel` | `detail_action` | ref selected | no active case |
| `materialize.plan` | `yai materialize plan <input>` | Plan materialization | `materialization_panel` | `form_action` | source/input selected | policy pack missing or case missing |
| `auth.logout` | `yai auth logout` | Log out | `account_panel` | `destructive_action` | auth posture present | auth already absent |
| `provider.check` | `yai provider check <provider>` | Check provider | `provider_panel` | `detail_action` | provider selected | runtime probe unavailable |

Repo-reality note:

* Loom already implements core pieces of this model:
  `command registry -> availability -> palette item -> overlay/detail`.
* `loom/src/command/registry.rs` already separates `effect`,
  `confirmation`, and `availability`.
* `loom/src/tui/overlays/palette.rs` already proves that disabled actions may
  remain visible with explicit reasons.

## Command Palette Requirements

Future TUI command palette items must follow this logical shape:

```text
action_id
label
search_terms
family
scope
requires_selection
requires_case
available_when
```

Palette field meanings:

| Field | Meaning |
| ----- | ------- |
| `action_id` | Canonical descriptor id. |
| `label` | Human-visible short title. |
| `search_terms` | Alternate words, aliases, and compatibility terms. |
| `family` | Canonical command family. |
| `scope` | Global, case-bound, provider-bound, evidence-bound, or diagnostic scope. |
| `requires_selection` | Whether a selected ref is required. |
| `requires_case` | Whether an active case is required. |
| `available_when` | Short availability/posture summary. |

Palette rules:

* palette search may index CLI aliases and legacy spellings
* palette execution must still resolve to canonical `action_id`
* palette entries may remain visible while unavailable
* unavailable entries must render a truthful reason, not disappear silently

## Shared Output Contract

CLI and TUI must consume the same logical output envelope:

```text
status
reason
posture
refs
warnings
next_actions
diagnostics
```

Shared output meaning:

| Field | Meaning |
| ----- | ------- |
| `status` | success/unavailable/blocked/partial-style outcome class |
| `reason` | primary human-readable cause or explanation |
| `posture` | auth/case/runtime/license/gate state summary |
| `refs` | stable case/job/evidence/record/lineage refs |
| `warnings` | non-fatal issues or policy notes |
| `next_actions` | recommended follow-up actions |
| `diagnostics` | structured details for read-only inspection |

Rules:

* CLI may render the envelope as JSON or compact text.
* TUI may group the same fields into panels, badges, and detail views.
* TUI must not invent separate TUI-only truth beyond the shared envelope.

## Forbidden TUI Actions

```text
TUI must not implement an action with no canonical action_id.
TUI must not create hidden session ownership.
TUI must not start/stop/restart runtime as a domain action.
TUI must not expose raw storage substrate mutation.
TUI must not expose raw hardware/fingerprint/secret data.
TUI must not bypass case/auth/gate posture.
```

Additional restrictions from audited repos:

* TUI must not turn client connection state into auth or active-case truth.
* TUI must not expose provider credentials, billing objects, or raw commercial
  plan payloads.
* TUI must not present attach/detach as login/logout.

## TUI / CLI Divergence Rules

```text
TUI may group actions visually.
TUI may show unavailable actions.
TUI may add guided workflows/wizards.
TUI may not rename the domain in a way that breaks command/API mapping.
CLI may expose compact commands.
CLI may not bypass canonical action descriptors.
```

Interpretation rules:

* TUI may collapse multiple related `action_id` values into one panel.
* CLI may expose aliases for migration or compatibility.
* compatibility aliases must still resolve to one canonical `action_id`.
* actions that compose multiple API operations must still have one stable
  `action_id`.

## Current Cross-Repo Consequences

* `api` should keep operation contracts and projection metadata authoritative.
* `sdk` should keep typed surfaces aligned to canonical action families and API
  operation ids rather than CLI strings.
* `cli` should present commands as projections over `action_id`, not as the
  domain model itself.
* `loom` should project palette/menu/panel actions from the same `action_id`
  descriptors and keep unavailable actions visible when useful.
* `yai` remains the owner of the deeper action spine:
  `operation -> case_action -> controlled_act -> evidence/state/lineage`.
