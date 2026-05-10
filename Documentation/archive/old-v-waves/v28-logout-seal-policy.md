# V28 — Logout / Seal Policy

## Status

* Delivery: V28
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: logout/seal policy docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V27 — Detach / Continuation Semantics
* Next delivery: V29 — Case Evidence Binding

## Purpose

V28 defines logout/seal policy and creates a verifiable contract artifact.

## Scope

Record:

* logout request vocabulary documented;
* logout policy decision vocabulary documented;
* decision statuses documented;
* safe reasons documented;
* auth/license/runtime/records/knowledge actions documented;
* JSON schema created;
* fixtures created;
* conformance script created;
* no logout behavior implemented;
* no lease invalidation implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/execution/logout-seal-policy.md` | create | logout/seal policy |
| api | `Documentation/waves/v28-logout-seal-policy.md` | create | delivery report |
| api | `schemas/logout-seal-policy.v1.schema.json` | create | policy contract schema |
| api | `fixtures/logout-seal-policy/*.json` | create | representative policy fixtures |
| api | `conformance/check_logout_seal_policy.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/logout-seal-policy.md` | create | runtime/core policy record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| logout/seal policy doc | created | API-side canonical policy prose |
| JSON schema | created | dependency-free JSON contract for request + decision |
| fixtures | created | five representative logout scenarios |
| conformance script | created | validates JSON parsing, required keys, and enum values |
| yai runtime/core doc | created | runtime/core companion policy record |

## Policy Model

| Concern | V28 policy |
| ------- | ---------- |
| detach vs logout | detach is connection; logout is auth/control posture |
| active case | preserved unless future explicit policy changes it |
| active job | not cancelled by default |
| execution lease | not released by default |
| auth_context | may be cleared, retained, refreshed, or revoked later depending decision |
| license_lease | not automatically invalidated by logout |
| runtime | operational actions may seal |
| records/evidence/knowledge | preserved |

## Fixture Summary

| Fixture | Scenario | Expected decision |
| ------- | -------- | ----------------- |
| `no-active-work.json` | no active work | `allowed` |
| `active-case-no-job.json` | active case, no job | `requires_confirmation` |
| `active-job-with-lease.json` | active job + execution lease | `requires_wait` |
| `expired-license-lease.json` | expired license lease | `blocked` |
| `force-request-requires-confirmation.json` | force mode | `requires_confirmation` |

## V23 Residual

```text
V23 VS Code docs present: no
If no, residual remains from V24-V27 baseline and is not fixed in V28.
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
| api | `test -f Documentation/execution/logout-seal-policy.md` | pass | new policy doc |
| api | `test -f Documentation/waves/v28-logout-seal-policy.md` | pass | new report |
| api | `test -f schemas/logout-seal-policy.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_logout_seal_policy.py` | pass | conformance |
| api | `python3 conformance/check_logout_seal_policy.py` | pass | `logout-seal-policy: ok` |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/logout-seal-policy -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/logout-seal-policy.md` | pass | new runtime/core doc |
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

### Finding A — Logout Is Auth/Control Posture

Record:
Logout changes auth/control posture; it is not detach and not runtime stop.

### Finding B — Work Is Not Destroyed By Default

Record:
Jobs, execution leases, records, evidence and knowledge are not destroyed by
logout by default.

### Finding C — Schema/Fixtures Exist

Record:
V28 created a verifiable contract artifact, not only prose.

### Finding D — License Lease Remains Distinct

Record:
Logout may affect auth_context; license_lease is governed by explicit policy and
future V43/V50 behavior.

### Finding E — V29 Can Bind Evidence

Record:
With logout not deleting evidence, V29 can define evidence binding under cases.

## V28 Completion Checklist

* [x] `Documentation/execution/logout-seal-policy.md` exists
* [x] `Documentation/waves/v28-logout-seal-policy.md` exists
* [x] `schemas/logout-seal-policy.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists
* [x] `yai/Documentation/execution/logout-seal-policy.md` exists
* [x] logout_request vocabulary documented
* [x] logout_policy_decision vocabulary documented
* [x] decision statuses documented
* [x] safe reasons documented
* [x] auth_context actions documented
* [x] license_lease actions documented
* [x] runtime seal actions documented
* [x] records/evidence/knowledge actions documented
* [x] no logout implementation added
* [x] no lease invalidation implementation added
* [x] no job cancellation implementation added
* [x] no runtime seal implementation added
* [x] no API endpoint added
* [x] no SDK client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
