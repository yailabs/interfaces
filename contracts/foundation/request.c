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


#include "api/contracts/foundation/request.h"

#include <stdio.h>
#include <string.h>

void yai_api_request_init(yai_api_request_t *request,
                          const char *family_ref,
                          const char *surface_ref,
                          const char *command_ref,
                          int argc,
                          char **argv)
{
    if (!request) return;
    memset(request, 0, sizeof(*request));
    snprintf(request->family_ref, sizeof(request->family_ref), "%s", family_ref ? family_ref : "");
    snprintf(request->surface_ref, sizeof(request->surface_ref), "%s",
             surface_ref ? surface_ref : "");
    snprintf(request->command_ref, sizeof(request->command_ref), "%s",
             command_ref ? command_ref : "");
    request->argc = argc;
    request->argv = argv;
}
