# V30 — Knowledge Binding

## Status

* Delivery: V30
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: knowledge binding docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V29 — Case Evidence Binding
* Next delivery: V31 — Provider Authority Binding

## Purpose

V30 defines knowledge/materialized memory as case-bound governed state and
creates a verifiable contract artifact.

## Scope

Record:

* knowledge.case_ref invariant documented;
* knowledge kinds documented;
* visibility values documented;
* recall policy documented;
* write policy documented;
* derivation status documented;
* detach/logout/seal preservation rules documented;
* JSON schema created;
* fixtures created;
* conformance script created;
* no knowledge storage implemented;
* no retrieval/index/recall implementation added;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/execution/knowledge-binding.md` | create | case knowledge binding |
| api | `docs/waves/v30-knowledge-binding.md` | create | delivery report |
| api | `schemas/knowledge-binding.v1.schema.json` | create | knowledge contract schema |
| api | `fixtures/knowledge-binding/*.json` | create | representative knowledge fixtures |
| api | `conformance/check_knowledge_binding.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/knowledge-binding.md` | create | runtime/core knowledge record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| knowledge binding doc | created | API-side canonical knowledge ownership contract |
| JSON schema | created | dependency-free JSON contract for case-bound knowledge |
| fixtures | created | five representative knowledge scenarios |
| conformance script | created | validates JSON parsing, required keys, enum values, and `knowledge.case_ref` |
| yai runtime/core doc | created | runtime/core companion knowledge record |

## Knowledge Ownership Model

| Concern | V30 policy |
| ------- | ---------- |
| `case_ref` | required owner |
| `source_evidence_refs` | optional source/reference |
| `source_record_refs` | optional source/reference |
| `source_job_refs` | optional source/reference |
| `source_provider_call_refs` | optional source/reference |
| `lineage_refs` | optional provenance |
| client ref | provenance only |
| session | no ownership |
| workspace/window | no ownership |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `manual-summary-knowledge.json` | manual summary | `knowledge.case_ref` present |
| `evidence-derived-knowledge.json` | evidence-derived knowledge | evidence refs optional, `case_ref` owner |
| `job-derived-knowledge.json` | job-derived knowledge | job refs optional, `case_ref` owner |
| `provider-derived-knowledge.json` | provider output materialized | provider ref optional, `case_ref` owner |
| `detached-case-knowledge.json` | knowledge after detach | detach does not delete knowledge |

## V23 Residual

```text
V23 VS Code docs present: no
If no, residual remains from V24-V29 baseline and is not fixed in V30.
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
| api | `test -f docs/execution/knowledge-binding.md` | pass | new policy doc |
| api | `test -f docs/waves/v30-knowledge-binding.md` | pass | new report |
| api | `test -f schemas/knowledge-binding.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_knowledge_binding.py` | pass | conformance |
| api | `python3 conformance/check_knowledge_binding.py` | pass | `knowledge-binding: ok` |
| api | `python3 conformance/check_case_evidence_binding.py` | pass | V29 regression |
| api | `python3 conformance/check_logout_seal_policy.py` | pass | V28 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/knowledge-binding -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/knowledge-binding.md` | pass | new runtime/core doc |
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

### Finding A — Knowledge Is Case-bound

Record:
Knowledge/materialized memory belongs to `case_ref`, even when derived from
evidence, records, jobs, providers or models.

### Finding B — Knowledge Survives Detach / Logout

Record:
Detach, logout, runtime seal and license expiry do not delete knowledge by
default.

### Finding C — Recall Remains Governed

Record:
Recall must not bypass auth, case, runtime gate, license or machine posture.

### Finding D — Schema/Fixtures Exist

Record:
V30 created a verifiable contract artifact, not only prose.

### Finding E — Provider Authority Can Build On Knowledge Boundary

Record:
V31 can now define provider authority without letting provider outputs own
knowledge.

## V30 Completion Checklist

* [x] `docs/execution/knowledge-binding.md` exists
* [x] `docs/waves/v30-knowledge-binding.md` exists
* [x] `schemas/knowledge-binding.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists
* [x] `yai/Documentation/execution/knowledge-binding.md` exists
* [x] knowledge.case_ref invariant documented
* [x] knowledge kinds documented
* [x] visibility documented
* [x] recall policy documented
* [x] write policy documented
* [x] derivation status documented
* [x] detach/logout/seal preservation rules documented
* [x] no knowledge storage implemented
* [x] no retrieval/index/recall implementation added
* [x] no API endpoint added
* [x] no SDK client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
