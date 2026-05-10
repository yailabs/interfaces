# Client Projection Boundary

API defines what clients can project from the protocol. It does not own client implementation, package shape, screen layout, or terminal interaction design.

## API Client Boundary

API owns:

- operation and action descriptor semantics
- client references and attachment references
- request/response contract consumed by clients
- operation projection metadata used by clients
- compatibility boundaries for older transport paths

API delegates:

- typed client/package truth to `../sdk/Documentation/README.md` and the expected `../sdk/Documentation/INDEX.md`
- terminal client UX truth to `../console/Documentation`
- runtime behavior and system truth to `../yai/Documentation`

## Projection Rule

Client projections must be derived from API operation and action descriptor records. A client may choose presentation, command wording, navigation, or UI grouping, but those choices do not redefine protocol truth.
