# Interface Checks

`tools/checks/` contains lightweight INTF.6 guardrails for the unified
interfaces repository.

Checks:

- `check-generated-output-exclusion.sh`: fails when excluded generated/build
  output directories exist under package roots.
- `check-package-protocol-drift.sh`: verifies required root artifacts exist and
  prints conservative manual-review warnings for risky package/protocol drift
  vocabulary.

These checks do not replace language package builds, tests, or full conformance
profiles.
