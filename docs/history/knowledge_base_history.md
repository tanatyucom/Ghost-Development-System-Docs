# Knowledge Base History

## Purpose

この文書は、Ghost Development System Knowledge Base 自身の進化を記録します。

GameGhost の CHANGELOG、Development History、Decision Log ではありません。
Knowledge Base の構造、運用、review quality、project management、AI
collaboration がどのように改善されたかを簡潔に残します。

## Ver1.0

### Added

- Knowledge Base Index。
- 目的別 navigation。
- AI Entry Points。
- Authority Order。
- Knowledge Promotion guidance。
- Scaling Policy。

### Reason

Architecture、Workflow、Roadmap、Rules、Templates、Examples、Glossary が増え、
人間と AI がどこから読めばよいか分かりにくくなったため。

### Evolution

Knowledge Base が単なる folder collection から、目的別に読める公式入口を持つ
documentation system へ進化した。

## Ver1.1

### Added

- Project First Principle。
- Japanese First。
- Cross Project Impact。
- Project Rules。
- Language Rules。
- Ghost Development System Roadmap。
- Target Project を含む Q file template。

### Reason

Ghost Development System を GameGhost から独立した親の開発基盤として扱う必要が
明確になったため。

人間が理解できない依頼文は Human Approval を満たせず、Target Project が曖昧な
Q は誤編集や scope drift を起こす可能性があるため。

### Evolution

Knowledge Base が、GameGhost 補助文書ではなく、複数 project を支える開発基盤の
ルールセットへ進化した。

## Ver1.2

### Added

- Roadmap README の roadmap 一覧。
- Project Hierarchy。
- 強化された Review Checklist。
- Decision Background の軽量な記録方針。
- Knowledge Base History。

### Reason

Ver1.1 で追加した Project First、Japanese First、Cross Project Impact を、review
品質と navigation の中で安定して使えるようにする必要があったため。

Knowledge Base 自身の進化を振り返れる場所がないと、なぜ現在の構造になったのか
が将来分かりにくくなるため。

### Evolution

Knowledge Base が、入口とルールを持つ状態から、review quality と自己履歴を持つ
保守可能な documentation platform へ進化した。

## Ver1.3

### Added

- Artifact First / File Generation First rule.
- Output Policy for Chat versus Artifact decisions.
- Output Layer architecture boundary.
- Q template Output Format and Required Artifacts sections.
- Artifact First examples for long Q files, design documents, AI requests,
  review requests, and roadmap proposals.

### Reason

Long Q files, design documents, review requests, Codex requests, roadmap
proposals, and specifications can be truncated, copied incompletely, or lose
Markdown structure when they exist only in chat.

Reusable and Git-managed work needs durable file artifacts so humans and AI
review the same complete source.

### Evolution

Knowledge Base evolved from conversation-supported documentation into a
file-first artifact system for reusable requests, human approval, AI handoff,
and Knowledge Promotion.

## Ver1.4

### Added

- Q File Artifact Standard.
- Standard Q artifact save location: `docs/requests/`.
- Q artifact file naming pattern:
  `YYYY-MM-DD_<target_project>_<short_title>.md`.
- Completion report artifact naming pattern:
  `YYYY-MM-DD_<target_project>_<short_title>_completion_report.md`.
- Q template sections for Artifact Output, Save Location, File Naming,
  Related Completion Report, and Related Commit.
- Completion report template sections for Source Q File, Output Artifacts,
  Generated Files, Commit Hash, and Follow-up Q.
- Q File Artifact Workflow examples.

### Reason

Artifact First made file generation the general rule. Q files also need a
specific save location, naming standard, and completion report linkage so the
original request can be found after implementation.

### Evolution

Knowledge Base evolved from file-first output policy into a request artifact
workflow where Q, Codex execution, completion report, review, commit, and
Knowledge Promotion can be followed as one chain.

## Ver1.5

### Added

- Task Artifact Workspace standard.
- Project folders under `docs/requests/`.
- Status folders: `draft`, `approved`, `completed`, and `archived`.
- Full task workspace shape with `request.md`, `completion_report.md`,
  `notes.md`, and `attachments/`.
- Movement rules for `draft -> approved -> completed -> archived`.
- Review quality rule that missing Q artifact path is a review issue.
- Migration guidance for moving existing flat request artifacts safely.

### Reason

The flat `docs/requests/` model is useful at first, but it becomes hard to scan
as Q artifacts grow. Humans and AI need path-level signals for Target Project,
workflow status, task purpose, related completion report, notes, and
attachments.

### Evolution

Knowledge Base evolved from saved Q files into task workspaces that preserve
the whole request-to-review chain.

## Ver1.6

### Added

- Dirty Workspace Policy.
- File classification table for commit review.
- Commit Safety Checklist.
- Completion report fields for dirty workspace state, unrelated files,
  suggested restore commands, and safe commit set.
- Dirty workspace examples for restoring unrelated runtime files and keeping
  commits scoped.

### Reason

Local runtime files, generated reports, cache, and temporary outputs can remain
modified after successful work. Without a standard safety check, unrelated
files may be accidentally committed with documentation or implementation
changes.

### Evolution

Knowledge Base evolved from artifact traceability into commit safety practice:
every changed file should be classified before commit, and the safe commit set
should be explicit.

## Ver1.7

### Added

- Debug Artifact Review Rules.
- Debug Artifact Review Workflow.
- Q template fields for Debug Mode, intermediate artifacts, expected normal
  state, review viewpoints, AI review targets, and debug artifact Git policy.
- Completion report fields for debug artifact save location, verification
  target, expected normal state, review viewpoints, and follow-up Fix Q.
- Codex / AI implementation and review template guidance for Debug Mode.
- Debug Artifact Review examples.
- Glossary terms for Debug Artifact Review and Debug Artifact.

### Reason

AI, OCR, recommendation, auto-detection, candidate extraction, fuzzy matching,
and visual processing work can look successful in final output while
intermediate behavior is wrong.

Debug artifacts make the process inspectable, but they must not pollute normal
execution or enter Git accidentally.

### Evolution

Knowledge Base evolved from artifact traceability and commit safety into
development-time evidence review: intermediate artifacts can support human
approval, AI review, design review, and future Fix Q drafting without becoming
normal output.

## Ver1.8

### Added

- Audit Before Repair Rules.
- Audit Before Repair Workflow.
- Q template fields for source audit artifact, classification, repair scope,
  exclusions, evidence review, verification, safe commit set, and restore
  guidance.
- Completion report fields for Source Audit Artifact, Classification Summary,
  Repair Scope, Excluded Items, Fixed Files, Remaining Candidates, Safe Commit
  Set, and Suggested Restore Commands.
- AI collaboration guidance for audit-first repair handoff.
- Audit Before Repair examples.
- Glossary terms for Audit Before Repair and Repair Q.

### Reason

Repair work can damage source data, generated artifacts, DB files, OCR raw
evidence, or unrelated dirty workspace changes when the target is not audited
and classified first.

### Evolution

Knowledge Base evolved from development-time evidence review into
audit-first repair practice: repair work now starts from visible evidence and a
scoped Repair Q instead of broad one-shot modification.

## Ver1.9

### Added

- Review Entry Point Rule for Debug Artifact Review.
- Completion Report Template section for first artifact path, reason, and
  priority.
- Q File Template field for expected Review Entry Point.
- Codex Review Template checks for Review Entry Point.
- Steam OCR example showing contact sheet, overlay, crop, CSV, and Markdown
  report review order.
- PIP Rule Story candidate: Review Entry Point Rule / Too Many Artifacts.

### Reason

Debug Artifact Review can generate many artifacts: contact sheets, overlays,
crops, CSV files, and Markdown reports. Without a clear entry point, humans and
AI reviewers may not know where to start.

### Evolution

Knowledge Base evolved from "generate evidence" into "make evidence reviewable":
Completion Reports now identify the first artifact to inspect before listing
the full artifact set.

## Ver1.10

### Added

- PIP v1.1 Stable。
- PIP directory README。
- PIP Improvement History。
- PIP Decision History。
- Migration guide from PIP v1.0 to v1.1。
- PIP Changelog。
- Knowledge Base Index entry for PIP。
- Architecture boundary entry for PIP。
- Workflow guidance for PIP update and AI handoff。

### Reason

Roadmap2 と OCR review work により、PIP は単なる handoff document ではなく、
現在の project state と、なぜその状態になったかを説明する reusable briefing layer
であることが分かりました。

PIP が GitHub Docs、Information Package、roadmap archive、completion reports、
chat summaries と重複しないように、GDS 内での stable position が必要でした。

### Evolution

Knowledge Base は、reviewable debug artifacts から、briefing と history を含む
より完全な system へ進化しました。PIP は current state、Improvement History、
Decision History、AI handoff を扱い、GitHub Docs は Single Source of Truth のまま
維持されます。

## Ver1.11

### Added

- Roadmap2 Completion Delta integration for PIP v1.1。
- PIP Review Methodology。
- Trace Before Tune。
- First Broken Step。
- Review Entry Point。
- Human Visual Review。
- Evolution Chain。
- PIP Delta Integration Summary。

### Reason

Roadmap2 の OCR review では、最終結果だけではなく、中間 trace、最初に壊れた step、
review artifact の入口、人間による visual review が品質保証に必要であることが
確認されました。

### Evolution

PIP は current state と decision history だけでなく、その state に到達するための
review methodology も保存する briefing layer へ拡張されました。

## Ver1.12

### Added

- PIP v1.1 package reconciliation with `PIP_v1.0_stable.zip` and
  `GDS_PIP_v1.1_delta_package_20260708.zip`。
- PIP Case Index。
- Reconciliation Report。
- Evaluate What Actually Matters。
- Metrics can pass while visual containment fails。
- Target Row Identity / Title BBox traceability。
- Target Row Trace / Pipeline Trace as standard artifact option。
- Steam OCR v2 debugging sequence as reusable cases。

### Reason

実Delta Packageを確認した結果、前回のQ本文ベース統合では主要テーマは反映済みでしたが、
PIP v1.0 stable の improvement knowledge database という位置付けと、metric proxy /
visual containment / trace artifact option / case index の明示が不足していました。

### Evolution

PIP は briefing layer と improvement knowledge database の両方として整理され、
evidence package と実装文書の整合性を確認する reconciliation process も記録対象になりました。

## Ver1.13

### Added

- PIP Case Knowledge Base rule.
- PIP Case Knowledge Base workflow.
- Standard PIP folders: `pip/cases/`, `pip/rule_stories/`,
  `pip/evolutions/`, `pip/best_practices/`, and `pip/templates/`.
- PIP Tagging Standard.
- CASE template with required metadata and sections.
- Case Index search axes for Project, Category, Methodology, Priority,
  Lifecycle, and Related Rule.
- Glossary entries for PIP, PIP Case, PIP Case Index, and PIP Tagging Standard.

### Reason

PIP v1.1 established PIP as an improvement knowledge database, but reusable
cases still needed a stable structure, tag vocabulary, index policy, and CASE
template.

Without standard metadata and tags, future humans and AI cannot reliably find
cases by project, methodology, related rule, or lifecycle state.

### Evolution

Knowledge Base evolved from PIP package reconciliation into a case-based
knowledge system. Field issues and completion reports can now be promoted into
searchable CASE entries, then into Rule Stories, Best Practices, Evolutions,
or official rules and workflows when approved.

## Ver1.14

### Added

- Japanese PIP Master Document: `pip/MASTER_DOCUMENT_JP.md`.
- Japanese PIP Master Title List: `pip/MASTER_TITLE_LIST_JP.md`.
- `pip/investigations/` as a PIP Knowledge Base category.
- Candidate lists for CASE, Best Practice, Evolution, Investigation, and Rule
  Story entries derived from the master title list.
- README and Knowledge Base Index links to the master document and title list.
- Rule and workflow guidance for maintaining PIP Master Document / Title List
  integration.

### Reason

Roadmap2 produced reusable GDS / PIP methodology from Steam OCR v2
investigation work. The master document and title list needed to become
official PIP Knowledge Base entry points, not loose external evidence.

### Evolution

PIP evolved from case-based knowledge storage into a master-document-driven
knowledge structure. Roadmap2 lessons can now be reviewed from a single master
document, then followed into classified candidate files for future promotion.

## Ver1.15

### Added

- Debug Escalation Ladder Rules.
- Debug Escalation Ladder Workflow.
- Debug Escalation Ladder entry in README and Knowledge Base Index.
- Architecture boundary for debug escalation order.
- PIP Master Document section for Debug Escalation Ladder.
- Glossary terms for Debug Escalation Ladder, Phenomenon Check, Metrics Check,
  Pipeline Trace, and Root Cause Confirmation.

### Reason

Roadmap2 debugging showed that defects should not jump directly from symptom or
metric to parameter tuning or algorithm change.

GDS needed a standard escalation order that puts phenomenon confirmation,
metrics, human review, debug artifacts, pipeline trace, first broken step, and
root cause before algorithm modification.

### Evolution

Knowledge Base evolved from debug artifact review into a broader debugging
decision ladder. Debug Artifact Review now sits inside a larger escalation
sequence that protects evidence-first debugging and root-cause-first
improvement.

## Ver1.16

### Added

- Roadmap2 Knowledge Salvage Rules.
- Roadmap2 Knowledge Salvage Loop Workflow.
- Roadmap2 Knowledge Salvage entries in README, docs index, rules index,
  workflow index, architecture, glossary, and PIP index files.
- `pip/concepts/` as a PIP Knowledge Base category.
- Roadmap2 salvage candidate files for Concept, CASE, Best Practice,
  Evolution, Investigation, and Rule Story entries.
- PIP Case Index and Tagging Standard updates for Knowledge Salvage and
  Concept candidates.

### Reason

Roadmap2 still functioned as an external review source for reusable GDS / PIP
knowledge. To make GDS the single active Knowledge Base, remaining Roadmap2
knowledge needed a formal salvage loop instead of ad hoc review.

The loop prevents reusable knowledge from being lost in reviews, chats, or
external roadmap archives. It also separates documentation salvage from new
feature approval.

### Evolution

Knowledge Base evolved from storing PIP master documents into actively
extracting the remaining Roadmap2 knowledge until no missing reusable knowledge
remains.

Roadmap2 can become history only after remaining reusable knowledge is migrated,
classified as duplicate, classified as future candidate, or rejected as
non-reusable with review evidence.

## Ver1.17

### Added

- Concept Promotion Workflow.
- Concept status definitions: Candidate, Under Review, Experiment, Validated,
  Promoted, and Archived.
- Promotion criteria and archive criteria for `pip/concepts/`.
- PIP Case Knowledge Base rule updates for Concept Lifecycle.
- README, docs index, workflow index, PIP README, glossary, and architecture
  links for Concept Promotion.
- PIP Tagging Standard lifecycle values for concept review states.

### Reason

Roadmap2 Knowledge Salvage introduced `pip/concepts/`, but the concept folder
needed a lifecycle. Without status, promotion criteria, and archive criteria,
concepts could become loose notes instead of reviewed knowledge.

### Evolution

PIP evolved from preserving concept candidates into managing them through a
reviewed lifecycle. Concepts can now become stronger knowledge units such as
Rule, Best Practice, Workflow, Principle, CASE, Rule Story, Evolution,
Investigation, template, glossary, or architecture, or they can be archived
with a reason.

## Ver1.18

### Added

- Concept Template: `pip/templates/concept_template.md`.
- Concept Status Change Report Template:
  `pip/templates/concept_status_change_report_template.md`.
- Concept Review Checklist: `pip/templates/concept_review_checklist.md`.
- README, docs index, workflow index, PIP README, concepts README, tagging
  standard, and PIP Case Knowledge Base rule links for Concept operation
  templates.

### Reason

Concept Promotion Workflow defined statuses and promotion / archive criteria,
but the daily operation still needed standard artifacts for writing individual
concepts, recording status changes, and reviewing promotion or archive
decisions.

### Evolution

Concept management evolved from lifecycle definition into a repeatable artifact
set. New concepts can now be written consistently, status changes can be traced,
and promotion or archive decisions can be reviewed from a standard checklist.

## Ver1.19

### Added

- Concept ID Naming Rules: `docs/rules/concept_id_naming_rules.md`.
- Concept Index: `pip/concepts/concept_index.md`.
- `CONCEPT-YYYY-NNN` official ID format and `C-YYYY-NNN` short form.
- Concept Index status sections for Candidate, Under Review, Experiment,
  Validated, Promoted, and Archived.
- Promoted destination tracking and archive reason tracking.
- README, docs index, rules index, workflow, PIP README, concepts README,
  tagging standard, Concept Template, and Concept Status Change Report updates
  for Concept IDs and Concept Index.

### Reason

Concept templates and status reports made individual operation possible, but
Concepts still needed a stable ID and index standard before many Roadmap2
Salvage concepts are added.

### Evolution

Concept management evolved from file-level templates into indexed knowledge
management. Concepts can now be found by ID, grouped by status, and traced after
promotion or archive.

## Ver1.20

### Added

- Initial Roadmap2-derived core Concept entries:
  `CONCEPT-2026-001` through `CONCEPT-2026-012`.
- Concept Index registration for 12 Validated concepts.
- Related CASE, rule, workflow, source, last reviewed date, and next action for
  each initial core Concept.
- Initial core Concept references in README, docs index, PIP README, and
  concepts README.

### Reason

The Concept management system needed initial real data from Roadmap2 to prove
that lifecycle, templates, ID naming, and Concept Index can support reusable GDS
design philosophy.

### Evolution

Concept management evolved from structure-only documentation into an active
Knowledge Base containing validated Roadmap2 design concepts.

## Ver1.21

### Added

- Roadmap2 final review follow-up integration.
- `CONCEPT-2026-013`: Evidence Driven Development.
- `CONCEPT-2026-014`: Negative Knowledge.
- Related Concept links from First Broken Step and Pipeline Traceability.
- Investigation Pattern Template:
  `pip/templates/investigation_pattern_template.md`.
- `CASE-0008`: Steam OCR Root Cause Investigation.
- Knowledge Classification Rule for Concept, PIP, CASE, Investigation, and
  Negative Knowledge.
- README, docs index, PIP README, Concept Index, CASE Index, and folder README
  links for the follow-up knowledge.

### Reason

Roadmap2 final review found additional reusable knowledge after migration was
judged mostly complete. The remaining items needed to be placed into normal GDS
operation rather than treated as another salvage loop.

### Evolution

GDS Knowledge Base evolved from Roadmap2 salvage into normal reusable knowledge
operation. Final review knowledge is now classified into Concepts, CASE, and
Investigation templates with negative knowledge preserved where useful.

## Ver1.22

### Added

- First Broken Step Methodology:
  `docs/workflow/first_broken_step_methodology.md`.
- Workflow integration from Debug Escalation Ladder to First Broken Step
  Methodology.
- Rule integration in Debug Escalation Ladder Rules.
- Related Concept linkage for `CONCEPT-2026-002`.
- Related CASE linkage for `CASE-0008`.
- README, docs index, PIP README, Concept Index, and Case Index links.

### Reason

Roadmap2 proved that repeated tuning is weaker than tracing the pipeline to the
first broken step before confirming root cause and applying a fix.

### Evolution

GDS debugging methodology evolved from escalation order into a reusable method
for finding the exact first failing stage across OCR, import, API, parser,
database, UI, and AI pipelines.

## Ver1.23

### Added

- Startup Checklist Rules:
  `docs/rules/startup_checklist_rules.md`.
- Startup Checklist Workflow:
  `docs/workflow/startup_checklist_workflow.md`.
- Startup Checklist Template:
  `templates/startup_checklist_template.md`.
- Startup Checklist Examples:
  `examples/startup_checklist_examples.md`.
- README, Knowledge Base Index, rules index, workflow index, architecture, and
  glossary links for Startup Checklist.

### Reason

GDS has accumulated rules, workflows, methodologies, Q artifact standards, PIP
knowledge, and commit safety practices. In long-running development, the risk is
not only missing knowledge, but failing to recall the right knowledge at the
moment a new AI session, review, or Q execution starts.

### Evolution

Knowledge Base evolved from storing reusable rules into providing a startup
entry point that reminds humans and AI which existing rules, methodologies,
repository boundaries, Q artifacts, and commit policies apply before work
begins.

## Ver1.24

### Added

- Completion Checklist Rules:
  `docs/rules/completion_checklist_rules.md`.
- Completion Checklist Workflow:
  `docs/workflow/completion_checklist_workflow.md`.
- Completion Checklist Template:
  `templates/completion_checklist_template.md`.
- Completion Checklist Examples:
  `examples/completion_checklist_examples.md`.
- Completion Checklist fields in Q, completion report, and review checklist
  templates.
- README, Knowledge Base Index, rules index, workflow index, architecture, and
  glossary links for Completion Checklist.

### Reason

Startup Checklist standardized the beginning of work. GDS also needs a standard
ending check so verification, review, completion report, Improvement Review,
commit, tag, release, next Q, and workspace clean state are not left as vague
chat assumptions.

### Evolution

Knowledge Base evolved from startup confirmation into a paired start/end
control system. Work now has a defined entry check and a defined completion
check before it is treated as finished.

## Ver1.25

### Added

- Repository Root Validation Rules:
  `docs/rules/repository_root_validation_rules.md`.
- Repository Root Validation Workflow:
  `docs/workflow/repository_root_validation_workflow.md`.
- Repository Root Validation Template:
  `templates/repository_root_validation_template.md`.
- Repository Root Validation Examples:
  `examples/repository_root_validation_examples.md`.
- Repository root fields in Startup Checklist, Q template, Review Checklist,
  and Completion Report Template.

### Reason

Repository Information defines where work should happen, but it does not prove
that the current shell is actually inside that repository. Wrong Git roots,
home directories, backup folders, and reference-only repositories can cause
search, review, commit, and repair work to happen in the wrong place.

### Evolution

Startup Checklist evolved from declared repository confirmation into measured
repository confirmation. GDS now checks both the expected Working Repository and
the actual Git root before work begins.

## Ver1.26

### Added

- AI Proactive Proposal Rules:
  `docs/rules/ai_proactive_proposal_rules.md`.
- AI Proactive Proposal Examples:
  `examples/ai_proactive_proposal_examples.md`.
- AI Collaboration Rule updates for proactive proposals.
- Startup Checklist and review template fields for better approach, time
  saving, repository / scope concern, rule conflict, methodology conflict,
  maintenance risk, and knowledge opportunity.

### Reason

Long-running GDS work benefits when AI can raise evidence-based concerns and
better options before costly implementation. Without a rule, helpful AI
observations may remain unstated, or worse, may be silently applied as scope
changes.

### Evolution

AI collaboration evolved from instruction execution into human-led proposal
collaboration: AI may surface evidence-based options and concerns, while the
user keeps final judgment and implementation authority.

## Ver1.27

### Added

- Collaborative Decision Workflow:
  `docs/workflow/collaborative_decision_workflow.md`.
- Collaborative Decision Template:
  `templates/collaborative_decision_template.md`.
- Collaborative Decision Examples:
  `examples/collaborative_decision_examples.md`.
- Decision Template fields for AI Proposal, User Proposal, Discussion Summary,
  Evidence Reviewed, Knowledge Classification, Documentation Target, and
  Follow-up Q.
- README, Knowledge Base Index, Workflow Index, Architecture, Glossary, and AI
  Collaboration links for Collaborative Decision.

### Reason

AI Proactive Proposal lets AI raise evidence-based options and concerns, but
GDS also needs a standard path for turning AI proposals and user proposals into
discussed, evidence-reviewed, classified decisions.

### Evolution

AI collaboration evolved from proactive proposal into collaborative decision
making. Disagreement and alternative classification can now become durable
knowledge through discussion, evidence review, knowledge classification, and
documentation.

## Ver1.28

### Added

- Knowledge Poka-Yoke / Design For Forgetfulness as a core principle.
- Design philosophy guidance for making forgetting safe.
- README and Knowledge Base Index entries for Knowledge Poka-Yoke.
- Rule index and rule summary links from `rules.md` and `rules/README.md`.
- Workflow guidance for turning memory-dependent steps into checklist,
  template, validation, artifact, review, or automation controls.
- Glossary entry for Knowledge Poka-Yoke.

### Reason

GDS has added Startup Checklist, Completion Checklist, Repository Root
Validation, Q Artifact, Completion Report, AI Proactive Proposal, and
Collaborative Decision. These are not separate conveniences; they share one
principle: people forget, AI forgets, and processes drift.

The Knowledge Base needed to state that forgetting is a design condition, not a
personal failure. Long-running human / AI development should make important
steps visible, checkable, reviewable, and eventually automatable when safe.

### Evolution

Knowledge Base evolved from individual safeguards into a unified
forgetfulness-safe design philosophy. Repeated omissions, repository mistakes,
copy loss, missing artifacts, skipped verification, and drift-prone handoffs
can now be promoted into explicit controls instead of relying on memory.

## Ver1.29

### Added

- AI Repository Knowledge Access Index:
  `docs/ai_repository_index.md`.
- External Source Access Rules:
  `docs/rules/external_source_access_rules.md`.
- Raw URL entries for README, roadmap, architecture, rules, workflow,
  templates, examples, glossary, history, PIP, CASE, Concept, and methodology.
- README and Knowledge Base Index entry points for AI repository access.
- Completion Checklist and Completion Report template fields for AI Repository
  Index update review.
- Architecture, glossary, workflow, and rules links for the new access index.

### Reason

GDS Docs is used not only by humans, but also by ChatGPT, Codex, and other AI
systems as a public Knowledge Source. Normal GitHub page URLs may not be
reliably readable by AI tools, while Raw URLs are easier to fetch as source
files.

Without a maintained Raw URL index, AI may rely on stale chat context,
incomplete copy-paste, or missing files.

### Evolution

Knowledge Base evolved from a human-readable documentation set into an
AI-readable public source map. Public repository knowledge can now be reached
through a stable first file, and completion checks can catch missing Raw URL
entries when important public knowledge entry points change.

## Ver1.30

### Added

- AI Repository Index auto-generation script:
  `scripts/generate_ai_repository_index.py`.
- Markdown inventory generation for all repository Markdown files.
- Generated `docs/ai_repository_index.md` with Local Path, GitHub URL, Raw
  URL, Category, Priority, and Generated Timestamp.
- Validation for local path existence, duplicate entries, Markdown inventory
  coverage, and Raw URL formatting.
- Completion Checklist and Completion Report fields for:
  - AI Repository Index regenerated;
  - Validation passed;
  - New Markdown registered.
- External Source Access Rule updates for generation and validation commands.

### Reason

The first AI Repository Knowledge Access Index made public Raw URLs visible,
but a manual index can drift as Markdown files are added, moved, renamed, or
deleted.

Knowledge Poka-Yoke requires the system to make forgetting safe. The index
therefore needs generation and validation, not only human memory.

### Evolution

GDS evolved from a manually maintained AI access index into an auto-generated
repository knowledge map. AI readers can reach current Markdown knowledge more
reliably, and completion checks can verify that new Markdown files are
registered before work is treated as complete.

## Ver1.31

### Added

- GitHub Actions workflow:
  `.github/workflows/ai-repository-index-validation.yml`.
- CI triggers for push, pull request, and manual workflow dispatch.
- CI validation command:
  `python scripts/generate_ai_repository_index.py --validate`.
- CI up-to-date check that regenerates `docs/ai_repository_index.md` and fails
  if the generated file differs from the committed file.
- Completion Checklist and Completion Report fields for:
  - CI passed;
  - AI Repository validation passed;
  - Index up to date.

### Reason

Auto-generation and local validation reduce manual mistakes, but humans can
still forget to run the generator before push or pull request.

The AI Repository Index is an AI knowledge entry point, so drift should be
caught automatically before the repository is treated as healthy.

### Evolution

Knowledge Poka-Yoke evolved from local generation into CI-backed repository
health validation. Missing Markdown registration, stale Raw URL inventory, and
index drift can now fail the workflow instead of relying only on memory.

## Ver1.32

### Added

- Project Profile System:
  `project_profiles/`.
- GameGhost Project Profile:
  `project_profiles/gameghost/`.
- Future placeholders for AnimeGhost and ComicGhost profiles.
- Project Profile reading order for AI:
  GDS shared rules, Target Project Profile, Q File, Startup Checklist.
- Project Profile fields in Q file and completion report templates.
- Project Rules and Responsibility Boundary integration for Project Profiles.

### Reason

GDS shared rules apply across projects, but GameGhost, AnimeGhost, ComicGhost,
and future projects need project-specific repository, scope, workflow,
completion, and AI context.

Without a separate Project Profile, AI may mix GDS shared rules with a child
project's production repository, runtime ownership, or completion policy.

### Evolution

GDS evolved from Project First declarations into reusable project-specific
profiles. AI can now read shared GDS rules first, then the target project's
profile, then the current Q, reducing repository confusion and scope drift.

## Ver1.33

### Added

- AI Startup Procedure Rules:
  `docs/rules/ai_startup_procedure_rules.md`.
- AI Startup Procedure Workflow:
  `docs/workflow/ai_startup_procedure.md`.
- Standard AI reading order:
  AI Repository Index, Repository Root Validation, GDS Core Rules / Workflow,
  Target Project Profile, Current Q File, Startup Checklist, Scope / Out of
  Scope, Implementation / Review Start.
- Startup Checklist template fields for AI Repository Index, Project Profile,
  Core Rules / Workflow, Current Q File, Scope / Out of Scope, and Session
  Health.
- Q file and completion report template fields for AI Startup Procedure.
- README, Knowledge Base Index, rules index, workflow index, Project Profiles,
  and architecture links for AI Startup Procedure.

### Reason

Project Profiles separated GDS shared rules from project-specific context, and
AI Repository Index made public knowledge easier to read. The next risk was
that AI might read the right documents in the wrong order, skip Project
Profile, or begin work before validating the actual repository root.

### Evolution

GDS evolved from having separate startup safeguards into a single ordered
startup procedure. AI now has a standard beginning path that reduces repository
confusion, scope drift, Q artifact omissions, and Project Profile reading
misses before implementation or review begins.

## Ver1.34

### Added

- AI Daily Operation Cycle workflow:
  `docs/workflow/ai_daily_operation_cycle.md`.
- Standard operating cycle:
  AI Startup Procedure, Current Q Review, Implementation, Verification, Human
  Review, Completion Checklist, Commit / Push, Knowledge Update, Repository
  Update, Next Q Planning, and Next Startup.
- README, Knowledge Base Index, Workflow Index, Rules Index, Q Template, and
  Completion Report Template links for the daily cycle.
- Workflow Rules integration describing AI Daily Operation Cycle as the outer
  loop for recurring AI-assisted GDS work.

### Reason

GDS had startup checks, completion checks, Project Profiles, AI Repository
Index, Knowledge Poka-Yoke, AI Proactive Proposal, and Collaborative Decision,
but they still needed to be connected as one repeatable operating model.

Without a shared daily cycle, AI and humans may start correctly and finish
correctly, but fail to connect verification, review, knowledge update,
repository update, and next Q planning.

### Evolution

GDS evolved from individual safeguards into a continuous operation cycle. Each
task can now begin from AI Startup Procedure, complete through Completion
Checklist, update reusable knowledge, refresh repository entry points, and feed
the next Q back into the next startup.

## Ver1.35

### Added

- Daily Operation Checklist Template:
  `templates/daily_operation_checklist_template.md`.
- Checklist sections for AI Startup Procedure, Current Q Review,
  Implementation, Verification, Human Review, Completion Checklist, Commit /
  Push, Knowledge Update, Repository Update, Next Q Planning, and Next Startup.
- Completion Report Template fields for Daily Operation Checklist usage and
  artifact path.
- README, Knowledge Base Index, Workflow, and Template Index links for the
  checklist template.

### Reason

AI Daily Operation Cycle defined the operating loop, but daily work still
needed a concrete checklist artifact so humans and AI can confirm every phase
without relying on memory.

### Evolution

GDS evolved from a documented operation cycle into a checkable daily operation
artifact. The full cycle can now be recorded, reviewed, attached to completion
evidence, and reused by the next startup.

## Ver1.36

### Added

- GDS Health folder:
  `docs/health/`.
- GDS Health Dashboard:
  `docs/health/gds_health_dashboard.md`.
- Health areas for Repository Health, Knowledge Health, Rule Coverage,
  Workflow Coverage, Template Coverage, Example Coverage, Automation Coverage,
  CI Status, and Project Profile Coverage.
- README, Knowledge Base Index, Workflow Index, Template Index, Daily
  Operation Checklist, and Completion Report links for GDS Health.

### Reason

GDS had moved from creating individual rules and workflows into daily
operation. The next need was visibility: humans and AI need to see which parts
of the system are healthy, which are usable but need follow-up, and which
should block or trigger review.

### Evolution

GDS evolved from checklists and cycles into observable operations. Health is
now treated as early discovery and continuous improvement support, not as
blame or final quality scoring.

## Ver1.37

### Added

- GDS Health Update Workflow:
  `docs/workflow/gds_health_update_workflow.md`.
- Health update timing for rule, workflow, template, example, project profile,
  CI, automation, major release, and monthly review changes.
- Standard Health update procedure:
  identify affected area, review dashboard state, update Green / Yellow / Red
  status, update Current State, Target State, Notes, record improvement
  candidate, and reflect in Completion Report.
- Completion Report Template fields for GDS Health review, affected areas,
  status changes, improvement candidates, and Recommended Next Q.
- Daily Operation Checklist fields for affected health areas and update
  workflow confirmation.

### Reason

The GDS Health Dashboard made state visible, but its maintenance timing and
update method were not yet standardized.

Without an update workflow, Health could become a one-time dashboard instead of
a continuous improvement practice.

### Evolution

GDS Health evolved from a visible dashboard into a maintained operating loop.
Health can now be reviewed and updated when the Knowledge Base changes, then
reported through completion evidence.

## Ver1.38

### Added

- GDS Health validation script:
  `scripts/validate_gds_health.py`.
- Local validation for Health Dashboard existence, required Health areas,
  `Green` / `Yellow` / `Red` status values, required table fields, AI
  Repository Index registration, Workflow links, and README links.
- GDS Health validation command in README, Health README, Health Dashboard,
  and Health Update Workflow.
- Completion Report and Completion Checklist fields for GDS Health validation.

### Reason

GDS Health Dashboard and GDS Health Update Workflow made Health visible and
maintainable, but the repository still needed a mechanical guard against
missing areas, invalid statuses, blank Health fields, and broken entry-point
links.

### Evolution

GDS Health evolved from maintained documentation into checkable operational
health. Health state can now be reviewed by humans and validated by scripts,
preparing the path for CI-backed Health checks.

## Ver1.39

### Added

- UTF-8 Read Rule:
  `docs/rules/utf8_read_rules.md`.
- Mojibake Audit Report:
  `docs/history/mojibake_audit_report_2026-07-10.md`.
- AI Startup Procedure guidance for reading Japanese Q files with
  `Get-Content -Encoding UTF8` on Windows PowerShell 5.1.
- Q File Template, Startup Checklist Template, and Completion Report Template
  fields for UTF-8 read verification and mojibake reporting.

### Reason

Recent Q files were valid UTF-8, but plain Windows PowerShell 5.1
`Get-Content` displayed Japanese text as mojibake. That created false reports
that the Q file body was partially corrupted.

GDS needed a rule that separates file corruption from terminal display or
encoding-read problems.

### Evolution

Knowledge Poka-Yoke now covers text encoding reads. AI and humans can verify
Japanese Q files with explicit UTF-8 before reporting mojibake, and repository
Markdown mojibake audits can be recorded without unsafe bulk conversion.

## Ver1.40

### Added

- Repository Quality Audit script:
  `scripts/repository_quality_audit.py`.
- Repository Quality Audit Workflow:
  `docs/workflow/repository_quality_audit_workflow.md`.
- Repository Quality Report:
  `reports/repository_quality_report.md`.
- Completion Checklist and Completion Report fields for Repository Quality
  Audit result, report path, overall health, warning count, and error count.

### Reason

GDS had multiple separate validation points: AI Repository Index validation,
GDS Health validation, UTF-8 reading rules, and mojibake audit practice.

As validation grows, humans and AI need one entry point that answers whether
the repository is healthy enough for daily operation, review, release
readiness, or future CI promotion.

### Evolution

Repository quality evolved from individual checks into a single audit command
and report. The system can now surface UTF-8, mojibake, index, health, link,
README, history, project profile, and Markdown structure findings in one place
without treating warnings as blame.

## Ver1.41

### Added

- Japanese Documentation Localization Workflow:
  `docs/workflow/japanese_documentation_localization_workflow.md`.
- Japanese Documentation Localization Report:
  `reports/japanese_documentation_localization_report.md`.
- Language Rules update for documentation localization scope, English keep
  cases, and candidate classification.

### Reason

GDS Docs is Japanese-first, but newly added reports and workflows can still
contain English explanatory text. Human Approval requires that humans can read
the purpose, background, scope, result, and review guidance in Japanese.

### Evolution

Japanese First evolved from a general language rule into a localization
workflow. GDS can now distinguish explanation text that should be Japanese
from commands, paths, URLs, identifiers, status values, and external technical
terms that should remain English.

## Ver1.42

### Added

- Repository Quality Report generator localization.
- Japanese output messages in `scripts/repository_quality_audit.py`.
- Language Rules update for generated documentation output.
- Repository Quality Audit Workflow note that generated reports are Japanese-first.

### Reason

`reports/repository_quality_report.md` had been localized manually, but the
generator still contained English fixed strings. Re-running the audit could
return the report to mixed-language output and require manual translation.

Manual translation after generation is fragile and does not satisfy Knowledge
Poka-Yoke. Generated documentation should be usable as-is.

### Evolution

Japanese First evolved from document editing guidance into generator output
quality. Repository Quality Audit can now produce a Japanese-first report
directly, while preserving commands, paths, status values, and identifiers for
compatibility.

## Ver1.43

### Added

- H1 headings for existing template files that previously started without a
  top-level Markdown heading.
- Repository Quality Audit warning resolution for template Markdown structure.

### Reason

Repository Quality Audit reported one remaining warning: ten legacy templates
did not have H1 headings. The templates were usable, but they did not satisfy
the repository-wide Markdown structure check.

### Evolution

Template structure moved closer to the repository quality standard without
rewriting template content. Repository Quality Audit can now evaluate template
Markdown structure without known legacy H1 exceptions.

## Ver1.44

### Added

- Ghost Development System Roadmap Ver2 Platform Era.
- Foundation Era completed status.
- Platform Integration Era.
- Automation Server Era.
- Ghost Ecosystem Era.
- Continuous Improvement Era.
- Innovation Pipeline roadmap candidate.
- New Core Principle candidates:
  Silent Operation Principle, Platform First, Reuse Before Rebuild, and
  Innovation Pipeline.

### Reason

GDS Foundation v1 completed with Rules, Workflow, Knowledge Base, AI Repository
Index, Project Profile, AI Startup Procedure, Daily Operation, Health,
Repository Quality Audit, UTF-8 Read Rule, Localization, Validation, and
Template Standardization.

The roadmap needed to move from foundation construction to platform usage,
integration, automation candidates, and multi-project Ghost Ecosystem direction.

### Evolution

GDS evolved from a documentation foundation into a platform roadmap. Future work
now has a clearer path from Platform Integration to Automation Server, Ghost
Ecosystem, Continuous Improvement, and Innovation Pipeline promotion.

## Update Notes

この文書は詳細な Decision Log ではありません。

重要 decision の詳細な選択肢、却下理由、承認経緯が必要な場合は、別途 Decision
Log または ADR を作成します。
