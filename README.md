<!--
YAI API — Canonical Contract Surface for Governed Action

Copyright (c) 2026 Francesco Maiomascio.
All rights reserved.

This file is part of the YAI Community Source Tree.
Use, copying, modification, distribution, and production operation
are governed by the repository licensing documents, including
LICENSE, LICENSING.md, and COMMERCIAL.md.

Development and non-production use is permitted under the applicable
YAI license terms. Production, organizational, persistent,
collaborative, customer-affecting, or business-critical use requires
a commercial license.
-->

<div align="center">
  <img
    src="docs/reference/figures/yai-transp.png"
    alt="YAI"
    width="180"
  />
  <br />

  <strong>YAI API</strong>
  <br />
  <span>API projection for accountable runtime interaction.</span>

  <br /><br />

  ![Stage](https://img.shields.io/badge/stage-active%20development-2563eb?style=flat&labelColor=1f2937)
  ![Scope](https://img.shields.io/badge/scope-contracts%20%2F%20schemas%20%2F%20lifecycle-0f766e?style=flat&labelColor=1f2937)
  ![Repo](https://img.shields.io/badge/repo-yai--labs%2Fapi-334155?style=flat&labelColor=1f2937)
  ![License](https://img.shields.io/badge/license-community%20source-374151?style=flat&labelColor=1f2937)

  <br /><br />


</div>

## Contents

- [Why this repository exists](#why-this-repository-exists)
- [Repository identity](#repository-identity-local-vs-remote)
- [Contract boundary](#contract-boundary)
- [SDK consumption boundary](#sdk-consumption-boundary)
- [Wave status](#wave-status)
- [Build and validation](#build-and-validation)
- [Licensing](#licensing)

<br />

## Why This Repository Exists

`api` is the API projection surface for YAI. It owns API exposure grammar
(families, verbs, operations, projections), OpenAPI projection, API registry,
transport mapping, and API-specific conformance used by SDK and client
surfaces.

Canonical protocol meaning now drains toward `yai/protocols`. Runtime
implementation remains in `yai-labs/yai`.

## Repository Identity (Local vs Remote)

- Remote repository identity: `yai-labs/api`
- Conceptual product identity may still reference: `yai-api`

## Contract Boundary

Canonical API projection source lives here (`api`).

- Owns: OpenAPI, `registry/api-*.json`, API projection docs, HTTP/transport request-response mapping, API-specific conformance.
- Mirrors or projects: selected protocol-neutral schemas, fixtures, and conformance while cutover to `yai/protocols` is in progress.
- Does not own: transport-neutral protocol meaning, runtime execution, client product behavior, SDK package implementations, provider backends, account backend behavior.

Boundary guarantees:
- Root `yai/api` remains physically drained.
- `yai/core/api` remains absent.
- Runtime adapters remain in `yai/runtime/boundary/api`.

## SDK Consumption Boundary

SDK is the official client consumption layer.
Clients should normally consume SDK packages, not runtime adapters directly.

- SDK packages: `packages/c`, `packages/typescript`, `packages/python`
- Direct API usage policy: debug/conformance/bootstrap only

## Wave Status

- Wave 13: contract extraction and lifecycle closure completed.
- Wave 14: SDK contract-bound generation/normalization in progress.

## Build and Validation

Typical validation in this repository:

```sh
python3 -m json.tool extraction/source-manifest.json >/dev/null
```

## Licensing

> [!IMPORTANT]
> YAI is the **YAI Community Source Tree**. Development and non-production use are permitted under the applicable license terms. Commercial licensing is required for production, organizational, persistent, collaborative, customer-affecting, or business-critical use.


## Branch Alignment

Active cross-repo hardening branch: `refoundation/phase-01`.
