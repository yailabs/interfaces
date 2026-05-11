# Refoundation Phase 3C — C SDK Compat Isolation / C SDK Boundary Plan

## Executive Verdict

The C SDK is still valuable as a native transport and compatibility layer, but it is
not ready to serve as the canonical public SDK grammar surface for the refoundation
stack.

Phase 3B moved canonical public grammar into the TypeScript and Rust SDK packages,
aligned to `../api/registry/api-operations.v1.json`. Phase 3C confirms that the C
package should be treated as `compat-native-transitional` until its public headers,
typed helpers, and registry/tooling surfaces are partitioned more aggressively.

This means Phase 4 CLI Rust migration should depend on the canonical Rust SDK
surfaces and API registry, not on the C SDK's runtime/workspace-era grammar.

## C SDK Public Headers Classification

### Canonical-native transport or client-adjacent

- `include/yai_sdk/client.h`
  - low-level client handle and request entrypoints
  - explicitly labels itself as a compatibility low-level API
- `include/yai_sdk/transport.h`
  - runtime endpoint and local UDS locator model
  - transport/native, not API-registry grammar
- `include/yai_sdk/protocol.h`
  - protocol reply mapping helper
  - narrow internal/public utility, not canonical grammar

### Transitional runtime/workspace grammar

- `include/yai_sdk/public.h`
  - still presents a broad unified runtime/workspace taxonomy as the umbrella public
    surface
- `include/yai_sdk/runtime.h`
  - defines `yai.control.call.v1`, `runtime` target plane, and runtime command ids
- `include/yai_sdk/source.h`
  - typed source-plane helpers, but still built over runtime control-call envelopes
    and workspace-era aliases
- `include/yai_sdk/workspace.h`, `exec.h`, `db.h`, `data.h`, `graph.h`,
  `knowledge.h`, `policy.h`, `recovery.h`, `debug.h`
  - expose a workspace-command family model that does not map cleanly to the
    canonical API registry families

### Tooling/registry compatibility headers

- `include/yai_sdk/registry/registry.h`
  - already marked as internal compatibility/tooling surface
  - entrypoint for `yai law ...`, not a stable public SDK API
- `include/yai_sdk/registry/*`
  - law/registry metadata and validation helpers
  - compatibility/tooling surfaces, not canonical client grammar

## C SDK Source Classification

### Native transport/runtime ingress layer

- `src/client/client.c`
  - manages local UDS client lifecycle, authority role state, handshake, raw control
    call JSON path, and typed control-call path
- `src/rpc/rpc_client.c`
  - direct AF_UNIX RPC envelope transport to runtime ingress
- `src/platform/transport.c`
  - runtime endpoint resolution and owner-ref handling
- `src/platform/paths.c`
  - local runtime home, ingress socket, binary lookup, and install-root detection

### Transitional typed helper/model layer

- `src/source/source.c`
  - typed source helpers, but still constructs raw `yai.control.call.v1` runtime
    requests under the hood
- `src/models/runtime_models.c`
  - parses replies into runtime/governance/workspace-era state models using
    command-id heuristics such as `workspace.run` and `workspace.graph.summary`

### Compatibility law/registry/tooling layer

- `src/registry/registry.c`
  - effectively a `law` tooling/CLI helper surface
- `src/registry/registry_*`
  - governable-object registry, help, query, cache, load, validate
- `src/catalog/catalog.c`
  - command-catalog surface built around law/command metadata rather than the
    canonical API registry

## Compat/Native vs Canonical Boundaries

### What can remain native/compat

- local UDS transport and owner-ref resolution
- low-level client lifecycle and handshake behavior
- typed runtime/governance reply parsing utilities
- compatibility/raw JSON control-call fallback
- law/registry tooling, if clearly labeled internal/tooling only

### What must not define canonical public SDK grammar

- runtime/workspace command ids such as `yai.runtime.*` and `yai.workspace.*`
- broad workspace family wrappers presented as canonical API families
- control-call envelope type/target-plane constants as the default public grammar
- law/registry command catalogs as the source of canonical operation identity

### Canonical source of truth

Canonical public grammar should remain owned by:
- `../api/registry/api-operations.v1.json`
- `../api/registry/api-surfaces.v1.json`
- canonical TypeScript/Rust SDK surfaces introduced in Phase 3B

## Direct Runtime Coupling Inventory

Verified direct runtime/native coupling points:

- `packages/c/Makefile`
  - transitional fallback to `../yai/include/ipc` when no external law export is
    configured
- `packages/c/src/platform/paths.c`
  - probes `dist/bin`, `build/bin`, and `../yai/dist/bin` / `../yai/build/bin`
- `packages/c/src/rpc/rpc_client.c`
  - direct AF_UNIX transport to runtime ingress socket
- `packages/c/src/client/client.c`
  - opens runtime ingress directly and emits `runtime` target-plane requests
- `packages/c/src/source/source.c`
  - constructs raw `yai.control.call.v1` payloads targeting `runtime`
- `packages/c/src/registry/registry.c`
  - defaults registry/law discovery to `../law`

These are acceptable for a native compatibility layer, but they confirm that the C
package is not a pure canonical SDK operation client today.

## Operation Grammar Drift Inventory

### Drift from canonical API registry

Observed C-facing grammar still emphasizes:
- `runtime`
- `workspace`
- command ids like `yai.runtime.ping`, `yai.workspace.query`, `yai.workspace.run`
- policy/debug/recovery families expressed as workspace command helpers
- control-call envelope and target-plane fields instead of operation ids

### Canonical API registry contrast

The API registry now defines canonical families such as:
- `system`
- `case`
- `conversation`
- `prompting`
- `workflow`
- `governance`
- `control`
- `knowledge`
- `state`
- `providers`
- `models`
- `agents`
- `orchestrator`
- `output`
- `session`

The C SDK does not presently expose those families as its primary typed public
surface model.

## Risk to Rust CLI Migration

### Low risk if CLI depends on canonical Rust SDK

The CLI already depends on `yai-sdk-rust` in `Cargo.toml`. That is the right
migration anchor.

### Medium risk if CLI semantics keep following older SDK/C grammar

CLI still contains pre-Phase-3B drift such as:
- `runtime.status.inspect`
- `session.status.inspect`
- `case.current.inspect`
- `provider.list.inspect`
- help/registry text that still says `runtime` and singular `provider`

That drift is now a CLI migration problem, not a reason to keep the C SDK as the
canonical grammar source.

### High risk if C SDK remains bundled conceptually with canonical client grammar

If the C package continues to be described as the canonical native SDK grammar
surface, CLI migration could inherit:
- workspace-era command vocabulary
- runtime/control-call centric transport assumptions
- law/registry catalog dependence
- direct runtime binary and ingress resolution assumptions

## Required Isolation Plan

### Boundary decision

Treat `packages/c` as:
- `compat-native-transitional`

### Isolation goals

1. Keep native transport and low-level client lifecycle available.
2. Keep compatibility headers and workspace-era helpers buildable.
3. Stop presenting them as canonical API grammar for new consumers.
4. Partition tooling/law/catalog headers from public client headers more clearly.
5. Introduce a future canonical-operation client slice only after API-registry-backed
   operation mapping is explicit.

### Concrete follow-up steps

1. Mark public umbrella and README surfaces as compat/native-transitional.
2. Split headers into three documented classes:
   - native transport/client core
   - compatibility typed helpers
   - tooling/registry internal surfaces
3. Move `registry/law` entrypoints out of any implied public-stable surface story.
4. Add a dedicated API-registry-backed C operation client layer only if it becomes
   strategically necessary.
5. Keep CLI migration pinned to Rust SDK canonical surfaces, not C wrappers.

## Recommended Future Patch Waves

### Preferred next phase

- `Phase 4A — CLI Rust Migration Plan Against Canonical SDK`

This is now viable because canonical SDK grammar lives in Rust/TypeScript, and the
C package has been classified as a non-canonical native/compat layer.

### If more C preparation is required first

- `Phase 3D — C SDK Compat Boundary Annotation / Header Partition`

That phase should:
- annotate public headers by posture
- isolate tooling/registry headers from public install narratives
- keep build/test behavior intact
- avoid transport rewrites

## What Was Not Changed

- no C transport rewrite
- no C header removals
- no API registry changes
- no CLI implementation changes
- no `yai` implementation changes
- no TypeScript/Rust canonical surface changes
