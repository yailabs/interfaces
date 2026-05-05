# Operator Context Plane

## Status

* Delivery: V11
* Status: active local model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Define the operator context plane.

## Definition

The operator context is the local/current operator posture for a client command
or interactive shell.

It owns current operational selections, especially:

```text
operator_context.active_case_ref
```

It does not own auth, account, runtime lifecycle, case existence, or shell/client
connection lifecycle.

## Local V11 Marker

The local operator context marker is stored at:

```text
$YAI_CONFIG_HOME/operator/context.json
```

Default path:

```text
~/.yai/operator/context.json
```

V11 writes this marker shape:

```json
{
  "schema": "yai.operator-context.v1",
  "source": "cli",
  "principal": "local-dev:francescomaiomascio",
  "auth_context": "local-dev",
  "root_case_ref": "case://francescomaiomascio",
  "active_case_ref": "case://francescomaiomascio/projects/site-e0-cleanup",
  "client_ref": "cli",
  "shell_ref": null
}
```

The V10 marker schema `yai.operator-context.active-case.v1` remains readable as
a compatibility marker. New V11 writes use `yai.operator-context.v1`.

When no active case is selected, `active_case_ref` is null and the marker may be
retained.

## Ownership Table

| Concern | Canonical owner |
| ------- | --------------- |
| principal | auth plane |
| auth_context | auth plane |
| account_ref | external account platform |
| root_case_ref | case plane |
| case existence | case tree |
| active_case_ref | operator context |
| client connection | client plane, later V12 |
| shell lifecycle | shell plane, later V13 |
| runtime health/readiness | runtime plane |
| session | legacy compatibility only |

## Installed CLI Boundary

The primary local command path is installed `yai`.

Current residual: PATH must prefer `~/.cargo/bin` over `/usr/local/bin` until
runtime carrier shadowing is resolved.

## Boundary Rules

```text
operator context != session
operator context != auth login
operator context != account_ref
operator context != case tree
operator context != shell/client attach
operator context != runtime readiness
operator context owns active_case_ref
auth owns principal/auth_context
case tree owns case existence
client/shell planes own connection lifecycle later
runtime readiness remains separate
installed CLI invocation remains canonical
session remains legacy compatibility only
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| client connection model | V12 |
| shell UX model | V13 |
| runtime sealed enforcement | V14 |
| API operator context surfaces | V37 |
| SDK case/operator clients | V39 |
| logout policy with active case/job | V27 |
