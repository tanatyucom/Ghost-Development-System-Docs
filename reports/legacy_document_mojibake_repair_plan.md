# Legacy Document Mojibake Repair Plan

- Date: 2026-07-13
- Policy: no guessed repair, no broad automatic replacement.

## Decision

- Automatic repair is not approved in this pass.
- Reason: reverse conversion tests were not lossless enough to protect meaning.
- Repair scope for this Q: audit artifacts and explicit unresolved documentation only.

## Proposed Manual Repair Order

### P1 Critical

- `docs/ai_repository_index.md`: 4 candidate lines
- `docs/rules/rules.md`: 8 candidate lines
- `docs/workflow/README.md`: 15 candidate lines
- `docs/workflow/startup_checklist_workflow.md`: 49 candidate lines

### P2 High

- `README.md`: 185 candidate lines
- `docs/README.md`: 246 candidate lines

### P3 Medium

- `examples/migration_first_examples.md`: 18 candidate lines

### P4 Low

- `docs/history/knowledge_base_history.md`: 63 candidate lines

## Repair Rules

- Repair only from known source text, trusted prior version, or explicit human-provided replacement.
- Do not infer Japanese text from mojibake when the original cannot be proven.
- After each repair batch, rerun UTF-8 audit, mojibake scan, AI Repository Index validation, repository quality audit, and git diff --check.

