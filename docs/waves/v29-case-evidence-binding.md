# V29 — Case Evidence Binding

## Status

* Delivery: V29
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: case evidence binding docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V28 — Logout / Seal Policy
* Next delivery: V30 — Knowledge Binding

## Purpose

V29 defines evidence as case-bound proof material and creates a verifiable
contract artifact.

## Scope

Record:

* evidence.case_ref invariant documented;
* evidence kinds documented;
* visibility values documented;
* retention posture documented;
* detach/logout/seal preservation rules documented;
* JSON schema created;
* fixtures created;
* conformance script created;
* no evidence storage implemented;
* no retrieval/index implementation added;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/execution/case-evidence-binding.md` | create | case evidence binding |
| api | `docs/waves/v29-case-evidence-binding.md` | create | delivery report |
| api | `schemas/case-evidence-binding.v1.schema.json` | create | evidence contract schema |
| api | `fixtures/case-evidence-binding/*.json` | create | representative evidence fixtures |
| api | `conformance/check_case_evidence_binding.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/case-evidence-binding.md` | create | runtime/core evidence record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| case evidence doc | created | API-side canonical evidence ownership contract |
| JSON schema | created | dependency-free JSON contract for case-bound evidence |
| fixtures | created | five representative evidence scenarios |
| conformance script | created | validates JSON parsing, required keys, and enum values |
| yai runtime/core doc | created | runtime/core companion evidence record |

## Evidence Ownership Model

| Concern | V29 policy |
| ------- | ---------- |
| `case_ref` | required owner |
| `job_ref` | optional source/reference |
| `execution_lease_ref` | optional source/reference |
| `provider_call_ref` | optional source/reference |
| `runtime_gate_decision_ref` | optional evidence link |
| `license_lease_ref` | optional authorization posture reference |
| `machine_authorization_ref` | optional authorization posture reference |
| client ref | provenance only |
| session | no ownership |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `manual-note-evidence.json` | manual note | `evidence.case_ref` present |
| `job-output-evidence.json` | job output | `job_ref` optional, `case_ref` owner |
| `provider-call-evidence.json` | provider response | provider ref optional, `case_ref` owner |
| `gate-decision-evidence.json` | gate decision | gate ref optional, `case_ref` owner |
| `detached-job-evidence.json` | evidence after detach | detach does not delete evidence |

## V23 Residual

```text
V23 VS Code docs present: no
If no, residual remains from V24-V28 baseline and is not fixed in V29.
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
| api | `test -f docs/execution/case-evidence-binding.md` | pass | new policy doc |
| api | `test -f docs/waves/v29-case-evidence-binding.md` | pass | new report |
| api | `test -f schemas/case-evidence-binding.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_case_evidence_binding.py` | pass | conformance |
| api | `python3 conformance/check_case_evidence_binding.py` | pass | `case-evidence-binding: ok` |
| api | `python3 conformance/check_logout_seal_policy.py` | pass | V28 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/case-evidence-binding -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/case-evidence-binding.md` | pass | new runtime/core doc |
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

### Finding A — Evidence Is Case-bound

Record:
Evidence belongs to `case_ref`, even when produced by jobs, providers or gates.

### Finding B — Evidence Survives Detach / Logout

Record:
Detach, logout, runtime seal and license expiry do not delete evidence by default.

### Finding C — Schema/Fixtures Exist

Record:
V29 created a verifiable contract artifact, not only prose.

### Finding D — Evidence Enables Knowledge Binding

Record:
V30 can now define knowledge binding on top of case-bound evidence and records.

## V29 Completion Checklist

* [x] `docs/execution/case-evidence-binding.md` exists
* [x] `docs/waves/v29-case-evidence-binding.md` exists
* [x] `schemas/case-evidence-binding.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists
* [x] `yai/Documentation/execution/case-evidence-binding.md` exists
* [x] evidence.case_ref invariant documented
* [x] evidence kinds documented
* [x] visibility documented
* [x] retention posture documented
* [x] detach/logout/seal preservation rules documented
* [x] no evidence storage implemented
* [x] no retrieval/index implementation added
* [x] no API endpoint added
* [x] no SDK client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
