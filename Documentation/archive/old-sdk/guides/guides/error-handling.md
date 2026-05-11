# Error Handling

SDK packages should expose API errors and transport failures as typed package outcomes.

## Status Vocabulary

- `ok`
- `partial`
- `pending`
- `ready`
- `unavailable`
- `blocked`
- `denied`
- `error`

## Handling Rules

- Preserve API error codes and response envelope status.
- Distinguish transport not configured from runtime unavailable.
- Do not convert unavailable or denied status into success.
- Package-specific exceptions or result types must map back to API status and error semantics.
