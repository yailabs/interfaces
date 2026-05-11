# V33 — Flow Binding

## Status

* Delivery: V33
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: flow binding docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V32 — Agent Authority Binding
* Next delivery: V34 — Analytics Binding

## Purpose

V33 defines flows as governed, case-bound orchestration structures and creates a
verifiable contract artifact.

## Scope

Record:

* flow.case_ref invariant documented;
* flow kinds documented;
* requested actions documented;
* decision statuses documented;
* safe blocked reasons documented;
* flow output posture documented;
* coordination boundary documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created;
* no flow execution implemented;
* no DAG/executor implementation;
* no agent/provider/job execution implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/execution/flow-binding.md` | create | flow binding |
| api | `Documentation/waves/v33-flow-binding.md` | create | delivery report |
| api | `schemas/flow-binding.v1.schema.json` | create | flow binding contract schema |
| api | `fixtures/flow-binding/*.json` | create | representative flow binding fixtures |
| api | `conformance/check_flow_binding.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/flow-binding.md` | create | runtime/core flow binding record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| flow binding doc | created | API-side canonical flow binding contract |
| JSON schema | created | dependency-free JSON contract for governed flows |
| fixtures | created | five representative flow binding scenarios |
| conformance script | created | validates JSON parsing, required keys, enum values, and case/blocked posture rules |
| yai runtime/core doc | created | runtime/core companion flow binding record |

## Flow Binding Model

| Concern | V33 policy |
| ------- | ---------- |
| `case_ref` | required owner |
| `flow_ref` | flow identity |
| `flow_run_ref` | optional run identity |
| `job_refs` | optional coordinated jobs |
| `agent_instance_refs` | optional coordinated agents |
| `provider_call_refs` | optional coordinated provider calls |
| `execution_lease_refs` | optional continuity refs |
| `evidence_refs` | optional produced/referenced evidence |
| `knowledge_refs` | optional produced/referenced knowledge |
| `runtime_gate_decision_ref` | gate evidence |
| client ref | provenance only |
| session | no ownership |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `allowed-case-flow.json` | allowed case flow | `flow.case_ref` present |
| `blocked-missing-case.json` | missing case | decision requires case |
| `flow-with-agent-step.json` | flow coordinates agent | agent ref optional, `case_ref` owner |
| `flow-with-provider-step.json` | flow coordinates provider call | provider ref optional, authority required |
| `flow-output-to-evidence.json` | flow output becomes evidence | evidence ref optional, case remains owner |

## V23 Residual

```text
V23 VS Code docs present: no
If no, residual remains from V24-V32 baseline and is not fixed in V33.
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
| api | `test -f Documentation/execution/flow-binding.md` | pass | new policy doc |
| api | `test -f Documentation/waves/v33-flow-binding.md` | pass | new report |
| api | `test -f schemas/flow-binding.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_flow_binding.py` | pass | conformance |
| api | `python3 conformance/check_flow_binding.py` | pass | `flow-binding: ok` |
| api | `python3 conformance/check_agent_authority_binding.py` | pass | V32 regression |
| api | `python3 conformance/check_provider_authority_binding.py` | pass | V31 regression |
| api | `python3 conformance/check_knowledge_binding.py` | pass | V30 regression |
| api | `python3 conformance/check_case_evidence_binding.py` | pass | V29 regression |
| api | `python3 conformance/check_logout_seal_policy.py` | pass | V28 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/flow-binding -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/flow-binding.md` | pass | new runtime/core doc |
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

### Finding A — Flows Are Case-bound

Record:
Flows require `case_ref` and are not free-floating workflow engines.

### Finding B — Flows Coordinate, Not Own

Record:
Flows may coordinate jobs, agents and provider calls, but do not own them.

### Finding C — Flows Do Not Bypass Authority

Record:
Flow activity must use job, agent, provider and runtime authority boundaries.

### Finding D — Flow Outputs Do Not Own Evidence/Knowledge

Record:
Flow outputs may become evidence or knowledge candidates, but case remains owner.

### Finding E — Analytics Can Build On Flow Activity

Record:
V34 can now define analytics as derived from case-bound governed activity.

## V33 Completion Checklist

* [x] `Documentation/execution/flow-binding.md` exists
* [x] `Documentation/waves/v33-flow-binding.md` exists
* [x] `schemas/flow-binding.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists
* [x] `Documentation/execution/flow-binding.md` exists
* [x] flow.case_ref invariant documented
* [x] flow kinds documented
* [x] requested actions documented
* [x] decision statuses documented
* [x] safe blocked reasons documented
* [x] flow output posture documented
* [x] coordination boundary documented
* [x] E/V boundary documented
* [x] no flow execution implemented
* [x] no DAG/executor implementation added
* [x] no agent/provider/job execution implemented
* [x] no API endpoint added
* [x] no SDK flow client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
