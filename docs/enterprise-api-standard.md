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

Wave 22D8 boundary:
- API may expose account/auth/entitlement references and posture states;
- API does not define account database, billing endpoints, subscription flows, or login provider behavior.

Status honesty:
- `openApiStatus` and `conformanceStatus` are scaffolded until fully implemented and automated.


Client neutrality:
- API contracts are client-neutral.
- API does not own client UI/product behavior.
- API does not own SDK convenience behavior.
- clients should not bypass SDK except debug/conformance/bootstrap.
