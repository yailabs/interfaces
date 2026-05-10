# V48 — Runtime Sealed-by-License Behavior

## Status

* Delivery: V48
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: runtime sealed-by-license behavior docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V47 — Runtime License Check Response
* Next delivery: V49 — Offline Grace / Stale Lease Behavior

## Purpose

V48 defines the runtime sealed-by-license behavior contract without implementing
runtime enforcement.

## Scope

Record:

* seal-state vocabulary documented;
* seal reasons documented;
* operational readiness documented;
* diagnostic/allowed/blocked surfaces documented;
* recovery/next actions documented;
* safe status projection documented;
* response/enforcement split documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created or deviation recorded;
* no runtime enforcement implemented;
* no operation-blocking behavior implemented;
* no response handling/cache update implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/execution/runtime-sealed-by-license-behavior.md` | create | sealed-by-license behavior boundary |
| api | `Documentation/waves/v48-runtime-sealed-by-license-behavior.md` | create | delivery report |
| api | `schemas/runtime-sealed-by-license-behavior.v1.schema.json` | create | sealed-by-license schema |
| api | `fixtures/runtime-sealed-by-license-behavior/unsealed-valid-license.json` | create | unsealed valid posture fixture |
| api | `fixtures/runtime-sealed-by-license-behavior/sealed-missing-machine-authorization.json` | create | missing machine authorization fixture |
| api | `fixtures/runtime-sealed-by-license-behavior/sealed-expired-license-lease.json` | create | expired lease fixture |
| api | `fixtures/runtime-sealed-by-license-behavior/sealed-limit-exceeded.json` | create | limit exceeded fixture |
| api | `fixtures/runtime-sealed-by-license-behavior/diagnostics-only-stale-response.json` | create | diagnostics-only stale fixture |
| api | `fixtures/runtime-sealed-by-license-behavior/safe-seal-status-projection.json` | create | safe projection fixture |
| api | `conformance/check_runtime_sealed_by_license_behavior.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/runtime-sealed-by-license-behavior.md` | create | runtime/core boundary record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| runtime sealed-by-license doc | created | API execution contract added |
| JSON schema | created | dependency-free JSON schema artifact added |
| fixtures | created | six representative seal-state fixtures added |
| conformance script | created | dependency-free fixture/schema checks added |
| yai runtime/core doc | created | runtime/core boundary recorded |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `unsealed-valid-license.json` | valid posture | `seal_state` unsealed |
| `sealed-missing-machine-authorization.json` | missing machine auth | operational blocked |
| `sealed-expired-license-lease.json` | expired lease | operational blocked |
| `sealed-limit-exceeded.json` | account limit exceeded | limit seal reason |
| `diagnostics-only-stale-response.json` | stale response | diagnostics only |
| `safe-seal-status-projection.json` | safe projection | only safe fields |

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/execution/runtime-sealed-by-license-behavior.md` | pass | new policy doc |
| api | `test -f Documentation/waves/v48-runtime-sealed-by-license-behavior.md` | pass | new report |
| api | `test -f schemas/runtime-sealed-by-license-behavior.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_runtime_sealed_by_license_behavior.py` | pass | conformance |
| api | `python3 conformance/check_runtime_sealed_by_license_behavior.py` | pass | V48 conformance |
| api | `python3 conformance/check_runtime_license_check_response.py` | pass | V47 regression |
| api | `python3 conformance/check_runtime_license_check_request.py` | pass | V46 regression |
| api | `python3 conformance/check_license_lease_consumption.py` | pass | V43 regression |
| api | `python3 conformance/check_machine_authorization_consumption.py` | pass | V42 regression |
| api | `python3 conformance/check_runtime_gate_registry.py` | pass | gate regression |
| api | `python3 conformance/check_api_contracts.py` | pass | existing conformance |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/runtime-sealed-by-license-behavior -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/runtime-sealed-by-license-behavior.md` | pass | new runtime/core doc |
| yai | `make info` | pass | yai touched |
| yai | `make yai` | pass | yai touched |
| yai | `git diff --check` | pass | yai touched |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| cli | `cargo fmt --check` | not run | cli not touched |
| cli | `cargo test` | not run | cli not touched |
| sdk | validation | not run | docs-only unless touched |
| loom | validation | not run | docs-only unless touched |

## V48 Completion Checklist

* [x] `Documentation/execution/runtime-sealed-by-license-behavior.md` exists
* [x] `Documentation/waves/v48-runtime-sealed-by-license-behavior.md` exists
* [x] `schemas/runtime-sealed-by-license-behavior.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists or deviation recorded
* [x] `yai/Documentation/execution/runtime-sealed-by-license-behavior.md` exists
* [x] seal-state vocabulary documented
* [x] operational readiness documented
* [x] diagnostic/allowed/blocked surfaces documented
* [x] response/enforcement split documented
* [x] no runtime enforcement implemented
* [x] no operation-blocking behavior added
* [x] no response handling/cache update implemented
* [x] no API endpoint added
* [x] no SDK/CLI behavior added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
