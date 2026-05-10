# Release Policy

API releases must preserve protocol compatibility unless a breaking change is explicitly versioned and documented.

## Release Gates

- Registry and schema changes must be reflected in documentation and conformance checks.
- Transport and envelope changes must update the corresponding canonical docs.
- Error registry and status mappings must remain synchronized.
- OpenAPI projection must track public operation shape.
- Historical material must remain in `archive/`, not in the primary reading path.
