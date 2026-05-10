# V18 - Dev Wrapper Boundary

## Status

* Delivery: V18
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: dev-wrapper boundary documentation + local Documentation/help wording alignment
* Previous delivery: V17 - Service Lifecycle Boundary
* Next delivery: V19 - Runtime Control Plan

## Purpose

V18 separates dev-wrapper behavior from canonical service manager and runtime
control semantics.

## Scope

Record:

* dev-wrapper boundary documented;
* Makefile/script/service install surfaces classified;
* installed `yai` remains canonical user command;
* dev-wrapper does not authorize operations;
* dev-wrapper does not imply readiness;
* dev-wrapper does not own auth/case/operator context;
* no runtime control behavior added;
* no service lifecycle behavior changed.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `Documentation/runtime/dev-wrapper-boundary.md` | create | dev-wrapper boundary |
| api | `Documentation/waves/v18-dev-wrapper-boundary.md` | create | delivery report |
| yai | `README.md` | update | repo-level dev-wrapper vs canonical CLI boundary |
| yai | `packaging/services/README.md` | update | service bootstrap vs authorization/readiness boundary |
| cli | `README.md` | update | CLI vs external dev-wrapper boundary |
| cli | `MIGRATION_MAP.md` | update | migration row clarification for wrapper boundary |

## Dev Wrapper Classification

| Surface | Classification | Can authorize operations? | Can imply readiness? |
| ------- | -------------- | ------------------------- | -------------------- |
| `make yai` | `dev-wrapper/build` | no | no |
| `make info` | `dev-wrapper/inspection` | no | no |
| `make install` | `dev-wrapper/install` | no | no |
| `make install-service` | `dev-wrapper/service-bootstrap` | no | no |
| launchd/systemd | service manager / ops | no | no |
| installed `yai` | user-facing CLI | no by itself | no by itself |
| runtime carrier | service/internal | no by itself | no by itself |

## Boundary Matrix

| Statement | Required truth |
| --------- | -------------- |
| dev-wrapper authorizes operations | false |
| dev-wrapper implies readiness | false |
| dev-wrapper owns auth | false |
| dev-wrapper owns case selection | false |
| dev-wrapper owns operator context | false |
| dev-wrapper is session | false |
| service bootstrap means operationally unsealed | false |
| installed CLI command exists means runtime is running | false |

## Canonical Invocation

```bash
which yai
yai ...
```

Record:

* primary smoke uses `cargo run`: no
* primary smoke uses `YAI_CONFIG_HOME`: no
* primary smoke uses `YAI_ACCOUNT_USERNAME`: no
* path-bound `PATH=... yai` form reintroduced as canonical: no
* absolute installed CLI path reintroduced as canonical: no

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/runtime/dev-wrapper-boundary.md` | pass | new runtime doc |
| api | `test -f Documentation/waves/v18-dev-wrapper-boundary.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | available and clean |
| yai | `make info` | pass | read-only/dev-wrapper validation |
| yai | `make yai` | pass | build validation |
| cli | `cargo fmt --check` | not run | CLI source not touched |
| cli | `cargo test` | not run | CLI source not touched |
| cli | `cargo build` | not run | CLI source not touched |
| cli | `cargo install --path . --force` | not run | CLI source not touched |
| shell | `which yai` | pass | resolved to the installed CLI in the current shell |
| shell | `yai runtime status` | not run | V18 changed docs only |
| sdk | docs validation | not run | docs untouched |
| loom | docs validation | not run | docs untouched |

## Findings

### Finding A - Dev Wrapper Boundary Exists

Record:
V18 defines `dev-wrapper` as a development/ops bootstrap surface.

### Finding B - Dev Wrapper Does Not Authorize

Record:
Build/install/service bootstrap surfaces do not authorize operational mutation.

### Finding C - Dev Wrapper Does Not Imply Readiness

Record:
A successful build/install does not imply runtime readiness or operational
readiness.

### Finding D - Runtime Control Plan Remains Deferred

Record:
V18 does not introduce runtime control execution. V19 owns runtime control plan.

### Finding E - Canonical CLI Remains Separate

Record:
Installed `yai` remains the canonical operator command surface, separate from
Makefile/dev-wrapper surfaces.
