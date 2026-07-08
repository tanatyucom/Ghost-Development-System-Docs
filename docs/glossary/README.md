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

### Human Approval Gate

The rule that humans approve architecture changes, destructive changes, scope
expansion, releases, standardization, and migration work.

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

## Update Policy

Add glossary terms when a concept appears across multiple documents or is
important for AI collaboration.

Keep definitions short. Longer explanations belong in architecture, workflow,
rules, templates, or examples.

## Related Documents

- `docs/README.md`
- `docs/rules/project_rules.md`
- `docs/rules/language_rules.md`
- `docs/rules/artifact_first_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/audit_before_repair_rules.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/pip_case_knowledge_base_rules.md`
- `docs/rules/git_rules.md`
- `docs/workflow/commit_safety_checklist.md`
- `docs/requests/README.md`
- `docs/workflow/output_policy.md`
- `docs/workflow/audit_before_repair_workflow.md`
- `docs/workflow/debug_artifact_review_workflow.md`
- `docs/workflow/pip_case_knowledge_base_workflow.md`
- `docs/architecture/responsibility_boundary.md`
- `docs/history/knowledge_base_history.md`
