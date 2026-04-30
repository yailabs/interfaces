/*
 * YAI — Governed Case-Native Runtime
 *
 * Copyright (c) 2026 Francesco Maiomascio.
 * All rights reserved.
 *
 * This file is part of the YAI Community Source Tree.
 * Use, copying, modification, distribution, and production operation
 * are governed by the repository licensing documents, including
 * LICENSE, LICENSING.md, COMMERCIAL.md, and COPYING.
 *
 * Development and non-production use is permitted under the applicable
 * YAI license terms. Production, organizational, persistent,
 * collaborative, customer-affecting, or business-critical use requires
 * a commercial license.
 */


#include "api/contracts/foundation/metadata.h"

#include <stdio.h>
#include <string.h>

void yai_api_metadata_init(yai_api_metadata_t *metadata, const char *trace_id, const char *client_id)
{
    if (!metadata) return;
    memset(metadata, 0, sizeof(*metadata));
    snprintf(metadata->trace_id, sizeof(metadata->trace_id), "%s", trace_id ? trace_id : "");
    snprintf(metadata->client_id, sizeof(metadata->client_id), "%s", client_id ? client_id : "");
}
