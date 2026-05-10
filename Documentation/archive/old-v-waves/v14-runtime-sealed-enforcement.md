# V14 - Runtime Sealed Enforcement

## Status

* Delivery: V14
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: runtime sealed posture model + local CLI enforcement/report
* Previous delivery: V13 - Shell UX Model
* Next delivery: V15 - Runtime Readiness Projection

## Purpose

V14 introduces effective local sealed posture enforcement.

## Scope

Record:

* sealed posture model documented;
* local CLI operational guards added or confirmed;
* status/inspection surfaces remain truthful;
* operational actions are blocked without auth/case/operator posture;
* runtime health is not operational authorization;
* session does not unseal runtime;
* shell/client connection does not unseal runtime;
* no production backend added.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `Documentation/runtime/runtime-sealed-enforcement.md` | create | sealed posture model |
| api | `Documentation/waves/v14-runtime-sealed-enforcement.md` | create | delivery report |
| cli | `src/commands/case.rs` | implementation | local sealed enforcement for case operations |
| cli | `README.md` | docs | sealed posture wording |
| cli | `MIGRATION_MAP.md` | docs | sealed enforcement map |
| sdk | `README.md` | docs | sealed boundary clarification |
| loom | `README.md` | docs | sealed boundary clarification |

## Enforcement Matrix

| Command | Auth required | Case required | Active case required | Allowed sealed | Result |
| ------- | ------------- | ------------- | -------------------- | -------------- | ------ |
| `yai auth status` | no | no | no | yes | inspection |
| `yai runtime status` | no | no | no | yes | inspection |
| `yai case status` | no/yes | no/yes | no | yes if truthful | posture |
| `yai case open` | yes | root/tree | no | no | operational |
| `yai case enter` | yes | existing target | no | no | operational |
| `yai case leave` | no/yes | no | active optional | yes/no-op | clears operator context |
| `yai case close` | yes | existing target | target not active | no | operational |
| `yai shell ...` | no | no | no | yes if truthful-unavailable | UX only |

## Block Messages

Implemented local text-mode block messages:

```text
Operational action blocked: runtime is sealed for this command.
Reason: missing auth context.
Use `yai auth login --local-dev` for local development auth.
Runtime health/status does not imply operational authorization.
Session was not used.
```

```text
Operational action blocked: runtime is sealed for this command.
Reason: missing root case.
Run `yai auth login --local-dev` to ensure the local root case.
Session was not used.
```

```text
Operational action blocked: runtime is sealed for this command.
Reason: case boundary not found.
Use `yai case open <path-or-uri>` before selecting or closing this case.
Session was not used.
```

```text
Operational action blocked: active case safety.
Reason: target case is currently active.
Run `yai case leave` before closing this case.
Session was not used.
```

## Boundary Rules

Record:

```text
runtime running != runtime authorized
runtime healthy != operational actions allowed
client attached != login
auth login != shell
case selected != session
session does not unseal runtime
shell/client does not unseal runtime
```

## Installed CLI Validation

| Check | Result | Notes |
| ----- | ------ | ----- |
| installed CLI path | verify locally with `which yai` | installed CLI must resolve in the current shell |
| canonical smoke command form | `yai` | verify with `which yai`, then use plain `yai ...` |
| primary smoke uses `cargo run` | no | required |
| primary smoke uses `YAI_CONFIG_HOME` | no | required |
| primary smoke uses `YAI_ACCOUNT_USERNAME` | no | required |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/runtime/runtime-sealed-enforcement.md` | pass | new runtime doc |
| api | `test -f Documentation/waves/v14-runtime-sealed-enforcement.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| cli | `cargo fmt --check` | pass | after formatting `src/commands/case.rs` |
| cli | `cargo test` | pass | warnings only |
| cli | `cargo build` | pass | warnings only |
| cli | `cargo install --path . --force` | pass | installed CLI |
| shell | `yai auth status` | pass | inspection remained truthful; initial local state was `unauthenticated` |
| shell | clean/no-auth `yai case open projects/sealed-check` | pass | blocked with missing auth context, exit `6` |
| shell | clean/no-auth `yai case enter projects/sealed-check` | pass | blocked with missing auth context, exit `6` |
| shell | `yai auth login --local-dev` | pass | local-dev auth marker and root case restored |
| shell | `yai case open projects/sealed-check` | pass | allowed after auth, exit `0` |
| shell | `yai case enter projects/sealed-check` | pass | allowed after case exists, exit `0` |
| shell | `yai case close projects/sealed-check` | pass | blocked by active case safety, exit `6` |
| shell | `yai case leave` | pass | cleared operator context active case, exit `0` |
| shell | `yai case close projects/sealed-check` | pass | allowed after leave, exit `0` |
| sdk | docs validation | not run | docs-only unless touched substantially |
| loom | docs validation | not run | docs-only unless touched substantially |

Additional observed inspection results:

* `yai case status` before login: pass; reported sealed posture with `missing auth context`, exit `0`.
* `yai case status` after local-dev login: pass; reported `unsealed for local case operations`, exit `0`.
* `yai runtime status`: pass as truthful inspection; returned `runtime_transport_unavailable`, exit `4`.
* Post-validation cleanup: `yai auth logout` pass; auth marker cleared, root case and case tree markers retained by current CLI behavior.

## Findings

### Finding A - Sealed Posture Is Effective Locally

Record:
V14 blocks operational CLI actions when local auth/case/operator posture is
missing.

### Finding B - Runtime Inspection Remains Truthful

Record:
Status/inspection surfaces remain allowed where they do not mutate governed
state.

### Finding C - Session Does Not Unseal Runtime

Record:
Session is not used to authorize operational actions.

### Finding D - Shell/Client Do Not Unseal Runtime

Record:
Shell/client connection surfaces do not replace auth/case/operator context.

### Finding E - V15 Can Project Readiness

Record:
With local enforcement in place, V15 can align status output to readiness fields
such as `operationalReadiness` and `sealReason`.

## V14 Completion Checklist

* [x] `Documentation/runtime/runtime-sealed-enforcement.md` exists
* [x] `Documentation/waves/v14-runtime-sealed-enforcement.md` exists
* [x] sealed posture model documented
* [x] local operational action guards added or confirmed
* [x] missing auth blocks operational actions
* [x] missing case boundary blocks target case actions
* [x] active case safety still blocks close
* [x] status/inspection surfaces remain truthful
* [x] runtime health is not authorization
* [x] session does not unseal runtime
* [x] shell/client does not unseal runtime
* [x] no production auth added
* [x] no Supabase/database integration added
* [x] no account_ref/entitlement_ref/machine_authorization_ref added
* [x] no SDK runtime/client implementation added
* [x] no Loom behavior implementation added
* [x] installed CLI validation used
* [x] primary smoke does not use cargo run
* [x] primary smoke does not use YAI_CONFIG_HOME
* [x] primary smoke does not use YAI_ACCOUNT_USERNAME
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
