# API Envelope Model v1

## Purpose

Freeze the common API wire fields carried by request and response envelopes
across canonical client-runtime transports.

## Base API Envelope

Required fields:

- `schema`
- `envelope_id`
- `operation_id`
- `request_id`
- `correlation_id`
- `client`
- `transport`
- `created_at`

Optional fields:

- `case_ref`
- `principal_ref`
- `metadata`

## Interpretation

- `schema` identifies the concrete wire shape version.
- `envelope_id` identifies this specific envelope instance.
- `request_id` groups request and response for one logical API call.
- `correlation_id` links related API calls or follow-on stream frames.
- `client` identifies the API consumer surface.
- `transport` identifies the transport class that carried the envelope.
- `created_at` records envelope creation time in the transport-facing API layer.

## Status Boundary

The finite response-envelope status vocabulary for API.03 is:

- `ok`
- `accepted`
- `partial`
- `unavailable`
- `blocked`
- `invalid`
- `failed`

These statuses describe API operation outcome, not raw transport failure.

## Non-Goals

- no transport listener implementation
- no SDK encoder/decoder implementation
- no provider/model transport framing
