# API Mirror Sync Policy (Historical)

Current status: superseded by `interfaces`.

The former `api` repository name has been replaced by `interfaces`. The former
root `yai/api` compatibility mirror is not the canonical contract source.

## Canonical and Mirror Roles

- Canonical developer-interface repository: `interfaces`.
- Temporary in-repo compatibility mirror: historical `yai/api`.
- Runtime implementation source of truth: `yai` (`core/`, `include/`, `experience/clients/cli` integration points).
- SDK package source: `interfaces/packages`.

## Scope Ownership

- Contract/docs/schema/envelope/lifecycle changes should be authored against
  `interfaces` first.
- Historical `yai/api` mirror references must not define canonical contracts.
- API family implementation C files remain implementation-owned in `yai` unless explicitly converted to contract-only reference material.

## Safety Rules

- Do not destructively remove `yai/api` while runtime/build consumers still compile or include from `api/`.
- Do not introduce divergent manual edits in only one mirror without updating extraction manifests.
- Do not create or promote `core/api` as canonical API architecture.
- Runtime implementation is not moved in Wave 13B.

## Drain Gate

Historical `yai/api` compatibility material can be fully retired only after:
- runtime/build consumer audit is complete and green,
- include and Makefile dependencies on `api/` are migrated or replaced,
- compatibility surfaces are explicitly retired with verification.


## 13C Ownership Clarification

- `interfaces` owns contract surfaces.
- Historical `yai/api` does not own canonical contracts.
- Any remaining `yai/api` references are compatibility/runtime-adapter debt, not
  interface truth.


Wave 13D: mirrorBackToYaiApi=false because root `yai/api/` no longer exists.
