# License Lease Consumption

## Status

* Delivery: V43
* Status: active license lease consumption contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define how V/runtime consumes safe license lease posture.

## Canonical Invariants

```text
license_lease_consumption.license_lease_ref is required.
license_lease_consumption.lease_status is required.
license_lease_consumption.consumption_status is required.
license_lease_consumption.scope is required.
```

## License Lease Consumption Is Not

```text
lease issuance
entitlement evaluation
machine authorization
auth_context
login
session
billing/subscription
```

## Shape

```text
license_lease_consumption_ref
license_lease_ref
lease_status
consumption_status
scope
lease_source
grace_posture
stale_posture
refresh_posture
revocation_posture
diagnostic_posture
sealed_posture
issued_at optional
expires_at optional
last_validated_at optional
consumed_at optional
account_ref optional
principal_ref optional
auth_context_ref optional
entitlement_ref optional
machine_authorization_ref optional
local_machine_ref optional
runtime_gate_decision_ref optional
limit_projection_ref optional
blocked_reason optional
warning_codes optional
safe_lease_projection optional
```

## Lease Statuses

| Lease status | Meaning |
| ------------ | ------- |
| `not_present` | No safe lease posture is available. |
| `valid` | Safe lease posture is present for runtime consumption. |
| `expired` | Lease posture expired. |
| `revoked` | Lease posture was revoked by E/platform policy. |
| `stale` | Only a stale safe lease projection is available. |
| `pending_refresh` | Lease posture exists but requires future refresh handling. |
| `blocked` | Lease posture is blocked pending another requirement or policy. |
| `unknown` | Runtime cannot classify lease posture safely. |

## Consumption Statuses

| Consumption status | Meaning |
| ------------------ | ------- |
| `not_consumed` | Runtime has not consumed the lease posture yet. |
| `consumed` | Runtime consumes the safe lease posture. |
| `consumed_readonly` | Runtime only consumes the posture for read-only surfaces. |
| `diagnostics_only` | Only diagnostic surfaces remain available from the posture. |
| `blocked` | Runtime consumption is blocked for operational use. |
| `grace_active` | Runtime consumes a grace-window lease posture only. |
| `stale_accepted` | Runtime accepts a stale safe lease projection temporarily. |
| `stale_rejected` | Runtime rejects the stale lease posture for operational use. |
| `unknown` | Consumption status is not known safely. |

## Scopes

| Scope | Meaning |
| ----- | ------- |
| `local_runtime` | Lease scope applies to local runtime posture. |
| `account_linked_runtime` | Lease scope is tied to account-linked runtime posture. |
| `machine` | Lease scope applies to machine posture. |
| `principal` | Lease scope applies to principal posture. |
| `case_tree` | Lease scope may apply to a governed case tree. |
| `provider_access` | Lease scope may influence future provider access posture. |
| `cloud_compute` | Lease scope may influence future cloud-compute posture. |
| `release_update` | Lease scope covers release/update posture only. |
| `system_internal` | Scope is internal to system/runtime posture only. |

## Lease Sources

| Lease source | Meaning |
| ------------ | ------- |
| `platform_issued` | Safe lease posture originates from E/platform-issued lease policy. |
| `cached_projection` | Runtime consumes a cached safe lease projection only. |
| `manual_preview` | Safe lease posture is a non-authoritative preview surface. |
| `admin_override` | Safe lease posture reflects a future override relation without exposing internals. |
| `not_applicable` | No source applies to the current posture. |
| `unknown` | Lease source is not known safely. |

## Grace / Stale / Refresh / Revocation Postures

### Grace Postures

| Grace posture | Meaning |
| ------------- | ------- |
| `not_applicable` | No grace window applies to the posture. |
| `grace_available` | Grace may be available if expiry or validation conditions are met. |
| `grace_active` | Runtime observes an active grace posture. |
| `grace_expired` | Grace posture existed but is no longer active. |
| `grace_blocked` | Grace posture cannot be used safely. |
| `unknown` | Grace posture is not known safely. |

### Stale Postures

| Stale posture | Meaning |
| ------------- | ------- |
| `not_stale` | Lease posture is not stale. |
| `stale_accepted` | Runtime accepts a stale safe projection temporarily. |
| `stale_rejected` | Runtime rejects the stale safe projection operationally. |
| `stale_requires_refresh` | Stale posture requires a future refresh path. |
| `unknown` | Stale posture is not known safely. |

### Refresh Postures

| Refresh posture | Meaning |
| --------------- | ------- |
| `not_required` | No refresh is currently required. |
| `refresh_available` | A future refresh path may be available. |
| `refresh_required` | Refresh is required before operational use can continue. |
| `refresh_pending` | Refresh is pending in an external lifecycle. |
| `refresh_failed` | Refresh was attempted externally and failed. |
| `unknown` | Refresh posture is not known safely. |

### Revocation Postures

| Revocation posture | Meaning |
| ------------------ | ------- |
| `not_revoked` | No revocation posture is observed. |
| `revoked` | Lease posture is revoked. |
| `revocation_pending` | Revocation posture may be pending externally. |
| `revocation_unknown` | Revocation posture cannot be classified safely. |
| `unknown` | Revocation posture is not known safely. |

## Diagnostic / Sealed Postures

### Diagnostic Postures

| Diagnostic posture | Meaning |
| ------------------ | ------- |
| `diagnostics_allowed` | Diagnostic surfaces may remain available. |
| `diagnostics_limited` | Only limited diagnostic surfaces remain available. |
| `diagnostics_blocked` | Diagnostic surfaces are blocked. |
| `unknown` | Diagnostic posture is not known safely. |

### Sealed Postures

| Sealed posture | Meaning |
| -------------- | ------- |
| `unsealed_for_authorized_actions` | Authorized actions can proceed when other requirements are met. |
| `sealed_missing_lease` | Operational posture remains sealed because lease posture is missing. |
| `sealed_expired_lease` | Operational posture remains sealed because lease posture expired. |
| `sealed_revoked_lease` | Operational posture remains sealed because lease posture was revoked. |
| `sealed_stale_lease` | Operational posture remains sealed because only stale lease posture is available. |
| `sealed_refresh_required` | Operational posture remains sealed until a future refresh path succeeds. |
| `sealed_unknown` | Sealed posture is not known safely. |

## Blocked Reasons

| Blocked reason | Meaning |
| -------------- | ------- |
| `license_lease_missing` | Runtime cannot consume lease posture because it is missing. |
| `license_lease_expired` | Runtime cannot consume lease posture operationally because it expired. |
| `license_lease_revoked` | Runtime cannot consume lease posture operationally because it was revoked. |
| `license_lease_stale` | Runtime cannot consume lease posture operationally because only stale projection is available. |
| `refresh_required` | A future refresh path is required before operational use. |
| `machine_authorization_required` | A separate machine authorization posture is required. |
| `machine_authorization_revoked` | A separate machine authorization posture was revoked. |
| `entitlement_missing` | A separate entitlement posture is missing. |
| `runtime_gate_blocked` | A separate runtime gate blocks operational use. |
| `unsafe_projection` | The available projection is not safe to consume. |
| `unknown` | Blocked reason is not known safely. |

## Safe Lease Projection

```text
license_lease_ref
lease_status
consumption_status
scope
grace_posture
stale_posture
refresh_posture
diagnostic_posture
sealed_posture
expires_at optional
warning_codes optional
```

## Distinction Rules

```text
license lease consumption is not issuance
license lease consumption is not entitlement evaluation
license lease consumption is not machine authorization
license lease consumption is not auth_context
license lease consumption is not login
license lease consumption is not session
valid license lease does not imply all runtime actions allowed
valid license lease does not imply billing/subscription status
valid license lease does not expose plan/package objects
```

## E/V Boundary

```text
E issues and owns license lease policy and lifecycle.
V consumes safe license lease posture.
V does not mutate E lease records.
V does not infer pricing, billing, subscription or plan objects from
license_lease_ref.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| local lease cache / reboot continuity | V44 |
| account-scoped limit reconciliation | V45 |
| runtime license check request | V46 |
| runtime license check response | V47 |
| sealed-by-license behavior | V48 |
| offline grace / stale lease behavior | V49 |
| logout / revocation / lease invalidation | V50 |
