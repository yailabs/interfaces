# Enterprise SDK Standard

SDK role:
- official client consumption layer
- consumes API contracts from `../api`
- does not own runtime implementation
- serves product clients (Console/Design/Desktop/VSCode), legacy CLI/native compatibility clients, and automation/integration clients

Client adoption posture:
- migration planning is active
- direct runtime adapter usage is exception-only (`debug-conformance-bootstrap-only`)
- this wave does not claim all clients already migrated


Design consumer repository path: `../design` (product identity: YAI Design).


Wave 16B note: TypeScript plane clients are aligned to `../api/registry/api-operations.v1.json`.
SDK transport remains abstract unless explicitly configured.

Wave 17/A1: Console consumes SDK plane clients directly through typed operations with readiness envelopes. Loom is a legacy name.


## Wave 21 runtime service lifecycle note

The TypeScript SDK exposes runtime service lifecycle, health, status, and control-plan methods over the API operation registry. The transport remains abstract; unconfigured clients receive unavailable envelopes rather than fake service state.

Wave 22D3 note: sealed runtime posture is represented in the same typed contract.
SDK clients must not interpret runtime alive/healthy as automatic operational authority.

Wave 22D7 note: SDK runtime surfaces distinguish service lifecycle from operational readiness.
No system service manager integration is assumed by SDK contracts.

Wave 22D8 note: identity/account fields in SDK are posture/reference contracts.
SDK does not implement account backend, billing, OAuth provider, or credential persistence.
