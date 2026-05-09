# Case-bound Jobs

## Status

* Delivery: V25
* Status: active execution-governance model
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define the invariant that jobs are bound to cases.

## Canonical Invariant

```text
job.case_ref is required.
```

Jobs are case-bound execution records. They do not inherit ownership from the
client, shell, session, runtime process, or provider call that happened to
create, observe, or execute them.

## Job Is Not Owned By

```text
session
client
shell
terminal
Loom
VS Code
Desktop window
runtime process
provider call
account object
license object
```

## Job Shape

The canonical job shape may include:

```text
job_ref
case_ref
created_by_principal_ref
created_from_client_ref
operator_context_ref
runtime_gate_decision_ref
machine_authorization_ref
license_lease_ref
status
created_at
updated_at
started_at
completed_at
failed_at
blocked_reason
```

Field role notes:

```text
created_from_client_ref is provenance only.
operator_context_ref is selection/admission context only.
machine_authorization_ref and license_lease_ref are authorization posture refs.
runtime_gate_decision_ref is decision evidence.
None of them own the job.
```

## Lifecycle

| Status | Meaning |
| ------ | ------- |
| `created` | job record exists but is not admitted |
| `admitted` | posture allows scheduling |
| `blocked` | posture or limit blocks execution |
| `queued` | accepted but not running |
| `running` | actively executing |
| `paused` | execution paused |
| `completed` | completed successfully |
| `failed` | failed |
| `cancelled` | cancelled by policy/operator |
| `expired` | no longer valid to continue |

## Admission Requirements

A job may be admitted only when projected posture supports it:

```text
auth_context present
case_ref valid
operator context selected or explicit case_ref provided
runtime_gate_decision allows job action
machine_authorization_ref valid when required
license_lease valid when required
limit projection allows new job
```

V25 does not implement the evaluator. It defines the admission boundary only.

## Read Model

The canonical read model may expose:

```text
job_ref
case_ref
status
readiness
blocked_reason
active_step_ref optional
created_from_client_ref optional
lease_ref optional, V26
record_refs optional, V29
evidence_refs optional, V29
```

## Client / Session Boundary

```text
Clients may create or observe jobs.
Clients do not own jobs.
Session never owns jobs.
```

This means CLI, Loom, VS Code, and future Desktop clients may initiate or
inspect work, but job identity and continuity remain case-bound rather than
attachment-bound.

## Runtime / Gate Boundary

```text
Runtime readiness does not own job identity.
Runtime process does not own job identity.
runtime_gate_decision_ref, license_lease_ref, and machine_authorization_ref are
admission or authorization posture, not ownership.
```

V25 does not claim live license, machine, or entitlement evaluators. It only
defines how those refs participate in future admission evidence.

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| execution lease model | V26 |
| detach/continuation semantics | V27 |
| logout/seal policy | V28 |
| case evidence binding | V29 |
| knowledge binding | V30 |
| provider authority binding | V31 |
| agent authority binding | V32 |
| flow binding | V33 |
| runtime gate registry | V35 |
