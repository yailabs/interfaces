# Conformance Checklist (Scaffold)

- [ ] envelope fields present (`schema,status,reason,message,refs,warnings,errors`)
- [ ] status vocabulary constrained
- [ ] unavailable/pending represented honestly
- [ ] session-as-user not canonicalized
- [ ] CLI-only phrasing excluded from canonical API contract
- [ ] no raw core struct leakage in exported contracts
- [ ] no fake provider/model/agent success claims
- [ ] schema names versioned
