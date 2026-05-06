# V27 — Detach / Continuation Semantics

## Status

* Delivery: V27
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: detach/continuation semantics documentation + optional existing docs/status wording alignment
* Previous delivery: V26 — Execution Lease Model
* Next delivery: V28 — Logout / Seal Policy

## Purpose

V27 defines detach as a client/shell connection event, not domain lifecycle.

## Scope

Record:

* detach_event vocabulary documented;
* detach reasons documented;
* continuation outcomes documented;
* detach/job boundary documented;
* detach/execution lease boundary documented;
* detach/logout boundary documented;
* reconnect/resume boundary documented;
* no detach behavior implemented;
* no logout policy implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/execution/detach-continuation-semantics.md` | create | detach/continuation model |
| api | `docs/waves/v27-detach-continuation-semantics.md` | create | delivery report |
| yai | `Documentation/execution/detach-continuation-semantics.md` | create | runtime/core detach record |

## Detach Ownership Model

| Concern | Detach effect |
| ------- | ------------- |
| client connection | detached or disconnected |
| shell connection | detached or disconnected |
| auth_context | unchanged by detach |
| active_case_ref | unchanged by detach unless explicit case leave |
| case | unchanged |
| job | unchanged unless policy later says otherwise |
| execution lease | unchanged unless policy later says otherwise |
| license_lease | unchanged by detach |
| runtime lifecycle | unchanged by detach |
| records/evidence/knowledge | unchanged |
| session | no canonical ownership |

## Continuation Model

| Scenario | Expected V27 semantic |
| -------- | --------------------- |
| detach with no active work | client disconnect only |
| detach with active case | case remains; active_case_ref unchanged unless explicit leave |
| detach with leased job | job and lease may continue if policy allows |
| transport disconnect | observation lost; state must be re-read |
| reconnect | re-read posture; do not invent authorization |
| runtime sealed after detach | display blocked or sealed on next read |
| license lease expires after detach | V28, V43, and V50 policy later |

## Execution Lease Relationship

```text
Execution lease enables continuity of case-bound jobs.
Detach does not automatically release execution lease.
```

## Logout Boundary

```text
Detach is not logout.
V28 owns logout/seal policy.
```

## V23 Residual

```text
V23 VS Code docs present: no
Residual remains from V24-V26 baseline and is not fixed in V27.
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
| api | `test -f docs/execution/detach-continuation-semantics.md` | pass | new execution doc |
| api | `test -f docs/waves/v27-detach-continuation-semantics.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/detach-continuation-semantics.md` | pass | new runtime/core doc |
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

### Finding A — Detach Is Client/Connection Only

Record:
Detach affects client/shell observation and connection, not domain ownership.

### Finding B — Jobs And Leases May Continue

Record:
Case-bound jobs and execution leases may continue after detach if policy allows.

### Finding C — Detach Is Not Logout

Record:
Auth context and license lease are not revoked merely because a client detaches.

### Finding D — Reconnect Re-reads Posture

Record:
Reconnect/resume observes current posture and does not grant authorization.

### Finding E — V28 Can Define Logout / Seal Policy

Record:
With detach separated from logout, V28 can define logout with active work.

## V27 Completion Checklist

* [x] `docs/execution/detach-continuation-semantics.md` exists
* [x] `docs/waves/v27-detach-continuation-semantics.md` exists
* [x] `yai/Documentation/execution/detach-continuation-semantics.md` exists
* [x] detach_event vocabulary documented
* [x] detach reasons documented
* [x] continuation outcomes documented
* [x] detach/job boundary documented
* [x] detach/execution lease boundary documented
* [x] detach/logout boundary documented
* [x] reconnect/resume boundary documented
* [x] V23 residual recorded truthfully
* [x] no detach implementation added
* [x] no logout policy added
* [x] no lease manager added
* [x] no job runner added
* [x] no API endpoint added
* [x] no SDK client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
