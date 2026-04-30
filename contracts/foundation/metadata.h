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


#ifndef YAI_API_CONTRACTS_FOUNDATION_METADATA_H
#define YAI_API_CONTRACTS_FOUNDATION_METADATA_H

typedef struct {
    char trace_id[64];
    char client_id[64];
} yai_api_metadata_t;

void yai_api_metadata_init(yai_api_metadata_t *metadata, const char *trace_id, const char *client_id);

#endif
