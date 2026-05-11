# In-process Test Non-product Boundary v1

## Purpose

Prevent `in_process_test` from becoming a hidden product transport.

## Rules

- `in_process_test` is not product transport
- `in_process_test` is not SDK default transport
- `in_process_test` is not CLI or Loom runtime transport
- `in_process_test` does not replace Local IPC RPC, Local HTTP Loopback, or
  Local Event Stream
