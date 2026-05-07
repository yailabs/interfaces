# Local IPC RPC Streaming v1

## Purpose

Define how `local_ipc_rpc` carries realtime stream traffic for streamable
operations.

## Rules

- RPC streaming is allowed only for operations marked streamable in API.02.
- Stream frames must carry API.03 watch-event frame payloads.
- `stream.open` acknowledges stream startup.
- `stream.frame` carries non-terminal or terminal API.03 watch-event payloads.
- `stream.close` communicates explicit terminal closure posture.
- `heartbeat` is required for long-lived stream continuity.

## Semantics

- Heartbeat and terminal semantics must align with API.03 watch-event rules.
- Stream traffic does not turn generic request/response operations into stream
  operations.
- Provider/model frames are never exposed as client-runtime stream payloads.
