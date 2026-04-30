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


#include "api/contracts/runtime/execution.h"

#include <stdio.h>
#include <string.h>

void yai_api_execution_init(yai_api_execution_t *execution,
                            const char *execution_ref,
                            int exit_code)
{
    if (!execution) return;
    memset(execution, 0, sizeof(*execution));
    snprintf(execution->execution_ref, sizeof(execution->execution_ref), "%s",
             execution_ref ? execution_ref : "");
    execution->exit_code = exit_code;
}
