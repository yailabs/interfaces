# Request Envelope v1

## Purpose

Define the canonical request shape that transport entrypoints normalize before
dispatch into `yai/runtime/boundary/api`.

## Required Fields

- all base envelope fields from `api-envelope-model.v1.md`
- `input`

## Optional Fields

- `client_subject_ref`
- `client_connection_ref`
- `client_attachment_ref`
- `system_root_context_ref`
- `work_case_ref`
- `system_call_ref`
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
- A5 adds call-context projection fields to API envelopes.
- A5 does not implement runtime admission/materialization.
- `system_root_context_ref` defaults to `root-context://system/default` unless
  explicitly set.
- `system_call_ref` is optional because runtime admission/materialization may
  create it later.
- `work_case_ref` is optional and appears only when a call targets governed
  work.
