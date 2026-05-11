# Interface Package Alignment Profile v1

Status: active guardrail profile for INTF.6.

## Protocol Registry Integrity

Protocol registry checks must verify:

- operation identifiers remain stable unless a compatibility decision records
  the change;
- operation families, verbs, projections, clients, envelopes, errors, and
  surfaces are valid registry records;
- operation-to-transport mappings reference known operations and known
  transports;
- OpenAPI operation projections do not define new protocol operations.

## Schema, Envelope, And Error Alignment

Schema, envelope, and error checks must verify:

- request, response, readiness, and stream-frame contracts align with registry
  and mapping expectations;
- error codes and status mappings reference known error records;
- schema references point to canonical schema artifacts;
- package-facing envelope, status, and error types are projections, not
  protocol source of truth.

## Package Projection Alignment

SDK packages must consume canonical protocol artifacts from this repository.
They must not define protocol truth, transport semantics, operation semantics,
or runtime dispatch targets.

Package projection alignment requires:

- package identity is preserved;
- package README and package docs state the protocol truth boundary;
- generated or duplicated operation/envelope/status/error material is marked as
  projection;
- risky compatibility vocabulary is isolated and documented.

## SDK Package Validation Expectations

Rust:

- `cargo fmt --check`
- `cargo check`
- `cargo test`

Python:

- compile validation;
- pytest validation when tests exist;
- `no-tests-discovered` must be recorded when pytest collects 0 tests.

TypeScript:

- dependency installation or equivalent local tool availability;
- `npm test`;
- `npm run typecheck`.

C:

- `make check-config`;
- `make check`;
- law compatibility export availability for strict checks.

## Generated Surface Provenance

Generated surfaces retained in this repository must record:

- source registry version or digest;
- source schema version or digest;
- source mapping version or digest;
- generator name;
- generator version;
- generation command;
- generated surface version or stamp;
- source commit or release tag where available;
- conformance profile used for validation.

## Package Release Readiness

A package may be declared release-ready only after:

- protocol registry checks pass;
- schema/envelope/error checks pass;
- generated output exclusion checks pass;
- package validation for the target language passes or residuals are explicitly
  accepted by release policy;
- provenance is recorded for generated/package-facing surfaces;
- package compatibility docs identify supported protocol and conformance
  profile versions;
- compatibility-only vocabulary, including C command-id vocabulary, is not
  promoted to protocol truth.
