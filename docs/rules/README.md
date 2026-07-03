# Rules

## Purpose

This folder contains the official operating rules for Ghost Development System
Docs.

Rules define how humans and AI should plan, document, review, and maintain the
Ghost Development System knowledge base.

Core rules include Evidence First, Purpose-Oriented Naming, Human Approval Gate,
Knowledge Before Automation, and Artifact First.

## Contains

- `rules.md`: rules index and priority.
- `core_principles.md`: core development philosophy.
- `project_rules.md`: Project First Principle and Cross Project rules.
- `language_rules.md`: Japanese-first documentation operation rules.
- `documentation_rules.md`: documentation structure and update rules.
- `artifact_first_rules.md`: file generation rules for reusable Q files,
  design documents, AI requests, roadmap proposals, and long reviews.
- `q_file_artifact_standard.md`: Task Artifact Workspace, save location,
  status movement, naming, completion report pairing, notes, attachments, and
  commit linkage standard for Q file artifacts.
- `workflow_rules.md`: development workflow and gates.
- `git_rules.md`: Git history and commit rules.
- `quality_rules.md`: quality and review standards.
- `ai_collaboration_rules.md`: human and AI collaboration rules.
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
3. `project_rules.md`
4. `language_rules.md`
5. `documentation_rules.md`
6. `artifact_first_rules.md`
7. `q_file_artifact_standard.md`
8. `workflow_rules.md`
9. `quality_rules.md`
10. `ai_collaboration_rules.md`
11. `git_rules.md`
12. `script_architecture_rules.md`

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
