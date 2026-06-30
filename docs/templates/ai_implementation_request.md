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

## Repository Information

Before editing, identify and follow the Repository Information in the Q file or
request.

Confirm:

- Repository.
- Working Directory.
- Documentation Root.
- Runtime Root, if runtime work is explicitly in scope.
- Single Source of Truth.
- Related Repository boundaries.
- Scope Guard.

If Repository Information is missing or conflicts with the requested work, stop
and clarify before editing files.

## Scope

Implement only the accepted scope.

Do not implement Future Candidates unless the request explicitly promotes them
to current scope.

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
- Repository Information followed.
- Remaining Issues.
- Future Candidate Proposals.
- Recommended Next Q.
- Suggested Commit Message.

## Goal

AI should produce reviewable work that improves the project without expanding
scope or relying on hidden assumptions.
