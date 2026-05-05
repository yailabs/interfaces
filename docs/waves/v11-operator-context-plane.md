# V11 - Operator Context Plane

## Status

* Delivery: V11
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: operator context model documentation + local operator context alignment
* Previous delivery: V10.6 - CLI Binary Precedence / Runtime Carrier Boundary
* Next delivery: V12 - Client Connection Model

## Purpose

V11 generalizes active case ownership into the canonical operator context plane.

## Scope

Record:

* operator context plane documented;
* local operator context marker shape documented/aligned;
* `active_case_ref` remains outside session;
* auth owns principal/auth_context;
* case tree owns case existence;
* operator context owns current active case selection;
* client/shell lifecycle remains deferred to V12/V13;
* runtime readiness remains separate;
* installed CLI invocation remains canonical;
* session remains legacy compatibility only.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/operator/operator-context-plane.md` | create | canonical operator context model |
| api | `docs/waves/v11-operator-context-plane.md` | create | delivery report |
| cli | `src/commands/case.rs` | implementation | operator context marker shape alignment |
| cli | `src/app/cli.rs` | help text | active-case wording aligned to operator context |

## Operator Context State

| Field | Value |
| ----- | ----- |
| marker path | `~/.yai/operator/context.json` or `$YAI_CONFIG_HOME/operator/context.json` |
| schema | `yai.operator-context.v1` |
| source | `cli` |
| principal | `local-dev:<value>` |
| auth_context | `local-dev` |
| root_case_ref | `case://<account-username>` |
| current root example | `case://francescomaiomascio` |
| active_case_ref | case URI or null |
| client_ref | `cli` |
| shell_ref | null |
| session mutation | none |

## Ownership Model

| Concern | Owner after V11 |
| ------- | --------------- |
| principal | auth plane |
| auth_context | auth plane |
| root_case_ref | case plane |
| case existence | case tree manifest |
| active_case_ref | operator context |
| client connection | deferred to V12 |
| shell lifecycle | deferred to V13 |
| runtime health/readiness | runtime plane |
| session | legacy compatibility only |

## Command Behavior After V11

| Command | Expected behavior after V11 |
| ------- | --------------------------- |
| `yai case enter <case>` | writes operator context active_case_ref |
| `yai case leave` | clears operator context active_case_ref |
| `yai case status` | reports active case owner as operator context |
| `yai case list` | marks active case from operator context |
| `yai auth status` | may report active case but must not own it |
| `yai auth logout` | V27 policy deferred; observed behavior recorded below |

## Installed CLI Validation

| Check | Result | Notes |
| ----- | ------ | ----- |
| installed CLI path | verify locally with `which yai` | installed CLI must resolve in the current shell |
| plain `which yai` residual | `/usr/local/bin/yai` | runtime carrier still shadows in plain PATH |
| canonical smoke command form | `yai` | verify with `which yai`, then use plain `yai ...` |
| primary smoke uses `cargo run` | no | required |
| primary smoke uses `YAI_CONFIG_HOME` | no | required |
| primary smoke uses `YAI_ACCOUNT_USERNAME` | no | required |

## Boundary Rules

```text
operator context != session
operator context != auth login
operator context != account_ref
operator context != case tree
operator context != shell/client attach
operator context != runtime readiness
operator context owns active_case_ref
auth owns principal/auth_context
case tree owns case existence
runtime owns health/readiness
session remains legacy compatibility only
```

## Logout Policy

V11 does not implement V27 logout policy.

Observed behavior:

| Operation | Behavior |
| --------- | -------- |
| `yai auth logout` with active case | auth marker cleared; operator context retained |
| operator context marker | retained |
| active_case_ref | retained |
| root marker | retained |
| case tree manifest | retained |
| session mutation | none |

## Deferred to Later Waves

| Deferred item | Future wave |
| ------------- | ----------- |
| client connection model | V12 |
| shell UX model | V13 |
| runtime sealed enforcement | V14 |
| SDK runtime alignment | V20 |
| CLI SDK-first wiring | V21 |
| API operator context surfaces | V37 |
| SDK case clients | V39 |
| logout policy with active case/job | V27 |

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
| api | `test -f docs/operator/active-case-ref.md` | pass | baseline |
| api | `test -f docs/waves/v10-active-case-refactor.md` | pass | baseline |
| api | `test -f docs/cli/canonical-cli-invocation.md` | pass | baseline |
| api | `test -f docs/waves/v10-5-canonical-cli-install-and-invocation.md` | pass | baseline |
| api | `test -f docs/cli/cli-runtime-binary-boundary.md` | pass | baseline |
| api | `test -f docs/waves/v10-6-cli-binary-precedence-runtime-boundary.md` | pass | baseline |
| api | `test -f docs/operator/operator-context-plane.md` | pass | new operator context doc |
| api | `test -f docs/waves/v11-operator-context-plane.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| cli | `cargo fmt --check` | pass | exact result |
| cli | `cargo test` | pass | exact result; warnings only |
| cli | `cargo build` | pass | exact result; warnings only |
| cli | `cargo install --path . --force` | pass | installed CLI; warnings only |
| shell | `which yai` | pass | resolved to the installed CLI in the validation shell |
| shell | `yai --help` | pass | CLI help |
| shell | `yai auth login --local-dev` | pass | setup; no env username/config override |
| shell | `yai case open projects/site-e0-cleanup` | pass | setup |
| shell | `yai case enter projects/site-e0-cleanup` | pass | verified operator context |
| shell | inspect `~/.yai/operator/context.json` | pass | verified V11 marker shape and `active_case_ref` |
| shell | `yai case status` | pass | active case owner reported |
| shell | `yai auth status` | pass | active case reported without auth ownership |
| shell | `yai case leave` | pass | active case cleared |
| sdk | docs validation | not run | no SDK files changed |
| loom | docs validation | not run | no Loom files changed |

## Post-Edit Scans

```bash
rg -n "operator context|operator_context|active_case_ref|client_ref|shell_ref|auth_context|root_case_ref|session remains legacy|installed CLI|runtime carrier|session" docs/operator docs/waves docs/case docs/cli
```

Result: pass; V11 docs contain the expected operator context, installed CLI and
boundary terms.

```bash
rg -n "operator context|operator_context|active_case_ref|client_ref|shell_ref|auth_context|root_case_ref|Session was not modified|Session: legacy|case enter|case leave|case status|auth status|cargo run|YAI_CONFIG_HOME|YAI_ACCOUNT_USERNAME" src README.md MIGRATION_MAP.md
```

Result: pass; changed CLI source and existing docs contain the expected owner
and boundary terms. Cargo/env references remain debug/test-only documentation.

```bash
rg -n "session owns active case|session active case|active session case|operator context is session|session updated|session created|canonical smoke.*cargo run|canonical.*YAI_CONFIG_HOME|canonical.*YAI_ACCOUNT_USERNAME|production account connected|entitlement granted|machine authorized|Supabase login|device login complete|case://user root created|case://me root marker" api cli sdk loom
```

Result: pass; matches are legacy negative policy text or recorded forbidden-scan
commands, not new V11 implementation claims. Canonical-env/cargo matches are
historical V10.5/V10.6 validation records, not V11 primary smoke behavior.

## Findings

### Finding A - Operator Context Plane Exists

V11 defines the operator context plane as the owner of operational selections.

### Finding B - Active Case Ownership Is Stable

`operator_context.active_case_ref` remains the canonical active case owner.

### Finding C - Operator Context Is Not Auth

Auth provides principal/auth_context. Operator context uses that posture but does
not own login.

### Finding D - Operator Context Is Not Client/Shell Lifecycle

Client connection and shell lifecycle remain deferred to V12/V13.

### Finding E - V12 Can Define Client Connection Model

With operator context separated, V12 can define one-shot and long-lived client
connection semantics.

### Finding F - Installed CLI Path Remains Canonical

V11 validation uses installed `yai`, not `cargo run`. The V10.6 PATH residual
remains tracked.

## V11 Completion Checklist

* [x] `docs/operator/operator-context-plane.md` exists
* [x] `docs/waves/v11-operator-context-plane.md` exists
* [x] operator context ownership documented
* [x] active_case_ref ownership documented
* [x] principal/auth_context ownership remains auth plane
* [x] case existence ownership remains case tree
* [x] client/shell lifecycle deferred to V12/V13
* [x] runtime readiness remains separate
* [x] session remains legacy compatibility only
* [x] operator context marker shape/path recorded
* [x] installed CLI smoke path recorded
* [x] primary smoke does not use cargo run
* [x] primary smoke does not use YAI_CONFIG_HOME
* [x] primary smoke does not use YAI_ACCOUNT_USERNAME
* [x] no session mutation added
* [x] no client/shell attach implementation added
* [x] no production auth added
* [x] no account_ref/entitlement_ref/machine_authorization_ref added
* [x] no SDK operator/case client implementation added
* [x] no Loom behavior implementation added
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
