/* SPDX-License-Identifier: Apache-2.0 */
#pragma once

#ifdef __cplusplus
extern "C" {
#endif

#define YAI_SDK_ABI_VERSION 1

int yai_sdk_abi_version(void);
const char *yai_sdk_version(void);

/* Canonical unified-runtime public taxonomy. */
#include <yai_sdk/core.h>
#include <yai_sdk/runtime.h>
#include <yai_sdk/models.h>
#include <yai_sdk/targets.h>
#include <yai_sdk/transport.h>
#include <yai_sdk/workspace.h>
#include <yai_sdk/exec.h>
#include <yai_sdk/db.h>
#include <yai_sdk/data.h>
#include <yai_sdk/graph.h>
#include <yai_sdk/knowledge.h>
#include <yai_sdk/source.h>
#include <yai_sdk/policy.h>
#include <yai_sdk/recovery.h>
#include <yai_sdk/debug.h>
#include <yai_sdk/governance.h>

/* Stable legacy module surface retained for compatibility. */
#include <yai_sdk/errors.h>
#include <yai_sdk/paths.h>
#include <yai_sdk/context.h>
#include <yai_sdk/client.h>
#include <yai_sdk/catalog.h>
#include <yai_sdk/protocol.h>
#include <yai_sdk/rpc.h>
#include <yai_sdk/log.h>
#include <yai_sdk/reply/reply.h>
#include <yai_sdk/reply/reply_builder.h>
#include <yai_sdk/reply/reply_json.h>

#ifdef __cplusplus
}
#endif
