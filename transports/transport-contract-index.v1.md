# Transport Contract Index v1

## Purpose

Provide one canonical index for the frozen YAI transport contract set at the
end of the API transport contract-freeze phase.

API owns the contract surfaces listed here.
Runtime and SDK implementation remains deferred to named handoff waves.

## Indexed Contracts

| Transport | Contract status | Role | Product status | Root contract | Verticalized subtree |
| --------- | --------------- | ---- | -------------- | ------------- | -------------------- |
| `local_ipc_rpc` | frozen | native-local | primary product | `local-ipc-rpc.v1.md` | `local-ipc-rpc/` |
| `local_http_loopback` | frozen | browser/dashboard | primary product | `local-http-loopback.v1.md` | `local-http-loopback/` |
| `local_event_stream` | frozen | realtime | primary product | `local-event-stream.v1.md` | `local-event-stream/` |
| `lan_secure` | frozen | paired LAN | controlled future | `lan-secure.v1.md` | `lan-secure/` |
| `remote_https` | frozen | platform/account/future | controlled future | `remote-https.v1.md` | `remote-https/` |
| `provider_transport_boundary` | frozen | runtime-provider split | separate boundary | `provider-transport-boundary.v1.md` | none |
| `in_process_test` | frozen | test/conformance | non-product | `in-process-test.v1.md` | `in-process-test/` |
| `subprocess_stdio_compat` | frozen | compat/debug/migration | compat only | `subprocess-stdio-compat.v1.md` | `subprocess-stdio-compat/` |

## Readiness References

- Machine-readable readiness: `implementation-readiness-matrix.v1.json`
- Human-readable readiness: `implementation-readiness-matrix.v1.md`
- Runtime and SDK handoff: `implementation-handoff.v1.md`
- Summary doc: `../docs/transport-contract-index-implementation-readiness.md`

## Freeze Closure Rule

- API contracts are frozen enough to hand off implementation waves to runtime
  and SDK tracks.
- API does not implement listeners, servers, routers, stream serving, or SDK
  clients.
- Runtime will implement server-side and service-side behavior later.
- SDK will implement client transports later.
- CLI, Loom, and Web consume SDK transports later.
