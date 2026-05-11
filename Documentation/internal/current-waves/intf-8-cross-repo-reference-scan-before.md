# INTF.8 Cross-Repo Reference Scan Before

Status: captured before INTF.8 reference corrections.

## Scope

Broad scans were run from `/Users/francescomaiomascio/Developer/YAI` across:

- `yai`
- `interfaces`
- `console`
- `sdk`

Archives, internal docs, `.git`, and SDK tombstone files were excluded per the
delivery box.

## API Reference Scan Summary

The broad API scan produced many allowed conceptual hits for:

- `runtime/boundary/api` implementation paths in `yai`;
- `registry/api-*.json` interface artifacts;
- API envelope/error/operation vocabulary;
- Makefile and source include paths that are runtime implementation details.

Must-fix reference-doc hits found in `interfaces`:

- `interfaces/extraction/sdk-generation-gate.md` still pointed SDK generation
  input to `../api`.
- `interfaces/extraction/mirror-sync-policy.md` still described `../api` and
  `yai/api` as current active canonical/mirror roles.
- `interfaces/extraction/api-family-extraction-map.md` still described `../api`
  as canonical contract repository.

Out-of-scope hits found in forbidden or behavior-sensitive paths:

- `yai/src/runtime/boundary/**` README/source references to `../api` and
  `runtime/boundary/api`;
- `yai/Makefile` API boundary source paths;
- `yai/tools/checks/**` API build/runtime checks.

These were not edited in INTF.8 because `yai/src/**`, `yai/tools/**`, and
`yai/Makefile` are forbidden surfaces for this wave.

## SDK Reference Scan Summary

The broad SDK scan produced allowed hits for:

- package name `@yailabs/sdk`;
- package/import/include vocabulary such as `yai_sdk`;
- client subject refs such as `client-subject://sdk-rust`;
- explicit tombstone/historical references.

Must-fix reference-doc hits found in `interfaces`:

- `interfaces/extraction/sdk-generation-gate.md` still pointed SDK workspace to
  `../sdk`.
- `interfaces/extraction/source-manifest.json` still carried `../sdk` as SDK
  workspace/consumer repository.
- `interfaces/mappings/README.md` still said `../sdk` consumes mappings.
- `interfaces/transports/README.md` still said SDK client transports live under
  `../sdk/packages/*`.

Out-of-scope hits found in forbidden or behavior-sensitive paths:

- `console/Cargo.toml` still has a path dependency on `../sdk/packages/rust`.
- `console/src/client/errors.rs` still has an error message pointing to
  `../sdk/packages/rust`.
- `interfaces/packages/c/Makefile` still references `tools/sdk` helper paths.
- `yai/src/runtime/boundary/**` README/source references to `../sdk`.
- `yai/tools/checks/**` build status entries for the old SDK repository.

These were not edited in INTF.8 because they are source/build/package behavior
surfaces or explicitly forbidden paths for this reference-update wave.

## Active Allowed-Path Scan

When the scan was restricted to the active paths allowed by INTF.8:

- `yai/Documentation/**`
- `yai/README.md`
- `interfaces/Documentation/**`
- `interfaces/README.md`
- `interfaces/VERSIONING.md`
- package README files
- `console/Documentation/**`
- `console/README.md`
- `console/PRODUCT.md`
- `console/console.manifest.json`
- SDK tombstone docs

there were no must-fix active references. Remaining hits were already
historical/tombstone mentions, package names, import names, or conceptual
API/SDK terms.
