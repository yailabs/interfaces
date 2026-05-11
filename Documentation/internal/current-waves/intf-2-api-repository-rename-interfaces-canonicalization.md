# INTF.2 - API Repository Rename / Interfaces Canonicalization

## Status

Completed locally.

INTF.2 performed the local repository directory rename and canonicalized the
root and documentation identity to YAI Interfaces. No SDK drain occurred.

## Paths

- Old path: `/Users/francescomaiomascio/Developer/YAI/api`
- New path: `/Users/francescomaiomascio/Developer/YAI/interfaces`

`api/` no longer exists locally after the rename. `interfaces/` is the active
local repository directory.

## Root Files Changed

- `README.md`
- `interface-manifest.json`
- `VERSIONING.md`

## Docs Files Changed

- `Documentation/README.md`
- `Documentation/INDEX.md`
- `Documentation/architecture/README.md`
- `Documentation/architecture/overview.md`
- `Documentation/architecture/api-source-of-truth.md`
- `Documentation/architecture/protocol-api-boundary.md`
- `Documentation/architecture/client-projection-boundary.md`
- `Documentation/architecture/interface-source-of-truth.md`
- `Documentation/architecture/sdk-consumption-boundary.md`
- `Documentation/architecture/generation-boundary.md`
- `Documentation/architecture/conformance-boundary.md`
- `Documentation/architecture/package-boundary.md`
- `Documentation/architecture/external-developer-boundary.md`
- `Documentation/packages/README.md`
- `Documentation/generation/README.md`
- `Documentation/examples/README.md`
- `Documentation/decisions/active-decisions.md`
- `Documentation/internal/current-waves/intf-2-api-repository-rename-interfaces-canonicalization.md`

## Manifest

Created `interface-manifest.json` with:

- name: `yai-interfaces`
- kind: `developer-interface-repository`
- status: `pre-sdk-drain`
- source base: `api-renamed-to-interfaces`
- SDK drain status: `pending`

## Versioning

Created `VERSIONING.md`.

The versioning model distinguishes:

- protocol version;
- SDK package version;
- generated surface version;
- conformance profile version;
- repository release version.

## Remote Status

Remote rename is not required in INTF.2. The local repository still points to
the historical API remote:

```text
origin git@github.com:yailabs/api.git (fetch)
origin git@github.com:yailabs/api.git (push)
```

## Validation Results

Validation commands for INTF.2 passed after the local rename and identity
canonicalization:

- `test -d interfaces`
- `test ! -d api`
- `git -C interfaces diff --check`
- `git -C interfaces status --short`
- required file existence checks for root README, manifest, versioning, and
  Documentation README/INDEX
- required grep checks for `YAI Interfaces`, `developer-interface repository`,
  `pre-sdk-drain`, `protocol version`, `SDK package version`, and Documentation
  README identity
- protected artifact tree guard
- protected reference repo checks for `sdk` and `console`

## SDK Drain Confirmation

SDK was not drained in INTF.2.

No files were moved from `sdk/packages/`. No SDK package imports or package
manifests were rewritten. The standalone `sdk` repository remains active until
INTF.3/INTF.4 classify and drain SDK material.

## Reference Repo Confirmation

`sdk` and `console` were not modified.

`yai` source was not modified. Existing untracked `yai/Documentation/internal`
planning material predates INTF.2.

## Artifact Tree Confirmation

INTF.2 did not reorganize source/spec artifact trees. The protected artifact
roots remain in place for later targeted waves:

- `conformance/`
- `contracts/`
- `envelopes/`
- `errors/`
- `fixtures/`
- `lifecycle/`
- `mappings/`
- `openapi/`
- `projections/`
- `registry/`
- `schemas/`
- `transports/`

## Residual API Naming References

Residual `api` naming is expected in:

- remote URL `git@github.com:yailabs/api.git` until remote rename;
- protocol/API layer terminology;
- artifact filenames such as `api-operations.v1.json`;
- historical archive and internal material;
- source-base references explaining the INTF.2 rename.

These references are not treated as INTF.2 failures unless they claim the
active repository identity is still a standalone API repository.

## Next Wave Recommendation

Proceed to INTF.3: SDK Drain Inventory and Classification.

INTF.3 should inspect the current `sdk` repository, classify package,
generated, conformance, tool, documentation, compatibility, and archive
material, and prepare the controlled SDK drain plan without moving packages
until the drain wave.
