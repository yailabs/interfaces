# Local IPC RPC Frame Model v1

## Purpose

Define the transport frame wrapper that carries API.03 request envelopes,
response envelopes, handshake payloads, and watch-event stream frames over
`local_ipc_rpc`.

## Frame Fields

- `frame_schema`
- `frame_id`
- `frame_type`
- `frame_version`
- `request_id` (optional)
- `correlation_id` (optional)
- `stream_id` (optional)
- `sequence` (optional)
- `payload_encoding`
- `payload`
- `payload_size`
- `flags` (optional)
- `created_at` (optional)

## Payload Contract

- `operation.request` carries API.03 request-envelope payloads.
- `operation.response` carries API.03 response-envelope payloads.
- `stream.frame` carries API.03 watch-event payloads.
- `error` carries transport-level error payloads for frame/decode/handshake
  failures.

## Payload Encoding

- JSON is required for v1.
- Binary payload support is reserved and not implemented.
- Large-payload chunking is deferred.
