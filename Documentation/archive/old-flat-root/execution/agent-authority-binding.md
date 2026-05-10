# Agent Authority Binding

## Status

* Delivery: V32
* Status: active agent authority contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define agents as governed, case-bound actors.

## Canonical Invariant

```text
agent_instance.case_ref is required.
```

Agents are governed case-bound actors. They may request work, delegation,
provider access, or tool access, but they are not free-floating autonomous
authorities and they do not replace case, auth, gate, entitlement, license, or
machine posture.

## Agent Is Not Owned By

Agents must not be treated as owned by:

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
flow
provider calls
evidence
knowledge
runtime lifecycle
runtime gate decisions
license_lease
auth_context
```

## Shape

The canonical agent authority shape may include:

```text
agent_authority_ref
agent_ref
agent_instance_ref
case_ref
agent_role
requested_action
requested_at
requested_by_principal_ref optional
requested_from_client_ref optional
job_ref optional
flow_ref optional
execution_lease_ref optional
auth_context_ref optional
entitlement_ref optional
machine_authorization_ref optional
license_lease_ref optional
runtime_gate_decision_ref optional
limit_projection_ref optional
decision
reason
blocked_reason optional
agent_output_posture
allowed_provider_action_refs optional
allowed_tool_action_refs optional
output_evidence_refs optional
output_knowledge_refs optional
```

Field role notes:

```text
case_ref is the governed ownership boundary for the agent instance.
job_ref, flow_ref, and execution_lease_ref are optional execution provenance only.
auth_context_ref, entitlement_ref, machine_authorization_ref, license_lease_ref, and runtime_gate_decision_ref are admission posture refs only.
allowed_provider_action_refs and allowed_tool_action_refs are optional authority surfaces, not execution.
output_evidence_refs and output_knowledge_refs are optional produced refs, not ownership replacement.
limit_projection_ref is a safe future posture ref only.
```

## Agent Roles

| Agent role | Meaning |
| ---------- | ------- |
| `assistant` | general-purpose guided helper |
| `researcher` | evidence/context gathering agent |
| `coder` | implementation-oriented agent |
| `reviewer` | review, audit, or critique agent |
| `operator` | operational posture/action agent |
| `planner` | planning or decomposition agent |
| `critic` | adversarial or challenge agent |
| `summarizer` | synthesis and summarization agent |
| `specialist` | narrow-domain expert agent |
| `system_agent` | reserved system-scoped agent role |

## Requested Actions

| Requested action | Meaning |
| ---------------- | ------- |
| `spawn` | request a new agent instance |
| `resume` | request continuation of an existing agent instance |
| `pause` | request pause posture for an agent |
| `stop` | request stop posture for an agent |
| `delegate` | request delegated case-bound work |
| `request_provider_call` | request provider access through provider authority |
| `request_tool_call` | request tool access through future tool/runtime authority |
| `write_evidence` | request evidence materialization |
| `propose_knowledge` | request knowledge proposal/materialization |
| `read_case_context` | request governed case-context read posture |

## Decision Statuses

| Decision | Meaning |
| -------- | ------- |
| `allowed` | agent request is admitted under current governed posture |
| `blocked` | agent request is denied under current posture |
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
| `agent_role_not_allowed` | requested agent role is outside allowed posture |
| `agent_limit_exceeded` | safe agent limit projection has been exceeded |
| `flow_not_authorized` | flow relationship is not authorized for this request |
| `provider_authority_missing` | provider authority is required but absent |
| `tool_authority_missing` | tool/runtime authority is required but absent |
| `manual_review_required` | explicit review is required before admission |
| `unsafe_request` | governed posture classifies the request as unsafe |
| `unknown` | blocked reason is unresolved |

## Agent Output Posture

| Output posture | Meaning |
| -------------- | ------- |
| `no_output` | no output exists |
| `output_not_persisted` | output may exist transiently but was not persisted |
| `output_as_evidence` | output is captured as evidence |
| `output_as_knowledge_candidate` | output is captured as a knowledge candidate |
| `output_requires_review` | output exists but requires review before use |
| `output_redacted` | output exists but was redacted |
| `output_blocked` | output was blocked and not exposed |

## Provider / Tool Boundary

```text
agents may request provider calls only through provider authority.
agents may request tool calls only through future tool/runtime authority.
agent output may become evidence or knowledge candidate.
agent output does not own evidence or knowledge.
```

## E/V Boundary

```text
agent authority may reference entitlement_ref, license_lease_ref,
machine_authorization_ref and runtime_gate_decision_ref.
```

```text
agent authority must not consume:
pricing
billing provider object
Supabase user object
account profile
raw provider identity
full commercial plan objects
```

## Evidence / Knowledge Boundary

```text
Agent outputs may become evidence or knowledge candidates.
Agent outputs do not own evidence or knowledge.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| flow binding | V33 |
| analytics binding | V34 |
| runtime gate registry | V35 |
| case/job/flow limit boundary | V36 |
| local model/provider access boundary | V37 |
| SDK entitlement/license clients | V60 |
