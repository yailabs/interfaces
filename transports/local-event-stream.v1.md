# Local Event Stream v1

## Purpose

Define `local_event_stream` as the canonical realtime transport class for
runtime status, execution progress, records tail, case events, and posture
change observation.

API.06 verticalizes this transport into a dedicated contract subtree so
runtime, SDK, and client surfaces can implement bindings, subscription,
heartbeat, reconnect, redaction, and terminal-event semantics later without
inventing their own stream grammar.

## Bindings

- SSE for web/dashboard first
- RPC streaming over IPC for CLI/TUI and native clients
- WebSocket only when bidirectional realtime is explicitly justified

## Transport Relations

- `local_event_stream` is not `local_http_loopback` request/response.
- SSE may use HTTP mechanics, but emitted stream frames are not response
  envelopes.
- RPC streaming uses `local_ipc_rpc` as carrier, but stream payload semantics
  still follow Local Event Stream event frame grammar.
- Stream frames align with API.03 watch-event and stream-frame semantics.
- Terminal stream frames close streams; they are not normal operation
  responses.

## Classification

- status: primary now
- class: realtime watch/subscribe/tail transport separate from unary
  request/response calls

## Ownership

- API owns: event envelope, stream id, heartbeat, reconnect semantics,
  terminal/error event semantics
- Runtime owns: event publication, stream serving, fanout policy, dispatch from
  runtime observation sources
- SDK owns: watch/subscribe/tail client surfaces and reconnect handling

## Contract Surfaces

- `local-event-stream/README.md`
- `local-event-stream/sse-binding.v1.md`
- `local-event-stream/rpc-stream-binding.v1.md`
- `local-event-stream/websocket-reservation.v1.md`
- `local-event-stream/event-frame.v1.schema.json`
- `local-event-stream/event-types.v1.json`
- `local-event-stream/subscription-model.v1.md`
- `local-event-stream/heartbeat-reconnect.v1.md`
- `local-event-stream/backpressure-resume.v1.md`
- `local-event-stream/security-redaction.v1.md`
- `local-event-stream/errors-terminal-events.v1.md`
- `local-event-stream/conformance-profile.v1.md`

## Primary Users

- dashboard live status
- CLI tail/watch surfaces
- Loom/TUI live views
- local automation monitors

## Current Streamable Operations

- `case.records.tail`
- `state.records.tail`
- `workflow.runs.watch`

## Security Baseline

- heartbeat required
- terminal event/error semantics required
- reconnect semantics documented
- sensitive payloads must be projection-safe
- provider credentials must never appear in stream payloads
- LAN remains blocked by default unless `lan_secure` is separately enabled

## Non-goals

- not a synonym for HTTP
- not a synonym for WebSocket
- not a provider/model streaming boundary
- no SSE/WebSocket/IPC streaming implementation is added by this document
