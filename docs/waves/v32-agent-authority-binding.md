# V32 — Agent Authority Binding

## Status

* Delivery: V32
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: agent authority docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V31 — Provider Authority Binding
* Next delivery: V33 — Flow Binding

## Purpose

V32 defines agents as governed, case-bound actors and creates a verifiable
contract artifact.

## Scope

Record:

* agent_instance.case_ref invariant documented;
* agent roles documented;
* requested actions documented;
* decision statuses documented;
* safe blocked reasons documented;
* agent output posture documented;
* provider/tool boundary documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created;
* no agent execution implemented;
* no provider/tool execution implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/execution/agent-authority-binding.md` | create | agent authority binding |
| api | `docs/waves/v32-agent-authority-binding.md` | create | delivery report |
| api | `schemas/agent-authority-binding.v1.schema.json` | create | agent authority contract schema |
| api | `fixtures/agent-authority-binding/*.json` | create | representative agent authority fixtures |
| api | `conformance/check_agent_authority_binding.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/agent-authority-binding.md` | create | runtime/core agent authority record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| agent authority doc | created | API-side canonical agent authority contract |
| JSON schema | created | dependency-free JSON contract for governed agents |
| fixtures | created | five representative agent authority scenarios |
| conformance script | created | validates JSON parsing, required keys, enum values, and case/blocked posture rules |
| yai runtime/core doc | created | runtime/core companion agent authority record |

## Agent Authority Model

| Concern | V32 policy |
| ------- | ---------- |
| `case_ref` | required owner |
| `agent_ref` | agent identity |
| `agent_instance_ref` | runtime instance identity |
| `job_ref` | optional source/reference |
| `flow_ref` | optional source/reference |
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
| `allowed-agent-spawn.json` | allowed agent spawn | `agent_instance.case_ref` present |
| `blocked-missing-case.json` | missing case | decision requires case |
| `blocked-agent-limit.json` | max agent/concurrency limit | blocked reason present |
| `agent-provider-call-request.json` | agent requests provider call | provider authority boundary referenced |
| `agent-output-to-evidence.json` | agent output becomes evidence | evidence ref optional, case remains owner |

## V23 Residual

```text
V23 VS Code docs present: no
If no, residual remains from V24-V31 baseline and is not fixed in V32.
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
| api | `test -f docs/execution/agent-authority-binding.md` | pass | new policy doc |
| api | `test -f docs/waves/v32-agent-authority-binding.md` | pass | new report |
| api | `test -f schemas/agent-authority-binding.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_agent_authority_binding.py` | pass | conformance |
| api | `python3 conformance/check_agent_authority_binding.py` | pass | `agent-authority-binding: ok` |
| api | `python3 conformance/check_provider_authority_binding.py` | pass | V31 regression |
| api | `python3 conformance/check_knowledge_binding.py` | pass | V30 regression |
| api | `python3 conformance/check_case_evidence_binding.py` | pass | V29 regression |
| api | `python3 conformance/check_logout_seal_policy.py` | pass | V28 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/agent-authority-binding -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/agent-authority-binding.md` | pass | new runtime/core doc |
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

### Finding A — Agents Are Case-bound

Record:
Agent instances require `case_ref` and are not free-floating autonomous
authorities.

### Finding B — Agents Are Governed

Record:
Agent authority must pass auth, case, entitlement/license/machine/gate posture
when configured.

### Finding C — Agents Do Not Own Provider Calls Or Knowledge

Record:
Agents may request provider/tool actions and produce outputs, but outputs remain
case-bound evidence/knowledge candidates.

### Finding D — Agent Limits Are Admission Posture

Record:
V32 may name agent limit/concurrency posture but implements no limit evaluator.

### Finding E — Flow Binding Can Build On Agent Boundary

Record:
V33 can now define flows as case-bound coordinators of jobs/agents/provider
actions.

## V32 Completion Checklist

* [x] `docs/execution/agent-authority-binding.md` exists
* [x] `docs/waves/v32-agent-authority-binding.md` exists
* [x] `schemas/agent-authority-binding.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists
* [x] `Documentation/execution/agent-authority-binding.md` exists
* [x] agent_instance.case_ref invariant documented
* [x] agent roles documented
* [x] requested actions documented
* [x] decision statuses documented
* [x] safe blocked reasons documented
* [x] agent output posture documented
* [x] provider/tool boundary documented
* [x] E/V boundary documented
* [x] no agent execution implemented
* [x] no provider/tool execution implemented
* [x] no credential/secrets implementation added
* [x] no billing/metering implementation added
* [x] no API endpoint added
* [x] no SDK agent client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
