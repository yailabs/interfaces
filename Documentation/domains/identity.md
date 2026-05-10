# Identity Domain

The identity domain documents API-facing auth, principal, account, machine, entitlement, license, lease, and safe status projection boundaries.

This is an upstream API contract domain. It is not a native YAI runtime source plane. The runtime consumes bounded access projections from these contracts through `../yai/src/runtime/access`.

## Absorbed Semantics

- Principal model and no-hidden-session boundary.
- Auth status, local development auth, provider status, device login start, and logout operations.
- Machine identity, enrollment, authorization, lease consumption, revocation, offline grace, and account-scoped limit projections.
- Privacy-bounded machine evidence and safe status projection.

## Artifact References

- `schemas/auth-operation.v1.schema.json`
- `schemas/client-subject-ref.v1.schema.json`
- `schemas/local-machine-identity-store.v1.schema.json`
- `schemas/machine-enrollment-client-flow.v1.schema.json`
- `schemas/machine-authorization-consumption.v1.schema.json`
- `schemas/license-lease-consumption.v1.schema.json`
- `fixtures/auth-operation/`
