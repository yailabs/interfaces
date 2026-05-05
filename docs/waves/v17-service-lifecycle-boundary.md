# V17 - Service Lifecycle Boundary

## Status

* Delivery: V17
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: service lifecycle boundary documentation + local CLI status wording alignment
* Previous delivery: V16 - Allowed / Blocked Surfaces
* Next delivery: V18 - Dev Wrapper Boundary

## Purpose

V17 separates runtime service lifecycle from readiness and operational
authorization.

## Scope

Record:

* service lifecycle boundary documented;
* lifecycle states documented;
* operational readiness remains separate;
* `runtime_transport_unavailable` remains transport/lifecycle posture;
* status output aligned where scoped;
* no start/stop/restart behavior added;
* no service manager behavior added;
* session remains ignored as lifecycle/readiness/authorization source.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/runtime/service-lifecycle-boundary.md` | create | lifecycle/readiness boundary |
| api | `docs/waves/v17-service-lifecycle-boundary.md` | create | delivery report |
| cli | `README.md` | docs | lifecycle/readiness boundary wording |
| cli | `MIGRATION_MAP.md` | docs | runtime surface lifecycle note |
| cli | `src/output/render.rs` | implementation | runtime status lifecycle wording |
| cli | `tests/output_snapshot.rs` | test | runtime plain snapshot alignment |

## Lifecycle Model

| Field/state | Meaning | Owner |
| ----------- | ------- | ----- |
| `running` | runtime process alive | service lifecycle |
| `stopped` | runtime process not running | service lifecycle |
| `degraded` | runtime alive but impaired | service lifecycle/health |
| `unavailable` | lifecycle cannot be inspected | transport/lifecycle |
| `unknown` | lifecycle not known | status projection |
| `operationalReadiness` | governed operation allowed/blocked | readiness/governance |
| `sealReason` | reason for sealed/blocked posture | readiness/governance |

## Boundary Matrix

| Statement | Required truth |
| --------- | -------------- |
| runtime running authorizes operations | false |
| runtime healthy authorizes operations | false |
| runtime stopped logs out user | false |
| auth logout stops runtime | false |
| shell detach stops runtime | false |
| client detach stops runtime | false |
| session controls lifecycle | false |
| transport unavailable means auth failure | false |

## Runtime Status Output

Observed `yai runtime status` after V17, sealed/no-auth:

```text
Runtime status:
Lifecycle: unavailable
Health: unavailable
Readiness: unavailable
Transport: runtime_transport_unavailable

Operational readiness: sealed
Seal reason: missing_auth_context

Lifecycle is not authorization.
Runtime health/status does not imply operational authorization.
Transport unavailable is transport/lifecycle posture, not auth failure.
Session was not used.
```

Observed `yai runtime status` after local auth + active case, with transport still
unavailable:

```text
Runtime status:
Lifecycle: unavailable
Health: unavailable
Readiness: unavailable
Transport: runtime_transport_unavailable

Operational readiness: ready
Seal reason: none

Runtime transport is unavailable, but local operational posture is ready.
Lifecycle is not authorization.
Runtime health/status does not imply operational authorization.
Transport unavailable is transport/lifecycle posture, not auth failure.
Session was not used.
```

## Installed CLI Validation

| Check | Result | Notes |
| ----- | ------ | ----- |
| `which yai` | pass | installed CLI resolved in current shell |
| `yai --help` | pass | installed CLI |
| primary smoke uses `cargo run` | no | required |
| primary smoke uses `YAI_CONFIG_HOME` | no | required |
| primary smoke uses `YAI_ACCOUNT_USERNAME` | no | required |
| path-bound invocation reintroduced as canonical | no | required |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/runtime/service-lifecycle-boundary.md` | pass | new runtime doc |
| api | `test -f docs/waves/v17-service-lifecycle-boundary.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| cli | `cargo fmt --check` | pass | formatting clean |
| cli | `cargo test` | pass | warnings only |
| cli | `cargo build` | pass | warnings only |
| cli | `cargo install --path . --force` | pass | installed CLI successfully |
| yai | `make info` | pass | build metadata printed |
| yai | `make yai` | pass | nothing to be done |
| shell | `which yai` | pass | installed CLI resolution |
| shell | `yai runtime status` | pass | lifecycle/readiness projection; exit `4` with transport unavailable |
| shell | `yai auth status` | pass | auth posture separate |
| shell | `yai case status` | pass | case/operator posture separate |
| shell | `yai auth login --local-dev` | pass | setup |
| shell | `yai case open projects/lifecycle-check` | pass | setup |
| shell | `yai case enter projects/lifecycle-check` | pass | setup active |
| shell | `yai runtime status` | pass | local ready + transport unavailable still distinct; exit `4` |
| shell | cleanup `yai case leave` / `yai case close projects/lifecycle-check` / `yai auth logout` | pass | cleanup |
| sdk | docs validation | not run | docs-only; no SDK files touched |
| loom | docs validation | not run | docs-only; no Loom files touched |

## Findings

### Finding A - Lifecycle Boundary Exists

Record:
V17 separates runtime service lifecycle from readiness and authorization.

### Finding B - Running Can Still Be Sealed

Record:
A running or healthy runtime may still block operational mutation if auth/case/operator
posture is missing.

### Finding C - Transport Unavailable Is Separate

Record:
`runtime_transport_unavailable` is a transport/lifecycle inspection issue, not
auth failure.

### Finding D - Logout/Detach Do Not Stop Runtime

Record:
Auth logout, shell detach and client detach do not stop runtime.

### Finding E - V18 Can Define Dev Wrapper Boundary

Record:
With lifecycle separated from readiness, V18 can distinguish dev wrapper behavior
from future service manager behavior.

## V17 Completion Checklist

* [x] `docs/runtime/service-lifecycle-boundary.md` exists
* [x] `docs/waves/v17-service-lifecycle-boundary.md` exists
* [x] lifecycle states documented
* [x] lifecycle/readiness boundary documented
* [x] running-but-sealed documented
* [x] runtime transport unavailable documented separately
* [x] logout does not stop runtime
* [x] shell/client detach does not stop runtime
* [x] session does not control lifecycle
* [x] no runtime start/stop/restart behavior added
* [x] no service manager behavior added
* [x] no production auth added
* [x] no Supabase/database integration added
* [x] no SDK runtime/client implementation added
* [x] no Loom behavior implementation added
* [x] installed CLI validation used
* [x] primary smoke does not use cargo run
* [x] primary smoke does not use YAI_CONFIG_HOME
* [x] primary smoke does not use YAI_ACCOUNT_USERNAME
* [x] path-bound invocation not reintroduced as canonical
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
