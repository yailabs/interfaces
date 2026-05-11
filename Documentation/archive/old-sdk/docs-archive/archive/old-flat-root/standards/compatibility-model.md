# SDK Compatibility / Export Model

## Goal

Define how `sdk` consumes law-aligned information without structural dependency on live `law`.

## Allowed inputs

- exported compatibility snapshots
- generated artifacts produced by controlled tooling
- compatibility manifests with explicit version/range declaration

## Forbidden model

- treating live `law` tree as mandatory runtime dependency
- structural pinning from `sdk` to `law`

## Distinctions

- law source of truth: `law`
- exported compatibility baseline: generated snapshot/manifests used by SDK tooling
- SDK public surface: stable C APIs consumed by downstream clients
- runtime implementation target: unified `yai` runtime with workspace-first binding
  and canonical families (`core`, `exec`, `data`, `graph`, `knowledge`)

## Implementation posture

- runtime-critical SDK code must not require live repo traversal
- optional tooling may resolve external law artifacts for verification/generation
- compatibility results must be explicit and reproducible

## Architecture alignment rule

SDK compatibility behavior must preserve runtime semantics as received from `yai`
without introducing an alternate topology vocabulary. In particular:

- no active `brain`/`mind` subsystem framing
- no flattened "all ready" status when runtime reports bound/degraded splits
- workspace-bound state remains first-class in context APIs and output models

## Secure transport boundary

Compatibility contracts cover protocol/runtime semantics, not full network security.
For remote owner endpoint usage, secure peering assumptions must be satisfied by
runtime/deployment plane (for example private overlay).

## SW-2 delegated distribution boundary

SDK compatibility includes parsing and preserving owner-issued delegated edge
distribution metadata (grant/snapshot/envelope + scope/target fields) as
runtime semantics. This remains non-sovereign operational material.


## Build Contract Input

Native/C package has two explicit modes:

- Build mode (`make`): may use transitional non-public header fallback from `../yai/include/ipc` when `YAI_SDK_COMPAT_LAW_DIR` is absent.
- Compatibility gate (`make check-config`, `make test`): requires `YAI_SDK_COMPAT_LAW_DIR` with `contracts/protocol/include/protocol.h`.

Use `make check-config` in `packages/c` for deterministic diagnostics.
