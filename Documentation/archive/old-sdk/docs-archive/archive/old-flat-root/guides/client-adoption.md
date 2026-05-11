# Client Adoption Boundary (Wave 14D)

- Clients consume SDK packages, not runtime adapters directly.
- API remains canonical contract source (`../api`).
- Runtime remains implementation source (`../yai`).
- clients do not own runtime truth.

Client migration gate status:
- `clientMigrationGateStatus: ready-for-planning`
- This wave defines migration gate and repo strategy; it does not claim migration complete.

Client repo strategy:
- separate product repos
- generic `clients` repository is not final target

Direct runtime adapter policy:
- `debug-conformance-bootstrap-only`
- direct runtime adapter imports are forbidden for normal product paths.


Design consumer repository path: `../design` (product identity: YAI Design).


Console consumer path: `../console` (product identity: YAI Console).
Legacy Loom path/name: `../loom` / YAI Loom.


Wave 16B note: TypeScript plane clients are aligned to `../api/registry/api-operations.v1.json`.
SDK transport remains abstract unless explicitly configured.

Wave 17/A1: Console consumes SDK plane clients directly through typed operations with readiness envelopes.


## Wave 21 runtime service lifecycle note

The TypeScript SDK exposes runtime service lifecycle, health, status, and control-plan methods over the API operation registry. The transport remains abstract; unconfigured clients receive unavailable envelopes rather than fake service state.

Wave 22D3 extends runtime lifecycle/status typing with sealed posture fields so clients can distinguish runtime liveness/readiness from operational authority.

Wave 22D6: legacy session-first flows remain supported only for compatibility. New client
integration should target client-connection/operator-context and active-case posture
visibility as the canonical direction.

Wave 22D7: runtime-service boundary contracts separate service lifecycle from operational readiness.
Client UX should not treat runtime running/healthy as operator-authorized readiness.

Wave 22D8: SDK may carry `account_ref`/`entitlement_ref`/`auth_context` posture data when exposed by runtime contracts,
but SDK is not an account-product SDK and does not own billing/login backend flows.
