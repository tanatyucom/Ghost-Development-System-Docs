# Templates

## Purpose

This folder contains reusable templates for Ghost Development System Docs.

Templates help humans and AI create consistent Q files, specifications, reviews,
reports, roadmap items, and release documents.

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
- easier to review;
- easier for AI to execute without guessing;
- better at naming public roadmap items by purpose rather than by a single
  implementation method;
- better at separating approved scope from Future Candidates.

## Improvement Review

Every Q file, implementation request, review, and completion report should
include an Improvement Review.

Improvement Review asks whether the completed work revealed reusable knowledge
that should improve:

- Documentation.
- Templates.
- Workflow.
- Roadmap.
- Rules.
- Architecture.
- Knowledge Base.

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

Q files should state naming policy when a request renames roadmap items,
architecture topics, templates, or public knowledge base concepts.

Q files should also include Repository Information near the top of the request.
This prevents AI from confusing the active repository, documentation root,
runtime root, source of truth, or related repositories.

Recommended Repository Information fields:

- Repository.
- Working Directory.
- Documentation Root.
- Runtime Root, only when needed.
- Single Source of Truth.
- Related Repository, when another repository may be referenced.
- Scope Guard.

For documentation-only work, the Scope Guard should explicitly say which docs
folder may be edited and which runtime or related repositories must remain
reference-only.

Japanese-first Q files are recommended when the project owner reviews requests
in Japanese. Proper nouns, commands, paths, filenames, identifiers, and commit
messages may remain in English.

## Update Policy

When a real Q reveals a reusable pattern, update the related template as part of
the same documentation review when it is in scope.

Do not add one-off request details to templates. Add only reusable structure.
