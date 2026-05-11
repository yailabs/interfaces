# Local IPC RPC Cancellation and Timeout v1

## Purpose

Freeze request-scoped timeout and cancellation semantics for `local_ipc_rpc`.

## Timeout

- timeout is request-scoped
- timeout may be expressed through API.03 `timeout_ms`
- transport timeout must remain distinguishable from operation timeout

## Cancellation

- cancellation uses `cancellation_ref` or `request_id`
- `cancel.request` is advisory unless runtime confirms it
- cancellation confirmation or refusal flows back through response or stream
  semantics, not by inventing a second grammar

## Boundary

- API owns the timeout/cancellation contract.
- Runtime implements cancellation behavior later.
- SDK implements client-side timeout and cancel framing later.
