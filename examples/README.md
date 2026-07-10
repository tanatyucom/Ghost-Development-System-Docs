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
- `field_driven_development_cycle.md`: example for promoting field project
  learning into Ghost Development System.
- `evidence_feedback_loop.md`: example for connecting implementation results,
  metrics, knowledge promotion, and next improvement.
- `artifact_first_examples.md`: good and bad examples for file-first Q files,
  design documents, AI requests, review requests, and roadmap proposals.
- `startup_checklist_examples.md`: good and bad examples for startup
  repository confirmation, rule confirmation, methodology confirmation, Q
  artifact confirmation, scope guard, and commit policy checks.
- `repository_root_validation_examples.md`: good and bad examples for checking
  actual Git root against the expected Working Repository.
- `ai_proactive_proposal_examples.md`: good and bad examples for AI proposals
  that share evidence-based improvements, risks, conflicts, and knowledge
  opportunities without silently changing implementation.
- `collaborative_decision_examples.md`: good and bad examples for AI proposal,
  user proposal, discussion, evidence review, knowledge classification,
  decision, and documentation target.
- `completion_checklist_examples.md`: good and bad examples for completion
  verification, review, completion report, Improvement Review, commit / tag /
  release decisions, next Q, and workspace clean confirmation.
- `q_file_artifact_workflow.md`: good and bad examples for Task Artifact
  Workspaces, Q files, completion reports, notes, attachments, and related
  commit information.
- `audit_before_repair_examples.md`: good and bad examples for auditing,
  classifying, reviewing evidence, scoping repair Q files, and avoiding broad
  one-shot repair.
- `dirty_workspace_examples.md`: good and bad examples for classifying dirty
  workspace files, restoring accidental runtime changes, and keeping commits
  scoped.
- `migration_first_examples.md`: good and bad examples for migrating internal
  architecture to a new standard, updating references, verifying, removing
  legacy, and reporting public compatibility impact.
- `debug_artifact_review_examples.md`: good and bad examples for Debug Mode,
  intermediate artifact review, expected normal state, design review before
  fixes, and debug artifact Git policy.
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
- Use `field_driven_development_cycle.md` when a field project reveals reusable
  workflow, architecture, rule, or knowledge platform learning.
- Use `evidence_feedback_loop.md` when a completed task should be evaluated
  with metrics and converted into reviewed evidence.
- Use `artifact_first_examples.md` when deciding whether a long Q, design
  document, review request, Codex / Gemini / Claude request, or roadmap update
  proposal should be generated as `.md` / `.docx` artifacts instead of pasted
  into chat.
- Use `startup_checklist_examples.md` before starting a new AI session, Codex
  run, review, Q execution, or documentation update that could confuse
  repository boundaries, applicable rules, methodology, Q artifact state, or
  commit policy.
- Use `repository_root_validation_examples.md` when the current shell location,
  Git root, production repository, backup repository, or reference-only
  repository could be confused.
- Use `ai_proactive_proposal_examples.md` when AI should raise a better
  approach, time saving opportunity, conflict, risk, or knowledge opportunity
  before changing work.
- Use `collaborative_decision_examples.md` when proposals need discussion and
  knowledge classification before becoming a rule, workflow, CASE, concept,
  template, or future candidate.
- Use `completion_checklist_examples.md` before treating work as complete,
  committing, tagging, releasing, or handing off the next Q.
- Use `q_file_artifact_workflow.md` when saving a Q file in a
  `docs/requests/<target_project>/<status>/` workspace, naming it, linking it
  to a completion report, storing notes or attachments, moving status, or
  recording related commit status.
- Use `audit_before_repair_examples.md` before repair, cleanup, OCR result
  correction, DB correction, mojibake correction, duplicate resolution, or
  metadata correction when the target should be audited and classified first.
- Use `dirty_workspace_examples.md` before staging or committing when the
  workspace contains unrelated files, runtime data, local cache, temporary
  files, or review outputs.
- Use `migration_first_examples.md` when changing internal folder structure,
  script layout, adapter internal interface, prototype scripts, shared utility
  location, artifact workspace layout, queue / request structure, or future
  GhostCore / GDS internal modules.
- Use `debug_artifact_review_examples.md` when AI, OCR, recommendation,
  auto-detection, candidate extraction, fuzzy matching, visual overlays, or
  intermediate artifacts need review before fixes or final judgment.
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
- Metrics / Evidence completion report example.

## Update Policy

Update examples when templates or rules change enough that existing examples no
longer show the recommended pattern.

Do not use examples to introduce new rules. Promote reusable standards to
`docs/rules/` or `docs/templates/` first.

## Related Documents

- `docs/templates/`
- `docs/rules/`
- `docs/rules/startup_checklist_rules.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/rules/ai_proactive_proposal_rules.md`
- `docs/rules/completion_checklist_rules.md`
- `docs/workflow/startup_checklist_workflow.md`
- `docs/workflow/repository_root_validation_workflow.md`
- `docs/workflow/collaborative_decision_workflow.md`
- `docs/workflow/completion_checklist_workflow.md`
- `templates/startup_checklist_template.md`
- `templates/repository_root_validation_template.md`
- `templates/collaborative_decision_template.md`
- `templates/completion_checklist_template.md`
- `docs/templates/review_checklist.md`
- `docs/templates/q_file_template.md`
- `docs/templates/completion_report_template.md`
- `docs/requests/README.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/audit_before_repair_rules.md`
- `docs/rules/migration_first_rules.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/git_rules.md`
- `docs/workflow/commit_safety_checklist.md`
- `docs/workflow/audit_before_repair_workflow.md`
- `docs/workflow/debug_artifact_review_workflow.md`
- `docs/history/knowledge_base_history.md`
