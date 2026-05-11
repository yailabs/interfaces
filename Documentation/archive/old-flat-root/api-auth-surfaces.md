# API Auth Surfaces

## Status

* Delivery: V53
* Branch: `refoundation/phase-01`
* API family: `auth`
* Previous: V52 API Case Expansion

## Purpose

V53 expands and normalizes the canonical API `auth` surface so it matches the
command system, current CLI auth reality, future account/provider integration,
and the no-session doctrine already enforced across the YAI command system.

## Non-goals

* no provider auth implementation
* no browser/device login implementation
* no auth_context issuance
* no token signing or validation
* no CLI implementation
* no SDK generation
* no runtime behavior
* no API endpoint implementation

## Canonical Auth Operations

| Operation | action_id | CLI projection | Meaning | Owns session? | Owns entitlement/license/machine? |
| --------- | --------- | -------------- | ------- | ------------- | --------------------------------- |
| `auth.login` | `auth.login` | `yai auth login` | request canonical auth login posture | no | no |
| `auth.login.local_dev` | `auth.login.local_dev` | `yai auth login --local-dev` | local-development compatibility bootstrap | no | no |
| `auth.status` | `auth.status` | `yai auth status` | inspect auth posture | no | no |
| `auth.logout` | `auth.logout` | `yai auth logout` | clear auth posture | no | no |
| `auth.context.inspect` | `auth.context.inspect` | future `yai auth context inspect` | inspect safe auth-context projection | no | no |
| `auth.provider.status` | `auth.provider.status` | future `yai auth provider status` | inspect provider-auth adapter posture safely | no | no |
| `auth.device_login.start` | `auth.device_login.start` | future `yai auth device-login start` | begin future device-login contract | no | no |
| `auth.device_login.status` | `auth.device_login.status` | future `yai auth device-login status` | inspect future device-login attempt posture | no | no |
| `auth.device_login.cancel` | `auth.device_login.cancel` | future `yai auth device-login cancel` | cancel future device-login attempt posture | no | no |

## No-Session Boundary

```text
auth is canonical.
session is not auth.
provider session is not YAI session.
client attach is not auth.
shell attach is not auth.
```

V53 keeps `auth` as its own API family and leaves `session` explicitly
legacy/deprecated. The canonical auth surface is about auth posture and safe
auth-context projection only.

`auth.whoami` remains deprecated compatibility naming. V53 maps it to
`auth.context.inspect` instead of letting older wording keep semantic ownership.

## Auth / Entitlement / Machine / License Boundary

```text
auth login does not imply entitlement.
auth login does not imply machine authorization.
auth login does not imply license lease.
auth login does not imply runtime allowed.
auth login does not imply active case.
auth_context is separate from provider posture, license_lease, and machine authorization.
```

The V53 API contract only produces or inspects auth posture. It does not own:

* entitlement
* machine authorization
* license lease
* runtime gate decisions
* case selection
* operator context
* client attachment

Those boundaries remain future work for V54-V57.

## Logout Boundary

```text
logout does not stop runtime.
logout does not delete cases.
logout does not delete evidence.
logout does not delete knowledge.
logout does not delete records.
logout does not automatically revoke machine authorization or license lease unless a later explicit policy says so.
```

The V53 logout fixture and conformance checks make this explicit. Logout clears
auth posture only.

## Registry Changes

V53 changes these registry surfaces:

* `registry/api-operations.v1.json`
* `registry/api-operation-projections.v1.json`
* `registry/api-families.v1.json`
* `registry/api-surfaces.v1.json`
* `registry/yai-actions.v1.json`

Added or normalized operation ids:

* `auth.login`
* `auth.login.local_dev`
* `auth.status`
* `auth.logout`
* `auth.context.inspect`
* `auth.provider.status`
* `auth.device_login.start`
* `auth.device_login.status`
* `auth.device_login.cancel`

Compatibility decision:

* `auth.whoami` remains deprecated and maps to `auth.context.inspect`

## Schema / Fixtures / Conformance

V53 adds:

* `schemas/auth-operation.v1.schema.json`
* `fixtures/auth-operation/*.json`
* `conformance/check_auth_operations.py`

The schema centers on:

* `operation_id`
* `action_id`
* `request_kind`
* `operation_status`
* `auth_posture`
* `provider_posture`
* `auth_context_posture`
* `safe_projection`

The fixture set covers:

* unavailable production login posture
* local-dev login posture
* unauthenticated status
* local-dev status
* logout clearing auth only
* safe auth-context inspection
* provider-auth not configured posture
* future device-login contract start

Conformance enforces:

* required auth operation ids exist
* auth operations stay in the `auth` family
* `auth.whoami` is deprecated compatibility only
* auth operations do not emit records or rely on session ownership
* fixtures remain safe and token-free

## SDK / CLI / Loom Handoff

V53 does not add behavior.

It prepares:

* SDK clients to map onto canonical `auth.*` operations later
* CLI auth commands to keep projecting from `action_id` without reviving session
* Loom/TUI auth panels and palette entries to show available, unavailable, or planned auth actions from the same canonical action model

Current CLI reality remains valid:

* `yai auth login`
* `yai auth login --local-dev`
* `yai auth status`
* `yai auth logout`

V53 only formalizes the API contract layer beneath that surface.

## V54 Handoff

V54 follows with API operator-context surfaces so the active-case boundary can
be formalized separately from both session and auth.
