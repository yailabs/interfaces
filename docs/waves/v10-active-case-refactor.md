# V10 - Active Case Refactor

## Status

* Delivery: V10
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: CLI active case operator-context implementation + documentation/report
* Previous delivery: V9 - Case Commands
* Next delivery: V11 - Operator Context Plane

## Purpose

V10 moves active case selection out of session and into:

```text
operator_context.active_case_ref
```

## Scope

Record:

* `yai case enter <case>` now selects active case;
* `yai case leave` now clears active case;
* active case is stored outside session;
* active case must reference an existing local case;
* `case enter` does not create cases;
* `case leave` does not close cases;
* `case close` refuses to close active case;
* session remains legacy compatibility only.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/operator/active-case-ref.md` | create | active case ownership model |
| api | `docs/waves/v10-active-case-refactor.md` | create | delivery report |
| cli | `src/commands/case.rs` | implementation | active case operator context |
| cli | `src/commands/auth.rs` | implementation | report active case from auth status when present |
| cli | `README.md` | docs | document local operator context active case |
| cli | `MIGRATION_MAP.md` | docs | record V10 active case ownership |

## Operator Context State

| Field | Value |
| ----- | ----- |
| operator context path | `~/.yai/operator/context.json` or `$YAI_CONFIG_HOME/operator/context.json` |
| schema | `yai.operator-context.active-case.v1` |
| owner/source | `cli` |
| root case ref | `case://<account-username>` |
| current root example | `case://francesco` |
| active case field | `active_case_ref` |
| active case owner | `operator_context.active_case_ref` |
| session mutation | none |

## Command Surface After V10

| Command | Status after V10 | Behavior |
| ------- | --------------- | -------- |
| `yai case root` | implemented | prints username-root and active case if present |
| `yai case list` | implemented | lists cases and marks active if present |
| `yai case open <path-or-uri>` | implemented | creates/ensures case; does not select active |
| `yai case enter <case>` | implemented | sets `operator_context.active_case_ref` |
| `yai case leave` | implemented | clears `operator_context.active_case_ref` |
| `yai case status` | implemented | shows root/tree/active-case owner |
| `yai case close <case>` | implemented | refuses active/root; closes non-active nested leaf |

## Active Case Rules

Record:

* active case must be an existing case in the local tree manifest;
* `case enter` normalizes `case://me`;
* `case enter` rejects `case://user`;
* `case enter` does not create cases;
* `case open` does not select active case;
* `case leave` does not close cases;
* `case close` refuses the active case;
* root may be selected if it exists in the local tree manifest;
* root cannot be closed;
* session is not modified.

## Logout Policy

V10 does not implement V27 logout policy.

Observed behavior:

| Operation | Behavior |
| --------- | -------- |
| `yai auth logout` with active case | not retested in V10 smoke; implementation clears auth marker only |
| root marker | retained |
| case tree manifest | retained |
| operator context marker | retained unless explicitly changed by `yai case leave` |
| session mutation | none |

## Boundary Rules

```text
active case != session
active case != auth login
active case != root case creation
active case != shell/client attach
active case != runtime readiness
operator_context.active_case_ref must reference an existing case
case enter does not create cases
case leave does not close cases
case close does not clear active case implicitly
```

## Deferred to Later Waves

| Deferred item | Future wave |
| ------------- | ----------- |
| full operator context plane | V11 |
| client connection model | V12 |
| shell UX model | V13 |
| runtime sealed enforcement | V14 |
| case-bound jobs | V24 |
| logout policy with active jobs/cases | V27 |
| case evidence binding | V28 |
| knowledge binding | V29 |
| SDK case clients | V39 |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/waves/v0-command-reality-audit.md` | pass | baseline |
| api | `test -f docs/adr/ADR-V1-session-death-decision.md` | pass | baseline |
| api | `test -f docs/compat/session-legacy-containment.md` | pass | baseline |
| api | `test -f docs/waves/v2-legacy-session-containment.md` | pass | baseline |
| api | `test -f docs/waves/v3-auth-command-model.md` | pass | baseline |
| api | `test -f docs/waves/v4-local-dev-auth.md` | pass | baseline |
| api | `test -f docs/identity/principal-model.md` | pass | baseline |
| api | `test -f docs/waves/v5-principal-model.md` | pass | baseline |
| api | `test -f docs/case/root-user-case.md` | pass | baseline |
| api | `test -f docs/waves/v6-root-user-case.md` | pass | baseline |
| api | `test -f docs/case/case-uri-model.md` | pass | baseline |
| api | `test -f docs/waves/v7-case-uri-model.md` | pass | baseline |
| api | `test -f docs/case/case-tree-model.md` | pass | baseline |
| api | `test -f docs/waves/v8-case-tree-model.md` | pass | baseline |
| api | `test -f docs/case/case-commands.md` | pass | baseline |
| api | `test -f docs/waves/v9-case-commands.md` | pass | baseline |
| api | `test -f docs/operator/active-case-ref.md` | pass | new operator doc |
| api | `test -f docs/waves/v10-active-case-refactor.md` | pass | new report |
| cli | `cargo fmt --check` | pass | exact result |
| cli | `cargo test` | pass | exact result; warnings only |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v10-active-case-test cargo run --quiet -- auth login --local-dev` | pass | setup |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v10-active-case-test cargo run --quiet -- case open projects/site-e0-cleanup` | pass | create nested case |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v10-active-case-test cargo run --quiet -- case enter projects/site-e0-cleanup` | pass | selected active case |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v10-active-case-test cargo run --quiet -- case status` | pass | active case reported |
| cli | inspect operator context JSON | pass | verified `active_case_ref` |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v10-active-case-test cargo run --quiet -- case list` | pass | active case marked with `*` |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v10-active-case-test cargo run --quiet -- case close projects/site-e0-cleanup` | pass | refused while active with exit 2 |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v10-active-case-test cargo run --quiet -- case leave` | pass | active case cleared |
| cli | inspect operator context JSON after leave | pass | verified `active_case_ref: null` |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v10-active-case-test cargo run --quiet -- case close projects/site-e0-cleanup` | pass | closed after leave |
| cli | inspect case tree manifest JSON | pass | root retained and nested closed |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v10-active-case-test cargo run --quiet -- case enter projects/missing` | pass | rejected missing case with exit 5 |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v10-active-case-test cargo run --quiet -- case enter case://user/projects/x` | pass | rejected placeholder URI with exit 2 |
| sdk | docs validation | not run | no SDK files changed |
| loom | docs validation | not run | no Loom files changed |

## Findings

### Finding A - Active Case Moved Out of Session

V10 stores active case in `operator_context.active_case_ref`, not in session.

### Finding B - Enter/Leave Are Now Operational

`yai case enter` and `yai case leave` now mutate the local operator context.

### Finding C - Enter Does Not Create Cases

A case must already exist in the local tree before it can be entered.

### Finding D - Close Protects Active Case

`yai case close` refuses to close the active case until `yai case leave` clears
it.

### Finding E - V11 Can Generalize Operator Context

V10 creates the active-case field. V11 can model the broader operator context
plane distinct from client/shell.

## V10 Completion Checklist

* [x] `docs/operator/active-case-ref.md` exists
* [x] `docs/waves/v10-active-case-refactor.md` exists
* [x] `yai case enter <case>` sets active case
* [x] `yai case leave` clears active case
* [x] active case is stored outside session
* [x] operator context marker path recorded
* [x] `operator_context.active_case_ref` recorded
* [x] `yai case status` reports active case owner
* [x] `yai case list` reports/marks active case if implemented
* [x] `yai case close` refuses active case
* [x] `case enter` rejects missing cases
* [x] `case enter` rejects `case://user`
* [x] `case enter` does not create cases
* [x] `case leave` does not close cases
* [x] root case cannot be closed
* [x] no session mutation added
* [x] no production auth added
* [x] no account_ref/entitlement_ref/machine_authorization_ref added
* [x] no SDK case/operator client implementation added
* [x] no Loom behavior implementation added
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
