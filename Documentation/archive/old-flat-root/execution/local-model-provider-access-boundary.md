# Local Model / Provider Access Boundary

## Status

* Delivery: V37
* Status: active provider/model access contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define governed access boundaries for local models, external providers, hosted
models and custom/fine-tuned models.

## Canonical Invariants

```text
model_access_decision.access_target is required.
model_access_decision.access_mode is required.
model_access_decision.case_ref is required for case-scoped provider/model work.
```

Model/provider access is governed by case, auth, gate, limit, and safe posture
refs when configured. Local model access is not automatically free, external
provider access is not free-floating, hosted model access is future/optional and
not live by default, custom/fine-tuned model access is future/optional and not
live by default, model outputs do not own evidence or knowledge, and provider
credentials must not enter V/core contracts.

## Access Targets

| Access target | Meaning |
| ------------- | ------- |
| `local_model` | Local runtime model surface. |
| `external_provider` | External provider surface. |
| `hosted_model` | Hosted model surface behind hosted/cloud posture. |
| `custom_model` | Custom model capability surface. |
| `fine_tuned_model` | Fine-tuned model capability surface. |
| `provider_status` | Diagnostic provider posture inspection. |
| `model_status` | Diagnostic model posture inspection. |

## Access Modes

| Access mode | Meaning |
| ----------- | ------- |
| `local_runtime` | Local runtime-bound model posture. |
| `user_owned_provider` | User-owned provider credential posture without exposing secrets here. |
| `platform_managed_provider` | Platform-managed provider posture without exposing credentials here. |
| `hosted_platform` | Hosted/cloud platform posture. |
| `offline_cached` | Offline-cached status posture only. |
| `diagnostic_status` | Diagnostic-only status posture. |

## Requested Actions

| Requested action | Meaning |
| ---------------- | ------- |
| `inspect_status` | Inspect access posture without invoking a model. |
| `load_local_model` | Request local model load posture. |
| `invoke_local_model` | Request local model invocation posture. |
| `invoke_external_provider` | Request external provider invocation posture. |
| `invoke_hosted_model` | Request hosted model invocation posture. |
| `invoke_custom_model` | Request custom/fine-tuned model invocation posture. |
| `embed` | Request embedding-style capability. |
| `rerank` | Request reranking capability. |
| `summarize` | Request summarization capability. |
| `classify` | Request classification capability. |
| `extract` | Request extraction capability. |
| `tool_call` | Request tool-mediated model/provider action. |

## Decision Statuses

| Decision | Meaning |
| -------- | ------- |
| `allowed` | Access is admitted under current posture. |
| `blocked` | Access is denied under current posture. |
| `degraded` | Access is partially available with reduced posture. |
| `diagnostic_allowed` | Diagnostic inspection is allowed. |
| `requires_auth` | Auth posture is required. |
| `requires_case` | Case boundary is required. |
| `requires_entitlement` | Entitlement posture is required. |
| `requires_machine_authorization` | Machine authorization posture is required. |
| `requires_license_lease` | License lease posture is required. |
| `requires_runtime_gate` | Runtime/cloud gate posture is required. |
| `requires_limit_capacity` | Safe limit posture blocks operational access. |
| `requires_provider_budget` | Safe provider budget posture is required. |
| `requires_credentials` | Credential posture is required. |
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
| `provider_budget_exceeded` | Safe provider budget posture has been exceeded. |
| `provider_not_configured` | Provider surface is not configured. |
| `credentials_missing` | Credentials are required but absent. |
| `credentials_forbidden` | Credential posture is forbidden at this boundary. |
| `model_not_available` | Requested model is unavailable. |
| `model_not_allowed` | Requested model is outside allowed posture. |
| `hosted_model_not_enabled` | Hosted model posture is not enabled. |
| `custom_model_not_implemented` | Custom/fine-tuned model posture is deferred. |
| `cloud_capacity_unavailable` | Hosted/cloud capacity is unavailable. |
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
| `output_redacted` | Output exists but is redacted. |
| `output_blocked` | Output is blocked and not exposed. |
| `diagnostic_only` | Diagnostic-only output posture. |

## Credential Boundary

| Credential boundary | Meaning |
| ------------------- | ------- |
| `no_credentials_required` | No credentials are required at this posture. |
| `user_owned_credentials_required` | User-owned credentials are required but not exposed here. |
| `platform_managed_credentials_required` | Platform-managed credentials are required but not exposed here. |
| `credentials_present_but_not_exposed` | Credentials may exist but remain outside V/core contracts. |
| `credentials_missing` | Required credentials are absent. |
| `credentials_forbidden` | Credentials must not appear at this boundary. |
| `not_applicable` | Credential posture does not apply. |

## Local / Offline Boundary

```text
local model execution may be local-first, but operational access may still be
online-authorized through license/machine/gate posture.
local does not mean unlimited.
offline cached model status does not imply operational authorization.
```

## E/V Boundary

```text
model/provider access may reference entitlement_ref, license_lease_ref,
machine_authorization_ref, runtime_gate_decision_ref, limit_projection_ref and
provider_budget_ref.
```

```text
model/provider access must not consume:
pricing
billing provider object
Supabase user object
account profile
raw provider identity
full commercial plan objects
raw usage ledger
invoice/subscription objects
provider secret material
```

## Billing / Metering Boundary

```text
Provider/model access may be limit-sensitive or budget-sensitive.
V37 does not implement billing, metering, quota accounting or provider budgets.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| cloud compute boundary | V38 |
| machine authorization consumption | V42 |
| license lease consumption | V43 |
| local lease cache / reboot continuity | V44 |
| runtime license check request/response | V46/V47 |
| SDK entitlement/license clients | V60 |
