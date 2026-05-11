# External Developer Boundary

YAI Interfaces is the canonical surface for external developers building
clients, UIs, integrations, automations, generated clients, or conformance
tools.

## External Developers Consume

- Protocol/API operation contracts.
- Transport contracts.
- Schemas, envelopes, errors, registries, and mappings.
- OpenAPI projections.
- Official SDK packages after SDK drain.
- Examples and conformance profiles.

## External Developers Do Not Consume

- YAI runtime internals as public API.
- Console terminal UX internals as protocol truth.
- Web/account/product internals as interface truth.
- Historical SDK repository state after tombstone.

## Rule

External integrations should treat YAI Interfaces as the public developer
contract axis and should use conformance profiles to prove compatibility.
