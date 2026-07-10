# Public Glossary

## Purpose

This glossary defines common Ghost Development System terms in short,
human-readable language.

Use it to keep humans and AI aligned on public Knowledge Base vocabulary.

## Contains

- Shared public terms.
- Short definitions for humans and AI.
- Cross-document vocabulary used by rules, templates, roadmap, architecture,
  workflow, and examples.

## Does NOT Contain

- Long-form architecture explanation.
- Detailed workflow rules.
- Project-specific runtime terminology that belongs in a project repository.
- Decision Log entries.
- Historical changelog entries.

## Terms

### Ghost Development System

The archive-wide development platform direction for Gray Ghost Archive. It
supports workflow, review, documentation, templates, coordination, and
development infrastructure.

It is the parent development foundation for projects such as GameGhost,
AnimeGhost, ComicGhost, and Other. It does not automatically own
project-specific runtime behavior.

### DevelopmentSystem

Candidate implementation or folder name for the Ghost Development System
development infrastructure. It is a name candidate, not automatic approval to
create runtime folders.

### Knowledge Base

The durable public documentation set that records rules, roadmap, templates,
examples, architecture, workflow, and glossary terms.

### Archive Module

A module that owns its own business logic, schema, metadata, and import rules.

### Gray Ghost Core

The layer responsible for analysis, recommendation, and cross-module
intelligence.

### Launcher

The user entry point. It routes users to tools and archive targets but should
not own module business logic or DMS behavior.

### Repository Information

The Q file section that identifies Target Project, Repository, Working
Directory, Documentation Root, Runtime Root, Single Source Of Truth, Related
Repository, Cross Project Impact, and Scope Guard.

### Target Project

The project responsibility that a Q is about.

Examples include Ghost Development System, GameGhost, AnimeGhost, ComicGhost,
and Other.

### Cross Project Impact

The field that explains whether a Q affects another project.

Common values include None, Reference Only, Documentation Impact, Runtime
Impact, and Requires Separate Q.

### Project First Principle

The rule that every Q declares Target Project before implementation.

This prevents AI and humans from confusing the editable repository with the
project responsibility being discussed.

### Japanese First

The rule that Ghost Development System Docs uses Japanese by default for
human-facing judgment, approval, review, Q files, templates, rules, roadmap,
and completion reports.

### Scope Guard

The explicit edit boundary for a Q. It defines what may be edited and what must
not be touched.

### Single Source Of Truth

The repository or document set that is authoritative for the current Q.

### Purpose-Oriented Naming

The naming principle that public titles should describe the intended outcome
before a specific implementation method.

### Improvement Review

The completion step that asks what reusable knowledge was discovered and whether
it should improve Documentation, Templates, Workflow, Roadmap, Rules,
Architecture, or Knowledge Base.

### Future Candidate

An idea preserved for later review. It is not approved implementation scope.

### Knowledge Promotion

The process of moving reusable knowledge from a completed task into templates,
rules, examples, workflow, architecture, glossary, or other documentation.

### Knowledge Poka-Yoke

The GDS design principle that assumes humans forget, AI forgets, and processes
drift.

It turns memory-dependent work into visible checks, templates, validation,
artifacts, review points, and safe automation.

### Human Approval Gate

The rule that humans approve architecture changes, destructive changes, scope
expansion, releases, standardization, and migration work.

### Startup Checklist

The startup confirmation system used before a new AI session, Codex run,
review, Q execution, or documentation update begins.

It confirms repository boundaries, applicable rules, methodologies, Q artifact
status, scope, out-of-scope items, dirty workspace state, and commit policy.

### Repository Root Validation

The startup check that confirms the actual Git repository root with
`git rev-parse --show-toplevel` and compares it with the expected Working
Repository.

It prevents work, review, commit, tag, or release operations from starting in a
wrong folder, home directory, backup directory, or reference-only repository.

### AI Proactive Proposal

The collaboration rule that allows AI to share evidence-based improvements,
time saving opportunities, repository or scope concerns, rule conflicts,
methodology conflicts, maintenance risks, and knowledge opportunities before
changing implementation.

AI Proactive Proposal keeps final judgment with the user.

### Collaborative Decision

The workflow where AI proposals and user proposals are discussed, reviewed
against evidence, classified as knowledge, and turned into a documented
decision or follow-up.

It supports disagreement as a design process, not as an error.

### Completion Checklist

The completion confirmation system used before work is treated as complete,
committed, tagged, released, or handed off to the next Q.

It confirms verification, review, completion report, Improvement Review, commit
requirement and execution, tag requirement and execution, release requirement
and publication, Recommended Next Q, and workspace clean state.

### Artifact First

The rule that reusable, reviewable, AI-handoff, human-approval, or Git-managed
outputs should be generated as file artifacts before they become execution or
approval inputs.

Markdown `.md` is the standard format for Git and AI handoff. Word `.docx` is
used when human review, comments, approval, redline, or offline reading is
expected.

### Output Layer

The architecture boundary that decides whether an output should remain chat or
become a managed artifact.

It supports Human Approval Gate, prevents copy loss, and makes Knowledge
Promotion easier.

### Q File Artifact

A saved Q file used as the authoritative request for Codex, Gemini, Claude, or
human review.

Q file artifacts are stored in Task Artifact Workspaces under
`docs/requests/<target_project>/<status>/`.

### Task Artifact Workspace

A task folder that keeps the source request, completion report, notes, and
attachments together.

Standard form:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/
  request.md
  completion_report.md
  notes.md
  attachments/
```

Status folders are `draft`, `approved`, `completed`, and `archived`.

### Completion Report Artifact

A saved completion report that links finished work back to the source Q file,
generated files, output artifacts, commit hash when one exists, and follow-up
Q. It should be stored beside the source Q file.

### PIP

Project Information Package. A briefing layer that summarizes the current
project state, why it became that state, improvement history, decisions, known
issues, and next work.

PIP links official documents and evidence. It does not replace rules,
workflow, architecture, Q artifacts, completion reports, or source evidence.

### PIP Case

A reusable improvement knowledge entry stored under `pip/cases/`.

It records Problem, Symptoms, Investigation, Evidence, First Broken Step, Root
Cause, Fix, Validation, Lessons Learned, Related Rules, and Related Cases.

### PIP Case Index

The searchable entry point for PIP cases.

It supports lookup by Project, Category, Methodology, Priority, Lifecycle, and
Related Rule.

### PIP Master Document

The Japanese master document for Roadmap2-derived GDS / PIP methodology.

It summarizes investigation history, reusable principles, evolution, and
Roadmap3 positioning. The standard file is `pip/MASTER_DOCUMENT_JP.md`.

### PIP Master Title List

The Japanese title list used to classify reusable knowledge into CASE, Best
Practice, Evolution, Investigation, and Rule Story candidates.

The standard file is `pip/MASTER_TITLE_LIST_JP.md`.

### PIP Tagging Standard

The standard tag set for PIP cases, rule stories, evolutions, and best
practices.

Standard axes are Project, Category, Methodology, Priority, and Lifecycle.

### Debug Artifact Review

The rule and workflow for using Debug Mode during development to inspect
intermediate evidence before final judgment or fixes.

It applies to AI, OCR, recommendation, auto-detection, candidate extraction,
fuzzy matching, visual overlays, and similar uncertain processing.

Normal execution should not generate debug artifacts unless Debug Mode is
explicitly requested.

### Debug Artifact

A temporary development-time artifact such as an overlay image, candidate CSV,
intermediate JSON file, log, or report used to inspect process behavior.

Debug artifacts are not Git-managed by default. They may be promoted only by an
explicit Q or review decision.

### Debug Escalation Ladder

The standard GDS escalation order for uncertain defects and quality issues.

The ladder is Phenomenon Check, Metrics Check, Human Review, Debug Artifact
Generation, Pipeline Trace, First Broken Step Identification, Root Cause
Confirmation, and Algorithm Change.

### Phenomenon Check

The first debug step that confirms what is happening, where it happens, and
whether the issue is reproducible or human-visible.

### Metrics Check

The step that reviews logs, scores, measurements, or counters as evidence
input. Metrics do not override human review by themselves.

### Pipeline Trace

The step that records how data moves through processing stages so humans and AI
can see where state changes.

### Root Cause Confirmation

The step that confirms why the first broken step happened before algorithm
change or tuning is performed.

### Audit Before Repair

The rule and workflow for auditing, classifying, preserving evidence, and
getting required human review before repair work begins.

It applies to repair, cleanup, OCR result correction, DB correction, mojibake
correction, duplicate resolution, metadata correction, and similar work.

### Repair Q

A scoped Q artifact created after audit and classification. It identifies the
source audit artifact, target scope, exclusions, verification method, safe
commit set, and restore guidance.

### Dirty Workspace

A Git working tree state where modified, added, deleted, or untracked files
exist before commit review.

Dirty workspaces must be classified before staging or committing.

### Safe Commit Set

The set of changed files that belongs to the accepted scope and may be staged
or committed after review.

Unrelated runtime data, local cache, temporary files, and accidental outputs do
not belong in the safe commit set.

### Roadmap2 Knowledge Salvage

The loop that reviews Roadmap2, extracts reusable knowledge that has not yet
been migrated, creates Q artifacts for the missing knowledge, updates GDS / PIP,
and repeats until Roadmap2 has no remaining reusable knowledge outside the
official Knowledge Base.

### Missing Knowledge Extraction

The classification step that separates already migrated knowledge, missing
knowledge, duplicates, future candidates, non-reusable notes, human-approval
items, and source-evidence needs during Roadmap2 review.

### Concept Candidate

A reusable idea or vocabulary item that is not yet a CASE, Best Practice,
Evolution, Investigation, Rule Story, official rule, or workflow.

### Concept Promotion

The reviewed lifecycle that moves a concept from Candidate to Under Review,
Experiment, Validated, Promoted, or Archived.

Concept Promotion decides whether an idea becomes a stronger knowledge unit
such as Rule, Best Practice, Workflow, Principle, CASE, Rule Story, Evolution,
Investigation, template, glossary, or architecture.

### Validated Concept

A concept that has been tested in a real Q, review, documentation workflow, or
project workflow and is consistent with GDS principles.

### Salvage Completion Condition

The condition that Roadmap2 can become history only after reusable Roadmap2
knowledge has either been migrated into GDS / PIP, classified as duplicate,
classified as future candidate, or explicitly rejected as non-reusable.

## Update Policy

Add glossary terms when a concept appears across multiple documents or is
important for AI collaboration.

Keep definitions short. Longer explanations belong in architecture, workflow,
rules, templates, or examples.

## Related Documents

- `docs/README.md`
- `docs/rules/project_rules.md`
- `docs/rules/core_principles.md`
- `docs/rules/language_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/rules/ai_proactive_proposal_rules.md`
- `docs/rules/completion_checklist_rules.md`
- `docs/rules/artifact_first_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/audit_before_repair_rules.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/debug_escalation_ladder_rules.md`
- `docs/rules/pip_case_knowledge_base_rules.md`
- `docs/rules/roadmap2_knowledge_salvage_rules.md`
- `docs/rules/git_rules.md`
- `docs/workflow/commit_safety_checklist.md`
- `docs/workflow/startup_checklist_workflow.md`
- `docs/workflow/repository_root_validation_workflow.md`
- `docs/workflow/collaborative_decision_workflow.md`
- `docs/workflow/completion_checklist_workflow.md`
- `docs/requests/README.md`
- `docs/workflow/output_policy.md`
- `docs/workflow/audit_before_repair_workflow.md`
- `docs/workflow/debug_artifact_review_workflow.md`
- `docs/workflow/debug_escalation_ladder.md`
- `docs/workflow/pip_case_knowledge_base_workflow.md`
- `docs/workflow/concept_promotion_workflow.md`
- `docs/workflow/roadmap2_knowledge_salvage_loop.md`
- `docs/architecture/responsibility_boundary.md`
- `docs/history/knowledge_base_history.md`
