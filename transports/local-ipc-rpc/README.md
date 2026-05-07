# Local IPC RPC Contract

`api/transports/local-ipc-rpc/` holds the verticalized API.04 contract for the
`local_ipc_rpc` transport class.

Purpose:
- define the primary native-local client-runtime transport contract
- freeze discovery, handshake, frame, stream, cancellation, timeout, security,
  and error posture before implementation
- keep provider/model transport separate from client-runtime transport

Primary clients:
- Rust CLI
- Rust Loom/TUI
- future desktop/native clients
- local automation clients

Contract map:
- `discovery.v1.md`
- `handshake.v1.md`
- `frame.v1.schema.json`
- `frame-model.v1.md`
- `message-types.v1.json`
- `security.v1.md`
- `streaming.v1.md`
- `cancellation-timeout.v1.md`
- `errors.v1.md`
- `platform-bindings.v1.md`
- `conformance-profile.v1.md`

Boundary:
- API defines the contract only.
- Runtime implements the listener later.
- SDK implements the client later.
- CLI and Loom consume SDK transports later.
- No IPC server, Unix socket listener, or named pipe server is added here.
