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


#ifndef YAI_API_CONTRACTS_FOUNDATION_RESPONSE_H
#define YAI_API_CONTRACTS_FOUNDATION_RESPONSE_H

typedef struct {
    int status;
    char message[2048];
} yai_api_response_t;

void yai_api_response_set(yai_api_response_t *response, int status, const char *message);

#endif
