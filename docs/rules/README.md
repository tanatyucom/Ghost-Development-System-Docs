# Rules

## Purpose

This folder contains the official operating rules for Ghost Development System
Docs.

Rules define how humans and AI should plan, document, review, and maintain the
Ghost Development System knowledge base.

Core rules include Evidence First, Purpose-Oriented Naming, Human Approval Gate,
Knowledge Before Automation, Knowledge Poka-Yoke / Design For Forgetfulness,
Context Recovery Principle,
UTF-8 Read Rule, Encoding Regression Prevention,
External Source Access / AI Repository Knowledge Access, AI Startup Procedure, Startup Checklist,
Startup Completion Evidence / Gate,
Repository Root Validation, AI Proactive Proposal,
Completion Checklist, Completion Report, Hotfix Policy, Beginner & Future Self Test, Research Mission, Conversation Insight Capture, Pending Conversation Insight Review, Artifact First, Audit Before Repair, Debug Artifact Review, Debug Escalation Ladder,
Migration First, PIP Case Knowledge Base, and Roadmap2 Knowledge Salvage. Concept Promotion is
handled as part of PIP Case Knowledge Base. Concept ID Naming is the standard
for assigning stable Concept IDs and keeping the Concept Index traceable.
Platform Component Rules define component classification, naming,
Discoverability 3 Second Rule, shared library limits, migration criteria, and
Review Center placement policy.
Review Center Rules define Human Review Session Manager behavior, explicit
approval, persistence, plugin registration, gate export, and legacy migration
guards.
Platform Governance Rules define Temporary Assembly, Core + Adapter
Experimental Pattern, Architecture Promotion Lifecycle, Canonical Knowledge
Ownership, Local Rule lifecycle, and Vision-Driven Bottom-Up Development.
Documentation Synchronization Rules define the gate for keeping README files,
folder indexes, AI Repository Index, completion checklist, completion report,
and repository quality audit aligned after documentation changes.
Pending Conversation Insight Review Rules define the temporary queue between
Conversation Insight Candidate and formal registration when next-day or
next-chat Human Review is safer than immediate Q化 or Codex execution.
Persistent Collaboration, Platform First, Repository First, Download First,
Rule Priority, Command Rule, Review Rule, Completion Report First, AI
Cognitive Load Reduction, and Platform Philosophy are defined in
`ai_collaboration_rules.md` and `core_principles.md`.
Platform Era principle candidates are classified in
`docs/architecture/platform_era_core_principles.md` before any new rule is
promoted.

## Contains

- `rules.md`: rules index and priority.
- `core_principles.md`: core development philosophy and Platform Era
  classification entry point, including Context Recovery Principle.
- `utf8_read_rules.md`: UTF-8 reading rule for Japanese Markdown, Q files,
  request artifacts, completion reports, and mojibake reporting.
- `encoding_regression_prevention_rules.md`: commit-gate rule for preventing
  new mojibake, replacement characters, invalid UTF-8, and broad Markdown
  rewrite regressions.
- `external_source_access_rules.md`: Raw URL Index and external public
  repository access rule for ChatGPT, Codex, and other AI systems.
- `ai_startup_procedure_rules.md`: AI startup reading order and stop
  conditions before implementation, review, documentation update, or Q
  execution begins. Includes Information Package check and Research Task
  Detection before normal implementation starts.
- `project_rules.md`: Project First Principle and Cross Project rules.
- `language_rules.md`: Japanese-first documentation operation rules.
- `documentation_rules.md`: documentation structure and update rules.
- `startup_checklist_rules.md`: startup confirmation rule for repository,
  scope, applicable rules, methodologies, Q artifacts, and commit policy before
  implementation or review begins.
- Startup Completion Evidence / Gate is defined in
  `docs/workflow/startup_completion_evidence.md` and
  `docs/workflow/startup_completion_gate.md` as the proof layer after Startup
  Checklist and before Q creation, implementation, review, or documentation
  update.
- `repository_root_validation_rules.md`: rule for validating actual Git root
  against Working Repository before implementation, review, commit, tag, or
  release work begins.
- `ai_proactive_proposal_rules.md`: rule for AI to propose evidence-based
  improvements, time savings, conflicts, risks, or knowledge opportunities
  without silently changing implementation.
- `completion_checklist_rules.md`: completion confirmation rule for
  verification, review, completion report, Improvement Review, commit, tag,
  release, next Q, and workspace clean confirmation.
- `completion_report_rules.md`: Completion Report v2 required sections, Safe Commit Set, Commit / Push Status, Project Edit Status, Improvement Review, Lessons Learned, Reusable Assets Created, Remaining Issues, Recommended Next Q, and Suggested Commit Message rules.
- `hotfix_policy_rules.md`: rule for separating GDS Hotfix from normal
  release or improvement work. Defines Fix Once, Recover Everywhere, GDS asset
  ownership, hotfix classification, and hotfix adoption record expectations.
- `beginner_future_self_test_rules.md`: documentation quality rule for checking
  whether beginners, new AI sessions, future contributors, returning project
  owners, and future selves can understand purpose, current position, evidence,
  next action, and authority without hidden chat context.
- `research_mission_rules.md`: rule for scoped investigation missions that
  define Goal, Scope, Out of Scope, Evidence, Validation, Negative Result
  handling, and Completion Report before research begins. Startup Procedure
  branches here when Research Task Detection is Yes.
- `conversation_insight_capture_rules.md`: rule for detecting conversation-origin
  design philosophy, operation policy, maintenance policy, migration strategy,
  Command Center concepts, and long-term vision as Human Approval-gated
  pre-promotion knowledge without auto-saving or preserving full chat logs.
- `pending_conversation_insight_review_rules.md`: rule for temporarily holding
  conversation-origin candidates, reviewing them at Startup / Daily Knowledge
  Review, blocking Codex execution while pending, and confirming cleanup after
  reflection.
- `artifact_first_rules.md`: file generation rules for reusable Q files,
  design documents, AI requests, roadmap proposals, and long reviews.
- `q_file_artifact_standard.md`: Task Artifact Workspace, save location,
  status movement, naming, completion report pairing, notes, attachments, and
  commit linkage standard for Q file artifacts.
- `q_file_naming_rules.md`: Q ID, filename, date exception, request folder,
  status, revision, addendum, and completion report linkage rules.
- `q_file_template_rules.md`: mandatory Q template fields for repository
  context, commit / push policy, validation, AI Repository Index gate,
  completion report requirements, Safe Commit Set, and review decision.
- `audit_before_repair_rules.md`: audit, classification, evidence, human
  review, scoped repair Q, verification, and commit flow for repair work.
- `debug_artifact_review_rules.md`: Debug Mode, intermediate artifact review,
  expected normal state, review entry point, completion report announcement,
  AI review handoff, and Git policy for debug artifacts.
- `debug_escalation_ladder_rules.md`: standard escalation order from
  phenomenon check, metrics, human review, debug artifacts, pipeline trace,
  first broken step, root cause, to algorithm change.
- `migration_first_rules.md`: internal architecture rule for preferring
  standard migration, reference update, verification, and legacy removal over
  permanent compatibility fallback.
- `platform_component_rules.md`: component classification, folder, naming,
  shared library, migration, legacy, Review Center, and Human Approval rules for
  shared Ghost Platform components.
- `review_center_rules.md`: Human Review Session Manager rules for Review
  Center, including platform / domain boundary, GUI name, persistence, missing
  artifacts, correction history, plugin registration, gate export, and legacy
  behavior.
- `platform_governance_rules.md`: platform governance, Temporary Assembly,
  Core + Adapter Experimental Pattern, Architecture Promotion, canonical
  knowledge ownership, Local Rule lifecycle, and Vision-Driven Bottom-Up
  Development rules.
- `documentation_synchronization_rules.md`: rules for detecting documentation
  changes that require README, folder index, AI Repository Index, completion
  checklist, completion report, and repository quality synchronization before
  completion.
- `pip_case_knowledge_base_rules.md`: standard locations, metadata, tags,
  case sections, evidence linking, PIP Master Document / Title List handling,
  concept lifecycle, and promotion rules for PIP cases.
- `concept_id_naming_rules.md`: Concept ID format, sequence rules, Concept
  Index requirements, and promoted / archived tracking.
- `roadmap2_knowledge_salvage_rules.md`: final Roadmap2 knowledge migration
  loop, missing knowledge classification, destination rules, and completion
  criteria.
- `workflow_rules.md`: development workflow and gates.
  Includes AI Daily Operation Cycle as the outer loop for recurring
  AI-assisted GDS work.
- `git_rules.md`: Git history, dirty workspace policy, file classification,
  and commit safety rules.
- `quality_rules.md`: quality and review standards.
- `ai_collaboration_rules.md`: human and AI collaboration rules, including
  Persistent Collaboration, Platform First, Repository First, Download First,
  command presentation, review conclusion, completion report priority, and AI
  cognitive load reduction.
- `script_architecture_rules.md`: script architecture principles for related
  implementation repositories.

## Does NOT Contain

- Runtime implementation.
- Private archive data.
- Queue execution state.
- GitHub Actions configuration.
- Release process automation.

## Reading Order

1. `rules.md`
2. `core_principles.md`
3. `utf8_read_rules.md`
4. `encoding_regression_prevention_rules.md`
4. `external_source_access_rules.md`
5. `ai_startup_procedure_rules.md`
6. `project_rules.md`
7. `language_rules.md`
8. `documentation_rules.md`
9. `startup_checklist_rules.md`
10. `repository_root_validation_rules.md`
11. `ai_proactive_proposal_rules.md`
12. `completion_checklist_rules.md`
13. `completion_report_rules.md`
14. `hotfix_policy_rules.md`
15. `beginner_future_self_test_rules.md`
16. `research_mission_rules.md`
17. `conversation_insight_capture_rules.md`
18. `pending_conversation_insight_review_rules.md`
19. `artifact_first_rules.md`
20. `q_file_artifact_standard.md`
21. `q_file_naming_rules.md`
22. `q_file_template_rules.md`
23. `audit_before_repair_rules.md`
24. `debug_artifact_review_rules.md`
25. `debug_escalation_ladder_rules.md`
26. `migration_first_rules.md`
27. `platform_component_rules.md`
28. `review_center_rules.md`
29. `platform_governance_rules.md`
30. `documentation_synchronization_rules.md`
31. `pip_case_knowledge_base_rules.md`
32. `concept_id_naming_rules.md`
33. `roadmap2_knowledge_salvage_rules.md`
34. `workflow_rules.md`
35. `quality_rules.md`
36. `ai_collaboration_rules.md`
37. `git_rules.md`
38. `script_architecture_rules.md`

## Update Policy

Rules should be updated when repeated practice proves that a behavior should be
standardized.

New rules should be added only when they improve clarity, reduce mistakes, or
protect long-term maintainability.

Use one file for one theme. If a rule does not clearly belong in an existing
file, create a new rule document only after confirming that the responsibility
is distinct.

## Decision Background Policy

Important rules may include a short `Decision Background` section.

Use it to explain why the rule exists in a few lines.

Do not use it as a full Decision Log. Detailed alternatives, rejected options,
approval history, and long rationale should be handled by a separate decision
document or ADR when needed.
