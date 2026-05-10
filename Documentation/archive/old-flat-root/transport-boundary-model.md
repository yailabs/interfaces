# Transport Boundary Model

## Purpose

Define the canonical YAI transport vocabulary and ownership boundary before
transport implementation, SDK transport rewrites, runtime server work, or
client migration.

## Why Transport Is Separate From Operation Semantics

Operation semantics define what a YAI operation means.
Transport semantics define how a client reaches the runtime and how envelopes,
streams, timeouts, and errors move across that boundary.

API therefore owns transport contracts, not runtime listeners or SDK client
implementation details.

## Transport Classes

- `local_ipc_rpc`
- `local_http_loopback`
- `local_event_stream`
- `lan_secure`
- `remote_https`
- `provider_transport_boundary`
- `in_process_test`
- `subprocess_stdio_compat`

## Ownership Matrix

| Area | Owns | Does not own |
| ---- | ---- | ------------ |
| `api/transports` | transport contracts | server/client implementation |
| `yai/runtime/boundary/transport` | runtime-side transport boundary | API source-of-truth |
| `yai/runtime/boundary/service` | local service exposure/lifecycle boundary | SDK client behavior |
| `yai/runtime/boundary/api` | operation dispatch into runtime | physical socket/listener policy |
| `yai/runtime/connections` | client connection/session observation | provider/model transport |
| `yai/include/ipc` | C/ABI IPC contract headers | API projection docs |
| `yai/providers/transport` | runtime -> provider/model transport | client -> runtime API transport |
| `sdk/packages/*/src/transports` | SDK client transports | runtime server implementation |
| `cli` | CLI commands over SDK | custom transport grammar |
| `loom` | TUI over SDK | custom transport grammar |

## Primary-Now Transports

- `local_ipc_rpc` is primary now for CLI, Loom/TUI, and native local clients.
- `local_http_loopback` is primary now for dashboard/web/browser/dev.
- `local_event_stream` is primary now for realtime observation and must remain
  separate from unary request/response transport.

## Controlled/Future Transports

- `lan_secure` is controlled, disabled by default, and requires pairing.
- `remote_https` is the platform/account/license/machine/update/future hosted
  boundary and is not the default local runtime execution path.

## Test/Compat Transports

- `in_process_test` is test/conformance/dev harness only.
- `subprocess_stdio_compat` is compatibility/debug only and must not become
  canonical.

## Provider/Model Transport Separation

Provider/model transport is not client-runtime API transport.
Clients ask YAI operations through SDK-owned client transports.
Runtime then decides provider/model routing through `yai/providers/transport`.

## Security Baseline

### Local IPC RPC

- socket/pipe permissions required
- same-user local access by default
- version handshake required
- no remote exposure

### Local HTTP Loopback

- bind to loopback only by default
- strict origin/CORS
- local client token or equivalent required before sensitive operations
- no LAN exposure by default

### Local Event Stream

- heartbeat required
- terminal event/error semantics required
- reconnect semantics documented
- sensitive payloads must be projection-safe

### LAN Secure

- disabled by default
- explicit pairing
- TLS/token/certificate posture
- revocation
- device allowlist
- no automatic `0.0.0.0` bind

### Remote HTTPS

- platform-owned remote boundary
- no raw provider identity leakage into runtime core
- no pricing/billing object leakage into runtime core
- local-first runtime remains baseline

### Subprocess/Stdio Compat

- compat only
- not canonical
- should not be used for new SDK transports

## Non-goals

- no runtime transport implementation
- no IPC/RPC/HTTP/SSE/WebSocket/LAN listener implementation
- no SDK transport implementation
- no OpenAPI route expansion
- no Console behavior change
- no legacy CLI/Loom compatibility behavior change
- no provider/model invocation behavior change
