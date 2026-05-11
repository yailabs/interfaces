# Remote HTTPS v1

## Purpose

Define `remote_https` as the YAI platform/account remote boundary.

API.07 verticalizes this transport into a dedicated contract subtree so
runtime, SDK, and platform-facing clients can align on account, auth context,
machine authorization, license lease, release/update, and future hosted
capability posture later without turning Remote HTTPS into default local
runtime execution.

## Used For

- account/login support
- `auth_context` refresh
- machine authorization
- license lease
- release/update metadata
- future hosted capability

## Boundary Split

- `remote_https` is a platform/account/update/future capability boundary.
- `remote_https` is not default local runtime execution.
- `remote_https` is not LAN runtime exposure.
- `remote_https` is not `local_http_loopback`.
- `remote_https` is not provider/model transport.
- `remote_https` is not generic remote inference API by default.

## Not Used For

- pretending local runtime execution is remote by default
- replacing local-first runtime transport as the baseline

## Classification

- status: future/platform
- class: remote platform boundary

## Ownership

- API owns: remote contract
- Runtime owns: remote platform client when needed
- SDK owns: remote-capable client only where explicitly supported

## Security Baseline

- platform-owned remote boundary
- no raw provider identity leakage into runtime core
- no pricing/billing object leakage into runtime core
- local-first runtime remains baseline
- remote capability must be opt-in or capability-gated
- remote errors remain distinct from local runtime operation errors

## Contract Surfaces

- `remote-https/README.md`
- `remote-https/platform-boundary.v1.md`
- `remote-https/account-auth-boundary.v1.md`
- `remote-https/machine-license-boundary.v1.md`
- `remote-https/release-update-boundary.v1.md`
- `remote-https/future-hosted-capability-boundary.v1.md`
- `remote-https/security.v1.md`
- `remote-https/errors.v1.md`
- `remote-https/conformance-profile.v1.md`

## Non-goals

- not the default CLI/Loom transport
- not the provider/model transport boundary
- not a replacement for local-first runtime
- no hosted compute implementation is added by this document
- no remote platform call implementation is added by this document
