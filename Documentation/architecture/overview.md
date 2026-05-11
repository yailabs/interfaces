# Interfaces Architecture Overview

YAI Interfaces is the canonical developer-interface repository. It unifies the
protocol/API surface and the official SDK packages into one authority for
external and internal client authors.

The repository owns protocol contracts, operation semantics, transports,
envelopes, errors, schemas, registries, fixtures, conformance, OpenAPI
projections, mappings, contracts, lifecycle models, generated surfaces,
official SDK packages, developer examples, and integration contracts.

It does not own YAI runtime implementation, YAI service lifecycle
implementation, Console terminal UX, or web/account/product surfaces.

After INTF.4, SDK packages live under:

- `packages/rust`
- `packages/python`
- `packages/typescript`
- `packages/c`

The architecture separates five versioned layers:

- protocol version;
- SDK package version;
- generated surface version;
- conformance profile version;
- repository release version.

Developer and client flow:

```text
external client or Console or future Studio
  -> interfaces SDK/API
  -> yai runtime/system effect
```
