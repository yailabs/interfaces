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


#include "api/contracts/runtime/session.h"

#include <stdio.h>
#include <string.h>

void yai_api_session_init(yai_api_session_t *session,
                          const char *session_ref,
                          const char *scope_id,
                          int active)
{
    if (!session) return;
    memset(session, 0, sizeof(*session));
    snprintf(session->session_ref, sizeof(session->session_ref), "%s",
             session_ref ? session_ref : "");
    snprintf(session->scope_id, sizeof(session->scope_id), "%s", scope_id ? scope_id : "");
    session->active = active;
}
