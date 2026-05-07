# V46 — Runtime License Check Request

## Status

* Delivery: V46
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: runtime license check request docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V45 — Account-Scoped Limit Reconciliation
* Next delivery: V47 — Runtime License Check Response

## Purpose

V46 defines the safe request payload runtime may send to E/platform for a
license check.

## Scope

Record:

* request vocabulary documented;
* check scopes documented;
* request contexts documented;
* freshness/connectivity/privacy posture documented;
* safe request rules documented;
* request/response split documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created or deviation recorded;
* no endpoint/transport/polling/response implementation;
* no lease validation/refresh implementation;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/execution/runtime-license-check-request.md` | create | runtime license check request boundary |
| api | `docs/waves/v46-runtime-license-check-request.md` | create | delivery report |
| api | `schemas/runtime-license-check-request.v1.schema.json` | create | request schema |
| api | `fixtures/runtime-license-check-request/full-online-check-request.json` | create | full online request fixture |
| api | `fixtures/runtime-license-check-request/missing-machine-authorization-request.json` | create | missing machine authorization fixture |
| api | `fixtures/runtime-license-check-request/cached-lease-refresh-request.json` | create | cached lease request fixture |
| api | `fixtures/runtime-license-check-request/offline-stale-posture-request.json` | create | offline stale posture fixture |
| api | `fixtures/runtime-license-check-request/account-limit-reconciliation-request.json` | create | limit reconciliation request fixture |
| api | `fixtures/runtime-license-check-request/safe-request-projection.json` | create | safe request fixture |
| api | `conformance/check_runtime_license_check_request.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/runtime-license-check-request.md` | create | runtime/core request boundary record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| runtime license check request doc | created | API execution contract added |
| JSON schema | created | dependency-free JSON schema artifact added |
| fixtures | created | six representative request fixtures added |
| conformance script | created | dependency-free fixture/schema checks added |
| yai runtime/core doc | created | runtime/core boundary recorded |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `full-online-check-request.json` | full online request | safe refs only |
| `missing-machine-authorization-request.json` | missing machine auth | request posture only |
| `cached-lease-refresh-request.json` | cached lease refresh request | no refresh implementation |
| `offline-stale-posture-request.json` | offline/stale posture | request, not response |
| `account-limit-reconciliation-request.json` | includes limit reconciliation ref | no quota ledger |
| `safe-request-projection.json` | safe projection | no private fields |

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/execution/runtime-license-check-request.md` | pass | new policy doc |
| api | `test -f docs/waves/v46-runtime-license-check-request.md` | pass | new report |
| api | `test -f schemas/runtime-license-check-request.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_runtime_license_check_request.py` | pass | conformance |
| api | `python3 conformance/check_runtime_license_check_request.py` | pass | V46 conformance |
| api | `python3 conformance/check_account_scoped_limit_reconciliation.py` | pass | V45 regression |
| api | `python3 conformance/check_local_lease_cache_reboot_continuity.py` | pass | V44 regression |
| api | `python3 conformance/check_license_lease_consumption.py` | pass | V43 regression |
| api | `python3 conformance/check_machine_authorization_consumption.py` | pass | V42 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | existing conformance |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/runtime-license-check-request -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/runtime-license-check-request.md` | pass | new runtime/core doc |
| yai | `make info` | pass | yai touched |
| yai | `make yai` | pass | yai touched |
| yai | `git diff --check` | pass | yai touched |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| cli | `cargo fmt --check` | not run | cli not touched |
| cli | `cargo test` | not run | cli not touched |
| sdk | validation | not run | docs-only unless touched |
| loom | validation | not run | docs-only unless touched |

## V46 Completion Checklist

* [x] `docs/execution/runtime-license-check-request.md` exists
* [x] `docs/waves/v46-runtime-license-check-request.md` exists
* [x] `schemas/runtime-license-check-request.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists or deviation recorded
* [x] `yai/Documentation/execution/runtime-license-check-request.md` exists
* [x] request/check/freshness/connectivity/privacy vocabulary documented
* [x] request/response split documented
* [x] safe request rules documented
* [x] no endpoint/transport/polling implemented
* [x] no response handling implemented
* [x] no lease validation/refresh implemented
* [x] no API endpoint added
* [x] no SDK/CLI behavior added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
