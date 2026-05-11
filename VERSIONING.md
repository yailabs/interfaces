# Interfaces Versioning

YAI Interfaces separates protocol compatibility, SDK package releases,
generated surface provenance, conformance profiles, and repository releases.

This repository is currently `pre-sdk-drain`; SDK package source remains in
`../sdk` until later INTF waves.

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

## Generated surface version

The generated surface version is the version or stamp attached to generated
clients, schemas, OpenAPI output, registry outputs, and projection outputs.

Generated surfaces must record the protocol registry, schema, mapping, and
generator inputs used to create them.

## Conformance profile version

The conformance profile version identifies the required compatibility checks
for protocol integrity, generated surface validity, and SDK package alignment.

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

## INTF.1 Reference

The planning source for this model is
`../yai/Documentation/internal/current-waves/interfaces/interfaces-versioning-model.md`.
