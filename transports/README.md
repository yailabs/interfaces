# Transports

`api/transports/` is the canonical documentation root for YAI transport
contracts.

Core rule:

```text
API defines the transport contract.
Runtime implements server-side/local transport behavior.
SDK implements client-side transport behavior.
Clients consume SDK.
Provider/model transport is runtime -> provider/model, not client -> runtime.
```

## Purpose

Freeze transport vocabulary before any transport implementation rewrite or
client migration.

API.09 closes that transport contract-freeze phase with one canonical index,
one machine-readable readiness matrix, and one implementation handoff sequence.

## Transport Classes

| Transport | Status | Primary users | Binding | Notes |
| --------- | ------ | ------------- | ------- | ----- |
| Local IPC RPC | primary now | CLI, Loom/TUI, native clients | Unix socket / named pipe | default native local transport |
| Local HTTP Loopback | primary now | dashboard, web, browser, dev/debug | loopback HTTP | browser-friendly local transport |
| Local Event Stream | primary now | dashboard, CLI, TUI live views | SSE / RPC stream / future WebSocket | realtime transport class separate from request/response |
| LAN Secure | controlled | paired multi-machine local setups | secure network transport | disabled by default |
| Remote HTTPS | future/platform | account, license, machine, update, future hosted capability | HTTPS | not default runtime execution |
| Provider Transport Boundary | separate boundary | runtime -> provider/model | provider-specific | not client-runtime API |
| In-process Test | test only | conformance/dev harness | in-process direct call | not product transport |
| Subprocess/Stdio Compat | compat only | migration/debug | stdout/stderr parsing | not canonical |

## Ownership Split

- protocol meaning: `../yai/protocols`
- API exposure grammar: `../registry/`
- transport contract vocabulary: `api/transports/`
- runtime server/listener behavior: `../yai/runtime/boundary/transport`, `../yai/runtime/boundary/service`
- SDK client transports: `../sdk/packages/*`

See also:

- `transport-contract-index.v1.md`
- `implementation-readiness-matrix.v1.json`
- `implementation-readiness-matrix.v1.md`
- `implementation-handoff.v1.md`
- `../Documentation/transport-boundary-model.md`
- `../Documentation/transport-contract-index-implementation-readiness.md`
- `local-ipc-rpc.v1.md`
- `local-http-loopback.v1.md`
- `local-ipc-rpc/README.md`
- `local-http-loopback/README.md`
- `local-event-stream.v1.md`
- `local-event-stream/README.md`
- `lan-secure.v1.md`
- `lan-secure/README.md`
- `remote-https.v1.md`
- `remote-https/README.md`
- `../Documentation/lan-secure-remote-https-boundary.md`
- `provider-transport-boundary.v1.md`
- `in-process-test.v1.md`
- `in-process-test/README.md`
- `subprocess-stdio-compat.v1.md`
- `subprocess-stdio-compat/README.md`
- `../Documentation/in-process-subprocess-compat-boundary.md`
