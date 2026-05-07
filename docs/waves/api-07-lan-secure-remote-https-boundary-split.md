# API.07 — LAN Secure / Remote HTTPS Boundary Split

## Status

* Delivery: API.07
* Status: done
* Track: API / Transport / SDK / Runtime alignment
* Repo branch: `refoundation/phase-01`
* Repo change type: LAN Secure + Remote HTTPS boundary split
* Previous delivery: API.06 — Local Event Stream Contract Verticalization
* Next delivery: API.08 — In-process Test / Subprocess Stdio Compatibility Boundary

## Purpose

API.07 separates LAN Secure from Remote HTTPS and prevents both from being
confused with Local HTTP Loopback, Provider Transport, or default runtime
execution.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| `api` | `transports/lan-secure.v1.md` | modified | expand the LAN Secure root contract and point to the verticalized subtree |
| `api` | `transports/lan-secure/README.md` | added | create the LAN Secure contract root |
| `api` | `transports/lan-secure/pairing.v1.md` | added | define mandatory pairing posture |
| `api` | `transports/lan-secure/discovery.v1.md` | added | define LAN discovery posture without implementation |
| `api` | `transports/lan-secure/endpoint-binding.v1.md` | added | prohibit automatic `0.0.0.0` and wildcard LAN exposure |
| `api` | `transports/lan-secure/security.v1.md` | added | define disabled-by-default secure LAN posture |
| `api` | `transports/lan-secure/device-allowlist.v1.md` | added | define required device allowlist posture |
| `api` | `transports/lan-secure/revocation.v1.md` | added | define required revocation posture |
| `api` | `transports/lan-secure/operation-exposure.v1.md` | added | define blocked-by-default LAN operation exposure posture |
| `api` | `transports/lan-secure/errors.v1.md` | added | freeze LAN-specific error categories and distinction from operation errors |
| `api` | `transports/lan-secure/conformance-profile.v1.md` | added | define minimum LAN Secure contract claims |
| `api` | `transports/remote-https.v1.md` | modified | expand the Remote HTTPS root contract and point to the verticalized subtree |
| `api` | `transports/remote-https/README.md` | added | create the Remote HTTPS contract root |
| `api` | `transports/remote-https/platform-boundary.v1.md` | added | define platform-owned remote boundary posture |
| `api` | `transports/remote-https/account-auth-boundary.v1.md` | added | define account and auth boundary posture |
| `api` | `transports/remote-https/machine-license-boundary.v1.md` | added | define machine authorization and license lease posture |
| `api` | `transports/remote-https/release-update-boundary.v1.md` | added | define release and update metadata posture |
| `api` | `transports/remote-https/future-hosted-capability-boundary.v1.md` | added | reserve future hosted capability without claiming implementation |
| `api` | `transports/remote-https/security.v1.md` | added | define platform boundary security posture |
| `api` | `transports/remote-https/errors.v1.md` | added | freeze Remote HTTPS error categories |
| `api` | `transports/remote-https/conformance-profile.v1.md` | added | define minimum Remote HTTPS contract claims |
| `api` | `docs/lan-secure-remote-https-boundary.md` | added | summarize the split between LAN Secure, Remote HTTPS, loopback, and provider transport |
| `api` | `docs/waves/api-07-lan-secure-remote-https-boundary-split.md` | added | record scope and validation |
| `api` | `conformance/check_lan_remote_boundary.py` | added | validate LAN and Remote HTTPS split wording and non-implementation posture |
| `api` | `conformance/README.md` | modified | register the API.07 conformance checker |
| `api` | `mappings/lan-exposure-policy.v1.md` | modified | cross-link LAN exposure policy to the LAN Secure contract subtree |
| `api` | `mappings/transport-selection-policy.v1.md` | modified | cross-link selection policy to LAN Secure and Remote HTTPS contract docs |
| `api` | `mappings/provider-transport-exclusion-policy.v1.md` | modified | state that provider HTTP APIs are not YAI Remote HTTPS |
| `api` | `transports/README.md` | modified | cross-link the LAN Secure and Remote HTTPS verticalized subtrees |
| `yai` | `runtime/boundary/service/README.md` | modified | keep loopback separate from LAN and exclude Remote HTTPS server behavior |
| `yai` | `runtime/boundary/transport/README.md` | modified | align future LAN and Remote HTTPS transport ownership without semantic overreach |
| `yai` | `runtime/boundary/api/README.md` | modified | state that LAN, loopback, and IPC origins do not bypass guards once normalized |
| `yai` | `runtime/connections/README.md` | modified | define stronger observation posture for LAN without making observation authorization |
| `yai` | `providers/transport/README.md` | modified | separate provider HTTP APIs from YAI Remote HTTPS |
| `sdk` | `generated/README.md` | modified | keep generated LAN/Remote artifacts as API contract projections only |
| `sdk` | `packages/rust/README.md` | modified | keep `lan_secure` and `remote_https` out of default CLI/Loom posture |
| `sdk` | `packages/typescript/README.md` | modified | keep browser-local loopback/event-stream separate from LAN and Remote HTTPS |

## LAN Secure Result

Record:
- disabled by default
- pairing required
- allowlist required
- revocation required
- no automatic `0.0.0.0`
- operation exposure policy required
- no behavior implementation

## Remote HTTPS Result

Record:
- platform/account/update/future capability boundary
- not default local runtime execution
- not provider/model transport
- no hosted compute implementation
- no behavior implementation

## Boundary Split Result

| Boundary | Role | Default posture | Notes |
| -------- | ---- | --------------- | ----- |
| Local IPC RPC | same-machine native local | primary native | CLI/Loom target |
| Local HTTP Loopback | same-machine browser/dev | primary browser/dev | not LAN |
| Local Event Stream | realtime projection | primary realtime | not response envelope |
| LAN Secure | paired local-network runtime access | disabled | opt-in only |
| Remote HTTPS | platform/account/update/future capability | controlled/future | not default runtime execution |
| Provider Transport | runtime -> provider/model | separate | not client-runtime |

## Runtime/SDK Ownership Result

Record:
- API owns contracts
- runtime may implement LAN listener later
- runtime or platform-facing clients may use Remote HTTPS later
- SDK may implement LAN or Remote HTTPS clients later
- CLI/Loom unchanged

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| `api` | `find transports/lan-secure* transports/remote-https* transports mappings conformance docs -maxdepth 4 -type f | sort` | pass | confirmed LAN Secure and Remote HTTPS subtrees plus checker and wave report exist |
| `api` | `rg -n "lan_secure\|LAN\|0.0.0.0\|pairing\|device allowlist\|revocation\|remote_https\|Remote HTTPS\|platform\|account\|auth_context\|machine authorization\|license lease\|release\|update\|hosted\|provider transport\|loopback\|local_http_loopback\|local_ipc_rpc\|local_event_stream" README.md transports mappings conformance docs 2>/dev/null \|\| true` | pass | audit confirmed split vocabulary and pre-existing transport references |
| `yai` | `rg -n "lan_secure\|LAN\|0.0.0.0\|pairing\|allowlist\|revocation\|remote_https\|Remote HTTPS\|platform\|account\|auth_context\|machine authorization\|license lease\|release\|update\|provider transport\|loopback\|runtime/boundary/service\|runtime/boundary/transport" runtime/boundary runtime/connections providers/transport include/ipc README.md 2>/dev/null \|\| true` | pass | audit confirmed runtime/provider wording alignment points |
| `sdk` | `rg -n "lan_secure\|LAN\|remote_https\|Remote HTTPS\|platform\|account\|auth_context\|machine\|license\|local_http_loopback\|local_ipc_rpc\|local_event_stream\|provider transport\|HttpTransport\|YAI_API_ENDPOINT" README.md generated packages/rust packages/typescript packages/python packages/c 2>/dev/null \|\| true` | pass | audit confirmed SDK transport wording and migration-era HTTP reality |
| `cli` | `test ! -e source` | pass | required source-absence guard |
| `cli` | `scripts/check-no-source-dependency.sh` | pass | required |
| `cli` | `rg -n "LAN\|lan_secure\|remote_https\|Remote HTTPS\|HttpTransport\|YAI_API_ENDPOINT\|transport\|runtime" README.md src tests 2>/dev/null \|\| true` | pass | current CLI remains behavior-unchanged |
| `loom` | `rg -n "LAN\|lan_secure\|remote_https\|Remote HTTPS\|HttpTransport\|YAI_API_ENDPOINT\|transport\|runtime\|backend" README.md src tests 2>/dev/null \|\| true` | pass | current Loom remains behavior-unchanged |
| `api` | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| `api` | `python3 conformance/check_operation_registry.py` | pass | `conformance: ok` |
| `api` | `python3 conformance/check_operation_transport_mapping.py` | pass | `operation-transport-map: ok` |
| `api` | `python3 conformance/check_api_envelope_error_stream.py` | pass | `api-envelope-error-stream: ok` |
| `api` | `python3 conformance/check_local_ipc_rpc_contract.py` | pass | `local-ipc-rpc-contract: ok` |
| `api` | `python3 conformance/check_local_http_loopback_contract.py` | pass | `local-http-loopback-contract: ok` |
| `api` | `python3 conformance/check_local_event_stream_contract.py` | pass | `local-event-stream-contract: ok` |
| `api` | `python3 conformance/check_lan_remote_boundary.py` | pass | `lan-remote-boundary: ok` |
| `api` | `git diff --check` | pass | required |
| `yai` | `git diff --check` | pass | required |
| `sdk` | `git diff --check` | pass | docs-only touches |
| `cli` | `git diff --check` | pass | untouched |
| `loom` | `git diff --check` | pass | untouched |
| `all` | `rg -n "LAN enabled by default\|0.0.0.0 by default\|pairing optional for LAN\|Remote HTTPS is default local runtime execution\|Remote HTTPS replaces local runtime\|hosted compute implemented\|provider transport is Remote HTTPS\|Local HTTP Loopback is LAN\|SDK implements lan_secure\|SDK implements remote_https\|runtime implements LAN listener\|runtime implements Remote HTTPS client\|API implements LAN server\|API implements Remote HTTPS" ../api ../yai ../sdk ../cli ../loom 2>/dev/null \|\| true` | pass/classified | any matches are expected only in checker forbidden-phrase lists or wave-report command text; no positive implementation or unsafe boundary claims found |

## Non-Implementation Confirmation

Record:
- no LAN listener
- no pairing implementation
- no Remote HTTPS client
- no account, auth, license, or machine behavior
- no SDK LAN or Remote transport
- no CLI/Loom behavior change
- no hosted compute behavior
- no provider/model behavior change
