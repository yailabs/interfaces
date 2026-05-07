# API Envelope / Error / Stream Model

## Purpose

API.03 freezes the transport-facing wire shape used by request/response
operations, readiness/status projection payloads, API errors, and stream event
frames.

## Contract Surfaces

- `envelopes/`
- `errors/`
- `lifecycle/`
- `schemas/envelope.v1.schema.json`
- `schemas/request-envelope.v1.schema.json`
- `schemas/response-envelope.v1.schema.json`
- `schemas/error.v1.schema.json`
- `schemas/operation-result.v1.schema.json`
- `schemas/readiness-envelope.v1.schema.json`
- `schemas/watch-event.v1.schema.json`

## Model Summary

- Request/response transports carry normalized request envelopes and response
  envelopes.
- Stream transports carry stream event frames only.
- API errors distinguish transport failure, operation failure, and guard/sealed
  failure.
- Readiness/status projections remain explicit payloads rather than implicit
  success claims.

## Transport Relationship

- `local_ipc_rpc`: request envelopes, response envelopes, and RPC stream frames
- `local_http_loopback`: request envelopes and response envelopes
- `local_event_stream`: stream event frames only
- `lan_secure`: same envelope/frame contract as local transports, but gated and
  paired
- `remote_https`: same envelope/error contract where mapping allows

## Provider Boundary

Provider/model transport remains separate. Client-runtime API contracts may
reference records, evidence, readiness, or output projections derived from
runtime-provider work, but they do not expose raw provider transport frames.
