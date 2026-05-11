# Envelopes

`api/envelopes/` defines the canonical transport-facing envelope grammar used by
client-runtime API transports.

Primary files:

- `api-envelope-model.v1.md`
- `request-envelope.v1.md`
- `response-envelope.v1.md`
- `readiness-envelope.v1.md`

Envelope boundary:

- Protocols define transport-neutral meaning in `../yai/protocols`.
- API defines transport-facing request, response, readiness, and stream frame
  projection.
- Runtime will normalize physical transport frames into these envelope shapes
  later.
- SDK will encode and decode these envelope shapes later.
- A5 adds call-context projection fields to API envelopes.
- A5 does not implement runtime admission/materialization.

Canonical response status vocabulary:

- `ok`
- `accepted`
- `partial`
- `unavailable`
- `blocked`
- `invalid`
- `failed`

Transport failures and operation failures must remain distinguishable.
Non-terminal delivery moves through stream event frames rather than response
envelopes.

## A5 Call Context

Request, response, and readiness envelopes may carry:

- `client_subject_ref`
- `client_connection_ref`
- `client_attachment_ref`
- `system_root_context_ref`
- `work_case_ref`
- `system_call_ref`

Response envelopes may also carry `control_admission_ref`.

`system_call_ref` is optional in requests because runtime admission and durable
system call materialization start later. `work_case_ref` is optional and does
not merge system lineage with work-case lineage.
