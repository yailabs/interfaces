# Runtime License Check Response

## Status

* Delivery: V47
* Status: active runtime license check response contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define what E/platform may return to runtime after a license check request.

## Canonical Invariants

```text
runtime_license_check_response.runtime_license_check_response_ref is required.
runtime_license_check_response.runtime_license_check_request_ref is required.
runtime_license_check_response.decision is required.
runtime_license_check_response.reason is required.
runtime_license_check_response.responded_at is required.
```

## Response Is Not

```text
runtime enforcement
local cache persistence
billing/subscription object
provider/auth user object
session
```

## Shape

```text
runtime_license_check_response_ref
runtime_license_check_request_ref
decision
reason
blocked_reason optional
next_action
response_freshness
lease_posture
machine_authorization_posture
entitlement_posture
limit_posture
runtime_gate_posture
offline_grace_posture
cache_update_posture
responded_at
expires_at optional
refresh_after optional
safe_license_lease_projection optional
safe_machine_authorization_projection optional
safe_limit_projection optional
safe_runtime_gate_decision optional
warning_codes optional
```

## Decisions

| Decision | Meaning |
| -------- | ------- |
| `allowed` | Runtime received a safe allowed posture. |
| `blocked` | Runtime received a safe blocked posture. |
| `degraded` | Runtime received a degraded but still classified posture. |
| `diagnostics_only` | Runtime received a diagnostics-only posture. |
| `manual_review_required` | Runtime received a manual review posture. |
| `refresh_required` | Runtime received a refresh-required posture. |
| `unknown` | Runtime cannot classify the response safely. |

## Blocked Reasons

| Blocked reason | Meaning |
| -------------- | ------- |
| `missing_auth_context` | Auth context posture is missing. |
| `missing_machine_authorization` | Machine authorization posture is missing. |
| `machine_authorization_revoked` | Machine authorization posture is revoked. |
| `machine_authorization_expired` | Machine authorization posture is expired. |
| `missing_license_lease` | License lease posture is missing. |
| `license_lease_expired` | License lease posture is expired. |
| `license_lease_revoked` | License lease posture is revoked. |
| `license_lease_stale` | License lease posture is stale. |
| `entitlement_missing` | Entitlement posture is missing. |
| `limit_exceeded` | Limit posture is beyond a safe threshold. |
| `runtime_gate_blocked` | Runtime gate posture is blocked. |
| `online_check_required` | Online-safe check is required before use. |
| `manual_review_required` | Manual review is required before use. |
| `unsafe_projection` | The available projection is not safe to consume. |
| `unknown` | No narrower safe blocked reason is available. |

## Next Actions

| Next action | Meaning |
| ----------- | ------- |
| `none` | No immediate next action is implied by this posture. |
| `refresh_license_lease` | A future lease refresh path is indicated. |
| `reenroll_machine` | Machine re-enrollment posture is indicated. |
| `reauthenticate` | Auth posture must be renewed externally. |
| `reduce_usage` | Runtime should reduce usage posture later. |
| `retry_later` | Runtime should retry later. |
| `contact_support` | Support or operator review is indicated. |
| `diagnostics_only` | Only diagnostics-oriented follow-up is indicated. |
| `manual_review` | Manual review flow is indicated. |
| `unknown` | No narrower safe next action is available. |

## Response Freshness

| Response freshness | Meaning |
| ------------------ | ------- |
| `fresh` | Response posture is fresh enough for safe consumption. |
| `stale` | Response posture is stale. |
| `expired` | Response posture is expired. |
| `unknown` | Runtime cannot classify response freshness safely. |

## Lease / Machine / Entitlement / Limit / Gate Postures

### Lease Postures

| Lease posture | Meaning |
| ------------- | ------- |
| `valid` | Lease posture is valid. |
| `missing` | Lease posture is missing. |
| `expired` | Lease posture is expired. |
| `revoked` | Lease posture is revoked. |
| `stale` | Lease posture is stale. |
| `refresh_required` | Lease posture requires future refresh. |
| `grace_active` | Lease posture is in grace. |
| `unknown` | Lease posture is not known safely. |

### Machine Authorization Postures

| Machine authorization posture | Meaning |
| ----------------------------- | ------- |
| `authorized` | Machine authorization posture is authorized. |
| `missing` | Machine authorization posture is missing. |
| `pending` | Machine authorization posture is pending. |
| `revoked` | Machine authorization posture is revoked. |
| `expired` | Machine authorization posture is expired. |
| `blocked` | Machine authorization posture is blocked. |
| `unknown` | Machine authorization posture is not known safely. |

### Entitlement Postures

| Entitlement posture | Meaning |
| ------------------- | ------- |
| `entitled` | Entitlement posture is present. |
| `missing` | Entitlement posture is missing. |
| `expired` | Entitlement posture is expired. |
| `blocked` | Entitlement posture is blocked. |
| `unknown` | Entitlement posture is not known safely. |

### Limit Postures

| Limit posture | Meaning |
| ------------- | ------- |
| `within_limit` | Limit posture is inside safe range. |
| `near_limit` | Limit posture is nearing a threshold. |
| `limit_exceeded` | Limit posture is beyond safe range. |
| `stale_projection` | Limit posture depends on stale projection. |
| `unknown` | Limit posture is not known safely. |

### Runtime Gate Postures

| Runtime gate posture | Meaning |
| -------------------- | ------- |
| `gate_allowed` | Runtime gate posture is allowed. |
| `gate_blocked` | Runtime gate posture is blocked. |
| `gate_degraded` | Runtime gate posture is degraded. |
| `gate_unknown` | Runtime gate posture is not known safely. |

## Offline Grace / Cache Update Postures

### Offline Grace Postures

| Offline grace posture | Meaning |
| --------------------- | ------- |
| `not_applicable` | No offline grace posture applies. |
| `available` | Offline grace may be available. |
| `active` | Offline grace is active. |
| `expired` | Offline grace is expired. |
| `blocked` | Offline grace is blocked. |
| `unknown` | Offline grace posture is not known safely. |

### Cache Update Postures

| Cache update posture | Meaning |
| -------------------- | ------- |
| `no_cache_update` | No cache update posture is implied. |
| `cache_update_allowed` | Cache update may be allowed later. |
| `cache_update_required` | Cache update is required later. |
| `cache_invalidate_required` | Cache invalidation is required later. |
| `cache_update_blocked` | Cache update is blocked. |
| `unknown` | Cache update posture is not known safely. |

## Safe Response Rules

```text
response may include safe projections only
response must not include raw hardware identity
response must not include raw fingerprint
response must not include provider identity
response must not include billing/subscription/invoice/price objects
response must not include secrets/private keys
response must not include full account profile
response does not itself enforce runtime behavior
response does not itself update local cache
response does not itself mutate E records
```

## Response / Enforcement Split

```text
V47 defines response contract only.
V47 does not implement runtime sealed behavior.
V48 defines sealed-by-license behavior.
```

## E/V Boundary

```text
E/platform evaluates and returns response.
V consumes safe response posture later.
V47 does not implement enforcement, cache update, lease validation or runtime gate application.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| sealed-by-license behavior | V48 |
| offline grace / stale lease behavior | V49 |
| logout / revocation / lease invalidation | V50 |
