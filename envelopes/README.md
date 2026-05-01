# Envelopes

Canonical envelope shape:
- `schema`
- `status`
- `reason`
- `message`
- `refs`
- `warnings`
- `errors`

Canonical statuses:
- `ok`, `partial`, `pending`, `ready`, `unavailable`, `blocked`, `denied`, `error`

Pending/unavailable/deferred conditions must be explicitly represented and never implied as success.
