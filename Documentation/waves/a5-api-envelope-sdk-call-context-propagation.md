# A5 — API Envelope / SDK Call Context Propagation

## Status
Delivery: A5
Status: done
Track: A-series / API + SDK call context
Repo branch: refoundation/phase-01
Previous delivery: A4 — Protocol Contract for Client Attachment + System Call Record
Next delivery: A6 — Runtime Control Plane Admission Hook

## Purpose

A5 projects the A4 client attachment and system call context contracts into API
envelopes and SDK call context.

A4 defines protocol meaning.
A5 projects that meaning into API envelopes and SDK call context.
Runtime materialization starts later.
Control-plane admission starts later.
Console behavior does not change.

## Files Changed

| Repo | File | Change type |
| ---- | ---- | ----------- |
| `api` | `schemas/request-envelope.v1.schema.json` | add optional call-context refs |
| `api` | `schemas/response-envelope.v1.schema.json` | add optional response call-context refs and `control_admission_ref` |
| `api` | `schemas/readiness-envelope.v1.schema.json` | add optional readiness call-context refs |
| `api` | `schemas/client-ref.v1.schema.json` | add optional client subject/connection/attachment refs |
| `api` | `schemas/*client*-ref.v1.schema.json` | add A4 projection mirrors |
| `api` | `schemas/system-call-ref.v1.schema.json` | add A4 projection mirror |
| `api` | `schemas/system-root-context-ref.v1.schema.json` | add A4 projection mirror |
| `api` | `schemas/work-case-ref.v1.schema.json` | add A4 projection mirror |
| `api` | `schemas/system-call-record.v1.schema.json` | add A4 projection mirror |
| `api` | `schemas/work-case-binding.v1.schema.json` | add A4 projection mirror |
| `api` | `envelopes/*.md` | document A5 call-context projection |
| `api` | `registry/api-envelopes.v1.json` | record optional call-context fields |
| `api` | `conformance/check_client_call_context_projection.py` | add A5 projection checker |
| `api` | `conformance/check_api_envelope_error_stream.py` | extend envelope check for A5 refs |
| `api` | `Documentation/client/console-client-alignment.md` | document A5 boundary |
| `api` | `Documentation/operation-to-transport-mapping.md` | document A5 transport non-change |
| `api` | `Documentation/waves/a-series-map.md` | mark A5 done and A6 next |
| `sdk` | `packages/rust/src/call_context.rs` | add Rust call context model |
| `sdk` | `packages/rust/src/envelope.rs` | add optional response call-context refs |
| `sdk` | `packages/rust/src/transport.rs` | expose optional context invocation |
| `sdk` | `packages/rust/src/transports/local_ipc_rpc.rs` | include call context in request envelope |
| `sdk` | `packages/rust/src/transports/http.rs` | include call context in HTTP invoke body |
| `sdk` | `packages/rust/tests/client_call_context_contract.rs` | add Rust call-context tests |
| `sdk` | `packages/typescript/src/call-context.ts` | add TypeScript call context model |
| `sdk` | `packages/typescript/src/envelope.ts` | add optional response call-context refs |
| `sdk` | `packages/typescript/src/transport.ts` | expose optional context invocation |
| `sdk` | `packages/typescript/tests/client-call-context.test.ts` | add TypeScript compile-time contract test |
| `sdk` | SDK README files | document A5 non-implementation boundary |

## API Projection Result

A5 adds call-context projection fields to API envelopes.
A5 does not implement runtime admission/materialization.

Request envelopes now support:

- `client_subject_ref`
- `client_connection_ref`
- `client_attachment_ref`
- `system_root_context_ref`
- `work_case_ref`
- `system_call_ref`

Response envelopes now support those fields plus optional
`control_admission_ref`.

Readiness envelopes now support the same optional A4 refs as projection fields.

## SDK Propagation Result

Rust SDK and TypeScript SDK now expose a call-context type that carries:

- `request_id`
- `correlation_id`
- `client_ref`
- `client_subject_ref`
- optional `client_connection_ref`
- optional `client_attachment_ref`
- defaultable `system_root_context_ref`
- optional `work_case_ref`
- optional `system_call_ref`
- `transport`

The Rust Local IPC RPC and HTTP request builders include context fields where
available while preserving explicit transport selection.

## Optional Fields Confirmed

`system_call_ref` is optional in requests because runtime admission and durable
materialization may create it later.

`work_case_ref` is optional in requests and remains separate from client
attachment. If present, it does not merge system lineage with work-case lineage.

## Non-Implementation Confirmation

No runtime materialization was added.
No Control Plane admission hook was added.
No durable system call record append was added.
No runtime dispatch behavior changed.
No Console behavior changed.
No CLI/Loom behavior changed.
No provider/model behavior changed.
No LAN/Remote behavior changed.
No operation registry expansion was added.

## Validation Commands

```bash
python3 conformance/check_client_call_context_projection.py
python3 conformance/check_api_envelope_error_stream.py
python3 conformance/check_operation_transport_mapping.py
python3 conformance/check_transport_contract_index.py
find schemas registry -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null
git diff --check
```
