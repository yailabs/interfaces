# Error Code Registry

`errors/error-code-registry.v1.json` is the API error code authority.

## Rules

- Error codes are stable protocol values.
- Codes must map to safe client behavior and conformance expectations.
- Runtime exception names are not API error codes.
- Transport bindings may map error codes to HTTP status, stream terminal frames, or compatibility exit behavior.
