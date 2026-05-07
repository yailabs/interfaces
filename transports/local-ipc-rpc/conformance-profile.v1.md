# Local IPC RPC Conformance Profile v1

## Purpose

Define the minimum contract claims that a future `local_ipc_rpc`
implementation must satisfy.

## Required Contract Areas

- discovery order and error classification
- version handshake
- frame schema and message types
- JSON payload encoding for v1
- API.03 request/response/watch-event carriage
- same-machine and no-LAN security posture
- timeout and cancellation semantics
- separation of transport error from operation error

## Out of Scope for API.04

- IPC listener implementation
- Unix domain socket server implementation
- Windows named pipe server implementation
- SDK `LocalIpcRpcTransport`
- CLI or Loom default transport switch
