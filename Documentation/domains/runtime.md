# Runtime Domain

The runtime domain documents API-facing runtime posture, readiness, sealed behavior, local development wrapper boundary, and service lifecycle projection.

## Boundary

API documents runtime status and control projections only. Runtime implementation truth, service internals, process ownership, and enforcement logic are delegated to `../yai/Documentation`.

## Absorbed Semantics

- Runtime readiness projection.
- Allowed and blocked surfaces.
- Runtime sealed enforcement and license-sealed posture projection.
- Service lifecycle boundary and development wrapper boundary.
- Runtime gate registry and local compatibility containment.

## Artifact References

- `schemas/runtime-service-status.v1.schema.json`
- `schemas/runtime-gate-registry.v1.schema.json`
- `schemas/runtime-sealed-by-license-behavior.v1.schema.json`
- `fixtures/runtime-gate-registry/`
