# Machine Fingerprint Evidence Builder

## Status

* Delivery: V40
* Status: active machine evidence boundary contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define privacy-bounded machine evidence for future enrollment and authorization.

## Canonical Invariants

```text
machine_fingerprint_evidence.local_machine_identity_ref is required.
machine_fingerprint_evidence.local_machine_ref is required.
machine_fingerprint_evidence.evidence_kind is required.
machine_fingerprint_evidence.privacy_posture is required.
```

## Machine Fingerprint Evidence Is Not

```text
raw hardware fingerprint
machine authorization
license lease
login
session
auth_context
```

## Shape

```text
machine_fingerprint_evidence_ref
local_machine_identity_ref
local_machine_ref
machine_identity_store_ref optional
evidence_kind
evidence_status
evidence_source_policy
privacy_posture
minimization_posture
consent_posture
confidence_posture
rotation_posture
enrollment_use
created_at optional
expires_at optional
source_local_identity_status optional
machine_authorization_ref optional
machine_authorization_status optional
license_lease_ref optional
runtime_gate_decision_ref optional
warning_codes optional
redaction_notes optional
```

## Evidence Kinds

| Evidence kind | Meaning |
| ------------- | ------- |
| `local_identity_attestation` | Evidence posture derived only from local machine identity posture. |
| `privacy_bounded_fingerprint` | Privacy-bounded evidence may exist without exposing raw hardware identifiers. |
| `enrollment_candidate` | Evidence posture can be considered by a future enrollment workflow. |
| `rotation_evidence` | Evidence posture reflects local identity rotation. |
| `revocation_evidence` | Evidence posture reflects revocation-related follow-up. |
| `reboot_continuity_evidence` | Evidence posture describes continuity across restart or reboot. |
| `machine_posture_evidence` | Evidence posture summarizes safe local machine posture without becoming authorization. |

## Evidence Statuses

| Evidence status | Meaning |
| --------------- | ------- |
| `not_built` | No evidence output has been produced. |
| `built` | Privacy-bounded evidence posture exists. |
| `ready_for_enrollment` | Evidence posture can be presented to a future enrollment flow. |
| `requires_consent` | Evidence posture exists but cannot be used until consent posture is satisfied. |
| `requires_privacy_review` | Evidence posture requires further privacy review before future use. |
| `low_confidence` | Evidence posture is available but confidence is too low for strong follow-up. |
| `rotated` | Evidence posture reflects a rotated identity or rotated evidence relation. |
| `revoked` | Evidence posture is no longer suitable for future enrollment or authorization follow-up. |
| `blocked` | Evidence posture is blocked pending future workflow decisions. |
| `unknown` | Runtime cannot classify the evidence posture safely. |

## Evidence Source Policies

| Evidence source policy | Meaning |
| ---------------------- | ------- |
| `local_identity_only` | Evidence posture is derived only from the local machine identity posture. |
| `privacy_bounded_signals` | Only privacy-bounded signals may be used in a future implementation. |
| `user_confirmed_signals` | Evidence posture expects user-confirmed signals without exposing raw hardware fields. |
| `account_confirmed_signals` | Future account-side confirmation can complement the local posture. |
| `no_raw_hardware` | Raw hardware fields are explicitly forbidden from evidence contracts. |
| `not_applicable` | The source policy is not relevant for the current posture. |
| `unknown` | Source policy is not known safely. |

## Privacy Postures

| Privacy posture | Meaning |
| --------------- | ------- |
| `privacy_bounded` | Evidence posture is privacy-bounded for V/core use. |
| `minimized` | Only minimal evidence posture is retained. |
| `raw_hardware_forbidden` | Raw hardware fields are explicitly forbidden. |
| `redacted` | Evidence posture is redacted before any future handoff. |
| `requires_review` | Privacy review is required before future consumption. |
| `blocked` | Privacy posture blocks evidence use until future work resolves it. |
| `unknown` | Privacy posture is not known safely. |

## Minimization Postures

| Minimization posture | Meaning |
| -------------------- | ------- |
| `minimal` | Minimal evidence posture is retained. |
| `reduced` | Evidence posture is reduced relative to future richer candidates. |
| `aggregated` | Only aggregated evidence posture may be carried forward. |
| `hashed_or_derived_only` | Only derived, non-raw posture may exist in future implementations. |
| `redacted` | Sensitive posture was redacted before exposure. |
| `blocked` | Minimization posture blocks the evidence from future use. |
| `unknown` | Minimization posture is not known safely. |

## Consent Postures

| Consent posture | Meaning |
| --------------- | ------- |
| `not_required` | No additional consent is required for the posture as documented. |
| `required` | Future use requires explicit consent first. |
| `granted` | Consent posture is satisfied for future use. |
| `denied` | Consent posture blocks future use. |
| `deferred` | Consent handling is deferred to future workflow steps. |
| `unknown` | Consent posture is not known safely. |

## Confidence Postures

| Confidence posture | Meaning |
| ------------------ | ------- |
| `high` | Evidence posture is strong enough for future workflow consideration. |
| `medium` | Evidence posture is usable but not strong enough to stand alone. |
| `low` | Evidence posture is weak and should be treated carefully. |
| `insufficient` | Evidence posture is not sufficient for future workflow use. |
| `ambiguous` | Evidence posture is ambiguous and needs follow-up. |
| `unknown` | Confidence posture is not known safely. |

## Enrollment Use

| Enrollment use | Meaning |
| -------------- | ------- |
| `not_for_enrollment` | Evidence posture should not be used for enrollment. |
| `enrollment_ready` | Evidence posture is ready for a future enrollment flow. |
| `enrollment_pending` | Future enrollment work is expected but not complete. |
| `enrollment_blocked` | Future enrollment use is blocked. |
| `authorization_refresh_candidate` | Evidence posture may support future authorization refresh workflows without becoming authorization. |
| `unknown` | Enrollment use is not known safely. |

## Forbidden Raw Hardware / Secret Fields

```text
serial_number
serial
mac_address
mac
hardware_uuid
hardware_id
raw_fingerprint
raw_hardware_fingerprint
motherboard_serial
disk_serial
cpu_serial
device_serial
api_key
token
secret
password
private_key
signing_key
salt
raw_salt
```

## Privacy Rules

```text
machine fingerprint evidence must not contain raw serial number
machine fingerprint evidence must not contain raw MAC address
machine fingerprint evidence must not contain raw hardware UUID
machine fingerprint evidence must not contain raw hardware fingerprint
machine fingerprint evidence must not contain salts or private keys
machine fingerprint evidence must not grant machine authorization by itself
machine fingerprint evidence must not grant license lease by itself
machine fingerprint evidence must not be login/session/auth_context
```

## E/V Boundary

```text
V builds privacy-bounded local machine evidence posture.
E owns machine authorization decisions, authorization lifecycle, leases and
account limits.
V may later present safe evidence to E for enrollment.
V must not expose raw hardware or secrets.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| machine enrollment client flow | V41 |
| machine authorization consumption | V42 |
| license lease consumption | V43 |
| local lease cache / reboot continuity | V44 |
| runtime license check request/response | V46/V47 |
| sealed-by-license behavior | V48 |
