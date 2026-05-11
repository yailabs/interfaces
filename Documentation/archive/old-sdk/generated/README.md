# Generated Artifacts

Reserved for generated SDK outputs in future waves.

Wave 14 status: scaffold only. No full generated SDK artifacts yet.

These outputs are transport/client projections over API contracts.
They are not transport source-of-truth and do not define runtime listener
behavior.

API.02 alignment:
- generated outputs must consume API transport mapping rather than invent it
- generated outputs do not turn current HTTP migration paths into the only
  canonical client model

API.03 alignment:
- generated outputs must consume API envelope, error, and stream-frame grammar
- generated outputs do not become the source of truth for envelope shape

API.04 alignment:
- generated native-client artifacts must consume Local IPC RPC discovery,
  handshake, and frame contracts from `../api` when that generation exists

API.05 alignment:
- generated browser or local-web artifacts must consume Local HTTP Loopback
  route, header, origin, token, and request-response contracts from `../api`

API.06 alignment:
- generated realtime client artifacts must consume Local Event Stream event
  frame, binding, reconnect, and terminal-event contracts from `../api`

API.07 alignment:
- generated LAN-capable artifacts must consume explicit LAN Secure pairing,
  allowlist, revocation, and exposure contracts from `../api`
- generated remote-capable artifacts must consume Remote HTTPS platform
  boundary contracts from `../api` without turning remote access into the
  default runtime model

API.08 alignment:
- generated harness artifacts may consume `in_process_test` only in explicit
  conformance or test contexts
- generated compatibility artifacts must not prefer
  `subprocess_stdio_compat` over canonical product transports

API.09 alignment:
- generated outputs follow
  `../api/transports/implementation-readiness-matrix.v1.md`
- generated output sequencing follows
  `../api/transports/implementation-handoff.v1.md`
- no generated transport implementation is added by API.09

SDK.01 note:
- Rust `LocalIpcRpcTransport` is implemented as hand-written package code, not
  generated output
- no generated Local IPC RPC client surface is added in SDK.01

A5 note:
- generated outputs may later project SDK call context, but A5 hand-written SDK
  code is the current propagation surface
- generated outputs must not materialize system call records
- generated outputs must not perform control-plane admission
- `system_call_ref` remains optional and normally runtime-created later
- `work_case_ref` remains optional and separate from client attachment
