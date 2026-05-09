# Analytics Binding

## Status

* Delivery: V34
* Status: active analytics binding contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define analytics as derived from governed case-bound activity.

## Canonical Invariants

```text
analytics_event.case_ref is required.
analytics_projection.case_ref is required when projection is case-scoped.
```

Analytics binding may represent an event, summary, projection, or aggregate over
governed runtime activity. When analytics is case-scoped, the case boundary
remains mandatory. Analytics may summarize governed material, but it does not
become a new owner or authority surface.

## Analytics Is Not Primary Truth

```text
analytics is derived.
analytics is not primary truth.
records/evidence/knowledge/gate decisions remain source material.
analytics cannot override runtime_gate_decision.
analytics cannot override license_lease.
analytics cannot override evidence or knowledge.
analytics cannot create entitlement.
analytics cannot create billing consent.
```

## Analytics Does Not Own

Analytics must not be treated as owning:

```text
case
job
flow
agent
provider call
evidence
knowledge
runtime_gate_decision
entitlement
license_lease
machine_authorization_ref
auth_context
session
client
window
workspace state
billing provider object
raw provider identity
```

## Shape

The canonical analytics binding shape may include:

```text
analytics_ref
analytics_kind
analytics_scope
case_ref
metric_key
metric_value optional
measurement_unit optional
observed_at
window_start optional
window_end optional
source_record_refs optional
source_evidence_refs optional
source_knowledge_refs optional
source_job_refs optional
source_flow_refs optional
source_agent_instance_refs optional
source_provider_call_refs optional
runtime_gate_decision_refs optional
license_lease_refs optional
machine_authorization_refs optional
limit_projection_refs optional
derived_from_refs optional
visibility
retention_posture
decision
reason
blocked_reason optional
```

Field role notes:

```text
analytics_ref identifies the derived analytics material, not the source of truth.
case_ref is required when analytics_scope is case or case_tree.
source_* refs remain source material only and are not replaced by analytics.
runtime_gate_decision_refs, license_lease_refs, and machine_authorization_refs are posture/context references only.
limit_projection_refs are safe future posture references, not live counters.
metric_value and measurement_unit are optional summaries and do not create authority.
```

## Analytics Kinds

| Analytics kind | Meaning |
| -------------- | ------- |
| `case_activity` | derived case activity summary |
| `job_progress` | derived job progress or completion summary |
| `flow_progress` | derived flow progress summary |
| `agent_activity` | derived agent activity summary |
| `provider_activity` | derived provider activity summary |
| `evidence_growth` | derived evidence volume or change summary |
| `knowledge_growth` | derived knowledge volume or change summary |
| `gate_block` | derived blocked/admission posture summary |
| `limit_pressure` | derived limit or quota pressure summary |
| `runtime_readiness` | derived runtime readiness summary |
| `review_activity` | derived approval/review summary |
| `system_observation` | internal system observation summary |

## Analytics Scopes

| Analytics scope | Meaning |
| --------------- | ------- |
| `case` | analytics scoped to one governed case |
| `case_tree` | analytics scoped to a case hierarchy |
| `account_projection` | account-level safe projection surface |
| `machine_projection` | machine-level safe projection surface |
| `runtime_projection` | runtime-level safe projection surface |
| `system_internal` | internal-only analytics surface |

## Decision Statuses

| Decision | Meaning |
| -------- | ------- |
| `recorded` | derived analytics was admitted and recorded |
| `blocked` | analytics materialization was denied |
| `requires_case` | case binding is required before recording |
| `requires_auth` | auth posture is required before recording |
| `requires_gate` | runtime gate posture is required before recording |
| `redacted` | analytics exists but was redacted |
| `aggregated_only` | only aggregate analytics may be exposed |
| `unknown` | analytics recording posture is unresolved |

## Safe Blocked / Redaction Reasons

| Reason | Meaning |
| ------ | ------- |
| `missing_case_ref` | required case boundary is missing |
| `missing_auth_context` | auth posture is missing |
| `runtime_gate_blocked` | runtime gate posture blocks analytics recording |
| `insufficient_visibility` | visibility posture does not allow exposure |
| `privacy_redaction_required` | privacy posture requires redaction |
| `raw_provider_identity_forbidden` | raw provider identity cannot be consumed |
| `billing_object_forbidden` | billing objects cannot be consumed |
| `outside_scope` | requested analytics is outside allowed scope |
| `unknown` | blocked/redaction reason is unresolved |

## Visibility

| Visibility | Meaning |
| ---------- | ------- |
| `private` | visible only to narrow authorized posture |
| `case_visible` | visible within governed case posture |
| `team_visible` | visible to authorized team posture |
| `admin_visible` | visible to administrative posture |
| `system_internal` | internal-only runtime/system surface |
| `aggregated` | aggregate-only exposure |

## Retention Posture

| Retention posture | Meaning |
| ----------------- | ------- |
| `retain` | retain under explicit policy |
| `aggregate_only` | keep only aggregate projection |
| `redact_later` | retain with later redaction posture |
| `delete_only_by_explicit_policy` | delete only through explicit policy |
| `system_internal` | internal retention posture |
| `unknown` | retention posture unresolved |

## Billing / Metering Boundary

```text
analytics is not billing.
analytics is not quota accounting.
analytics is not a metering ledger.
analytics may reference limit_projection_refs or future meter refs only as safe
projection material.
V34 does not implement billing, meters, quotas or usage accounting.
```

## E/V Boundary

```text
analytics binding may reference entitlement_ref, license_lease_ref,
machine_authorization_ref, runtime_gate_decision_ref and limit_projection_ref.
```

```text
analytics binding must not consume:
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
| runtime gate registry | V35 |
| case/job/flow limit boundary | V36 |
| local model/provider access boundary | V37 |
| SDK entitlement/license clients | V60 |
