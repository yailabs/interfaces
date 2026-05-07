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
