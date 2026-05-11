# Interfaces Closure Validation

Status: passed with known residual warnings and pre-existing YAI source diff
caveat.

## Topology

- `test -d interfaces`: passed.
- `test -d sdk`: passed.
- `test -d yai`: passed.
- `test -d console`: passed.
- `test ! -d api`: passed.

## Manifest And JSON

- `python3 -m json.tool interfaces/interface-manifest.json >/dev/null`:
  passed.
- `python3 -m json.tool console/console.manifest.json >/dev/null`: passed.

## Guard Results

- `interfaces/tools/checks/check-generated-output-exclusion.sh`: passed with
  `generated-output-exclusion: ok`.
- `interfaces/tools/checks/check-package-protocol-drift.sh`: exited 0 with
  manual-review warnings.
- `interfaces/tools/checks/check-active-repo-references.sh`: exited 0 and
  classified remaining hits as allowed package/import/tombstone/history terms.
- `sdk/check-sdk-tombstone.sh`: passed with `sdk-tombstone: ok`.

## Diff Checks

- `git -C interfaces diff --check`: passed.
- `git -C yai diff --check`: passed.
- `git -C console diff --check`: passed.
- `git -C sdk diff --check`: passed.

## Package Validation Residuals From INTF.6

Rust:

- `cargo fmt`, `cargo check`, and `cargo test` passed in INTF.4.

Python:

- compile passed.
- pytest found 0 tests and exited 5.
- status: `no-tests-discovered`.

TypeScript:

- `npm test` and `npm run typecheck` blocked by missing `node_modules` / `tsc`.
- status: `dependency-install-required`.

C:

- `make check-config` and `make check` blocked by missing law compatibility
  export.
- status: `law-compatibility-export-required`.
- C command-id compatibility vocabulary remains isolated and not promoted to
  protocol truth.

## Package / Source Guards

Interfaces package source/test/example guard:

- passed; INTF.9 did not edit package source, include, test, or example paths.

Console source/build guard:

- passed; INTF.9 did not edit Console source, tests, scripts, tools, Cargo
  files, or build behavior.

YAI source guard:

- reports known pre-existing forbidden-path diffs.
- INTF.9 did not edit those paths.

Known YAI source guard output:

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

## Behavior-Boundary Scan

The optional behavior-boundary scan over `console/Cargo.toml`, `console/src`,
`yai/src/runtime/boundary`, `yai/include`, and `yai/protocols` found active
`api`/`sdk`/`interfaces` strings in behavior and protocol surfaces.

Decision:

- Do not edit behavior/source references in INTF.9.
- Treat these as candidate inputs for a later source-aware audit or cutover
  wave.

Reason:

- INTF.9 closes repo topology and documentation/reference ownership.
- Behavior-level cutover belongs to targeted future waves after `CMD.PLAN.1`
  or a dedicated `SOURCE.REF.0`.
