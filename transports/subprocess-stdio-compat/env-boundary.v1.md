# Subprocess Stdio Compat Environment Boundary v1

## Purpose

Define environment-variable posture for `subprocess_stdio_compat`.

## Rules

- environment variables must be explicit and bounded
- subprocess invocation must not depend on unbounded ambient environment
- missing environment configuration remains a transport setup failure
