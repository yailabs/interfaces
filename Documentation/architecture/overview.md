# Interfaces Architecture Overview

YAI Interfaces is the developer-interface surface for YAI clients, SDK
packages, generated clients, external integrations, and runtime-facing
adapters. It defines what operations exist, how they are named, how they are
carried over transports, and how request, response, readiness, error, and
stream data are shaped.

The interfaces repository contains the protocol/API layer and prepares for
official SDK packages after SDK drain. It does not implement runtime behavior,
own terminal UX, or own web/account/product surfaces.

## Canonical Model

- Operation families are public protocol families such as case, identity,
  runtime, operator, client, SDK projection, and execution.
- The protocol/API layer defines operation grammar, operation registries,
  transport eligibility, envelopes, errors, schemas, and mappings.
- API `identity` is an upstream contract family for access/auth/account
  projections; it is not a native YAI runtime plane and projects to
  `../yai/src/runtime/access`.
- Transports carry the same operation model through local IPC, loopback HTTP,
  event streams, secure remote paths, subprocess compatibility, and in-process
  tests.
- Envelopes and errors provide a transport-neutral request/response contract.
- Conformance checks validate registry, schema, envelope, mapping, transport,
  generated surface, and package alignment claims.
- Official SDK packages consume interface contracts after SDK drain; they do
  not redefine protocol truth.

## Ownership Summary

`interfaces` owns developer-interface truth.

`yai` owns runtime, system, governance, service lifecycle, packaging, and core
architecture truth.

`console` owns CLI mode, TUI mode, command UX, runtime attachment UX, terminal
copy, routing, and help behavior.

`web` owns public, account, download, home, dashboard, and commercial surfaces.

## Source Material Absorbed

DOCS.2 absorbed the pre-reset API plane, family, source-of-truth, and
projection filesystem notes into this architecture section. INTF.2
canonicalizes the local repository identity from the former API source base to
YAI Interfaces. Historical originals are preserved under `archive/`.
