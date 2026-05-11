# SDK Alignment Model (DX-1)

## Purpose

Define how `yai-sdk` aligns with the refounded YAI architecture so SDK surfaces
encode the governed domain model instead of flattening it into generic runtime
calls.

## Canonical thesis

SDK is a domain-faithful programmatic surface, not a thin wrapper over scattered
payloads.

## Target model alignment

DX-1 introduces explicit target distinctions:

- workspace owner target
- subordinate edge runtime target
- mesh peer target
- overlay-aware remote owner target
- overlay-aware remote peer target

Locator and identity remain distinct:

- node/runtime identity says *what* the target is
- locator/endpoint says *where* it is reached
- authority scope says *what* it is allowed to do

## Policy/delegation alignment

SDK must represent delegated distribution classes explicitly:

- policy snapshot
- enrollment grant
- capability envelope
- delegated scopes (observation/mediation/enforcement)
- validity/freshness indicators

## Query/inspect alignment

SDK model supports normalized consumption of owner-side inspect summaries for:

- source/edge runtime state
- mesh coordination/authority state
- transport/ingress/overlay condition
- governed case-state projections

## Mesh and overlay alignment

SDK semantics are mesh-aware and overlay-aware without collapsing boundaries:

- discovery/coordination/authority are distinct planes
- overlay reachability does not imply legitimacy
- remote reachability does not imply delegated scope validity

## Grounded state compatibility

SDK surfaces remain compatible with governed AI grounding by carrying
summary/graph-ready, provenance-aware state classes from owner-side runtime
projections.

## Guardrails

- do not flatten owner/edge/mesh/overlay targets into one generic target kind
- do not conflate locator with legitimacy
- do not expose transport state as authority state
- do not force CLI to invent semantics absent from SDK domain model
