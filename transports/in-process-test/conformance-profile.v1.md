# In-process Test Conformance Profile v1

## Purpose

Define the minimum contract claims that a future `in_process_test`
implementation must satisfy.

## Required Contract Areas

- test-only posture
- explicit harness context
- non-product boundary
- no guard bypass
- no provider credential access
- explicit harness or fixture ownership for persistent mutation

## Out of Scope for API.08

- no in-process runtime bridge implementation
- no SDK transport implementation
