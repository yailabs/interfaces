# Flow Binding

## Status

* Delivery: V33
* Status: active flow binding contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define flows as governed, case-bound orchestration structures.

## Canonical Invariant

```text
flow.case_ref is required.
```

Flows are governed case-bound orchestration structures. They may coordinate
jobs, agents, provider calls, tool actions, approvals, evidence materialization,
and knowledge proposals, but they are not free-floating workflow engines and
they do not replace case, auth, gate, entitlement, license, machine, or other
governed authority surfaces.

## Flow Is Not Owned By

Flows must not be treated as owned by:

```text
session
client
shell
terminal
Loom
VS Code
Desktop window
workspace
job
agent
provider call
evidence
knowledge
runtime lifecycle
runtime gate decisions
license_lease
auth_context
```

## Shape

The canonical flow binding shape may include:

```text
flow_ref
flow_run_ref optional
case_ref
flow_kind
requested_action
requested_at
requested_by_principal_ref optional
requested_from_client_ref optional
job_refs optional
agent_instance_refs optional
provider_call_refs optional
execution_lease_refs optional
evidence_refs optional
knowledge_refs optional
flow_step_refs optional
auth_context_ref optional
entitlement_ref optional
machine_authorization_ref optional
license_lease_ref optional
runtime_gate_decision_ref optional
limit_projection_ref optional
decision
reason
blocked_reason optional
flow_output_posture
```

Field role notes:

```text
case_ref is the governed ownership boundary for the flow.
flow_run_ref is an optional run identity, not a second owner.
job_refs, agent_instance_refs, provider_call_refs, and execution_lease_refs are optional coordinated refs only.
evidence_refs, knowledge_refs, and flow_step_refs are optional produced or linked refs, not ownership replacement.
auth_context_ref, entitlement_ref, machine_authorization_ref, license_lease_ref, and runtime_gate_decision_ref are authority posture refs only.
limit_projection_ref is a safe future posture ref only.
```

## Flow Kinds

| Flow kind | Meaning |
| --------- | ------- |
| `manual_workflow` | human-directed ordered workflow |
| `agentic_workflow` | workflow coordinating agent activity |
| `job_pipeline` | workflow coordinating job steps |
| `review_flow` | review-oriented flow with governed checkpoints |
| `approval_flow` | explicit approval and decision flow |
| `provider_pipeline` | flow coordinating provider-facing activity |
| `knowledge_pipeline` | flow coordinating knowledge-oriented derivation |
| `release_flow` | operational release/change flow |
| `system_flow` | reserved system-scoped flow kind |

## Requested Actions

| Requested action | Meaning |
| ---------------- | ------- |
| `create` | request flow creation posture |
| `start` | request admission to start a flow |
| `resume` | request continuation of a paused or deferred flow |
| `pause` | request pause posture for a flow |
| `stop` | request stop posture for a flow |
| `cancel` | request cancellation posture for a flow |
| `add_step` | request addition of a governed flow step |
| `remove_step` | request removal of a flow step |
| `run_step` | request admission to execute a specific step |
| `delegate_to_agent` | request governed delegation to an agent |
| `request_provider_call` | request provider access through provider authority |
| `write_evidence` | request evidence materialization |
| `propose_knowledge` | request knowledge proposal/materialization |
| `inspect_status` | request governed flow inspection posture |

## Decision Statuses

| Decision | Meaning |
| -------- | ------- |
| `allowed` | flow request is admitted under current governed posture |
| `blocked` | flow request is denied under current posture |
| `requires_auth` | auth posture is missing or insufficient |
| `requires_case` | case boundary is missing or unresolved |
| `requires_entitlement` | entitlement posture is required before admission |
| `requires_machine_authorization` | machine posture is required before admission |
| `requires_license_lease` | license lease posture is required before admission |
| `requires_runtime_gate` | runtime gate posture is required before admission |
| `requires_limit_capacity` | concurrency or limit posture blocks admission |
| `requires_manual_review` | admission is deferred to explicit review |
| `unknown` | admission posture is unresolved |

## Safe Blocked Reasons

| Blocked reason | Meaning |
| -------------- | ------- |
| `missing_auth_context` | auth posture is missing |
| `missing_case_ref` | case boundary is missing |
| `missing_operator_context` | operator context is required but absent |
| `missing_entitlement` | entitlement posture is required but absent |
| `machine_not_authorized` | machine posture is not authorized |
| `license_lease_expired` | license lease exists but is expired |
| `runtime_gate_blocked` | runtime gate posture blocks admission |
| `flow_kind_not_allowed` | requested flow kind is outside allowed posture |
| `flow_limit_exceeded` | safe flow limit projection has been exceeded |
| `agent_authority_missing` | governed agent authority is required but absent |
| `provider_authority_missing` | governed provider authority is required but absent |
| `job_limit_exceeded` | safe job limit projection has been exceeded |
| `manual_review_required` | explicit review is required before admission |
| `unsafe_request` | governed posture classifies the request as unsafe |
| `unknown` | blocked reason is unresolved |

## Flow Output Posture

| Output posture | Meaning |
| -------------- | ------- |
| `no_output` | no output exists |
| `output_not_persisted` | output may exist transiently but was not persisted |
| `output_as_evidence` | output is captured as evidence |
| `output_as_knowledge_candidate` | output is captured as a knowledge candidate |
| `output_requires_review` | output exists but requires review before use |
| `output_redacted` | output exists but was redacted |
| `output_blocked` | output was blocked and not exposed |

## Coordination Boundary

```text
flows may coordinate jobs, agents and provider calls only through governed
authority.
flows may produce or reference evidence/knowledge candidates.
flows do not own evidence or knowledge.
flows do not bypass job/agent/provider/runtime gates.
```

## E/V Boundary

```text
flow binding may reference entitlement_ref, license_lease_ref,
machine_authorization_ref and runtime_gate_decision_ref.
```

```text
flow binding must not consume:
pricing
billing provider object
Supabase user object
account profile
raw provider identity
full commercial plan objects
```

## Evidence / Knowledge Boundary

```text
Flow outputs may become evidence or knowledge candidates.
Flow outputs do not own evidence or knowledge.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| analytics binding | V34 |
| runtime gate registry | V35 |
| case/job/flow limit boundary | V36 |
| local model/provider access boundary | V37 |
| SDK entitlement/license clients | V60 |
