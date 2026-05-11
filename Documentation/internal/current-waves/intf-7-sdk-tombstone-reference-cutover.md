# INTF.7 SDK Tombstone / Interfaces Reference Cutover

Status: complete with pre-existing YAI source guard caveat documented.

## Preflight State

Work repos:

- `/Users/francescomaiomascio/Developer/YAI/interfaces`
- `/Users/francescomaiomascio/Developer/YAI/sdk`
- `/Users/francescomaiomascio/Developer/YAI/yai`
- `/Users/francescomaiomascio/Developer/YAI/console`

Observed before INTF.7:

- `interfaces` was dirty from INTF.4 through INTF.6 documentation, package,
  conformance, generation, and guardrail work.
- `sdk` was dirty from INTF.4 drain deletions and was not yet tombstoned.
- `yai` already had documentation diffs and unrelated source/protocol/include
  diffs before this wave.
- `console` had no status output before this wave.
- Local `api/` was absent.

The pre-existing `yai` source/protocol/include diffs were not discarded or
rewritten by INTF.7.

## SDK Tombstone Status

The old standalone SDK repository was reduced to a tombstone/historical repo.

Tombstone files created:

- `sdk/README.md`
- `sdk/TOMBSTONE.md`
- `sdk/MIGRATION.md`
- `sdk/archive/README.md`
- `sdk/archive/drain-summary.md`
- `sdk/check-sdk-tombstone.sh`

Active SDK directories removed from `sdk`:

- `.agents/`
- `.github/`
- `Documentation/`
- `conformance/`
- `extraction/`
- `generated/`
- `packages/`
- `tools/`

`sdk/README.md`, `sdk/TOMBSTONE.md`, and `sdk/MIGRATION.md` now point active
SDK package, conformance, generation, and developer-interface work to
`interfaces`.

## SDK Absence Guard

`sdk/check-sdk-tombstone.sh` was added and made executable.

Observed result:

```sh
sdk-tombstone: ok
```

The guard fails if active SDK surfaces such as `packages/`, `Documentation/`,
`conformance/`, `generated/`, `extraction/`, `tools/`, `src/`, or `include/`
reappear in the tombstone repository.

## Interfaces Updates

Files updated or created in `interfaces`:

- `README.md`
- `Documentation/README.md`
- `Documentation/packages/README.md`
- `Documentation/reference/sdk-package-index.md`
- `Documentation/archive/old-sdk/README.md`
- `Documentation/archive/old-sdk/sdk-tombstone-summary.md`
- `Documentation/internal/current-waves/intf-7-sdk-tombstone-reference-cutover.md`
- `interface-manifest.json`

`interface-manifest.json` now records:

- `sdk_drain_status`: `tombstoned`
- `old_sdk_repo.status`: `historical-tombstone`
- `old_sdk_repo.canonical_replacement`: `interfaces/packages`

`Documentation/reference/sdk-package-index.md` points active SDK package roots
to:

- `interfaces/packages/rust`
- `interfaces/packages/python`
- `interfaces/packages/typescript`
- `interfaces/packages/c`

The old standalone SDK repository is documented as tombstone/historical only.

## YAI Reference Cutover

Allowed `yai/Documentation/**` files updated:

- `yai/Documentation/README.md`
- `yai/Documentation/INDEX.md`
- `yai/Documentation/architecture/repository-boundaries.md`
- `yai/Documentation/architecture/runtime-spine.md`
- `yai/Documentation/reference/repository-map.md`
- `yai/Documentation/reference/ownership-matrix.md`
- `yai/Documentation/internal/current-waves/interfaces/interfaces-wave-map.md`

Active YAI documentation now records:

- `interfaces`: protocol/API/SDK/conformance/developer-interface truth
- `sdk`: tombstone/historical only
- `api`: historical name replaced by `interfaces`

No INTF.7 edits were made to YAI runtime/source paths.

## Console Reference Cutover

Allowed Console files updated:

- `console/README.md`
- `console/PRODUCT.md`
- `console/console.manifest.json`
- `console/Documentation/README.md`
- `console/Documentation/INDEX.md`
- `console/Documentation/architecture/sdk-api-consumption-boundary.md`
- `console/Documentation/runtime-attachment/sdk-api-consumption.md`
- `console/Documentation/reference/manifest.md`
- `console/Documentation/decisions/active-decisions.md`

Active Console documentation now records:

```text
Console command / TUI UX
  -> interfaces SDK/API surface
  -> yai runtime/system effect
```

Console consumes YAI Interfaces and does not depend on the old standalone SDK
repository as an active developer surface.

No INTF.7 edits were made to Console source, tests, scripts, tools, or Cargo
files.

## Stale Reference Scan Results

SDK repository scan:

- No active-primary `../sdk`, `github.com/yailabs/sdk`, or standalone SDK
  repository authority references remain in the scanned active docs.
- Allowed hits remain for package/import identities and docs file names:
  `@yailabs/sdk`, `yai_sdk`, `sdk-package-index.md`,
  `sdk-consumption-boundary.md`, `sdk-generation.md`, and `sdk-examples.md`.
- Allowed tombstone/historical mentions remain where they explicitly identify
  the old SDK repository as historical only.

API repository scan:

- No active-primary `../api`, `github.com/yailabs/api`, or standalone API
  repository authority references remain in the scanned active docs.
- Allowed hits remain for API concept/artifact names such as API envelopes,
  API error model, API inventory, public API family wording, and generated
  registry file names.
- Historical API repository references remain only as replacement/history
  wording.

## Validation Results

From `/Users/francescomaiomascio/Developer/YAI`:

- `test -d interfaces`: passed.
- `test -d sdk`: passed.
- `test ! -d api`: passed.
- `git -C interfaces diff --check`: passed.
- `git -C sdk diff --check`: passed.
- `git -C yai diff --check`: passed.
- `git -C console diff --check`: passed.

SDK tombstone validation:

- Required tombstone file checks: passed.
- Active directory absence checks for `sdk/packages`, `sdk/Documentation`,
  `sdk/conformance`, `sdk/generated`, `sdk/extraction`, and `sdk/tools`:
  passed.
- `sdk/check-sdk-tombstone.sh`: passed.

Interfaces validation:

- `python3 -m json.tool interface-manifest.json >/dev/null`: passed.
- Required `tombstoned`, `interfaces/packages`, old SDK summary, and INTF.7
  report checks: passed.

Source guards:

- Interfaces package source guard: passed; no package source/test/example
  changes were made by INTF.7.
- Console source guard: passed; no Console source/test/script/tool/Cargo
  changes were made by INTF.7.
- YAI source guard reports pre-existing source/protocol/include diffs that were
  already present before INTF.7. INTF.7 did not edit those paths.

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
```

## Allowed Exceptions

- `@yailabs/sdk` remains the TypeScript package name.
- `yai_sdk` remains the Python import and C include vocabulary.
- `<yai_sdk/...>` remains the C include path.
- API remains valid as a protocol/interface concept, but not as an active
  standalone repository owner.
- SDK remains valid as package/interface vocabulary, but the old standalone SDK
  repository is tombstone/historical only.

## Boundary Confirmation

- No package names or imports were changed.
- No SDK package source was moved or edited.
- No API operation semantics, protocol semantics, or transport semantics were
  changed.
- No INTF.7 edits were made to YAI runtime/source paths.
- No INTF.7 edits were made to Console implementation paths.
- CMD.PLAN.1 was not resumed.

## Next Wave

INTF.8 can be reduced to residual cross-repo reference cleanup and remote
repository-administration closure if needed. INTF.9 can then focus on the next
runtime/console planning sequence without relying on the old SDK repository.
