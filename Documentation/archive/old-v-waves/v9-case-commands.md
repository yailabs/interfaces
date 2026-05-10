# V9 - Case Commands

## Status

* Delivery: V9
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: CLI case command implementation + documentation/report
* Previous delivery: V8 - Case Tree Model
* Next delivery: V10 - Active Case Refactor

## Purpose

V9 introduces canonical local CLI case commands:

```bash
yai case root
yai case list
yai case open <path-or-uri>
yai case enter <case>
yai case leave
yai case status
yai case close <case>
```

V9 does not implement active case selection. V10 owns
`operator_context.active_case_ref`.

## Scope

Record:

* case command surface added;
* root/list/open/status/close behavior implemented locally;
* enter/leave present but deferred to V10;
* username-root model preserved;
* `case://me` alias preserved;
* `case://user` remains placeholder/provisional only;
* session remains legacy compatibility only;
* no active case selection added.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `Documentation/case/case-commands.md` | create | canonical case command model |
| api | `Documentation/waves/v9-case-commands.md` | create | delivery report |
| cli | `src/app/cli.rs` | implementation | wire canonical case command parser surface |
| cli | `src/commands/case.rs` | implementation | local CLI case commands over case tree manifest |
| cli | `README.md` | docs | document V9 case command model |
| cli | `MIGRATION_MAP.md` | docs | record V9 case command status |

## Command Surface

| Command | Status after V9 | Behavior |
| ------- | --------------- | -------- |
| `yai case root` | implemented | prints local authenticated principal root case |
| `yai case list` | implemented | lists local case tree manifest |
| `yai case open <path-or-uri>` | implemented | creates or ensures nested manifest entry |
| `yai case enter <case>` | present, V10-deferred | no active case mutation; exits unavailable |
| `yai case leave` | present, V10-deferred | no active case mutation; exits unavailable |
| `yai case status` | implemented | shows root/tree/active-case posture |
| `yai case close <case>` | implemented | removes nested case entry; root cannot be closed |

## Case Tree State

| Field | Value |
| ----- | ----- |
| root form | `case://<account-username>` |
| current example root | `case://francesco` |
| alias | `case://me` |
| placeholder only | `case://user` |
| manifest path | `~/.yai/case/case-tree.json` or `$YAI_CONFIG_HOME/case/case-tree.json` |
| nested case creation command | `yai case open <path-or-uri>` |
| nested case close command | `yai case close <case>` |
| active case selected | no |
| session mutation | none |

## Case Open/Close Semantics

Record:

* `open` ensures nested case manifest entry;
* `open` does not select active case;
* `close` may remove nested leaf case;
* `close` must not close root;
* root marker remains retained;
* case tree marker remains retained;
* session is not modified.

## Active Case Deferral

```text
V9 introduces the command names `case enter` and `case leave`, but active case
selection is deferred to V10.

No `operator_context.active_case_ref` is created in V9.
No session-backed active case is introduced in V9.
```

## Boundary Rules

```text
case commands != session
case commands != production account auth
case commands != entitlement
case commands != machine authorization
case commands != runtime readiness
case enter/leave != implemented active case until V10
case://me != persisted root node
case://user != persisted canonical root
```

## Deferred to Later Waves

| Deferred item | Future wave |
| ------------- | ----------- |
| active case out of session | V10 |
| operator context plane | V11 |
| shell/client attach model | V13 |
| runtime sealed enforcement | V14 |
| case-bound jobs | V24 |
| case evidence binding | V28 |
| knowledge binding | V29 |
| SDK case clients | V39 |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/waves/v0-command-reality-audit.md` | pass | baseline |
| api | `test -f Documentation/adr/ADR-V1-session-death-decision.md` | pass | baseline |
| api | `test -f Documentation/compat/session-legacy-containment.md` | pass | baseline |
| api | `test -f Documentation/waves/v2-legacy-session-containment.md` | pass | baseline |
| api | `test -f Documentation/waves/v3-auth-command-model.md` | pass | baseline |
| api | `test -f Documentation/waves/v4-local-dev-auth.md` | pass | baseline |
| api | `test -f Documentation/identity/principal-model.md` | pass | baseline |
| api | `test -f Documentation/waves/v5-principal-model.md` | pass | baseline |
| api | `test -f Documentation/case/root-user-case.md` | pass | baseline |
| api | `test -f Documentation/waves/v6-root-user-case.md` | pass | baseline |
| api | `test -f Documentation/case/case-uri-model.md` | pass | baseline |
| api | `test -f Documentation/waves/v7-case-uri-model.md` | pass | baseline |
| api | `test -f Documentation/case/case-tree-model.md` | pass | baseline |
| api | `test -f Documentation/waves/v8-case-tree-model.md` | pass | baseline |
| api | `test -f Documentation/case/case-commands.md` | pass | new command doc |
| api | `test -f Documentation/waves/v9-case-commands.md` | pass | new report |
| cli | `cargo fmt --check` | pass | exact result after formatting |
| cli | `cargo test` | pass | exact result; warnings only |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v9-case-test cargo run --quiet -- auth login --local-dev` | pass | setup |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v9-case-test cargo run --quiet -- case root` | pass | root `case://francesco` reported |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v9-case-test cargo run --quiet -- case list` | pass | root list verified |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v9-case-test cargo run --quiet -- case open projects/site-e0-cleanup` | pass | nested case created in manifest |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v9-case-test cargo run --quiet -- case list` | pass | nested case appears |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v9-case-test cargo run --quiet -- case status` | pass | active case none |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v9-case-test cargo run --quiet -- case enter projects/site-e0-cleanup` | pass | expected V10-deferred message; exits unavailable |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v9-case-test cargo run --quiet -- case leave` | pass | expected V10-deferred message; exits unavailable |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v9-case-test cargo run --quiet -- case close projects/site-e0-cleanup` | pass | nested case removed |
| cli | inspect case tree manifest JSON | pass | root retained and nested case closed |
| sdk | docs validation | not run | no SDK files changed |
| loom | docs validation | not run | no Loom files changed |

## Findings

### Finding A - Case Commands Exist

V9 introduces the canonical local CLI case command surface.

### Finding B - Open/Close Mutate Tree, Not Active Case

`case open` and `case close` mutate the local case tree manifest, but do not
select or clear active case.

### Finding C - Enter/Leave Are Deferred

`case enter` and `case leave` exist as canonical command surfaces, but active
case selection is deferred to V10.

### Finding D - Session Remains Legacy

V9 does not use session as case owner, active case owner or harness.

### Finding E - V10 Can Add Active Case Refactor

With case commands present, V10 can implement `operator_context.active_case_ref`.

## V9 Completion Checklist

* [x] `Documentation/case/case-commands.md` exists
* [x] `Documentation/waves/v9-case-commands.md` exists
* [x] `yai case root` implemented or truthfully recorded
* [x] `yai case list` implemented or truthfully recorded
* [x] `yai case open <path-or-uri>` implemented or truthfully recorded
* [x] `yai case enter <case>` present and V10-deferred
* [x] `yai case leave` present and V10-deferred
* [x] `yai case status` implemented or truthfully recorded
* [x] `yai case close <case>` implemented or truthfully recorded
* [x] username-root model preserved
* [x] `case://me` alias preserved
* [x] `case://user` not persisted as canonical root
* [x] no active case selection added
* [x] no operator context active ref added
* [x] no session mutation added
* [x] no production auth added
* [x] no account_ref/entitlement_ref/machine_authorization_ref added
* [x] no SDK case client implementation added
* [x] no Loom behavior implementation added
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
