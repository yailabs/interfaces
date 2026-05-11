# ==========================================
# yai-sdk (C) Build System
# ==========================================

CC ?= cc
AR ?= ar
ARFLAGS ?= rcs
ROOT_DIR := $(abspath .)
SDK_REPO_ROOT := $(abspath $(ROOT_DIR)/../..)

OUT_BUILD_DIR ?= $(ROOT_DIR)/build
OUT_LIB_DIR   ?= $(ROOT_DIR)/dist/lib
OUT_BIN_DIR   ?= $(ROOT_DIR)/dist/bin
BUILD_DIR := $(OUT_BUILD_DIR)
LIB_DIR   := $(OUT_LIB_DIR)
BIN_DIR   := $(OUT_BIN_DIR)
DOCS_DIR  ?= $(ROOT_DIR)/dist/docs

PREFIX ?= /usr/local
INSTALL_LIB_DIR ?= $(PREFIX)/lib
INSTALL_INC_DIR ?= $(PREFIX)/include

# --- Resolve law path (compatibility source, no structural pin implied) ---
YAI_SDK_COMPAT_LAW_DIR ?= $(shell $(SDK_REPO_ROOT)/tools/sdk/sh/resolve_law.sh)
YAI_LAW_ROOT ?= $(YAI_SDK_COMPAT_LAW_DIR)

LAW_INC_PROTOCOL := $(YAI_SDK_COMPAT_LAW_DIR)/contracts/protocol/include
LAW_INC_VAULT    := $(YAI_SDK_COMPAT_LAW_DIR)/contracts/vault/include
LAW_INC_RUNTIME  := $(YAI_SDK_COMPAT_LAW_DIR)/contracts/protocol/runtime/include

TRANSITIONAL_YAI_ROOT := $(abspath $(SDK_REPO_ROOT)/../yai)
TRANSITIONAL_YAI_INCLUDE := $(TRANSITIONAL_YAI_ROOT)/include

LAW_PROTOCOL_HEADER := $(YAI_SDK_COMPAT_LAW_DIR)/contracts/protocol/include/protocol.h
LAW_COMPAT_MODE := missing
ifneq ($(wildcard $(LAW_PROTOCOL_HEADER)),)
LAW_COMPAT_MODE := external-law-export
else ifneq ($(wildcard $(TRANSITIONAL_YAI_INCLUDE)/ipc/rpc.h),)
LAW_COMPAT_MODE := transitional-yai-ipc
endif

# Compiler and linker flags
CFLAGS ?= -Wall -Wextra -O2 -std=c11 -MMD -MP
CFLAGS += -I$(ROOT_DIR)/include -I$(ROOT_DIR)/include/compat -I$(ROOT_DIR)/third_party/cjson
CFLAGS += -I$(LAW_INC_PROTOCOL) -I$(LAW_INC_VAULT) -I$(LAW_INC_RUNTIME)
ifeq ($(LAW_COMPAT_MODE),transitional-yai-ipc)
CFLAGS += -I$(TRANSITIONAL_YAI_INCLUDE)
endif
CFLAGS += -DYAI_LAW_ROOT='"$(YAI_SDK_COMPAT_LAW_DIR)"' -DYAI_SDK_COMPAT_LAW_DIR='"$(YAI_SDK_COMPAT_LAW_DIR)"' -D_POSIX_C_SOURCE=200809L
YAI_SDK_VERSION ?= 0.1.0
CFLAGS += -DYAI_SDK_VERSION_STR='"$(YAI_SDK_VERSION)"'
CFLAGS += -fPIC
LDFLAGS ?=
EXTRA_CFLAGS ?=

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
SDK_SO_LDFLAGS := -dynamiclib
PROTOCOL_SO_LDFLAGS := -dynamiclib
else
SDK_SO_LDFLAGS := -shared -Wl,-soname,libyai_sdk.so
PROTOCOL_SO_LDFLAGS := -shared -Wl,-soname,libruntime_protocol.so
endif

SDK_LIB      := $(LIB_DIR)/libyai_sdk.a
PROTOCOL_LIB := $(LIB_DIR)/libruntime_protocol.a
SDK_SO       := $(LIB_DIR)/libyai_sdk.so
PROTOCOL_SO  := $(LIB_DIR)/libruntime_protocol.so

SRCS_PROTOCOL := \
  src/rpc/rpc_client.c \
  third_party/cjson/cJSON.c

SRCS_SDK := \
  src/sdk_public.c \
  src/platform/paths.c \
  src/platform/context.c \
  src/platform/transport.c \
  src/platform/log.c \
  src/client/client.c \
  src/reply/reply_builder.c \
  src/reply/reply_json.c \
  src/source/source.c \
  src/protocol/reply_map.c \
  src/models/runtime_models.c \
  src/registry/registry.c \
  src/catalog/catalog.c \
  src/registry/registry_help.c \
  src/registry/registry_paths.c \
  src/registry/registry_cache.c \
  src/registry/registry_load.c \
  src/registry/registry_query.c \
  src/registry/registry_validate.c

OBJS_PROTOCOL := $(patsubst %.c,$(BUILD_DIR)/%.o,$(SRCS_PROTOCOL))
OBJS_SDK      := $(patsubst %.c,$(BUILD_DIR)/%.o,$(SRCS_SDK))
ALL_OBJS      := $(OBJS_PROTOCOL) $(OBJS_SDK)
DEPS          := $(ALL_OBJS:.o=.d)

TEST_BIN := $(BUILD_DIR)/tests/sdk_smoke
CATALOG_TEST_BIN := $(BUILD_DIR)/tests/catalog_smoke
HELP_INDEX_TEST_BIN := $(BUILD_DIR)/tests/help_index_smoke
WORKSPACE_TEST_BIN := $(BUILD_DIR)/tests/workspace_smoke
RUNTIME_LOCATOR_TEST_BIN := $(BUILD_DIR)/tests/runtime_locator_smoke
PUBLIC_SURFACE_TEST_BIN := $(BUILD_DIR)/tests/public_surface_smoke
MODELS_CONTRACT_TEST_BIN := $(BUILD_DIR)/tests/models_contract_smoke
WORKSPACE_TYPED_SURFACE_TEST_BIN := $(BUILD_DIR)/tests/workspace_typed_surface_smoke
SOURCE_TYPED_SURFACE_TEST_BIN := $(BUILD_DIR)/tests/source_typed_surface_smoke
SDK_TEST_HOME := $(BUILD_DIR)/test-home
EXAMPLE_BASIC_BIN := $(BIN_DIR)/example_01_basic_connection
EXAMPLE_CONTEXT_BIN := $(BIN_DIR)/example_02_workspace_context
EXAMPLE_CUSTOM_BIN := $(BIN_DIR)/example_03_custom_control_call
EXAMPLE_VERTICAL_BIN := $(BIN_DIR)/example_04_workspace_verticalized
EXAMPLE_SOURCE_BIN := $(BIN_DIR)/example_05_source_plane_typed

.PHONY: all clean dirs test test-repeat info libs api-boundary-check check coverage docs docs-clean install examples check-config

all: libs

libs: $(SDK_LIB) $(PROTOCOL_LIB) $(SDK_SO) $(PROTOCOL_SO)

info:
	@echo "YAI_SDK_ROOT: $(ROOT_DIR)"
	@echo "YAI_SDK_COMPAT_LAW_DIR: $(YAI_SDK_COMPAT_LAW_DIR)"
	@echo "YAI_LAW_ROOT (legacy alias): $(YAI_LAW_ROOT)"
	@echo "LAW_COMPAT_MODE: $(LAW_COMPAT_MODE)"
	@if [ "$(LAW_COMPAT_MODE)" = "transitional-yai-ipc" ]; then 	  echo "TRANSITIONAL_YAI_INCLUDE: $(TRANSITIONAL_YAI_INCLUDE)"; 	fi
	@echo "Protocol Objects: $(OBJS_PROTOCOL)"


check-config:
	@if [ -z "$(YAI_SDK_COMPAT_LAW_DIR)" ]; then \
	  echo "ERROR: missing YAI_SDK_COMPAT_LAW_DIR."; \
	  echo "Set YAI_SDK_COMPAT_LAW_DIR to a law compatibility export containing contracts/protocol/include/protocol.h"; \
	  echo "Example: export YAI_SDK_COMPAT_LAW_DIR=/absolute/path/to/law-export"; \
	  exit 2; \
	fi
	@if [ ! -f "$(YAI_SDK_COMPAT_LAW_DIR)/contracts/protocol/include/protocol.h" ]; then \
	  echo "ERROR: invalid YAI_SDK_COMPAT_LAW_DIR=$(YAI_SDK_COMPAT_LAW_DIR)"; \
	  echo "Missing contracts/protocol/include/protocol.h"; \
	  exit 2; \
	fi
	@echo "[CHECK-CONFIG] law compatibility export ok: $(YAI_SDK_COMPAT_LAW_DIR)"

dirs:
	@mkdir -p $(BUILD_DIR) $(LIB_DIR) $(BUILD_DIR)/tests $(BIN_DIR)

$(PROTOCOL_LIB): $(OBJS_PROTOCOL)
	@echo "[AR] $@"
	@$(AR) $(ARFLAGS) $@ $^

$(SDK_LIB): $(ALL_OBJS)
	@echo "[AR] $@"
	@$(AR) $(ARFLAGS) $@ $^

$(SDK_SO): $(ALL_OBJS)
	@echo "[LD.SO] $@"
	@$(CC) $(SDK_SO_LDFLAGS) -o $@ $^ $(LDFLAGS)

$(PROTOCOL_SO): $(ALL_OBJS)
	@echo "[LD.SO] $@"
	@$(CC) $(PROTOCOL_SO_LDFLAGS) -o $@ $^ $(LDFLAGS)

$(BUILD_DIR)/%.o: %.c | dirs
	@mkdir -p $(dir $@)
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) -c $< -o $@

clean:
	@rm -rf $(BUILD_DIR) $(LIB_DIR) $(BIN_DIR) $(DOCS_DIR) $(ROOT_DIR)/coverage

api-boundary-check:
	@$(SDK_REPO_ROOT)/tools/sdk/sh/check_api_boundaries.sh

test: check-config api-boundary-check $(TEST_BIN) $(CATALOG_TEST_BIN) $(HELP_INDEX_TEST_BIN) $(WORKSPACE_TEST_BIN) $(RUNTIME_LOCATOR_TEST_BIN) $(PUBLIC_SURFACE_TEST_BIN) $(MODELS_CONTRACT_TEST_BIN) $(WORKSPACE_TYPED_SURFACE_TEST_BIN) $(SOURCE_TYPED_SURFACE_TEST_BIN)
	@rm -rf "$(SDK_TEST_HOME)"
	@mkdir -p "$(SDK_TEST_HOME)"
	@echo "[TEST_HOME] $(SDK_TEST_HOME)"
	@$(MAKE) api-boundary-check
	@echo "[RUN] $(TEST_BIN)"
	@HOME="$(SDK_TEST_HOME)" YAI_LAW_ROOT="$(YAI_SDK_COMPAT_LAW_DIR)" YAI_SDK_COMPAT_REGISTRY_DIR="$(YAI_SDK_COMPAT_LAW_DIR)" $(TEST_BIN)
	@echo "[RUN] $(CATALOG_TEST_BIN)"
	@HOME="$(SDK_TEST_HOME)" YAI_LAW_ROOT="$(YAI_SDK_COMPAT_LAW_DIR)" YAI_SDK_COMPAT_REGISTRY_DIR="$(YAI_SDK_COMPAT_LAW_DIR)" $(CATALOG_TEST_BIN)
	@echo "[RUN] $(HELP_INDEX_TEST_BIN)"
	@HOME="$(SDK_TEST_HOME)" YAI_LAW_ROOT="$(YAI_SDK_COMPAT_LAW_DIR)" YAI_SDK_COMPAT_REGISTRY_DIR="$(YAI_SDK_COMPAT_LAW_DIR)" $(HELP_INDEX_TEST_BIN)
	@echo "[RUN] $(WORKSPACE_TEST_BIN)"
	@HOME="$(SDK_TEST_HOME)" YAI_LAW_ROOT="$(YAI_SDK_COMPAT_LAW_DIR)" YAI_SDK_COMPAT_REGISTRY_DIR="$(YAI_SDK_COMPAT_LAW_DIR)" $(WORKSPACE_TEST_BIN)
	@echo "[RUN] $(RUNTIME_LOCATOR_TEST_BIN)"
	@HOME="$(SDK_TEST_HOME)" YAI_LAW_ROOT="$(YAI_SDK_COMPAT_LAW_DIR)" YAI_SDK_COMPAT_REGISTRY_DIR="$(YAI_SDK_COMPAT_LAW_DIR)" $(RUNTIME_LOCATOR_TEST_BIN)
	@echo "[RUN] $(PUBLIC_SURFACE_TEST_BIN)"
	@HOME="$(SDK_TEST_HOME)" YAI_LAW_ROOT="$(YAI_SDK_COMPAT_LAW_DIR)" YAI_SDK_COMPAT_REGISTRY_DIR="$(YAI_SDK_COMPAT_LAW_DIR)" $(PUBLIC_SURFACE_TEST_BIN)
	@echo "[RUN] $(MODELS_CONTRACT_TEST_BIN)"
	@HOME="$(SDK_TEST_HOME)" YAI_LAW_ROOT="$(YAI_SDK_COMPAT_LAW_DIR)" YAI_SDK_COMPAT_REGISTRY_DIR="$(YAI_SDK_COMPAT_LAW_DIR)" $(MODELS_CONTRACT_TEST_BIN)
	@echo "[RUN] $(WORKSPACE_TYPED_SURFACE_TEST_BIN)"
	@HOME="$(SDK_TEST_HOME)" YAI_LAW_ROOT="$(YAI_SDK_COMPAT_LAW_DIR)" YAI_SDK_COMPAT_REGISTRY_DIR="$(YAI_SDK_COMPAT_LAW_DIR)" $(WORKSPACE_TYPED_SURFACE_TEST_BIN)
	@echo "[RUN] $(SOURCE_TYPED_SURFACE_TEST_BIN)"
	@HOME="$(SDK_TEST_HOME)" YAI_LAW_ROOT="$(YAI_SDK_COMPAT_LAW_DIR)" YAI_SDK_COMPAT_REGISTRY_DIR="$(YAI_SDK_COMPAT_LAW_DIR)" $(SOURCE_TYPED_SURFACE_TEST_BIN)

test-repeat:
	@echo "[RUN] deterministic check #1"
	@$(MAKE) --no-print-directory test
	@echo "[RUN] deterministic check #2"
	@$(MAKE) --no-print-directory test

check:
	@$(MAKE) clean
	@$(MAKE) EXTRA_CFLAGS="-O1 -g -fsanitize=address,undefined -fno-omit-frame-pointer" LDFLAGS="$(LDFLAGS) -fsanitize=address,undefined" test

coverage:
	@$(MAKE) clean
	@$(MAKE) EXTRA_CFLAGS="-O0 -g --coverage" LDFLAGS="$(LDFLAGS) --coverage" test
	@mkdir -p coverage
	@if command -v gcovr >/dev/null 2>&1; then \
	  gcovr -r . --html --html-details -o coverage/index.html; \
	  echo "[COVERAGE] coverage/index.html"; \
	else \
	  echo "[COVERAGE] gcovr not found; raw .gcda/.gcno files generated under build/"; \
	fi

docs:
	@mkdir -p $(DOCS_DIR)
	@doxygen Doxyfile
	@echo "[DOCS] $(DOCS_DIR)/html/index.html"

docs-clean:
	@rm -rf $(DOCS_DIR)

examples: $(EXAMPLE_BASIC_BIN) $(EXAMPLE_CONTEXT_BIN) $(EXAMPLE_CUSTOM_BIN) $(EXAMPLE_VERTICAL_BIN) $(EXAMPLE_SOURCE_BIN)
	@echo "[EXAMPLES] built under $(BIN_DIR)"

install: libs
	@install -d "$(DESTDIR)$(INSTALL_LIB_DIR)" "$(DESTDIR)$(INSTALL_INC_DIR)/yai_sdk"
	@install -m 0644 $(SDK_LIB) "$(DESTDIR)$(INSTALL_LIB_DIR)/"
	@install -m 0644 $(PROTOCOL_LIB) "$(DESTDIR)$(INSTALL_LIB_DIR)/"
	@install -m 0755 $(SDK_SO) "$(DESTDIR)$(INSTALL_LIB_DIR)/"
	@install -m 0755 $(PROTOCOL_SO) "$(DESTDIR)$(INSTALL_LIB_DIR)/"
	@cp -R include/yai_sdk "$(DESTDIR)$(INSTALL_INC_DIR)/"
	@echo "[INSTALL] libs -> $(DESTDIR)$(INSTALL_LIB_DIR), headers -> $(DESTDIR)$(INSTALL_INC_DIR)/yai_sdk"

$(TEST_BIN): tests/sdk_smoke.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@

$(CATALOG_TEST_BIN): tests/catalog_smoke.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@

$(HELP_INDEX_TEST_BIN): tests/help_index_smoke.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@

$(WORKSPACE_TEST_BIN): tests/workspace_smoke.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@

$(RUNTIME_LOCATOR_TEST_BIN): tests/runtime_locator_smoke.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@

$(PUBLIC_SURFACE_TEST_BIN): tests/public_surface_smoke.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@

$(EXAMPLE_BASIC_BIN): examples/01_basic_connection.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@

$(EXAMPLE_CONTEXT_BIN): examples/02_workspace_context.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@

$(EXAMPLE_CUSTOM_BIN): examples/03_custom_control_call.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@

$(EXAMPLE_VERTICAL_BIN): examples/04_workspace_verticalized.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@

$(EXAMPLE_SOURCE_BIN): examples/05_source_plane_typed.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@

-include $(DEPS)

$(MODELS_CONTRACT_TEST_BIN): tests/models_contract_smoke.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@

$(WORKSPACE_TYPED_SURFACE_TEST_BIN): tests/workspace_typed_surface_smoke.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@

$(SOURCE_TYPED_SURFACE_TEST_BIN): tests/source_typed_surface_smoke.c $(SDK_LIB) | dirs
	@echo "[CC] $<"
	@$(CC) $(CFLAGS) $(EXTRA_CFLAGS) $< $(SDK_LIB) $(LDFLAGS) -o $@
