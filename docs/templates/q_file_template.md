# Q File Template

Version:

Status:

Workflow:

Category:

Priority:

Commit:

```text
Do not commit unless explicitly requested. Provide a suggested commit message
instead.
```

## Repository Information

Define the repository and edit boundaries before describing the task.

### Repository

Repository name.

Example:

```text
Ghost-Development-System-Docs
```

### Working Directory

Absolute path to the repository root that AI should treat as the working
directory.

Example:

```text
C:\GitHub\Ghost-Development-System-Docs
```

### Documentation Root

Absolute path to the documentation root when the task is documentation-related.

Example:

```text
C:\GitHub\Ghost-Development-System-Docs\docs
```

### Runtime Root

Use only when runtime implementation is explicitly in scope.

For documentation-only work, write:

```text
Not in scope.
```

### Single Source Of Truth

Repository or document set that should be treated as authoritative for this Q.

Example:

```text
Ghost-Development-System-Docs
```

### Related Repository

Optional repository that may be referenced but should not be edited unless
explicitly listed in scope.

Example:

```text
GameGhost: reference only. Do not update, sync, or copy files.
```

### Scope Guard

State the hard edit boundary.

Examples:

- Edit only `Ghost-Development-System-Docs/docs`.
- Treat GameGhost as reference only.
- Do not update files outside the listed target repository.
- Do not sync changes to related repositories.

## Purpose

Describe what this Q should achieve.

Write the goal so a human can understand the expected result without private
context.

## Background

Explain why this Q is needed.

Include related roadmap review, decision, queue item, current focus, or previous
work if relevant.

## Approved Decisions

List decisions that are already approved.

Unapproved ideas should be placed in Review Requests or Future Candidates, not
here.

## Naming Policy

Describe any naming rules that apply to this Q.

Recommended default:

- Prefer purpose-oriented names for roadmap items, Q titles, and public
  knowledge base topics.
- Use implementation names in descriptions only when they clarify the current
  target or method.
- Keep legacy or implementation-specific names as Current Target, Current
  Implementation, or Background when they remain useful.

## Scope

Describe the work that is included in this Q.

Examples:

- Documentation update only.
- Roadmap review only.
- Template update only.
- Rules review only.

## Do

List concrete work items.

Examples:

- Update `docs/roadmap/roadmap.md`.
- Review `docs/rules/`.
- Improve `docs/templates/q_file_template.md`.
- Align README purpose, scope, and repository structure.

## Do Not

List out-of-scope items explicitly.

Examples:

- Do not change runtime code.
- Do not run Git migration.
- Do not update GitHub Actions.
- Do not create a release.
- Do not sync another repository.
- Do not commit.
- Do not implement Future Candidates.

## Target Files

List expected files or folders.

Examples:

- `README.md`
- `docs/roadmap/`
- `docs/rules/`
- `docs/templates/`

## Completion Criteria

Define concrete conditions for completion.

Examples:

- Only files under `docs/` are updated.
- Runtime Code is not changed.
- Git Migration is not performed.
- Commit is not created.
- Related repositories are not updated, synced, or copied.
- Updated templates are delivered.
- Changed files and summary are reported.
- Remaining Issues, improvement proposals, Recommended Next Q, and Suggested
  Commit Message are included.

## Review Requests

Ask for review perspectives.

Examples:

- long-term maintainability;
- AI collaboration quality;
- public knowledge base clarity;
- purpose-oriented naming;
- responsibility boundaries;
- roadmap consistency;
- workflow fit;
- template reusability.

## Future Candidates

List ideas that should be considered later but not implemented in this Q.

Examples:

- Development Knowledge Platform.
- Development Knowledge DB.
- Dependency Index.
- Universal Project Search.
- DB Impact Analyzer.
- Documentation Impact Analyzer.
- Architecture Viewer.
- Rename Compatibility Analyzer.

## Acceptance Criteria

Define completion conditions.

Examples:

- Target documents are updated.
- Scope and non-scope are respected.
- Repository Information is complete enough to prevent repository or edit-target
  confusion.
- Public names describe purpose before implementation technique.
- Future Candidates remain separate from approved work.
- Rules, roadmap, templates, and README are consistent.
- Commit is not created when the Q says not to commit.

## Deliverables

Request the final report format.

Recommended:

- Changed Files.
- Summary.
- Verification.
- Remaining Issues.
- Recommended Improvements.
- Future Candidates.
- Future Candidate Proposals.
- Recommended Next Q.
- Suggested Commit Message.

## Improvement Review

Review the completed work and propose improvements for:

- Documentation.
- Templates.
- Workflow.
- Roadmap.
- Rules.
- Architecture.
- Knowledge Base.

### Recommended

List high-value improvements suitable for near-term adoption.

### Future Candidates

List interesting ideas that should remain future work.

## Suggested Commit Message

```text
docs: update ghost development system knowledge base
```

## Writing Notes

- Japanese-first Q files are recommended for human review when the project
  owner works primarily in Japanese.
- Proper nouns, commands, paths, filenames, identifiers, and commit messages may
  remain in English.
- Keep Future Candidates separate from approved work.
- Make out-of-scope items explicit to prevent scope drift.
- Put Repository Information near the top of each Q so AI can confirm the
  working directory, documentation root, source of truth, and related repository
  boundaries before editing.
- Knowledge evolves through implementation.
- Reusable knowledge should be promoted to templates, rules, examples, or
  documentation whenever practical.
