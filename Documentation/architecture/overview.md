# API Architecture Overview

The API repository is the protocol authority for YAI clients and runtime-facing adapters. It defines what operations exist, how they are named, how they are carried over transports, and how request, response, readiness, error, and stream data are shaped.

The API layer is a contract and projection layer. It does not implement runtime behavior, package SDK clients, or define terminal UX. Those concerns are delegated to YAI, SDK, and Console documentation.

## Canonical Model

- Operation families are public protocol families such as case, identity, runtime, operator, client, SDK projection, and execution.
- Operations are expressed with a stable grammar and stored in registry artifacts.
- Transports carry the same operation model through local IPC, loopback HTTP, event streams, secure remote paths, subprocess compatibility, and in-process tests.
- Envelopes and errors provide a transport-neutral request/response contract.
- Conformance checks validate registry, schema, envelope, mapping, transport, and domain projections.

## Source Material Absorbed

DOCS.2 absorbed the pre-reset API plane, family, source-of-truth, and projection filesystem notes into this architecture section. The inspected originals are preserved under `archive/old-flat-root/`.
