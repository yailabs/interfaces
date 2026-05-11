# Package Taxonomy

SDK package families provide typed client behavior for different language consumers.

## Package Families

- `packages/rust`: native Rust clients, explicit client transports, typed operation surfaces, and native package validation.
- `packages/typescript`: TypeScript/browser/local-web consumers, generated or hand-written typed surfaces, local HTTP and event stream alignment.
- `packages/python`: Python integration and automation package surface.
- `packages/c`: native C compatibility package, local tooling, and transitional native integration.

## Taxonomy Rule

Package behavior may differ by language and runtime environment, but protocol identity still comes from API artifacts. Package taxonomy does not create new protocol families.
