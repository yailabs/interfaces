# Runtime Implementation Boundary

The API defines contracts that runtime adapters implement. It does not define runtime internal architecture.

## API Side

- Operation ids and request/response schemas.
- Envelope, error, readiness, and stream frame shape.
- Transport mapping and exposure policy.
- Conformance checks for the API contract.

## Runtime Side

- Handler implementation.
- Service lifecycle and process management.
- State stores, gates, providers, agents, jobs, leases, and machine-local behavior.
- Runtime enforcement and operational posture.

Runtime truth is documented in `../yai/Documentation`. API domain docs describe only the externally visible projection.
