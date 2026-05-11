# Local Event Stream Contract

`api/transports/local-event-stream/` holds the verticalized API.06 contract for
the `local_event_stream` transport class.

Purpose:
- define the primary realtime projection channel for runtime status,
  watch/tail, execution progress, and live observation
- freeze binding, event frame, subscription, heartbeat, reconnect,
  backpressure, redaction, and terminal-error posture before implementation
- keep API.03 stream frames separate from normal response envelopes

Binding split:
- SSE is the primary web or dashboard binding
- RPC streaming over `local_ipc_rpc` is the primary native-local binding
- WebSocket is reserved for future bidirectional realtime only

Current streamable operations:
- `case.records.tail`
- `state.records.tail`
- `workflow.runs.watch`

Primary consumers:
- dashboard and browser runtime status panels
- Loom or TUI live panels
- CLI watch or tail commands later
- desktop or native clients later
- local automation monitors later

Boundary:
- API defines the stream contract only.
- Runtime implements publication and serving later.
- SDK implements stream clients later.
- No SSE server, WebSocket server, RPC stream transport, or runtime event bus
  behavior is added here.
