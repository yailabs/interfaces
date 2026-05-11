# Protocol/API Source Of Truth

Protocol/API source of truth now lives in YAI Interfaces artifacts and this
documentation tree. This file preserves the API-layer view inside the broader
interfaces repository.

## Normative Artifact Roots

- `registry/` defines families, verbs, operations, projections, clients, envelopes, errors, surfaces, and action descriptors.
- `schemas/` defines operation, envelope, reference, and domain payload schema contracts.
- `mappings/` defines operation dispatch, transport selection, exposure, and streamability policy.
- `transports/`, `envelopes/`, and `errors/` define transport and wire-level contracts.
- `openapi/` defines the OpenAPI projection.
- `conformance/` defines checks that validate the artifacts.

## Documentation Authority

- `architecture/` explains ownership and boundary rules.
- `operations/` explains operation grammar and registry semantics.
- `transports/`, `envelopes/`, and `errors/` explain wire behavior.
- `domains/` explains API-facing domain projection semantics.
- `reference/` indexes artifact roots without moving or rewriting them.

## Delegation

YAI owns runtime implementation truth. Console owns terminal client UX truth.
Official SDK packages live under `interfaces/packages/`.

YAI Interfaces documents the protocol/API boundary these consumers use or
implement.
