# In-process Test Purpose v1

## Purpose

Define `in_process_test` as a direct harness and conformance transport for
controlled non-product contexts only.

## Rules

- conformance and deterministic test harnesses may use `in_process_test`
- dev-only simulations may use `in_process_test`
- product clients must not treat `in_process_test` as a canonical transport
