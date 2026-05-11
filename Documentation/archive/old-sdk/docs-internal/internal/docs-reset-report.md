# DOCS.3 SDK Documentation Reset Report

## Status

DOCS.3 completed. The SDK documentation tree now uses the frozen canonical structure and keeps historical material in manifested archive/internal locations.

## Counts

- Before file count: 43
- After file count: 88
- Files classified: 88
- Canonical/reset files created or rewritten: 45
- Files absorbed and archived: 38
- Files retained in place: 5
- Files deleted: 0
- Files left undecided: 0

## Target Tree Created

Created canonical sections: `architecture/`, `packages/`, `guides/`, `standards/`, `conformance/`, `reference/`, `decisions/`, `internal/`, and `archive/`.

Primary directory scan result:

- `Documentation`
- `Documentation/architecture`
- `Documentation/archive`
- `Documentation/conformance`
- `Documentation/decisions`
- `Documentation/guides`
- `Documentation/internal`
- `Documentation/packages`
- `Documentation/reference`
- `Documentation/standards`

## Canonical Docs Created Or Reworked

Created or rewrote `README.md`, `INDEX.md`, all section READMEs, architecture docs, package docs, guide docs, standard docs, conformance docs, reference indexes, decision docs, internal manifest, archive manifest, classification TSV, before snapshots, and this reset report.

## Absorption Summary

- Old architecture docs were absorbed into canonical `architecture/` docs.
- Package, guide, standard, and report material was absorbed into `packages/`, `guides/`, `standards/`, and `conformance/`.
- Legacy uppercase SDK docs were absorbed and archived under `archive/legacy-sdk/`.
- Old workspace/demo material was absorbed where SDK-relevant and archived under `archive/old-workspace/`.
- Old reports were absorbed into conformance docs or archived under `archive/old-reports/`.
- Completed waves were archived under `archive/old-waves/`.
- Root pre-reset files were archived under `archive/old-flat-root/`.

## Internal Manifest Summary

`internal/internal-manifest.md` limits internal material to reset evidence and current non-public buckets. No active current wave or report file remained after classification.

## Archive Manifest Summary

`archive/historical-manifest.md` records every archived file with old path, new path, classification, absorption target, reason, delete permission, and validation note.

## Forbidden Primary Sections

The old primary `legacy/`, `reports/`, and `waves/` sections were removed or replaced by canonical target sections. No primary `cli/`, `loom/`, `audits/`, `migration/`, `refoundation/`, `business/`, or `refactors/` section exists.

## Deletion Summary

No file was deleted. Empty pre-reset directories were removed only after their files were moved to manifested archive/internal destinations.

## Validation Results

- `git diff --check`: pass, no output.
- Required target file and directory `test` commands: pass.
- `find Documentation -maxdepth 1 -type d | sort`: only canonical DOCS.3 primary directories are present.
- `find Documentation -maxdepth 2 -type f | sort`: target files are present; archive/internal detail continues below maxdepth 2.
- Forbidden primary section scan: pass, no output.
- Artifact movement guard: pass, no output for `packages/`, `conformance/`, `generated/`, `extraction/`, or `tools/`.
- Ownership contradiction scan: pass, no output.
- Corrected active product naming scan excluding `Documentation/archive/**` and `Documentation/internal/**`: pass, no output.
- Classification completeness check: `files=88 classified_rows=88`.
- Supplemental trailing-whitespace scan over Markdown/TSV/TXT in `Documentation`: pass, no output.

## Filename Scan Note

The required forbidden-primary filename scan produced one entry:

- `Documentation/guides/client-adoption.md`

This is a required DOCS.3 target file. The broad `*cli*` pattern matches the substring in `client`; this file is SDK client-adoption documentation, not old command-product documentation.

## Old Naming Scan Note

The exact old naming command using `--glob '!archive/**' --glob '!internal/**'` from the repo root produced 14 historical matches under `Documentation/archive/` because those glob patterns did not prune the prefixed search paths in this invocation. Filtering the exact output to non-archive/non-internal paths produced no output, and the corrected command with `--glob '!Documentation/archive/**' --glob '!Documentation/internal/**'` produced no output.

## Cross-Repo Untouched Check

- `git -C yai diff --name-only`: no output.
- `git -C console diff --name-only`: no output.
- `git -C api diff --name-only`: reports 193 pre-existing DOCS.2 paths from the previous delivery baseline. DOCS.3 did not write to `api`; all DOCS.3 writes are under `sdk/Documentation`.

## Cross-Repo And Artifact Guard

DOCS.3 wrote only under `sdk/Documentation`. SDK package/source/artifact roots outside `Documentation` were indexed but not moved or rewritten. `yai`, `api`, and `console` were not modified by DOCS.3.

## Residual Risks

No manual-review files remain undecided. The only cross-repo validation caveat is the pre-existing uncommitted DOCS.2 diff in `api`.
