# Old SDK Tombstone Summary

INTF.7 tombstoned the old SDK repository.

The old SDK repository is historical only. It must not receive active SDK
source, generated surfaces, conformance checks, or developer-interface
documentation.

Canonical active locations:

- Rust package: `interfaces/packages/rust`
- Python package: `interfaces/packages/python`
- TypeScript package: `interfaces/packages/typescript`
- C package: `interfaces/packages/c`
- Protocol/API truth: `interfaces`
- Conformance: `interfaces/conformance`
- Generation/provenance: `interfaces/generators` and `interfaces/projections`
- Historical old SDK archive: `interfaces/Documentation/archive/old-sdk`

The old SDK repo must not define protocol truth and must not be used by Console
or YAI as an active dependency.
