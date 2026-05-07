# V43 — License Lease Consumption

## Status

* Delivery: V43
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: license lease consumption docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V42 — Machine Authorization Consumption
* Next delivery: V44 — Local Lease Cache / Reboot Continuity

## Purpose

V43 defines how runtime consumes safe license lease posture without issuing,
validating or persisting leases.

## Scope

Record:

* license lease consumption vocabulary documented;
* lease statuses documented;
* consumption statuses documented;
* grace/stale/refresh/revocation posture documented;
* diagnostic/sealed posture documented;
* safe lease projection documented;
* distinction from auth/machine/billing/session documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created or deviation recorded;
* no lease issuance/signing/validation implemented;
* no cache/persistence implemented;
* no runtime enforcement implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/execution/license-lease-consumption.md` | create | license lease consumption |
| api | `docs/waves/v43-license-lease-consumption.md` | create | delivery report |
| api | `schemas/license-lease-consumption.v1.schema.json` | create | license lease consumption schema |
| api | `fixtures/license-lease-consumption/valid-lease-consumed.json` | create | representative license lease fixture |
| api | `fixtures/license-lease-consumption/expired-lease-blocked.json` | create | blocked lease fixture |
| api | `fixtures/license-lease-consumption/revoked-lease-blocked.json` | create | blocked lease fixture |
| api | `fixtures/license-lease-consumption/stale-lease-grace.json` | create | grace/stale lease fixture |
| api | `fixtures/license-lease-consumption/missing-machine-authorization.json` | create | separate machine authorization relation fixture |
| api | `fixtures/license-lease-consumption/safe-lease-projection.json` | create | safe lease projection fixture |
| api | `conformance/check_license_lease_consumption.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/license-lease-consumption.md` | create | runtime/core license lease record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| license lease consumption doc | created | API execution contract added |
| JSON schema | created | dependency-free JSON schema artifact added |
| fixtures | created | six representative license lease fixtures added |
| conformance script | created | dependency-free fixture/schema checks added |
| yai runtime/core doc | created | runtime/core boundary recorded |

## License Lease Consumption Model

| Concern | V43 policy |
| ------- | ---------- |
| `license_lease_ref` | required safe ref |
| lease status | required |
| consumption status | required |
| scope | required |
| grace/stale/refresh posture | safe posture only |
| `machine_authorization_ref` | optional relation |
| `entitlement_ref` | optional relation |
| diagnostics | may remain available |
| sealed posture | reflects blocked operational posture |
| billing/subscription | forbidden |
| session | no ownership |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `valid-lease-consumed.json` | valid lease consumed | required refs present |
| `expired-lease-blocked.json` | expired lease | blocked reason present |
| `revoked-lease-blocked.json` | revoked lease | sealed posture |
| `stale-lease-grace.json` | stale lease in grace | grace posture |
| `missing-machine-authorization.json` | lease requires machine auth | machine auth relation distinct |
| `safe-lease-projection.json` | safe lease projection | only safe fields |

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/execution/license-lease-consumption.md` | pass | new policy doc |
| api | `test -f docs/waves/v43-license-lease-consumption.md` | pass | new report |
| api | `test -f schemas/license-lease-consumption.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_license_lease_consumption.py` | pass | conformance |
| api | `python3 conformance/check_license_lease_consumption.py` | pass | V43 conformance |
| api | `python3 conformance/check_machine_authorization_consumption.py` | pass | V42 regression |
| api | `python3 conformance/check_machine_enrollment_client_flow.py` | pass | V41 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | existing conformance |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/license-lease-consumption -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/license-lease-consumption.md` | pass | new runtime/core doc |
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
Runtime consumes safe license lease posture; E/platform owns lease policy and lifecycle.

### Finding B — Lease Is Distinct From Auth / Machine / Billing

Record:
License lease is distinct from auth_context, machine authorization, entitlement,
billing/subscription and session.

### Finding C — Valid Lease Is Not Unlimited Runtime Access

Record:
Valid license lease does not imply every runtime action is allowed.

### Finding D — Safe Projection Only

Record:
V/core consumes safe lease projection fields, not billing/subscription/private E
internals.

### Finding E — V44 Can Define Cache Continuity

Record:
V44 can now define local lease cache and reboot continuity without changing
lease issuance semantics.

## V43 Completion Checklist

* [x] `docs/execution/license-lease-consumption.md` exists
* [x] `docs/waves/v43-license-lease-consumption.md` exists
* [x] `schemas/license-lease-consumption.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists or deviation recorded
* [x] `yai/Documentation/execution/license-lease-consumption.md` exists
* [x] license lease consumption vocabulary documented
* [x] lease statuses documented
* [x] consumption statuses documented
* [x] grace/stale/refresh/revocation posture documented
* [x] diagnostic/sealed posture documented
* [x] safe lease projection documented
* [x] distinction from auth/machine/billing/session documented
* [x] E/V boundary documented
* [x] no lease issuance/signing/validation implemented
* [x] no cache/persistence implemented
* [x] no runtime enforcement implemented
* [x] no API endpoint added
* [x] no SDK license lease client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
