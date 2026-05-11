# Interfaces Versioning

YAI Interfaces separates protocol compatibility, SDK package releases,
generated surface provenance, conformance profiles, and repository releases.

This repository is currently
`intf-6-conformance-generation-package-guardrails`; active SDK package source
lives under `packages/`, while generated build outputs and SDK tombstone work
remain outside this wave.

## Version Layers

## Protocol version

The protocol version covers operations, transports, envelopes, errors, schemas,
registries, mappings, lifecycle models, and compatibility contracts.

Protocol version is defined by interface artifacts, not by SDK packages or
OpenAPI output.

## SDK package version

The SDK package version is the language package version for Rust, Python,
TypeScript, and C packages after SDK drain.

SDK packages must declare the protocol version and conformance profile version
they support. SDK packages must not define protocol version.

Package versions remain language package versions:

- Rust crate: `yai-sdk-rust`
- Python distribution/import: `yailabs-yai-sdk` / `yai_sdk`
- TypeScript package: `@yailabs/sdk`
- C package: public include prefix `<yai_sdk/...>`

C ABI compatibility is package/ABI compatibility, not protocol version. The
old C command-id vocabulary remains compatibility vocabulary until a later
conformance/provenance wave isolates it.

## Generated surface version

The generated surface version is the version or stamp attached to generated
clients, schemas, OpenAPI output, registry outputs, and projection outputs.

Generated surfaces must record the protocol registry, schema, mapping, and
generator inputs used to create them. INTF.6 requires generated surfaces to
record source registry/schema/mapping versions or digests, generator name and
version, generation command, generated surface version or stamp, source commit
or release tag where available, and the conformance profile used for
validation.

## Conformance profile version

The conformance profile version identifies the required compatibility checks
for protocol integrity, generated surface validity, and SDK package alignment.

The active INTF.6 package alignment profile is
`conformance/profiles/interface-package-alignment.v1.md`.

## Repository release version

The repository release version identifies a release of the combined interfaces
repository. It may contain multiple protocol, package, generated surface, and
conformance profile versions, but it does not replace those layer-specific
versions.

## Compatibility Matrix

Interfaces releases must maintain a compatibility matrix that relates:

- repository release version;
- protocol version;
- conformance profile version;
- SDK package version for each language after drain;
- generated surface versions;
- OpenAPI projection version;
- minimum supported YAI runtime compatibility when known;
- Console projection compatibility when known.

## Provenance

Generated and package-facing surfaces must record provenance: input artifact
versions or digests, generator identity, source commit or release tag,
conformance profile, compatibility aliases, and deprecation state.

## Release Sequencing

1. Freeze protocol artifacts.
2. Run protocol conformance checks.
3. Generate or refresh generated surfaces.
4. Validate generated surface provenance.
5. Validate SDK packages against protocol and conformance profile versions.
6. Update the compatibility matrix.
7. Publish repository release notes.
8. Publish package releases with explicit supported protocol and conformance
   versions.

## INTF.5 Documentation Rule

Documentation must not collapse SDK package version into protocol version.
Protocol, SDK package, generated surface, conformance profile, and repository
release versions remain separate compatibility layers.

## INTF.6 Guardrail Rule

Package releases declare supported protocol and conformance versions. Current
validation residuals remain explicit:

- Rust: `passed`
- Python: `no-tests-discovered`
- TypeScript: `dependency-install-required`
- C: `law-compatibility-export-required`

Generated output exclusions are enforced by
`tools/checks/check-generated-output-exclusion.sh`. Package/protocol drift is
first guarded by `tools/checks/check-package-protocol-drift.sh`, which prints
manual-review warnings and does not replace full conformance.
