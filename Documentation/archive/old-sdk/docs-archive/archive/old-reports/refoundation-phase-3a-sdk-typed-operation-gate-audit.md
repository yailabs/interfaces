# Refoundation Phase 3A — SDK Typed Operation Gate Audit

## 1. Executive verdict

SDK is aligned enough to start Phase 3B typed-surface cleanup, but it is not
safe to present current TypeScript or Rust operation constants as canonical API
grammar.

- Canonical source is stable enough: `../api` now exposes `workflow`,
  `state.records`, `orchestrator`, `control`, and `system`.
- TypeScript and Rust preserve truthful unavailable behavior when transport is
  missing, which is the right boundary behavior.
- The main problem is grammar drift: several public SDK surfaces and operation
  constants still use names that are absent from the canonical API registry.

Closest package to canonical boundary discipline:
- Rust, because it is small, transport-bound, and does not import runtime
  internals directly.

Highest typed-surface drift:
- TypeScript, because it publicly exports `FlowSurface`, `RecordsSurface`,
  `RuntimeSurface`, and `SupervisorSurface` as first-path client surfaces.

Highest total legacy/coupling drift:
- C, because it remains workspace/runtime-command oriented and still has
  transitional build/runtime coupling to sibling runtime materials.

## 2. Canonical API comparison

| Canonical family/surface from api | TypeScript | Rust | C | Python | Drift notes |
|---|---|---|---|---|---|
| `system` | partial | partial | partial | no | TS/Rust expose public `runtime`, not canonical `system`; C stays runtime/workspace oriented |
| `case` | partial | partial | no | no | TS/Rust family shell exists, but current op ids are not in api registry |
| `conversation` | no | no | no | no | no surfaced client family |
| `prompting` | no | no | no | no | no surfaced client family |
| `workflow` | no | no | no | no | TS exposes legacy `flow` instead of canonical `workflow` |
| `governance` | partial | const-only | partial | no | readiness/control helpers do not match canonical api operations |
| `control` | partial | const-only | partial | no | TS/Rust use `control.readiness.inspect`, absent from api |
| `knowledge` | no | no | partial | no | C has workspace/query helpers, not canonical api family surface |
| `state` | no | const-only | no | no | TS exposes root `records`; Rust has `records_projection_list` const only |
| `skills` | no | no | no | no | missing |
| `providers` | no | partial | partial | no | Rust exposes singular `provider`; C has provider-adjacent query helpers only |
| `models` | no | partial | no | no | Rust exposes `models.list.inspect`, absent from api |
| `agents` | partial | no | no | no | TS `AgentSurface` targets non-canonical orchestration op |
| `orchestrator` | no | no | no | no | no canonical orchestrator surface; TS/Rust keep legacy orchestration naming in constants |
| `analytics` | no | no | no | no | missing |
| `output` | no | no | no | no | missing |
| `auth` | no | no | no | no | missing |
| `identity` | no | no | no | no | missing |
| `session` | no | partial | no | no | Rust has `session` surface, but `session.status.inspect` is absent from api |
| `client` | no | no | no | no | missing |

## 3. Forbidden public grammar findings

### P0 — public SDK API exposes forbidden or non-canonical primary surfaces

- TypeScript exports `FlowSurface` from `packages/typescript/src/index.ts` and
  exposes `client.flow` in `packages/typescript/src/client.ts`.
- TypeScript exports `RecordsSurface` and exposes `client.records`, preserving
  root-records public grammar instead of canonical `state.records`.
- TypeScript exports `SupervisorSurface` and exposes `client.supervisor`, even
  though it is documented as a compatibility alias over `control`.
- TypeScript exports `RuntimeSurface` and exposes `client.runtime`, while api
  canonical public family is `system`.
- Rust exports `client.runtime()` and `client.provider()` public surfaces, which
  keep pre-canonical family names (`runtime`, singular `provider`).

### P1 — operation constants are API-behind or compat-only

- TypeScript `YAI_OPERATIONS` includes:
  - `runtime.status.inspect`
  - `runtime.service.lifecycle.inspect`
  - `runtime.service.health.inspect`
  - `runtime.service.control.plan`
  - `case.watch.snapshot`
  - `case.memory.projection.inspect`
  - `records.projection.list`
  - `flow.binding.readiness.inspect`
  - `governance.readiness.inspect`
  - `control.readiness.inspect`
  - `agent.orchestration.entry.propose`
- Rust mirrors the same drift in `packages/rust/src/operations.rs`, plus
  `session.status.inspect`, `case.current.inspect`, `provider.list.inspect`, and
  `models.list.inspect`.
- A direct registry grep in `../api` found none of the TypeScript/Rust
  operation ids above in canonical api registry/docs/surface metadata.
- `supervisorReadinessInspect` is already a compat alias to
  `control.readiness.inspect`, but the target operation id is also absent from
  api, so it is a compat alias over another drifted constant.

### P2 — active docs overstate alignment

- `Documentation/standards/family-availability.md` says TypeScript plane clients are
  aligned to `../api/registry/api-operations.v1.json`.
- `Documentation/guides/client-adoption.md` repeats that alignment claim.
- `Documentation/architecture/sdk-architecture.md` and repo README still narrate public
  `runtime` and orchestration-oriented surfaces.
- `README.md` and `packages/rust/README.md` promote Rust methods backed by
  operation ids that are absent from api.

### P3 — archived/legacy residue

- `Documentation/legacy/*` still contains flow-oriented historical references, which is
  acceptable as archive residue when not treated as live surface doctrine.

## 4. TypeScript SDK audit

Current state:
- public exports: `RuntimeSurface`, `CaseSurface`, `RecordsSurface`,
  `FlowSurface`, `GovernanceSurface`, `ControlSurface`, `SupervisorSurface`,
  `AgentSurface`
- public client properties: `runtime`, `case`, `records`, `flow`,
  `governance`, `control`, `supervisor`, `agent`

Drift:
- `FlowSurface` is a direct public legacy surface and should not remain primary.
- `RecordsSurface` preserves forbidden root-records public grammar.
- `RuntimeSurface` should move behind canonical `SystemSurface` naming.
- `AgentSurface.entryProposal()` targets `agent.orchestration.entry.propose`,
  which does not exist in api and preserves legacy orchestration grammar.
- Even surfaces with canonical family names (`governance`, `control`) currently
  invoke non-canonical readiness inspect operation ids.

Boundary behavior:
- good: every surface returns `unavailableEnvelope(...)` when transport is not
  configured
- good: `execution_claim: false` and `implementation_status:
  "transport-unconfigured"` are truthful

Recommended Phase 3B patch set:
- introduce canonical public surfaces:
  - `SystemSurface`
  - `WorkflowSurface`
  - `StateSurface` or `StateRecordsSurface`
  - `ProvidersSurface`
  - `OrchestratorSurface`
- move `FlowSurface`, `RecordsSurface`, `RuntimeSurface`, and
  `SupervisorSurface` behind explicit compat exports
- replace hand-curated constants with api-registry-aligned constants only
- keep compatibility aliases only where clearly marked `compat` and only when
  backed by canonical target operations

## 5. Rust SDK audit

Current state:
- surfaced client families: `runtime`, `session`, `case`, `provider`, `models`
- no direct runtime/core imports
- transport uses `YaiTransport::invoke`

Drift:
- public family names still expose `runtime` and singular `provider`
- operation constants are API-behind, including:
  - `runtime.status.inspect`
  - `session.status.inspect`
  - `case.current.inspect`
  - `provider.list.inspect`
  - `models.list.inspect`
  - `records.projection.list`
  - `flow.binding.readiness.inspect`
  - `agent.orchestration.entry.propose`

Boundary behavior:
- good: `NotConfiguredTransport` returns `TransportNotConfigured`
- good: tests assert non-success when transport is absent
- good: no fake ready/success posture in transport layer

Loom suitability:
- transport/error discipline is good enough for Loom-facing cleanup work
- public grammar and constants need canonicalization before Phase 5 Loom
  projection depends on them as stable contract

## 6. C SDK audit

Current state:
- rich native surface centered on runtime/workspace/source/governance helpers
- public umbrella header remains `packages/c/include/yai_sdk/public.h`
- low-level client and RPC path are mature relative to other packages

Direct runtime/internal coupling risk:
- `packages/c/Makefile` still falls back to `../yai/include/ipc` in transitional
  build mode
- `packages/c/src/platform/paths.c` probes `../yai/dist/bin` and
  `../yai/build/bin`
- `packages/c/src/rpc/rpc_client.c` speaks direct runtime ingress over UDS
- `packages/c/src/client/client.c` builds raw `yai.control.call.v1` requests
- `packages/c/src/registry/registry.c` is compatibility/law oriented, not api
  operation-registry driven

API alignment posture:
- C does not currently expose canonical api family surfaces as first-class typed
  clients
- it is better described as CLI-native/runtime-adjacent SDK infrastructure than
  as an api-registry-aligned public family SDK

CLI-native suitability:
- strong for native/runtime-bound tooling
- weak for canonical api family adoption until compat layers are isolated from
  new public surface doctrine

## 7. Python SDK audit

Current state:
- package is intentionally thin
- `YaiSdkClient` is a stub
- no family surfaces are implemented

Implication:
- Python has the least public drift because it exposes almost nothing
- Python also has no meaningful canonical family coverage yet

Recommended posture:
- keep Phase 3B minimal
- add canonical client shape only after TypeScript/Rust constants and family
  names are stabilized

## 8. SDK transport / unavailable behavior

Verified:
- TypeScript returns unavailable envelopes rather than fake success when
  transport is not configured
- Rust returns `TransportNotConfigured` rather than fake success when transport
  is not configured
- C uses direct runtime RPC/open paths and does not synthesize fake success, but
  it bypasses the api operation-registry model by speaking runtime control-call
  and workspace command dialects
- Python has no active transport path

Conclusion:
- truthfulness on unavailable transport is mostly good
- operation-grammar alignment is the blocking issue, not fake execution

## 9. Required Phase 3B patch plan

1. Generate or curate canonical SDK operation constants directly from
   `../api/registry/api-operations.v1.json`.
2. Add a registry-to-SDK conformance check that fails when public SDK constants
   use forbidden grammar (`flow`, `records`, `orchestration`, root `policy`,
   runtime lifecycle control).
3. TypeScript:
   - add canonical `system`, `workflow`, `state.records`, `providers`,
     `orchestrator` surfaces
   - move `FlowSurface`, `RecordsSurface`, `RuntimeSurface`, and
     `SupervisorSurface` into explicit compat layer or compat exports
   - replace `agent.orchestration.entry.propose` with canonical agents or
     orchestrator mapping only if present in api
4. Rust:
   - replace drifted constants with api-aligned constants
   - rename public `runtime` family surface to `system`
   - rename singular `provider` to `providers`
   - keep `session` only if mapped to actual api operation ids
5. C:
   - isolate workspace/runtime command taxonomy as compat/native layer
   - prevent new canonical public SDK docs from presenting C workspace/runtime
     commands as api family model
   - reduce transitional `../yai` fallback reliance where feasible
6. Python:
   - add minimal canonical client shell only after api-aligned constant set is
     agreed

## 10. SDK -> CLI/Loom impact

Before Phase 4 CLI Rust migration:
- Rust must expose api-aligned operation constants and family names
- compat-only names must be clearly separated from canonical names
- CLI-facing consumers must not inherit `runtime`, `provider`, `flow`, or
  `supervisor` as canonical public grammar

Before Phase 5 Loom projection:
- TypeScript must stop advertising legacy surfaces as first-path exports
- Loom-facing typed surfaces should bind to canonical api families only
- readiness/unavailable behavior can remain transport-truthful, but operation
  names must match api registry

## Recommended next phase

Phase 3B — SDK Canonical Surface Cleanup / Typed Operation Constants Patch
