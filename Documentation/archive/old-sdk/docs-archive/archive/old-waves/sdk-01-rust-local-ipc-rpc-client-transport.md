# SDK.01 — Rust Local IPC RPC Client Transport

## Status

* Delivery: SDK.01
* Status: done
* Track: SDK / Rust transport implementation
* Repo branch: `refoundation/phase-01`
* Repo change type: Rust Local IPC RPC client transport
* Previous delivery: RT.02 — Local IPC RPC Runtime Listener
* Next delivery: SDK.02 — TypeScript Local HTTP Loopback Client

## Purpose

Implement the Rust SDK-side `local_ipc_rpc` transport surface without switching
CLI or Loom to IPC yet.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| `sdk` | `packages/rust/src/transports/mod.rs` | modified | export Local IPC RPC transport modules |
| `sdk` | `packages/rust/src/transports/local_ipc_rpc.rs` | added | implement explicit Rust Local IPC RPC transport and connection boundary |
| `sdk` | `packages/rust/src/transports/local_ipc_rpc_endpoint.rs` | added | implement endpoint discovery helpers and result classes |
| `sdk` | `packages/rust/src/transports/local_ipc_rpc_frame.rs` | added | implement frame type vocabulary and JSON frame helpers |
| `sdk` | `packages/rust/src/transports/local_ipc_rpc_handshake.rs` | added | implement typed handshake request and response validation |
| `sdk` | `packages/rust/src/transports/local_ipc_rpc_error.rs` | added | implement Local IPC RPC transport error mapping helpers |
| `sdk` | `packages/rust/src/lib.rs` | modified | export Local IPC RPC transport public types |
| `sdk` | `packages/rust/src/status.rs` | modified | add structured transport contract error variant |
| `sdk` | `packages/rust/README.md` | modified | document SDK.01 Local IPC RPC posture and no consumer switch |
| `sdk` | `packages/rust/tests/local_ipc_rpc_transport_contract.rs` | added | validate discovery, handshake, frame model, and non-default posture |
| `sdk` | `conformance/README.md` | modified | record SDK.01 conformance coverage |
| `sdk` | `generated/README.md` | modified | state no generated Local IPC RPC client was added |
| `sdk` | `Documentation/waves/sdk-01-rust-local-ipc-rpc-client-transport.md` | added | record implementation status and validation |

## Implementation Result

Record:
- explicit `LocalIpcRpcTransport`
- explicit/env/discovery-file/platform-default endpoint helpers
- typed frame and handshake models aligned to API.04 vocabulary
- Unix domain socket client connection attempt on Linux/macOS
- Windows named-pipe posture explicitly deferred
- safe `not_configured`, `endpoint_missing`, `permission_denied`,
  `version_mismatch`, and `runtime_unavailable` behavior
- no default switch for CLI or Loom

## Deferred Runtime/E2E Notes

Record:
- RT.02 runtime listener is still partial
- runtime listener is not wired into default daemon activation yet
- accept-loop dispatch remains deferred
- live JSON frame/response E2E remains deferred
- SDK.01 therefore stays truthful when runtime is unavailable or non-responsive

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| `sdk` | `git status --short` | pass | worktree was clean before SDK.01 implementation |
| `sdk` | `git branch --show-current` | pass | `refoundation/phase-01` |
| `sdk` | `cargo test` | pass | Rust SDK unit and integration tests passed, including Local IPC RPC contract coverage |
| `sdk` | `git diff --check` | pass | required |
| `yai` | `git status --short` | pass/classified | reference repo contained unrelated pre-existing drift outside SDK.01 scope |
| `api` | `git status --short` | pass/classified | reference repo contained unrelated pre-existing drift outside SDK.01 scope |

## Non-Migration Confirmation

Record:
- no CLI default transport switch
- no Loom default transport switch
- no runtime listener change
- no Local HTTP change
- no Local Event Stream change
- no LAN or Remote HTTPS change
- no provider/model transport behavior
