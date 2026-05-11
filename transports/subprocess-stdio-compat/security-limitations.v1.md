# Subprocess Stdio Compat Security Limitations v1

## Purpose

Freeze the minimum safety posture for `subprocess_stdio_compat`.

## Rules

- `subprocess_stdio_compat` is not a runtime server replacement
- `subprocess_stdio_compat` is not a provider/model transport shortcut
- no new SDK feature should prefer `subprocess_stdio_compat`
- compatibility invocation does not bypass runtime guards or operation mapping
