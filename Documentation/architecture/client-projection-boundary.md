# Client Projection Boundary

YAI Interfaces defines what clients can project from the protocol/API layer. It
does not own client implementation, package ergonomics, screen layout, or
terminal interaction design.

## Interfaces Client Boundary

YAI Interfaces owns:

- operation and action descriptor semantics
- client references and attachment references
- request/response contract consumed by clients
- operation projection metadata used by clients
- compatibility boundaries for older transport paths

YAI Interfaces delegates:

- current typed client/package source to `../sdk` until SDK drain
- future official SDK package behavior to `interfaces/packages/`
- terminal client UX truth to `../console/Documentation`
- runtime behavior and system truth to `../yai/Documentation`

## Projection Rule

Client projections must be derived from interface operation and action
descriptor records. A client may choose presentation, command wording,
navigation, or UI grouping, but those choices do not redefine protocol truth.
