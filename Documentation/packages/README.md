# Packages

Packages documents official SDK package boundaries for YAI Interfaces.

## Current Phase

This repository is `pre-sdk-drain`. SDK package source remains in `../sdk`
until later INTF waves classify and move package material into
`interfaces/packages/`.

## Future Package Families

- Rust SDK package.
- Python SDK package.
- TypeScript SDK package.
- C SDK package.

## Rules

- Packages consume YAI Interfaces protocol/API contracts.
- Packages do not define operation semantics, transport truth, envelope truth,
  error truth, or protocol version.
- Packages declare supported protocol and conformance versions.
- Package release claims require validation evidence.

## Deferred Work

INTF.3 inventories SDK material. INTF.4 drains package source into
`interfaces/packages/`.
