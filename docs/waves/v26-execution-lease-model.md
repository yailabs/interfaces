# V26 — Execution Lease Model

## Status

* Delivery: V26
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: execution lease model documentation + optional existing docs/status wording alignment
* Previous delivery: V25 — Case-bound Jobs
* Next delivery: V27 — Detach / Continuation Semantics

## Purpose

V26 defines execution leases for continuity of case-bound jobs.

## Scope

Record:

* execution_lease_ref vocabulary documented;
* execution_lease.job_ref invariant documented;
* execution_lease.case_ref invariant documented;
* execution lease lifecycle documented;
* execution lease vs license lease distinction documented;
* client detach boundary documented;
* no lease manager implemented;
* no execution behavior added;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/execution/execution-lease-model.md` | create | execution lease model |
| api | `docs/waves/v26-execution-lease-model.md` | create | delivery report |
| yai | `Documentation/execution/execution-lease-model.md` | create | runtime/core lease record |

## Lease Ownership Model

| Concern | Owner / role |
| ------- | ------------ |
| `execution_lease_ref` | lease identity |
| `job_ref` | required binding |
| `case_ref` | required binding |
| runtime holder | continuity holder |
| client ref | provenance only |
| operator context | admission/selection context only |
| session | no ownership |
| license_lease | authorization posture only |
| machine_authorization_ref | authorization posture only |
| runtime_gate_decision | admission evidence only |

## Lifecycle Model

| State | Meaning |
| ----- | ------- |
| `proposed` | lease requested but not active |
| `active` | lease currently governs continuity |
| `stale` | heartbeat or freshness is old |
| `renewing` | renewal is in progress |
| `paused` | execution continuity paused |
| `revoked` | lease revoked by policy |
| `expired` | lease expired |
| `released` | lease released cleanly |
| `completed` | associated work completed |
| `failed` | associated work failed |

## Execution Lease vs License Lease

```text
execution_lease governs work continuity.
license_lease governs account/machine/runtime authorization.
```

## Detach Boundary

```text
client detach does not automatically cancel job, release execution lease, revoke
auth_context, revoke license_lease or stop runtime.
```

## V23 Residual

```text
V23 VS Code docs present: no
Residual remains from V24/V25 baseline and is not fixed in V26.
```

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/execution/execution-lease-model.md` | pass | new execution doc |
| api | `test -f docs/waves/v26-execution-lease-model.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/execution-lease-model.md` | pass | new runtime/core doc |
| yai | `make info` | pass | yai touched |
| yai | `make yai` | pass | `Nothing to be done for 'yai'` |
| yai | `git diff --check` | pass | yai touched |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| cli | `cargo fmt --check` | not run | cli not touched |
| cli | `cargo test` | not run | cli not touched |
| sdk | validation | not run | docs-only unless touched |
| loom | validation | not run | docs-only unless touched |

## Findings

### Finding A — Execution Lease Is Continuity

Record:
Execution leases govern continuity of case-bound jobs.

### Finding B — Execution Lease Is Not Authorization

Record:
License lease, machine authorization and runtime gate decision are authorization
posture/evidence, not execution lease ownership.

### Finding C — Clients Are Provenance Only

Record:
Clients may create or observe leased jobs, but do not own execution leases.

### Finding D — Detach Needs Dedicated Semantics

Record:
V27 defines detach/continuation behavior using the execution lease model.

## V26 Completion Checklist

* [x] `docs/execution/execution-lease-model.md` exists
* [x] `docs/waves/v26-execution-lease-model.md` exists
* [x] `yai/Documentation/execution/execution-lease-model.md` exists
* [x] execution_lease_ref vocabulary documented
* [x] execution_lease.job_ref invariant documented
* [x] execution_lease.case_ref invariant documented
* [x] execution lease lifecycle documented
* [x] execution lease vs license lease distinction documented
* [x] client detach boundary documented
* [x] client/session ownership boundary documented
* [x] runtime/license/machine/gate posture boundary documented
* [x] V23 residual recorded truthfully
* [x] no lease manager added
* [x] no job runner added
* [x] no API endpoint added
* [x] no SDK lease client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
