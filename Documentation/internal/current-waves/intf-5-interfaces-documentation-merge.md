# INTF.5 Interfaces Documentation Merge

Status: complete with noted pre-existing SDK repository dirtiness.

## Files Changed

Primary interface docs updated:

- `README.md`
- `VERSIONING.md`
- `interface-manifest.json`
- `Documentation/README.md`
- `Documentation/INDEX.md`

Architecture docs updated:

- `Documentation/architecture/README.md`
- `Documentation/architecture/api-source-of-truth.md`
- `Documentation/architecture/client-projection-boundary.md`
- `Documentation/architecture/overview.md`
- `Documentation/architecture/interface-source-of-truth.md`
- `Documentation/architecture/protocol-api-boundary.md`
- `Documentation/architecture/sdk-consumption-boundary.md`
- `Documentation/architecture/generation-boundary.md`
- `Documentation/architecture/conformance-boundary.md`
- `Documentation/architecture/package-boundary.md`
- `Documentation/architecture/external-developer-boundary.md`

Package, conformance, generation, examples, and reference docs updated or
created:

- `Documentation/packages/README.md`
- `Documentation/packages/package-taxonomy.md`
- `Documentation/packages/package-release-model.md`
- `Documentation/packages/rust.md`
- `Documentation/packages/python.md`
- `Documentation/packages/typescript.md`
- `Documentation/packages/c.md`
- `Documentation/packages/package-compatibility.md`
- `Documentation/conformance/implementation-readiness.md`
- `Documentation/conformance/sdk-conformance.md`
- `Documentation/conformance/package-validation-residuals.md`
- `Documentation/generation/README.md`
- `Documentation/generation/generated-surface.md`
- `Documentation/generation/sdk-generation.md`
- `Documentation/generation/schema-generation.md`
- `Documentation/generation/openapi-generation.md`
- `Documentation/generation/registry-generation.md`
- `Documentation/generation/provenance-requirements.md`
- `Documentation/examples/README.md`
- `Documentation/examples/external-client-authoring.md`
- `Documentation/examples/local-runtime-connection.md`
- `Documentation/examples/protocol-examples.md`
- `Documentation/examples/sdk-examples.md`
- `Documentation/reference/package-index.md`
- `Documentation/reference/sdk-package-index.md`
- `Documentation/reference/generated-surface-index.md`

Other docs updated:

- `Documentation/archive/historical-manifest.md`
- `Documentation/decisions/active-decisions.md`
- `Documentation/domains/client.md`
- `Documentation/domains/sdk.md`
- package README files under `packages/rust`, `packages/python`,
  `packages/typescript`, and `packages/c`

Snapshot files created:

- `Documentation/internal/current-waves/intf-5-before-doc-file-list.txt`
- `Documentation/internal/current-waves/intf-5-before-doc-tree.txt`

## Docs Merged

`interfaces/Documentation` now presents YAI Interfaces as the unified
developer-interface surface for protocol/API truth, SDK package truth,
generation/provenance, conformance, external developer examples, and package
reference.

Active docs state that SDK packages live under:

- `packages/rust`
- `packages/python`
- `packages/typescript`
- `packages/c`

The previous SDK repository remains present and pending tombstone.

## Package Docs Updated

Rust:

- Path: `packages/rust`
- Package name: `yai-sdk-rust`
- INTF.4 validation: `cargo fmt`, `cargo check`, and `cargo test` passed

Python:

- Path: `packages/python`
- Distribution/import: `yailabs-yai-sdk` / `yai_sdk`
- INTF.4 validation: compile passed; pytest found 0 tests

TypeScript:

- Path: `packages/typescript`
- Package name: `@yailabs/sdk`
- INTF.4 residual: `npm test` and `npm run typecheck` unavailable because
  `node_modules` was not moved

C:

- Path: `packages/c`
- Include prefix: `<yai_sdk/...>`
- INTF.4 residual: `make check-config` and `make check` blocked by missing law
  compatibility export
- Old command-id vocabulary remains compatibility-only pending INTF.6

## Conformance Residuals Documented

`Documentation/conformance/package-validation-residuals.md` records:

- Rust checks passed.
- Python pytest exit 5 is classified as `no-tests-discovered`.
- TypeScript is classified as `dependency-install-required`.
- C is classified as `law-compatibility-export-required`.

INTF.6 is recorded as the owner for guardrails, provenance, and package
validation hardening.

## Generation And Provenance

Generation docs now state:

- generated outputs are not source of truth;
- OpenAPI is projection;
- SDK operation constants and envelope types are package projections pending
  validation;
- generated outputs require registry, schema, mapping, and generator
  provenance;
- TypeScript `dist/`, Rust `target/`, and C `build/` and `dist/` were
  intentionally excluded from INTF.4.

## Archive And Historical Manifest

`Documentation/archive/historical-manifest.md` now lists the old SDK archive
families under `Documentation/archive/old-sdk/`.

Historical standalone SDK material remains under `Documentation/archive/**` and
is not active developer-interface authority.

## Active Standalone SDK Wording Scan

Command:

```sh
rg -n "standalone SDK repo|standalone sdk repo|SDK repo owns protocol|../api|../sdk|github.com/yailabs/sdk|yailabs/sdk" \
  Documentation README.md VERSIONING.md \
  --glob '!Documentation/archive/**' \
  --glob '!Documentation/internal/**'
```

Result: no active standalone SDK repository, SDK-repo-owns-protocol, `../api`,
`../sdk`, or repository URL authority claims remain.

The scan still reports `@yailabs/sdk` package identity references because the
pattern includes `yailabs/sdk`. Those hits are required package-name references,
not active repository URL or standalone SDK authority claims.

## Validation Results

From `interfaces`:

- `git diff --check`: passed.
- Required file existence checks: passed.
- `python3 -m json.tool interface-manifest.json >/dev/null`: passed.
- Required grep checks for YAI Interfaces, package identities, OpenAPI
  projection, and SDK protocol-truth boundary: passed.
- Active standalone SDK wording scan: passed with justified `@yailabs/sdk`
  package-name hits.
- Package source guard: passed; no tracked package source/test/example changes
  from INTF.5.

From workspace root:

- `git -C yai diff --name-only`: no output.
- `git -C console diff --name-only`: no output.
- `git -C sdk diff --name-only`: reported pre-existing SDK drain deletions
  already observed during INTF.5A preflight. INTF.5 did not modify `sdk`.

## Boundary Confirmation

- No package source code was modified for INTF.5.
- No SDK tombstone was created.
- `sdk` was not modified by INTF.5.
- `yai` and `console` were not modified by INTF.5.
