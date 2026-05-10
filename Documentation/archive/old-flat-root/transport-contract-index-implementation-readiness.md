# Transport Contract Index / Implementation Readiness

API.09 closes the API transport contract-freeze phase.

The canonical close-out surfaces are:

- `../transports/transport-contract-index.v1.md`
- `../transports/implementation-readiness-matrix.v1.json`
- `../transports/implementation-readiness-matrix.v1.md`
- `../transports/implementation-handoff.v1.md`

Primary-now implementation handoff:

- `local_ipc_rpc` is the first native-local runtime and SDK implementation
  candidate.
- `local_http_loopback` is the next browser/dashboard request-response
  candidate.
- `local_event_stream` is the next realtime serving and client candidate.

Controlled or non-product posture:

- `lan_secure` and `remote_https` remain controlled future boundaries.
- `provider_transport_boundary` remains separate from client-runtime API
  transport.
- `in_process_test` remains test-only.
- `subprocess_stdio_compat` remains compat-only.

API.09 does not add implementation.
It hands off implementation sequencing to `RT.*`, `SDK.*`, `CLI.*`,
`LOOM.*`, and `WEB.*` tracks.
