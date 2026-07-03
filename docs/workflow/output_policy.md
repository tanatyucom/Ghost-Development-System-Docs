# Output Policy

**Version:** 1.1

**Last Updated:** 2026-07-04

## Purpose

This document defines when Ghost Development System work should be delivered in
chat and when it should be generated as a file artifact.

It supports Artifact First by preventing long reusable content from becoming
trapped in chat.

## Core Decision

Use chat for short, temporary conversation.

Use a file artifact for reusable, reviewable, AI-handoff, or Git-managed
content.

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

## Workflow Placement

Artifact generation belongs before implementation or review when the artifact
defines scope.

Recommended flow:

```text
Idea
  -> Q Artifact Workspace
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
`docs/requests/<target_project>/<status>/` using the Task Artifact Workspace
standard from `docs/rules/q_file_artifact_standard.md`.

## Failure Modes Prevented

Artifact First prevents:

- truncated chat requests;
- missing copied sections;
- broken Markdown;
- human copy mistakes;
- AI execution from incomplete input;
- weak Git history;
- hard-to-review approval context.

## Related Documents

- `docs/rules/artifact_first_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/requests/README.md`
- `docs/templates/q_file_template.md`
- `docs/templates/ai_implementation_request.md`
- `docs/examples/artifact_first_examples.md`
