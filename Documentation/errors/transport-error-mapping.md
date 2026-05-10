# Transport Error Mapping

Transport error mapping defines how canonical API errors appear on each transport.

## Artifact References

- `errors/error-transport-map.v1.md`
- `transports/local-ipc-rpc/errors.v1.md`
- `transports/local-http-loopback/errors.v1.md`
- `transports/local-event-stream/errors-terminal-events.v1.md`
- `transports/lan-secure/errors.v1.md`
- `transports/remote-https/errors.v1.md`
- `transports/subprocess-stdio-compat/errors.v1.md`
- `transports/in-process-test/errors.v1.md`

## Mapping Rule

Transport-specific failures must resolve to canonical API error codes or documented transport errors. They must not create hidden operation semantics.
