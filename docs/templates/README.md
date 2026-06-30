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
- better at separating approved scope from Future Candidates.

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

Japanese-first Q files are recommended when the project owner reviews requests
in Japanese. Proper nouns, commands, paths, filenames, identifiers, and commit
messages may remain in English.

## Update Policy

When a real Q reveals a reusable pattern, update the related template as part of
the same documentation review when it is in scope.

Do not add one-off request details to templates. Add only reusable structure.
