# Logout / Seal Policy

## Status

* Delivery: V28
* Status: active policy contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define logout policy when active cases, jobs or execution leases may exist.

## Canonical Rule

```text
logout is not detach.
logout is not runtime stop by default.
logout is not job cancellation by default.
```

Logout changes auth and control posture. It does not, by itself, destroy
case-bound work, close the active case, or delete durable state.

## Request Shape

The canonical logout request shape may include:

```text
logout_request_ref
principal_ref
account_ref optional
auth_context_ref
operator_context_ref optional
active_case_ref optional
observed_job_refs optional
observed_execution_lease_refs optional
observed_license_lease_ref optional
requested_mode
requested_at
requested_by_client_ref optional
```

## Decision Shape

The canonical logout policy decision shape may include:

```text
logout_policy_decision_ref
logout_request_ref
decision
reason
required_confirmation
next_actions
affected_case_refs
affected_job_refs
affected_execution_lease_refs
auth_context_action
license_lease_action
runtime_seal_action
records_evidence_action
knowledge_action
created_at
```

Field role notes:

```text
affected_case_refs identify observed or governed case posture only.
affected_job_refs identify case-bound work under review only.
affected_execution_lease_refs identify continuity posture only.
logout_policy_decision does not implement cancellation, revocation or sealing.
```

## Decision Statuses

| Status | Meaning |
| ------ | ------- |
| `allowed` | logout may proceed under the current posture |
| `blocked` | logout cannot proceed under the current posture |
| `requires_confirmation` | operator confirmation is required before logout proceeds |
| `requires_wait` | logout should wait for active work posture to settle |
| `requires_pause` | logout should pause governed work before proceeding |
| `requires_stop` | logout should stop governed work before proceeding |
| `force_allowed` | force-mode logout may proceed under explicit policy |
| `force_denied` | force-mode logout is denied under the current posture |

## Safe Reasons

| Reason | Meaning |
| ------ | ------- |
| `no_active_work` | no active case-bound work was observed |
| `active_case_present` | an active case posture is present |
| `active_job_present` | an active job posture is present |
| `active_execution_lease_present` | an execution lease is actively governing continuity |
| `license_lease_active` | a license lease is active and should be preserved or inspected |
| `license_lease_expired` | the observed license lease is expired |
| `runtime_gate_blocked` | runtime gate posture blocks further operational action |
| `machine_authorization_missing` | required machine authorization posture is missing |
| `policy_requires_confirmation` | policy requires explicit operator confirmation |
| `insufficient_authority` | the requester lacks authority for the requested mode |
| `unknown` | the policy reason is not yet known |

## Policy Actions

### Auth Context Actions

| Action | Meaning |
| ------ | ------- |
| `clear_auth_context` | clear auth posture as part of logout completion |
| `retain_until_expiry` | keep the current auth posture until expiry policy applies |
| `refresh_required` | an auth refresh is required before further action |
| `revoke_later` | auth revocation is deferred to a later explicit policy |
| `not_applicable` | no auth action applies |

### License Lease Actions

| Action | Meaning |
| ------ | ------- |
| `retain_until_expiry` | keep the current license lease until its own expiry |
| `mark_stale` | mark the observed license posture stale for later refresh |
| `invalidate_on_revoke` | invalidate only when an explicit revoke policy applies |
| `refresh_required` | a refreshed license posture is required before future actions |
| `not_applicable` | no license action applies |

### Runtime Seal Actions

| Action | Meaning |
| ------ | ------- |
| `seal_operational_actions` | future operational actions should be sealed |
| `allow_diagnostics_only` | diagnostics may remain visible while operations are sealed |
| `retain_current_readonly` | preserve current read-only posture |
| `no_runtime_change` | no runtime posture change is required |

### Records / Evidence Actions

| Action | Meaning |
| ------ | ------- |
| `preserve` | keep durable records and evidence intact |
| `flush_pending` | flush pending durable writes without deletion |
| `seal_writes` | seal future writes while preserving existing state |
| `not_applicable` | no records or evidence action applies |

### Knowledge Actions

| Action | Meaning |
| ------ | ------- |
| `preserve` | keep case-bound knowledge intact |
| `flush_pending` | flush pending knowledge writes without deletion |
| `seal_writes` | seal future knowledge writes while preserving existing state |
| `not_applicable` | no knowledge action applies |

## Active Work Policy

| Situation | Default policy |
| --------- | -------------- |
| no active case, job, or lease | logout allowed |
| active case only | logout allowed or requires confirmation depending policy |
| active job without lease | requires confirmation or pause policy |
| active job with execution lease | requires wait, pause, stop, or force decision |
| active license lease | retain until expiry unless explicit revoke policy exists |
| expired license lease | seal operational actions |
| unknown active work | block or require confirmation |

## Distinctions

### Logout vs Detach

```text
detach changes client observation/connection.
logout changes auth/control posture.
```

### Logout vs License Lease

```text
logout may affect auth_context.
logout does not automatically invalidate license_lease unless policy says so.
license_lease expiry or revocation may seal runtime independently of logout.
```

## Non-Deletion Rule

```text
Logout must not delete records, evidence or knowledge.
```

Logout may seal future operational actions or writes, but the durable state
itself remains preserved unless a later explicit policy says otherwise.

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| case evidence binding | V29 |
| knowledge binding | V30 |
| provider authority binding | V31 |
| agent authority binding | V32 |
| flow binding | V33 |
| license lease consumption | V43 |
| sealed-by-license behavior | V48 |
| logout/revocation/lease invalidation implementation | V50 |
