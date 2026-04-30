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


# Migration From experience/clients/cli/source/ipc

`experience/clients/cli/source/ipc` is now a legacy migration surface.

Migration order:

1. promote family logic into `api/families/*`
2. move shared dispatch logic into `api/boundary/*`
3. convert `experience/clients/cli/source/cmd/*` to consume `api/*`
4. shrink and remove `experience/clients/cli/source/ipc`
