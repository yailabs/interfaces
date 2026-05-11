# In-process Test and Subprocess Compat Boundary

## Purpose

API.08 separates test-only in-process harness transport from compatibility-only
subprocess stdio transport and keeps both distinct from canonical product
transports.

## Boundary Split

| Boundary | Role | Default posture | Notes |
| -------- | ---- | --------------- | ----- |
| Local IPC RPC | native-local product transport | primary native | Console target |
| Local HTTP Loopback | browser or dashboard product transport | primary browser/dev | request-response only |
| Local Event Stream | realtime product transport | primary realtime | not response envelope |
| In-process Test | direct harness or conformance transport | test-only | non-product |
| Subprocess Stdio Compat | process-invocation compatibility transport | compat-only | not canonical |
| Provider Transport | runtime -> provider/model | separate | not client-runtime |

## Key Rules

- `in_process_test` is for harness, conformance, and dev-only simulation.
- `subprocess_stdio_compat` is for legacy, debug, and migration compatibility.
- neither replaces Local IPC RPC, Local HTTP Loopback, or Local Event Stream.
- neither bypasses API envelopes, operation mapping, runtime guards, or
  provider boundaries.
