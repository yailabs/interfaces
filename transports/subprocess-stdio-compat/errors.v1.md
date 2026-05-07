# Subprocess Stdio Compat Errors v1

## Purpose

Freeze transport-specific error posture for `subprocess_stdio_compat`.

## Required Error Categories

- `executable_not_found`
- `process_spawn_failed`
- `process_timeout`
- `stdout_decode_failed`
- `invalid_stdout_envelope`
- `stderr_diagnostic`
- `exit_status_failure`
- `env_missing`
- `compat_transport_deprecated`

## Rules

- process lifecycle errors remain transport errors
- operation errors remain response-envelope errors
- stderr diagnostics do not redefine structured stdout success
