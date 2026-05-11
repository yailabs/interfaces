# Remote HTTPS Conformance Profile v1

## Purpose

Define the minimum contract claims that a future `remote_https`
implementation must satisfy.

## Required Contract Areas

- platform/account/update/future capability boundary posture
- not default local runtime execution
- not LAN runtime exposure
- not provider/model transport
- machine, license, release, and auth boundary posture
- distinct remote error categories
- no pricing or billing leakage into runtime core

## Out of Scope for API.07

- no Remote HTTPS client implementation
- no account/auth/license/machine behavior implementation
- no release or update client implementation
- no hosted compute implementation
