# Cloud Compute Boundary

## Status

* Delivery: V38
* Status: active cloud compute boundary contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define cloud compute as optional governed capacity, distinct from local runtime
execution.

## Canonical Invariants

```text
cloud_compute_decision.compute_target is required.
cloud_compute_decision.compute_mode is required.
cloud_compute_decision.case_ref is required for case-scoped cloud work.
```

Cloud compute is optional governed capacity. Local runtime execution is not
cloud compute. Local-first does not imply cloud-free forever, online-authorized
does not imply cloud-only execution, cloud compute does not own case, job,
flow, evidence, knowledge, license_lease, machine_authorization_ref, billing,
or session.

## Compute Targets

| Compute target | Meaning |
| -------------- | ------- |
| `local_runtime` | Local runtime execution surface. |
| `local_model` | Local model execution surface. |
| `external_provider` | External provider execution surface. |
| `hosted_model` | Hosted model surface without implying full cloud compute. |
| `cloud_job` | Cloud compute job surface. |
| `managed_remote_job` | Managed remote job posture surface. |
| `priority_queue` | Queue-priority posture surface. |
| `dedicated_capacity` | Dedicated capacity posture surface. |
| `cloud_artifact_build` | Cloud artifact build posture surface. |
| `cloud_evaluation` | Cloud evaluation posture surface. |

## Compute Modes

| Compute mode | Meaning |
| ------------ | ------- |
| `local_only` | Work remains local. |
| `cloud_optional` | Cloud compute is optional if posture permits. |
| `cloud_required` | Cloud compute is required for the requested posture. |
| `hosted_platform` | Hosted/cloud platform posture. |
| `managed_execution` | Managed remote execution posture. |
| `diagnostic_status` | Diagnostic-only status posture. |
| `not_applicable` | Compute mode does not apply. |

## Requested Actions

| Requested action | Meaning |
| ---------------- | ------- |
| `inspect_status` | Inspect cloud posture without remote execution. |
| `request_cloud_capacity` | Request cloud capacity posture. |
| `submit_remote_job` | Request managed remote job submission posture. |
| `resume_remote_job` | Request managed remote job resume posture. |
| `cancel_remote_job` | Request managed remote job cancellation posture. |
| `invoke_hosted_model` | Request hosted model posture. |
| `run_cloud_evaluation` | Request cloud evaluation posture. |
| `build_cloud_artifact` | Request cloud artifact build posture. |
| `enter_priority_queue` | Request priority queue posture. |
| `use_dedicated_capacity` | Request dedicated capacity posture. |

## Decision Statuses

| Decision | Meaning |
| -------- | ------- |
| `allowed` | Cloud posture is admitted under current governed state. |
| `blocked` | Cloud posture is denied under current state. |
| `degraded` | Cloud posture is partially available with reduced service. |
| `diagnostic_allowed` | Diagnostic inspection is allowed. |
| `requires_auth` | Auth posture is required. |
| `requires_case` | Case boundary is required. |
| `requires_entitlement` | Entitlement posture is required. |
| `requires_machine_authorization` | Machine authorization posture is required. |
| `requires_license_lease` | License lease posture is required. |
| `requires_runtime_gate` | Runtime/cloud gate posture is required. |
| `requires_limit_capacity` | Safe limit posture blocks access. |
| `requires_cloud_capacity` | Cloud capacity posture is required. |
| `requires_manual_review` | Manual review is required. |
| `not_implemented` | Capability is deferred and not live. |
| `unknown` | Posture cannot be classified safely. |

## Blocked Reasons

| Blocked reason | Meaning |
| -------------- | ------- |
| `missing_auth_context` | Auth posture is missing. |
| `missing_case_ref` | Case boundary is missing. |
| `missing_entitlement` | Entitlement posture is missing. |
| `machine_not_authorized` | Machine posture is not authorized. |
| `license_lease_expired` | License posture is expired. |
| `runtime_gate_blocked` | Runtime gate posture blocks access. |
| `limit_exceeded` | Safe limit posture has been exceeded. |
| `cloud_compute_not_enabled` | Cloud compute is not enabled. |
| `cloud_capacity_unavailable` | Cloud capacity is unavailable. |
| `priority_queue_required` | Priority queue posture is required. |
| `dedicated_capacity_required` | Dedicated capacity posture is required. |
| `hosted_model_not_enabled` | Hosted model posture is not enabled. |
| `managed_execution_not_available` | Managed remote execution posture is unavailable. |
| `region_not_available` | Requested compute region is unavailable. |
| `billing_required_but_unavailable` | Billing posture is deferred and unavailable here. |
| `manual_review_required` | Explicit review is required. |
| `unsafe_request` | Request is unsafe under governed posture. |
| `unknown` | No narrower safe reason is available. |

## Output Posture

| Output posture | Meaning |
| -------------- | ------- |
| `no_output` | No output exists. |
| `output_not_persisted` | Output may exist transiently but is not persisted. |
| `output_as_evidence_candidate` | Output may become evidence candidate material. |
| `output_as_knowledge_candidate` | Output may become knowledge candidate material. |
| `cloud_artifact_ref_only` | Only a cloud artifact reference is exposed. |
| `output_redacted` | Output exists but is redacted. |
| `output_blocked` | Output is blocked and not exposed. |
| `diagnostic_only` | Diagnostic-only output posture. |

## Infrastructure Boundary

| Infrastructure boundary | Meaning |
| ----------------------- | ------- |
| `no_cloud_infrastructure` | No cloud infrastructure is involved. |
| `platform_managed_infrastructure` | Platform-managed infrastructure posture only. |
| `customer_managed_infrastructure` | Customer-managed infrastructure posture only. |
| `hybrid_local_cloud` | Hybrid local/cloud posture. |
| `infrastructure_not_exposed_to_v` | Infrastructure details remain outside V/core. |
| `not_applicable` | Infrastructure posture does not apply. |

## Local / Cloud Boundary

```text
local runtime work may proceed locally when authorized.
cloud compute is optional capacity for hosted/remote/managed work.
hosted model access does not imply full cloud compute.
cloud compute access does not imply billing implementation.
cloud compute access does not imply enterprise/SLA commitment.
```

## E/V Boundary

```text
cloud compute decisions may reference entitlement_ref, license_lease_ref,
machine_authorization_ref, runtime_gate_decision_ref, limit_projection_ref,
cloud_compute_ref, cloud_compute_minutes_ref, priority_queue_ref and
dedicated_capacity_ref.
```

```text
cloud compute decisions must not consume:
pricing
billing provider object
Supabase user object
account profile
raw provider identity
full commercial plan objects
raw usage ledger
invoice/subscription objects
cloud provider secret material
infrastructure provider account objects
```

## Billing / Metering Boundary

```text
Cloud compute may be capacity-sensitive or meter-sensitive.
V38 does not implement billing, metering, usage accounting or cloud capacity allocation.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| local machine identity store | V39 |
| machine fingerprint evidence builder | V40 |
| machine enrollment client flow | V41 |
| machine authorization consumption | V42 |
| license lease consumption | V43 |
| account-scoped limit reconciliation | V45 |
| runtime license check request/response | V46/V47 |
