# V49 — Offline Grace / Stale Lease Behavior

## Status

* Delivery: V49
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: offline grace / stale lease behavior docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V48 — Runtime Sealed-by-License Behavior
* Next delivery: V50 — Logout / Revocation / Lease Invalidation

## Purpose

V49 defines bounded offline grace and stale lease behavior without implementing
offline mode or runtime enforcement.

## Scope

Record:

* grace/stale/offline vocabulary documented;
* operational/diagnostic/surface posture documented;
* refresh/recovery/next-action posture documented;
* safe grace projection documented;
* offline grace is not permanent offline authorization documented;
* stale lease is not valid lease documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created or deviation recorded;
* no offline mode/connectivity probing implemented;
* no grace timer/refresh/cache update implemented;
* no runtime enforcement implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/execution/offline-grace-stale-lease-behavior.md` | create | offline grace and stale lease boundary |
| api | `Documentation/waves/v49-offline-grace-stale-lease-behavior.md` | create | delivery report |
| api | `schemas/offline-grace-stale-lease-behavior.v1.schema.json` | create | offline grace and stale lease schema |
| api | `fixtures/offline-grace-stale-lease-behavior/grace-active-limited-operational.json` | create | bounded grace fixture |
| api | `fixtures/offline-grace-stale-lease-behavior/grace-expired-sealed.json` | create | expired grace fixture |
| api | `fixtures/offline-grace-stale-lease-behavior/stale-lease-diagnostics-only.json` | create | stale diagnostics-only fixture |
| api | `fixtures/offline-grace-stale-lease-behavior/offline-refresh-required.json` | create | offline refresh-required fixture |
| api | `fixtures/offline-grace-stale-lease-behavior/online-refresh-recovers.json` | create | online recovery fixture |
| api | `fixtures/offline-grace-stale-lease-behavior/safe-grace-projection.json` | create | safe projection fixture |
| api | `conformance/check_offline_grace_stale_lease_behavior.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/offline-grace-stale-lease-behavior.md` | create | runtime/core boundary record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| offline grace / stale lease doc | created | API execution contract added |
| JSON schema | created | dependency-free JSON schema artifact added |
| fixtures | created | six representative grace/stale fixtures added |
| conformance script | created | dependency-free fixture/schema checks added |
| yai runtime/core doc | created | runtime/core boundary recorded |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `grace-active-limited-operational.json` | grace active | bounded/limited posture |
| `grace-expired-sealed.json` | grace expired | sealed/blocked posture |
| `stale-lease-diagnostics-only.json` | stale lease | diagnostics only |
| `offline-refresh-required.json` | offline but refresh required | refresh posture |
| `online-refresh-recovers.json` | online recovery posture | next action refresh |
| `safe-grace-projection.json` | safe projection | only safe fields |

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/execution/offline-grace-stale-lease-behavior.md` | pass | new policy doc |
| api | `test -f Documentation/waves/v49-offline-grace-stale-lease-behavior.md` | pass | new report |
| api | `test -f schemas/offline-grace-stale-lease-behavior.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_offline_grace_stale_lease_behavior.py` | pass | conformance |
| api | `python3 conformance/check_offline_grace_stale_lease_behavior.py` | pass | V49 conformance |
| api | `python3 conformance/check_runtime_sealed_by_license_behavior.py` | pass | V48 regression |
| api | `python3 conformance/check_runtime_license_check_response.py` | pass | V47 regression |
| api | `python3 conformance/check_runtime_license_check_request.py` | pass | V46 regression |
| api | `python3 conformance/check_local_lease_cache_reboot_continuity.py` | pass | V44 regression |
| api | `python3 conformance/check_license_lease_consumption.py` | pass | V43 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | existing conformance |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/offline-grace-stale-lease-behavior -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/offline-grace-stale-lease-behavior.md` | pass | new runtime/core doc |
| yai | `make info` | pass | yai touched |
| yai | `make yai` | pass | yai touched |
| yai | `git diff --check` | pass | yai touched |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| cli | `cargo fmt --check` | not run | cli not touched |
| cli | `cargo test` | not run | cli not touched |
| sdk | validation | not run | docs-only unless touched |
| loom | validation | not run | docs-only unless touched |

## V49 Completion Checklist

* [x] `Documentation/execution/offline-grace-stale-lease-behavior.md` exists
* [x] `Documentation/waves/v49-offline-grace-stale-lease-behavior.md` exists
* [x] `schemas/offline-grace-stale-lease-behavior.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists or deviation recorded
* [x] `yai/Documentation/execution/offline-grace-stale-lease-behavior.md` exists
* [x] grace/stale/offline vocabulary documented
* [x] operational/diagnostic/surface posture documented
* [x] refresh/recovery posture documented
* [x] offline grace is not permanent offline authorization documented
* [x] stale lease is not valid lease documented
* [x] no offline mode/connectivity probing implemented
* [x] no grace timer/refresh/cache update implemented
* [x] no runtime enforcement added
* [x] no API endpoint added
* [x] no SDK/CLI behavior added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
