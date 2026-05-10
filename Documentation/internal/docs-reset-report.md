# DOCS.2 API Documentation Reset Report

## Status

DOCS.2 completed. The API documentation tree now uses the frozen canonical structure and keeps historical material in manifested archive/internal locations.

## Counts

- Before file count: 198
- After file count: 264
- Files classified: 264
- Canonical/reset files created or rewritten: 66
- Files absorbed and archived: 193
- Files retained in place: 5
- Files deleted: 0
- Files left undecided: 0

## Target Tree Created

Created canonical sections: `architecture/`, `operations/`, `transports/`, `envelopes/`, `errors/`, `domains/`, `conformance/`, `reference/`, `decisions/`, `internal/`, and `archive/`.

Primary directory scan result:

- `Documentation`
- `Documentation/architecture`
- `Documentation/archive`
- `Documentation/conformance`
- `Documentation/decisions`
- `Documentation/domains`
- `Documentation/envelopes`
- `Documentation/errors`
- `Documentation/internal`
- `Documentation/operations`
- `Documentation/reference`
- `Documentation/transports`

## Canonical Docs Created Or Reworked

Created or rewrote `README.md`, `INDEX.md`, all section READMEs, architecture docs, operations docs, transport docs, envelope docs, error docs, domain docs, conformance docs, reference indexes, decision docs, internal manifest, archive manifest, classification TSV, before snapshots, and this reset report.

## Absorption Summary

- Root API model documents were absorbed into canonical `architecture/`, `operations/`, `transports/`, `envelopes/`, `errors/`, `domains/`, and `conformance/` docs.
- Domain directories were absorbed into `domains/` and archived under `archive/old-flat-root/`.
- Historical command-product material was absorbed into operation/action/client/SDK projection docs and archived under `archive/legacy-cli/`.
- SDK projection material was absorbed into `domains/sdk.md` and archived under `archive/old-sdk/`.
- Retired client material was absorbed into `domains/client.md` and `architecture/client-projection-boundary.md`, then archived under `archive/legacy-loom/`.
- Completed waves were archived under `archive/old-v-waves/`.
- Refoundation history was archived under `archive/refoundation/`.

## Internal Manifest Summary

`internal/internal-manifest.md` limits internal material to reset evidence and current audit/wave buckets. `internal/current-audits/` contains the inspected API leakage audit. `internal/current-waves/` has no active wave file after classification.

## Archive Manifest Summary

`archive/historical-manifest.md` records every archived file with old path, new path, classification, absorption target, reason, delete permission, and validation note.

## Deletion Summary

No file was deleted. Empty pre-reset directories were removed only after their files were moved to manifested archive/internal destinations.

## Forbidden Primary Sections

The old primary `cli/`, `sdk/`, `waves/`, `adr/`, `build/`, `case/`, `client/`, `compat/`, `execution/`, `identity/`, `operator/`, and `runtime/` sections were removed or replaced by canonical target sections.

## Validation Results

- `git diff --check`: pass, no output.
- Required target file and directory `test` commands: pass.
- Forbidden primary section scan: pass, no output.
- Artifact movement guard: pass, no output.
- Ownership contradiction scan: pass, no output.
- Corrected active product naming scan excluding `Documentation/archive/**` and `Documentation/internal/**`: pass, no output.
- Cross-repo untouched check: `git -C yai diff --name-only`, `git -C sdk diff --name-only`, and `git -C console diff --name-only` all produced no output.
- Classification completeness check: `files=264 classified_rows=264`.
- Supplemental trailing-whitespace scan over Markdown/TSV/TXT in `Documentation`: pass, no output.

## Filename Scan Note

The required forbidden-primary filename scan produced two entries:

- `Documentation/domains/client.md`
- `Documentation/architecture/client-projection-boundary.md`

These are required DOCS.2 target files. The broad `*cli*` pattern matches the substring in `client`; neither file is command-product documentation.

## Old Naming Scan Note

The exact old naming command using `--glob '!archive/**' --glob '!internal/**'` from the repo root produced historical matches under `Documentation/archive/` and `Documentation/internal/` because those glob patterns did not prune the prefixed search paths in this invocation. Filtering the exact output to non-archive/non-internal paths produced no output, and the corrected command with `--glob '!Documentation/archive/**' --glob '!Documentation/internal/**'` produced no output.

## Cross-Repo And Artifact Guard

DOCS.2 wrote only under `api/Documentation`. Artifact roots outside `Documentation` were indexed but not moved or rewritten. `yai`, `sdk`, and `console` were not modified.

## Residual Risks

No manual-review files remain undecided. `domains/sdk.md` points to the expected SDK ownership paths, including `../sdk/Documentation/INDEX.md`; the current SDK repo still exposes `DOCS_INDEX.md`, but DOCS.2 does not modify SDK.
