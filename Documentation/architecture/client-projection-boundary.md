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

- terminal client UX truth to Console documentation
- runtime behavior and system truth to YAI runtime documentation

Official SDK package behavior now lives under `interfaces/packages/`.

## Projection Rule

Client projections must be derived from interface operation and action
descriptor records. A client may choose presentation, command wording,
navigation, or UI grouping, but those choices do not redefine protocol truth.
