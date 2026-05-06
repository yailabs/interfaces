# V25 — Case-bound Jobs

## Status

* Delivery: V25
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: case-bound job model documentation + optional existing docs/status wording alignment
* Previous delivery: V24 — Desktop / Long-Lived Client Alignment
* Next delivery: V26 — Execution Lease Model

## Purpose

V25 defines jobs as case-bound execution records.

## Scope

Record:

* job.case_ref invariant documented;
* job lifecycle vocabulary documented;
* job admission requirements documented;
* client/session ownership boundary documented;
* future license/machine/gate posture documented;
* no job runner implemented;
* no API/SDK/CLI behavior added;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/execution/case-bound-jobs.md` | create | case-bound job model |
| api | `docs/waves/v25-case-bound-jobs.md` | create | delivery report |
| yai | `Documentation/execution/case-bound-jobs.md` | create | runtime/core job ownership record |

## Job Ownership Model

| Concern | Owner / role |
| ------- | ------------ |
| `job_ref` | job identity |
| `case_ref` | required owner |
| client ref | provenance only |
| operator context | admission/selection context |
| session | no ownership |
| runtime process | execution substrate, not owner |
| provider call | step/action, not owner |
| license lease | authorization posture |
| machine authorization | authorization posture |
| runtime gate decision | admission evidence |

## Lifecycle Model

| State | Meaning |
| ----- | ------- |
| `created` | job record exists but is not admitted |
| `admitted` | posture allows scheduling |
| `blocked` | posture or limit blocks execution |
| `queued` | accepted but not running |
| `running` | actively executing |
| `paused` | execution paused |
| `completed` | completed successfully |
| `failed` | failed |
| `cancelled` | cancelled by policy/operator |
| `expired` | no longer valid to continue |

## Admission Requirements

| Requirement | Status |
| ----------- | ------ |
| auth_context | required when account-linked |
| case_ref | required |
| operator context or explicit case_ref | required |
| runtime_gate_decision | required when gates exist |
| machine_authorization_ref | required when machine gate exists |
| license_lease | required when license gate exists |
| account-scoped limit projection | required when limit gates exist |

## V23 Residual

```text
V23 VS Code docs present: no
Residual remains from V24 baseline and is not fixed in V25.
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
| api | `test -f docs/execution/case-bound-jobs.md` | pass | new execution doc |
| api | `test -f docs/waves/v25-case-bound-jobs.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/case-bound-jobs.md` | pass | new runtime/core doc |
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

### Finding A — Jobs Are Case-bound

Record:
`job.case_ref` is the canonical ownership invariant.

### Finding B — Clients Are Provenance Only

Record:
CLI, Loom, VS Code and Desktop may create/observe jobs, but do not own them.

### Finding C — Session Does Not Own Jobs

Record:
Session remains non-canonical and cannot own work.

### Finding D — Gate/License/Machine Refs Are Admission Posture

Record:
Future license/machine/entitlement refs are admission or authorization posture,
not job ownership.

### Finding E — V26 Can Define Execution Lease

Record:
With ownership fixed, V26 can define how execution may outlive client
attachment.

## V25 Completion Checklist

* [x] `docs/execution/case-bound-jobs.md` exists
* [x] `docs/waves/v25-case-bound-jobs.md` exists
* [x] `yai/Documentation/execution/case-bound-jobs.md` exists
* [x] job.case_ref invariant documented
* [x] job lifecycle documented
* [x] admission requirements documented
* [x] client/session ownership boundary documented
* [x] runtime/license/machine/gate posture boundary documented
* [x] V23 residual recorded truthfully
* [x] no job runner added
* [x] no API endpoint added
* [x] no SDK job client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
