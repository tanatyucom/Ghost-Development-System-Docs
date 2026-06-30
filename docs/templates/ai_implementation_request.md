# AI Implementation Request

If the implementation request is prepared as a Q file, prefer:

```text
docs/templates/q_file_template.md
```

Q files should be Japanese-first so future human review remains easy.
Proper nouns, commands, file names, paths, and identifiers may remain in
English.

Workflow Version:

- Use `docs/workflow/development_workflow_v2_trial.md` when the task is part of
  the Ver1.4 workflow trial.
- Rules take precedence over the trial workflow and over this request.

Read documents in the following order:

1. `docs/rules/`
2. `docs/workflow/development_cycle.md`
3. `docs/workflow/development_workflow.md`
4. `docs/status/current_focus.md`
5. `<Implementation Specification>`

Implement according to the Specification.

Do not implement features outside the Scope.

After implementation report:

- Changed Files
- Verification
- Remaining Issues
- Current Focus updates
- Retrospective notes
- Suggested Commit Message

Do not commit.

Wait for review.
