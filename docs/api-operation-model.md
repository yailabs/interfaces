# API Operation Model

Wave 16B introduces operation IDs as client-facing contract seams.

Operation IDs are declared in `registry/api-operations.v1.json` and do not imply runtime execution.
Stability and implementation fields are authoritative for readiness.

Transport, endpoint, and execution remain outside this repository.
API operation IDs are client-neutral contracts, not client implementation state.

Wave 17 consumer note: Loom uses SDK typed plane clients mapped to this operation model.


## Wave 21 runtime service lifecycle note

Runtime lifecycle operations use `schemas/runtime-service-status.v1.schema.json` and remain readiness/control-plan contracts. They do not claim system service management, provider/model execution, or start/stop execution. Runtime adapters live in `../yai/runtime/boundary/api`; API contracts remain in this repository.

Wave 22D3 extends the runtime service status contract with sealed posture fields.
Runtime liveness/health/readiness is explicitly separated from operational authority:
runtime may be alive/healthy while `sealed=true` and operational actions remain blocked.

Wave 22D4 visibility note: runtime status can expose client-connection/operator-context
posture as readiness projection only. No connect/disconnect workflow, login, or
operator success path is implied by this contract.

Wave 22D5 visibility note: runtime status may also expose active-case readiness
fields (`activeCasePosture`, `activeCaseReason`, `activeCaseRef`) as operator-context
projection only. This does not imply case creation/attach/select workflows.

Wave 22D6 session compatibility note: legacy `session` semantics remain available only as
transitional compatibility. Canonical forward surfaces are identity posture, runtime
client-connection, operator-context, and case-plane-owned active case state.

Wave 22D7 runtime service boundary note:
- runtime status distinguishes service lifecycle/manager posture from operational readiness;
- service may be running while operational readiness remains sealed/blocked;
- no systemd/launchd integration is claimed by this contract.

Wave 22D8 account-system boundary note:
- runtime/API may expose `account_ref`/`entitlement_ref`/`auth_context` posture fields as references only;
- runtime API contracts are not account backend, billing, subscription, or OAuth provider surfaces.
- normal product path is SDK-first; direct runtime usage is debug/conformance/bootstrap only.
