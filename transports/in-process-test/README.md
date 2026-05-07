# In-process Test Contract

`api/transports/in-process-test/` holds the verticalized API.08 contract for
the `in_process_test` transport class.

Purpose:
- define test, conformance, harness, and dev-only transport posture
- keep harness semantics explicit without promoting them to product transport
- prevent in-process shortcuts from bypassing API envelopes, operation
  mapping, runtime guards, or provider boundaries

Boundary:
- `in_process_test` is test-only
- `in_process_test` is non-product
- `in_process_test` is not CLI or Loom runtime transport
- `in_process_test` is not dashboard or browser transport
- `in_process_test` is not provider/model transport

Out of scope:
- no in-process runtime bridge implementation
- no hidden SDK default transport
- no runtime guard bypass
