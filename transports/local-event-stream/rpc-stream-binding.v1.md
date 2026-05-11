# Local Event Stream RPC Stream Binding v1

## Purpose

Define RPC streaming over `local_ipc_rpc` as the primary native-local binding
for `local_event_stream`.

## Rules

- RPC stream uses Local IPC RPC framing as carrier.
- Payloads still follow API.03 watch-event and Local Event Stream event frame
  semantics.
- RPC streaming is the target native-local binding for CLI, Loom, TUI, and
  future native clients.
- Stream payload semantics remain API-owned even when the carrier is IPC RPC.

## Boundary

- API.06 defines stream payload semantics only.
- No RPC stream implementation is added here.
