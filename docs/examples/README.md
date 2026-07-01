# Examples

## Purpose

This folder is the best practice library for Ghost Development System Docs.

Examples show how the rules and templates should look in real documentation
work. They are written for humans and AI so new Q files, reviews, completion
reports, and documentation requests can start from a clear reference.

## Contains

- `good_q.md`: example of a well-written Q file.
- `good_review.md`: example of a complete review report.
- `good_completion_report.md`: example completion report.
- `improvement_review.md`: example Improvement Review section.
- `purpose_oriented_naming.md`: before and after examples for
  purpose-oriented naming.
- `knowledge_before_automation.md`: good and bad examples for converting
  automation failures into reusable knowledge before adding complexity.
- `repository_information.md`: example of repository boundaries, source of
  truth, scope guard, and completion criteria.
- `authority_matrix.md`: example edit and reference authority matrix.
- `adr_example.md`: example Architecture Decision Record.

## Does NOT Contain

- Runtime code.
- Active Queue state.
- Approved project decisions.
- Templates to copy without review.
- Private repository information.

## Templates vs Examples

Templates live in:

```text
docs/templates/
```

Templates define reusable structure.

Examples live in:

```text
docs/examples/
```

Examples show realistic usage of that structure.

Use templates when creating a new document. Use examples when you need to see
what a complete, well-scoped document should feel like.

## When To Use Each Example

- Use `good_q.md` before writing a new Q file for Codex or another AI.
- Use `good_review.md` when reviewing documentation, roadmap, rules, templates,
  or architecture changes.
- Use `good_completion_report.md` when reporting finished documentation work.
- Use `improvement_review.md` when you need to separate near-term recommended
  improvements from future candidates.
- Use `purpose_oriented_naming.md` when renaming roadmap items or public
  knowledge base topics.
- Use `knowledge_before_automation.md` when an automation failure may be better
  solved by Review, Human Approval, Alias, Metadata, Rules, or Knowledge Base
  updates before adding more automation.
- Use `repository_information.md` when a task may involve multiple
  repositories, documentation roots, runtime roots, or reference-only sources.
- Use `authority_matrix.md` when a task needs explicit Editable, Reference
  Only, and Forbidden boundaries.
- Use `adr_example.md` when documenting a decision that should remain
  understandable over time.

## AI Usage Notes

AI should treat these files as examples, not as active instructions.

When examples conflict with rules or templates, follow:

1. `docs/rules/`
2. `docs/templates/`
3. `docs/examples/`

## Future Example Candidates

- Design Philosophy document example.
- Template Lifecycle example.
- Documentation Health Check example.
- Documentation Coverage Report example.
- Knowledge Base Index example.

## Update Policy

Update examples when templates or rules change enough that existing examples no
longer show the recommended pattern.

Do not use examples to introduce new rules. Promote reusable standards to
`docs/rules/` or `docs/templates/` first.

## Related Documents

- `docs/templates/`
- `docs/rules/`
- `docs/templates/review_checklist.md`
- `docs/templates/q_file_template.md`
- `docs/history/knowledge_base_history.md`
