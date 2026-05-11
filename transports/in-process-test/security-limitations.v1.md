# In-process Test Security Limitations v1

## Purpose

Freeze the minimum safety posture for `in_process_test`.

## Rules

- no production runtime attachment
- no provider credential access
- no account, license, or machine bypass
- no runtime guard bypass
- no persistent user state mutation unless the fixture or harness explicitly
  owns it
