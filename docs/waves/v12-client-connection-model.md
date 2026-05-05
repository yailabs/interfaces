# V12 - Client Connection Model

## Status

* Delivery: V12
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: client connection model documentation + optional CLI/help/status wording alignment
* Previous delivery: V11 - Operator Context Plane
* Next delivery: V13 - Shell UX Model

## Purpose

V12 defines explicit client connection lifecycle semantics.

## Scope

Record:

* client connection model documented;
* one-shot CLI model documented;
* long-lived Loom/UI model documented;
* SDK transport client model documented;
* client does not own auth;
* client does not own case;
* client does not own active case;
* client does not own runtime lifecycle;
* client does not own session;
* shell attach/detach deferred to V13.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/client/client-connection-model.md` | create | canonical client connection model |
| api | `docs/waves/v12-client-connection-model.md` | create | delivery report |
| cli | `README.md` | docs | one-shot CLI client wording |
| sdk | `README.md` | docs | SDK transport client boundary |
| loom | `README.md` | docs | long-lived client boundary |

## Client Model

| Client | Kind | Lifecycle | Domain ownership |
| ------ | ---- | --------- | ---------------- |
| CLI | `cli-one-shot` | one-shot | none |
| Loom | `loom-tui` | long-lived | none |
| VS Code | `vscode-extension` | long-lived | none |
| Desktop | `desktop-app` | long-lived | none |
| SDK | `sdk-embedded` | library-managed | none |
| Runtime internal | `service/internal` | service/internal | none |

## Ownership Model

| Concern | Owner after V12 |
| ------- | --------------- |
| principal | auth plane |
| auth_context | auth plane |
| root_case_ref | case plane |
| case existence | case tree manifest |
| active_case_ref | operator context |
| client_ref | client connection plane |
| shell lifecycle | deferred to V13 |
| runtime lifecycle | runtime/service plane |
| runtime readiness | runtime readiness plane |
| session | legacy compatibility only |

## Command Behavior After V12

| Command/surface | Expected behavior after V12 |
| --------------- | --------------------------- |
| installed `yai ...` | one-shot CLI client |
| `yai auth ...` | auth plane commands invoked by CLI client |
| `yai case ...` | case/operator commands invoked by CLI client |
| Loom | long-lived client/TUI model, no domain ownership |
| SDK clients | transport clients, no domain ownership |
| `yai client attach/detach` | deferred |
| `yai shell attach/detach` | deferred to V13 |

## Installed CLI Validation

| Check | Result | Notes |
| ----- | ------ | ----- |
| installed CLI path | verify locally with `which yai` | installed CLI must resolve in the current shell |
| plain `which yai` residual | not observed in current shell | `which yai` resolved to the installed CLI; V10.6 residual remains historical/tracked |
| canonical smoke command form | `yai` | verify with `which yai`, then use plain `yai ...` |
| primary smoke uses `cargo run` | no | required |
| primary smoke uses `YAI_CONFIG_HOME` | no | required |
| primary smoke uses `YAI_ACCOUNT_USERNAME` | no | required |

## Boundary Rules

Record:

```text
client connection != session
client connection != auth login
client connection != account_ref
client connection != root case
client connection != active case
client connection != operator context
client connection != runtime lifecycle
client connection != runtime readiness
shell attach/detach belongs to V13
```

## Deferred to Later Waves

| Deferred item | Future wave |
| ------------- | ----------- |
| shell UX model | V13 |
| runtime sealed enforcement | V14 |
| SDK runtime surface alignment | V20 |
| CLI SDK-first wiring | V21 |
| Loom alignment | V22 |
| VS Code alignment | V23 |
| API operator context surfaces | V37 |
| SDK case clients | V39 |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/client/client-connection-model.md` | pass | new client doc |
| api | `test -f docs/waves/v12-client-connection-model.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| cli | `cargo fmt --check` | not run | CLI source not touched |
| cli | `cargo test` | not run | CLI source not touched |
| cli | `cargo build` | not run | CLI source not touched |
| cli | `cargo install --path . --force` | pass | installed CLI; warnings only |
| shell | `which yai` | pass | resolved to the installed CLI in the validation shell |
| shell | `yai --help` | pass | installed CLI help with auth/case/session wording |
| shell | `yai auth status` | pass | truthful unauthenticated auth posture |
| shell | `yai case status` | fail | exited unauthenticated; missing local auth marker |
| sdk | docs validation | not run | docs-only |
| loom | docs validation | not run | docs-only |

## Post-Edit Scans

```bash
rg -n "client connection|client_ref|cli-one-shot|loom-tui|sdk-embedded|long-lived|one-shot|shell lifecycle|session remains legacy|runtime carrier" docs/client docs/waves docs/operator docs/cli
```

Expected:
matches in V12 docs.

```bash
rg -n "client connection|client_ref|cli-one-shot|loom-tui|sdk-embedded|long-lived|one-shot|shell attach|client attach|session" api cli sdk loom
```

Expected:
matches in V12 docs and any touched docs/help.

```bash
rg -n "client owns auth|client owns active case|client owns root case|client owns runtime lifecycle|client is session|session owns client|client attach implemented|shell attach implemented|production account connected|Supabase login complete|entitlement granted" api cli sdk loom
```

Expected:
no new fake ownership/implementation/backend claims.

Result:
matches only in historical validation command text, not as new implementation or
ownership claims.

## Findings

### Finding A - Client Model Exists

Record:
V12 defines explicit client connection lifecycle semantics.

### Finding B - CLI Is One-Shot

Record:
Installed `yai ...` commands are one-shot CLI client invocations.

### Finding C - Loom Is Long-Lived

Record:
Loom is a long-lived client/TUI surface, but does not own auth/case/operator
domain state.

### Finding D - SDK Is Transport

Record:
SDK clients are transport/library clients and do not own domain state.

### Finding E - V13 Can Define Shell UX

Record:
With client connection boundaries documented, V13 can define shell UX and
attach/detach semantics without reviving session.

## V12 Completion Checklist

* [x] `docs/client/client-connection-model.md` exists
* [x] `docs/waves/v12-client-connection-model.md` exists
* [x] one-shot CLI model documented
* [x] long-lived Loom/UI model documented
* [x] SDK transport client model documented
* [x] client_ref ownership documented
* [x] auth ownership remains auth plane
* [x] active_case_ref ownership remains operator context
* [x] case existence ownership remains case tree
* [x] runtime lifecycle/readiness remains separate
* [x] session remains legacy compatibility only
* [x] shell/client attach commands not implemented
* [x] installed CLI validation path recorded
* [x] primary smoke does not use cargo run
* [x] primary smoke does not use YAI_CONFIG_HOME
* [x] primary smoke does not use YAI_ACCOUNT_USERNAME
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
