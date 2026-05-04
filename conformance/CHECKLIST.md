# Conformance Checklist (Scaffold)

- [ ] envelope fields present (`schema,status,reason,message,refs,warnings,errors`)
- [ ] status vocabulary constrained
- [ ] unavailable/pending represented honestly
- [ ] session-as-user not canonicalized
- [ ] CLI-only phrasing excluded from canonical API contract
- [ ] no raw core struct leakage in exported contracts
- [ ] no fake provider/model/agent success claims
- [ ] prompting remains distinct from conversation lifecycle and message persistence
- [ ] prompting remains distinct from agents and does not imply provider/model execution
- [ ] schema names versioned
- [ ] registry canonical public plane keys do not include `flow`, root `records`, `orchestration`
- [ ] registry canonical surface keys do not include CLI aliases (`ai`, `runtime`, `govern`, `provider`, `agent`, `inspect`)
- [ ] operation IDs do not use forbidden root namespaces (`flow.*`, `records.*`, `orchestration.*`, `supervisor.*`, `policy.*`)
