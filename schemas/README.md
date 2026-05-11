# Schemas

`api/schemas/` is a mixed projection surface.

API-owned schema families here include:
- envelope, request-envelope, response-envelope
- error vocabulary
- watch-event
- record/evidence/case/workflow/client refs
- operation-result
- operation-contract/family/projection

Protocol-neutral schemas may also appear here as API-side mirrors for
projection, compatibility, or conformance consumers.

Canonical rule:
- transport-neutral protocol schemas: `../yai/protocols/schemas`
- API-facing schema projection: `api/schemas/`
