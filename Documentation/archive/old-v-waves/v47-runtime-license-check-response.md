# V47 — Runtime License Check Response

## Status

* Delivery: V47
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: runtime license check response docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V46 — Runtime License Check Request
* Next delivery: V48 — Runtime Sealed-by-License Behavior

## Purpose

V47 defines the safe response E/platform may return to runtime after a license
check request.

## Scope

Record:

* response vocabulary documented;
* decision statuses documented;
* blocked reasons documented;
* next actions documented;
* lease/machine/entitlement/limit/gate posture documented;
* safe response rules documented;
* response/enforcement split documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created or deviation recorded;
* no response transport/handling implemented;
* no enforcement/cache update implemented;
* no lease validation/entitlement evaluation implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/execution/runtime-license-check-response.md` | create | runtime license check response boundary |
| api | `Documentation/waves/v47-runtime-license-check-response.md` | create | delivery report |
| api | `schemas/runtime-license-check-response.v1.schema.json` | create | response schema |
| api | `fixtures/runtime-license-check-response/allowed-response.json` | create | allowed response fixture |
| api | `fixtures/runtime-license-check-response/blocked-missing-machine-authorization.json` | create | missing machine authorization fixture |
| api | `fixtures/runtime-license-check-response/blocked-expired-lease.json` | create | expired lease fixture |
| api | `fixtures/runtime-license-check-response/blocked-limit-exceeded.json` | create | limit exceeded fixture |
| api | `fixtures/runtime-license-check-response/grace-response.json` | create | grace response fixture |
| api | `fixtures/runtime-license-check-response/safe-response-projection.json` | create | safe response fixture |
| api | `conformance/check_runtime_license_check_response.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/runtime-license-check-response.md` | create | runtime/core response boundary record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| runtime license check response doc | created | API execution contract added |
| JSON schema | created | dependency-free JSON schema artifact added |
| fixtures | created | six representative response fixtures added |
| conformance script | created | dependency-free fixture/schema checks added |
| yai runtime/core doc | created | runtime/core boundary recorded |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `allowed-response.json` | allowed response | no blocked reason |
| `blocked-missing-machine-authorization.json` | missing machine auth | blocked reason present |
| `blocked-expired-lease.json` | expired lease | blocked reason present |
| `blocked-limit-exceeded.json` | limit exceeded | limit posture blocked |
| `grace-response.json` | grace response | grace posture present |
| `safe-response-projection.json` | safe projection | only safe fields |

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/execution/runtime-license-check-response.md` | pass | new policy doc |
| api | `test -f Documentation/waves/v47-runtime-license-check-response.md` | pass | new report |
| api | `test -f schemas/runtime-license-check-response.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_runtime_license_check_response.py` | pass | conformance |
| api | `python3 conformance/check_runtime_license_check_response.py` | pass | V47 conformance |
| api | `python3 conformance/check_runtime_license_check_request.py` | pass | V46 regression |
| api | `python3 conformance/check_account_scoped_limit_reconciliation.py` | pass | V45 regression |
| api | `python3 conformance/check_local_lease_cache_reboot_continuity.py` | pass | V44 regression |
| api | `python3 conformance/check_license_lease_consumption.py` | pass | V43 regression |
| api | `python3 conformance/check_machine_authorization_consumption.py` | pass | V42 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | existing conformance |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/runtime-license-check-response -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/runtime-license-check-response.md` | pass | new runtime/core doc |
| yai | `make info` | pass | yai touched |
| yai | `make yai` | pass | yai touched |
| yai | `git diff --check` | pass | yai touched |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| cli | `cargo fmt --check` | not run | cli not touched |
| cli | `cargo test` | not run | cli not touched |
| sdk | validation | not run | docs-only unless touched |
| loom | validation | not run | docs-only unless touched |

## V47 Completion Checklist

* [x] `Documentation/execution/runtime-license-check-response.md` exists
* [x] `Documentation/waves/v47-runtime-license-check-response.md` exists
* [x] `schemas/runtime-license-check-response.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists or deviation recorded
* [x] `yai/Documentation/execution/runtime-license-check-response.md` exists
* [x] response decision/posture vocabulary documented
* [x] response/enforcement split documented
* [x] safe response rules documented
* [x] no response transport/handling implemented
* [x] no runtime enforcement implemented
* [x] no cache update implemented
* [x] no lease validation/entitlement evaluation implemented
* [x] no API endpoint added
* [x] no SDK/CLI behavior added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
