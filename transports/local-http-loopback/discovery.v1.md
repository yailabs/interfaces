# Local HTTP Loopback Discovery v1

## Purpose

Define endpoint discovery order for `local_http_loopback` without implementing
discovery logic.

## Discovery Order

1. explicit SDK or client configuration
2. `YAI_LOCAL_HTTP_ENDPOINT` or equivalent environment variable
3. runtime endpoint discovery file
4. platform default loopback port or runtime service registry
5. `not_configured`

## Discovery Result Classes

- `not_configured`
- `endpoint_missing`
- `connection_refused`
- `origin_blocked`
- `token_required`
- `token_rejected`
- `version_mismatch`
- `runtime_unavailable`

## Notes

- Discovery order is API-owned contract, not SDK implementation code.
- Discovery does not authorize LAN exposure or bypass runtime guards.
