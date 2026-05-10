# Shell UX Model

## Status

* Delivery: V13
* Status: active model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Define shell as a UX/connection surface, not a domain owner.

## Canonical Commands

| Command | V13 behavior |
| ------- | ------------ |
| `yai shell` | interactive UX surface, may be unavailable/planned |
| `yai shell list` | shell registry inspection, may be unavailable/planned |
| `yai shell attach <shell_id>` | UX connection, not auth/case/session |
| `yai shell detach` | UX disconnection, not logout/case/session |

## Local V13 Model

```json
{
  "shell_ref": "deferred-or-local",
  "shell_kind": "interactive-ux",
  "connection_lifecycle": "long-lived",
  "client_ref": "cli",
  "operator_context_ref": "~/.yai/operator/context.json",
  "auth_context": "observed",
  "active_case_ref": "observed-from-operator-context",
  "session_ref": null
}
```

## Boundary Rules

```text
shell != session
shell attach != auth login
shell detach != auth logout
shell attach != case enter
shell detach != case leave
shell attach != runtime start
shell detach != runtime stop
shell does not own active_case_ref
shell does not own root_case_ref
shell does not own jobs
shell does not own permissions
shell observes auth/operator/case state
session remains legacy compatibility only
```

## Ownership Table

| Concern | Owner |
| ------- | ----- |
| auth login/logout/status | auth plane |
| root case | case plane |
| active_case_ref | operator context |
| case tree | case plane |
| client connection | client plane |
| shell UX | shell plane |
| runtime lifecycle | runtime/service plane |
| session | legacy compatibility only |

## Relationship To V11 And V12

V11 established `operator_context.active_case_ref` as the owner of active case
selection.

V12 established client connection as a connection/execution surface rather than
a domain owner.

V13 keeps those boundaries intact and adds the shell plane:

```text
client plane = connection category
shell plane = interactive UX lifecycle
operator context = observed operator posture
auth/case/runtime = separate domain planes
```

## Command Consequences

`yai shell` does not replace:

```text
yai auth ...
yai case ...
operator context
runtime lifecycle
```

Shell attach/detach may exist as truthful unavailable/planned surfaces before a
real shell registry or backend exists.

That is acceptable in V13 as long as the command text does not fake auth,
session, active case, or runtime lifecycle ownership.

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| runtime sealed enforcement | V14 |
| runtime readiness projection | V15 |
| SDK runtime alignment | V20 |
| CLI SDK-first wiring | V21 |
| Loom alignment | V22 historical |
| Console canonicalization | A1 |
| detach semantics | V26 |
| logout policy | V27 |
