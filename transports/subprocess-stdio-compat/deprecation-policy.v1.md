# Subprocess Stdio Compat Deprecation Policy v1

## Purpose

Define deprecation posture for `subprocess_stdio_compat`.

## Rules

- `subprocess_stdio_compat` is compatibility-only
- it is not canonical for new SDK transports
- migration-era consumers should move toward Local IPC RPC, Local HTTP
  Loopback, or Local Event Stream as appropriate
