# YAI SDK Surface Contract

## Scope

Defines stable public API commitments for `sdk` after SDK-1 public-surface
realignment.

## Canonical public surface center

Primary canonical public headers:

- `include/yai_sdk/public.h`
- `include/yai_sdk/core.h`
- `include/yai_sdk/runtime.h`
- `include/yai_sdk/models.h`
- `include/yai_sdk/transport.h`
- `include/yai_sdk/workspace.h`
- `include/yai_sdk/exec.h`
- `include/yai_sdk/db.h`
- `include/yai_sdk/data.h`
- `include/yai_sdk/graph.h`
- `include/yai_sdk/knowledge.h`
- `include/yai_sdk/source.h`
- `include/yai_sdk/policy.h`
- `include/yai_sdk/recovery.h`
- `include/yai_sdk/debug.h`
- `include/yai_sdk/governance.h`

## Unified runtime model commitments

The SDK public contract must expose one runtime model only:

- unified runtime
- workspace-first binding
- canonical runtime families: `core`, `exec`, `data`, `graph`, `knowledge`

SDK public contract must not reintroduce legacy subsystem topology as canonical
consumer model.

## Compatibility posture

Compatibility headers remain supported for consumer continuity, but are
non-canonical for new API design:

- `client`, `context`, `paths`, `catalog`, `protocol`, `rpc`, `reply`

Compatibility aliases must remain thin and must not create a second documented
public taxonomy.

## Registry posture

`include/yai_sdk/registry/*` is not default public-stable surface.
It is internal/advanced compatibility support and may change more aggressively.

## Dependency posture

SDK surface must remain usable without structural pinning to live `law` repo.
Compatibility is declared via version/compat docs and optional exported artifact
workflows.

## SDK-2 model commitments

Client contracts must expose canonical runtime truth:

- runtime liveness distinct from capability readiness
- workspace binding distinct from workspace selection
- capability-family state modeled for `exec`, `data`, `graph`, `knowledge`
- governance/attachability state modeled without legacy subsystem topology
- runtime target resolution modeled explicitly (default local, explicit local endpoint, explicit owner endpoint)

Compatibility JSON-only call paths remain supported but are non-canonical for new consumers.

## DX-1 target and scope contract

SDK public contract distinguishes:

- runtime target identity (owner/edge/mesh/overlay remote)
- transport locator/endpoint details
- delegated scope and validity metadata

Consumers must not collapse these dimensions into a single generic target field.
