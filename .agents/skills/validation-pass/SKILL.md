---
name: validation-pass
description: Run the narrowest truthful validation for the changed surface and report exact results.
---

Procedure:
1. Run `.agents/validation/commands.md`.
2. Run `git diff --check`.
3. Run drift checks and vendor-folder regression checks.
4. Run fake path/module/command scans where possible.
