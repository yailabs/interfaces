# In-process Test Harness Boundary v1

## Purpose

Define harness posture for `in_process_test`.

## Rules

- harness context must be explicit
- harness execution does not redefine product transport semantics
- harness entrypoints still normalize into API request envelopes when they are
  used
- harness transport does not bypass runtime guard checks or operation mapping

## Boundary

- API.08 does not implement a harness bridge
