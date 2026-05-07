# Request Envelope v1

## Purpose

Define the canonical request shape that transport entrypoints normalize before
dispatch into `yai/runtime/boundary/api`.

## Required Fields

- all base envelope fields from `api-envelope-model.v1.md`
- `input`

## Optional Fields

- `idempotency_key`
- `stream_request`
- `timeout_ms`
- `cancellation_ref`

## Notes

- `input` is the canonical operation input payload.
- `stream_request` is a request-side hint that the client expects stream event
  delivery semantics rather than only unary response handling.
- `timeout_ms` and `cancellation_ref` are API envelope controls, not physical
  transport policy.
- Request envelopes no longer treat legacy `session` as canonical envelope
  ownership.
