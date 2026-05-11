# Remote HTTPS Machine and License Boundary v1

## Purpose

Define machine authorization and license lease posture for `remote_https`.

## Rules

- machine authorization may use `remote_https`
- license lease refresh may use `remote_https`
- machine or license failures remain remote boundary failures and do not
  redefine local runtime execution as remote
- pricing or billing objects must not leak into runtime core

## Boundary

- API.07 adds no machine authorization or license implementation
