# SDK Documentation

`sdk/Documentation` is the canonical documentation surface for YAI SDK and typed client consumers. It owns SDK package behavior, typed client consumption, language package families, SDK compatibility, SDK release/versioning, generated surface boundaries, SDK conformance, and developer experience guidance.

## Ownership

SDK owns:

- typed client truth
- language package truth
- SDK package-family truth
- SDK compatibility truth
- SDK versioning and release truth
- SDK generation boundary
- SDK conformance and developer experience truth

SDK delegates:

- API owns protocol, operation grammar, transport, envelope, and error truth in `../api/Documentation`
- YAI owns runtime, system, and governance truth in `../yai/Documentation`
- Console owns terminal command and TUI UX truth in `../console/Documentation`

## Official Reading Path

1. `Documentation/README.md`
2. `Documentation/INDEX.md`
3. `Documentation/architecture/overview.md`
4. `Documentation/architecture/sdk-architecture.md`
5. `Documentation/architecture/api-consumption-model.md`
6. `Documentation/architecture/transport-consumption-model.md`
7. `Documentation/architecture/package-taxonomy.md`
8. `Documentation/packages/README.md`
9. `Documentation/guides/quickstart.md`
10. `Documentation/standards/compatibility-model.md`
11. `Documentation/conformance/sdk-conformance.md`
12. `Documentation/reference/package-index.md`

## Sections

- `architecture/` explains SDK ownership and consumption boundaries.
- `packages/` documents Rust, TypeScript, Python, C, and release behavior.
- `guides/` gives developer adoption and integration paths.
- `standards/` defines compatibility, status, family availability, and release policy.
- `conformance/` records SDK validation and DX reliability policy.
- `reference/` indexes artifact roots without moving them.
- `decisions/` records active SDK decisions.
- `internal/` and `archive/` are not the public reading path.

Do not use `internal/` or `archive/` as current SDK authority unless a canonical document explicitly points there for history.
