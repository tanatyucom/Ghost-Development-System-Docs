# Extension And Versioning Policy

## Extension Policy

Specialized evidence contracts must:

1. keep all parent required fields;
2. add domain-specific fields in a named specialization section;
3. map domain result values to the common action meaning;
4. declare producer and consumer;
5. preserve Human Approval and SCW behavior;
6. document compatibility with current templates, reports, and completion flow.

## Specialization Examples

```text
Platform Execution Evidence Contract
  -> Startup Enforcement Evidence Specialization
  -> Repository Quality Gate Evidence Specialization
  -> Command Center Decision Evidence Specialization
  -> Completion Review Evidence Specialization
  -> Knowledge Promotion Evidence Specialization
```

## Versioning Policy

| Change | Version Impact |
| --- | --- |
| Add optional field | Minor revision |
| Add required parent field | Major revision |
| Rename required field | Breaking revision |
| Change lifecycle meaning | Major revision |
| Add specialization field | Specialization revision |
| Change result mapping | Major revision |

## Compatibility Rules

- Historical artifacts are not mass-migrated.
- Human-readable Markdown sections remain valid.
- JSON / YAML serialization is future work.
- Specializations cannot weaken parent Human Approval, SCW, or mutation rules.
- Evidence completeness is not approval.
