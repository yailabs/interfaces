# Provider Transport Exclusion Policy v1

## Purpose

This policy prevents confusion between client-runtime API transport and
runtime-provider/model transport.

## Rule

- `provider_transport_boundary` is never an allowed client-runtime transport.
- Client-runtime operation mapping ends at runtime dispatch.
- Provider/model routing begins only after `runtime/boundary/api` has accepted
  and dispatched a normalized API operation envelope.
- RT.04 and A1 must not treat `providers.list` or `models.list` as provider or
  model execution. Those entries stay in client-runtime mapping terms, but
  their current Local IPC RPC coverage is explicitly deferred.

## Ownership Split

- `api/mappings` may mark an operation as `runtime_provider_only` to show that
  provider/model routing may occur after dispatch.
- `yai/providers/transport` owns runtime -> provider/model transport behavior.
- SDK clients do not speak provider/model transport directly.
- CLI and Loom do not bypass SDK transports to talk to providers.
- provider HTTP APIs are provider/model transport, not YAI `remote_https`
  platform transport.

## Non-Goals

- no provider protocol grammar
- no provider invocation implementation
- no client shortcut around runtime dispatch
