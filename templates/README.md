# Templates

## Purpose

This folder contains reusable templates for Ghost Development System Docs.

Templates help humans and AI create consistent Q files, specifications, reviews,
reports, roadmap items, and release documents.

Templates also define when reusable outputs should be generated as file
artifacts instead of being delivered only in chat.

Startup checklist templates help humans and AI confirm repository boundaries,
applicable rules, methodologies, Q artifact status, scope, and commit policy
before implementation or review begins.

Repository root validation templates help confirm the actual Git repository root
matches the expected Working Repository before implementation, review, commit,
tag, or release work begins.

Completion checklist templates help humans and AI confirm verification, review,
completion report, Improvement Review, commit / tag / release decisions,
Recommended Next Q, and workspace clean state before a task is treated as
complete. They also check whether the AI Repository Knowledge Access Index
needs regeneration and validation when public knowledge entry points changed.

Daily operation checklist templates help humans and AI record the whole AI
Daily Operation Cycle from startup through Current Q Review, implementation,
verification, Human Review, Completion Checklist, commit / push, Knowledge
Update, Repository Update, Next Q Planning, and Next Startup.

Multi-AI handoff templates help ChatGPT, Codex, Claude, Gemini, human review,
and other AI contexts transfer Current Status, Current Focus, Scope, Source of
Truth, Changed Files, Verification Results, Remaining Issues, Recommended Next
Q, and Suggested Commit Message without relying on temporary chat memory. The
handoff checklist template reviews whether that artifact is complete enough for
the receiver. Reference examples live in
`examples/multi_ai_handoff_reference_examples.md`.

Information Package templates help AI assistants, humans, and future Command
Center workflows share Project Summary, Current Status, Current Focus, Active
Repository, Related Rules, Related Templates, Recent Decisions, Open Issues,
Recent Artifacts, Recommended Next Q, and Notes without treating chat as the
source of truth.

Health documents such as `docs/health/gds_health_dashboard.md` may be used
beside templates when a task should record GDS operating health rather than
only task completion.

Q-related templates use the Task Artifact Workspace standard for request,
completion report, notes, attachments, status movement, and related commit
tracking.

Completion and review templates also include dirty workspace and commit safety
fields so unrelated files, restore suggestions, and safe commit sets are
visible before commit.

Q, AI implementation, completion report, and Codex review templates also
include Migration First fields so internal architecture changes record
Migration Plan, Reference Update, Legacy Removal, Public Compatibility Impact,
Remaining Legacy, and Restore / Rollback Guidance.

Q, AI implementation, completion report, and Codex review templates also
include Debug Artifact Review fields so AI, OCR, recommendation,
auto-detection, candidate extraction, fuzzy matching, and visual processing
work records Debug Mode, intermediate artifacts, expected normal state, review
viewpoints, AI review targets, and debug artifact Git policy.

When many artifacts are generated, Q, completion report, and Codex review
templates should also carry a Review Entry Point so the reviewer knows where to
start.

Q and completion report templates also include Audit Before Repair fields so
repair work records source audit artifacts, classification, repair scope,
excluded items, remaining candidates, verification, safe commit set, and
restore guidance.

## Contains

### Planning

- `roadmap_template.md`
- `queue_template.md`
- `decision_template.md`
- `innovation_pipeline_template.md`
- `platform_promotion_decision_report_template.md`
- `platform_registry_update_template.md`

### Development

- `specification_template.md`
- `architecture_template.md`
- `feature_template.md`
- `bugfix_template.md`
- `refactoring_template.md`

### AI Collaboration

- `startup_checklist_template.md`
- `daily_operation_checklist_template.md`
- `repository_root_validation_template.md`
- `collaborative_decision_template.md`
- `information_package_template.md`
- `multi_ai_handoff_template.md`
- `multi_ai_handoff_checklist_template.md`
- `completion_checklist_template.md`
- `q_file_template.md`
- `ai_implementation_request.md`
- `codex_review_template.md`
- `review_checklist.md`
- `completion_report_template.md`

### Release

- `release_checklist.md`
- `release_notes_template.md`

## Does NOT Contain

- Runtime code.
- Active Queue state.
- Private project data.
- Release artifacts.

## Template Policy

Templates should be updated when repeated work shows a better standard pattern.

Promote improvements into templates when they help future Q files become:

- clearer;
- safer;
- easier to generate as durable file artifacts;
- easier to review;
- easier for AI to execute without guessing;
- better at naming public roadmap items by purpose rather than by a single
  implementation method;
- better at separating approved scope from Future Candidates;
- better at migrating internal architecture to a new standard without
  accumulating permanent legacy fallback.
- better at reviewing intermediate debug artifacts before code edits or final
  judgment.
- better at keeping public Raw URL entry points available for AI repository
  knowledge access.
- better at handing work off between AI tools without losing repository
  context, scope boundaries, verification results, or next action.
- better at packaging current project state for AI, human review, and future
  Command Center use without replacing repository source-of-truth documents.

## Improvement Review

Every Q file, implementation request, review, and completion report should
include an Improvement Review.

When measurable results are available, reports should also include Metrics /
Evidence. Metrics should identify source, sample or period, interpretation, and
what was not measured.

Improvement Review asks whether the completed work revealed reusable knowledge
that should improve:

- Documentation.
- Templates.
- Workflow.
- Roadmap.
- Rules.
- Architecture.
- Knowledge Base.
- Metrics / Evidence.

Separate proposals into:

- Recommended: high-value improvements suitable for near-term adoption.
- Future Candidates: useful ideas that should remain future work.

Knowledge evolves through implementation. Reusable knowledge should be promoted
to templates, rules, examples, or documentation whenever practical.

## Q Files

`q_file_template.md` is the standard template for reusable Codex request files.

Use it for:

- roadmap review;
- documentation update;
- rules review;
- template update;
- architecture review;
- future DMS-generated fix proposals.

Q files should make scope, non-scope, target files, deliverables, and commit
policy explicit.

Q files should also make Output Format and Required Artifacts explicit.

Default artifact policy:

- Markdown `.md` is required for reusable, AI-handoff, or Git-managed Q files.
- Word `.docx` is required when human review, comments, approval, or offline
  reading is expected.
- Chat should contain the summary and artifact paths or links only when the
  file artifact is authoritative.
- Q artifacts should be saved in Task Artifact Workspaces under
  `docs/requests/<target_project>/<status>/`.
- Full workspaces should use `request.md`, `completion_report.md`, `notes.md`,
  and `attachments/`.
- Simple Q artifacts may use
  `YYYY-MM-DD_<target_project>_<short_title>.md` when a full workspace is not
  needed yet.
- Completion report artifacts should be saved beside the source Q.

Q files should state naming policy when a request renames roadmap items,
architecture topics, templates, or public knowledge base concepts.

Q files should include Migration First fields when they change internal folder
structure, script layout, adapter internal interface, prototype scripts, shared
utility location, artifact workspace layout, queue / request internal
structure, or future GhostCore / GDS internal modules.

Q files should include Debug Artifact Review fields when they involve AI, OCR,
recommendation, auto-detection, candidate extraction, fuzzy matching, visual
overlays, or intermediate processing. They should state whether Debug Mode is
required, where debug artifacts will be saved, what normal should look like,
what viewpoints to review, and whether debug artifacts are excluded from Git.
When many artifacts are expected, Q files should also define the expected
Review Entry Point.

Q files should include Audit Before Repair fields when they request repair,
cleanup, OCR result correction, DB correction, mojibake correction, duplicate
resolution, metadata correction, or other maintenance where audit and
classification should happen before repair.

Q files should also include Repository Information near the top of the request.
This prevents AI from confusing the active repository, documentation root,
runtime root, source of truth, or related repositories.

Recommended Repository Information fields:

- Target Project.
- Repository.
- Working Directory.
- Documentation Root.
- Runtime Root, only when needed.
- Single Source of Truth.
- Related Repository, when another repository may be referenced.
- Cross Project Impact.
- Scope Guard.

For documentation-only work, the Scope Guard should explicitly say which docs
folder may be edited and which runtime or related repositories must remain
reference-only.

Japanese-first Q files are the default for Ghost Development System Docs.
Proper nouns, commands, paths, filenames, identifiers, and commit messages may
remain in English.

## Update Policy

When a real Q reveals a reusable pattern, update the related template as part of
the same documentation review when it is in scope.

Do not add one-off request details to templates. Add only reusable structure.

## Related Documents

- `templates/q_file_template.md`
- `templates/startup_checklist_template.md`
- `templates/daily_operation_checklist_template.md`
- `templates/repository_root_validation_template.md`
- `templates/collaborative_decision_template.md`
- `templates/completion_checklist_template.md`
- `templates/review_checklist.md`
- `templates/completion_report_template.md`
- `templates/codex_review_template.md`
- `docs/ai_repository_index.md`
- `docs/health/gds_health_dashboard.md`
- `docs/rules/external_source_access_rules.md`
- `docs/requests/README.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/audit_before_repair_rules.md`
- `docs/rules/migration_first_rules.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/git_rules.md`
- `docs/workflow/commit_safety_checklist.md`
- `docs/workflow/audit_before_repair_workflow.md`
- `docs/workflow/debug_artifact_review_workflow.md`
- `docs/rules/project_rules.md`
- `docs/rules/language_rules.md`
- `docs/workflow/README.md`
