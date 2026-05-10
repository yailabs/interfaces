# Subprocess Stdio Compatibility

Subprocess stdio compatibility preserves a controlled compatibility transport for older process-based clients.

## Artifact References

- ``transports/subprocess-stdio-compat.v1.md``
- ``transports/subprocess-stdio-compat/``

## Contract Model

Compatibility covers purpose, environment boundary, stdout/stderr contract, exit status model, errors, limitations, deprecation policy, and conformance profile.

## Operation Relationship

Allowed operations are controlled by `mappings/operation-transport-map.v1.json` and related mapping policy. Transport docs describe how operations are carried; operation docs define what operations mean.
