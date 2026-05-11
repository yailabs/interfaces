# INTF.4 SDK Drain into Interfaces Packages

Status: complete with recorded validation blockers.

## Moved Package Areas

- Rust package moved from `sdk/packages/rust/` to `interfaces/packages/rust/`.
  - Preserved crate name: `yai-sdk-rust`.
  - Moved `Cargo.toml`, `Cargo.lock`, `README.md`, `src/`, and `tests/`.
- Python package moved from `sdk/packages/python/` to
  `interfaces/packages/python/`.
  - Preserved distribution/import: `yailabs-yai-sdk` / `yai_sdk`.
  - Moved `pyproject.toml`, `README.md`, `src/`, `tests/`, and `examples/`.
- TypeScript package moved from `sdk/packages/typescript/` to
  `interfaces/packages/typescript/`.
  - Preserved package name: `@yailabs/sdk`.
  - Moved `package.json`, `package-lock.json`, `README.md`, `src/`, `tests/`,
    `examples/`, `tsconfig.json`, and `tsconfig.test.json`.
- C package moved from `sdk/packages/c/` to `interfaces/packages/c/`.
  - Preserved include prefix: `<yai_sdk/...>`.
  - Moved `Makefile`, `Doxyfile`, `README.md`, `include/`, `src/`, `tests/`,
    `examples/`, `packaging/`, `wrappers/`, and `third_party/`.

Package names, imports, and include prefixes were not renamed.

## Excluded Generated and Build Outputs

The following generated/build outputs were not moved into `interfaces`:

- `sdk/packages/rust/target/`
- `sdk/packages/typescript/node_modules/`
- `sdk/packages/typescript/dist/`
- `sdk/packages/c/build/`
- `sdk/packages/c/dist/`

Root guards confirmed these paths do not exist under `interfaces/packages/`.

## Docs Merged

- Added `Documentation/packages/sdk-drain-package-notes.md`.
- Added `Documentation/generation/sdk-generation.md`.
- Added `Documentation/conformance/sdk-package-conformance.md`.
- Added `Documentation/reference/sdk-package-index.md`.
- Moved SDK package docs into `Documentation/packages/`:
  - `c.md`
  - `package-release-model.md`
  - `python.md`
  - `rust.md`
  - `typescript.md`
- Moved SDK conformance docs into `Documentation/conformance/`:
  - `api-inventory.md`
  - `dx-reliability-checklist.md`
  - `generated-surface.md`
  - `sdk-conformance.md`
- Moved SDK reference indexes into `Documentation/reference/`:
  - `api-inventory-index.md`
  - `generated-surface-index.md`
  - `package-index.md`

Active package docs were adjusted away from standalone `../api` wording where
encountered.

## Docs Archived

Historical standalone SDK docs and root metadata were archived under
`Documentation/archive/old-sdk/`:

- `docs-archive/`
- `docs-internal/`
- `architecture/`
- `guides/`
- `standards/`
- `decisions/`
- `reference-figures/`
- `root/`
- `generated/`
- `extraction/`
- `conformance-root/`

The archived SDK manifest is at
`Documentation/archive/old-sdk/root/sdk-manifest.json`.

## Tools

Moved active SDK tools to `interfaces/tools/sdk/sh/`:

- `check_api_boundaries.sh`
- `resolve_law.sh`

Path updates:

- C package `Makefile` now calls `tools/sdk/sh/resolve_law.sh`.
- C package `Makefile` now calls `tools/sdk/sh/check_api_boundaries.sh`.
- `check_api_boundaries.sh` now checks `packages/c/include/yai_sdk/public.h`.

Manual-review tooling left in `sdk`: `.agents/` and `.github/`.

## Manifest, Versioning, and Ignore Policy

- `interface-manifest.json` now records `packages.rust`, `packages.python`,
  `packages.typescript`, and `packages.c` with `drained-from-sdk` status.
- `interface-manifest.json` records the old SDK archive location and marks the
  repository status as `intf-4-sdk-drain`.
- `VERSIONING.md` records protocol/package separation, language package
  identities, C ABI/package compatibility, and compatibility-only C command
  vocabulary.
- `.gitignore` was created with generated-output protections for:
  - `packages/rust/target/`
  - `packages/typescript/node_modules/`
  - `packages/typescript/dist/`
  - `packages/c/build/`
  - `packages/c/dist/`

## Package Validation Results

Rust:

- `cargo fmt --check`: failed before formatting moved source; `cargo fmt` was
  run and `cargo fmt --check` then passed.
- `CARGO_TARGET_DIR=/private/tmp/yai-intf4-cargo-target cargo check`: passed.
- `CARGO_TARGET_DIR=/private/tmp/yai-intf4-cargo-target cargo test`: passed,
  24 tests passed plus doctests with 0 tests.

Python:

- `python3 -m compileall src`: passed.
- `python3 -m pytest tests`: exited 5 because 0 tests were collected.

TypeScript:

- `npm test`: failed because `tsc` was not found.
- `npm run typecheck`: failed because `tsc` was not found; `node_modules` was
  intentionally not moved.

C:

- `make check-config`: failed because no law compatibility export was found.
- `make OUT_BUILD_DIR=/private/tmp/yai-intf4-c-build OUT_LIB_DIR=/private/tmp/yai-intf4-c-dist/lib OUT_BIN_DIR=/private/tmp/yai-intf4-c-dist/bin DOCS_DIR=/private/tmp/yai-intf4-c-dist/docs check`:
  failed at `check-config` for the same missing law compatibility export.

Root guards:

- `git diff --check`: passed.
- `test ! -d packages/rust/target`: passed.
- `test ! -d packages/typescript/node_modules`: passed.
- `test ! -d packages/typescript/dist`: passed.
- `test ! -d packages/c/build`: passed.
- `test ! -d packages/c/dist`: passed.
- `python3 -m json.tool interface-manifest.json >/dev/null`: passed.

SDK repo checks:

- `test -d sdk`: passed.
- `test ! -d sdk/packages/rust/src`: passed.
- `test ! -d sdk/packages/python/src`: passed.
- `test ! -d sdk/packages/typescript/src`: passed.
- `test ! -d sdk/packages/c/src`: passed.

Cross-repo checks:

- `git -C yai diff --name-only`: no output.
- `git -C console diff --name-only`: no output.

Repo-local validation:

- `.agents` vendor folder guards passed.
- `python3 -m json.tool extraction/source-manifest.json >/dev/null`: passed.
- Secret scan produced pre-existing policy/checker vocabulary hits; no new
  secret material was introduced by INTF.4 package drain.

## SDK Repo Residual Contents

The `sdk` repo remains present. Residual contents include:

- `.agents/`
- `.github/`
- `.gitignore`
- community/license/security files
- `VERSION`
- `law-compatibility.v1.json`
- empty documentation and tooling parent directories
- generated/build outputs intentionally not drained:
  - `packages/rust/target/`
  - `packages/typescript/node_modules/`
  - `packages/typescript/dist/`
  - `packages/c/build/`
  - `packages/c/dist/`

## Manual Review Leftovers

- `sdk/law-compatibility.v1.json`
- `sdk/.agents/`
- `sdk/.github/`
- root community/license/security files
- residual generated/build outputs listed above
- empty parent directories left by the controlled drain

## Tombstone and Boundary Confirmation

No SDK tombstone README was created.

No YAI or Console source was modified.

SDK package operation constants/envelope types remain package projections
pending later validation. The old C command-id vocabulary remains compatibility
vocabulary and was not promoted to protocol truth.
