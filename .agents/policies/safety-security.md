# Safety And Security

- Do not add secrets, tokens, private keys, or environment values.
- Do not capture provider credentials or local machine secrets.
- Do not commit unsafe command transcripts as if they were product state.
- Do not claim validation, release, or runtime success unless a real command proved it.
- If sensitive material is encountered, stop and report it instead of copying it into `.agents`.
