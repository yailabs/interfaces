# Operation Registry

The operation registry is the machine-readable authority for API operation identity and projection metadata.

## Artifact Roots

- `registry/api-families.v1.json`
- `registry/api-verbs.v1.json`
- `registry/api-operations.v1.json`
- `registry/api-operation-projections.v1.json`
- `registry/yai-actions.v1.json`

## Registry Responsibilities

- Register public operation ids.
- Connect operation ids to families, verbs, schemas, projections, and action descriptors.
- Mark deprecated or forbidden operations explicitly.
- Keep command/action projections derived from protocol operations.
- Provide stable input to conformance and OpenAPI projection.

## Non-Goals

The registry does not define runtime handler code, SDK package APIs, or Console UX. It defines protocol identity and projection metadata consumed by those layers.
