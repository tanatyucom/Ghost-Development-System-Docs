# Templates

## Purpose

This folder contains reusable templates for Ghost Development System Docs.

Templates help humans and AI create consistent Q files, specifications, reviews,
reports, roadmap items, and release documents.

Templates also define when reusable outputs should be generated as file
artifacts instead of being delivered only in chat.

Q-related templates use the Task Artifact Workspace standard for request,
completion report, notes, attachments, status movement, and related commit
tracking.

Completion and review templates also include dirty workspace and commit safety
fields so unrelated files, restore suggestions, and safe commit sets are
visible before commit.

## Contains

### Planning

- `roadmap_template.md`
- `queue_template.md`
- `decision_template.md`

### Development

- `specification_template.md`
- `architecture_template.md`
- `feature_template.md`
- `bugfix_template.md`
- `refactoring_template.md`

### AI Collaboration

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
- better at separating approved scope from Future Candidates.

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

- `docs/templates/q_file_template.md`
- `docs/templates/review_checklist.md`
- `docs/templates/completion_report_template.md`
- `docs/requests/README.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/git_rules.md`
- `docs/workflow/commit_safety_checklist.md`
- `docs/rules/project_rules.md`
- `docs/rules/language_rules.md`
- `docs/workflow/README.md`
