# Runtime Gate Registry

## Status

* Delivery: V35
* Status: active runtime gate contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define runtime action gate classification.

## Canonical Invariants

```text
runtime_action.runtime_action_key is required.
runtime_action.gate_classification is required.
runtime_gate_decision.runtime_action_key is required.
```

Runtime-visible actions must be classified before they are evaluated. The
registry defines what an action is, what family it belongs to, what kind of
gate posture it requires, and whether it may remain visible while sealed. It
does not grant access and it does not evaluate live runtime posture.

## Runtime Gate Registry Is Not

```text
The registry is not a gate evaluator.
The registry is not entitlement implementation.
The registry is not billing or metering.
```

## Shape

The canonical runtime action registry entry may include:

```text
runtime_action_key
runtime_action_family
runtime_action_label
action_category
gate_classification
allowed_during_sealed
required_context
required_refs
required_postures
blocked_reasons
decision_outputs
limit_sensitive
metering_sensitive
cloud_sensitive
writes_state
writes_evidence
writes_knowledge
controls_runtime
```

Field role notes:

```text
runtime_action_key is the required stable action identifier.
gate_classification is the required gate class for the action.
required_context, required_refs, and required_postures describe admission vocabulary only.
blocked_reasons and decision_outputs define safe runtime_gate_decision output vocabulary.
allowed_during_sealed distinguishes diagnostic/read-only posture from operational/write posture.
limit_sensitive and metering_sensitive classify future posture only; they do not implement limits or billing.
```

## Runtime Action Families

| Runtime action family | Meaning |
| --------------------- | ------- |
| `diagnostics` | diagnostic and status-facing runtime actions |
| `auth` | auth posture and login/logout related actions |
| `case` | case boundary actions |
| `operator_context` | operator-context actions |
| `job` | job lifecycle actions |
| `execution_lease` | execution continuity actions |
| `provider` | provider-facing governed actions |
| `agent` | agent admission and action requests |
| `flow` | flow coordination actions |
| `evidence` | evidence materialization actions |
| `knowledge` | knowledge materialization or proposal actions |
| `analytics` | analytics exposure actions |
| `runtime_control` | runtime control-plan or control actions |
| `machine_authorization` | machine posture actions |
| `license` | license posture actions |
| `release_update` | release/update channel actions |
| `cloud_compute` | cloud-capacity-facing actions |
| `admin` | administrative control actions |

## Action Categories

| Action category | Meaning |
| --------------- | ------- |
| `diagnostic_read` | diagnostic or status read surface |
| `safe_read` | safe read surface that does not mutate governed state |
| `case_read` | case-bound read surface |
| `case_write` | case-bound mutation or open/close surface |
| `operational` | governed operational mutation surface |
| `execution` | execution-starting or execution-mutating surface |
| `provider_action` | provider-facing action request |
| `agent_action` | agent admission or action request |
| `flow_action` | flow coordination action |
| `evidence_write` | evidence-producing write surface |
| `knowledge_write` | knowledge-producing write surface |
| `analytics_read` | derived analytics read surface |
| `runtime_control` | runtime-control or service-control surface |
| `release_update` | release/update mutation surface |
| `admin_control` | administrative control surface |

## Gate Classifications

| Gate classification | Meaning |
| ------------------- | ------- |
| `ungated_diagnostic` | diagnostic surface allowed without operational admission |
| `auth_required` | auth posture is required |
| `case_required` | case boundary is required |
| `operator_context_required` | operator context is required |
| `entitlement_required` | entitlement posture is required |
| `machine_authorization_required` | machine posture is required |
| `license_lease_required` | license lease posture is required |
| `runtime_gate_required` | explicit runtime gate posture is required |
| `limit_required` | limit/concurrency posture is required |
| `manual_review_required` | manual review posture is required |
| `admin_required` | administrative posture is required |
| `blocked_always_until_implemented` | action must remain blocked until implemented |

## Decision Statuses

| Decision status | Meaning |
| --------------- | ------- |
| `allowed` | action is admitted |
| `blocked` | action is denied |
| `degraded` | action is admitted only in degraded form |
| `diagnostic_allowed` | diagnostic surface is allowed |
| `read_only_allowed` | read-only surface is allowed |
| `requires_auth` | auth posture is required |
| `requires_case` | case boundary is required |
| `requires_operator_context` | operator context is required |
| `requires_entitlement` | entitlement posture is required |
| `requires_machine_authorization` | machine posture is required |
| `requires_license_lease` | license lease posture is required |
| `requires_runtime_gate` | runtime gate posture is required |
| `requires_limit_capacity` | limit or concurrency posture is required |
| `requires_manual_review` | manual review is required |
| `admin_only` | action is admin-only |
| `not_implemented` | action exists in registry but is not implemented |
| `unknown` | decision posture is unresolved |

## Safe Blocked Reasons

| Blocked reason | Meaning |
| -------------- | ------- |
| `missing_auth_context` | auth posture is missing |
| `missing_case_ref` | case boundary is missing |
| `missing_operator_context` | operator context is missing |
| `missing_entitlement` | entitlement posture is missing |
| `machine_not_authorized` | machine posture is not authorized |
| `license_lease_missing` | license lease is required but missing |
| `license_lease_expired` | license lease exists but is expired |
| `runtime_gate_blocked` | runtime gate posture blocks the action |
| `limit_exceeded` | limit posture blocks the action |
| `quota_exhausted` | quota posture blocks the action |
| `manual_review_required` | review posture blocks the action pending review |
| `admin_required` | admin posture is required |
| `cloud_capacity_unavailable` | cloud capacity is unavailable |
| `release_channel_not_allowed` | release channel posture blocks the action |
| `operation_not_implemented` | action is intentionally unimplemented |
| `runtime_sealed` | sealed runtime posture blocks the action |
| `unsafe_request` | request is classified as unsafe |
| `unknown` | blocked reason is unresolved |

## Sealed Runtime Rules

```text
diagnostic/read-only actions may be allowed while sealed.
operational/write actions must not be allowed solely because runtime is running.
runtime healthy does not imply runtime authorized.
runtime running does not imply gate allowed.
```

## Billing / Metering Boundary

```text
runtime gate registry may mark actions as metering_sensitive or limit_sensitive.
V35 does not implement billing, quota, metering or usage accounting.
```

## E/V Boundary

```text
runtime gate registry may reference entitlement_ref, license_lease_ref,
machine_authorization_ref, runtime_gate_decision_ref and limit_projection_ref.
```

```text
runtime gate registry must not consume:
pricing
billing provider object
Supabase user object
account profile
raw provider identity
full commercial plan objects
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| case/job/flow limit boundary | V36 |
| local model/provider access boundary | V37 |
| cloud compute boundary | V38 |
| machine authorization consumption | V42 |
| license lease consumption | V43 |
| runtime license check request/response | V46/V47 |
| sealed-by-license behavior | V48 |
