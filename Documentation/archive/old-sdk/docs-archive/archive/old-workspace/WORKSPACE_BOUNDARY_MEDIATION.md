# SDK Workspace Boundary Mediation (WS-11)

Canonical chain: `cli -> sdk -> yai`.

## SDK Responsibilities

- resolve command/catalog surfaces from compatibility registry
- build/forward control calls without leaking runtime internals into CLI
- preserve workspace descriptors and execution/degraded fields from runtime replies
- expose deterministic error codes for stale/invalid/degraded contexts
- preserve canonical readiness dimensions in consumer-facing models:
  - runtime reachable/liveness
  - workspace selected
  - workspace-bound capability readiness (ready/degraded/unbound)

## Non-Responsibilities

- owning runtime enforcement logic
- duplicating workspace containment rules from runtime
- embedding command-topology truth that belongs to law/runtime contracts

## Drift Guardrails

- API boundary check fails if CLI includes SDK internal registry headers
- API boundary check fails if CLI regresses to legacy workspace command IDs
- API/output checks fail if reply mediation collapses bound/degraded/unbound
  semantics into a single generic ready flag
