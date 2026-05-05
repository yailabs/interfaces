# V13 - Shell UX Model

## Status

* Delivery: V13
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: shell UX model documentation + optional CLI command/help surfaces
* Previous delivery: V12 - Client Connection Model
* Next delivery: V14 - Runtime Sealed Enforcement

## Purpose

V13 defines shell as a UX/connection plane, not a domain owner.

## Scope

Record:

* shell UX model documented;
* shell is not session;
* shell attach is not auth login;
* shell detach is not auth logout;
* shell attach is not case enter;
* shell detach is not case leave;
* shell attach/detach does not mutate session;
* shell does not own runtime lifecycle;
* command surfaces added or explicitly not added.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/client/shell-ux-model.md` | create | canonical shell UX model |
| api | `docs/waves/v13-shell-ux-model.md` | create | delivery report |
| cli | `README.md` | docs | shell UX surface wording |
| cli | `MIGRATION_MAP.md` | docs | shell command family map |
| cli | `src/app/cli.rs` | command/help | add canonical `shell` command surface |
| cli | `src/commands/mod.rs` | command wiring | dispatch shell command family |
| cli | `src/commands/shell.rs` | create | truthful unavailable shell UX command surfaces |
| cli | `src/commands/session.rs` | help wording | point legacy session away from shell ownership |
| cli | `tests/help_snapshot.rs` | test | shell help coverage |
| cli | `tests/output_snapshot.rs` | test | shell unavailable output coverage |
| sdk | `README.md` | docs | SDK does not own shell UX |
| loom | `README.md` | docs | shell plane wording for Loom UX |
| loom | `docs/sdk-first-client-contract.md` | docs | shell plane boundary wording |

## Shell Command Surface

| Command | Status after V13 | Behavior |
| ------- | --------------- | -------- |
| `yai shell` | implemented | truthful unavailable shell UX surface |
| `yai shell list` | implemented | truthful unavailable shell registry inspection |
| `yai shell attach <shell_id>` | implemented | truthful unavailable UX connection command |
| `yai shell detach` | implemented | truthful unavailable UX disconnection command |

## Boundary Rules

Record:

```text
shell != session
shell attach != auth login
shell detach != auth logout
shell attach != case enter
shell detach != case leave
shell attach != runtime start
shell detach != runtime stop
shell does not own active_case_ref
shell does not own root_case_ref
shell does not own jobs
shell does not own permissions
session remains legacy compatibility only
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
| api | `test -f docs/client/shell-ux-model.md` | pass | new shell doc |
| api | `test -f docs/waves/v13-shell-ux-model.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| cli | `cargo fmt --check` | pass | after `cargo fmt` |
| cli | `cargo test` | pass | 16 tests passed; warnings only |
| cli | `cargo build` | pass | warnings only |
| cli | `cargo install --path . --force` | pass | installed CLI; warnings only |
| shell | `yai --help` | pass | installed CLI help includes `shell` |
| shell | `yai shell --help` | pass | shell command help with `list`, `attach`, `detach` |
| shell | `yai shell` | pass | truthful unavailable shell root surface; exit 5 |
| shell | `yai shell attach demo` | pass | truthful unavailable attach surface; exit 5 |
| shell | `yai shell detach` | pass | truthful unavailable detach surface; exit 5 |
| sdk | docs validation | not run | docs-only unless touched substantially |
| loom | docs validation | not run | docs-only unless touched substantially |

## Post-Edit Scans

```bash
rg -n "shell UX|shell != session|shell attach|shell detach|auth login|auth logout|case enter|case leave|runtime start|runtime stop|session remains legacy" docs/client docs/waves docs/operator
```

Expected:
matches in V13 docs.

```bash
rg -n "shell UX|shell attach|shell detach|shell != session|session attach|session detach|auth login|case enter|runtime start|runtime stop" api cli sdk loom
```

Expected:
matches in V13 docs and touched docs/help.

```bash
rg -n "shell owns auth|shell owns active case|shell owns root case|shell owns runtime lifecycle|shell is session|session owns shell|shell attach logs in|shell detach logs out|shell attach selects active case|shell detach leaves case|shell attach starts runtime|shell detach stops runtime|production account connected|Supabase login complete|entitlement granted" api cli sdk loom
```

Expected:
no new fake ownership/implementation/backend claims.

Result:
matches appear only inside historical validation command text and policy/report
surfaces, not as new positive implementation or ownership claims.

## Findings

### Finding A - Shell UX Model Exists

Record:
V13 defines shell as a UX/connection surface.

### Finding B - Shell Is Not Session

Record:
Shell attach/detach does not revive session as domain owner.

### Finding C - Shell Does Not Own Auth Or Case

Record:
Shell attach does not login. Shell detach does not logout. Shell attach/detach
does not enter or leave active case.

### Finding D - Shell Does Not Own Runtime Lifecycle

Record:
Shell attach/detach does not start or stop runtime.

### Finding E - V14 Can Enforce Runtime Sealed Posture

Record:
With auth/case/operator/client/shell planes separated, V14 can start enforcing
runtime sealed posture.

## V13 Completion Checklist

* [x] `docs/client/shell-ux-model.md` exists
* [x] `docs/waves/v13-shell-ux-model.md` exists
* [x] shell UX ownership documented
* [x] shell/session boundary documented
* [x] shell/auth boundary documented
* [x] shell/case boundary documented
* [x] shell/runtime lifecycle boundary documented
* [x] command surfaces added or explicitly not added
* [x] no session mutation added
* [x] no auth behavior changed
* [x] no active case behavior changed
* [x] no runtime lifecycle behavior changed
* [x] no production auth added
* [x] no Supabase/database integration added
* [x] no SDK shell/client implementation added
* [x] no Loom behavior implementation added
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
