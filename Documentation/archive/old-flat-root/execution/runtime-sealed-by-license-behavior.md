# Runtime Sealed-by-License Behavior

## Status

* Delivery: V48
* Status: active sealed-by-license behavior contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define how runtime interprets license/machine/lease response posture into
sealed or unsealed operational readiness.

## Canonical Invariants

```text
runtime_license_seal_state.seal_state is required.
runtime_license_seal_state.seal_reason is required.
runtime_license_seal_state.operational_readiness is required.
runtime_license_seal_state.diagnostic_posture is required.
```

## Sealed-by-License Is Not

```text
runtime stopped
service lifecycle
auth logout
session detach
billing/subscription
```

## Shape

```text
runtime_license_seal_state_ref
runtime_license_check_response_ref optional
license_lease_ref optional
machine_authorization_ref optional
local_machine_ref optional
runtime_gate_decision_ref optional
limit_projection_ref optional
seal_state
seal_reason
operational_readiness
diagnostic_posture
allowed_surface_posture
blocked_surface_posture
recovery_posture
next_action
response_freshness
cache_posture optional
offline_grace_posture optional
warning_codes optional
safe_status_projection optional
```

## Seal States

| Seal state | Meaning |
| ---------- | ------- |
| `unsealed` | Runtime may expose operational surfaces under current posture. |
| `sealed` | Operational surfaces remain blocked by current license posture. |
| `partially_sealed` | Some non-diagnostic surfaces remain available, but full operations are not. |
| `diagnostics_only` | Runtime remains available for diagnostics while operational actions stay sealed. |
| `unknown` | Seal posture could not be classified safely. |

## Seal Reasons

| Seal reason | Meaning |
| ----------- | ------- |
| `none` | No seal reason is currently asserted. |
| `missing_machine_authorization` | Machine authorization posture is absent. |
| `machine_authorization_revoked` | Machine authorization posture is revoked. |
| `machine_authorization_expired` | Machine authorization posture is expired. |
| `missing_license_lease` | License lease posture is absent. |
| `license_lease_expired` | License lease posture is expired. |
| `license_lease_revoked` | License lease posture is revoked. |
| `license_lease_stale` | License lease posture is stale. |
| `entitlement_missing` | Required entitlement posture is missing. |
| `limit_exceeded` | Account-scoped limit posture blocks operations. |
| `runtime_gate_blocked` | Runtime gate posture blocks the requested surface. |
| `online_check_required` | Safe local posture is insufficient without an online check. |
| `manual_review_required` | Manual review is required before operations continue. |
| `unsafe_projection` | Provided posture is not safe to consume. |
| `unknown` | Seal reason is not safely known. |

## Operational Readiness

| Operational readiness | Meaning |
| --------------------- | ------- |
| `ready` | Runtime may expose operational surfaces under current posture. |
| `blocked` | Runtime is not operationally ready for blocked surfaces. |
| `degraded` | Runtime may operate with restricted surfaces or limited scope. |
| `diagnostics_only` | Runtime should remain diagnostic-only. |
| `unknown` | Readiness cannot be classified safely. |

## Diagnostic / Allowed / Blocked Surface Postures

| Diagnostic posture | Meaning |
| ------------------ | ------- |
| `diagnostics_allowed` | Diagnostics may remain visible or callable. |
| `diagnostics_limited` | Diagnostics remain available in a reduced form. |
| `diagnostics_blocked` | Diagnostics are also blocked. |
| `unknown` | Diagnostic posture is not safely known. |

| Allowed surface posture | Meaning |
| ----------------------- | ------- |
| `diagnostics_only` | Only diagnostic surfaces remain available. |
| `read_only_only` | Read-only surfaces remain available. |
| `operational_allowed` | Operational surfaces may remain available. |
| `limited_operational` | A constrained operational subset may remain available. |
| `none` | No non-blocked surface is asserted. |
| `unknown` | Allowed surface posture is not safely known. |

| Blocked surface posture | Meaning |
| ----------------------- | ------- |
| `none` | No specific blocked operational surface is asserted. |
| `operational_write_blocked` | Operational write actions remain blocked. |
| `provider_actions_blocked` | Provider-facing actions remain blocked. |
| `agent_flow_job_blocked` | Agent, flow, or job actions remain blocked. |
| `knowledge_evidence_write_blocked` | Knowledge and evidence writes remain blocked. |
| `runtime_control_blocked` | Runtime control actions remain blocked. |
| `all_operational_blocked` | All operational surfaces remain blocked. |
| `unknown` | Blocked surface posture is not safely known. |

## Recovery / Next Actions

| Recovery posture | Meaning |
| ---------------- | ------- |
| `none` | No recovery posture is asserted. |
| `refresh_license_lease` | Recovery depends on a newer lease posture. |
| `reenroll_machine` | Recovery depends on machine re-enrollment. |
| `reauthenticate` | Recovery depends on a new authentication context. |
| `reduce_usage` | Recovery depends on lower account-scoped usage pressure. |
| `wait_for_manual_review` | Recovery depends on manual review. |
| `retry_online` | Recovery depends on an online retry. |
| `contact_support` | Recovery depends on operator or support action. |
| `unknown` | Recovery posture is not safely known. |

| Next action | Meaning |
| ----------- | ------- |
| `none` | No next action is asserted. |
| `run_diagnostics` | Run diagnostics before retrying operations. |
| `refresh_license_lease` | Request refreshed lease posture. |
| `request_machine_enrollment` | Request machine enrollment or re-enrollment. |
| `reauthenticate` | Re-establish safe auth posture. |
| `retry_license_check` | Retry the runtime license check later. |
| `reduce_usage` | Reduce usage before retrying. |
| `contact_support` | Escalate to support or operator intervention. |
| `manual_review` | Wait for or trigger manual review. |
| `unknown` | Next action is not safely known. |

## Cache / Offline Grace Postures

| Cache posture | Meaning |
| ------------- | ------- |
| `not_applicable` | Cache posture is not relevant to current seal state. |
| `cache_current` | Cached posture is current. |
| `cache_stale` | Cached posture is stale. |
| `cache_expired` | Cached posture is expired. |
| `cache_invalidated` | Cached posture is invalidated. |
| `cache_update_required` | A later cache update would be required. |
| `unknown` | Cache posture is not safely known. |

| Offline grace posture | Meaning |
| --------------------- | ------- |
| `not_applicable` | Offline grace does not apply. |
| `available` | Offline grace could be used later. |
| `active` | Offline grace is currently active. |
| `expired` | Offline grace has expired. |
| `blocked` | Offline grace cannot be used. |
| `unknown` | Offline grace posture is not safely known. |

## Safe Status Projection

```text
seal_state
seal_reason
operational_readiness
diagnostic_posture
allowed_surface_posture
blocked_surface_posture
recovery_posture
next_action
response_freshness
warning_codes optional
```

## Behavior Rules

```text
sealed-by-license does not stop runtime
sealed-by-license does not imply service lifecycle stopped
runtime running does not imply unsealed
runtime healthy does not imply operational actions allowed
diagnostics may remain available while operational actions are sealed
operational/write actions must remain blocked when seal_state is sealed
response posture may inform seal state but does not itself enforce runtime
```

## E/V Boundary

```text
E/platform evaluates license posture and returns response.
V48 defines runtime behavior contract from response posture.
V48 does not implement enforcement, cache update, lease validation or entitlement evaluation.
V48 must not expose billing, subscription, raw hardware, provider identity or secrets.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| offline grace / stale lease behavior | V49 |
| logout / revocation / lease invalidation | V50 |
| API registry refactor | V51 |
| API case expansion | V52 |
| API auth surfaces | V53 |
