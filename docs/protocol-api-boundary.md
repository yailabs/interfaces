# Protocol / API Boundary

## Purpose

Define the cut line between canonical YAI protocol ownership and API projection
ownership after the V28.6 cutover closure.

## Canonical Rule

```text
yai/protocols defines transport-neutral meaning.
api defines exposure, mapping, and API-facing compatibility.
```

## Protocol Owns

- transport-neutral schemas
- protocol fixtures
- protocol conformance
- invariants and vocabulary
- runtime-neutral contract meaning

## API Owns

- `openapi/`
- `registry/api-*.json`
- API projection docs
- HTTP/request-response mapping
- API-specific conformance
- compatibility mirrors needed while cutover is incomplete

## API Shape

The API projection shape is now explicitly documented as:

```text
api/
  README.md
  docs/
  openapi/
  registry/
  projections/
  mappings/
  conformance/
  fixtures/
  examples/
  tools/
```

## Current V28.6 Reality

- `openapi/`, `registry/`, `conformance/`, `fixtures/`, `schemas/`, and `docs/`
  remain active surfaces.
- `projections/`, `mappings/`, `transports/`, `examples/`, and `tools/` now
  exist as documentation-only projection roots.
- API mirror conformance now reads canonical protocol files from
  `../yai/protocols` and fails on drift between canonical protocol artifacts and
  API mirror copies.

## Cutover Rule

API may retain mirror copies of selected schemas, fixtures, and conformance
checks where projection or validation consumers still need them. Those mirrors
are compatibility surfaces, not protocol truth.
