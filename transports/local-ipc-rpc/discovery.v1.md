# Local IPC RPC Discovery v1

## Purpose

Define endpoint discovery order for `local_ipc_rpc` without implementing
discovery logic.

## Discovery Order

1. explicit SDK/client configuration
2. `YAI_LOCAL_IPC_ENDPOINT` or equivalent environment variable
3. runtime endpoint discovery file
4. platform default socket/pipe path
5. `not_configured`

## Discovery Result Classes

- `not_configured`: no explicit or discoverable endpoint contract is available
- `endpoint_missing`: a configured or discoverable location was expected but is
  absent
- `permission_denied`: socket or pipe exists but the client cannot access it
- `version_mismatch`: endpoint is reachable but handshake negotiation fails
- `runtime_unavailable`: endpoint exists but runtime is not accepting valid API
  traffic

## Notes

- Discovery order is API-owned contract, not SDK implementation code.
- Runtime owns the lifecycle of endpoint discovery files later.
- Discovery does not bypass transport security, auth, or runtime guards.
