# Client Connection Model

## Status

* Delivery: V12
* Status: active model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Define one-shot and long-lived YAI client connection semantics.

## Definition

A client is a command surface, UI surface, SDK transport surface, or application
surface that connects to YAI runtime/API/state.

A client is not the owner of auth, case, operator context, session or runtime
lifecycle.

It is a connection/execution surface, not a domain owner.

## Client Kinds

| Client kind | Lifecycle | Example |
| ----------- | --------- | ------- |
| `console-terminal` | terminal client | YAI Console |
| `cli-one-shot` | legacy one-shot command compatibility | installed `yai case status` |
| `loom-tui` | legacy long-lived TUI name | Loom compatibility |
| `vscode-extension` | long-lived/editor client | VS Code |
| `desktop-app` | long-lived app | Desktop |
| `sdk-embedded` | library-managed | Rust/TS SDK client |
| `service/internal` | service/internal | runtime internals |

## Local V12 Models

Local Console model:

```json
{
  "client_ref": "console",
  "client_kind": "console-terminal",
  "connection_lifecycle": "terminal",
  "source": "yai-console",
  "operator_context_ref": "observed-or-local",
  "auth_context": "observed-or-deferred",
  "runtime_endpoint": "deferred-or-configured",
  "session_ref": null
}
```

Legacy CLI compatibility model:

```json
{
  "client_ref": "cli",
  "client_kind": "cli-one-shot",
  "connection_lifecycle": "one-shot",
  "source": "installed-cli",
  "operator_context_ref": "~/.yai/operator/context.json",
  "auth_context": "local-dev",
  "runtime_endpoint": "deferred-or-configured",
  "session_ref": null
}
```

Legacy Loom compatibility model:

```json
{
  "client_ref": "loom",
  "client_kind": "loom-tui",
  "connection_lifecycle": "long-lived",
  "operator_context_ref": "observed-or-local",
  "auth_context": "observed-or-deferred",
  "session_ref": null
}
```

SDK model:

```json
{
  "client_ref": "sdk",
  "client_kind": "sdk-embedded",
  "connection_lifecycle": "library-managed",
  "transport": "http/local",
  "session_ref": null
}
```

## Ownership Table

| Concern | Owner |
| ------- | ----- |
| principal | auth plane |
| auth_context | auth plane |
| case existence | case tree |
| active_case_ref | operator context |
| client_ref | client connection plane |
| shell lifecycle | shell plane, V13 |
| runtime lifecycle | runtime/service plane |
| session | legacy compatibility only |

## Boundary Rules

```text
client connection != session
client connection != auth login
client connection != account_ref
client connection != root case
client connection != active case
client connection != operator context
client connection != runtime lifecycle
client connection != runtime readiness
Console terminal state may read/write operator context but does not own it
Legacy CLI one-shot invocation may read/write operator context but does not own it
Legacy Loom may hold long-lived UI state but must not own auth/case/domain state
SDK client is transport/client library, not domain owner
shell attach/detach belongs to V13
client attach/detach commands are deferred
session remains legacy compatibility only
```

## Installed CLI Boundary

Record:

```text
The canonical CLI path is installed `yai`.
Current shell validation resolves `yai` to `~/.cargo/bin/yai`.
V10.6 retains the historical `/usr/local/bin/yai` shadowing residual as a
tracked compatibility note.
```

Installed `yai ...` is a one-shot client invocation.

Each command invocation may observe auth posture, case posture, operator
context, and runtime endpoint configuration, but it does not become a long-lived
session owner.

## Relationship To V11

V11 defined operator context as the owner of `active_case_ref`.

V12 keeps that ownership stable and adds the missing client boundary:

```text
operator context = current operator posture
client connection = invocation or long-lived connection surface
shell lifecycle = deferred UX plane
```

The CLI may write `operator_context.client_ref = "cli"` in local posture, but
that does not make the CLI the owner of operator context itself.

## Command Surface Consequences

Console:

```text
YAI Console = canonical terminal client
```

Legacy installed CLI:

```text
installed `yai ...` = cli-one-shot
```

Legacy Loom:

```text
Loom = historical long-lived client/TUI surface name
```

SDK:

```text
SDK clients = embedded transport clients
```

Legacy session:

```text
legacy `session` remains compatibility-only and must not be revived as the
canonical name for client connection lifecycle
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| shell UX model | V13 |
| runtime sealed enforcement | V14 |
| SDK runtime surface alignment | V20 |
| CLI SDK-first wiring | V21 |
| Loom alignment | V22 historical |
| VS Code alignment | V23 |
| Console canonicalization | A1 |
| API operator context surfaces | V37 |
