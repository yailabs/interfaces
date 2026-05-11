# In-process Test v1

## Purpose

Define `in_process_test` as a conformance/dev harness transport class.

API.08 verticalizes this transport into a dedicated contract subtree so test,
conformance, and harness surfaces can stay explicit without becoming hidden
product transports or hidden shortcuts around API envelopes, operation mapping,
or runtime guards.

## Classification

- status: test only
- class: in-process direct invocation for tests and controlled harnesses

## Allowed Uses

- API conformance validation
- SDK conformance validation
- runtime adapter tests
- schema and fixture replay
- deterministic test harness
- dev-only simulation

## Ownership

- API owns: only the contract language that marks this class as non-product
- Runtime owns: any harness adapter used for tests
- SDK may consume: harness-only client adapters where explicitly test-scoped

## Guardrails

- must not become a product transport
- must not become a hidden SDK/runtime shortcut
- must not redefine canonical network/IPC transport semantics
- must not become CLI or Loom runtime transport
- must not bypass guards, operation mapping, or provider boundaries

## Contract Surfaces

- `in-process-test/README.md`
- `in-process-test/purpose.v1.md`
- `in-process-test/harness-boundary.v1.md`
- `in-process-test/conformance-usage.v1.md`
- `in-process-test/security-limitations.v1.md`
- `in-process-test/non-product-boundary.v1.md`
- `in-process-test/errors.v1.md`
- `in-process-test/conformance-profile.v1.md`

## Non-goals

- no production transport implementation
- no hidden bypass of runtime boundary ownership
