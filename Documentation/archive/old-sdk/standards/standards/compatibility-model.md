# Compatibility Model

SDK compatibility protects existing consumers while moving package surfaces toward API-aligned typed clients.

## Allowed Compatibility

- Explicit aliases with canonical replacements.
- Transitional native package helpers.
- Generated or exported compatibility snapshots.
- Package-level deprecation windows with validation coverage.

## Forbidden Compatibility

- Treating compatibility names as new canonical grammar.
- Requiring live runtime or unrelated repository layout as package truth.
- Shelling out to retired product surfaces for core SDK behavior.
- Hiding unavailable or blocked transport state.
