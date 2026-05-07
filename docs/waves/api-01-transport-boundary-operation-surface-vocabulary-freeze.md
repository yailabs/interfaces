# API.01 — Transport Boundary / Operation Surface Vocabulary Freeze

## Status

* Delivery: API.01
* Status: done
* Track: API / Transport / SDK / Runtime alignment
* Repo branch: `refoundation/phase-01`
* Repo change type: documentation-only transport boundary definition
* Previous delivery: V28.6 — Protocol Cutover Closure / Specs Rename & API Projection Reshape
* Next delivery: API.02 — Operation-to-Transport Mapping / Dispatch Contract

## Purpose

API.01 freezes transport vocabulary and ownership before implementation.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `transports/README.md` | update | freeze transport vocabulary root |
| api | `transports/local-ipc-rpc.v1.md` | create | define primary local native transport |
| api | `transports/local-http-loopback.v1.md` | create | define browser/dashboard local HTTP transport |
| api | `transports/local-event-stream.v1.md` | create | define realtime stream transport |
| api | `transports/lan-secure.v1.md` | create | define controlled LAN transport |
| api | `transports/remote-https.v1.md` | create | define platform/future remote boundary |
| api | `transports/provider-transport-boundary.v1.md` | create | separate runtime-provider transport |
| api | `transports/in-process-test.v1.md` | create | mark harness-only transport |
| api | `transports/subprocess-stdio-compat.v1.md` | create | mark compat-only transport |
| api | `docs/transport-boundary-model.md` | create | define transport boundary model and ownership matrix |
| api | `docs/waves/api-01-transport-boundary-operation-surface-vocabulary-freeze.md` | create | record delivery |
| api | `README.md` | update | cross-link API transport ownership |
| api | `mappings/README.md` | update | clarify mapping vs transport ownership |
| api | `projections/README.md` | update | clarify SDK/client projection relation |
| yai | `runtime/boundary/README.md` | update | align runtime boundary ownership |
| yai | `runtime/boundary/transport/README.md` | update | align runtime transport boundary ownership |
| yai | `runtime/boundary/service/README.md` | update | define loopback/local service exposure boundary |
| yai | `runtime/connections/README.md` | create | define connection/session observation boundary |
| yai | `include/ipc/README.md` | create | define IPC ABI/header ownership |
| yai | `providers/transport/README.md` | create | define runtime-provider transport boundary |
| sdk | `README.md` | update | clarify SDK client-side transport ownership |
| sdk | `generated/README.md` | update | mark generated outputs as projections, not transport truth |
| sdk | `packages/rust/README.md` | update | clarify current HTTP vs frozen native transport target |
| sdk | `packages/typescript/README.md` | update | clarify browser/loopback transport ownership |

## Transport Classes

| Transport | Status | Primary users | Binding | Notes |
| --------- | ------ | ------------- | ------- | ----- |
| Local IPC RPC | primary now | CLI, Loom/TUI, native clients | Unix socket / named pipe | default for local Rust clients |
| Local HTTP Loopback | primary now | dashboard/web/dev | localhost HTTP | browser-friendly |
| Local Event Stream | primary now | dashboard/TUI/CLI live views | SSE / RPC stream / future WebSocket | realtime |
| LAN Secure | controlled | multi-machine local setups | paired secure network transport | disabled by default |
| Remote HTTPS | future/platform | account/license/machine/update/future hosted | HTTPS | not default runtime execution |
| Provider Transport | separate boundary | runtime -> provider/model | provider-specific | not client-runtime API |
| In-process Test | test only | conformance/dev | direct in-process | not product |
| Subprocess/Stdio Compat | compat only | migration/debug | binary stdout/stderr | not canonical |

## Ownership Matrix

| Area | Owns | Does not own |
| ---- | ---- | ------------ |
| `api/transports` | transport contracts | server/client implementation |
| `yai/runtime/boundary/transport` | runtime-side transport boundary | API source-of-truth |
| `yai/runtime/boundary/service` | local service exposure/lifecycle boundary | SDK client behavior |
| `yai/runtime/boundary/api` | operation dispatch into runtime | physical socket/listener policy |
| `yai/runtime/connections` | client connection/session observation | provider/model transport |
| `yai/include/ipc` | C/ABI IPC contract headers | API projection docs |
| `yai/providers/transport` | runtime -> provider/model transport | client -> runtime API transport |
| `sdk/packages/*/src/transports` | SDK client transports | runtime server implementation |
| `cli` | CLI commands over SDK | custom transport grammar |
| `loom` | TUI over SDK | custom transport grammar |

## Security Baseline

- Local IPC RPC: socket/pipe permissions required, same-user local access by
  default, version handshake required, no remote exposure.
- Local HTTP Loopback: bind to loopback only by default, strict origin/CORS,
  local client token or equivalent required before sensitive operations, no LAN
  exposure by default.
- Local Event Stream: heartbeat required, terminal event/error semantics
  required, reconnect semantics documented, sensitive payloads must be
  projection-safe.
- LAN Secure: disabled by default, explicit pairing, TLS/token/certificate
  posture, revocation, device allowlist, no automatic `0.0.0.0` bind.
- Remote HTTPS: platform-owned remote boundary, no raw provider identity
  leakage into runtime core, no pricing/billing object leakage into runtime
  core, local-first runtime remains baseline.
- Subprocess/Stdio: compat only, not canonical, should not be used for new SDK
  transports.

## Non-Implementation Confirmation

Record:
no server implemented.
no SDK transport implemented.
no CLI/Loom behavior changed.
no provider/model behavior changed.
no OpenAPI expansion.
no auth/license/machine behavior added.

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `git diff --check` | pass | required |
| api | `test -f transports/README.md && test -f transports/local-ipc-rpc.v1.md && test -f transports/local-http-loopback.v1.md && test -f transports/local-event-stream.v1.md && test -f transports/lan-secure.v1.md && test -f transports/remote-https.v1.md && test -f transports/provider-transport-boundary.v1.md && test -f transports/in-process-test.v1.md && test -f transports/subprocess-stdio-compat.v1.md && test -f docs/transport-boundary-model.md && test -f docs/waves/api-01-transport-boundary-operation-surface-vocabulary-freeze.md` | pass | required existence checks |
| api | `rg -n "API implements transport\|API owns runtime transport implementation\|SDK owns runtime server\|CLI defines transport grammar\|Loom defines transport grammar\|provider transport is client runtime transport\|LAN enabled by default\|0.0.0.0 by default\|subprocess is canonical" ../api ../yai ../sdk ../cli ../loom 2>/dev/null \|\| true` | pass | no matches |
| yai | `git diff --check` | pass | touched |
| yai | `test -f runtime/boundary/README.md && test -f runtime/boundary/transport/README.md && test -f runtime/boundary/service/README.md && test -f runtime/connections/README.md && test -f include/ipc/README.md && test -f providers/transport/README.md` | pass | required existence checks |
| cli | `test ! -e source` | pass | required |
| cli | `scripts/check-no-source-dependency.sh` | pass | required |
| cli | `git diff --check` | pass | repo untouched |
| sdk | `git diff --check` | pass | touched |
| loom | `git diff --check` | pass | repo untouched |
