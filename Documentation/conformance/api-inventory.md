# API Inventory

The SDK API inventory tracks package surfaces against API operations and protocol artifacts.

## Inventory Inputs

- `registry/api-operations.v1.json`
- `registry/api-operation-projections.v1.json`
- `mappings/operation-transport-map.v1.json`
- package source and generated surfaces under `packages/`

## Current Lessons Absorbed

DOCS.3 absorbed the API inventory and refoundation reports into this conformance surface. The main rule is that SDK package constants and typed surfaces must present API-aligned canonical names, while retained aliases remain compatibility-only.
