# Q Creation Intent Classification Decision

## Decision

Use three fail-closed classes:

1. Explicit bounded implementation intent: approval granted at Q creation.
2. Explicit draft/review/no-implementation intent: `DRAFT ONLY`.
3. Genuine ambiguity: clarification or `SCW_REQUIRED`.

Natural-language context determines intent; the repository validator checks the
resulting Q metadata for internal consistency and does not pretend to infer user
intent.
