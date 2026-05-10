# V31 — Provider Authority Binding

## Status

* Delivery: V31
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: provider authority docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V30 — Knowledge Binding
* Next delivery: V32 — Agent Authority Binding

## Purpose

V31 defines provider calls as governed, case-bound actions and creates a
verifiable contract artifact.

## Scope

Record:

* provider_call.case_ref invariant documented;
* provider requested actions documented;
* decision statuses documented;
* safe blocked reasons documented;
* provider output posture documented;
* E/V boundary documented;
* billing/metering boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created;
* no provider execution implemented;
* no model invocation implemented;
* no billing/metering implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/execution/provider-authority-binding.md` | create | provider authority binding |
| api | `Documentation/waves/v31-provider-authority-binding.md` | create | delivery report |
| api | `schemas/provider-authority-binding.v1.schema.json` | create | provider authority contract schema |
| api | `fixtures/provider-authority-binding/*.json` | create | representative provider authority fixtures |
| api | `conformance/check_provider_authority_binding.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/provider-authority-binding.md` | create | runtime/core provider authority record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| provider authority doc | created | API-side canonical provider authority contract |
| JSON schema | created | dependency-free JSON contract for governed provider calls |
| fixtures | created | five representative provider authority scenarios |
| conformance script | created | validates JSON parsing, required keys, enum values, and case/blocked posture rules |
| yai runtime/core doc | created | runtime/core companion provider authority record |

## Provider Authority Model

| Concern | V31 policy |
| ------- | ---------- |
| `case_ref` | required owner |
| `job_ref` | optional source/reference |
| `execution_lease_ref` | optional source/reference |
| `auth_context_ref` | authorization posture |
| `entitlement_ref` | authorization posture |
| `machine_authorization_ref` | authorization posture |
| `license_lease_ref` | authorization posture |
| `runtime_gate_decision_ref` | gate evidence |
| `output_evidence_refs` | optional produced evidence |
| `output_knowledge_refs` | optional produced knowledge candidates |
| client ref | provenance only |
| session | no ownership |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `allowed-provider-call.json` | allowed provider call | `provider_call.case_ref` present |
| `blocked-missing-case.json` | missing case | decision requires case |
| `blocked-missing-entitlement.json` | missing entitlement | blocked reason present |
| `blocked-license-expired.json` | expired license | blocked reason present |
| `provider-output-to-evidence.json` | provider output becomes evidence | evidence ref optional, case remains owner |

## V23 Residual

```text
V23 VS Code docs present: no
If no, residual remains from V24-V30 baseline and is not fixed in V31.
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
| api | `test -f Documentation/execution/provider-authority-binding.md` | pass | new policy doc |
| api | `test -f Documentation/waves/v31-provider-authority-binding.md` | pass | new report |
| api | `test -f schemas/provider-authority-binding.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_provider_authority_binding.py` | pass | conformance |
| api | `python3 conformance/check_provider_authority_binding.py` | pass | `provider-authority-binding: ok` |
| api | `python3 conformance/check_knowledge_binding.py` | pass | V30 regression |
| api | `python3 conformance/check_case_evidence_binding.py` | pass | V29 regression |
| api | `python3 conformance/check_logout_seal_policy.py` | pass | V28 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/provider-authority-binding -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/provider-authority-binding.md` | pass | new runtime/core doc |
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

### Finding A — Provider Calls Are Case-bound

Record:
Provider calls require `case_ref` and are not free-floating model/provider calls.

### Finding B — Provider Calls Are Governed

Record:
Provider authority must pass auth, case, entitlement/license/machine/gate posture
when configured.

### Finding C — Provider Outputs Do Not Own Evidence/Knowledge

Record:
Provider outputs may become evidence or knowledge candidates, but case remains
owner.

### Finding D — Billing/Metering Is Deferred

Record:
V31 may name metering/limit refs but implements no billing or metering.

### Finding E — Agent Authority Can Build On Provider Boundary

Record:
V32 can now define agents as case-bound actors that may request provider calls
only through governed authority.

## V31 Completion Checklist

* [x] `Documentation/execution/provider-authority-binding.md` exists
* [x] `Documentation/waves/v31-provider-authority-binding.md` exists
* [x] `schemas/provider-authority-binding.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists
* [x] `Documentation/execution/provider-authority-binding.md` exists
* [x] provider_call.case_ref invariant documented
* [x] requested actions documented
* [x] decision statuses documented
* [x] safe blocked reasons documented
* [x] provider output posture documented
* [x] E/V boundary documented
* [x] billing/metering boundary documented
* [x] no provider execution implemented
* [x] no model invocation implemented
* [x] no credential/secrets implementation added
* [x] no billing/metering implementation added
* [x] no API endpoint added
* [x] no SDK provider client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
