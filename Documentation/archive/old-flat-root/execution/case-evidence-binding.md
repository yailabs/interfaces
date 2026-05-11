# Case Evidence Binding

## Status

* Delivery: V29
* Status: active execution/evidence contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define evidence as case-bound proof material.

## Canonical Invariant

```text
evidence.case_ref is required.
```

Evidence is case-native proof material. It may be produced by runtime
observation, operator action, provider interactions, gate posture, or
case-bound work, but the ownership boundary remains the case.

## Evidence Is Not Owned By

Evidence must not be treated as owned by:

```text
session
client
shell
terminal
Loom
VS Code
Desktop window
runtime process
provider response alone
job alone
license_lease
auth_context
```

## Shape

The canonical evidence shape may include:

```text
evidence_ref
case_ref
evidence_kind
title
summary optional
created_at
created_by_principal_ref optional
created_from_client_ref optional
job_ref optional
execution_lease_ref optional
record_ref optional
provider_call_ref optional
runtime_gate_decision_ref optional
license_lease_ref optional
machine_authorization_ref optional
artifact_refs optional
lineage_refs optional
content_digest optional
retention_policy_ref optional
visibility
retention_posture
```

Field role notes:

```text
job_ref is optional provenance or source context only.
execution_lease_ref is optional continuity context only.
provider_call_ref is optional source context only.
runtime_gate_decision_ref is optional evidence link only.
license_lease_ref and machine_authorization_ref are optional authorization posture refs only.
record_ref is an optional related durable record ref, not evidence ownership.
```

## Evidence Kinds

| Kind | Meaning |
| ---- | ------- |
| `manual_note` | operator-authored case note or summary |
| `job_output` | output emitted by case-bound work |
| `provider_response` | provider-returned material captured as case evidence |
| `runtime_decision` | runtime-produced decision or control posture material |
| `gate_decision` | gate posture or gate decision evidence |
| `file_artifact` | file or blob artifact linked to the case |
| `log_excerpt` | excerpt from governed logs or observation streams |
| `test_result` | test or verification result tied to the case |
| `approval` | explicit approval evidence |
| `rejection` | explicit rejection evidence |
| `warning` | warning posture evidence |
| `error` | error posture evidence |
| `system_observation` | general system observation preserved as evidence |

## Visibility

| Visibility | Meaning |
| ---------- | ------- |
| `private` | visible only to the local or narrow owning posture |
| `case_visible` | visible to the governed case surface |
| `team_visible` | visible to the authorized team surface |
| `admin_visible` | visible to administrative or governance operators |
| `system_internal` | system-internal evidence surface only |

## Retention Posture

| Retention posture | Meaning |
| ----------------- | ------- |
| `retain` | preserve as normal durable case evidence |
| `seal_writes` | preserve existing evidence while sealing future writes |
| `redact_later` | preserve now and defer redaction policy |
| `delete_only_by_explicit_policy` | deletion requires a later explicit policy |
| `unknown` | retention posture is not yet known |

## Ownership And Lineage

```text
Evidence belongs to case_ref.
Evidence may reference jobs, execution leases, records, provider calls, runtime gate decisions, and artifacts.
Those refs provide lineage and provenance, not ownership replacement.
```

This means a provider response, job output, or gate decision may contribute
evidence, but none of those surfaces own the evidence by themselves.

## Detach / Logout / Seal Rules

```text
detach does not delete evidence
logout does not delete evidence by default
runtime seal does not delete evidence by default
license lease expiry does not delete evidence by default
evidence writes may be sealed while evidence reads remain governed by policy
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| knowledge binding | V30 |
| provider authority binding | V31 |
| agent authority binding | V32 |
| flow binding | V33 |
| analytics binding | V34 |
| runtime gate registry | V35 |
| SDK case clients | V59 |
| entitlement/license clients | V60 |
