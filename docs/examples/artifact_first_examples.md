# Artifact First Examples

## Purpose

This document shows good and bad examples for Artifact First / File Generation
First.

Use it when deciding whether a Q, design document, specification, review
request, AI request, or roadmap proposal should live in chat or in a managed
file artifact.

## Bad Example: Long Q Only In Chat

A user writes a long Q directly in chat.

The Q includes:

- repository information;
- scope guard;
- target files;
- completion criteria;
- deliverables;
- suggested commit message.

Problem:

- the chat message is truncated;
- one copied section is missing;
- Markdown headings are broken;
- completion criteria are omitted;
- Codex implements from incomplete input;
- the final request is not easy to store in Git.

Result:

The implementation may be based on a damaged request. Reviewers cannot easily
prove what the original approved request contained.

## Bad Example: Design Document As Chat Text

A design document is pasted into chat for review.

Problem:

- the document cannot be diffed easily;
- comments and approvals are separated from the source;
- another AI may receive a partial copy;
- future readers cannot find the design in the Knowledge Base.

Result:

The design becomes hidden conversation instead of reusable knowledge.

## Good Example: Q As Managed Artifacts

The Q is generated as:

```text
docs/requests/ghost-development-system/approved/GDS-0001_artifact_first_update/request.md
docs/requests/ghost-development-system/approved/GDS-0001_artifact_first_update/request.docx
```

The workspace also reserves the related completion report and notes locations:

```text
docs/requests/ghost-development-system/approved/GDS-0001_artifact_first_update/
  request.md
  completion_report.md
  notes.md
  attachments/
```

The Markdown file is used for:

- Git review;
- Codex handoff;
- diff review;
- Knowledge Base promotion.

The Word file is used for:

- human review;
- comments;
- approval;
- offline reading.

The chat response contains only:

- short summary;
- artifact paths;
- verification notes;
- remaining issues.

Result:

Codex receives the full file. Reviewers can inspect the same source. The Q can
be committed, reused, or promoted later.

## Bad Example: Artifact Outside Workspace

The Q is generated as a file but left only in a download or temporary folder.

Problem:

- the artifact is not under `docs/requests/`;
- no status folder shows whether it is draft, approved, completed, or archived;
- the completion report has no guaranteed location beside the Q;
- Git-managed review cannot treat the file as the authoritative source.

Result:

The work still depends on fragile handoff even though a file exists.

## Good Example: AI Implementation Request

Instead of pasting a long Codex request into chat, create:

```text
docs/requests/ghost-development-system/approved/GDS-0002_codex_artifact_first_request/request.md
```

The file includes:

- Repository Information;
- Output Format;
- Required Artifacts;
- Scope Guard;
- Do / Do Not;
- Completion Criteria;
- Deliverables;
- Suggested Commit Message.

Chat says:

```text
Created the Codex request as:
docs/requests/ghost-development-system/approved/GDS-0002_codex_artifact_first_request/request.md

Use that file as the authoritative implementation request.
```

Result:

The AI request is complete, reviewable, and Git-managed.

## Good Example: Roadmap Proposal

A roadmap update proposal is prepared as:

```text
docs/roadmap/proposals/output_layer_proposal.md
```

If human review is expected, also prepare:

```text
docs/roadmap/proposals/output_layer_proposal.docx
```

Chat summarizes the proposal and links to the artifacts.

Result:

Roadmap review can happen against stable files instead of incomplete copied
chat.

## Decision Rule

If the output will be reused, reviewed, handed to AI, approved by a human, or
managed in Git, generate the file artifact first.

If the output is only a short consultation, clarification, or status update,
chat is enough.

## Related Documents

- `docs/rules/artifact_first_rules.md`
- `docs/workflow/output_policy.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/requests/README.md`
- `docs/templates/q_file_template.md`
