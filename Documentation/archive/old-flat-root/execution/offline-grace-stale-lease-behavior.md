# Offline Grace / Stale Lease Behavior

## Status

* Delivery: V49
* Status: active offline grace / stale lease behavior contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define bounded offline grace and stale lease behavior.

## Canonical Invariants

```text
offline_grace_state.grace_status is required.
offline_grace_state.stale_lease_status is required.
offline_grace_state.operational_readiness is required.
offline_grace_state.allowed_surface_posture is required.
```

## Offline Grace Is Not

```text
offline-first product promise
permanent offline authorization
login
session
auth_context
billing/subscription
```

## Shape

```text
offline_grace_state_ref
license_lease_ref optional
local_lease_cache_ref optional
runtime_license_check_response_ref optional
machine_authorization_ref optional
local_machine_ref optional
grace_status
stale_lease_status
offline_status
connectivity_posture
operational_readiness
diagnostic_posture
allowed_surface_posture
blocked_surface_posture
refresh_posture
recovery_posture
next_action
grace_started_at optional
grace_expires_at optional
last_online_at optional
last_validated_at optional
warning_codes optional
safe_grace_projection optional
```

## Grace / Stale / Offline / Connectivity Postures

| Grace status | Meaning |
| ------------ | ------- |
| `not_applicable` | Offline grace does not apply to the current posture. |
| `grace_available` | Offline grace could become active under bounded policy. |
| `grace_active` | Offline grace is currently active under bounded policy. |
| `grace_expired` | Offline grace was available but has expired. |
| `grace_blocked` | Offline grace cannot be used. |
| `unknown` | Grace posture is not safely known. |

| Stale lease status | Meaning |
| ------------------ | ------- |
| `not_stale` | Lease posture is not stale. |
| `stale_accepted` | Stale lease posture remains temporarily acceptable. |
| `stale_limited` | Stale lease posture allows only bounded surfaces. |
| `stale_requires_refresh` | Stale lease posture requires refresh before broader use. |
| `stale_rejected` | Stale lease posture cannot be used. |
| `unknown` | Stale posture is not safely known. |

| Offline status | Meaning |
| -------------- | ------- |
| `online` | Runtime is currently online. |
| `offline` | Runtime is currently offline. |
| `degraded_connectivity` | Connectivity is partially degraded. |
| `connectivity_unknown` | Connectivity state is not safely known. |

| Connectivity posture | Meaning |
| -------------------- | ------- |
| `online_check_available` | An online check can be attempted. |
| `online_check_unavailable` | An online check cannot currently be attempted. |
| `retry_online_required` | Broader use depends on retrying online. |
| `offline_allowed` | Bounded offline use remains acceptable. |
| `offline_limited` | Only restricted offline use remains acceptable. |
| `offline_blocked` | Offline use is blocked. |
| `unknown` | Connectivity posture is not safely known. |

## Operational / Diagnostic / Surface Postures

| Operational readiness | Meaning |
| --------------------- | ------- |
| `ready` | Runtime may expose operational surfaces under current bounded posture. |
| `limited` | Runtime may expose only limited operational surfaces. |
| `blocked` | Runtime is not operationally ready for blocked surfaces. |
| `diagnostics_only` | Runtime should remain diagnostics-only. |
| `unknown` | Operational readiness is not safely known. |

| Diagnostic posture | Meaning |
| ------------------ | ------- |
| `diagnostics_allowed` | Diagnostics may remain available. |
| `diagnostics_limited` | Diagnostics remain available in reduced form. |
| `diagnostics_blocked` | Diagnostics are blocked. |
| `unknown` | Diagnostic posture is not safely known. |

| Allowed surface posture | Meaning |
| ----------------------- | ------- |
| `diagnostics_only` | Only diagnostic surfaces remain available. |
| `read_only_only` | Read-only surfaces remain available. |
| `limited_operational` | Limited operational surfaces remain available. |
| `operational_allowed` | Operational surfaces remain available under current bounded posture. |
| `none` | No allowed surface is asserted. |
| `unknown` | Allowed surface posture is not safely known. |

| Blocked surface posture | Meaning |
| ----------------------- | ------- |
| `none` | No blocked surface is asserted. |
| `new_jobs_blocked` | New jobs remain blocked. |
| `provider_actions_blocked` | Provider-facing actions remain blocked. |
| `agent_flow_job_blocked` | Agent, flow, or job actions remain blocked. |
| `knowledge_evidence_write_blocked` | Knowledge and evidence writes remain blocked. |
| `runtime_control_blocked` | Runtime control actions remain blocked. |
| `all_operational_blocked` | All operational surfaces remain blocked. |
| `unknown` | Blocked surface posture is not safely known. |

## Refresh / Recovery / Next Actions

| Refresh posture | Meaning |
| --------------- | ------- |
| `not_required` | No refresh posture is asserted. |
| `recommended` | Refresh is recommended but not strictly required for current bounded posture. |
| `required` | Refresh is required before broader use. |
| `pending` | Refresh is pending. |
| `failed` | Refresh previously failed. |
| `blocked` | Refresh cannot currently proceed. |
| `unknown` | Refresh posture is not safely known. |

| Recovery posture | Meaning |
| ---------------- | ------- |
| `none` | No recovery posture is asserted. |
| `retry_online` | Recovery depends on retrying online. |
| `refresh_license_lease` | Recovery depends on refreshed lease posture. |
| `reauthenticate` | Recovery depends on re-authentication. |
| `reenroll_machine` | Recovery depends on machine re-enrollment. |
| `wait_for_connectivity` | Recovery depends on improved connectivity. |
| `diagnostics_only` | Recovery remains bounded to diagnostics. |
| `contact_support` | Recovery depends on operator or support action. |
| `unknown` | Recovery posture is not safely known. |

| Next action | Meaning |
| ----------- | ------- |
| `none` | No next action is asserted. |
| `continue_limited` | Continue only with bounded surfaces. |
| `run_diagnostics` | Run diagnostics before retrying operations. |
| `retry_online_check` | Retry an online check later. |
| `refresh_license_lease` | Refresh or request fresher lease posture. |
| `reauthenticate` | Re-establish safe auth posture. |
| `request_machine_enrollment` | Request machine enrollment or re-enrollment. |
| `contact_support` | Escalate to support or operator action. |
| `unknown` | Next action is not safely known. |

## Safe Grace Projection

```text
grace_status
stale_lease_status
offline_status
operational_readiness
diagnostic_posture
allowed_surface_posture
blocked_surface_posture
refresh_posture
next_action
grace_expires_at optional
warning_codes optional
```

## Behavior Rules

```text
offline grace is bounded
offline grace is not offline-first product promise
offline grace is not permanent offline authorization
stale lease is not valid lease
stale lease may allow diagnostics or limited operation only if policy allows
grace active does not imply all runtime actions allowed
diagnostics may remain available while offline/stale/expired
operational/write actions may be limited or blocked
```

## E/V Boundary

```text
E/platform defines grace policy and lease lifecycle.
V49 defines runtime behavior contract for safe grace/stale posture.
V49 does not implement connectivity checks, refresh, enforcement, cache update
or lease validation.
V49 must not expose billing, subscription, raw hardware, provider identity or secrets.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| logout / revocation / lease invalidation | V50 |
| API registry refactor | V51 |
| API case expansion | V52 |
| API auth surfaces | V53 |
