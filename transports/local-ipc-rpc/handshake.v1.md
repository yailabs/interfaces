# Local IPC RPC Handshake v1

## Purpose

Freeze the required capability negotiation performed before operation traffic
is accepted on `local_ipc_rpc`.

## Client Handshake Request

Client sends:
- `transport_name`
- `transport_version`
- `api_envelope_version`
- `client_ref`
- `supported_frame_versions`
- `supported_stream_modes`
- `requested_capabilities`

## Runtime Handshake Response

Runtime responds with:
- `accepted` or `rejected`
- `runtime_ref` (optional)
- `negotiated_frame_version`
- `negotiated_api_envelope_version`
- `supported_features`
- `rejection_error` when rejected

## Rules

- `transport_name` for this profile is `local_ipc_rpc`.
- Version handshake is required before sensitive operations.
- Rejection remains a transport-level failure, not an operation-level result.
- Once normalized, `runtime/boundary/api` does not care whether the caller came
  from a Unix domain socket or a Windows named pipe.
