# A5 — SDK Call Context Propagation

## Status

Delivery: A5
Status: done
Track: A-series / API + SDK call context
Repo branch: refoundation/phase-01
Previous delivery: A4 — Protocol Contract for Client Attachment + System Call Record
Next delivery: A6 — Runtime Control Plane Admission Hook

## Purpose

Project A4 client attachment and system call context refs into SDK call-context
types and request construction.

## Rust Result

Rust adds `YaiCallContext` and `YaiCallContextConfig`.

Local IPC RPC and HTTP request construction include call-context fields where
available. Local IPC RPC remains explicit and is not made the default transport.

## TypeScript Result

TypeScript adds `YaiCallContext` and call-context builders. The transport
interface accepts optional context for future request construction.

## Boundary

SDK propagates call context.
SDK does not materialize system call records.
SDK does not perform control-plane admission.
`system_call_ref` is optional and normally runtime-created later.
`work_case_ref` is optional and separate from client attachment.

## Validation

```bash
cargo test --manifest-path packages/rust/Cargo.toml
npm --prefix packages/typescript test
npm --prefix packages/typescript run build
git diff --check
```
