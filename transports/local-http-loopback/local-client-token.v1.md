# Local HTTP Loopback Local Client Token v1

## Purpose

Freeze the role of a local client token or equivalent local credential for
`local_http_loopback`.

## Rules

- local client token or equivalent is required before sensitive operations
- explicit dev-mode posture is required if unauthenticated local read surfaces
  are ever permitted
- token posture is separate from CORS posture
- token failure is a transport or security failure, not an operation result

## Notes

- API.05 defines token posture and header role only.
- No token issuance, validation, or storage behavior is implemented here.
