# Operation Grammar

API operations use a stable dotted grammar:

```text
family.resource.verb
```

The grammar identifies a protocol operation, not a UI command or runtime function.

## Rules

- `family` is a public API family registered in `registry/api-families.v1.json`.
- `resource` names the API-facing resource or projection.
- `verb` is a registered API verb from `registry/api-verbs.v1.json`.
- Runtime service lifecycle verbs are not automatically public API operations.
- Operation ids must map to registry records, schemas, transport policy, and conformance checks.

## Examples

- `case.root.get`
- `case.tree.list`
- `auth.status.get`
- `operator.context.current`
- `runtime.status.get`

The exact authoritative set is the operation registry, not examples in prose.
