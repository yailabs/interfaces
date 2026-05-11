# Operator Domain

The operator domain documents API-facing operator context and active case references.

## Semantics

- Operator context is explicit API context, not hidden runtime state.
- Active case references are projections that clients can inspect or set through registered operations.
- Operator context does not redefine auth, runtime, or work execution ownership.

## Artifact References

- `schemas/operator-context-operation.v1.schema.json`
- `fixtures/operator-context-operation/`
- `registry/api-operations.v1.json`
