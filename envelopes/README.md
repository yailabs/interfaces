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
