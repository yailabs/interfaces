# SDK Architecture

The SDK is a contract-bound typed client layer over the API. It packages stable client behavior for Rust, TypeScript, Python, and C consumers.

## Architecture Commitments

- Use API operation and envelope contracts as upstream protocol input.
- Expose typed package APIs with honest unavailable or deferred behavior when transport or runtime support is absent.
- Keep package code free of direct runtime implementation ownership.
- Keep terminal UX and command wording outside SDK authority.
- Preserve compatibility aliases only when they protect consumers and remain clearly non-canonical.

## Absorbed Legacy Model

DOCS.3 absorbed the SDK alignment model, public runtime surface notes, API discipline notes, and surface contract material into this canonical architecture. Historical originals are preserved under `archive/legacy-sdk/`.
