# Protocol / API Boundary

## Purpose

Define the cut line between canonical YAI protocol ownership and API projection
ownership during the V28.5 filesystem cutover.

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

## Target API Shape

The target API projection shape for later waves is:

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

## Current V28.5 Reality

- `openapi/`, `registry/`, `conformance/`, `fixtures/`, and `docs/` exist now.
- `projections/`, `mappings/`, `examples/`, and `tools/` are target surfaces,
  but they do not exist in the current repository state.
- V28.5 does not invent those directories prematurely.
- API mirror conformance now reads canonical protocol files from
  `../yai/protocols` and fails on drift between canonical protocol artifacts and
  API mirror copies.

## Cutover Rule

Until OpenAPI, registry, and API-specific validation are fully rewired, API may
retain mirror copies of selected schemas, fixtures, and conformance checks.
Those mirrors are compatibility surfaces, not protocol truth.
