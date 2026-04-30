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

# Request / Response Model

Requests carry family, surface, command, metadata, and runtime context.

Responses should converge on envelope fields:
- `schema`
- `status`
- `reason`
- `message`
- typed payload (`data` or family payload)
- `refs`
- `warnings`
- `errors`

Canonical status vocabulary:
- `ok`
- `partial`
- `pending`
- `ready`
- `unavailable`
- `blocked`
- `denied`
- `error`

Compatibility note:
Legacy CLI-facing message strings can remain where required, but are not the final canonical API contract shape.
