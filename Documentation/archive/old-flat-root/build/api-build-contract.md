# API Build / Conformance Contract

## Status
- Track: BUILD
- Wave: BUILD.4
- Scope: API contract/conformance validation
- Implementation status: no conformance refactor

## Purpose
Define the canonical validation entrypoint for the `api` repo.

## Canonical Commands

| Command | Role | Status |
|---|---|---|
| `python3 conformance/check_api_contracts.py` | Canonical API contract/conformance validation command | Passed on the current branch during BUILD.4 |

## Non-canonical / Absent Commands

- Root `make all` is absent on the current branch and is not canonical.
- Root `make test` is absent on the current branch and is not canonical.
- `python3 -m pytest` is not a canonical repo-level validation entrypoint in BUILD.4; the discovery probe failed because the local Python environment does not provide `pytest`.
- BUILD.4 does not document absent or failing probes as canonical commands.

## Manual Validation Procedure

```sh
cd /home/mothx/COMPUTER_SCIENCE/DEV_CODE/YAI/api
python3 conformance/check_api_contracts.py
```

## Interpretation

- `python3 conformance/check_api_contracts.py` is the canonical API validation candidate for the current repo state.
- Passing conformance does not imply an implementation runtime build, app build, or cross-repo green status.
- The `api` repo currently validates contracts, schemas, registries, and fixtures through the conformance surface that exists today.
- App/runtime build belongs elsewhere unless a future repo change establishes a distinct build surface here.

## Topology Note

- `Documentation/` is the canonical documentation root for the `api` repo.
- The historical alternate documentation root has been drained into
  `Documentation/` to remove root-level documentation ambiguity.
- The existing root `tools/` surface remains in place, and
  `tools/build/check_api_build_contract.sh` remains the canonical BUILD.4 guard
  entrypoint for repo-local validation.

## Deferred Decisions

- Whether the `api` repo should later expose a root `make test` or `make all`.
- Whether conformance should later be wrapped in another script or task entrypoint.
- Whether `pytest` should become a relevant repo-level validation surface.
- Whether schema validation should later be split by domain.
- Whether a future cross-repo orchestration layer should call the BUILD.4 guard script.
