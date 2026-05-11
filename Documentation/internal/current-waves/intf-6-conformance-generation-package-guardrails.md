# INTF.6 Conformance / Generation / Package Guardrails

Status: complete with residuals documented and guardrails established.

## Preflight State

Work repo: `/Users/francescomaiomascio/Developer/YAI/interfaces`

Reference repos:

- `/Users/francescomaiomascio/Developer/YAI/yai`
- `/Users/francescomaiomascio/Developer/YAI/sdk`
- `/Users/francescomaiomascio/Developer/YAI/console`

Observed before INTF.6:

- `interfaces` was dirty from INTF.5 documentation merge and INTF.4 drained
  package/doc material.
- `sdk` was dirty from INTF.4 drain deletions and was not tombstoned.
- `yai` had pre-existing untracked internal audit/wave material.
- `console` had no status output.

Known INTF.4 validation residuals:

- Python: compile passed; pytest found 0 tests and exited 5.
- TypeScript: `npm test` and `npm run typecheck` blocked by missing
  `node_modules` / `tsc`.
- C: `make check-config` and `make check` blocked by missing law compatibility
  export.

## Files Created Or Updated

Conformance:

- `conformance/README.md`
- `conformance/profiles/README.md`
- `conformance/profiles/interface-package-alignment.v1.md`
- `conformance/reports/README.md`
- `conformance/reports/intf-6-package-validation-status.md`
- `Documentation/conformance/package-validation-residuals.md`

Generation and provenance:

- `generators/README.md`
- `generators/provenance-policy.md`
- `projections/README.md`
- `projections/generated/README.md`
- `Documentation/generation/provenance-requirements.md`
- `Documentation/reference/generated-surface-index.md`

Package docs:

- `Documentation/packages/package-compatibility.md`
- `Documentation/packages/rust.md`
- `Documentation/packages/python.md`
- `Documentation/packages/typescript.md`
- `Documentation/packages/c.md`

Guard scripts:

- `tools/checks/README.md`
- `tools/checks/check-generated-output-exclusion.sh`
- `tools/checks/check-package-protocol-drift.sh`

C compatibility boundary:

- `Documentation/reference/c-sdk-command-compatibility.md`

Manifest/versioning:

- `interface-manifest.json`
- `VERSIONING.md`

## Package Validation Statuses

| Package | Status | Residual labels |
| --- | --- | --- |
| Rust `yai-sdk-rust` | INTF.4 `cargo fmt`, `cargo check`, and `cargo test` passed | `passed`, `pending-provenance`, `pending-protocol-drift-check` |
| Python `yailabs-yai-sdk` / `yai_sdk` | compile passed; pytest found 0 tests | `no-tests-discovered`, `pending-provenance`, `pending-protocol-drift-check` |
| TypeScript `@yailabs/sdk` | `npm test` and `npm run typecheck` blocked by missing `tsc` | `dependency-install-required`, `pending-provenance`, `pending-protocol-drift-check` |
| C `<yai_sdk/...>` | `make check-config` and `make check` blocked by missing law compatibility export | `law-compatibility-export-required`, `pending-provenance`, `pending-protocol-drift-check`, `manual-review` |

## Generated Output Exclusion Status

`tools/checks/check-generated-output-exclusion.sh` checks that these paths are
absent:

- `packages/rust/target`
- `packages/typescript/node_modules`
- `packages/typescript/dist`
- `packages/c/build`
- `packages/c/dist`

Observed INTF.6 result: passed.

## Protocol / Package Drift Guard Status

`tools/checks/check-package-protocol-drift.sh` is a conservative first
guardrail. It verifies required root artifacts exist, checks generated-output
exclusion, and prints warnings for manual review.

Observed INTF.6 result: exited 0 with manual-review warnings for:

- C `YAI_SDK_CMD_WORKSPACE_*` compatibility command vocabulary;
- hardcoded operation constants or operation ids in package projection code;
- package envelope/status/error types that require projection provenance review.

These warnings are expected residuals for INTF.6 and do not declare package
release readiness.

## C Command Compatibility Boundary

`Documentation/reference/c-sdk-command-compatibility.md` records:

- C SDK command-id vocabulary is compatibility vocabulary, not protocol truth.
- `YAI_SDK_CMD_WORKSPACE_*` must not define operation semantics.
- Future mapping to interfaces operation ids is required before treating these
  ids as current command architecture.
- INTF.6 does not remove or rename C command vocabulary.

## Manifest And Versioning Changes

`interface-manifest.json` now records:

- package validation status per Rust, Python, TypeScript, and C package;
- conformance profile reference:
  `conformance/profiles/interface-package-alignment.v1.md`;
- generated output exclusion guard reference:
  `tools/checks/check-generated-output-exclusion.sh`;
- package/protocol drift guard reference:
  `tools/checks/check-package-protocol-drift.sh`.

`VERSIONING.md` preserves:

- protocol version separate from SDK package version;
- generated surface version;
- conformance profile version;
- repository release version;
- package releases declaring supported protocol and conformance versions.

## Validation Results

Commands run from `interfaces` during INTF.6:

- `.agents/validation/commands.md` required probes:
  - `pwd`: confirmed `/Users/francescomaiomascio/Developer/YAI/interfaces`.
  - `git branch --show-current`: `refoundation/phase-01`.
  - `git status --short`: showed expected INTF.5/INTF.6 dirty interfaces
    state.
  - `.agents` file listing: passed.
  - repository directory listing excluding common generated roots: passed.
  - `.agents/codex`, `.agents/claude`, `.agents/cursor`,
    `.agents/copilot` absence checks: passed.
- `python3 -m json.tool extraction/source-manifest.json >/dev/null`: passed.
- `git diff --check`: passed.
- required INTF.6 file existence checks: passed.
- executable checks for both guard scripts: passed.
- `./tools/checks/check-generated-output-exclusion.sh`: passed.
- `./tools/checks/check-package-protocol-drift.sh`: exited 0 with documented
  manual-review warnings.
- `python3 -m json.tool interface-manifest.json >/dev/null`: passed.
- required grep checks for residual labels, provenance policy, C command
  compatibility, and `SDK package version`: passed.
- package source guard:
  `git diff --name-only | grep -E '^packages/(rust|python|typescript|c)/(src|include|tests|examples)/' && exit 1 || true`:
  passed.

Cross-repo guard:

- `git -C yai diff --name-only`: final sanity check showed tracked diffs in
  `yai` that were not part of INTF.6 edits:
  `.agents/system/canonical-paths.md`,
  `.agents/system/cross-repo-boundary.md`,
  `.agents/system/ownership-map.md`,
  `.agents/system/repo-profile.md`,
  `Documentation/decisions/active-decisions.md`,
  `Documentation/decisions/adr-index.md`,
  `Documentation/examples/README.md`,
  `Documentation/reference/repository-map.md`,
  `src/governance/README.md`,
  `src/governance/registry/legal/README.md`,
  `src/runtime/operator/pilot.c`.
- `git -C console diff --name-only`: no output.
- `git -C sdk diff --name-only`: reported pre-existing INTF.4 drain deletions.
  INTF.6 did not modify `sdk`.

## Residual Risks

- Python package still has no discovered tests.
- TypeScript validation still requires dependency installation or an equivalent
  `tsc` tool path.
- C strict checks still require law compatibility export.
- Package operation constants and envelope/status/error types still need
  provenance and full protocol drift validation.
- C command vocabulary remains compatibility-only and requires future mapping
  before release-ready current command architecture.

## Next Wave

INTF.7 owns SDK Tombstone / Absence Guard.

## Boundary Confirmation

- No package names/import paths were renamed.
- No SDK tombstone was created.
- No generated outputs were moved into package roots.
- No INTF.6 edits were made in `yai`, `sdk`, or `console`. Current `yai`
  workspace diffs observed during final sanity check are treated as external
  pre-existing/concurrent workspace state and were not touched by this delivery.
