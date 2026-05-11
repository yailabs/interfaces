# Operation Result Model v1

## Purpose

Define the normalized `result` payload carried by successful or partial
response envelopes.

## Fields

- `outcome`
- `summary`
- `data`
- `refs`
- `records_emitted`
- `evidence_emitted`
- `stream_started`

## Notes

- `outcome` mirrors API-facing result posture and should stay aligned with the
  response status vocabulary.
- `summary` is a compact human-readable interpretation of the result payload.
- `data` is the typed operation result payload projected by API contracts.
- `stream_started` indicates that a response acknowledged follow-on stream
  delivery via `stream_ref`.
