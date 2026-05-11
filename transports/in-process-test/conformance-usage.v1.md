# In-process Test Conformance Usage v1

## Purpose

Define approved conformance usage for `in_process_test`.

## Allowed Uses

- API conformance validation
- SDK conformance validation
- runtime adapter tests
- schema or fixture replay
- deterministic replay in a controlled harness

## Rules

- conformance usage remains test-only
- fixture ownership must be explicit when user state mutation is involved
