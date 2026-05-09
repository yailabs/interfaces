# Transport Selection Policy v1

## Purpose

This policy defines how SDK clients should choose a transport from the allowed
set in `operation-transport-map.v1.json`.

## Selection Order

1. Resolve the operation id in the canonical map.
2. If the operation is `streamable`, use `local_event_stream`.
3. If the operation dispatches to `platform_remote_api`, use `remote_https`.
4. For local native clients, prefer `local_ipc_rpc` when allowed.
5. For browser/dashboard clients, prefer `local_http_loopback` when allowed.
6. `lan_secure` is never auto-selected; it requires explicit paired opt-in.
7. `in_process_test` is test-only.
8. `subprocess_stdio_compat` is explicit compatibility/debug fallback only.

## Runtime Truth Guard

- Contract-allowed transport is not the same as currently audited runtime
  support.
- When `operation-transport-map.v1.json` carries `runtime_ipc_coverage`, SDK
  and conformance consumers must treat it as the Local IPC RPC reality marker
  for the current audited runtime state.
- A1 records RT.04 Local IPC RPC truth only for the audited read/projection
  subset; it does not promote deferred, blocked, or provider/model surfaces to
  supported.

## Primary-Now Defaults

- `local_ipc_rpc` is the default local native transport for CLI, Loom/TUI, and
  future native desktop clients.
- `local_http_loopback` is the browser/dashboard/dev transport when the
  operation is safe for loopback-local exposure.
- `local_event_stream` is reserved for streamable/watch/tail/status-event
  surfaces.

See also:
- `../transports/transport-contract-index.v1.md`
- `../transports/implementation-readiness-matrix.v1.md`
- `../transports/implementation-handoff.v1.md`
- `../transports/local-ipc-rpc.v1.md`
- `../transports/local-ipc-rpc/README.md`
- `../transports/local-http-loopback.v1.md`
- `../transports/local-http-loopback/README.md`
- `../transports/local-event-stream.v1.md`
- `../transports/local-event-stream/README.md`
- `../transports/lan-secure.v1.md`
- `../transports/lan-secure/README.md`
- `../transports/remote-https.v1.md`
- `../transports/remote-https/README.md`
- `../transports/in-process-test.v1.md`
- `../transports/in-process-test/README.md`
- `../transports/subprocess-stdio-compat.v1.md`
- `../transports/subprocess-stdio-compat/README.md`

## Disallowed Selection Behavior

- Do not treat HTTP as the only canonical transport.
- Do not select `remote_https` for local runtime execution by default.
- Do not select `lan_secure` unless the operation mapping and runtime pairing
  posture both allow it.
- Do not treat Local HTTP Loopback as LAN exposure.
- Do not treat `in_process_test` as product transport.
- Do not use `subprocess_stdio_compat` for new canonical SDK transports.
