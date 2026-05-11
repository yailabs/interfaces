# Local Event Stream SSE Binding v1

## Purpose

Define SSE as the primary web and dashboard binding for `local_event_stream`.

## Rules

- SSE is the primary web or dashboard binding for one-way runtime-to-client
  events.
- SSE may use HTTP mechanics, but emitted frames are not API.03 response
  envelopes.
- A stream open may follow HTTP or SSE binding, but emitted frames use stream
  frame grammar.
- Browser stream access must obey the same local origin and token posture used
  by Local HTTP Loopback where applicable.

## Boundary

- API.06 defines binding posture only.
- No SSE server implementation is added here.
