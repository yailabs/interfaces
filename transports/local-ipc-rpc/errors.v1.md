# Local IPC RPC Errors v1

## Purpose

Preserve the distinction between transport errors and operation errors for
`local_ipc_rpc`.

## Rules

- transport errors and operation errors remain distinct
- IPC frame decode errors are transport errors
- handshake rejection is a transport negotiation error
- permission denied at socket or pipe level is a transport/security error
- runtime sealed and guard failures are operation or guard errors carried in
  API.03 response envelopes
- provider/model errors must not leak raw provider transport frames

## Examples

- malformed frame payload: transport error
- version mismatch: transport error
- runtime unavailable after endpoint discovery: transport error
- validation failure inside an accepted operation: operation error
- forbidden or sealed operation: guard or operation error
