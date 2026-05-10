# API Source Of Truth

API source of truth lives in the API repository artifacts and this documentation tree.

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

YAI owns runtime implementation truth, SDK owns typed package truth, and Console owns terminal client UX truth. API documents the protocol boundary they consume or implement.
