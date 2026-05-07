# V42 — Machine Authorization Consumption

## Status

* Delivery: V42
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: machine authorization consumption docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V41 — Machine Enrollment Client Flow
* Next delivery: V43 — License Lease Consumption

## Purpose

V42 defines how runtime consumes safe machine authorization posture without
issuing authorization.

## Scope

Record:

* machine authorization consumption vocabulary documented;
* authorization statuses documented;
* consumption statuses documented;
* diagnostic/sealed posture documented;
* safe status projection documented;
* privacy rules documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created or deviation recorded;
* no authorization issuance implemented;
* no license lease implementation;
* no runtime enforcement implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/execution/machine-authorization-consumption.md` | create | machine authorization consumption |
| api | `docs/waves/v42-machine-authorization-consumption.md` | create | delivery report |
| api | `schemas/machine-authorization-consumption.v1.schema.json` | create | machine authorization consumption schema |
| api | `fixtures/machine-authorization-consumption/authorized-machine-consumed.json` | create | representative authorization fixture |
| api | `fixtures/machine-authorization-consumption/revoked-machine-blocked.json` | create | blocked authorization fixture |
| api | `fixtures/machine-authorization-consumption/expired-machine-blocked.json` | create | blocked authorization fixture |
| api | `fixtures/machine-authorization-consumption/pending-machine-diagnostics-only.json` | create | diagnostics-only fixture |
| api | `fixtures/machine-authorization-consumption/missing-license-lease-required.json` | create | separate lease fixture |
| api | `fixtures/machine-authorization-consumption/safe-status-projection.json` | create | safe projection fixture |
| api | `conformance/check_machine_authorization_consumption.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/machine-authorization-consumption.md` | create | runtime/core authorization consumption record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| machine authorization consumption doc | created | API execution contract added |
| JSON schema | created | dependency-free JSON schema artifact added |
| fixtures | created | six representative machine authorization fixtures added |
| conformance script | created | dependency-free fixture/schema checks added |
| yai runtime/core doc | created | runtime/core boundary recorded |

## Machine Authorization Consumption Model

| Concern | V42 policy |
| ------- | ---------- |
| `machine_authorization_ref` | required safe ref |
| `local_machine_ref` | required local relation |
| authorization status | required |
| consumption status | required |
| diagnostics | may remain available |
| sealed posture | reflects blocked operational posture |
| license lease | separate future relation |
| E record internals | forbidden |
| raw hardware | forbidden |
| session | no ownership |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `authorized-machine-consumed.json` | authorized machine posture | required refs present |
| `revoked-machine-blocked.json` | revoked machine | blocked reason present |
| `expired-machine-blocked.json` | expired authorization | sealed posture |
| `pending-machine-diagnostics-only.json` | pending auth | diagnostics-only |
| `missing-license-lease-required.json` | auth present, lease required | lease posture distinct |
| `safe-status-projection.json` | safe projection | only safe fields |

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/execution/machine-authorization-consumption.md` | pass | new policy doc |
| api | `test -f docs/waves/v42-machine-authorization-consumption.md` | pass | new report |
| api | `test -f schemas/machine-authorization-consumption.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_machine_authorization_consumption.py` | pass | conformance |
| api | `python3 conformance/check_machine_authorization_consumption.py` | pass | V42 conformance |
| api | `python3 conformance/check_machine_enrollment_client_flow.py` | pass | V41 regression |
| api | `python3 conformance/check_machine_fingerprint_evidence_builder.py` | pass | V40 regression |
| api | `python3 conformance/check_local_machine_identity_store.py` | pass | V39 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | existing conformance |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/machine-authorization-consumption -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/machine-authorization-consumption.md` | pass | new runtime/core doc |
| yai | `make info` | pass | yai touched |
| yai | `make yai` | pass | yai touched |
| yai | `git diff --check` | pass | yai touched |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| cli | `cargo fmt --check` | not run | cli not touched |
| cli | `cargo test` | not run | cli not touched |
| sdk | validation | not run | docs-only unless touched |
| loom | validation | not run | docs-only unless touched |

## Findings

### Finding A — Runtime Consumes, Does Not Issue

Record:
Runtime consumes safe machine authorization posture; E/platform issues and owns
machine_authorization_ref.

### Finding B — Authorization Is Not License Lease

Record:
Authorized machine posture is distinct from license lease posture.

### Finding C — Diagnostics May Remain Available

Record:
Diagnostics may remain available when machine authorization blocks operational
actions.

### Finding D — Safe Projection Only

Record:
V/core consumes safe projection fields, not E internals, raw hardware, provider
identity or billing objects.

### Finding E — V43 Can Define Lease Consumption

Record:
V43 can now define license lease consumption separately from machine
authorization.

## V42 Completion Checklist

* [x] `docs/execution/machine-authorization-consumption.md` exists
* [x] `docs/waves/v42-machine-authorization-consumption.md` exists
* [x] `schemas/machine-authorization-consumption.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists or deviation recorded
* [x] `yai/Documentation/execution/machine-authorization-consumption.md` exists
* [x] machine authorization consumption vocabulary documented
* [x] authorization statuses documented
* [x] consumption statuses documented
* [x] diagnostic/sealed posture documented
* [x] safe status projection documented
* [x] privacy rules documented
* [x] E/V boundary documented
* [x] no authorization issuance implemented
* [x] no license lease implementation added
* [x] no runtime enforcement implemented
* [x] no API endpoint added
* [x] no SDK machine authorization client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
