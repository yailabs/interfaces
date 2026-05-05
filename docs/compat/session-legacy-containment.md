# Session Legacy Containment

## Status

* Delivery: V2
* Status: active containment policy
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Previous delivery: V1 - Session Death Decision
* Next delivery: V3 - Auth Command Model

## Policy

`session` is a legacy compatibility surface.

It is not the canonical YAI domain model.

Session is a legacy compatibility surface.
It is not the canonical YAI domain model.

Use:
  yai auth ...
  yai case ...
  yai shell ... / yai client ...

Session must not be used to model login, account, active case, work ownership,
permissions or the root harness.

## Canonical Replacement Model

```text
auth login
  -> principal/account context
  -> root case case://user
  -> nested cases
  -> governed work
```

## Allowed Session Use

| Use | Allowed | Constraint |
| --- | ------- | ---------- |
| compatibility bridge | yes | temporary only |
| migration bridge | yes | must map to auth/case/operator/client planes |
| debug/dev shim | yes | must not be public canonical model |
| historical reference | yes | must be clearly marked legacy |
| canonical user/account model | no | use auth/principal/account_ref |
| canonical work boundary | no | use case |
| canonical active case owner | no | use operator context |
| canonical shell/client lifecycle owner | no | use shell/client |

## User-Facing Wording Rule

Any new user-facing `session` text must say:

```text
legacy compatibility
not canonical
prefer auth/case/shell/client
```

## Forbidden New Language

Do not introduce new language that says or implies:

* session is the primary domain model;
* session owns login;
* session owns account identity;
* session owns active case;
* session owns work;
* session owns permissions;
* session owns the root harness;
* session attach is the canonical onboarding flow.

## Replacement Vocabulary

| Old wording | Replacement |
| ----------- | ----------- |
| user session | authenticated principal / operator context |
| session attach | shell/client attach or auth login, depending on context |
| session status | auth/case/runtime/client status, depending on context |
| active session | active case ref / operator context |
| session workspace | case |
| session harness | `case://user` |
| session permissions | authorization/governance |

## Future Work

| Future wave | Purpose |
| ----------- | ------- |
| V3 | Auth Command Model |
| V4 | Local Dev Auth |
| V9 | Case Commands |
| V10 | Active Case Refactor |
| V13 | Shell UX Model |
| V34 | API Registry Refactor |
| V40 | CLI Deprecation UX |
| V41 | Migration Shim |
| V42 | Remove Session Runtime Ownership |
| V43 | Remove Session Docs |
| V44 | Remove Session API Canon |
