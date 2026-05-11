# Native/C SDK Package

This is the native C SDK package for YAI (`packages/c`).

This package lives in `interfaces/packages/c` and preserves public include
prefix `<yai_sdk/...>`. It is an official SDK package projection over YAI
Interfaces protocol truth; it does not define protocol truth.

INTF.4 validation residual: `make check-config` and `make check` were blocked
because no law compatibility export was available. The old command-id
vocabulary remains compatibility-only pending INTF.6.

Current posture:
- native/compat-heavy and transitional
- suitable for native runtime ingress, local tooling, and compatibility helpers
- not the canonical source of public SDK grammar

Canonical public SDK grammar is defined by:
- `../../registry/api-operations.v1.json`
- canonical SDK surfaces in `packages/typescript` and `packages/rust`

The C package's compatibility command, workspace, runtime, and control-call helpers
remain available, but they are not the canonical API grammar surface for new SDK
consumers.

## Contract

- Primary target for Console-compatible native clients; `yai-cli` remains a legacy command/client name.
- Uses SDK/public surfaces only.
- Must not expose `yai/core` internals as public dependency.
- Must not shell out to CLI for core SDK behavior.
- Must not own runtime execution or API ownership.
- Future cleanup should isolate compatibility/native helpers from canonical
  operation clients rather than expand workspace-era grammar.

## Build Modes

- `make`: builds SDK libraries. If `YAI_SDK_COMPAT_LAW_DIR` is not set, build uses a **transitional non-public fallback** to `../yai/include/ipc` to provide protocol headers.
- `make check-config`: strict law compatibility validation for external export.
- `make test`: law-gated; requires `make check-config` to pass.

## Law Compatibility Build Input

Required variable for full compatibility checks/tests:
- `YAI_SDK_COMPAT_LAW_DIR`

Expected path inside that directory:
- `contracts/protocol/include/protocol.h`

Validation:
```sh
make check-config
```

Build/Test:
```sh
make clean || true
make
make test || true
```
