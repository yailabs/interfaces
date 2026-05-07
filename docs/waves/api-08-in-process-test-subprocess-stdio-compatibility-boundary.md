# API.08 — In-process Test / Subprocess Stdio Compatibility Boundary

## Status

* Delivery: API.08
* Status: done
* Track: API / Transport / SDK / Runtime alignment
* Repo branch: `refoundation/phase-01`
* Repo change type: test/compat transport boundary verticalization
* Previous delivery: API.07 — LAN Secure / Remote HTTPS Boundary Split
* Next delivery: API.09 — Cloud Compute Boundary

## Purpose

API.08 separates `in_process_test` from `subprocess_stdio_compat` and prevents
both from being confused with canonical product transports or hidden runtime or
SDK shortcuts.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| `api` | `transports/in-process-test.v1.md` | modified | expand the In-process Test root contract and point to the verticalized subtree |
| `api` | `transports/in-process-test/README.md` | added | create the In-process Test contract root |
| `api` | `transports/in-process-test/purpose.v1.md` | added | define test and conformance purpose |
| `api` | `transports/in-process-test/harness-boundary.v1.md` | added | define explicit harness boundary posture |
| `api` | `transports/in-process-test/conformance-usage.v1.md` | added | define approved conformance usage |
| `api` | `transports/in-process-test/security-limitations.v1.md` | added | prevent bypass of guards, credentials, and persistent state safety |
| `api` | `transports/in-process-test/non-product-boundary.v1.md` | added | prevent promotion to product transport |
| `api` | `transports/in-process-test/errors.v1.md` | added | freeze harness-specific error categories |
| `api` | `transports/in-process-test/conformance-profile.v1.md` | added | define minimum in-process contract claims |
| `api` | `transports/subprocess-stdio-compat.v1.md` | modified | expand the subprocess stdio compat root contract and point to the verticalized subtree |
| `api` | `transports/subprocess-stdio-compat/README.md` | added | create the subprocess stdio compat contract root |
| `api` | `transports/subprocess-stdio-compat/purpose.v1.md` | added | define legacy/debug/migration purpose |
| `api` | `transports/subprocess-stdio-compat/stdout-stderr-contract.v1.md` | added | freeze stdout/stderr and envelope posture |
| `api` | `transports/subprocess-stdio-compat/exit-status-model.v1.md` | added | separate process exit status from operation result |
| `api` | `transports/subprocess-stdio-compat/env-boundary.v1.md` | added | define bounded environment posture |
| `api` | `transports/subprocess-stdio-compat/security-limitations.v1.md` | added | prevent subprocess from becoming server replacement or boundary bypass |
| `api` | `transports/subprocess-stdio-compat/deprecation-policy.v1.md` | added | define compat-only and migration posture |
| `api` | `transports/subprocess-stdio-compat/errors.v1.md` | added | freeze subprocess-specific error categories |
| `api` | `transports/subprocess-stdio-compat/conformance-profile.v1.md` | added | define minimum compat contract claims |
| `api` | `docs/in-process-subprocess-compat-boundary.md` | added | summarize the split between in-process, subprocess compat, and canonical transports |
| `api` | `docs/waves/api-08-in-process-test-subprocess-stdio-compatibility-boundary.md` | added | record scope and validation |
| `api` | `conformance/check_test_compat_transport_boundary.py` | added | validate API.08 non-product and compat-only wording |
| `api` | `conformance/README.md` | modified | register the API.08 checker |
| `api` | `transports/README.md` | modified | cross-link the API.08 subtrees |
| `api` | `mappings/transport-selection-policy.v1.md` | modified | keep test/compat transport selection explicit and non-canonical |
| `api` | `mappings/operation-dispatch-contract.v1.md` | modified | state that test/compat entrypoints still normalize envelopes and respect guards |
| `api` | `projections/README.md` | modified | prevent test/compat surfaces from claiming projection ownership |
| `yai` | `runtime/boundary/transport/README.md` | modified | keep in-process and subprocess surfaces out of runtime production transport ownership |
| `yai` | `runtime/boundary/api/README.md` | modified | make test/compat normalization and guard preservation explicit |
| `yai` | `tests/harness/yai/README.md` | added | classify harness semantics as non-product transport semantics |
| `sdk` | `generated/README.md` | modified | keep generated test/compat outputs non-canonical |
| `sdk` | `packages/rust/README.md` | modified | keep subprocess compat out of canonical Rust transport evolution |
| `sdk` | `packages/typescript/README.md` | modified | keep subprocess compat out of canonical TypeScript transport evolution |

## In-process Test Result

Record:
- test-only
- non-product
- explicit harness context
- no production runtime attachment
- no provider credential access
- no guard bypass
- no account/license/machine bypass
- no persistent user state mutation unless fixture or harness ownership is explicit
- no behavior implementation

## Subprocess Stdio Compat Result

Record:
- compat-only
- not canonical
- structured stdout required if used
- stderr diagnostics only
- exit status separated from operation result
- environment variables explicit and bounded
- process lifecycle errors remain transport errors
- operation errors remain response-envelope errors
- no behavior implementation

## Boundary Split Result

| Boundary | Role | Default posture | Notes |
| -------- | ---- | --------------- | ----- |
| Local IPC RPC | native-local product transport | primary native | CLI/Loom target |
| Local HTTP Loopback | browser/dashboard product transport | primary browser/dev | request-response |
| Local Event Stream | realtime product transport | primary realtime | not response envelope |
| In-process Test | harness and conformance transport | test-only | non-product |
| Subprocess Stdio Compat | migration/debug process transport | compat-only | not canonical |
| Provider Transport | runtime -> provider/model | separate | not client-runtime |

## Runtime/SDK Ownership Result

Record:
- API owns the test and compat contracts
- runtime may implement harness adapters later but does not gain a product
  transport here
- SDK may implement harness or compat clients later in explicit test or debug
  scope only
- CLI/Loom remain consumers and unchanged

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| `api` | `find transports/in-process-test* transports/subprocess-stdio-compat* transports mappings conformance docs projections -maxdepth 4 -type f | sort` | pass | confirmed API.08 subtree files, checker, and wave report exist |
| `api` | `rg -n "in_process_test\|subprocess_stdio_compat\|subprocess\|stdio\|stdout\|stderr\|in-process\|harness\|conformance\|compat\|debug\|migration\|YAI_API_ENDPOINT\|Local IPC RPC\|Local HTTP Loopback\|Local Event Stream" README.md transports mappings conformance docs projections 2>/dev/null \|\| true` | pass | audit confirmed test/compat vocabulary and prior transport context |
| `yai` | `find runtime/boundary tests/harness tools/runtime -maxdepth 3 -type f | sort` | pass | confirmed runtime boundary surfaces and real harness path |
| `yai` | `rg -n "in_process_test\|subprocess_stdio_compat\|subprocess\|stdio\|stdout\|stderr\|harness\|conformance\|compat\|debug\|Local IPC RPC\|Local HTTP Loopback\|Local Event Stream" runtime/boundary tests/harness tools/runtime README.md 2>/dev/null \|\| true` | pass | audit confirmed harness and boundary wording alignment points |
| `sdk` | `rg -n "in_process_test\|subprocess_stdio_compat\|subprocess\|stdio\|stdout\|stderr\|harness\|conformance\|compat\|debug\|Local IPC RPC\|Local HTTP Loopback\|Local Event Stream\|HttpTransport\|YAI_API_ENDPOINT" README.md generated packages/rust packages/typescript conformance 2>/dev/null \|\| true` | pass | audit confirmed SDK transport wording and migration-era HTTP reality |
| `cli` | `test ! -e source` | pass | required source-absence guard |
| `cli` | `scripts/check-no-source-dependency.sh` | pass | required |
| `cli` | `rg -n "in_process_test\|subprocess_stdio_compat\|subprocess\|stdio\|stdout\|stderr\|compat\|debug\|migration\|HttpTransport\|YAI_API_ENDPOINT\|transport\|runtime" README.md src tests docs 2>/dev/null \|\| true` | pass | current CLI wording did not require API.08 edits |
| `loom` | `rg -n "in_process_test\|subprocess_stdio_compat\|subprocess\|stdio\|stdout\|stderr\|compat\|debug\|migration\|HttpTransport\|YAI_API_ENDPOINT\|transport\|runtime\|backend" README.md src tests docs 2>/dev/null \|\| true` | pass | current Loom wording did not require API.08 edits |
| `api` | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| `api` | `python3 conformance/check_operation_registry.py` | pass | `conformance: ok` |
| `api` | `python3 conformance/check_operation_transport_mapping.py` | pass | `operation-transport-map: ok` |
| `api` | `python3 conformance/check_api_envelope_error_stream.py` | pass | `api-envelope-error-stream: ok` |
| `api` | `python3 conformance/check_local_ipc_rpc_contract.py` | pass | `local-ipc-rpc-contract: ok` |
| `api` | `python3 conformance/check_local_http_loopback_contract.py` | pass | `local-http-loopback-contract: ok` |
| `api` | `python3 conformance/check_local_event_stream_contract.py` | pass | `local-event-stream-contract: ok` |
| `api` | `python3 conformance/check_lan_remote_boundary.py` | pass | `lan-remote-boundary: ok` |
| `api` | `python3 conformance/check_test_compat_transport_boundary.py` | pass | `test-compat-transport-boundary: ok` |
| `api` | `git diff --check` | pass | required |
| `yai` | `git diff --check` | pass | required |
| `sdk` | `git diff --check` | pass | docs-only touches |
| `cli` | `git diff --check` | pass | untouched |
| `loom` | `git diff --check` | pass | untouched |
| `all` | `rg -n "in-process bridge implemented\|subprocess runner implemented\|stdout parser implemented\|subprocess is canonical\|in_process_test is product transport\|SDK implements subprocess_stdio_compat\|SDK implements in_process_test\|CLI defaults to subprocess\|Loom defaults to subprocess\|API implements subprocess transport\|runtime implements subprocess transport" ../api ../yai ../sdk ../cli ../loom 2>/dev/null \|\| true` | pass/classified | any matches are expected only in checker forbidden-phrase lists or wave-report command text; no positive implementation or unsafe boundary claims found |

## Non-Implementation Confirmation

Record:
- no in-process runtime bridge
- no test transport implementation
- no subprocess runner
- no stdout parser implementation
- no SDK transport implementation
- no CLI/Loom behavior change
- no runtime behavior change
- no provider/model behavior change
