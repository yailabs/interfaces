# Implementation Readiness Matrix v1

## Purpose

Summarize which frozen API transport contracts are ready to hand off into
runtime and SDK implementation waves, and which remain controlled future,
separate-boundary, test-only, or compatibility-only.

## Readiness Table

| Transport | Contract status | Implementation priority | Runtime readiness | SDK readiness | Client default | Next runtime wave | Next SDK wave | Next client wave |
| --------- | --------------- | ----------------------- | ----------------- | ------------- | -------------- | ----------------- | ------------- | ---------------- |
| `local_ipc_rpc` | frozen | primary_now | ready_for_implementation | ready_for_client_implementation | cli_loom_native | `RT.01 / RT.02` | `SDK.01` | `CLI.01 / LOOM.01` |
| `local_http_loopback` | frozen | primary_now | ready_for_implementation | ready_for_client_implementation | dashboard_web | `RT.03` | `SDK.02` | `WEB.01` |
| `local_event_stream` | frozen | primary_now | ready_for_implementation | ready_for_client_implementation | realtime | `RT.04` | `SDK.03` | `WEB.01 / CLI.01 / LOOM.01` |
| `lan_secure` | frozen | controlled_future | future_only | future_only | none | none | none | none |
| `remote_https` | frozen | controlled_future | future_only | future_only | none | none | none | none |
| `provider_transport_boundary` | frozen | separate_boundary | separate_provider_boundary | separate_provider_boundary | none | none | none | none |
| `in_process_test` | frozen | test_only | not_product | test_only | none | none | none | none |
| `subprocess_stdio_compat` | frozen | compat_only | not_product | compat_only | none | none | none | none |

## Readiness Notes

- `local_ipc_rpc` is the first implementation candidate for runtime and Rust
  SDK work.
- `local_http_loopback` and `local_event_stream` remain primary product
  transports, but follow after the native-local path in the named handoff
  sequence.
- `lan_secure` and `remote_https` are frozen as controlled future boundaries,
  not default implementation targets.
- `provider_transport_boundary` remains outside client-runtime transport
  implementation.
- `in_process_test` and `subprocess_stdio_compat` remain non-product
  boundaries.

## Source

Machine-readable form: `implementation-readiness-matrix.v1.json`
