# Error Transport Map v1

## Purpose

Clarify how API error objects relate to transport classes without collapsing
transport failure into operation failure.

## Rule

- Request/response transports carry response envelopes whose `error` field uses
  the canonical API error model.
- `local_event_stream` carries stream event frames whose `error` field uses the
  same canonical API error model.
- Transport setup, reachability, decode, and framing failures must remain
  classifiable as transport errors.
- Operation guard, validation, availability, and runtime-sealed failures must
  remain classifiable as operation or guard errors.

## Transport Relationship

- `local_ipc_rpc`: request envelope, response envelope, and RPC stream frames
- `local_http_loopback`: request envelope and response envelope
- `local_event_stream`: stream event frames only
- `lan_secure`: same envelope/frame contract as local transports, but paired and
  gated
- `remote_https`: request/response envelope contract where mapping allows

Provider/model transport remains excluded from client-runtime API error framing.
