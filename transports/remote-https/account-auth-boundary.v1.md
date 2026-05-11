# Remote HTTPS Account and Auth Boundary v1

## Purpose

Define account and `auth_context` posture for `remote_https`.

## Rules

- account login support may use `remote_https`
- `auth_context` refresh may use `remote_https`
- account-required and expired-auth conditions remain remote boundary errors,
  not local runtime transport errors
- account/auth flows must not be confused with session or local runtime health

## Boundary

- API.07 adds no account or auth implementation
