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


#ifndef YAI_API_CONTRACTS_RUNTIME_SESSION_H
#define YAI_API_CONTRACTS_RUNTIME_SESSION_H

typedef struct {
    char session_ref[64];
    char scope_id[64];
    int active;
} yai_api_session_t;

void yai_api_session_init(yai_api_session_t *session,
                          const char *session_ref,
                          const char *scope_id,
                          int active);

#endif
