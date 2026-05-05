# V19 - Runtime Control Plan

## Status

* Delivery: V19
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: runtime control plan documentation + optional runtime status/control wording alignment
* Previous delivery: V18 - Dev Wrapper Boundary
* Next delivery: V20 - SDK Runtime Surface Alignment

## Purpose

V19 defines `controlPlan` as plan/projection, not runtime control execution.

## Scope

Record:

* controlPlan model documented;
* start/stop/restart remain unavailable/planned unless actually implemented;
* dev-wrapper remains separate from control execution;
* service manager remains separate from controlPlan;
* no fake start/stop/restart claims introduced;
* no runtime lifecycle behavior added.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/runtime/runtime-control-plan.md` | create | controlPlan model |
| api | `docs/waves/v19-runtime-control-plan.md` | create | delivery report |
| cli | `README.md` | update | runtime control wording |
| cli | `MIGRATION_MAP.md` | update | runtime control boundary note |
| sdk | `README.md` | update | runtime control boundary clarification |
| yai | `README.md` | update | dev-wrapper/controlPlan boundary |
| yai | `packaging/services/README.md` | update | service adapter/controlPlan boundary |

## controlPlan Model

| Field | Meaning |
| ----- | ------- |
| `serviceManager` | service manager detected/expected |
| `start.available` | whether canonical start is available |
| `start.reason` | why start is available/unavailable |
| `start.executionClaim` | whether start was executed |
| `stop.available` | whether canonical stop is available |
| `stop.reason` | why stop is available/unavailable |
| `stop.executionClaim` | whether stop was executed |
| `restart.available` | whether canonical restart is available |
| `restart.reason` | why restart is available/unavailable |
| `restart.executionClaim` | whether restart was executed |

## Boundary Matrix

| Statement | Required truth |
| --------- | -------------- |
| controlPlan executes start/stop | false |
| controlPlan proves service manager exists | false |
| dev-wrapper is controlPlan execution | false |
| Makefile start/install means canonical runtime control | false |
| runtime status claiming plan means action happened | false |
| session can execute runtime control | false |

## Runtime Status Behavior

```text
controlPlan projected in runtime status: no
```

Current local CLI status remains lifecycle/readiness-oriented. `controlPlan`
projection is deferred to V20/V21 rather than being faked in V19.

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
| api | `test -f docs/runtime/runtime-control-plan.md` | pass | new runtime doc |
| api | `test -f docs/waves/v19-runtime-control-plan.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | available and clean |
| yai | `make info` | pass | dev-wrapper validation |
| yai | `make yai` | pass | build validation |
| cli | `cargo fmt --check` | not run | CLI source not touched |
| cli | `cargo test` | not run | CLI source not touched |
| cli | `cargo build` | not run | CLI source not touched |
| cli | `cargo install --path . --force` | not run | CLI source not touched |
| shell | `which yai` | pass | resolved to the installed CLI in the current shell |
| shell | `yai runtime status` | pass | no `controlPlan` projected; lifecycle/readiness output remained truthful |
| sdk | docs validation | not run | docs-only boundary note |
| loom | docs validation | not run | docs untouched |

## Findings

### Finding A - controlPlan Exists

Record:
V19 defines `controlPlan` as plan/projection.

### Finding B - controlPlan Is Not Execution

Record:
`controlPlan` does not claim start/stop/restart executed.

### Finding C - Dev Wrapper Remains Separate

Record:
Makefile/service bootstrap surfaces remain dev-wrapper/ops surfaces, not
canonical runtime control.

### Finding D - Service Manager Remains Deferred

Record:
No service manager runtime control was implemented in V19.

### Finding E - V20 Can Align SDK Runtime Surface

Record:
With controlPlan semantics fixed, V20 can align SDK runtime status/controlPlan
fields without fake execution claims.
