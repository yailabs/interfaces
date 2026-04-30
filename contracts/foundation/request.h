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


#ifndef YAI_API_CONTRACTS_FOUNDATION_REQUEST_H
#define YAI_API_CONTRACTS_FOUNDATION_REQUEST_H

#include <stddef.h>

typedef struct {
    char family_ref[32];
    char surface_ref[64];
    char command_ref[64];
    int argc;
    char **argv;
} yai_api_request_t;

void yai_api_request_init(yai_api_request_t *request,
                          const char *family_ref,
                          const char *surface_ref,
                          const char *command_ref,
                          int argc,
                          char **argv);

#endif
