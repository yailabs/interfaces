# Family Availability

Source of truth: API contract family mapping and contract status.

Client adoption note:
- family availability informs SDK migration sequencing.
- unavailable/deferred families must not be represented as completed in client migration plans.


Design consumer repository path: `../design` (product identity: YAI Design).


Wave 16B note: TypeScript and Rust canonical clients follow `../api/registry/api-operations.v1.json`.
SDK transport remains abstract unless explicitly configured.

Wave 17/A1: Console consumes SDK plane clients directly through typed operations with readiness envelopes.

Wave 22D6: session-oriented client usage is compatibility-only. New client adoption should
prefer system/runtime posture plus client connection/operator context surfaces.

## Rust SDK Family Availability (CLI Core)

- system: transport-backed when endpoint listener is active (`system.status`)
- session: transport-backed when endpoint listener is active (`session.status`)
- case: transport-backed when endpoint listener is active (`case.current`)
- providers: transport-backed when endpoint listener is active (`providers.list`)
- models: transport-backed when endpoint listener is active (`models.list`)
- conversation: seed surface present for `conversation.current`
- prompting: seed surface present for `prompting.context.assemble`

Compatibility aliases remain available for `runtime` and singular `provider`, but only as naming shims over canonical surfaces.

Listener contract used for local verification: `http://127.0.0.1:7410` served by `yai --api-only` in the runtime repo.
