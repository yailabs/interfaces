# Error Model

Canonical error object shape:
- `code`
- `message`
- `details` (optional structured fields)
- `retryable` (optional bool)

Canonical warning object shape:
- `code`
- `message`
- `details` (optional)

`refs` values in envelopes should identify command/surface/family/runtime context when applicable.
