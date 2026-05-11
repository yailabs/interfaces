# Case / Job / Flow Limit Boundary

## Status

* Delivery: V36
* Status: active limit boundary contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define runtime-visible limit projections for cases, jobs, flows, agents and
provider calls.

## Canonical Invariants

```text
limit_projection.limit_key is required.
limit_projection.subject_ref is required.
limit_projection.scope is required.
```

## Limit Projection Is Not

```text
Limit projection is not billing.
Limit projection is not a meter ledger.
Limit projection is not a subscription object.
Limit projection is not a plan object.
```

## Shape

```text
limit_projection_ref
limit_key
limit_family
scope
subject_ref
case_ref optional
job_ref optional
flow_ref optional
agent_instance_ref optional
provider_ref optional
runtime_action_key optional
runtime_gate_decision_ref optional
entitlement_ref optional
machine_authorization_ref optional
license_lease_ref optional
window
current_usage optional
max_allowed optional
remaining optional
soft_limit optional
hard_limit optional
warning_threshold optional
decision
blocked_reason optional
observed_at
expires_at optional
source_ref optional
```

## Limit Families

| Limit family | Meaning |
| ------------ | ------- |
| `case` | Case-bound capacity posture. |
| `job` | Job concurrency or throughput posture. |
| `flow` | Flow coordination capacity posture. |
| `agent` | Agent admission or concurrency posture. |
| `provider_call` | Provider-call capacity posture. |
| `knowledge` | Knowledge write capacity posture. |
| `evidence` | Evidence write capacity posture. |
| `runtime_action` | Runtime action volume posture. |
| `machine` | Machine admission posture. |
| `release_update` | Release/update distribution posture. |
| `cloud_compute` | Cloud compute consumption posture. |
| `admin` | Administrative capacity posture. |

## Limit Scopes

| Limit scope | Meaning |
| ----------- | ------- |
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
| `max_release_downloads` | Maximum release/update downloads. |
| `cloud_compute_minutes` | Cloud compute time posture. |

## Windows

| Window | Meaning |
| ------ | ------- |
| `none` | No rolling window is applied. |
| `minute` | Minute-based posture window. |
| `hour` | Hour-based posture window. |
| `day` | Day-based posture window. |
| `week` | Week-based posture window. |
| `month` | Month-based posture window. |
| `billing_period` | Billing-period posture only; not a billing implementation. |
| `lease_period` | Lease-period posture. |
| `release_period` | Release/update period posture. |
| `custom` | Explicit custom window. |

## Decision Statuses

| Decision | Meaning |
| -------- | ------- |
| `allowed` | Observed posture is inside limit. |
| `warning` | Observed posture is nearing a threshold. |
| `blocked` | Observed posture is beyond an allowed threshold. |
| `requires_entitlement` | Entitlement posture is missing or required. |
| `requires_license_lease` | License lease posture is missing or required. |
| `requires_machine_authorization` | Machine authorization posture is missing or required. |
| `requires_limit_projection` | Runtime cannot continue safely without projection input. |
| `requires_manual_review` | Manual review is required before action. |
| `unknown` | Projection cannot be classified safely. |

## Blocked Reasons

| Blocked reason | Meaning |
| -------------- | ------- |
| `limit_exceeded` | Observed usage is beyond allowed posture. |
| `quota_exhausted` | Available capacity has been exhausted. |
| `missing_limit_projection` | No safe projection is available. |
| `missing_entitlement` | Entitlement posture is required but absent. |
| `license_lease_expired` | License posture is expired. |
| `machine_not_authorized` | Machine posture is not authorized. |
| `manual_review_required` | Review must occur before continuation. |
| `plan_package_unavailable` | Upstream package posture is unavailable to this runtime surface. |
| `billing_required_but_unavailable` | Billing-related posture is deferred and unavailable here. |
| `unknown` | No narrower safe reason is available. |

## Account-global Sharing Rule

```text
Account-scoped limits are shared across authorized machines and runtime
instances.
Authorized machines do not multiply account capacity.
Runtime instances do not create independent quota universes.
```

## Analytics Boundary

```text
analytics may summarize limit pressure.
analytics is not the limit source of truth.
analytics does not increment counters.
analytics does not grant or block actions.
```

## Billing / Metering Boundary

```text
limit_projection is not billing.
limit_projection is not a meter ledger.
limit_projection is not a subscription object.
V36 does not implement billing, metering, usage accounting or quota counters.
```

## E/V Boundary

```text
V may consume safe limit_projection.
V must not consume:
  pricing
  billing provider object
  Supabase user object
  account profile
  raw provider identity
  full commercial plan objects
  raw usage ledger
  invoice/subscription objects
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| local model/provider access boundary | V37 |
| cloud compute boundary | V38 |
| machine authorization consumption | V42 |
| license lease consumption | V43 |
| account-scoped limit reconciliation | V45 |
| runtime license check request/response | V46/V47 |
| SDK entitlement/license clients | V60 |
