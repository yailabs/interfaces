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


#include "api/contracts/identity/surface_ref.h"

#include <stdio.h>
#include <string.h>

void yai_api_surface_ref_set(yai_api_surface_ref_t *ref, const char *value)
{
    if (!ref) return;
    memset(ref, 0, sizeof(*ref));
    snprintf(ref->value, sizeof(ref->value), "%s", value ? value : "");
}
