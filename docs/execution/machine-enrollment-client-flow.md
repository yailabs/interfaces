# Machine Enrollment Client Flow

## Status

* Delivery: V41
* Status: active machine enrollment client-flow contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define runtime/client-side machine enrollment request posture.

## Canonical Invariants

```text
machine_enrollment_request.local_machine_identity_ref is required.
machine_enrollment_request.local_machine_ref is required.
machine_enrollment_request.enrollment_intent is required.
machine_enrollment_request.enrollment_channel is required.
```

## Machine Enrollment Request Is Not

```text
machine authorization
license lease
login
session
auth_context
raw hardware fingerprint
```

## Shape

```text
machine_enrollment_request_ref
local_machine_identity_ref
local_machine_ref
machine_fingerprint_evidence_ref optional
enrollment_intent
enrollment_channel
enrollment_status
account_confirmation_posture
browser_handoff_posture
device_code_posture
privacy_posture
consent_posture
requested_at optional
expires_at optional
requested_by_principal_ref optional
requested_from_client_ref optional
auth_context_ref optional
account_ref optional
principal_ref optional
machine_authorization_ref optional
machine_authorization_status optional
license_lease_ref optional
runtime_gate_decision_ref optional
blocked_reason optional
next_actions optional
warning_codes optional
```

## Enrollment Intents

| Enrollment intent | Meaning |
| ----------------- | ------- |
| `authorize_machine` | Request posture seeks future machine authorization. |
| `refresh_machine_authorization` | Request posture seeks refresh of an existing future authorization relation. |
| `replace_machine` | Request posture seeks replacement of a prior machine relation. |
| `rotate_machine_identity` | Request posture follows local identity rotation. |
| `recover_machine_identity` | Request posture follows recovery of a prior local identity posture. |
| `inspect_enrollment_status` | Request posture only inspects enrollment standing. |

## Enrollment Channels

| Enrollment channel | Meaning |
| ------------------ | ------- |
| `browser_handoff` | Future browser handoff may be needed, but V41 does not implement it. |
| `device_code` | Future device-code flow may be needed, but V41 does not implement it. |
| `account_portal` | Future account portal follow-up may be needed. |
| `manual_review` | Future manual review may be needed. |
| `local_preview` | Local runtime/client posture may preview what future enrollment would require. |
| `not_applicable` | No enrollment channel applies to the current posture. |

## Enrollment Statuses

| Enrollment status | Meaning |
| ----------------- | ------- |
| `not_started` | No enrollment request posture has started. |
| `ready` | Enrollment request posture is ready for future handoff. |
| `pending_browser_handoff` | A future browser handoff step is expected. |
| `pending_device_code` | A future device-code step is expected. |
| `pending_account_confirmation` | Account confirmation is still pending in E/platform. |
| `pending_manual_review` | Manual review is still pending. |
| `approved` | E/platform-approved posture is observed, but V41 does not issue it. |
| `rejected` | E/platform rejected the request posture. |
| `expired` | Enrollment posture expired before completion. |
| `blocked` | Enrollment posture is blocked pending future follow-up. |
| `cancelled` | Enrollment posture has been cancelled. |
| `unknown` | Runtime/client cannot classify the posture safely. |

## Account Confirmation Postures

| Account confirmation posture | Meaning |
| ---------------------------- | ------- |
| `not_required` | No account confirmation is needed for the current posture. |
| `required` | Account confirmation is required before future completion. |
| `pending` | Account confirmation is still pending. |
| `confirmed` | Account confirmation has been observed from E/platform. |
| `denied` | Account confirmation was denied by E/platform. |
| `expired` | Account confirmation opportunity expired. |
| `unknown` | Account confirmation posture is not known safely. |

## Browser Handoff Postures

| Browser handoff posture | Meaning |
| ----------------------- | ------- |
| `not_required` | No browser handoff is needed. |
| `required` | Browser handoff is required before future completion. |
| `ready_to_open` | Runtime/client posture is ready for a future browser open step. |
| `opened` | A browser-opened posture may be observed later, but V41 does not perform it. |
| `callback_pending` | A future callback would still be pending. |
| `callback_received` | A future callback-received posture may be observed later. |
| `failed` | Browser handoff posture failed. |
| `unknown` | Browser handoff posture is not known safely. |

## Device Code Postures

| Device code posture | Meaning |
| ------------------- | ------- |
| `not_required` | No device code is needed. |
| `required` | Device code is required before future completion. |
| `generated` | A future generated device-code posture may be observed later. |
| `pending_poll` | A future polling step would still be pending. |
| `confirmed` | Device-code confirmation has been observed. |
| `expired` | Device-code posture expired. |
| `failed` | Device-code posture failed. |
| `unknown` | Device-code posture is not known safely. |

## Privacy / Consent Postures

### Privacy Postures

| Privacy posture | Meaning |
| --------------- | ------- |
| `privacy_bounded` | Enrollment request posture is privacy-bounded. |
| `evidence_minimized` | Enrollment relies on minimized safe evidence only. |
| `requires_consent` | Privacy posture requires explicit consent before future completion. |
| `requires_privacy_review` | Privacy posture requires review before future completion. |
| `blocked` | Privacy posture blocks progress. |
| `unknown` | Privacy posture is not known safely. |

### Consent Postures

| Consent posture | Meaning |
| --------------- | ------- |
| `not_required` | No additional consent is required. |
| `required` | Consent is required before future completion. |
| `granted` | Consent posture is satisfied. |
| `denied` | Consent posture blocks future completion. |
| `deferred` | Consent handling is deferred to a future step. |
| `unknown` | Consent posture is not known safely. |

## Blocked Reasons

| Blocked reason | Meaning |
| -------------- | ------- |
| `missing_auth_context` | Auth posture is missing for future enrollment work. |
| `missing_local_machine_identity` | The local machine identity posture is missing. |
| `missing_machine_evidence` | Safe machine evidence posture is missing when needed. |
| `evidence_not_privacy_bounded` | Evidence posture is not safe enough for future enrollment use. |
| `consent_required` | Consent is required before future completion. |
| `privacy_review_required` | Privacy review is required before future completion. |
| `account_confirmation_required` | Account confirmation is required from E/platform. |
| `manual_review_required` | Manual review is required from E/platform. |
| `machine_limit_exceeded` | Future machine limit posture prevents progress. |
| `machine_already_authorized` | A machine is already authorized for the observed posture. |
| `machine_authorization_revoked` | Prior authorization posture was revoked. |
| `enrollment_expired` | Enrollment posture expired. |
| `unsafe_request` | The request posture is unsafe to continue. |
| `unknown` | Blocked reason is not known safely. |

## Next Actions

| Next action | Meaning |
| ----------- | ------- |
| `open_browser` | Future flow would need a browser step. |
| `show_device_code` | Future flow would need a device-code presentation step. |
| `wait_for_account_confirmation` | Runtime/client should wait for E/platform confirmation. |
| `wait_for_manual_review` | Runtime/client should wait for E/platform review. |
| `retry_with_fresh_evidence` | Fresh privacy-bounded evidence is needed. |
| `rotate_local_identity` | Local identity rotation should occur before retry. |
| `contact_support` | Manual follow-up outside V/core is needed. |
| `cancel` | Current posture should be cancelled. |
| `none` | No further action is currently indicated. |

## Privacy Rules

```text
machine enrollment request must not contain raw serial number
machine enrollment request must not contain raw MAC address
machine enrollment request must not contain raw hardware UUID
machine enrollment request must not contain raw hardware fingerprint
machine enrollment request must not contain salts or private keys
machine enrollment request must not grant machine authorization by itself
machine enrollment request must not grant license lease by itself
machine enrollment request must not be login/session/auth_context
```

## E/V Boundary

```text
V defines local enrollment request posture and safe evidence handoff.
E owns account confirmation, approval/rejection, machine_authorization_ref
issuance, authorization lifecycle, leases and account limits.
V may later consume machine_authorization_ref after E issues it.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| machine authorization consumption | V42 |
| license lease consumption | V43 |
| local lease cache / reboot continuity | V44 |
| account-scoped limit reconciliation | V45 |
| runtime license check request/response | V46/V47 |
| sealed-by-license behavior | V48 |
