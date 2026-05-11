# Action Descriptor Model

Action descriptors connect API operations to client-consumable action metadata while keeping protocol truth in the API registry.

## Descriptor Fields

An action descriptor may include:

- action id
- operation id
- family and capability group
- required context such as case, identity, operator, or runtime posture
- safety and gate metadata
- streamability and transport eligibility
- conformance expectations

## Registry Relationship

`registry/yai-actions.v1.json` is indexed by `reference/registry-index.md` and validated by conformance checks. It is a protocol projection artifact, not a client UX file.

## Boundary

Action descriptors can inform client rendering, but they do not own SDK package APIs or Console terminal UX.
