# Remote HTTPS Errors v1

## Purpose

Freeze Remote HTTPS boundary error posture.

## Required Error Categories

- `platform_unavailable`
- `account_required`
- `auth_context_expired`
- `machine_authorization_required`
- `license_lease_expired`
- `release_metadata_unavailable`
- `remote_capability_not_enabled`
- `remote_operation_not_supported`
- `remote_timeout`
- `remote_policy_blocked`

## Rules

- remote boundary failures remain distinct from local runtime operation errors
- platform policy failure is not LAN failure
- remote timeout is not the same as local runtime unavailability
