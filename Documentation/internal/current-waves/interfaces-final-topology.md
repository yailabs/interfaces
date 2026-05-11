# Interfaces Final Topology

Status: final topology for INTF.9 closure.

## Active Repositories

`yai`:

Runtime, system, governance, service lifecycle, and core architecture.

`interfaces`:

Protocol/API/SDK/conformance/generated-surface/package/developer-interface
truth.

`console`:

Terminal client UX, CLI mode, TUI mode, command UX, and runtime attachment UX.

`web`:

Public, account, home, download, dashboard, and commercial surface.

## Historical / Tombstone

`sdk`:

Tombstone/historical only.

`api`:

Historical name replaced by `interfaces`.

`cli`:

Tombstone/historical only.

`loom`:

Historical name only.

## Consumption Path

```text
console command / future studio / external client
  -> interfaces SDK/API surface
  -> yai runtime/system effect
```

## Interface Ownership

Protocol source of truth:

- `interfaces/operations`
- `interfaces/registry`
- `interfaces/schemas`
- `interfaces/mappings`
- `interfaces/envelopes`
- `interfaces/errors`
- `interfaces/transports`

SDK packages:

- `interfaces/packages/rust`
- `interfaces/packages/python`
- `interfaces/packages/typescript`
- `interfaces/packages/c`

Conformance:

- `interfaces/conformance`

Generation/provenance:

- `interfaces/generators`
- `interfaces/projections`
- `interfaces/tools/checks`

## Non-Ownership

`interfaces` does not own runtime implementation.

`interfaces` does not own terminal UX.

`interfaces` does not own web/account/commercial product truth.

`interfaces` does not own YAI service lifecycle implementation.
