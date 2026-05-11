# INTF.8 Cross-Repo Reference Scan After

Status: complete; no must-fix hits remain in active allowed documentation
surfaces.

## Corrected During INTF.8

Interfaces reference surfaces corrected:

- `extraction/sdk-generation-gate.md`
- `extraction/mirror-sync-policy.md`
- `extraction/api-family-extraction-map.md`
- `extraction/source-manifest.json`
- `mappings/README.md`
- `transports/README.md`
- `interface-manifest.json`

Guard file added:

- `tools/checks/check-active-repo-references.sh`

## Active Reference Scan Result

The final active documentation scan was run over:

- `yai/Documentation`
- `interfaces/Documentation`
- `interfaces/README.md`
- `interfaces/VERSIONING.md`
- `console/Documentation`
- `console/README.md`
- `console/PRODUCT.md`
- `sdk/README.md`
- `sdk/TOMBSTONE.md`
- `sdk/MIGRATION.md`

Remaining API hits:

- `yai/Documentation/reference/ownership-matrix.md`: allowed historical
  reference: old API repository name replaced by `interfaces`.

Remaining SDK hits:

- `@yailabs/sdk`: allowed package name.
- old standalone SDK repository wording: allowed tombstone/historical wording.
- `sdk-*.md` file names and SDK category docs: allowed conceptual SDK terms.

`tools/checks/check-active-repo-references.sh` exited 0 and classified all
active allowed-path hits as:

- `allowed-package-or-import`
- `allowed-tombstone-or-history`
- `allowed-concept-term`

No `must-fix` active allowed-path references remain.

## Broad Scan Residuals

The broad scan still sees references in out-of-scope behavior/source/build
surfaces:

- `console/Cargo.toml`
- `console/src/client/errors.rs`
- `interfaces/packages/c/Makefile`
- `yai/src/runtime/boundary/**`
- `yai/tools/checks/**`
- `yai/Makefile`

INTF.8 did not edit these paths. They should be treated as future behavior or
build-dependency cutover work, not documentation reference drift.
