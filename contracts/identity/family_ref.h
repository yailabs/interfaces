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


#ifndef YAI_API_CONTRACTS_IDENTITY_FAMILY_REF_H
#define YAI_API_CONTRACTS_IDENTITY_FAMILY_REF_H

typedef struct {
    char value[32];
} yai_api_family_ref_t;

void yai_api_family_ref_set(yai_api_family_ref_t *ref, const char *value);

#endif
