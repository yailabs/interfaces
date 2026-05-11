# Local Lease Cache / Reboot Continuity

## Status

* Delivery: V44
* Status: active local lease cache boundary contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define safe local continuity posture for license leases across terminal close,
runtime restart and machine reboot.

## Canonical Invariants

```text
local_lease_cache.license_lease_ref is required.
local_lease_cache.cache_status is required.
local_lease_cache.continuity_status is required.
local_lease_cache.reboot_posture is required.
```

## Local Lease Cache Is Not

```text
lease issuance
lease validation
auth_context
login
session
billing/subscription
permanent offline authorization
```

## Shape

```text
local_lease_cache_ref
license_lease_ref
cache_status
continuity_status
reboot_posture
terminal_close_posture
runtime_restart_posture
offline_grace_posture
stale_posture
refresh_required_posture
invalidation_posture
cached_at optional
expires_at optional
last_validated_at optional
local_machine_ref optional
machine_authorization_ref optional
account_ref optional
principal_ref optional
entitlement_ref optional
runtime_gate_decision_ref optional
limit_projection_ref optional
blocked_reason optional
warning_codes optional
safe_cache_projection optional
```

## Cache Statuses

| Cache status | Meaning |
| ------------ | ------- |
| `not_cached` | No safe lease cache posture is available. |
| `cached` | A safe cached lease projection is available for runtime consumption. |
| `cache_unavailable` | Cache posture is unavailable to runtime. |
| `cache_corrupt` | Cache posture exists but cannot be consumed safely. |
| `cache_expired` | Cached lease posture is expired. |
| `cache_revoked` | Cached lease posture reflects revocation. |
| `cache_invalidated` | Cached lease posture was invalidated by another policy event. |
| `cache_stale` | Cached lease posture is stale and may require refresh. |
| `unknown` | Runtime cannot classify cache posture safely. |

## Continuity Statuses

| Continuity status | Meaning |
| ----------------- | ------- |
| `no_continuity` | No safe continuity posture is available. |
| `continuity_available` | Continuity posture may be available if other conditions are met. |
| `continuity_active` | Safe continuity posture is active for local use. |
| `continuity_limited` | Continuity posture exists but only in a limited form. |
| `continuity_blocked` | Continuity posture is blocked for operational use. |
| `continuity_requires_refresh` | Continuity posture exists but requires future refresh before operational use. |
| `unknown` | Continuity status is not known safely. |

## Reboot / Terminal / Restart Postures

### Reboot Postures

| Reboot posture | Meaning |
| -------------- | ------- |
| `not_applicable` | Reboot continuity does not apply to the current posture. |
| `survives_reboot` | Safe cache posture may survive reboot without becoming login or session state. |
| `does_not_survive_reboot` | Safe cache posture does not survive reboot. |
| `reboot_requires_refresh` | Safe cache posture after reboot requires refresh before operational use. |
| `reboot_blocked` | Reboot continuity is blocked. |
| `unknown` | Reboot posture is not known safely. |

### Terminal Close Postures

| Terminal close posture | Meaning |
| ---------------------- | ------- |
| `not_applicable` | Terminal close continuity does not apply to the current posture. |
| `survives_terminal_close` | Safe cache posture may survive terminal close. |
| `terminal_close_requires_refresh` | Terminal close continuity requires refresh before operational use. |
| `terminal_close_blocks_operations` | Terminal close continuity does not preserve operational posture. |
| `unknown` | Terminal close posture is not known safely. |

### Runtime Restart Postures

| Runtime restart posture | Meaning |
| ----------------------- | ------- |
| `not_applicable` | Runtime restart continuity does not apply to the current posture. |
| `survives_runtime_restart` | Safe cache posture may survive runtime restart. |
| `restart_requires_refresh` | Runtime restart continuity requires refresh before operational use. |
| `restart_blocks_operations` | Runtime restart continuity blocks operational posture. |
| `unknown` | Runtime restart posture is not known safely. |

## Offline Grace / Stale / Refresh / Invalidation Postures

### Offline Grace Postures

| Offline grace posture | Meaning |
| --------------------- | ------- |
| `not_applicable` | No offline grace posture applies. |
| `offline_grace_available` | Offline grace may be available if other conditions are met. |
| `offline_grace_active` | Offline grace is active for the cached posture. |
| `offline_grace_expired` | Offline grace existed but is no longer active. |
| `offline_grace_blocked` | Offline grace cannot be used safely. |
| `unknown` | Offline grace posture is not known safely. |

### Stale Postures

| Stale posture | Meaning |
| ------------- | ------- |
| `not_stale` | Cached posture is not stale. |
| `stale_accepted` | Runtime accepts stale cached posture temporarily. |
| `stale_requires_refresh` | Cached posture is stale and requires refresh. |
| `stale_rejected` | Runtime rejects stale cached posture operationally. |
| `unknown` | Stale posture is not known safely. |

### Refresh Required Postures

| Refresh required posture | Meaning |
| ------------------------ | ------- |
| `not_required` | No refresh is currently required. |
| `required` | Refresh is required before operational use can continue. |
| `pending` | Refresh is pending in an external lifecycle. |
| `failed` | Refresh was attempted externally and failed. |
| `blocked` | Refresh is blocked by another requirement or policy. |
| `unknown` | Refresh posture is not known safely. |

### Invalidation Postures

| Invalidation posture | Meaning |
| -------------------- | ------- |
| `not_invalidated` | No invalidation posture is observed. |
| `invalidated_by_revocation` | Cache posture is invalidated by lease revocation. |
| `invalidated_by_expiry` | Cache posture is invalidated by lease expiry. |
| `invalidated_by_logout` | Cache posture is invalidated by logout-adjacent boundary without becoming auth/login state. |
| `invalidated_by_machine_change` | Cache posture is invalidated by machine mismatch or machine change. |
| `invalidated_by_policy` | Cache posture is invalidated by another policy outcome. |
| `unknown` | Invalidation posture is not known safely. |

## Blocked Reasons

| Blocked reason | Meaning |
| -------------- | ------- |
| `lease_not_cached` | Runtime cannot consume continuity posture because no cache exists. |
| `lease_cache_corrupt` | Runtime cannot consume continuity posture because cache posture is corrupt. |
| `lease_cache_expired` | Runtime cannot consume continuity posture because cached lease is expired. |
| `lease_cache_revoked` | Runtime cannot consume continuity posture because cached lease is revoked. |
| `lease_cache_stale` | Runtime cannot consume continuity posture because cached lease is stale. |
| `refresh_required` | A future refresh path is required before operational use. |
| `machine_authorization_required` | A separate machine authorization posture is required. |
| `machine_mismatch` | Cache posture does not match the local machine relation safely. |
| `logout_invalidated` | Cache posture was invalidated by logout-adjacent boundary. |
| `policy_invalidated` | Cache posture was invalidated by policy. |
| `unsafe_projection` | The available projection is not safe to consume. |
| `unknown` | Blocked reason is not known safely. |

## Safe Cache Projection

```text
license_lease_ref
cache_status
continuity_status
reboot_posture
offline_grace_posture
stale_posture
refresh_required_posture
expires_at optional
warning_codes optional
```

## Distinction Rules

```text
local lease cache is not lease issuance
local lease cache is not lease validation
local lease cache is not auth_context
local lease cache is not login
local lease cache is not session
local lease cache is not billing/subscription
local lease cache is not permanent offline authorization
valid cache does not imply all runtime actions allowed
```

## E/V Boundary

```text
E owns lease policy, issuance, revocation and lifecycle.
V may consume safe cached lease posture.
V does not mutate E lease records.
V does not infer billing, subscription or plan objects from cached lease posture.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| account-scoped limit reconciliation | V45 |
| runtime license check request | V46 |
| runtime license check response | V47 |
| sealed-by-license behavior | V48 |
| offline grace / stale lease behavior | V49 |
| logout / revocation / lease invalidation | V50 |
