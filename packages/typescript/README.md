# TypeScript SDK Package

Enterprise package for TypeScript consumers of YAI SDK contracts.

This package lives in `interfaces/packages/typescript` and preserves package
name `@yailabs/sdk`. It is an official SDK package projection over YAI
Interfaces protocol truth; it does not define protocol truth.

INTF.4 validation residual: `npm test` and `npm run typecheck` were unavailable
because `node_modules` was intentionally not moved.

Install dependencies:
```sh
npm install --ignore-scripts
```

Validation:
```sh
npm run typecheck
```

Build:
```sh
npm run build
```

Runtime note:

- `runtime.controlPlan()` is plan/projection only.
- unavailable transport must remain unavailable, not fake ready.
- SDK surfaces must not claim runtime start/stop/restart executed unless a real
  transport operation and validation prove it.
- TypeScript/browser clients align primarily to `local_http_loopback` and
  `local_event_stream`.
- TypeScript SDK transport ownership is client-side only; runtime listeners stay
  in `../yai`.

API.02 mapping rule:
- TypeScript SDK consumes API operation-to-transport mapping from
  `../../mappings`
- TypeScript SDK does not invent operation-to-transport grammar
- loopback and event-stream transport selection must follow the canonical map,
  not ad hoc client rules

API.03 envelope rule:
- TypeScript SDK will encode and decode API request envelopes, response
  envelopes, and stream event frames from the interfaces package source tree
- current simplified TypeScript envelope types remain migration-era
  implementation until later SDK alignment waves
- TypeScript SDK does not define envelope grammar independently

A5 call-context rule:
- SDK propagates call context.
- SDK does not materialize system call records.
- SDK does not perform control-plane admission.
- `system_call_ref` is optional and normally runtime-created later.
- `work_case_ref` is optional and separate from client attachment.
- TypeScript `YaiCallContext` carries request/correlation ids, client refs,
  system/root context, optional work-case binding, optional system call ref, and
  transport.

API.04 Local IPC RPC note:
- browser TypeScript clients remain aligned to `local_http_loopback` and
  `local_event_stream`
- Node or Electron TypeScript clients may support `local_ipc_rpc` later if a
  non-browser transport is justified
- TypeScript SDK does not define IPC grammar independently

API.05 Local HTTP Loopback rule:
- `local_http_loopback` is the target browser and dashboard request-response
  transport
- `local_event_stream` remains separate for realtime delivery
- TypeScript SDK will consume API route, header, origin, CORS, and local token
  contracts later

API.06 Local Event Stream rule:
- `local_event_stream` is the target realtime transport for dashboard and
  browser live updates
- SSE is the primary web binding
- stream frames are not response envelopes

API.07 LAN and Remote rule:
- `local_http_loopback` and `local_event_stream` remain the browser-local
  targets
- `lan_secure` requires explicit paired configuration if it is ever supported
- `remote_https` is not a replacement for local runtime access

API.08 Test and Compat rule:
- `in_process_test` may be used for TypeScript SDK or conformance harnesses
  later in explicit test contexts
- `subprocess_stdio_compat` is compatibility or debug only
- TypeScript SDK must not prefer subprocess compatibility for new canonical
  transports

API.09 implementation readiness:
- `local_http_loopback` is frozen and ready for canonical TypeScript client
  work in `SDK.02`
- `local_event_stream` is frozen and ready for canonical realtime client work
  in `SDK.03`
- `local_ipc_rpc` remains non-browser and optional for Node or Electron later,
  not the primary TypeScript browser target
- readiness and handoff are centralized in
  interfaces transport implementation readiness and handoff artifacts
