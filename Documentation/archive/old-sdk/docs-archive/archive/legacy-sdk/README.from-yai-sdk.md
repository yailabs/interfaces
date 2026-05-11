# yai-sdk

`yai-sdk` is the SDK/client bridge surface over canonical `yai-api` contracts.

It consumes canonical contracts from `../api`.

It does not own or implement:
- YAI runtime execution
- API contract ownership
- YAI client products
- account/billing/OAuth/organization backend
- governance/control truth
- agent/provider/model execution

Wave 14 posture:
- TypeScript and Python packages are initial contract-bound SDK surfaces.
- OpenAPI in `../api` remains scaffolded; this SDK is scaffolded/partial and reported honestly.

## SDK Authority (Wave 14B)

- `yai-sdk` is the official client consumption layer.
- Clients should consume YAI through SDK surfaces, not by directly depending on runtime adapters.
- Direct API/runtime-adapter use is limited to debug, conformance, and temporary bootstrap.
- Native clients (including CLI) require a native/C SDK bridge (`packages/c`).
