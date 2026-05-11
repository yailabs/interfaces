# Execution Lease Model

## Status

* Delivery: V26
* Status: active execution-governance model
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define how governed work may continue beyond client attachment.

## Canonical Invariants

```text
execution_lease.job_ref is required.
execution_lease.case_ref is required.
```

Execution leases govern continuity of case-bound work. They do not create free-
floating client work and they do not replace case ownership established in V25.

## Execution Lease Is Not

Execution lease is not any of these ownership replacements:

```text
session
client
shell
terminal
window
license_lease
runtime_gate_decision
```

It also does not belong to Loom, VS Code, or a Desktop window that happens to
observe or initiate the job.

## Shape

An execution lease may include:

```text
execution_lease_ref
job_ref
case_ref
status
holder_runtime_ref
holder_process_ref optional
created_from_client_ref optional
created_by_principal_ref
operator_context_ref optional
runtime_gate_decision_ref optional
license_lease_ref optional
machine_authorization_ref optional
issued_at
expires_at
last_heartbeat_at optional
revoked_at optional
revocation_reason optional
continuation_policy
```

Field role notes:

```text
holder_runtime_ref identifies the runtime continuity holder.
created_from_client_ref is provenance only.
operator_context_ref is admission/selection context only.
runtime_gate_decision_ref is admission evidence only.
license_lease_ref and machine_authorization_ref are authorization posture only.
None of them replace job_ref or case_ref.
```

## Lifecycle

| Status | Meaning |
| ------ | ------- |
| `proposed` | lease requested but not active |
| `active` | lease currently governs continuity |
| `stale` | heartbeat or freshness is old |
| `renewing` | renewal is in progress |
| `paused` | execution continuity paused |
| `revoked` | lease revoked by policy |
| `expired` | lease expired |
| `released` | lease released cleanly |
| `completed` | associated work completed |
| `failed` | associated work failed |

## Execution Lease vs License Lease

```text
execution_lease governs work continuity.
license_lease governs account/machine/runtime authorization.
```

An execution lease may reference `license_lease_ref` as admission posture.
An execution lease must not replace `license_lease`.
An expired or revoked `license_lease` may later force pause, revoke, or seal
policy on execution continuity, but V26 does not implement that policy.

Likewise, `runtime_gate_decision_ref` and `machine_authorization_ref` remain
authorization evidence or posture. They do not own continuity and do not grant
authority by themselves.

## Detach Boundary

```text
Client detach is not job cancellation.
Client detach is not lease revocation.
Client detach is not logout.
```

More specifically:

```text
client detach does not automatically release execution lease
client detach does not automatically cancel job
client detach does not automatically revoke auth_context
client detach does not automatically revoke license_lease
client detach does not imply runtime stopped
```

V27 owns final detach and continuation semantics. V26 only fixes the continuity
boundary so detach is not mistaken for ownership.

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| detach/continuation semantics | V27 |
| logout/seal policy | V28 |
| case evidence binding | V29 |
| knowledge binding | V30 |
| provider authority binding | V31 |
| agent authority binding | V32 |
| flow binding | V33 |
| runtime gate registry | V35 |
| license lease consumption | V43 |
| logout/revocation/lease invalidation | V50 |
