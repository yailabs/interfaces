# V36 — Case / Job / Flow Limit Boundary

## Status

* Delivery: V36
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: runtime limit boundary docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V35 — Runtime Gate Registry
* Next delivery: V37 — Local Model / Provider Access Boundary

## Purpose

V36 defines safe runtime limit projections for cases, jobs, flows, agents and
provider calls.

## Scope

* limit_projection invariants documented;
* limit families documented;
* limit scopes documented;
* limit keys documented;
* decision statuses documented;
* blocked reasons documented;
* account-global sharing documented;
* analytics boundary documented;
* billing/metering boundary documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created or deviation recorded;
* no limit evaluator implemented;
* no billing/metering/quota implementation;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/execution/case-job-flow-limit-boundary.md` | create | limit boundary |
| api | `Documentation/waves/v36-case-job-flow-limit-boundary.md` | create | delivery report |
| api | `schemas/case-job-flow-limit-boundary.v1.schema.json` | create | limit boundary schema |
| api | `fixtures/case-job-flow-limit-boundary/*.json` | create | representative limit fixtures |
| api | `conformance/check_case_job_flow_limit_boundary.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/case-job-flow-limit-boundary.md` | create | runtime/core limit boundary record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| limit boundary doc | created | API execution doctrine added. |
| JSON schema | created | Dependency-free contract artifact. |
| fixtures | created | Representative allowed, warning, blocked, and shared-capacity examples. |
| conformance script | created | Dependency-free fixture/schema validation. |
| yai runtime/core doc | created | Runtime/core boundary recorded. |

## Limit Boundary Model

| Concern | V36 policy |
| ------- | ---------- |
| `limit_projection_ref` | projection identity |
| `limit_key` | required |
| `scope` | required |
| `subject_ref` | required |
| `current_usage` | safe projection only |
| `max_allowed` | safe projection only |
| `remaining` | safe projection only |
| `runtime_gate_decision_ref` | optional gate relation |
| analytics | derived view only |
| billing/metering | not implemented / not owned |
| plan/package | not consumed by V |
| session | no ownership |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `case-limit-allowed.json` | case limit allowed | required keys present |
| `job-limit-blocked.json` | job limit exceeded | blocked reason present |
| `flow-limit-warning.json` | flow warning threshold | warning threshold present |
| `agent-limit-blocked.json` | agent limit exceeded | blocked reason present |
| `provider-call-limit-metering-sensitive.json` | provider call limit/metering sensitive | no billing implementation |
| `account-global-limit-shared-across-machines.json` | account-global shared capacity | scope `account_global` |

## CLI Source Absence Check

Record:

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/execution/case-job-flow-limit-boundary.md` | pass | new policy doc |
| api | `test -f Documentation/waves/v36-case-job-flow-limit-boundary.md` | pass | new report |
| api | `test -f schemas/case-job-flow-limit-boundary.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_case_job_flow_limit_boundary.py` | pass | conformance |
| api | `python3 conformance/check_case_job_flow_limit_boundary.py` | pass | V36 conformance |
| api | `python3 conformance/check_runtime_gate_registry.py` | pass | V35 regression |
| api | `python3 conformance/check_analytics_binding.py` | pass | V34 regression |
| api | `python3 conformance/check_flow_binding.py` | pass | V33 regression |
| api | `python3 conformance/check_agent_authority_binding.py` | pass | V32 regression |
| api | `python3 conformance/check_provider_authority_binding.py` | pass | V31 regression |
| api | `python3 conformance/check_knowledge_binding.py` | pass | V30 regression |
| api | `python3 conformance/check_case_evidence_binding.py` | pass | V29 regression |
| api | `python3 conformance/check_logout_seal_policy.py` | pass | V28 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | existing conformance |
| api | `find schemas -name '*.json' -print0 \| xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/case-job-flow-limit-boundary -name '*.json' -print0 \| xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/case-job-flow-limit-boundary.md` | pass | new runtime/core doc |
| yai | `make info` | pass | yai touched |
| yai | `make yai` | pass | yai touched |
| yai | `git diff --check` | pass | yai touched |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| sdk | validation | not run | docs-only unless touched |
| loom | validation | not run | docs-only unless touched |

## Findings

### Finding A — Limits Are Safe Projections

Record:
Runtime consumes safe limit projections, not plan/billing/quota ledger objects.

### Finding B — Account Capacity Is Shared

Record:
Authorized machines and runtime instances do not multiply account-global limits.

### Finding C — Analytics Does Not Evaluate Limits

Record:
Analytics may summarize limit pressure but is not limit source of truth.

### Finding D — Billing/Metering Is Deferred

Record:
V36 defines limit boundary but implements no billing, metering, quotas or usage
accounting.

### Finding E — V37 Can Define Provider/Model Access

Record:
Provider/model access can now consume safe limit projections and runtime gate
classifications.

## V36 Completion Checklist

* [x] `Documentation/execution/case-job-flow-limit-boundary.md` exists
* [x] `Documentation/waves/v36-case-job-flow-limit-boundary.md` exists
* [x] `schemas/case-job-flow-limit-boundary.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists or deviation recorded
* [x] `yai/Documentation/execution/case-job-flow-limit-boundary.md` exists
* [x] limit_projection invariants documented
* [x] limit families documented
* [x] limit scopes documented
* [x] limit keys documented
* [x] account-global sharing documented
* [x] analytics boundary documented
* [x] billing/metering boundary documented
* [x] E/V boundary documented
* [x] no limit evaluator implemented
* [x] no quota counter implemented
* [x] no billing/metering implementation added
* [x] no API endpoint added
* [x] no SDK limit client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
