# SDK Consumption Boundary

SDK packages are typed consumers of YAI Interfaces contracts.

## Current Phase

The repository is currently `pre-sdk-drain`. SDK package source remains in
`../sdk` until later INTF waves classify and move package material into
`interfaces/packages/`.

## SDK Owns After Drain

After SDK drain, official SDK packages own language-specific package behavior,
ergonomics, release metadata, and compatibility aliases under
`interfaces/packages/`.

## SDK Does Not Own

SDK packages do not own protocol version, operation semantics, transport truth,
envelope shape, error shape, registry truth, schema truth, or conformance truth.

## Consumption Rule

SDK packages consume protocol, operation, transport, schema, envelope, error,
registry, mapping, lifecycle, and conformance definitions from YAI Interfaces.
They must report unavailable, deferred, blocked, denied, and error states
honestly.
