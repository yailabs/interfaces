# Generation

Generation documents generated surface boundaries and provenance rules for YAI
Interfaces.

## Generated Surfaces

Generated surfaces may include SDK clients, schemas, OpenAPI output, registry
outputs, projection outputs, and compatibility indexes.

## Source Inputs

Generated surfaces consume:

- operation and registry artifacts;
- schemas;
- envelopes;
- errors;
- mappings;
- transport contracts;
- lifecycle models;
- package templates after SDK drain.

## Rules

- Generated surfaces do not define protocol truth.
- Generated surfaces must record provenance.
- Generated surfaces must preserve operation ids, envelope semantics, error
  semantics, and transport eligibility.
- Generated surface claims require conformance evidence.
