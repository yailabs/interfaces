# Runtime License Check Request

## Status

* Delivery: V46
* Status: active runtime license check request contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define what runtime may send when requesting a license check.

## Canonical Invariants

```text
runtime_license_check_request.runtime_license_check_request_ref is required.
runtime_license_check_request.local_machine_ref is required.
runtime_license_check_request.request_kind is required.
runtime_license_check_request.check_scope is required.
runtime_license_check_request.requested_at is required.
```

## Request Is Not

```text
response
license issuance
lease validation
entitlement evaluation
billing/subscription
login
session
```

## Shape

```text
runtime_license_check_request_ref
request_kind
check_scope
request_context
request_freshness
connectivity_posture
privacy_posture
requested_at
local_machine_ref
runtime_instance_ref optional
local_machine_identity_ref optional
machine_authorization_ref optional
license_lease_ref optional
auth_context_ref optional
account_ref optional
principal_ref optional
entitlement_ref optional
limit_projection_refs optional
account_limit_reconciliation_ref optional
local_lease_cache_ref optional
runtime_gate_decision_ref optional
machine_fingerprint_evidence_ref optional
requested_actions optional
client_ref optional
next_expected_response
warning_codes optional
```

## Request Kinds

| Request kind | Meaning |
| ------------ | ------- |
| `initial_check` | Runtime is preparing an initial request posture. |
| `refresh_check` | Runtime is requesting a fresh external evaluation posture. |
| `revalidation_check` | Runtime is requesting revalidation of an existing safe posture. |
| `offline_grace_check` | Runtime is reporting offline grace posture for later evaluation. |
| `stale_cache_check` | Runtime is reporting stale cache posture for later evaluation. |
| `machine_authorization_check` | Runtime is requesting evaluation with machine authorization posture emphasis. |
| `limit_reconciliation_check` | Runtime is requesting evaluation with limit reconciliation posture emphasis. |
| `diagnostic_check` | Runtime is preparing a diagnostic-only request posture. |

## Check Scopes

| Check scope | Meaning |
| ----------- | ------- |
| `local_runtime` | Request applies to local runtime posture. |
| `machine` | Request applies to machine-scoped posture. |
| `account` | Request applies to account-scoped posture. |
| `principal` | Request applies to principal-scoped posture. |
| `case_tree` | Request applies to case hierarchy posture. |
| `provider_access` | Request applies to provider access posture. |
| `cloud_compute` | Request applies to cloud compute posture. |
| `release_update` | Request applies to release/update posture. |
| `system_internal` | Request applies to internal runtime posture. |

## Request Contexts

| Request context | Meaning |
| --------------- | ------- |
| `startup` | Request is prepared during runtime startup. |
| `runtime_restart` | Request is prepared after runtime restart posture. |
| `reboot_continuity` | Request is prepared after reboot continuity posture. |
| `terminal_resume` | Request is prepared after terminal resumption. |
| `before_operational_action` | Request is prepared before a governed action. |
| `scheduled_refresh` | Request is prepared as part of scheduled refresh posture. |
| `manual_refresh` | Request is prepared by operator or explicit manual flow. |
| `diagnostic` | Request is prepared for diagnostics only. |

## Freshness / Connectivity / Privacy Postures

### Request Freshness

| Request freshness | Meaning |
| ----------------- | ------- |
| `fresh` | Runtime is preparing a fresh request posture. |
| `stale` | Runtime is preparing a request from stale posture. |
| `expired` | Runtime is preparing a request from expired posture. |
| `unknown` | Runtime cannot classify freshness safely. |

### Connectivity Postures

| Connectivity posture | Meaning |
| -------------------- | ------- |
| `online` | Runtime is preparing the request from online posture. |
| `offline` | Runtime is preparing the request from offline posture only. |
| `degraded` | Runtime is preparing the request from degraded connectivity posture. |
| `unknown` | Connectivity posture is not known safely. |

### Privacy Postures

| Privacy posture | Meaning |
| --------------- | ------- |
| `safe_refs_only` | Request contains only safe references and posture. |
| `privacy_bounded_evidence` | Request references privacy-bounded evidence posture. |
| `no_raw_hardware` | Request explicitly excludes raw hardware identity. |
| `redacted` | Request uses redacted posture where detail is not safe to send. |
| `requires_review` | Request posture requires later privacy review. |
| `unknown` | Privacy posture is not known safely. |

## Next Expected Responses

| Next expected response | Meaning |
| ---------------------- | ------- |
| `runtime_license_check_response` | Runtime expects the future V47 response contract. |
| `diagnostic_only_response` | Runtime expects diagnostic-only response posture later. |
| `manual_review_response` | Runtime expects review-oriented response posture later. |
| `not_applicable` | No response posture is expected from this request shape. |
| `unknown` | Runtime cannot classify the expected response safely. |

## Safe Request Rules

```text
request may include safe refs and posture only
request must not include raw hardware identity
request must not include raw machine fingerprint
request must not include provider identity
request must not include billing/subscription/invoice/price objects
request must not include secrets/private keys
request must not include full account profile
request does not grant or deny authorization
request does not validate lease
request does not refresh lease
```

## Request / Response Split

```text
V46 defines request only.
V46 does not define allowed/blocked final response semantics.
V47 defines runtime license check response.
```

## E/V Boundary

```text
V prepares safe request posture.
E/platform evaluates and returns response later.
V46 does not evaluate entitlement, license, machine authorization or limits.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| runtime license check response | V47 |
| sealed-by-license behavior | V48 |
| offline grace / stale lease behavior | V49 |
| logout / revocation / lease invalidation | V50 |
