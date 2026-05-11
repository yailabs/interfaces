# INTF.9 — Interfaces Closure / Command Planning Unblock

## Status

Complete with command planning conditionally unblocked.

`interfaces` is the active developer-interface repository. `sdk` is
tombstone/historical only. `api` is absent locally and historical by name.

Command planning may resume after INTF.9, but command implementation remains
blocked until `CMD.PLAN.1`. `CMD.DECISION.0` is still required before
`CMD.PLAN.1` unless the existing runtime/client command boundary decision is
explicitly promoted to that role.

## Completed INTF Series

- INTF.0: decided API/SDK repository unification path.
- INTF.1: established interfaces target structure.
- INTF.2: canonicalized former API repo as `interfaces`.
- INTF.3: inventoried and classified SDK drain inputs.
- INTF.4: drained SDK packages into `interfaces/packages`.
- INTF.5: merged API and SDK documentation into `interfaces/Documentation`.
- INTF.6: added conformance, generation, package, and provenance guardrails.
- INTF.7: tombstoned old standalone `sdk` and cut over YAI/Console references.
- INTF.8: swept cross-repo references and added active repo reference guard.
- INTF.9: documented final topology, closure validation, and command planning
  unblock conditions.

## Final Topology

```text
console -> interfaces -> yai
```

Active:

- `yai`: runtime/system/governance/service lifecycle/core architecture.
- `interfaces`: protocol/API/SDK/conformance/generated-surface/package/
  developer-interface truth.
- `console`: terminal client UX, CLI mode, TUI mode, command UX, runtime
  attachment UX.
- `web`: public/account/home/download/dashboard/commercial surface.

Historical/tombstone:

- `sdk`: tombstone/historical only.
- `api`: historical name replaced by `interfaces`.
- `cli`: tombstone/historical only.
- `loom`: historical name only.

See:

- `Documentation/internal/current-waves/interfaces-final-topology.md`
- `Documentation/internal/current-waves/interfaces-closure-validation.md`

## What Is Active

`interfaces` owns:

- protocol and operation registry truth;
- schemas, mappings, envelopes, errors, transports;
- OpenAPI projection policy;
- generated-surface provenance;
- conformance profiles and reports;
- SDK package docs and package indexes;
- official SDK package roots under `packages/rust`, `packages/python`,
  `packages/typescript`, and `packages/c`;
- active developer examples and integration contracts.

`console` consumes the `interfaces` SDK/API surface and projects terminal UX.

`yai` receives runtime/system effects and owns runtime implementation and
service lifecycle.

## What Is Historical

The old standalone `sdk` repository is historical/tombstone only and must not
receive active package source, conformance, generated surfaces, or developer
documentation.

The old `api` repository name is historical. Active protocol/API truth is in
`interfaces`.

Old `cli` and `loom` naming remain historical and must not be revived as active
command ownership surfaces.

## Validation Summary

Topology:

- `interfaces`, `sdk`, `yai`, and `console` exist.
- `api/` is absent locally.
- `interfaces` remote is configured as `git@github.com:yailabs/interfaces.git`.

Validation:

- `git -C interfaces diff --check`: passed.
- `git -C yai diff --check`: passed.
- `git -C console diff --check`: passed.
- `git -C sdk diff --check`: passed.
- `python3 -m json.tool interfaces/interface-manifest.json`: passed.
- `python3 -m json.tool console/console.manifest.json`: passed.
- `interfaces/tools/checks/check-generated-output-exclusion.sh`: passed.
- `interfaces/tools/checks/check-package-protocol-drift.sh`: exited 0 with
  manual-review warnings.
- `interfaces/tools/checks/check-active-repo-references.sh`: exited 0 with
  allowed classifications only.
- `sdk/check-sdk-tombstone.sh`: passed.

Source guards:

- Interfaces package source/test/example guard: passed.
- Console source/build guard: passed.
- YAI source guard reports known pre-existing forbidden-path diffs. INTF.9 did
  not edit those paths.

## Command Planning Unblock Decision

Command planning may resume after INTF.9 on this mapping:

```text
console command
  -> interfaces SDK/API surface
  -> yai runtime/system effect
```

`CMD.PLAN.1` may resume if:

- `interfaces` remains active;
- `sdk` remains tombstone;
- `api` remains absent/historical;
- Console consumes `interfaces`;
- YAI names `interfaces` as developer-interface owner;
- package names/imports remain stable;
- runtime shell closure doctrine remains active;
- `CMD.DECISION.0` exists, or an existing runtime/client boundary decision is
  explicitly promoted to that role.

Command implementation is not unblocked by INTF.9. It remains blocked until
`CMD.PLAN.1`.

## Residual Reference / Behavior Boundary Note

INTF.8 recommended checking whether behavior-level references such as:

- `console/Cargo.toml`
- `console/src/client/errors.rs`
- `yai/src/runtime/boundary/**`

need cutover now.

Decision for INTF.9:

- Do not edit behavior/source references in INTF.9.
- Record them as candidate inputs for later source-aware waves only.

Reason:

- INTF closes repo topology and documentation/reference ownership.
- Source behavior cutover belongs to targeted future waves after `CMD.PLAN.1`
  or a dedicated source-boundary audit.

## Residual Risks

- Remote GitHub metadata for old `api`/`sdk` repositories may need admin
  archive/description updates.
- `yai` has pre-existing source diffs outside the INTF series.
- TypeScript package validation still has `dependency-install-required`
  residual because `node_modules` / `tsc` were unavailable.
- C package validation still has `law-compatibility-export-required`
  residual.
- C command-id compatibility vocabulary remains isolated, not removed.
- Source behavior references may require a later targeted audit.
- `CMD.DECISION.0` was not found as an explicit artifact name during INTF.9;
  create it or promote the existing runtime/client boundary decision before
  `CMD.PLAN.1`.

## Next Recommended Waves

- `CMD.DECISION.0`, if not already completed under an equivalent formal name.
- `CMD.PLAN.1`.
- `MAKE.0`.
- Optional `SOURCE.REF.0` for behavior-level `api`/`sdk`/`interfaces`
  references.

## Boundary Confirmation

- No package source code was modified by INTF.9.
- No runtime source code was modified by INTF.9.
- No Console source code was modified by INTF.9.
- No API/protocol operation semantics were modified by INTF.9.
- No SDK package names/imports were changed.
- No Makefiles or build behavior were changed.
- No command implementation was changed.
