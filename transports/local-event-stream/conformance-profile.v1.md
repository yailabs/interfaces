# Local Event Stream Conformance Profile v1

## Purpose

Define the minimum contract claims that a future `local_event_stream`
implementation must satisfy.

## Required Contract Areas

- SSE primary web binding
- RPC stream over `local_ipc_rpc` primary native-local binding
- WebSocket reserved but not primary
- event frame schema and event-type registry
- subscription model for existing streamable operations only
- heartbeat, reconnect, and explicit resume posture
- backpressure, dropped-event, and terminal-error posture
- projection-safe and redacted payload posture

## Out of Scope for API.06

- SSE server implementation
- WebSocket server implementation
- RPC streaming implementation
- runtime event bus implementation
- SDK stream client implementation
