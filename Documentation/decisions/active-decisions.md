# Active Decisions

## Interfaces Protocol Authority

YAI Interfaces is the source of truth for protocol contracts, operation
grammar, operation registry, transport mapping, envelopes, errors, schemas,
fixtures, mappings, OpenAPI projections, and interface conformance.

## Explicit Context

Interface operations must carry explicit context through envelopes and operation
inputs. Hidden runtime state is not interface authority.

## Delegated Ownership

Runtime/system truth belongs to YAI documentation. Terminal client UX truth
belongs to Console documentation. Official SDK package truth belongs under
`interfaces/packages/`.

## Historical Material

Historical decision files remain in `archive/` and are not the active
interfaces reading path.
