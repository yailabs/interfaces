# API Envelopes

Canonical response envelope direction (Wave 12G):

- `schema`
- `status`
- `reason`
- `message`
- typed payload (`data` or family payload)
- `refs`
- `warnings`
- `errors`

Canonical status vocabulary:
- `ok`
- `partial`
- `pending`
- `ready`
- `unavailable`
- `blocked`
- `denied`
- `error`

Notes:
- `unavailable` is valid for honest absence.
- `pending` is valid readiness posture.
- CLI-only phrasing must not become canonical API contract semantics.
