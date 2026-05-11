# Interface Source Of Truth

YAI Interfaces owns developer-interface truth.

Source-of-truth artifacts are:

- protocol contracts;
- operation registry;
- operation-to-transport mappings;
- schemas;
- envelopes;
- errors;
- registries;
- lifecycle and compatibility contracts.

Protocol, operation registry, schema, and mapping artifacts define interface
truth. OpenAPI, generated clients, SDK operation constants, SDK envelope types,
and package reference docs are projections over that truth.

SDK packages consume the interface truth as typed language surfaces. They must
not redefine protocol semantics, operation identifiers, transport grammar,
envelope grammar, error semantics, or runtime dispatch targets.
