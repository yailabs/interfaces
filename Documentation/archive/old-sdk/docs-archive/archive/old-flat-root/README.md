# SDK Docs

## Buckets
- `architecture/`: canonical SDK architecture and source dependency model
- `guides/`: operator/developer usage guides
- `standards/`: compatibility/versioning/quality standards
- `reports/`: inventory and DX checks
- `legacy/`: historical/transitional material

## Package Docs
- `../packages/typescript/README.md`
- `../packages/python/README.md`
- `../packages/c/README.md`
- `../packages/rust/README.md`

## Source of Truth
- API contracts and operation registry: `../api`
- SDK implementations: `../sdk/packages/*`
- runtime implementation: `../yai`
- client consumers: `../design`, `../console`
- legacy client name/path: `../loom`

Boundary note:
- SDK is the official client consumption layer.
- direct runtime adapter usage is debug/conformance/bootstrap only.
