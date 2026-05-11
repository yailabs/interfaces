# Cross-Repo Boundary

- `external`: `../yai` owns runtime kernel behavior and implementation truth.
- `external`: `../sdk` owns typed clients and package ergonomics.
- `external`: `../console` owns operator and product UI behavior.
- `external`: `../catalog` owns catalog metadata and descriptors.

Observed local boundary:

- `observed`: this repo owns API projection surfaces, not runtime implementation.
