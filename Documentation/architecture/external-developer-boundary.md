# External Developer Boundary

External developers consume YAI Interfaces through:

- protocol documentation;
- operation, transport, envelope, and error docs;
- SDK packages;
- examples;
- conformance policy;
- compatibility and package matrices;
- generated and OpenAPI projections with provenance.

Developer and client flow:

```text
external client or Console or future Studio
  -> interfaces SDK/API
  -> yai runtime/system effect
```

External developer docs must identify whether a surface is protocol truth,
package projection, generated projection, or historical material.
