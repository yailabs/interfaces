# Conformance

Run:
- `python3 conformance/check_operation_registry.py`
- `python3 conformance/check_api_contracts.py`
- `python3 conformance/check_logout_seal_policy.py`
- `python3 conformance/check_case_evidence_binding.py`

Coverage:
- registry grammar integrity
- schema reference integrity
- OpenAPI parse + operationId/family-tag consistency
- forbidden lifecycle/policy/supervisor checks
- API mirror alignment with canonical protocol artifacts in `../yai/protocols`

Boundary:
- `check_api_contracts.py` and `check_operation_registry.py` are API-owned checks.
- `check_logout_seal_policy.py` and `check_case_evidence_binding.py` are API-side
  mirror checks that consume canonical protocol artifacts from `yai/protocols`.
