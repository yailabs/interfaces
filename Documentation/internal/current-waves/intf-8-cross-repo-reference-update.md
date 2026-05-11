# INTF.8 Cross-Repo Reference Update

Status: complete with source/build residuals documented as out of scope.

## Preflight State

Work repos:

- `/Users/francescomaiomascio/Developer/YAI/yai`
- `/Users/francescomaiomascio/Developer/YAI/interfaces`
- `/Users/francescomaiomascio/Developer/YAI/console`
- `/Users/francescomaiomascio/Developer/YAI/sdk`

Observed before INTF.8:

- `yai` was dirty before this wave, including documentation diffs and
  pre-existing forbidden-path diffs under `src/`, `include/`, `protocols/`,
  `tools/`, and `Makefile`.
- `interfaces` was dirty from INTF.4 through INTF.7 work.
- `console` was dirty from INTF.7 documentation/manifest cutover.
- `sdk` was dirty from INTF.7 tombstone reduction.
- Local `api/` was absent.
- `sdk/check-sdk-tombstone.sh` passed before INTF.8 edits.

## Files Changed By Repo

`interfaces`:

- `Documentation/internal/current-waves/intf-8-cross-repo-reference-scan-before.md`
- `Documentation/internal/current-waves/intf-8-cross-repo-reference-scan-after.md`
- `Documentation/internal/current-waves/intf-8-cross-repo-reference-update.md`
- `extraction/sdk-generation-gate.md`
- `extraction/mirror-sync-policy.md`
- `extraction/api-family-extraction-map.md`
- `extraction/source-manifest.json`
- `mappings/README.md`
- `transports/README.md`
- `interface-manifest.json`
- `tools/checks/check-active-repo-references.sh`

`yai`:

- No INTF.8 edits.

`console`:

- No INTF.8 edits.

`sdk`:

- No INTF.8 edits.

## Before Scan Summary

`Documentation/internal/current-waves/intf-8-cross-repo-reference-scan-before.md`
records the broad before scan.

Findings:

- Active allowed documentation paths had no must-fix references.
- Interfaces non-Documentation reference surfaces still had current-looking
  references to `../api`, `../sdk`, `api/mappings`, `api/transports`, and
  `../sdk/packages/*`.
- Forbidden or behavior-sensitive paths still contain old API/SDK references,
  including `console/Cargo.toml`, `console/src/client/errors.rs`,
  `yai/src/runtime/boundary/**`, `yai/tools/checks/**`, and `yai/Makefile`.

## Reference Corrections

YAI:

- No INTF.8 edits were made.
- Active YAI documentation was already aligned by INTF.7.

Interfaces:

- SDK generation gate now names `interfaces` as the input repository and
  `packages/` as the SDK package workspace.
- Mirror sync policy now says the former API repository name is superseded by
  `interfaces`.
- API family extraction map now names `interfaces` as current contract owner.
- Extraction source manifest now uses `interfaces` and `interfaces/packages`
  for contract/package source fields.
- Mapping docs now say SDK packages under `../packages/` consume mappings.
- Transport docs now say `interfaces/transports` owns transport contracts and
  SDK client transports live under `../packages/*`.
- `interface-manifest.json` now records INTF.8 status and the active repo
  reference guard.

Console:

- No INTF.8 edits were made.
- Active Console documentation and manifest were already aligned by INTF.7.

SDK:

- No INTF.8 edits were made.
- Tombstone docs remain valid and the tombstone guard passes.

## After Scan Summary

`Documentation/internal/current-waves/intf-8-cross-repo-reference-scan-after.md`
records the after scan.

Final active documentation scan result:

- No `must-fix` active allowed-path API references remain.
- No `must-fix` active allowed-path SDK references remain.
- Remaining hits are allowed package names, import/include vocabulary,
  tombstone/historical references, or conceptual API/SDK terms.

The new guard:

```sh
interfaces/tools/checks/check-active-repo-references.sh
```

exited 0 and classified remaining active allowed-path hits as allowed.

## Remaining Allowed Exceptions

- `@yailabs/sdk`: allowed TypeScript package name.
- `yailabs-yai-sdk` and `yai_sdk`: allowed Python package/import names.
- `<yai_sdk/...>` and `include/yai_sdk`: allowed C include vocabulary.
- `sdk-*` file names and SDK category docs: allowed conceptual SDK terms.
- API envelope/error/operation/registry names: allowed protocol/interface
  vocabulary.
- Explicit old API/SDK tombstone or historical references.

## Residual Risks

The broad scan still finds old API/SDK references in forbidden or
behavior-sensitive surfaces:

- `console/Cargo.toml`
- `console/src/client/errors.rs`
- `interfaces/packages/c/Makefile`
- `yai/src/runtime/boundary/**`
- `yai/tools/checks/**`
- `yai/Makefile`

INTF.8 did not change those paths because this wave was not a source behavior,
build dependency, package behavior, or command planning wave.

## Validation Results

Validation run from `/Users/francescomaiomascio/Developer/YAI`:

- Repo-local validation skill probes in `yai`:
  - `pwd`: `/Users/francescomaiomascio/Developer/YAI/yai`.
  - `git branch --show-current`: `refoundation/phase-01`.
  - `.agents` file listing: passed.
  - root directory listing excluding common generated roots: passed.
  - `.agents/codex`, `.agents/claude`, `.agents/cursor`, and
    `.agents/copilot` absence checks: passed.
- `test -d yai`: passed.
- `test -d interfaces`: passed.
- `test -d console`: passed.
- `test -d sdk`: passed.
- `test ! -d api`: passed.
- `git -C yai diff --check`: passed.
- `git -C interfaces diff --check`: passed.
- `git -C console diff --check`: passed.
- `git -C sdk diff --check`: passed.
- `sdk/check-sdk-tombstone.sh`: passed.
- `python3 -m json.tool interfaces/interface-manifest.json`: passed.
- `python3 -m json.tool interfaces/extraction/source-manifest.json`: passed.
- `python3 -m json.tool console/console.manifest.json`: passed.
- `interfaces/tools/checks/check-active-repo-references.sh`: passed.

Source guards:

- Interfaces package source/test/example guard: passed.
- Console source/build guard: passed.
- YAI source guard reports pre-existing forbidden-path diffs that were already
  present before INTF.8. INTF.8 did not edit those paths.

YAI source guard output:

```text
include/yai/governance/registry.h
protocols/MIGRATION_FROM_SPECS.md
protocols/registry/topology/module-nuclei.v1.json
protocols/registry/topology/path-ownership.v1.json
src/governance/README.md
src/governance/corpus/legal/view.c
src/governance/registry/class.c
src/governance/registry/ids.c
src/governance/registry/index.c
src/governance/registry/iterator.c
src/governance/registry/legal/README.md
src/governance/registry/legal/legal-bundles.v1.json
src/governance/registry/legal/legal-resolution.v1.json
src/governance/registry/legal/legal-sources.v1.json
src/governance/registry/namespace.c
src/governance/registry/query.c
src/governance/registry/record.c
src/governance/registry/registry.c
src/governance/registry/status.c
src/runtime/operator/pilot.c
tools/checks/contracts/check-runtime-operation-bindings.py
```

## Boundary Confirmation

- No package names/imports were changed.
- No C include paths were changed.
- No package source/test/example files were edited by INTF.8.
- No YAI runtime/source files were edited by INTF.8.
- No Console source/build files were edited by INTF.8.
- No SDK package source or tombstone policy was changed.
- Command planning was not resumed.

## Recommendation For INTF.9

INTF.9 can close the interface unification sequence and unblock command
planning on the final topology:

```text
console -> interfaces -> yai
```

If INTF.9 is allowed to touch behavior/build surfaces, it should explicitly
decide how to handle remaining out-of-scope references in `console/Cargo.toml`,
`console/src/client/errors.rs`, `yai/src/runtime/boundary/**`, `yai/tools/**`,
and `yai/Makefile`.
