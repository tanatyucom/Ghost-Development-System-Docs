# AI Implementation Request

Use this template when asking AI to implement or update project artifacts.

If the request is prepared as a Q file, prefer:

```text
docs/templates/q_file_template.md
```

## Read First

Read documents in this order:

1. `docs/rules/`
2. `docs/roadmap/`
3. `docs/workflow/`
4. related templates
5. the target specification or Q file

Rules take precedence over workflow drafts, roadmap, templates, and Queue
items.

## Output Format

For reusable, reviewable, or Git-managed requests, prepare the request as a
file artifact instead of relying on the chat body.

Standard formats:

- Markdown `.md`
- Word `.docx`

Markdown is required for Git-managed work and AI handoff. `.docx` is required
when human review, comments, approval, or offline reading is expected.

When an artifact is authoritative, the chat response should contain only a
summary, artifact path or link, verification notes, and remaining issues.

## Task Artifact Workspace

When the request is a Q artifact, use the workspace path defined by the Q.

Confirm:

- Target Project folder.
- Status folder.
- Artifact Workspace path.
- Source Q path.
- Related Completion Report path.
- Output artifacts.
- Related Commit placeholder.

If the Q is approved for execution, it should be in the `approved` workspace.
After work is completed and reviewed, the completion report should be stored
beside the source Q.

## Repository Information

Before editing, identify and follow the Repository Information in the Q file or
request.

Confirm:

- Target Project.
- Repository.
- Working Directory.
- Documentation Root.
- Runtime Root, if runtime work is explicitly in scope.
- Single Source of Truth.
- Related Repository boundaries.
- Cross Project Impact.
- Scope Guard.

If Repository Information is missing or conflicts with the requested work, stop
and clarify before editing files.

## Language

Ghost Development System Docs uses Japanese-first documentation.

Human-facing purpose, scope, review, completion, and approval text should be
written in Japanese by default. Code, APIs, identifiers, filenames, paths, Git
commands, and commit messages may remain in English.

## Scope

Implement only the accepted scope.

Do not implement Future Candidates unless the request explicitly promotes them
to current scope.

## Naming Policy

When creating or renaming roadmap items, Q titles, architecture topics, or
public knowledge base concepts, prefer purpose-oriented names.

Use implementation terms in descriptions when they clarify the current method,
but avoid making a single method the public title when the project goal is
broader.

## Human Approval Gate

Stop and ask for approval before:

- destructive changes;
- Git migration;
- release creation;
- GitHub Actions changes;
- runtime implementation outside the request;
- architecture changes that exceed the accepted scope;
- commits when the request says not to commit.

## Documentation-Only Requests

For documentation-only requests:

- update Markdown only;
- edit only the repository and documentation root listed in Repository
  Information;
- do not change runtime code;
- do not run migrations;
- do not create releases;
- do not sync other repositories;
- do not commit unless explicitly requested.

## Report After Work

Report:

- Changed Files.
- Summary.
- Verification.
- Source Q path.
- Artifact Workspace path.
- Output artifacts.
- Dirty workspace detected?
- Unrelated files?
- Suggested restore commands.
- Safe commit set.
- Metrics / Evidence, when measurable results are available.
- Repository Information followed.
- Remaining Issues.
- Recommended Improvements.
- Future Candidates.
- Future Candidate Proposals.
- Recommended Next Q.
- Suggested Commit Message.

## Improvement Review

After completing the accepted scope, review whether the work revealed reusable
knowledge that should improve:

- Documentation.
- Templates.
- Workflow.
- Roadmap.
- Rules.
- Architecture.
- Knowledge Base.
- Metrics / Evidence.

Separate output into:

- Recommended: high-value improvements suitable for near-term adoption.
- Future Candidates: useful ideas that should remain future work.

Knowledge evolves through implementation. Reusable knowledge should be promoted
to templates, rules, examples, or documentation whenever practical.

## Goal

AI should produce reviewable work that improves the project without expanding
scope or relying on hidden assumptions.
