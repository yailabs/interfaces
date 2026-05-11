# YAI Interfaces Documentation Index

## Official Interfaces Reading Path

1. `README.md`
2. `INDEX.md`
3. `architecture/overview.md`
4. `architecture/interface-source-of-truth.md`
5. `architecture/protocol-api-boundary.md`
6. `architecture/sdk-consumption-boundary.md`
7. `architecture/generation-boundary.md`
8. `architecture/package-boundary.md`
9. `architecture/external-developer-boundary.md`
10. `operations/operation-grammar.md`
11. `operations/operation-to-transport-mapping.md`
12. `transports/local-ipc-rpc.md`
13. `envelopes/request-response-model.md`
14. `errors/error-model.md`
15. `conformance/conformance-policy.md`
16. `packages/README.md`
17. `generation/README.md`
18. `examples/README.md`
19. `reference/registry-index.md`

## Architecture

- `architecture/overview.md`
- `architecture/interface-source-of-truth.md`
- `architecture/protocol-api-boundary.md`
- `architecture/sdk-consumption-boundary.md`
- `architecture/generation-boundary.md`
- `architecture/conformance-boundary.md`
- `architecture/package-boundary.md`
- `architecture/external-developer-boundary.md`
- `architecture/operation-model.md`
- `architecture/transport-model.md`
- `architecture/envelope-error-stream-model.md`
- `architecture/client-projection-boundary.md`
- `architecture/runtime-implementation-boundary.md`

## Operations

- `operations/operation-grammar.md`
- `operations/operation-registry.md`
- `operations/operation-to-transport-mapping.md`
- `operations/command-projection-model.md`
- `operations/action-descriptor-model.md`

## Transports

- `transports/local-ipc-rpc.md`
- `transports/local-http-loopback.md`
- `transports/local-event-stream.md`
- `transports/lan-secure-remote.md`
- `transports/remote-https.md`
- `transports/subprocess-stdio-compat.md`
- `transports/in-process-test.md`
- `transports/transport-contract-index.md`

## Envelopes And Errors

- `envelopes/request-response-model.md`
- `envelopes/request-envelope.md`
- `envelopes/response-envelope.md`
- `envelopes/readiness-envelope.md`
- `envelopes/stream-frame-model.md`
- `errors/error-model.md`
- `errors/error-code-registry.md`
- `errors/http-status-map.md`
- `errors/transport-error-mapping.md`

## Domains

- `domains/case.md`
- `domains/identity.md`
- `domains/runtime.md`
- `domains/operator.md`
- `domains/client.md`
- `domains/sdk.md`
- `domains/execution.md`

## Conformance

- `conformance/conformance-policy.md`
- `conformance/release-policy.md`
- `conformance/versioning-and-compatibility.md`
- `conformance/implementation-readiness.md`
- `conformance/check-index.md`
- `conformance/sdk-conformance.md`
- `conformance/package-validation-residuals.md`

## Packages

- `packages/README.md`
- `packages/package-taxonomy.md`
- `packages/package-release-model.md`
- `packages/rust.md`
- `packages/python.md`
- `packages/typescript.md`
- `packages/c.md`
- `packages/package-compatibility.md`

## Generation

- `generation/README.md`
- `generation/generated-surface.md`
- `generation/sdk-generation.md`
- `generation/schema-generation.md`
- `generation/openapi-generation.md`
- `generation/registry-generation.md`
- `generation/provenance-requirements.md`

## Examples

- `examples/README.md`
- `examples/external-client-authoring.md`
- `examples/local-runtime-connection.md`
- `examples/protocol-examples.md`
- `examples/sdk-examples.md`

## Reference

- `reference/registry-index.md`
- `reference/schema-index.md`
- `reference/fixture-index.md`
- `reference/openapi-index.md`
- `reference/contract-index.md`
- `reference/package-index.md`
- `reference/sdk-package-index.md`
- `reference/generated-surface-index.md`
- `reference/transport-artifact-index.md`

## Cross-Repo Model

YAI owns runtime and system truth. Console owns terminal client UX truth. Product
repositories own web, account, dashboard, download, and commercial surfaces.

Developer and client flow:

```text
external client or Console or future Studio
  -> interfaces SDK/API
  -> yai runtime/system effect
```
