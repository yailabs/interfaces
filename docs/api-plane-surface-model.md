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
API is client-neutral contract surface and not a client implementation or UI state owner.


## Wave 21 runtime service lifecycle note

Runtime lifecycle operations use `schemas/runtime-service-status.v1.schema.json` and remain readiness/control-plan contracts. They do not claim system service management, provider/model execution, or start/stop execution. Runtime adapters live in `../yai/runtime/boundary/api`; API contracts remain in this repository.

Wave 22D3 adds sealed-runtime posture projection to the same lifecycle/status contract.
No new endpoint families are introduced; contract extension is in-place.

Wave 22D7 note:
- runtime plane status contracts separate service lifecycle from operator/client/session/account semantics;
- service manager posture remains planned unless explicit integration is delivered.

Wave 22D8 note:
- identity/account surfaces in API are reference/posture contracts only;
- account product backend ownership remains external to core runtime contracts.
- clients should not bypass SDK except debug/conformance/bootstrap.
