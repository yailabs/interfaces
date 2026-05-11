# Implementation Handoff v1

## Purpose

Name the next runtime, SDK, CLI, Loom, and Web implementation waves after the
API transport contract-freeze phase.

This file defines sequence and ownership only.
It does not implement transport behavior.

## Primary Handoff Sequence

1. `RT.01 — Runtime Transport Boundary Skeleton`
   Establish the runtime-side transport substrate and shared boundary
   scaffolding that consumes frozen API transport contracts.
2. `RT.02 — Local IPC RPC Runtime Listener`
   Implement the first primary product listener using the frozen
   `local_ipc_rpc` contract.
3. `SDK.01 — Rust Local IPC RPC Client Transport`
   Implement the first canonical native-local client transport for Rust.
4. `CLI.01 — CLI Local IPC RPC Default`
   Switch CLI default transport consumption to the Rust SDK Local IPC RPC path.
5. `LOOM.01 — Loom Local IPC RPC Default`
   Switch Loom default transport consumption to the Rust SDK Local IPC RPC
   path.
6. `RT.03 — Local HTTP Loopback Runtime Server`
   Implement the primary browser and dashboard local runtime server boundary.
7. `SDK.02 — TypeScript Local HTTP Loopback Client`
   Implement the canonical TypeScript browser/dashboard request-response
   transport.
8. `WEB.01 — Dashboard Local Runtime Binding`
   Bind dashboard and web clients to the canonical local runtime contracts.
9. `RT.04 — Local Event Stream Runtime Serving`
   Implement canonical realtime serving over the frozen Local Event Stream
   contract.
10. `SDK.03 — Stream Clients TS/Rust`
    Implement canonical stream clients for TypeScript and Rust SDKs.

## Controlled or Deferred Boundaries

- `lan_secure` remains frozen but controlled future only.
- `remote_https` remains frozen but controlled future only.
- `provider_transport_boundary` remains a separate runtime-provider boundary.
- `in_process_test` remains test-only and non-product.
- `subprocess_stdio_compat` remains compat-only and non-canonical.

## Ownership Reminder

- API owns contract freeze, indexing, and handoff language.
- Runtime owns listener, server, service, and stream-serving implementation.
- SDK owns client transport implementation.
- CLI, Loom, and Web consume SDK transports; they do not define transport
  grammar.
