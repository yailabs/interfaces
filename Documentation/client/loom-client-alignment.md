# Loom Client Alignment

## Status

* Delivery: V22
* Status: historical compatibility note after A1
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

This file is retained so V22 references keep resolving.

A1 canonicalizes the active terminal client as **YAI Console**. Loom is now a
legacy product name and compatibility surface, not a separate canonical client.

Active model: [console-client-alignment.md](console-client-alignment.md).

## Compatibility Role

```text
Loom is a historical long-lived client/TUI surface name.
Console is the canonical terminal client.
Legacy Loom compatibility surfaces may observe and present runtime/auth/case/
operator/readiness posture, but they do not own domain truth.
```

## Compatibility Ownership Table

| Concern | Owner |
| ------- | ----- |
| auth truth | auth/E/V auth context |
| account_ref | E platform |
| root case | case plane |
| active_case_ref | operator context |
| runtime lifecycle | runtime/service plane |
| readiness projection | runtime/readiness plane |
| entitlement/license/machine refs | E contracts consumed by V |
| legacy Loom connection state | compatibility client state |
| session | legacy compatibility only |

## Wording Rules

| Avoid | Use |
| ----- | --- |
| `Loom terminal client` | `YAI Console` |
| `Loom owns case` | `Console observes case posture` / `legacy Loom observes case posture` |
| `session attached` | `client connected` / `runtime posture observed` |
| `session selected case` | `operator_context.active_case_ref` |
| `client logged in` | `auth posture: authenticated/local-dev/unauthenticated` |
| `runtime ready because UI connected` | `readiness projection` |

## Compatibility Rule

Legacy Loom wording may remain in historical wave reports, compatibility
launchers, manifest aliases, and migration notes. Active API/SDK/client design
must target Console.
