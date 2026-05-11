# Local HTTP Loopback Errors v1

## Purpose

Preserve the distinction between HTTP transport or gateway failures and API
operation failures for `local_http_loopback`.

## Rules

- HTTP status errors and API operation errors remain distinct
- 4xx and 5xx transport or gateway failures do not automatically equal
  operation failure
- operation, guard, and runtime errors are carried through API.03 response
  envelopes
- runtime sealed and guard failures are operation or guard errors, not CORS
  errors
- CORS, origin, or token failures are transport or security failures
- provider or model transport failures must not appear as raw browser-facing
  transport payloads
