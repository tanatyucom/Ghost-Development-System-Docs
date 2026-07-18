# Examples

## Purpose

This folder is the best practice library for Ghost Development System Docs.

Examples show how the rules and templates should look in real documentation
work. They are written for humans and AI so new Q files, reviews, completion
reports, and documentation requests can start from a clear reference.

## Contains

- `good_q.md`: example of a well-written Q file.
- `good_review.md`: example of a complete review report.
- `good_completion_report.md`: legacy simple example completion report.
- `completion_report_examples.md`: good and bad examples for Completion Report
  v2, including Identity, Changed Files, Verification, Safe Commit Set,
  Commit / Push Status, Project Edit Status, Improvement Review, Lessons
  Learned, Reusable Assets Created, Remaining Issues, Recommended Next Q, and
  Suggested Commit Message.
- `repository_recommendation_examples.md`: examples for Codex Repository
  Recommendation blocks, including normal commit recommendation, validation
  failure, mixed scope, push review, diverged branch, tag recommendation, stale
  recommendation, and insufficient evidence.
- `workflow_recommendation_examples.md`: examples for ChatGPT Workflow
  Recommendation blocks, including approval request mode, execution instruction
  mode, missing pending request, independent approval units, stale state, mixed
  scope, audience wording, duplicate approval prompt, tag independence, and
  UTF-8 display false positives.
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
- `beginner_future_self_test_examples.md`: PASS, PASS WITH MINOR IMPROVEMENTS,
  FAIL, and duplication-guard examples for checking whether documentation is
  understandable to beginners, new AI sessions, returning project owners, and
  future selves.
- `context_recovery_examples.md`: examples for future self recovery, incident
  recovery, and new AI session recovery without relying on memory or chat
  history.
- `q_file_artifact_workflow.md`: good and bad examples for Task Artifact
  Workspaces, Q files, completion reports, notes, attachments, and related
  commit information.
- `q_file_examples.md`: good and bad examples for Q ID, Q filename,
  date exception, request workspace, addendum, repository context, and
  completion report linkage.
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
- `innovation_pipeline_examples.md`: examples for moving ideas through Idea,
  Experiment, Prototype, Validation, Platform Promotion, Standardization, and
  Propagation.
- `conversation_insight_examples.md`: good and bad examples for proposing,
  approving, drafting, reviewing, and promoting conversation-origin insights
  without auto-saving chat or treating Future Candidates as approved scope.
- `pending_conversation_insight_examples.md`: good and bad examples for
  temporarily holding conversation-origin ideas, next-day review, Codex
  execution restriction, and cleanup confirmation.
- `platform_promotion_decision_report_examples.md`: examples for Promote,
  Revise, Reject, and Archive decisions after Innovation Pipeline validation.
- `platform_standard_registry_examples.md`: examples for Candidate to
  Standard, Standard update, Deprecated, and Replaced registry operations.
- `platform_registry_update_completed_examples.md`: completed examples for
  New Standard, Standard Update, Deprecation, Replacement, and Archive registry
  update artifacts.
- `platform_discoverability_and_component_examples.md`: good and bad examples
  for Platform folder placement, component classification, naming, plugin
  discoverability, Review Center split, and migration candidate decisions.
- `review_center_examples.md`: good and bad examples for Review Center
  platform / adapter split, explicit approval state, resume behavior, and
  avoiding silent auto approval.
- Documentation Synchronization:
  `documentation_synchronization_examples.md` shows good and bad examples for
  keeping README / folder index, AI Repository Index, completion checklist,
  completion report, and repository quality audit aligned after documentation
  changes.
- `documentation_synchronization_examples.md`: good and bad examples for
  updating README / folder index entry points, AI Repository Index, completion
  checklist, completion report, and Repository Quality Audit after
  documentation changes.
- `persistent_collaboration_examples.md`: good and bad examples for command
  presentation, review conclusion, Download First, Repository First, Platform
  First, AI collaboration, and completion report priority.
- `multi_ai_handoff_reference_examples.md`: good and bad examples for
  ChatGPT, Codex, Claude, Gemini, and human review handoff artifacts.
- `artifact_metadata_reference_examples.md`: good and bad examples for
  Structured Artifact Metadata YAML front matter across Q, Completion Report,
  Information Package, Multi-AI Handoff, Registry Update, and Health Report.
- `capability_examples.md`: good and bad examples for verifying capability
  before answering whether the current AI, repository, tool, permission, or
  connected service can complete a task.
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
- Use `completion_report_examples.md` when checking whether a Completion
  Report v2 is complete, reviewable, and safe to hand off.
- Use `repository_recommendation_examples.md` when Codex needs to recommend
  Commit, Push, or Tag to ChatGPT without implying Human Final Approval or
  execution authority.
- Use `workflow_recommendation_examples.md` when ChatGPT needs to convert
  Completion Review and Codex Repository Recommendation into a human-facing
  Workflow Recommendation or Execution Instruction.
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
- Use `beginner_future_self_test_examples.md` when reviewing whether a
  managed artifact can be understood without hidden chat context and without
  excessive duplication.
- Use `context_recovery_examples.md` when checking whether a project,
  artifact, server procedure, or AI handoff can be safely resumed by someone
  who remembers nothing.
- Use `q_file_artifact_workflow.md` when saving a Q file in a
  `docs/requests/<project>/<status>/` workspace, naming it, linking it
  to a completion report, storing notes or attachments, moving status, or
  recording related commit status.
- Use `q_file_examples.md` when deciding Q ID, filename, date exception,
  addendum versus new Q, repository context, or Safe Commit Set linkage.
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
- Use `innovation_pipeline_examples.md` when a field project experiment,
  improvement idea, or future automation candidate may become a Platform
  Standard through Innovation Pipeline.
- Use `conversation_insight_examples.md` when a conversation reveals reusable
  design philosophy, operation policy, maintenance policy, migration strategy,
  Command Center concept, or long-term vision that may need Human
  Approval-gated preservation before promotion.
- Use `pending_conversation_insight_examples.md` when a conversation reveals a
  promising idea but immediate registration, Q化, or Codex execution should be
  deferred until next Startup or Human Review.
- Use `platform_promotion_decision_report_examples.md` when deciding whether a
  validated Innovation Pipeline item should be promoted, revised, rejected, or
  archived.
- Use `platform_standard_registry_examples.md` when adding, promoting,
  updating, deprecating, or replacing a Platform Standard Registry entry.
- Use `platform_registry_update_completed_examples.md` when filling out
  `templates/platform_registry_update_template.md` for a real registry update.
- Use `platform_discoverability_and_component_examples.md` when deciding whether
  a component belongs under Platform, a project adapter, shared library, plugin,
  engine, service, schema, review, import, export, or report folder.
- Use `review_center_examples.md` when designing a human review session,
  adapter boundary, explicit approval state, resume behavior, correction
  history, or gate-ready review export.
- Use `documentation_synchronization_examples.md` when a rule, workflow,
  architecture, template, example, report, README, or AI index update may need
  synchronized documentation entry points before completion.
- Use `persistent_collaboration_examples.md` when applying persistent
  collaboration behavior across ChatGPT, Codex, Claude, Gemini, human review,
  Q files, completion reports, command presentation, and review conclusions.
- Use `multi_ai_handoff_reference_examples.md` when filling out
  `templates/multi_ai_handoff_template.md` for feature implementation, review,
  bug fix, investigation-only, or uncommitted dirty workspace handoff.
- Use `artifact_metadata_reference_examples.md` when reviewing whether
  structured artifact metadata is readable, safe, and aligned with
  `templates/structured_artifact_metadata_template.md`.
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
- Platform Standard Registry example.
- Platform Discoverability / Component Interface example.
- Multi-AI Handoff example for generated Information Packages.
- Artifact Metadata examples for future validators and Command Center routing.

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
- `docs/workflow/conversation_insight_capture_workflow.md`
- `docs/workflow/completion_checklist_workflow.md`
- `templates/startup_checklist_template.md`
- `templates/repository_root_validation_template.md`
- `templates/collaborative_decision_template.md`
- `templates/completion_checklist_template.md`
- `docs/templates/review_checklist.md`
- `templates/Q_TEMPLATE.md`
- `docs/templates/completion_report_template.md`
- `docs/requests/README.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_naming_rules.md`
- `docs/rules/q_file_template_rules.md`
- `docs/workflow/q_file_creation_workflow.md`
- `docs/workflow/q_revision_addendum_workflow.md`
- `docs/rules/audit_before_repair_rules.md`
- `docs/rules/migration_first_rules.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/git_rules.md`
- `docs/rules/ai_collaboration_rules.md`
- `templates/multi_ai_handoff_template.md`
- `templates/multi_ai_handoff_checklist_template.md`
- `templates/structured_artifact_metadata_template.md`
- `docs/workflow/commit_safety_checklist.md`
- `docs/workflow/audit_before_repair_workflow.md`
- `docs/workflow/debug_artifact_review_workflow.md`
- `docs/history/knowledge_base_history.md`
