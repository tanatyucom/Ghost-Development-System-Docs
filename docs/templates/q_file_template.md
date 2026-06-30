# Q File Template

Status:

Workflow:

Category:

Priority:

Commit:

```text
Do not commit unless explicitly requested. Provide a suggested commit message
instead.
```

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

## Review Requests

Ask for review perspectives.

Examples:

- long-term maintainability;
- AI collaboration quality;
- public knowledge base clarity;
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
- Future Candidate Proposals.
- Recommended Next Q.
- Suggested Commit Message.

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
