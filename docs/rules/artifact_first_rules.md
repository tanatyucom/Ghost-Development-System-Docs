# Artifact First Rules

**Version:** 1.2

**Last Updated:** 2026-07-11

## Purpose

This document defines the Artifact First / File Generation First rule for
Ghost Development System Docs.

Reusable, reviewable, or Git-managed outputs should be generated as durable
files instead of being delivered only in chat.

## Core Rule

When an output is expected to be reused, reviewed, shared with another AI, or
managed in Git, create a managed file artifact first.

For Q files, creating the artifact is not complete until the file has been
saved into the Task Artifact Workspace under `docs/requests/`. A Q that remains
only in chat, a download folder, clipboard, or sandbox-local path is not the
authoritative execution input.

Chat should contain only:

- a short summary;
- changed file list;
- verification notes;
- links or paths to the generated artifacts.

Do not use a long chat body as the authoritative copy for reusable work.

## Standard Artifact Formats

Standard formats:

- Markdown `.md`
- Word `.docx`

Use Markdown when the artifact should be stored in Git, reviewed as text, or
used directly by Codex, Gemini, Claude, or another AI.

Use `.docx` when human review, redline, offline reading, or non-Git review is
expected.

Additional formats may be used when the content requires them:

- PDF
- CSV
- XLSX
- PPTX

## Required File-First Outputs

Generate files by default for:

- Q files;
- templates;
- checklists;
- prompts;
- Markdown documents;
- reports;
- design documents;
- specifications;
- Codex requests;
- Gemini requests;
- Claude requests;
- AI implementation requests;
- roadmap update proposals;
- long review requests;
- long completion reports;
- reusable review checklists;
- human approval packets;
- Git-managed documentation.

If one of these outputs is short enough for chat but is expected to be reused
or committed later, still create the file artifact.

## Q File Rule

Q files should be generated as files by default.

Preferred form:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/request.md
```

When human review is expected before execution, also generate:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/request.docx
```

Simple file form is allowed when a full workspace is not needed yet:

```text
docs/requests/<project>/<status>/Q_<Q_ID>_<short_topic>_JP.md
```

The chat response should not contain the full Q unless explicitly requested. It
should summarize the purpose, list the artifact paths, and state how to use
the file.

Q file artifacts and their related completion reports should follow
`docs/rules/q_file_artifact_standard.md`, `docs/rules/q_file_naming_rules.md`, and `docs/rules/q_file_template_rules.md`.

The completion report should be saved into the same workspace as the source Q:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/completion_report.md
```

## Design And Specification Rule

Design documents and specifications should be generated as managed artifacts.

Use `.md` as the Git and AI handoff source. Use `.docx` when the document is
intended for human review, comments, approval, or offline reading.

Do not rely on copied chat text as the single source of truth for architecture,
scope, completion criteria, or implementation instructions.

## AI Request Rule

Codex, Gemini, Claude, and other AI implementation or review requests should be
prepared as files when they contain non-trivial scope, repository boundaries,
completion criteria, or deliverables.

The file should include Repository Information, Scope Guard, Do / Do Not,
Completion Criteria, Deliverables, and Suggested Commit Message when relevant.

## Roadmap And Review Rule

Roadmap update proposals and long review requests should be generated as file
artifacts.

This prevents:

- truncated requests;
- missing copied sections;
- broken Markdown;
- accidental omission of completion criteria;
- AI implementation based on incomplete input;
- weak Git history for reviewed decisions.

## Exceptions

Chat-only output is acceptable for:

- short questions;
- quick clarification;
- small status updates;
- one-off summaries that are not reused;
- exploratory discussion before an artifact is requested.

When a chat-only discussion becomes reusable or decision-bearing, promote it to
an artifact before implementation or approval.

## Decision Background

Long Q files, design documents, review requests, roadmap proposals, and AI
instructions are easy to damage when they live only in chat. They can be cut
off, copied incompletely, lose Markdown structure, or disappear from the
working context.

File artifacts make the work reviewable, reusable, Git-manageable, and easier
for humans and AI to verify.

## Related Documents

- `docs/workflow/output_policy.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_naming_rules.md`
- `docs/rules/q_file_template_rules.md`
- `docs/requests/README.md`
- `templates/Q_TEMPLATE.md`
- `docs/templates/ai_implementation_request.md`
- `docs/examples/artifact_first_examples.md`
- `docs/architecture/responsibility_boundary.md`
