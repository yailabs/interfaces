# Machine Authorization Consumption

## Status

* Delivery: V42
* Status: active machine authorization consumption contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define how V/runtime consumes safe machine authorization posture.

## Canonical Invariants

```text
machine_authorization_consumption.machine_authorization_ref is required.
machine_authorization_consumption.local_machine_ref is required.
machine_authorization_consumption.authorization_status is required.
machine_authorization_consumption.consumption_status is required.
```

## Machine Authorization Consumption Is Not

```text
authorization issuance
enrollment approval
license lease
auth_context
login
session
hardware fingerprinting
```

## Shape

```text
machine_authorization_consumption_ref
machine_authorization_ref
local_machine_ref
local_machine_identity_ref optional
authorization_status
consumption_status
authorization_scope
authorization_source
lease_requirement_posture
diagnostic_posture
sealed_posture
consumed_at optional
expires_at optional
account_ref optional
principal_ref optional
auth_context_ref optional
license_lease_ref optional
runtime_gate_decision_ref optional
limit_projection_ref optional
blocked_reason optional
warning_codes optional
safe_status_projection optional
```

## Authorization Statuses

| Authorization status | Meaning |
| -------------------- | ------- |
| `not_present` | No safe machine authorization posture is available. |
| `pending` | Authorization posture exists but is not yet usable for operational access. |
| `authorized` | Safe authorization posture is present for runtime consumption. |
| `revoked` | Authorization posture was revoked by E/platform. |
| `expired` | Authorization posture expired. |
| `blocked` | Authorization posture is blocked pending a future dependency or policy. |
| `unknown` | Runtime cannot classify authorization posture safely. |

## Consumption Statuses

| Consumption status | Meaning |
| ------------------ | ------- |
| `not_consumed` | Runtime has not consumed the posture yet. |
| `consumed` | Runtime consumes the safe authorization posture. |
| `consumed_readonly` | Runtime only consumes the posture for read-only surfaces. |
| `diagnostics_only` | Only diagnostics remain available from the posture. |
| `blocked` | Runtime consumption is blocked for operational use. |
| `stale` | Runtime consumes a stale safe projection only. |
| `unknown` | Consumption status is not known safely. |

## Authorization Scopes

| Authorization scope | Meaning |
| ------------------- | ------- |
| `local_runtime` | Authorization scope applies to local runtime posture. |
| `account_linked_runtime` | Authorization scope is tied to an account-linked runtime posture. |
| `release_access` | Authorization scope covers release access posture only. |
| `update_access` | Authorization scope covers update access posture only. |
| `provider_access` | Authorization scope may influence future provider access posture. |
| `cloud_compute` | Authorization scope may influence future cloud-compute posture. |
| `system_internal` | Scope is internal to system/runtime posture only. |

## Authorization Sources

| Authorization source | Meaning |
| -------------------- | ------- |
| `platform_issued` | Safe posture originates from an E/platform-issued authorization. |
| `manual_preview` | Safe posture is a non-authoritative preview surface. |
| `admin_override` | Safe posture reflects a future override relation without exposing internals. |
| `cached_projection` | Runtime consumes a cached safe projection only. |
| `not_applicable` | No source applies to the current posture. |
| `unknown` | Authorization source is not known safely. |

## Lease Requirement Postures

| Lease requirement posture | Meaning |
| ------------------------- | ------- |
| `not_required` | No license lease is required for the current posture. |
| `required` | A license lease is required before operational use. |
| `present` | A separate license lease relation is observed. |
| `missing` | A required separate license lease relation is missing. |
| `expired` | A separate license lease relation is expired. |
| `refresh_required` | A separate license lease refresh is required. |
| `unknown` | Lease requirement posture is not known safely. |

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
| `sealed_missing_authorization` | Operational posture remains sealed because authorization is missing. |
| `sealed_revoked` | Operational posture remains sealed because authorization was revoked. |
| `sealed_expired` | Operational posture remains sealed because authorization expired. |
| `sealed_pending` | Operational posture remains sealed while authorization is pending. |
| `sealed_license_required` | Operational posture remains sealed until a separate license lease is satisfied. |
| `sealed_unknown` | Sealed posture is not known safely. |

## Blocked Reasons

| Blocked reason | Meaning |
| -------------- | ------- |
| `machine_authorization_missing` | Runtime cannot consume authorization because it is missing. |
| `machine_authorization_pending` | Runtime cannot consume authorization operationally because it is pending. |
| `machine_authorization_revoked` | Runtime cannot consume authorization operationally because it was revoked. |
| `machine_authorization_expired` | Runtime cannot consume authorization operationally because it expired. |
| `machine_authorization_blocked` | Runtime cannot consume authorization because it is blocked. |
| `license_lease_required` | A separate license lease requirement blocks operational use. |
| `license_lease_missing` | A required separate license lease relation is missing. |
| `runtime_gate_blocked` | A separate runtime gate blocks operational use. |
| `local_machine_mismatch` | The safe authorization posture does not match the local machine relation. |
| `unsafe_projection` | The available projection is not safe to consume. |
| `unknown` | Blocked reason is not known safely. |

## Safe Status Projection

```text
machine_authorization_ref
local_machine_ref
authorization_status
consumption_status
authorization_scope
diagnostic_posture
sealed_posture
expires_at optional
warning_codes optional
```

## Privacy Rules

```text
machine authorization consumption must not expose private E record internals
machine authorization consumption must not expose raw hardware identifiers
machine authorization consumption must not expose raw fingerprint material
machine authorization consumption must not expose provider identity
machine authorization consumption must not expose billing objects
machine authorization consumption must not expose secrets or private keys
```

## E/V Boundary

```text
E issues and owns machine_authorization_ref.
V consumes safe machine authorization posture.
V does not mutate E authorization records.
V does not infer billing, entitlement, license lease or plan state from
machine_authorization_ref alone.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| license lease consumption | V43 |
| local lease cache / reboot continuity | V44 |
| account-scoped limit reconciliation | V45 |
| runtime license check request/response | V46/V47 |
| sealed-by-license behavior | V48 |
| offline grace / stale lease behavior | V49 |
