# Enterprise API Standard (Wave 14C3)

API repository role:
- Canonical contract source.
- Not runtime implementation.
- Not CLI behavior owner.
- Not client UI/product state owner.
- Not SDK convenience semantics owner.

API owns:
- schemas
- envelopes
- lifecycle vocabulary
- error model
- family contracts
- OpenAPI/conformance direction

API does not own:
- runtime execution
- runtime adapter implementation
- account/billing/OAuth/provider implementation
- raw core struct exposure
- local provider/model assumptions

Status honesty:
- `openApiStatus` and `conformanceStatus` are scaffolded until fully implemented and automated.


Client neutrality:
- API contracts are client-neutral.
- API does not own client UI/product behavior.
- API does not own SDK convenience behavior.
