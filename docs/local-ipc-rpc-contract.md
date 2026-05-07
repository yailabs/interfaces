# Local IPC RPC Contract

## Purpose

API.04 defines `local_ipc_rpc` as the primary native-local client-runtime
transport contract before implementation.

## Contract Summary

- platform bindings: Unix domain socket on macOS/Linux, named pipe on Windows
- discovery order: explicit config, environment override, discovery file,
  platform default, then not configured
- handshake: transport, frame, envelope, client, stream-mode, and capability
  negotiation
- frame model: a transport frame wrapper carrying API.03 request envelopes,
  response envelopes, and watch-event frames
- stream behavior: allowed only for API.02 streamable operations
- security posture: same-machine only, no LAN, same-user default, version
  handshake, no provider credential leakage

## Ownership

- API owns the `local_ipc_rpc` contract.
- Runtime implements the server/listener later.
- SDK implements the client transport later.
- CLI and Loom consume SDK later.

## See Also

- `../transports/local-ipc-rpc.v1.md`
- `../transports/local-ipc-rpc/README.md`
- `../transports/local-ipc-rpc/discovery.v1.md`
- `../transports/local-ipc-rpc/handshake.v1.md`
- `../transports/local-ipc-rpc/frame-model.v1.md`
- `../transports/local-ipc-rpc/security.v1.md`
- `../transports/local-ipc-rpc/streaming.v1.md`
- `../transports/local-ipc-rpc/cancellation-timeout.v1.md`
- `../transports/local-ipc-rpc/errors.v1.md`
