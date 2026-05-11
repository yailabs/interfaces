# Canonical CLI Command Inventory

## Status

* Delivery: V50.5
* Track: V — CLI/API/SDK/runtime command canon
* Branch: `refoundation/phase-01`
* Status of this document: preliminary flat inventory retained for cross-checking
* Authoritative source of truth: `api/Documentation/cli/canonical-yai-command-system.md`

## Purpose

This document is the preliminary flat command inventory produced in V50.5.

V50.6 supersedes it with the authoritative system reconstruction in:

* `api/Documentation/cli/canonical-yai-command-system.md`

This file remains useful as a cross-check against repo reality across `api`,
`cli`, `sdk`, `yai`, and `loom`, especially for implemented-vs-target drift,
but it is no longer the command-system source of truth.

It does not treat current implementation as the whole truth. The matrix below
includes:

* seed commands already required by the current CLI narrative;
* commands implemented today in Rust CLI;
* commands already seeded in the API registry or SDK surfaces;
* legacy compatibility vocabulary still visible in docs or code;
* families that should remain outside the canonical CLI.

## Non-goals

* not implementation
* not registry refactor
* not SDK generation
* not command deletion
* not runtime behavior

## Canonical Rules

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
```

## Command Status Vocabulary

| Status | Meaning |
| ------ | ------- |
| `canonical_target` | accepted public CLI target; may or may not be implemented yet |
| `implemented_current` | present in the current Rust CLI and safe to invoke today, including truthful unavailable surfaces |
| `planned` | named shape is reserved or strongly implied, but parser/behavior is absent |
| `docs_only` | documented shape only; implementation/parser absent |
| `legacy_compat` | compatibility bridge surface still present or still taught for migration |
| `deprecated` | migration bridge only; should be hidden or removed after replacement lands |
| `forbidden` | should not be implemented as a canonical public CLI command |
| `external_to_cli` | belongs to service/bootstrap, admin, packaging, or another plane rather than domain CLI |
| `runtime_internal` | runtime/private control concept, not a public CLI family |
| `api_only` | seeded in API contracts but not yet accepted as a local CLI surface |
| `sdk_only` | available as SDK helper/surface without a canonical CLI promise |
| `dev_wrapper` | repository/bootstrap wrapper, not a user-facing domain command |
| `unknown_needs_audit` | family or command exists as a concept, but ownership and canonical grammar are unresolved |

## Test Priority Vocabulary

| Priority | Meaning |
| -------- | ------- |
| `P0` | must test before V milestone close |
| `P1` | must test before preview licensed flow |
| `P2` | should test before public preview |
| `P3` | future / integration |
| `N/A` | not a CLI command |

## Gate / Posture Vocabulary

| Gate / posture | Meaning |
| -------------- | ------- |
| `no_auth_required` | command can run without authenticated posture |
| `diagnostic_allowed` | command may remain available while sealed or degraded |
| `auth_required` | command needs auth posture |
| `case_required` | command needs case identity or case tree posture |
| `active_case_required` | command needs `operator_context.active_case_ref` |
| `operator_context_required` | command depends on operator-context posture |
| `machine_authorization_required` | command depends on machine authorization posture |
| `license_lease_required` | command depends on license lease posture |
| `entitlement_required` | command depends on entitlement posture |
| `runtime_gate_required` | command depends on runtime gate posture |
| `limit_projection_required` | command depends on limit projection posture |
| `cloud_capacity_required` | command depends on cloud capacity posture |
| `admin_required` | command belongs to future admin boundary |
| `manual_review_required` | command may require explicit review posture |
| `not_implemented` | current implementation is absent |
| `forbidden` | command must not become canonical CLI grammar |

## Canonical Command Matrix

### Auth

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `auth` | `yai auth login` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/auth.rs` | `cli` | `auth.login` | none | `n/a` | `no_auth_required` | `P0` | Parser exists today; without `--local-dev` it truthfully reports production auth unavailable. |
| `auth` | `yai auth login --local-dev` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/auth.rs` | `cli` | `auth.login` plus local CLI compatibility | none | `n/a` | `no_auth_required` | `P0` | Canonical local-dev bootstrap surface in the current Rust CLI. |
| `auth` | `yai auth status` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/auth.rs` | `cli` | `auth.status` | none | `n/a` | `diagnostic_allowed` | `P0` | Canonical auth inspection surface; distinct from session and runtime health. |
| `auth` | `yai auth logout` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/auth.rs` | `cli` | `auth.logout` | none | `n/a` | `auth_required` | `P0` | Truthful cleanup surface; current implementation safely no-ops when no local-dev marker exists. |

### Account

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `account` | `yai account status` | `unknown_needs_audit` | no | not present; account posture appears only in Loom UX code | `cli` + identity/auth contracts | `auth` / `identity` families exist; no `account` family | `loom/src/yai/account.rs` only | `n/a` | `auth_required` | `P2` | Account vocabulary exists in product posture, but canonical CLI grammar is unresolved. |
| `account` | `yai account open` | `unknown_needs_audit` | no | not present | `cli` + product/account plane | none | none | `n/a` | `auth_required` | `P3` | Could imply dashboard/browser ownership rather than local CLI. |
| `account` | `yai account access` | `unknown_needs_audit` | no | not present | `cli` + identity/auth contracts | none | none | `n/a` | `auth_required` | `P2` | Boundary with entitlement, machine, and license posture is unresolved. |
| `account` | `yai account preferences` | `unknown_needs_audit` | no | not present | `cli` + client-local profile/config plane | none | none | `n/a` | `auth_required` | `P3` | Could collapse account settings into local config without a clear backend owner. |

### Case

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `case` | `yai case root` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/case.rs` | `cli` | closest current contract is `case.tree` / local root case posture | none | `n/a` | `auth_required` | `P0` | Current Rust CLI local-manifest surface; no session mutation. |
| `case` | `yai case list` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/case.rs` | `cli` | `case.list` | Rust SDK has `client.case().list()` constants but CLI currently uses local manifest logic | `n/a` | `auth_required` | `P0` | Canonical seed command; current CLI implementation is local-tree oriented. |
| `case` | `yai case open <path-or-uri>` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/case.rs` | `cli` | closest current family is `case.create` | none | `n/a` | `auth_required` | `P0` | Current mutation creates or ensures a nested case in local manifest state. |
| `case` | `yai case enter <case>` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/case.rs` | `cli` | closest current family is `case.use` | none | `n/a` | `auth_required + operator_context_required + case_required` | `P0` | Current owner of active case is operator context, not session. |
| `case` | `yai case leave` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/case.rs` | `cli` | local operator-context clear; no direct API op | none | `n/a` | `operator_context_required` | `P0` | Cleanup/no-op surface; should remain distinct from logout and shell detach. |
| `case` | `yai case status` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/case.rs` | `cli` | partial overlap with `case.current` plus runtime active-case posture | partial Rust SDK `client.case().current()` | `n/a` | `diagnostic_allowed` | `P0` | Inspection remains available while sealed. |
| `case` | `yai case close <case>` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/case.rs` | `cli` | no exact canonical API op yet | none | `n/a` | `auth_required + case_required + operator_context_required` | `P0` | Local manifest mutation; cannot close root or active case. |

### Operator Context

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `operator-context` | `yai context status` | `unknown_needs_audit` | no | not present; current ownership is embedded in `cli/src/commands/case.rs` | `cli` | none | none | `n/a` | `auth_required + operator_context_required` | `P1` | Current CLI keeps operator context under `yai case status`. |
| `operator-context` | `yai context current` | `unknown_needs_audit` | no | not present; local marker logic lives in `cli/src/commands/case.rs` | `cli` | none | none | `n/a` | `auth_required + operator_context_required` | `P1` | Boundary between case and explicit context family remains unresolved. |
| `operator-context` | `yai context switch <case>` | `unknown_needs_audit` | no | not present; closest current behavior is `yai case enter <case>` | `cli` | none | none | `n/a` | `auth_required + operator_context_required + case_required` | `P1` | Likely redundant with `yai case enter` unless a separate context family is accepted. |
| `operator-context` | `yai context clear` | `unknown_needs_audit` | no | not present; closest current behavior is `yai case leave` | `cli` | none | none | `n/a` | `operator_context_required` | `P1` | Explicit context command may remain unnecessary if `case leave` stays canonical. |

### Shell

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `shell` | `yai shell` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/shell.rs` | `cli` UX plane | none | none | `n/a` | `no_auth_required + diagnostic_allowed` | `P0` | Canonical interactive shell UX entry; shell is not session. |
| `shell` | `yai shell list` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/shell.rs` | `cli` UX plane | none | none | `n/a` | `no_auth_required + diagnostic_allowed` | `P0` | Truthful shell-inspection surface; backend registry is not implemented. |
| `shell` | `yai shell attach <shell_id>` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/shell.rs` | `cli` UX plane | none | none | `n/a` | `no_auth_required + diagnostic_allowed` | `P0` | UX connection command only; not auth login, case enter, or runtime start. |
| `shell` | `yai shell detach` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/shell.rs` | `cli` UX plane | none | none | `n/a` | `no_auth_required + diagnostic_allowed` | `P0` | UX connection command only; not auth logout, case leave, or runtime stop. |

### Client

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `client` | `yai client list` | `canonical_target` | no | not present in Rust CLI; API registry seeds `client.list` | `cli` | `client.list` | no typed client surface audited in this wave | `n/a` | `auth_required + diagnostic_allowed` | `P1` | Explicit client family is a likely canonical replacement for legacy session attachment language. |
| `client` | `yai client attach <client_id>` | `unknown_needs_audit` | no | not present; Loom has `/attach`, legacy ownership lived under session | `cli` + runtime/API boundary | no `client.attach` op found; legacy `session.attach` exists | none | `n/a` | `auth_required + runtime_gate_required` | `P2` | Current API/SDK split does not yet seed a clean client attach operation. |
| `client` | `yai client detach` | `unknown_needs_audit` | no | not present; Loom has `/detach`, legacy ownership lived under session | `cli` + runtime/API boundary | no `client.detach` op found; legacy `session.detach` exists | none | `n/a` | `auth_required + runtime_gate_required` | `P2` | Likely future client UX surface, but not yet canonicalized in API grammar. |
| `client` | `yai client status` | `canonical_target` | no | not present in Rust CLI; API registry seeds `client.status` | `cli` | `client.status` | none audited | `n/a` | `auth_required + diagnostic_allowed` | `P1` | Good candidate to replace legacy session posture language. |

### Runtime

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `runtime` | `yai runtime status` | `legacy_compat` | yes | `cli/src/app/cli.rs`, `cli/src/commands/runtime.rs`, `cli/src/sdk/runtime.rs` | `cli` | `system.status` | `client.system().status()` via CLI compatibility wiring | `n/a` | `diagnostic_allowed` | `P0` | Current public CLI surface; canonical API/SDK family is `system`, not `runtime`. |
| `runtime` | `yai runtime readiness` | `docs_only` | no | not present; readiness is projected inside current runtime status output | `cli` | `system.status` | `client.system().status()` | `n/a` | `diagnostic_allowed` | `P1` | Exact split between status and readiness is still a documentation gap. |
| `runtime` | `yai runtime lifecycle` | `planned` | no | not present; lifecycle is visible in status payloads only | `cli` | `system.runtime.inspect` / `system.status` | `client.system().status()` partial | `n/a` | `diagnostic_allowed` | `P2` | Read-only lifecycle inspection may be acceptable; lifecycle control is not. |
| `runtime` | `yai runtime gates` | `planned` | no | not present | `cli` + control plane | closest current ops are `control.gates.list` / `control.gates.show` | Rust/TS ops constants only | `n/a` | `auth_required + runtime_gate_required` | `P2` | This is probably a `control` command rendered through runtime context, not a pure runtime family. |
| `runtime` | `yai runtime diagnostics` | `planned` | no | not present; current local analog is `yai doctor` | `cli` | `system.check` | none wired in current CLI | `n/a` | `diagnostic_allowed` | `P2` | Keep separate from runtime lifecycle control. |
| `runtime` | `yai runtime start` | `forbidden` | no | not present; only dev-wrapper/service bootstrap surfaces exist | `service/bootstrap` | none | none | `n/a` | `forbidden` | `N/A` | Migration docs already classify start/stop/restart as non-canonical public grammar. |
| `runtime` | `yai runtime stop` | `forbidden` | no | not present; only dev-wrapper/service bootstrap surfaces exist | `service/bootstrap` | none | none | `n/a` | `forbidden` | `N/A` | Runtime lifecycle ownership must not collapse into domain CLI. |
| `runtime` | `yai runtime restart` | `forbidden` | no | not present; only dev-wrapper/service bootstrap surfaces exist | `service/bootstrap` | none | none | `n/a` | `forbidden` | `N/A` | Restart is a host/service concern, not canonical domain CLI. |

### System and Status

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `system` | `yai system status` | `canonical_target` | no | not present; current behavior is exposed through `yai runtime status` | `cli` | `system.status` | `client.system().status()` | `n/a` | `diagnostic_allowed` | `P0` | Strongest canonical target before V51. |
| `system` | `yai system info` | `planned` | no | not present | `cli` | closest current op is `system.runtime.inspect` | none wired in current CLI | `n/a` | `diagnostic_allowed` | `P1` | Exact payload split between `info`, `status`, and `doctor` still needs cleanup. |
| `status` | `yai status` | `unknown_needs_audit` | no | not present | `cli` | maybe `system.status`, but unresolved | none | `n/a` | `diagnostic_allowed` | `P1` | Root status risks duplicating `system status` and `runtime status`. |
| `status` | `yai version` | `implemented_current` | yes | `cli/src/app/cli.rs` | `cli` | none | none | `n/a` | `no_auth_required` | `P0` | Foundation/local command; not an API family. |
| `status` | `yai doctor` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/doctor.rs` | `cli` | closest conceptual peer is `system.check`; command is local-only | none | `n/a` | `diagnostic_allowed` | `P0` | Current truthful local diagnostic surface. |

### Config

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `config` | `yai config show` | `canonical_target` | no | root `yai config` exists but returns unavailable via `cli/src/commands/config.rs` | `cli` | none | none | `n/a` | `no_auth_required` | `P1` | Local configuration is a CLI concern; subcommand grammar is still missing. |
| `config` | `yai config path` | `canonical_target` | no | root `yai config` exists but returns unavailable via `cli/src/commands/config.rs` | `cli` | none | none | `n/a` | `no_auth_required` | `P1` | Useful companion to `YAI_CONFIG_HOME` and profile debugging. |
| `config` | `yai config validate` | `planned` | no | root `yai config` exists but returns unavailable via `cli/src/commands/config.rs` | `cli` | none | none | `n/a` | `no_auth_required` | `P2` | Validation boundary likely overlaps with `doctor`. |

### Job and Execution Lease

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `job` | `yai job list` | `unknown_needs_audit` | no | not present | `cli` + workflow/control planes | no `job` family found | none | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P2` | Exact split between job and workflow run ownership is unresolved. |
| `job` | `yai job status <job>` | `unknown_needs_audit` | no | not present | `cli` + workflow/control planes | none | none | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P2` | Could map to workflow runs or future execution records. |
| `job` | `yai job start <spec>` | `unknown_needs_audit` | no | not present | `cli` + workflow/control planes | maybe `act.run` / `workflow.*` later | none | `n/a` | `auth_required + active_case_required + machine_authorization_required + license_lease_required + entitlement_required + runtime_gate_required + limit_projection_required` | `P2` | Command family is likely future-facing, not settled. |
| `job` | `yai job cancel <job>` | `unknown_needs_audit` | no | not present | `cli` + control plane | none | none | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P3` | Cancel semantics do not yet exist in the audited registry. |
| `job` | `yai job logs <job>` | `unknown_needs_audit` | no | not present | `cli` + workflow/runtime observation | none | none | `n/a` | `auth_required + active_case_required + diagnostic_allowed` | `P3` | Might collapse into generic `logs` unless a job family is accepted. |
| `execution-lease` | `yai lease execution status <job>` | `unknown_needs_audit` | no | not present | `cli` + runtime/license boundary | no public family found | none | `n/a` | `auth_required + active_case_required + license_lease_required` | `P2` | Execution-lease is a boundary concept, not yet a public CLI family. |
| `execution-lease` | `yai lease execution list` | `unknown_needs_audit` | no | not present | `cli` + runtime/license boundary | no public family found | none | `n/a` | `auth_required + license_lease_required` | `P2` | Should not be invented before registry/API ownership is clear. |

### Flow and Agent

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `flow` | `yai flow list` | `legacy_compat` | no | current CLI only has root placeholder `cli/src/app/cli.rs`, `cli/src/commands/flow.rs` | `cli` | target family is `workflow.list` | Rust/TS operation constants only | `n/a` | `auth_required + active_case_required` | `P2` | `flow` is legacy public grammar; canonical API family is `workflow`. |
| `flow` | `yai flow status <flow>` | `legacy_compat` | no | current CLI only has root placeholder `cli/src/app/cli.rs`, `cli/src/commands/flow.rs` | `cli` | closest targets are `workflow.show` / `workflow.runs.watch` | Rust/TS operation constants only | `n/a` | `auth_required + active_case_required + diagnostic_allowed` | `P2` | Preserve only as migration language if needed. |
| `flow` | `yai flow run <flow>` | `legacy_compat` | no | current CLI only has root placeholder `cli/src/app/cli.rs`, `cli/src/commands/flow.rs` | `cli` | closest targets are `workflow.*` or `act.run` | none | `n/a` | `auth_required + active_case_required + machine_authorization_required + license_lease_required + entitlement_required + runtime_gate_required + limit_projection_required` | `P2` | Running flows is future-facing and should converge on workflow grammar. |
| `flow` | `yai flow stop <flow>` | `legacy_compat` | no | current CLI only has root placeholder `cli/src/app/cli.rs`, `cli/src/commands/flow.rs` | `cli` | no canonical stop op found | none | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P3` | Stop semantics are not seeded in the audited API registry. |
| `agent` | `yai agent list` | `legacy_compat` | no | current CLI only has root placeholder `cli/src/app/cli.rs`, `cli/src/commands/agent.rs` | `cli` | target family is `agents.list` | Rust/TS ops constants only | `n/a` | `auth_required + active_case_required` | `P2` | Current CLI family is singular; API/SDK family is plural `agents`. |
| `agent` | `yai agent status <agent>` | `legacy_compat` | no | current CLI only has root placeholder `cli/src/app/cli.rs`, `cli/src/commands/agent.rs` | `cli` | closest target is `agents.trace` | Rust/TS ops constants only | `n/a` | `auth_required + active_case_required + diagnostic_allowed` | `P2` | Exact status grammar is not settled. |
| `agent` | `yai agent spawn <role>` | `legacy_compat` | no | current CLI only has root placeholder `cli/src/app/cli.rs`, `cli/src/commands/agent.rs` | `cli` | closest target is `agents.run` / `agents.plan` | Rust/TS ops constants only | `n/a` | `auth_required + active_case_required + entitlement_required + runtime_gate_required` | `P2` | Spawn grammar is not yet seeded as canonical public CLI. |
| `agent` | `yai agent stop <agent>` | `legacy_compat` | no | current CLI only has root placeholder `cli/src/app/cli.rs`, `cli/src/commands/agent.rs` | `cli` | no exact stop op found | none | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P3` | Stop semantics remain unsettled. |

### Provider and Model

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `provider` | `yai provider list` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/provider.rs` | `cli` | target op is `providers.list` | `client.providers().list()` plus compat `client.provider().list_inspect()` | `n/a` | `diagnostic_allowed` | `P1` | Implemented today, but singular family diverges from canonical API/SDK plural form. |
| `provider` | `yai provider status` | `planned` | no | not present; current CLI only ships `provider list` | `cli` | `providers.status` family resource exists | no typed CLI surface | `n/a` | `diagnostic_allowed` | `P2` | Naming should converge on `providers` before public stabilization. |
| `provider` | `yai provider check <provider>` | `planned` | no | not present | `cli` | closest target is `providers.probe` | Rust/TS operation constants for `providers.probe` | `n/a` | `diagnostic_allowed` | `P2` | Do not imply provider invocation or credential mutation. |
| `model` | `yai models list` | `implemented_current` | yes | `cli/src/app/cli.rs`, `cli/src/commands/models.rs` | `cli` | `models.list` | `client.models().list()` | `n/a` | `diagnostic_allowed` | `P1` | Current CLI surface is plural `models`, not singular `model`. |
| `model` | `yai model status` | `planned` | no | not present; current CLI only ships `models list` | `cli` | `models` family seeded; exact status op not audited | no typed CLI surface | `n/a` | `diagnostic_allowed` | `P2` | Singular/plural CLI grammar is still divergent. |
| `model` | `yai model check <model>` | `planned` | no | not present | `cli` | closest target is `models.capabilities.show` | Rust/TS operation constants for `models.capabilities.show` | `n/a` | `diagnostic_allowed` | `P2` | Must not imply live provider/model execution. |

### Knowledge, Memory, Recall, Records, Evidence, Analytics

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `knowledge` | `yai knowledge list` | `planned` | no | not present | `cli` | `knowledge` family seeded; exact `list` op not confirmed | no typed CLI surface audited | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P2` | Knowledge family exists in API/YAI, but CLI grammar is not yet present. |
| `knowledge` | `yai knowledge status` | `planned` | no | not present | `cli` | knowledge family seeded | none | `n/a` | `auth_required + active_case_required + diagnostic_allowed` | `P2` | Likely future posture/inspection command. |
| `knowledge` | `yai knowledge inspect <ref>` | `planned` | no | not present | `cli` | closest current ops are `knowledge.query` / `knowledge.lineage.trace` | Rust/TS operation constants only | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P2` | Exact inspect grammar remains unresolved. |
| `memory` | `yai memory status` | `planned` | no | not present | `cli` | `knowledge.memory` resource exists at family level | none | `n/a` | `auth_required + active_case_required + diagnostic_allowed` | `P2` | Memory should stay case-bound and governed. |
| `recall` | `yai recall query <query>` | `unknown_needs_audit` | no | not present | `cli` | no `recall` family found; closest families are `knowledge` and `analytics` | none | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P2` | Root recall grammar risks bypassing governed knowledge/query boundaries. |
| `records` | `yai records list` | `legacy_compat` | no | current CLI only has root placeholder `cli/src/app/cli.rs`, `cli/src/commands/records.rs` | `cli` | target family is `state.records.*` | Rust/TS constants for `state.records.query` / `state.records.tail` | `n/a` | `auth_required + active_case_required` | `P2` | Root `records` grammar diverges from canonical `state.records`. |
| `records` | `yai records inspect <record>` | `legacy_compat` | no | current CLI only has root placeholder `cli/src/app/cli.rs`, `cli/src/commands/records.rs` | `cli` | target family is `state.records.*` | Rust/TS constants only | `n/a` | `auth_required + active_case_required + diagnostic_allowed` | `P2` | Likely should move under `state`. |
| `evidence` | `yai evidence list` | `unknown_needs_audit` | no | not present | `cli` | closest seeded op is `control.evidence.show` | none | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P2` | Evidence exists as a domain concept, but public CLI family ownership is unresolved. |
| `evidence` | `yai evidence inspect <evidence>` | `unknown_needs_audit` | no | not present | `cli` | closest seeded op is `control.evidence.show` | none | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P2` | May belong under control rather than root evidence. |
| `analytics` | `yai analytics status` | `planned` | no | not present | `cli` | analytics family seeded | none | `n/a` | `auth_required + active_case_required + diagnostic_allowed` | `P2` | Analytics is derived, not primary truth. |
| `analytics` | `yai analytics summary` | `planned` | no | not present | `cli` | closest op is `analytics.workflows.summary` | none | `n/a` | `auth_required + active_case_required + diagnostic_allowed` | `P2` | Summary surfaces must remain projection-only. |

### Governance, Policy, Control, Skills

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `governance` | `yai govern status` | `canonical_target` | no | current CLI only has root placeholder `yai governance` in `cli/src/app/cli.rs`, `cli/src/commands/governance.rs` | `cli` | `governance.status` / `governance.posture` | Rust/TS operation constants for `governance.posture` | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P2` | Naming divergence is active: current CLI says `governance`, requested target says `govern`. |
| `governance` | `yai govern policy list` | `canonical_target` | no | current CLI only has root placeholder `yai governance` in `cli/src/app/cli.rs`, `cli/src/commands/governance.rs` | `cli` | `governance.policy.*` | Rust/TS operation constants for `governance.policy.resolve` only | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P2` | Policy list grammar is not yet explicitly seeded. |
| `governance` | `yai govern policy inspect <policy>` | `canonical_target` | no | current CLI only has root placeholder `yai governance` in `cli/src/app/cli.rs`, `cli/src/commands/governance.rs` | `cli` | closest current op is `governance.policy.resolve` | Rust/TS operation constants only | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P2` | Exact inspect/resolve split still needs cleanup. |
| `policy` | `yai policy ...` | `forbidden` | no | not present | `governance` family, not root CLI | use `governance.policy.*` | none | `n/a` | `forbidden` | `N/A` | Migration plan explicitly forbids root policy ownership. |
| `control` | `yai control status` | `canonical_target` | no | current CLI only has legacy root placeholder `yai supervisor` in `cli/src/app/cli.rs`, `cli/src/commands/supervisor.rs` | `cli` | `control.status` | Rust/TS operation constants for `control.*` | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P2` | Canonical target is `control`; current placeholder still says `supervisor`. |
| `control` | `yai control plan` | `unknown_needs_audit` | no | not present | `cli` + runtime/control boundary | compat concept exists as `runtime.service.control.plan` only | Rust compat operation constants only | `n/a` | `auth_required + diagnostic_allowed` | `P2` | Current control-plan semantics are projections, not proof of start/stop/restart execution. |
| `skills` | `yai skills list` | `planned` | no | not present | `cli` | skills family seeded | no typed CLI surface audited | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P2` | API family exists, but no public CLI parser yet. |
| `skills` | `yai skills inspect <skill>` | `planned` | no | not present | `cli` | skills family seeded | none | `n/a` | `auth_required + active_case_required + runtime_gate_required` | `P2` | Exact list/inspect grammar remains future-facing. |

### Query, Inspect, Logs

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `query` | `yai query <query>` | `forbidden` | no | not present | family-specific owners such as knowledge or analytics | closest current ops are `knowledge.query` and `analytics.query` | Rust/TS constants for those families only | `n/a` | `forbidden` | `N/A` | Root `query` is too ambiguous and risks bypassing case/governance boundaries. |
| `inspect` | `yai inspect <ref>` | `forbidden` | no | not present; legacy inspect family was explicitly called non-canonical in migration docs | family-specific owners | none | none | `n/a` | `forbidden` | `N/A` | Inspection should map to real families or remain compat-only. |
| `logs` | `yai logs` | `unknown_needs_audit` | no | not present | `cli` + runtime/workflow observation planes | no canonical `logs` family found | none | `n/a` | `diagnostic_allowed` | `P3` | Root logs grammar is ambiguous across runtime, jobs, and workflows. |
| `logs` | `yai logs tail` | `unknown_needs_audit` | no | not present | `cli` + runtime/workflow observation planes | no canonical `logs.tail` op found | none | `n/a` | `diagnostic_allowed` | `P3` | May eventually split into family-specific tails. |

### Release, Update, Download

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `release` | `yai release status` | `planned` | no | not present | packaging/release plane exposed through CLI if ever accepted | none | none | `n/a` | `diagnostic_allowed` | `P3` | Must not imply live artifact control or provider/model execution. |
| `update` | `yai update status` | `planned` | no | not present | packaging/update plane | none | none | `n/a` | `diagnostic_allowed` | `P3` | Future-facing only; no current implementation promise. |
| `update` | `yai update check` | `planned` | no | not present | packaging/update plane | none | none | `n/a` | `diagnostic_allowed` | `P3` | Should remain truthful about offline/local-only builds. |
| `download` | `yai download status` | `planned` | no | not present | packaging/artifact plane | none | none | `n/a` | `diagnostic_allowed` | `P3` | Must not claim direct artifact authority before packaging decisions land. |

### Machine, License, Entitlement, Limits, Cloud

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `machine` | `yai machine status` | `planned` | no | not present | `cli` + identity/runtime boundary | family-level identity machine posture only | none | `n/a` | `auth_required + diagnostic_allowed` | `P1` | Machine posture is documented in V42 but not yet surfaced as CLI grammar. |
| `machine` | `yai machine enroll` | `planned` | no | not present | `cli` + platform/machine authorization boundary | none seeded in current audit | none | `n/a` | `auth_required + manual_review_required` | `P1` | Do not imply machine authorization issuance in current build. |
| `machine` | `yai machine authorization status` | `planned` | no | not present | `cli` + identity/runtime boundary | family-level identity authorization posture only | none | `n/a` | `auth_required + diagnostic_allowed` | `P1` | Good future diagnostic command once contracts mature. |
| `license` | `yai license status` | `planned` | no | not present | `cli` + license/runtime boundary | boundary docs exist; no command op seeded | none | `n/a` | `auth_required + machine_authorization_required + diagnostic_allowed` | `P1` | V43/V46-V50 define posture, not command behavior. |
| `license` | `yai license check` | `planned` | no | not present | `cli` + license/runtime boundary | request/response contracts exist, not CLI behavior | none | `n/a` | `auth_required + machine_authorization_required + runtime_gate_required` | `P1` | Must not imply request transport or enforcement exists today. |
| `license` | `yai license lease status` | `planned` | no | not present | `cli` + license/runtime boundary | lease posture docs exist; no command op seeded | none | `n/a` | `auth_required + license_lease_required + diagnostic_allowed` | `P1` | Should consume safe lease posture only. |
| `entitlement` | `yai entitlement status` | `planned` | no | not present | `cli` + identity/license boundary | identity family includes entitlement vocabulary | none | `n/a` | `auth_required + entitlement_required` | `P1` | Do not collapse entitlement into billing/account profile. |
| `limits` | `yai limits status` | `planned` | no | not present | `cli` + limit reconciliation boundary | limit contracts exist in docs; no CLI op seeded | none | `n/a` | `auth_required + entitlement_required + limit_projection_required` | `P1` | Limits are shared account posture, not multiplied by machines or runtimes. |
| `cloud` | `yai cloud status` | `planned` | no | not present | `cli` + cloud capacity boundary | no current family found | none | `n/a` | `auth_required + cloud_capacity_required` | `P3` | Cloud posture should stay diagnostic/projection only until a real boundary exists. |
| `cloud` | `yai cloud capacity` | `planned` | no | not present | `cli` + cloud capacity boundary | no current family found | none | `n/a` | `auth_required + cloud_capacity_required` | `P3` | Do not imply quota truth, metering, or billing ownership. |

### Admin and Support

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `admin` | `yai admin status` | `external_to_cli` | no | not present | enterprise/admin plane | none audited | none | `n/a` | `admin_required` | `N/A` | Not a canonical local operator CLI surface in current repo reality. |
| `support` | `yai support status` | `planned` | no | not present | support/diagnostic plane | none audited | none | `n/a` | `auth_required + diagnostic_allowed` | `P3` | Might become a support-bundle or support-posture surface later. |
| `support` | `yai support contact` | `external_to_cli` | no | not present | enterprise/support plane | none audited | none | `n/a` | `auth_required` | `N/A` | Contact workflows are likely external to local CLI. |

### Session Legacy

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `session-legacy` | `yai session status` | `legacy_compat` | yes | `cli/src/app/cli.rs`, `cli/src/commands/session.rs`, `cli/src/sdk/runtime.rs` | migration bridge only | `session.status` | `client.session().status()` | `n/a` | `diagnostic_allowed` | `P0` | Current Rust CLI still ships this compatibility command; it must not own auth, case, or runtime truth. |
| `session-legacy` | `yai session attach` | `deprecated` | no | not present in current Rust CLI; historical ownership lived in removed legacy `source/` and Loom UX words | migration bridge only | legacy `session.attach` exists in API registry | none audited | `n/a` | `forbidden` | `P1` | Must not revive session as canonical attach grammar. |
| `session-legacy` | `yai session detach` | `deprecated` | no | not present in current Rust CLI; historical ownership lived in removed legacy `source/` and Loom UX words | migration bridge only | legacy `session.detach` exists in API registry | none audited | `n/a` | `forbidden` | `P1` | Migration bridge only; replace with shell/client language where needed. |

### Dev Wrapper

| family | command | status | implemented today | current location if implemented | target owner | API family / operation if known | SDK surface if known | runtime_action_key if known | required posture / gates | test priority | notes |
| ------ | ------- | ------ | ----------------- | ------------------------------- | ------------ | ------------------------------- | ------------------- | --------------------------- | ------------------------ | ------------- | ----- |
| `dev-wrapper` | `make yai` | `dev_wrapper` | yes | `yai/Makefile` | repo/bootstrap plane | none | none | `n/a` | `no_auth_required` | `N/A` | Build/bootstrap helper, not a canonical user-facing domain command. |
| `dev-wrapper` | `make info` | `dev_wrapper` | yes | `yai/Makefile` | repo/bootstrap plane | none | none | `n/a` | `no_auth_required` | `N/A` | Repo inspection helper only. |
| `dev-wrapper` | `make install-service` | `dev_wrapper` | yes | `yai/Makefile` | service/bootstrap plane | none | none | `n/a` | `no_auth_required` | `N/A` | Service bootstrap is not auth, case, or runtime domain CLI. |
| `dev-wrapper` | `make uninstall-service` | `dev_wrapper` | yes | `yai/Makefile` | service/bootstrap plane | none | none | `n/a` | `no_auth_required` | `N/A` | Service uninstall remains outside canonical domain CLI. |
| `dev-wrapper` | `launchctl ...` | `dev_wrapper` | yes | host service manager usage documented around install/uninstall flows | host/service manager | none | none | `n/a` | `no_auth_required` | `N/A` | Host service-manager surface, not a YAI domain command family. |
| `dev-wrapper` | `cargo run ...` | `dev_wrapper` | yes | repo-local debug invocation across `cli` / `loom` | repo/debug plane | none | none | `n/a` | `no_auth_required` | `N/A` | Debug-only invocation; not the installed canonical `yai` experience. |

## Cross-Repo Divergence

| Surface | api registry / docs | cli implementation / docs | sdk surfaces | yai runtime docs | loom docs / TUI | Status | Gap | Action needed |
| ------- | ------------------- | ------------------------- | ------------ | ---------------- | --------------- | ------ | --- | ------------- |
| `auth` | `auth.*` family seeded | `yai auth ...` exists; local-dev is current truth; production auth unavailable | no typed auth client | runtime boundary docs define posture-only ownership | LoginShell and dev bypass exist, not backend auth | diverged | API seeds auth broadly, CLI implements only local-dev-safe subset, SDK missing, Loom is UX-only | keep auth canonical in inventory; wire via later auth wave, not V50.5 |
| `case` | `case.*` family seeded | `root/list/open/enter/leave/status/close` implemented locally; `case current` remains in legacy/help/docs | Rust SDK has `case.current/list/show`; not the full local tree grammar | runtime docs already center case/operator context | Loom says case surface unavailable | diverged | CLI local-tree grammar is ahead of API/SDK naming | preserve CLI case canon; map API/SDK gaps explicitly in V51+ |
| `session` | public `session` family still seeded | only `yai session status` remains in Rust CLI | typed session surfaces remain | runtime docs increasingly say session is not canonical | Loom still uses some session posture language | diverged | registry/sdk still teach session family while policy says non-canonical | mark session as legacy/deprecated bridge |
| `runtime` | canonical family is `system`; lifecycle/readiness posture exists | public command still says `runtime status` | SDK already exposes `client.system().status()` and runtime compat alias | runtime docs separate liveness from authorization | Loom renders runtime posture truthfully | diverged | CLI name lags API/SDK canon | record `system status` as target and `runtime status` as legacy compat |
| `shell/client` | `client` family seeded; no `shell` family | shell UX commands exist; client family absent | SDK owns transport clients, not shell | runtime docs separate client/shell from auth/case | Loom has `/attach` `/detach` UX only | diverged | shell/client semantics split across CLI UX, API client family, Loom commands | keep shell canonical UX; audit client as target family |
| `provider` | family is `providers` | current CLI says singular `provider list` | SDK canonical surface is plural `providers` plus compat alias | runtime docs keep provider/model execution out of CLI truth | Loom only shows pending provider/model posture | diverged | CLI public grammar is singular while API/SDK are plural | mark singular provider as current compat, plural as target direction |
| `model` | family is `models` | current CLI already says `models list`; requested audit family was singular `model` | SDK canonical surface is `models` | runtime docs keep model execution out of CLI truth | Loom only shows pending provider/model posture | diverged | singular/plural family name not yet normalized in audit language | keep actual current command in matrix and note naming drift |
| `agent` | family is plural `agents` | current CLI only has singular root scaffold `agent` | Rust/TS ops seed plural `agents.*` | runtime docs discuss agents as capability plane | Loom has no agent command family | diverged | API/SDK plural, CLI singular scaffold only | mark `agent` as legacy compat / planned migration target |
| `flow` | canonical family is `workflow` | current CLI only has legacy root scaffold `flow` | Rust/TS ops seed `workflow.*` | runtime/docs still reference orchestration/flow planes | Loom has no public flow grammar | diverged | CLI still carries legacy name | classify `flow` as legacy compat and target `workflow` later |
| `knowledge` | family seeded | no CLI grammar | TS/Rust ops seed `knowledge.query` / lineage | runtime docs strongly own knowledge plane | Loom only has product notes | diverged | API/YAI are ahead of CLI | keep family in inventory as planned |
| `evidence` | evidence mostly nested under control contracts | no CLI grammar | no audited CLI-oriented SDK surface | runtime/docs treat evidence as core domain output | Loom has no evidence command | diverged | root evidence family ownership unresolved | leave as unknown_needs_audit |
| `analytics` | analytics family seeded | no CLI grammar | TS/Rust ops seed analytics ops | runtime/docs say analytics is derived, not truth | Loom has no analytics grammar | diverged | API plane exists, CLI/TUI absent | keep as planned with truth boundary |
| `governance/policy/control` | `governance` and `control` families seeded; root `policy` not seeded | CLI still scaffolds `governance` and `supervisor` only | SDK ops seed governance/control constants | runtime/docs use governance/control vocabulary | Loom has no matching command family | diverged | CLI naming lags API family canon; `policy` root is unsafe | target `govern` / `control`; forbid root `policy` |
| `machine/license` | identity family exists; V42-V50 docs define posture boundaries | no CLI grammar | no typed SDK auth/license machine clients audited | runtime/docs define posture-only ownership and non-implementation | Loom may display future safe refs only | diverged | contracts exist but no command canon yet | keep as planned future diagnostic family only |
| `limits` | limit and reconciliation contracts exist in docs | no CLI grammar | no audited SDK surface | runtime/docs define posture only | Loom may display safe posture later | diverged | boundary exists without command surface | keep as planned status-only family |
| `cloud` | no direct family audited | no CLI grammar | no audited SDK surface | runtime/docs do not expose local cloud CLI | Loom has no cloud commands | gap | no current canonical owner | leave planned/future only |
| `release/update` | no direct family audited | no CLI grammar | no audited SDK surface | runtime/docs treat service/bootstrap separately | Loom has no release/update commands | gap | packaging/update plane unresolved | keep future-facing and non-claiming |

## Holes / Missing Decisions

* exact boundary between `yai status`, `yai system status`, and `yai runtime status`
* whether client commands are separate from shell commands
* whether operator context has direct CLI commands or remains under case
* whether governance, policy, and control are one family, two families, or a nested set
* whether root `query`, `inspect`, and `logs` are canonical or remain debug/dev or family-specific
* whether machine, license, entitlement, and limits commands become real CLI families or stay API/SDK-first
* when session commands become hidden or removed from public help
* how SDK surfaces map to CLI commands once V51 normalizes the registry narrative
* how `runtime_action_key` should map to CLI command families; no stable key was exposed by the audited repos in this wave
* whether `account` becomes a first-class CLI family or stays distributed across `auth`, `identity`, `license`, and `config`
* whether `job` is a real family or only a projection over workflow/control/runtime records
* whether `support` and `admin` belong to local CLI at all

## Future Test Matrix

| command | expected exit class | sealed / no-auth behavior | local-dev behavior | active-case behavior | future licensed behavior | JSON output required | snapshot test required | integration test required |
| ------- | ------------------- | ------------------------- | ----------------- | ------------------- | ----------------------- | ------------------- | --------------------- | ------------------------- |
| `yai auth login --local-dev` | success or truthful unavailable | should not require runtime unseal | primary path | no active case required | must not fabricate entitlement/license | yes | yes | yes |
| `yai auth status` | success | inspection allowed while sealed | shows local-dev posture | no active case required | must stay distinct from session/runtime health | yes | yes | yes |
| `yai auth logout` | success or truthful no-op | should not stop runtime or clear shell/client | clears local-dev marker only | must not delete cases | must not mutate machine/license truth | yes | yes | yes |
| `yai case root` | success / governed failure | blocked on missing auth posture | local-dev path enabled | no active case required | must not depend on session | yes | yes | yes |
| `yai case open <path>` | success / governed failure | blocked on missing auth posture | local-dev path enabled | no active case required | must remain local case-tree mutation | yes | yes | yes |
| `yai case enter <case>` | success / governed failure | blocked when sealed for operator selection | local-dev path enabled | sets active case | future licensed flow must not revive session | yes | yes | yes |
| `yai case leave` | success / no-op | allowed while sealed | local-dev path enabled | clears active case | must remain distinct from logout | yes | yes | yes |
| `yai case status` | success | inspection allowed while sealed | local-dev path enabled | shows active case posture | future license/machine posture may decorate but not own it | yes | yes | yes |
| `yai runtime status` | success / runtime unavailable / config error | still available while sealed | unchanged | no active case required | must keep lifecycle separate from authorization | yes | yes | yes |
| `yai shell list` | success / truthful unavailable | allowed while sealed | unchanged | no active case required | must stay UX-only | yes | yes | no |
| `yai shell attach <shell_id>` | success / truthful unavailable | allowed while sealed | unchanged | no active case required | must not imply login or runtime start | yes | yes | no |
| `yai session status` | success / runtime unavailable | inspection allowed | unchanged | no active case required | must remain clearly legacy | yes | yes | yes |
| `yai provider list` | success / runtime unavailable | diagnostic allowed | unchanged | no active case required | must not imply provider execution | yes | yes | yes |
| `yai models list` | success / runtime unavailable | diagnostic allowed | unchanged | no active case required | must not imply model execution | yes | yes | yes |
| `yai system status` | success / runtime unavailable | inspection allowed while sealed | unchanged | no active case required | target command for post-V51 rename path | yes | yes | yes |

## Final Classification Summary

* `P0` commands: `yai auth login`, `yai auth login --local-dev`, `yai auth status`, `yai auth logout`, `yai case root`, `yai case list`, `yai case open`, `yai case enter`, `yai case leave`, `yai case status`, `yai case close`, `yai shell`, `yai shell list`, `yai shell attach`, `yai shell detach`, `yai runtime status`, `yai version`, `yai doctor`, `yai session status`
* `P1` commands: `yai system status`, `yai client list`, `yai client status`, `yai config show`, `yai config path`, `yai provider list`, `yai models list`, `yai machine status`, `yai machine enroll`, `yai machine authorization status`, `yai license status`, `yai license check`, `yai license lease status`, `yai entitlement status`, `yai limits status`
* legacy commands: `yai runtime status`, `yai session status`, `yai flow ...`, singular `yai provider ...`, singular `yai agent ...`, root `yai records ...`
* forbidden commands: `yai runtime start`, `yai runtime stop`, `yai runtime restart`, root `yai policy ...`, root `yai query ...`, root `yai inspect ...`
* external/dev-wrapper commands: `make yai`, `make info`, `make install-service`, `make uninstall-service`, `launchctl ...`, `cargo run ...`, likely `yai admin ...`, likely `yai support contact`
* `unknown_needs_audit` commands: `yai account ...`, `yai context ...`, `yai client attach`, `yai client detach`, `yai job ...`, `yai lease execution ...`, `yai recall query ...`, `yai evidence ...`, `yai logs ...`, `yai cloud ...`
