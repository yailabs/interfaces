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


#ifndef YAI_API_CONTRACTS_FOUNDATION_ERROR_H
#define YAI_API_CONTRACTS_FOUNDATION_ERROR_H

typedef struct {
    char code[64];
    char message[256];
} yai_api_error_t;

void yai_api_error_set(yai_api_error_t *error, const char *code, const char *message);

#endif
