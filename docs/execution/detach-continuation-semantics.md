# Detach / Continuation Semantics

## Status

* Delivery: V27
* Status: active execution-governance model
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define detach as a client/shell connection event, not domain ownership.

## Canonical Rule

```text
detach is not logout.
detach is not job cancellation.
detach is not runtime stop.
detach is not case close.
```

Detach changes client observation and connection posture. It does not, by
itself, change ownership of cases, jobs, execution leases, or records.

## Detach Event Shape

The canonical detach event shape may include:

```text
detach_event_ref
client_ref
client_kind
shell_ref optional
operator_context_ref optional
active_case_ref observed optional
job_refs observed optional
execution_lease_refs observed optional
reason
occurred_at
```

Field role notes:

```text
active_case_ref is observed posture only.
job_refs are observed work bindings only.
execution_lease_refs are observed continuity bindings only.
None of these fields imply that detach owns domain lifecycle.
```

## Detach Reasons

| Reason | Meaning |
| ------ | ------- |
| `user_requested` | operator intentionally detached the client or shell |
| `client_exit` | client process exited |
| `shell_exit` | shell UX exited |
| `transport_disconnect` | connection layer detached or became unavailable |
| `network_loss` | network path was lost |
| `editor_window_closed` | editor surface closed |
| `desktop_app_closed` | desktop client closed |
| `terminal_closed` | terminal surface closed |
| `crash_observed` | process or client crash was observed |
| `unknown` | detach cause is not known |

## Continuation Outcomes

| Outcome | Meaning |
| ------- | ------- |
| `no_active_work` | no case-bound work was active at detach time |
| `work_continues` | work continues under existing policy and continuity posture |
| `work_paused_by_policy` | policy pauses work after detach |
| `work_requires_reconnect` | further observation or control requires a later reconnect |
| `work_blocked_by_gate` | work cannot continue because gate posture blocks it |
| `manual_review_required` | continuation requires later operator or governance review |
| `unknown` | continuation status is not yet known |

## Detach Does Not

Detach must not automatically:

```text
logout
leave active case
close case
cancel job
release execution lease
revoke auth_context
revoke license_lease
revoke machine authorization
stop runtime
delete records/evidence/knowledge
mutate session
```

## Continuation Rules

```text
case remains case-bound
job remains job.case_ref-bound
execution lease remains job_ref/case_ref-bound
runtime may continue if authorized and lease policy allows
records/evidence remain case-bound
knowledge remains case-bound
client may later reconnect and re-read state
```

## Reconnect / Resume

```text
reconnect re-reads posture
resume observes current job/lease/case state
reconnect does not grant auth
reconnect does not refresh license_lease by itself
reconnect does not unseal runtime by itself
reconnect does not recreate execution lease by itself
```

Reconnect and resume are continuity-observation events, not automatic
reauthorization events.

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| logout/seal policy | V28 |
| case evidence binding | V29 |
| knowledge binding | V30 |
| provider authority binding | V31 |
| agent authority binding | V32 |
| flow binding | V33 |
| runtime gate registry | V35 |
| license lease consumption | V43 |
| logout/revocation/lease invalidation | V50 |
