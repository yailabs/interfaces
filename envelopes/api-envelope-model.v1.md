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
- `client_subject_ref`
- `client_connection_ref`
- `client_attachment_ref`
- `system_root_context_ref`
- `work_case_ref`
- `system_call_ref`
- `metadata`

## Interpretation

- `schema` identifies the concrete wire shape version.
- `envelope_id` identifies this specific envelope instance.
- `request_id` groups request and response for one logical API call.
- `correlation_id` links related API calls or follow-on stream frames.
- `client` identifies the API consumer surface.
- `transport` identifies the transport class that carried the envelope.
- `created_at` records envelope creation time in the transport-facing API layer.

## A5 Call Context Projection

A5 adds call-context projection fields to API envelopes.
A5 does not implement runtime admission/materialization.

The A5 fields project the A4 protocol meaning from `../yai/protocols` into API
envelope shape. They do not create durable `system_call_record` instances and
do not add Control Plane admission behavior.

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
