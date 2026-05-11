# Repo Profile

- Repository name: `api`
- Repository role: API/platform boundary and service contract projection
- Owns:
  - `observed`: `contracts/`, `schemas/`, `envelopes/`, `errors/`, `transports/`, `openapi/`, `projections/`, `mappings/`, `registry/`, `lifecycle/`, `conformance/`, `extraction/`
- Consumes:
  - `external`: runtime semantics from `../yai`
  - `external`: SDK and console consumption boundaries
  - `external`: catalog projections from `../catalog`
- Exports:
  - `observed`: service/API contract material and projection docs
- Must not own:
  - `external`: local runtime internals, console UI, SDK behavior authority, catalog truth
- Current known status:
  - `observed`: branch `refoundation/phase-01`
  - `observed`: `.agents/` exists
  - `observed`: worktree was clean before `.agents` edits
