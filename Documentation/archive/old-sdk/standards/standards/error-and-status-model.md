# Error And Status Model

SDK packages map API response, error, readiness, and transport status into language-specific types.

## Status Vocabulary

- `ok`
- `partial`
- `pending`
- `ready`
- `unavailable`
- `blocked`
- `denied`
- `error`

## Mapping Rule

Package-specific errors must preserve API status and error meaning. Transport failures may add package context, but must not invent API operation semantics.
