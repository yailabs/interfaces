# Logout / Revocation / Lease Invalidation

## Status

* Delivery: V50
* Status: active invalidation behavior contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define runtime invalidation posture for logout, revocation and lease invalidation.

## Canonical Invariants

```text
runtime_invalidation_event.invalidation_kind is required.
runtime_invalidation_event.invalidation_reason is required.
runtime_invalidation_event.seal_state is required.
runtime_invalidation_event.operational_readiness is required.
```

## Invalidation Is Not

```text
runtime stop
case deletion
evidence deletion
knowledge deletion
session
billing/subscription
```

## Shape

```text
runtime_invalidation_event_ref
invalidation_kind
invalidation_reason
affected_refs
auth_context_ref optional
license_lease_ref optional
machine_authorization_ref optional
local_machine_ref optional
local_machine_identity_ref optional
local_lease_cache_ref optional
runtime_license_check_response_ref optional
runtime_gate_decision_ref optional
seal_state
operational_readiness
diagnostic_posture
cache_invalidation_posture
lease_invalidation_posture
machine_authorization_posture
logout_posture
preservation_posture
recovery_posture
next_action
warning_codes optional
safe_invalidation_projection optional
```

## Invalidation Kinds / Reasons

| Invalidation kind | Meaning |
| ----------------- | ------- |
| `logout` | Auth/logout posture invalidates operational readiness. |
| `machine_authorization_revoked` | Machine authorization posture is revoked. |
| `machine_authorization_expired` | Machine authorization posture is expired. |
| `license_lease_revoked` | License lease posture is revoked. |
| `license_lease_expired` | License lease posture is expired. |
| `cache_invalidated` | Local cache posture is invalidated. |
| `auth_context_expired` | Auth context posture has expired. |
| `policy_invalidated` | Governing policy invalidates current posture. |
| `manual_admin_revocation` | Admin revocation invalidates current posture. |
| `unknown` | Invalidation kind is not safely known. |

| Invalidation reason | Meaning |
| ------------------- | ------- |
| `user_logout` | User-triggered logout posture. |
| `provider_logout` | Provider or remote auth logout posture. |
| `auth_context_expired` | Auth context expired under policy. |
| `machine_revoked` | Machine authorization was revoked. |
| `machine_expired` | Machine authorization expired. |
| `lease_revoked` | License lease was revoked. |
| `lease_expired` | License lease expired. |
| `lease_stale_rejected` | Stale lease posture was rejected. |
| `cache_expired` | Cache posture expired. |
| `cache_corrupt` | Cache posture is corrupt or unsafe. |
| `runtime_gate_blocked` | Runtime gate posture blocks further use. |
| `account_disabled` | Account-level policy disabled the current posture. |
| `manual_review_required` | Manual review is required. |
| `admin_revocation` | Admin revocation is the governing reason. |
| `unsafe_projection` | Provided posture is unsafe to consume. |
| `unknown` | Invalidation reason is not safely known. |

## Seal / Operational / Diagnostic Postures

| Seal state | Meaning |
| ---------- | ------- |
| `unsealed` | No operational seal is asserted. |
| `sealed` | Operational surfaces remain sealed. |
| `partially_sealed` | Some bounded surfaces remain available while others are sealed. |
| `diagnostics_only` | Runtime remains diagnostic-only. |
| `unknown` | Seal posture is not safely known. |

| Operational readiness | Meaning |
| --------------------- | ------- |
| `ready` | Runtime may expose operational surfaces under current posture. |
| `blocked` | Runtime is not operationally ready for blocked surfaces. |
| `degraded` | Runtime may expose only degraded or bounded surfaces. |
| `diagnostics_only` | Runtime should remain diagnostics-only. |
| `unknown` | Operational readiness is not safely known. |

| Diagnostic posture | Meaning |
| ------------------ | ------- |
| `diagnostics_allowed` | Diagnostics may remain available. |
| `diagnostics_limited` | Diagnostics remain available in reduced form. |
| `diagnostics_blocked` | Diagnostics are blocked. |
| `unknown` | Diagnostic posture is not safely known. |

## Cache / Lease / Machine Authorization Postures

| Cache invalidation posture | Meaning |
| -------------------------- | ------- |
| `not_applicable` | Cache invalidation does not apply. |
| `cache_retained` | Cache is still present but not necessarily authoritative. |
| `cache_marked_invalid` | Cache is marked invalid. |
| `cache_requires_refresh` | Cache requires refreshed posture. |
| `cache_must_not_be_used` | Cache must not be used as authorization posture. |
| `unknown` | Cache invalidation posture is not safely known. |

| Lease invalidation posture | Meaning |
| -------------------------- | ------- |
| `not_applicable` | Lease invalidation does not apply. |
| `lease_retained` | Lease ref remains present without proving validity. |
| `lease_marked_invalid` | Lease posture is marked invalid. |
| `lease_revoked` | Lease posture is revoked. |
| `lease_expired` | Lease posture is expired. |
| `lease_must_not_be_used` | Lease must not be used for authorization posture. |
| `unknown` | Lease invalidation posture is not safely known. |

| Machine authorization posture | Meaning |
| ----------------------------- | ------- |
| `not_applicable` | Machine authorization posture does not apply. |
| `machine_authorization_retained` | Machine authorization ref remains present without proving validity. |
| `machine_authorization_revoked` | Machine authorization posture is revoked. |
| `machine_authorization_expired` | Machine authorization posture is expired. |
| `machine_authorization_pending_review` | Machine authorization requires review. |
| `machine_authorization_must_refresh` | Machine authorization requires refresh or re-enrollment. |
| `unknown` | Machine authorization posture is not safely known. |

## Logout / Preservation / Recovery / Next Actions

| Logout posture | Meaning |
| -------------- | ------- |
| `not_logout` | Event is not logout-driven. |
| `logout_clears_auth_context` | Logout clears auth posture. |
| `logout_preserves_cases` | Logout does not delete or close cases by default. |
| `logout_preserves_records` | Logout does not delete records/evidence by default. |
| `logout_requires_work_policy` | Logout must account for active work policy. |
| `logout_blocks_operational_actions` | Logout seals future operational actions. |
| `unknown` | Logout posture is not safely known. |

| Preservation posture | Meaning |
| -------------------- | ------- |
| `preserve_cases_records_evidence_knowledge` | Cases, records, evidence, and knowledge remain preserved. |
| `preserve_cases_only` | Cases are preserved but broader preservation is not asserted. |
| `requires_explicit_deletion_policy` | Destructive behavior requires a future explicit policy. |
| `not_applicable` | Preservation posture does not apply. |
| `unknown` | Preservation posture is not safely known. |

| Recovery posture | Meaning |
| ---------------- | ------- |
| `none` | No recovery posture is asserted. |
| `reauthenticate` | Recovery depends on re-authentication. |
| `refresh_license_lease` | Recovery depends on refreshed lease posture. |
| `reenroll_machine` | Recovery depends on machine enrollment or re-enrollment. |
| `retry_online_check` | Recovery depends on a new online check. |
| `contact_support` | Recovery depends on operator or support intervention. |
| `manual_review` | Recovery depends on manual review. |
| `unknown` | Recovery posture is not safely known. |

| Next action | Meaning |
| ----------- | ------- |
| `none` | No next action is asserted. |
| `run_diagnostics` | Run diagnostics before broader recovery steps. |
| `reauthenticate` | Re-establish safe auth posture. |
| `refresh_license_lease` | Refresh or request newer lease posture. |
| `request_machine_enrollment` | Request machine enrollment or re-enrollment. |
| `retry_license_check` | Retry the license check later. |
| `leave_active_case` | Leave active case before certain future actions. |
| `resolve_active_work` | Resolve active work before progressing. |
| `contact_support` | Escalate to support or operator action. |
| `manual_review` | Wait for or trigger manual review. |
| `unknown` | Next action is not safely known. |

## Safe Invalidation Projection

```text
invalidation_kind
invalidation_reason
seal_state
operational_readiness
diagnostic_posture
cache_invalidation_posture
lease_invalidation_posture
machine_authorization_posture
logout_posture
preservation_posture
recovery_posture
next_action
warning_codes optional
```

## Behavior Rules

```text
logout does not stop runtime by default
logout does not delete cases by default
logout does not delete records by default
logout does not delete evidence by default
logout does not delete knowledge by default
revocation seals operational actions but does not delete local identity by default
lease invalidation seals operational actions but does not delete case-bound work
diagnostics may remain available after logout/revocation/invalidation
cache invalidated means cache must not be used as authorization
```

## E/V Boundary

```text
E/platform owns revocation, machine authorization lifecycle and lease lifecycle.
V50 defines runtime invalidation posture.
V50 does not mutate E records.
V50 does not implement deletion/enforcement.
V50 must not expose billing, subscription, raw hardware, provider identity or secrets.
```

## Handoff

```text
V50 closes the machine authorization / license lease runtime boundary group.
V51 begins API registry refactor.
```
