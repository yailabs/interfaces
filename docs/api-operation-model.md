# API Operation Model

Wave 16B introduces operation IDs as client-facing contract seams.

Operation IDs are declared in `registry/api-operations.v1.json` and do not imply runtime execution.
Stability and implementation fields are authoritative for readiness.

Transport, endpoint, and execution remain outside this repository.

Wave 17 consumer note: Loom uses SDK typed plane clients mapped to this operation model.
