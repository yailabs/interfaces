# Conformance

Conformance checks protect protocol integrity, generated-surface provenance,
and SDK package alignment.

Primary check families:

- protocol registry integrity;
- schema, envelope, and error alignment;
- operation-to-transport mapping integrity;
- OpenAPI projection consistency;
- generated surface provenance;
- SDK package projection alignment.

Current package alignment profile:

- `conformance/profiles/interface-package-alignment.v1.md`

Current package validation report:

- `conformance/reports/intf-6-package-validation-status.md`

Run existing protocol checks directly from this directory, for example:

```sh
python3 conformance/check_operation_registry.py
python3 conformance/check_api_contracts.py
python3 conformance/check_operation_transport_mapping.py
python3 conformance/check_api_envelope_error_stream.py
```

Run INTF.6 lightweight guardrails:

```sh
./tools/checks/check-generated-output-exclusion.sh
./tools/checks/check-package-protocol-drift.sh
```

Guardrail scripts are deliberately conservative. They do not replace full
language package validation or release readiness.
