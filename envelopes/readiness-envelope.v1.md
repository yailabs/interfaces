# Readiness Envelope v1

## Purpose

Define the normalized readiness/status projection payload used when API surfaces
return readiness-facing information.

## Required Fields

- `schema`
- `status`
- `execution_claim`
- `implementation_status`

## Optional Fields

- `envelope_id`
- `operation_id`
- `request_id`
- `correlation_id`
- `client_ref`
- `system_call_ref`
- `client_subject_ref`
- `client_connection_ref`
- `client_attachment_ref`
- `system_root_context_ref`
- `work_case_ref`
- `message`
- `readiness`
- `data`
- `refs`
- `warnings`

## Notes

- This shape preserves current simplified readiness/status projection behavior
  while freezing the richer API.03 contract that SDK and runtime can align to
  later.
- Readiness payloads remain API-facing projections; they do not become transport
  or runtime implementation truth by themselves.
- A5 adds call-context projection fields to API envelopes.
- A5 does not implement runtime admission/materialization.
- A readiness envelope may project the same optional A4 refs as request and
  response envelopes.
