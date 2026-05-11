# V50 — Logout / Revocation / Lease Invalidation

## Status

* Delivery: V50
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: logout / revocation / lease invalidation docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V49 — Offline Grace / Stale Lease Behavior
* Next delivery: V51 — API Registry Refactor

## Purpose

V50 defines invalidation posture for logout, revocation and lease invalidation
without implementing destructive behavior or enforcement.

## Scope

Record:

* invalidation vocabulary documented;
* seal/diagnostic/operational posture documented;
* cache/lease/machine authorization invalidation posture documented;
* preservation posture documented;
* safe invalidation projection documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created or deviation recorded;
* no logout/revocation/cache deletion implemented;
* no runtime enforcement implemented;
* no case/evidence/knowledge deletion implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/execution/logout-revocation-lease-invalidation.md` | create | invalidation boundary |
| api | `Documentation/waves/v50-logout-revocation-lease-invalidation.md` | create | delivery report |
| api | `schemas/logout-revocation-lease-invalidation.v1.schema.json` | create | invalidation schema |
| api | `fixtures/logout-revocation-lease-invalidation/logout-seals-operational.json` | create | logout invalidation fixture |
| api | `fixtures/logout-revocation-lease-invalidation/machine-revoked-seals-runtime.json` | create | machine revocation fixture |
| api | `fixtures/logout-revocation-lease-invalidation/lease-revoked-invalidates-cache.json` | create | lease revocation/cache invalidation fixture |
| api | `fixtures/logout-revocation-lease-invalidation/lease-expired-diagnostics-only.json` | create | diagnostics-only expiry fixture |
| api | `fixtures/logout-revocation-lease-invalidation/case-evidence-knowledge-preserved.json` | create | preservation fixture |
| api | `fixtures/logout-revocation-lease-invalidation/safe-invalidation-projection.json` | create | safe projection fixture |
| api | `conformance/check_logout_revocation_lease_invalidation.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/logout-revocation-lease-invalidation.md` | create | runtime/core boundary record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| logout / revocation / lease invalidation doc | created | API execution contract added |
| JSON schema | created | dependency-free JSON schema artifact added |
| fixtures | created | six representative invalidation fixtures added |
| conformance script | created | dependency-free fixture/schema checks added |
| yai runtime/core doc | created | runtime/core boundary recorded |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `logout-seals-operational.json` | logout seals operation | does not stop runtime |
| `machine-revoked-seals-runtime.json` | machine revoked | operational blocked |
| `lease-revoked-invalidates-cache.json` | lease revoked | cache must not be used |
| `lease-expired-diagnostics-only.json` | lease expired | diagnostics only |
| `case-evidence-knowledge-preserved.json` | preservation | cases/evidence/knowledge preserved |
| `safe-invalidation-projection.json` | safe projection | only safe fields |

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/execution/logout-revocation-lease-invalidation.md` | pass | new policy doc |
| api | `test -f Documentation/waves/v50-logout-revocation-lease-invalidation.md` | pass | new report |
| api | `test -f schemas/logout-revocation-lease-invalidation.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_logout_revocation_lease_invalidation.py` | pass | conformance |
| api | `python3 conformance/check_logout_revocation_lease_invalidation.py` | pass | V50 conformance |
| api | `python3 conformance/check_offline_grace_stale_lease_behavior.py` | pass | V49 regression |
| api | `python3 conformance/check_runtime_sealed_by_license_behavior.py` | pass | V48 regression |
| api | `python3 conformance/check_runtime_license_check_response.py` | pass | V47 regression |
| api | `python3 conformance/check_local_lease_cache_reboot_continuity.py` | pass | V44 regression |
| api | `python3 conformance/check_license_lease_consumption.py` | pass | V43 regression |
| api | `python3 conformance/check_machine_authorization_consumption.py` | pass | V42 regression |
| api | `python3 conformance/check_logout_seal_policy.py` | pass | V28 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | existing conformance |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/logout-revocation-lease-invalidation -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/logout-revocation-lease-invalidation.md` | pass | new runtime/core doc |
| yai | `make info` | pass | yai touched |
| yai | `make yai` | pass | yai touched |
| yai | `git diff --check` | pass | yai touched |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| cli | `cargo fmt --check` | not run | cli not touched |
| cli | `cargo test` | not run | cli not touched |
| sdk | validation | not run | docs-only unless touched |
| loom | validation | not run | docs-only unless touched |

## V50 Completion Checklist

* [x] `Documentation/execution/logout-revocation-lease-invalidation.md` exists
* [x] `Documentation/waves/v50-logout-revocation-lease-invalidation.md` exists
* [x] `schemas/logout-revocation-lease-invalidation.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists or deviation recorded
* [x] `yai/Documentation/execution/logout-revocation-lease-invalidation.md` exists
* [x] invalidation vocabulary documented
* [x] preservation posture documented
* [x] safe invalidation projection documented
* [x] no logout/revocation/cache deletion implemented
* [x] no runtime enforcement implemented
* [x] no case/evidence/knowledge deletion implemented
* [x] no API endpoint added
* [x] no SDK/CLI behavior added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
