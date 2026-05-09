# API Projection Filesystem

## Status

* Delivery: V28.6
* Repo: `api`
* Role: API projection over canonical YAI protocols

## Purpose

Define `api` as an API projection repository with explicit projection-oriented
roots.

## Canonical Rule

```text
api projects yai/protocols into API surfaces.
api does not own protocol meaning.
```

## Projection Shape

```text
api/
  README.md
  Documentation/
  openapi/
  registry/
  projections/
  mappings/
  transports/
  schemas/
  fixtures/
  conformance/
  contracts/
  examples/
  tools/
```

## Root Classification

| Path | Role | Classification | Canonical owner |
| ---- | ---- | -------------- | --------------- |
| `openapi/` | HTTP/API projection output | `api_projection_root` | `api` |
| `registry/` | API exposure grammar | `api_projection_root` | `api` |
| `projections/` | projection-model docs root | `api_projection_root` | `api` |
| `mappings/` | protocol-to-API mapping docs root | `api_projection_root` | `api` |
| `transports/` | transport exposure docs root | `api_projection_root` | `api` |
| `examples/` | API-consumer example docs root | `api_projection_root` | `api` |
| `tools/` | projection-support tooling docs root | `api_projection_root` | `api` |
| `schemas/` | API-owned schemas plus protocol mirrors | `mixed_projection_surface` | split: `api` + `yai/protocols` |
| `fixtures/` | API-side example/mirror fixtures | `projection_mirror_surface` | split: `api` + `yai/protocols` |
| `conformance/` | API checks plus protocol-mirror drift checks | `mixed_projection_surface` | split: `api` + `yai/protocols` |
| `contracts/` | C ABI/reference audit surface | `legacy_audit_surface` | `api` pending separate audit |

## Boundary Notes

- `schemas/`, `fixtures/`, and selected `conformance/` checks may mirror
  canonical protocol artifacts from `../yai/protocols`, but those copies are
  compatibility/projection surfaces only.
- `registry/`, `openapi/`, `projections/`, `mappings/`, and `transports/` are
  API-owned exposure surfaces.
- `contracts/` remains intentionally separate from protocol ownership pending a
  dedicated ABI/reference decision.

## V28.6 Outcome

V28.6 does not add transport behavior or endpoint implementation. It reshapes
the visible repository narrative so the filesystem itself reads as an API
projection layer over `yai/protocols`.

See also:

- `Documentation/protocol-api-boundary.md`
