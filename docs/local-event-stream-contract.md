# Local Event Stream Contract

## Purpose

API.06 defines `local_event_stream` as the primary realtime projection
transport contract before implementation.

## Contract Summary

- primary web binding: SSE
- primary native-local binding: RPC streaming over `local_ipc_rpc`
- WebSocket is reserved for future bidirectional realtime only
- stream frames follow a dedicated event-frame grammar aligned to API.03 and
  are not response envelopes
- current streamable operations remain `case.records.tail`,
  `state.records.tail`, and `workflow.runs.watch`
- heartbeat, reconnect, resume posture, backpressure, redaction, and terminal
  event semantics are explicit
- `local_event_stream` is separate from Local HTTP Loopback request/response
  even when SSE uses HTTP mechanics

## Ownership

- API owns the `local_event_stream` contract.
- Runtime implements publication and serving later.
- SDK implements stream clients later.
- Provider or model transport remains separate.
