# Subprocess Stdio Compat v1

## Purpose

Define `subprocess_stdio_compat` as a temporary compatibility/debug transport
class where a client executes a binary and parses stdout/stderr.

API.08 verticalizes this transport into a dedicated contract subtree so
legacy/debug/migration process invocation stays explicit without becoming a
hidden long-term SDK transport or a replacement for Local IPC RPC, Local HTTP
Loopback, or Local Event Stream.

## Classification

- status: compat only
- class: subprocess/stdout/stderr compatibility bridge

## Allowed Uses

- temporary VS Code compatibility
- migration compatibility
- debug tooling where no canonical SDK transport exists yet
- smoke checks
- local developer diagnostics

## Guardrails

- must not become canonical SDK/client transport
- must not be used for new SDK transport design
- must not be described as the preferred local runtime transport
- must not replace runtime listener or server behavior
- must not redefine operation grammar

## Contract Surfaces

- `subprocess-stdio-compat/README.md`
- `subprocess-stdio-compat/purpose.v1.md`
- `subprocess-stdio-compat/stdout-stderr-contract.v1.md`
- `subprocess-stdio-compat/exit-status-model.v1.md`
- `subprocess-stdio-compat/env-boundary.v1.md`
- `subprocess-stdio-compat/security-limitations.v1.md`
- `subprocess-stdio-compat/deprecation-policy.v1.md`
- `subprocess-stdio-compat/errors.v1.md`
- `subprocess-stdio-compat/conformance-profile.v1.md`

## Non-goals

- no subprocess transport implementation is added by this document
- no promotion to primary transport status
