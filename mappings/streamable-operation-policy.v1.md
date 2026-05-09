# Streamable Operation Policy v1

## Purpose

This policy separates realtime event delivery from ordinary request/response
transport.

## Rule

- `local_event_stream` is only for streamable/watch/tail/status-event
  operations.
- Generic request/response operations must not use `local_event_stream` as
  their default transport.
- RT.04 and A1 Local IPC RPC coverage markers do not widen stream support;
  request/response IPC audit must not be misread as Local Event Stream
  implementation coverage.
- `local_event_stream` may carry only stream event frames.
- Stream frames must not be treated as normal response envelopes.

## Current Streamable Registry Surfaces

- `case.records.tail`
- `state.records.tail`
- `workflow.runs.watch`

## Binding Model

- Web/dashboard first binding: SSE.
- Native CLI/TUI binding: streaming over `local_ipc_rpc`.
- WebSocket remains future-only and must be justified before use.

## Stream Contract

- event envelope semantics remain API-owned
- heartbeat semantics are required
- reconnect semantics are required
- terminal event and error event semantics are required
- sensitive payloads must remain projection-safe
- terminal stream frames must clearly indicate closed, cancelled, or error
  posture

See also:
- `../transports/local-event-stream.v1.md`
- `../transports/local-event-stream/README.md`
