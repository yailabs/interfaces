# API Mirror Sync Policy (Wave 13B)

## Canonical and Mirror Roles

- Canonical API contract repository after Wave 13: `../api`.
- Temporary in-repo compatibility mirror: `yai/api`.
- Runtime implementation source of truth: `yai` (`core/`, `include/`, `experience/clients/cli` integration points).
- Wave 14 SDK source: `../api`.

## Scope Ownership

- Contract/docs/schema/envelope/lifecycle changes should be authored against `../api` first.
- `yai/api` must mirror canonical contract changes when compatibility/build consumers still depend on local paths.
- API family implementation C files remain implementation-owned in `yai` unless explicitly converted to contract-only reference material.

## Safety Rules

- Do not destructively remove `yai/api` while runtime/build consumers still compile or include from `api/`.
- Do not introduce divergent manual edits in only one mirror without updating extraction manifests.
- Do not create or promote `core/api` as canonical API architecture.
- Runtime implementation is not moved in Wave 13B.

## Drain Gate

`yai/api` can be fully drained only after:
- runtime/build consumer audit is complete and green,
- include and Makefile dependencies on `api/` are migrated or replaced,
- compatibility surfaces are explicitly retired with verification.


## 13C Ownership Clarification

- `../api` owns contract surfaces.
- `yai/api` does not own canonical contracts.
- `yai/api` retains runtime adapters and compatibility mirror surfaces until consumer migration is complete.


Wave 13D: mirrorBackToYaiApi=false because root `yai/api/` no longer exists.
