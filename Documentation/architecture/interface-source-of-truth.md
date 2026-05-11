# Interface Source Of Truth

YAI Interfaces source of truth lives in this repository's artifacts and
documentation tree.

## Normative Artifact Roots

- `registry/` defines families, verbs, operations, projections, clients,
  envelopes, errors, surfaces, and action descriptors.
- `schemas/` defines operation, envelope, reference, and domain payload schema
  contracts.
- `mappings/` defines operation dispatch, transport selection, exposure, and
  streamability policy.
- `transports/`, `envelopes/`, and `errors/` define transport and wire-level
  contracts.
- `contracts/` defines foundation, identity, runtime, and client contract
  material.
- `lifecycle/` defines operation result and compatibility lifecycle material.
- `openapi/` defines OpenAPI projection output.
- `conformance/` defines checks that validate the artifacts.

## Documentation Authority

- `architecture/` explains ownership and boundary rules.
- `operations/` explains operation grammar and registry semantics.
- `transports/`, `envelopes/`, and `errors/` explain wire behavior.
- `domains/` explains protocol/API-facing domain projection semantics.
- `packages/` explains official SDK package boundaries after SDK drain.
- `generation/` explains generated surface boundaries and provenance.
- `reference/` indexes artifact roots without moving or rewriting them.

## Delegation

YAI owns runtime implementation truth. Console owns terminal client UX truth.
Web owns public/account/product surfaces. SDK package source remains in `../sdk`
until SDK drain, then package truth moves under `interfaces/packages/`.

YAI Interfaces documents the developer-interface boundary these consumers use
or implement.
