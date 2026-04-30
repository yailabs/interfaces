<!--
YAI — Governed Case-Native Runtime

Copyright (c) 2026 Francesco Maiomascio.
All rights reserved.

This file is part of the YAI Community Source Tree.
Use, copying, modification, distribution, and production operation
are governed by the repository licensing documents, including
LICENSE, LICENSING.md, COMMERCIAL.md, and COPYING.

Development and non-production use is permitted under the applicable
YAI license terms. Production, organizational, persistent,
collaborative, customer-affecting, or business-critical use requires
a commercial license.
-->

# API

`api/` is the temporary in-repo source root for the future standalone `api` repository.

Wave 12G status: extraction-prepared, not extracted.
Wave 13 target: perform repository extraction and lifecycle closure.
Wave 14 target: SDK bridge generation over canonical API contracts.

## Current role

`api/` owns contract-facing surfaces for:
- contracts
- schemas
- envelope conventions
- error model conventions
- lifecycle/readiness state conventions
- family boundaries and registry descriptors
- conformance direction
- extraction manifest

`api/` is not a CLI mirror and not a dump of core structs.

## Extraction target (Wave 13)

Future `api` repository shape:
- `contracts/`
- `schemas/`
- `envelopes/`
- `errors/`
- `lifecycle/`
- `families/`
- `openapi/`
- `conformance/`
- `docs/`
- `versioning/`
- `extraction-manifest.json`

This wave does not create the external repository and does not move code out of `yai`.

## Transitional note

Some families still carry compatibility semantics (`session attach --user`, `session active-case`, CLI-anchored text outputs).
They remain operationally compatible in 12G and are explicitly tracked as extraction couplings for Wave 13.
