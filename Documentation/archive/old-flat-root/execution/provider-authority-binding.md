# Provider Authority Binding

## Status

* Delivery: V31
* Status: active provider authority contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define provider calls as governed, case-bound actions.

## Canonical Invariant

```text
provider_call.case_ref is required.
```

Provider calls are governed case-bound actions. They may request model or
provider capabilities, but they are not free-floating work and they do not
replace case, auth, gate, entitlement, license, or machine posture.

## Provider Call Is Not Owned By

Provider calls must not be treated as owned by:

```text
session
client
shell
terminal
Loom
VS Code
Desktop window
workspace
runtime process alone
provider account alone
model response alone
job alone
evidence alone
knowledge alone
license_lease
auth_context
```

## Shape

The canonical provider authority shape may include:

```text
provider_call_ref
case_ref
provider_ref
model_ref optional
requested_action
requested_at
requested_by_principal_ref optional
requested_from_client_ref optional
job_ref optional
execution_lease_ref optional
auth_context_ref optional
entitlement_ref optional
machine_authorization_ref optional
license_lease_ref optional
runtime_gate_decision_ref optional
decision
reason
blocked_reason optional
provider_output_posture
output_evidence_refs optional
output_knowledge_refs optional
metering_ref optional
limit_projection_ref optional
```

Field role notes:

```text
case_ref is the governed ownership boundary for provider calls.
job_ref and execution_lease_ref are optional execution provenance only.
auth_context_ref, entitlement_ref, machine_authorization_ref, license_lease_ref, and runtime_gate_decision_ref are admission posture refs only.
output_evidence_refs and output_knowledge_refs are optional produced refs, not ownership replacement.
metering_ref and limit_projection_ref are safe future posture refs only.
```

## Requested Actions

| Requested action | Meaning |
| ---------------- | ------- |
| `complete` | text or multimodal completion-style generation |
| `embed` | embedding-style representation request |
| `rerank` | ranking or reranking request |
| `classify` | classification request |
| `summarize` | summarization request |
| `extract` | extraction or structured pull request |
| `tool_call` | provider-mediated tool or function call request |
| `model_status` | inspect model availability or posture |
| `provider_status` | inspect provider availability or posture |

## Decision Statuses

| Decision | Meaning |
| -------- | ------- |
| `allowed` | provider call is admitted under current governed posture |
| `blocked` | provider call is denied under current posture |
| `requires_auth` | auth posture is missing or insufficient |
| `requires_case` | case boundary is missing or unresolved |
| `requires_entitlement` | entitlement posture is required before admission |
| `requires_machine_authorization` | machine posture is required before admission |
| `requires_license_lease` | license lease posture is required before admission |
| `requires_runtime_gate` | runtime gate posture is required before admission |
| `requires_limit_capacity` | limit or quota posture blocks admission |
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
| `provider_not_configured` | provider surface is not configured |
| `model_not_allowed` | requested model is outside allowed posture |
| `limit_exceeded` | safe limit projection has been exceeded |
| `quota_exhausted` | quota posture is exhausted |
| `billing_required_but_unavailable` | billing posture is required but not implemented here |
| `manual_review_required` | explicit review is required before admission |
| `unsafe_request` | governed posture classifies the request as unsafe |
| `unknown` | blocked reason is unresolved |

## Provider Output Posture

| Output posture | Meaning |
| -------------- | ------- |
| `no_output` | no output exists |
| `output_not_persisted` | output may exist transiently but was not persisted |
| `output_as_evidence` | output is captured as evidence |
| `output_as_knowledge_candidate` | output is captured as a knowledge candidate |
| `output_redacted` | output exists but was redacted |
| `output_blocked` | output was blocked and not exposed |

## E/V Boundary

```text
provider authority may reference entitlement_ref, license_lease_ref,
machine_authorization_ref and runtime_gate_decision_ref.
```

```text
provider authority must not consume:
pricing
billing provider object
Supabase user object
account profile
raw provider identity
full commercial plan objects
```

## Billing / Metering Boundary

```text
provider authority may reference metering_ref or limit_projection_ref as safe future posture.
V31 does not implement metering or billing.
billing_required_but_unavailable is a blocked reason, not a billing implementation.
```

## Evidence / Knowledge Boundary

```text
Provider outputs may become evidence or knowledge candidates.
Provider outputs do not own evidence or knowledge.
```

Provider outputs can contribute source material, but evidence remains bound to
`case_ref` and knowledge remains bound to `case_ref`.

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| agent authority binding | V32 |
| flow binding | V33 |
| analytics binding | V34 |
| runtime gate registry | V35 |
| local model/provider access boundary | V37 |
| SDK entitlement/license clients | V60 |
