# Account-Scoped Limit Reconciliation

## Status

* Delivery: V45
* Status: active account-scoped limit reconciliation contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define how runtime consumes account-scoped limit reconciliation posture without
implementing counters or billing.

## Canonical Invariants

```text
account_limit_reconciliation.account_ref is required.
account_limit_reconciliation.limit_key is required.
account_limit_reconciliation.scope is required.
account_limit_reconciliation.reconciliation_status is required.
```

## Reconciliation Is Not

```text
usage accounting
quota ledger
billing/metering
plan/package object
runtime-owned account truth
```

## Shape

```text
account_limit_reconciliation_ref
account_ref
principal_ref optional
limit_projection_ref optional
limit_key
scope
subject_ref optional
machine_authorization_ref optional
local_machine_ref optional
license_lease_ref optional
runtime_gate_decision_ref optional
account_global_usage optional
local_observed_usage optional
remote_observed_usage optional
remaining optional
max_allowed optional
reconciliation_status
conflict_status
staleness_posture
offline_posture
cache_posture
decision
blocked_reason optional
warning_codes optional
observed_at optional
expires_at optional
safe_reconciliation_projection optional
```

## Scopes

| Scope | Meaning |
| ----- | ------- |
| `account_global` | Shared account-wide capacity across authorized machines and runtimes. |
| `principal` | Principal-scoped posture. |
| `machine` | Machine-local posture. |
| `case_tree` | Case hierarchy posture. |
| `case` | Single-case posture. |
| `runtime_instance` | Runtime-instance posture. |
| `team` | Team-scoped posture. |
| `organization` | Organization-scoped posture. |
| `system_internal` | Internal runtime posture. |

## Limit Keys

| Limit key | Meaning |
| --------- | ------- |
| `max_open_cases` | Maximum simultaneously open cases. |
| `max_active_cases` | Maximum active cases. |
| `max_nested_cases` | Maximum nested case depth or count. |
| `max_parallel_jobs` | Maximum parallel jobs. |
| `max_active_flows` | Maximum active flows. |
| `max_concurrent_agents` | Maximum concurrent agents. |
| `max_provider_calls` | Maximum provider calls in scope. |
| `max_knowledge_writes` | Maximum knowledge writes. |
| `max_evidence_writes` | Maximum evidence writes. |
| `max_authorized_machines` | Maximum authorized machines sharing account capacity. |
| `max_runtime_actions` | Maximum governed runtime actions. |
| `cloud_compute_minutes` | Cloud compute time posture. |

## Reconciliation Statuses

| Reconciliation status | Meaning |
| --------------------- | ------- |
| `not_reconciled` | No safe reconciliation posture is available yet. |
| `reconciled` | Local runtime has a safe reconciled posture. |
| `reconciled_with_warnings` | Runtime has a safe posture with warning conditions. |
| `stale_local` | Local posture is stale relative to expected account truth. |
| `requires_refresh` | Runtime requires a future refresh before relying on posture operationally. |
| `conflict_detected` | Runtime observed conflicting local and remote-safe postures. |
| `blocked` | Runtime must treat the posture as blocked. |
| `unknown` | Runtime cannot classify reconciliation posture safely. |

## Conflict / Staleness / Offline / Cache Postures

### Conflict Statuses

| Conflict status | Meaning |
| --------------- | ------- |
| `none` | No safe conflict is observed. |
| `local_exceeds_remote` | Local observed usage is higher than remote-safe posture. |
| `remote_exceeds_local` | Remote-safe posture is higher than local observed usage. |
| `machine_mismatch` | Machine-related posture does not align safely. |
| `lease_mismatch` | Lease-related posture does not align safely. |
| `cache_mismatch` | Cached posture does not align safely with current observations. |
| `requires_manual_review` | Runtime can only classify the conflict as requiring review. |
| `unknown` | Conflict status is not known safely. |

### Staleness Postures

| Staleness posture | Meaning |
| ----------------- | ------- |
| `fresh` | Reconciliation posture is current enough for safe consumption. |
| `stale` | Reconciliation posture is stale. |
| `stale_accepted` | Runtime accepts stale posture temporarily. |
| `stale_requires_refresh` | Runtime requires refresh because posture is stale. |
| `stale_rejected` | Runtime rejects stale posture operationally. |
| `unknown` | Staleness posture is not known safely. |

### Offline Postures

| Offline posture | Meaning |
| --------------- | ------- |
| `online` | Runtime is operating with online-safe posture. |
| `offline_allowed` | Offline posture is allowed in a bounded way. |
| `offline_limited` | Offline posture is limited and cannot create independent quota. |
| `offline_blocked` | Offline posture cannot be used safely. |
| `offline_requires_refresh` | Offline posture requires future refresh before safe use. |
| `unknown` | Offline posture is not known safely. |

### Cache Postures

| Cache posture | Meaning |
| ------------- | ------- |
| `cache_not_used` | No local cache posture contributed to reconciliation. |
| `cache_current` | Cache posture contributed and remains current enough for safe consumption. |
| `cache_stale` | Cache posture contributed but is stale. |
| `cache_expired` | Cache posture contributed but is expired. |
| `cache_invalidated` | Cache posture contributed but was invalidated by another condition. |
| `unknown` | Cache posture is not known safely. |

## Decisions / Blocked Reasons / Warning Codes

### Decisions

| Decision | Meaning |
| -------- | ------- |
| `allowed` | Runtime may proceed within safe reconciled posture. |
| `warning` | Runtime may proceed with visible warning posture. |
| `blocked` | Runtime must block operational use. |
| `requires_refresh` | Runtime requires fresh reconciliation posture before use. |
| `requires_online_check` | Runtime requires an online-safe check before use. |
| `requires_manual_review` | Runtime requires manual review before safe use. |
| `unknown` | Runtime cannot decide safely. |

### Blocked Reasons

| Blocked reason | Meaning |
| -------------- | ------- |
| `limit_exceeded` | Observed usage is beyond allowed posture. |
| `quota_exhausted` | Shared capacity has been exhausted. |
| `missing_limit_projection` | No safe limit projection is available. |
| `stale_limit_projection` | The available limit projection is too stale for safe use. |
| `account_global_limit_exceeded` | Shared account-global capacity is exhausted across machines or runtimes. |
| `machine_mismatch` | Machine-related posture prevents safe reconciliation use. |
| `license_lease_required` | Separate lease posture is required. |
| `license_lease_expired` | Lease posture is expired. |
| `machine_authorization_required` | Separate machine authorization posture is required. |
| `online_check_required` | Online-safe check is required before use. |
| `manual_review_required` | Manual review is required before use. |
| `unsafe_projection` | Available projection is not safe to consume. |
| `unknown` | No narrower safe blocked reason is available. |

### Warning Codes

| Warning code | Meaning |
| ------------ | ------- |
| `near_limit` | Shared capacity is nearing an operational threshold. |
| `stale_projection` | Runtime is relying on stale but still exposed posture. |
| `offline_limited` | Offline posture is limited. |
| `refresh_recommended` | A refresh is recommended soon. |
| `machine_limit_pressure` | Pressure is shared across multiple authorized machines. |
| `cache_used` | Local cache posture influenced the reconciliation. |
| `unknown` | No narrower safe warning is available. |

## Safe Reconciliation Projection

```text
account_ref
limit_key
scope
reconciliation_status
staleness_posture
offline_posture
cache_posture
decision
warning_codes optional
expires_at optional
```

## Account-global Sharing Rule

```text
authorized machines and runtime instances do not multiply account capacity.
local cached limits do not create independent quota.
runtime instances do not create independent quota universes.
analytics may summarize limit pressure but does not evaluate limits.
```

## E/V Boundary

```text
E owns entitlement, plan/package, account-global source-of-truth limits and
billing/package semantics.
V consumes safe limit reconciliation posture.
V does not mutate E usage records, quota ledgers or billing objects.
V must not infer pricing, billing, subscription or plan objects from
limit_projection_ref.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| runtime license check request | V46 |
| runtime license check response | V47 |
| sealed-by-license behavior | V48 |
| offline grace / stale lease behavior | V49 |
| logout / revocation / lease invalidation | V50 |
