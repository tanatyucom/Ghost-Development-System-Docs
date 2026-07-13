# Documentation Synchronization Examples

## Good Example: New Rule

Changed files:

```text
docs/rules/example_rules.md
docs/workflow/example_workflow.md
examples/example_examples.md
```

Required synchronization:

- Add rule to `docs/rules/README.md`.
- Add workflow to `docs/workflow/README.md`.
- Add examples to `examples/README.md`.
- Add high-level entry to `docs/README.md` if it is a public standard.
- Regenerate and validate `docs/ai_repository_index.md`.
- Run Repository Quality Audit.
- Record Documentation Synchronization Review in Completion Report.

## Bad Example: Hidden Standard

Changed files:

```text
docs/architecture/new_platform_standard.md
```

Missing:

- no `docs/architecture/README.md` entry;
- no `docs/README.md` entry;
- AI Repository Index not regenerated;
- Completion Report says only "docs updated".

Why this is bad:

- Human readers cannot discover the standard.
- AI agents may not find the new source of truth.
- Future Qs may recreate the same idea.

## Good Example: Not Required Reason

Changed file:

```text
reports/internal_review_notes.md
```

Completion Report:

```text
Documentation Synchronization required: No
Reason: report is task-local and already reachable through the request workspace.
AI Repository Index regenerated: No
Repository Quality Audit executed: Yes
```

Why this is good:

- The omission is intentional and reviewable.
- Repository Quality still confirms no broken links or missing README structure.

## Bad Example: AI Index Drift

Changed files:

```text
docs/rules/new_gate_rules.md
docs/workflow/new_gate_workflow.md
```

Problem:

```text
README entries were updated, but docs/ai_repository_index.md was not regenerated.
```

Why this is bad:

- Public AI access sees stale knowledge.
- Raw URL entry points are incomplete.

