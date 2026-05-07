# Local IPC RPC v1

## Purpose

Define `local_ipc_rpc` as the primary native local transport for Rust CLI,
Rust Loom/TUI, desktop/native clients, and other same-machine SDK consumers.

API.04 verticalizes this transport into a dedicated contract subtree so runtime
and SDK can implement discovery, handshake, framing, streaming, cancellation,
and security later without inventing divergent grammar.

## Binding

- Unix domain socket on macOS/Linux
- named pipe on Windows

## Classification

- status: primary now
- class: local native request/response plus native streaming

## Ownership

- API owns: operation envelope, frame contract, handshake, version negotiation,
  error mapping, stream/cancel/timeout semantics
- Runtime owns: server/listener, socket/pipe permissions, discovery hooks,
  dispatch into `runtime/boundary/api`
- SDK owns: client transport, discovery, request framing, response decoding,
  stream reader, transport errors

## Contract Surfaces

- `local-ipc-rpc/README.md`
- `local-ipc-rpc/discovery.v1.md`
- `local-ipc-rpc/handshake.v1.md`
- `local-ipc-rpc/frame.v1.schema.json`
- `local-ipc-rpc/frame-model.v1.md`
- `local-ipc-rpc/message-types.v1.json`
- `local-ipc-rpc/security.v1.md`
- `local-ipc-rpc/streaming.v1.md`
- `local-ipc-rpc/cancellation-timeout.v1.md`
- `local-ipc-rpc/errors.v1.md`
- `local-ipc-rpc/platform-bindings.v1.md`
- `local-ipc-rpc/conformance-profile.v1.md`

## Primary Users

- Rust CLI
- Rust Loom/TUI
- desktop/native local clients
- local automation where native same-host access is preferred

## Security Baseline

- socket/pipe permissions required
- same-user local access by default
- version handshake required
- no remote exposure
- same-machine only
- no LAN
- no default world-writable socket
- no provider credentials sent over client-runtime transport

## Non-goals

- not a LAN listener
- not a provider/model transport
- not a subprocess/stdout compatibility shim
- no implementation is added by this document
