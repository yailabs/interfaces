# Provider Transport Boundary v1

## Purpose

Prevent confusion between client-runtime API transport and runtime-provider
transport.

## Rule

```text
Client asks a YAI operation.
Runtime decides provider/model routing.
Provider transport is runtime -> provider/model only.
```

## Classification

- status: separate boundary
- existing repository area: `../yai/src/providers/transport/`

## Ownership

- API owns: only the boundary language needed to prevent confusion
- Runtime and provider layers own: local, remote, LAN, and provider-specific
  execution behavior

## Non-goals

- this is not client -> runtime API transport
- SDK clients must not route directly as provider transport owners
- no provider/model invocation behavior is added by this document
