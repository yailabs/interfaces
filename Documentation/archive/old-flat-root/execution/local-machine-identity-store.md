# Local Machine Identity Store

## Status

* Delivery: V39
* Status: active machine identity boundary contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define local runtime machine identity posture without raw hardware leakage.

## Canonical Invariants

```text
local_machine_identity.local_machine_identity_ref is required.
local_machine_identity.local_machine_ref is required.
local_machine_identity.store_status is required.
```

## Local Machine Identity Is Not

```text
machine authorization
license lease
auth context
login
session
raw hardware fingerprint
```

## Shape

```text
local_machine_identity_ref
local_machine_ref
machine_identity_store_ref
store_status
identity_status
created_at optional
updated_at optional
rotated_at optional
revoked_at optional
last_seen_at optional
storage_posture
rotation_posture
privacy_posture
evidence_builder_status
enrollment_readiness
machine_authorization_ref optional
machine_authorization_status optional
license_lease_ref optional
runtime_gate_decision_ref optional
warning_codes optional
```

## Store Statuses

| Store status | Meaning |
| ------------ | ------- |
| `not_created` | No local identity posture exists yet. |
| `created` | A local identity posture was established in the runtime. |
| `loaded` | A previously established local identity posture was loaded. |
| `unavailable` | The identity store cannot currently be accessed. |
| `corrupt` | The identity store exists but cannot be trusted as-is. |
| `rotated` | The local identity posture has been rotated. |
| `revoked` | The local identity posture is no longer valid for future workflows. |
| `stale` | The local identity posture exists but needs refresh or follow-up. |
| `unknown` | The runtime cannot classify the store posture safely. |

## Identity Statuses

| Identity status | Meaning |
| --------------- | ------- |
| `unbound` | The identity is not yet associated with future enrollment or authorization work. |
| `local_only` | The identity is only a local runtime posture. |
| `enrollment_ready` | The identity posture can be consumed by future enrollment work. |
| `enrollment_pending` | Follow-up enrollment work is expected but not complete. |
| `authorized` | A future authorization relation exists, but V39 does not implement it. |
| `revoked` | The identity posture is no longer trusted for future enrollment or authorization. |
| `expired` | The identity posture is no longer current enough to rely on. |
| `blocked` | The identity posture is blocked pending a future workflow. |
| `unknown` | The runtime cannot classify the identity posture safely. |

## Storage Postures

| Storage posture | Meaning |
| --------------- | ------- |
| `not_persisted` | The runtime has not persisted the identity posture. |
| `local_file` | A local file-backed posture may be used in future implementations. |
| `platform_keychain` | A platform keychain-backed posture may be used in future implementations. |
| `runtime_state_store` | Runtime state can carry the posture without making it login or session state. |
| `external_secret_store` | A future external store may hold posture metadata without exposing secrets to V/core. |
| `unavailable` | The runtime cannot access the intended storage posture. |
| `unknown` | The storage posture is not known safely. |

## Rotation Postures

| Rotation posture | Meaning |
| ---------------- | ------- |
| `not_rotated` | No rotation has occurred. |
| `rotation_available` | Rotation can happen in a future workflow. |
| `rotation_required` | Rotation should happen before future workflows proceed. |
| `rotated` | Rotation already happened. |
| `rotation_blocked` | Rotation is blocked pending a future dependency. |
| `unknown` | Rotation posture is not known safely. |

## Privacy Postures

| Privacy posture | Meaning |
| --------------- | ------- |
| `privacy_bounded` | The posture is constrained to privacy-safe identity metadata. |
| `raw_hardware_forbidden` | Raw hardware identifiers are explicitly excluded. |
| `minimized` | Only the minimal local identity posture is retained. |
| `requires_review` | Privacy review is needed before future workflow use. |
| `unknown` | Privacy posture is not known safely. |

## Evidence Builder Statuses

| Evidence builder status | Meaning |
| ----------------------- | ------- |
| `not_built` | No future evidence builder output exists. |
| `ready_for_evidence_builder` | The posture is ready for a future evidence builder. |
| `evidence_builder_required` | A future evidence builder step is required. |
| `evidence_built` | A future evidence builder relation exists, but V39 does not implement it. |
| `evidence_blocked` | The evidence builder relation is blocked pending future work. |
| `unknown` | Evidence builder posture is not known safely. |

## Enrollment Readiness

| Enrollment readiness | Meaning |
| -------------------- | ------- |
| `not_ready` | The posture is not ready for enrollment. |
| `ready` | The posture can be used by a future enrollment workflow. |
| `pending_account_confirmation` | Future enrollment work is waiting on account-side confirmation. |
| `requires_auth` | Future enrollment work requires auth first. |
| `requires_machine_authorization` | Future enrollment work depends on E-owned authorization posture. |
| `blocked` | Enrollment readiness is blocked pending future work. |
| `unknown` | Enrollment readiness is not known safely. |

## Privacy Rules

```text
local machine identity must not be raw serial number
local machine identity must not be raw MAC address
local machine identity must not be raw hardware UUID
local machine identity must not be raw hardware fingerprint
local machine identity must not expose provider identity
local machine identity must not expose account profile
local machine identity does not grant machine authorization by itself
local machine identity does not grant license lease by itself
```

## Continuity Rules

```text
local machine identity may survive terminal close
local machine identity may survive reboot if storage policy allows
local machine identity is not login
local machine identity is not auth_context
local machine identity is not client attachment
local machine identity is not session
```

## E/V Boundary

```text
V defines local machine identity posture and future evidence builder inputs.
E owns machine_authorization_ref, authorization lifecycle, leases and account limits.
V consumes machine_authorization_ref and license_lease later, not raw E account objects.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| machine fingerprint evidence builder | V40 |
| machine enrollment client flow | V41 |
| machine authorization consumption | V42 |
| license lease consumption | V43 |
| local lease cache / reboot continuity | V44 |
| account-scoped limit reconciliation | V45 |
| runtime license check request/response | V46/V47 |
