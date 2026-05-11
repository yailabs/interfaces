# In-process Test Errors v1

## Purpose

Freeze harness-specific error posture for `in_process_test`.

## Required Error Categories

- `harness_not_configured`
- `fixture_invalid`
- `operation_not_supported_in_harness`
- `guard_required_even_in_harness`
- `test_transport_misuse`
- `deterministic_replay_failed`

## Rules

- harness setup failure remains distinct from operation failure
- guard failure remains a guard or operation boundary, not silent harness
  success
