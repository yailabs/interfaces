# API Plane/Surface Model

Wave 16B sets planes/surfaces as canonical API model.
`families/` remains a compatibility grouping and extraction history, not final architecture.

Canonical planes:
- runtime
- case
- records
- flow
- governance
- supervisor
- orchestration
- agents
- knowledge
- skills
- providers
- models
- analytics
- identity

Machine-readable source:
- `registry/api-plane-surfaces.v1.json`
- `registry/api-operations.v1.json`

Wave 17 consumer note: Loom uses SDK typed plane clients mapped to this operation model.


## Wave 21 runtime service lifecycle note

Runtime lifecycle operations use `schemas/runtime-service-status.v1.schema.json` and remain readiness/control-plan contracts. They do not claim system service management, provider/model execution, or start/stop execution. Runtime adapters live in `../yai/runtime/boundary/api`; API contracts remain in this repository.
