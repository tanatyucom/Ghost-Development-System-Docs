# Output Policy

**Version:** 1.3

**Last Updated:** 2026-07-05

## Purpose

This document defines when Ghost Development System work should be delivered in
chat and when it should be generated as a file artifact.

It supports Artifact First by preventing long reusable content from becoming
trapped in chat.

## Core Decision

Use chat for short, temporary conversation.

Use a file artifact for reusable, reviewable, AI-handoff, or Git-managed
content.

For Q files, file artifact means saved in the Task Artifact Workspace under
`docs/requests/`, not only generated in chat, a download folder, or a temporary
sandbox path.

Debug artifacts are not automatically authoritative output artifacts. They are
development-time evidence used for review. Generate them only in Debug Mode,
announce their paths in the completion report when relevant, and do not commit
them unless a Q explicitly promotes them to Git-managed knowledge.

## Output Decision Table

| Output Type | Default Output |
|---|---|
| Short consultation | Chat |
| Clarification question | Chat |
| Status update | Chat |
| Long Q | Artifact |
| Design document | Artifact |
| Specification | Artifact |
| Review request | Artifact |
| Codex request | Artifact |
| Gemini request | Artifact |
| Claude request | Artifact |
| AI implementation request | Artifact |
| Roadmap update proposal | Artifact |
| Human approval packet | Artifact |
| Git-managed documentation | Artifact |
| Debug overlay / intermediate evidence | Debug artifact, not chat |

## Artifact Format Policy

Standard artifact formats:

- Markdown `.md`
- Word `.docx`

Use Markdown `.md` when:

- the artifact should be stored in Git;
- another AI should consume it;
- a reviewer needs stable headings and checklists;
- the document should remain diffable.

Use Word `.docx` when:

- human review is expected;
- comments, redlines, or approval review are expected;
- the artifact should be shared outside a Git workflow;
- offline reading is likely.

Use PDF, CSV, XLSX, or PPTX only when the content requires that format.

## Chat Body Policy

When the authoritative output is an artifact, the chat body should contain:

- short purpose summary;
- generated artifact paths or links;
- changed files, when repository files changed;
- verification notes;
- remaining issues, when any.

The chat body should not contain the full long-form Q, design document,
specification, review request, or AI request unless explicitly requested.

When Debug Artifact Review applies, the chat body or completion report should
summarize the debug artifact location and expected normal state. It should not
embed large debug logs, generated overlays, or intermediate data directly in
chat unless explicitly requested.

## Workflow Placement

Artifact generation belongs before implementation or review when the artifact
defines scope.

Recommended flow:

```text
Idea
  -> Q ID Decision
  -> Q Artifact Workspace
  -> Save request.md in docs/requests/
  -> Workspace Save Verification
  -> Approval
  -> Codex / AI Implementation
  -> Completion Report Artifact
  -> Human Review
  -> Commit
  -> Knowledge Promotion
  -> Archive
```

If a chat discussion becomes long, reusable, decision-bearing, or Git-managed,
promote it to a file artifact before continuing.

Q artifacts and completion report artifacts should be saved under
`docs/requests/<project>/<status>/` using the Task Artifact Workspace
standard from `docs/rules/q_file_artifact_standard.md` and Q ID / filename
standard from `docs/rules/q_file_naming_rules.md`.

Implementation should begin only after the source Q has a workspace path and
the chat response or completion report can name that path. The matching
completion report should be saved in the same workspace as `request.md`.

## Failure Modes Prevented

Artifact First prevents:

- truncated chat requests;
- missing copied sections;
- broken Markdown;
- human copy mistakes;
- AI execution from incomplete input;
- weak Git history;
- hard-to-review approval context.
- silent intermediate processing failures;
- accidental debug artifact commits;
- debug output leaking into normal execution.

## Related Documents

- `docs/rules/artifact_first_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_naming_rules.md`
- `docs/rules/q_file_template_rules.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/requests/README.md`
- `templates/Q_TEMPLATE.md`
- `docs/templates/ai_implementation_request.md`
- `docs/examples/artifact_first_examples.md`
- `docs/examples/debug_artifact_review_examples.md`
