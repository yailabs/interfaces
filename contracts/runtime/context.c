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


#include "api/contracts/runtime/context.h"

#include <stdio.h>
#include <string.h>

void yai_api_context_init(yai_api_context_t *context,
                          const char *actor_id,
                          const char *case_id,
                          const char *flow_id)
{
    if (!context) return;
    memset(context, 0, sizeof(*context));
    snprintf(context->actor_id, sizeof(context->actor_id), "%s", actor_id ? actor_id : "");
    snprintf(context->case_id, sizeof(context->case_id), "%s", case_id ? case_id : "");
    snprintf(context->flow_id, sizeof(context->flow_id), "%s", flow_id ? flow_id : "");
}
