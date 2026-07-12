# Q File Artifact Workflow Examples

## Purpose

This document shows good and bad examples for saving Q files and completion
reports as artifacts.

Use it when preparing a Q for Codex or another AI.

## Bad Example: Q Only In Chat

A long Q is pasted directly into chat.

The chat contains:

- Repository Information;
- Scope Guard;
- Do / Do Not;
- Completion Criteria;
- Deliverables;
- Suggested Commit Message.

Problem:

- the Q may be truncated;
- Markdown may be damaged;
- a copied section may be missed;
- Codex may execute from incomplete input;
- the original Q may not be findable later.

Result:

Review cannot reliably compare implementation against the original request.

## Bad Example: Implementation Without Saved Q

A user describes a request in chat and asks Codex to start immediately.

No Q artifact is saved in:

```text
docs/requests/
```

No completion report artifact is planned.

Problem:

- the source request is not Git-managed;
- future reviewers cannot find the exact approved scope;
- follow-up work has to reconstruct context from chat;
- commit review cannot link back to a stable Q file.

Result:

The project loses reusable knowledge even if the implementation succeeds.

## Bad Example: Q Generated But Not Saved To Workspace

A Q file is generated in a download folder or temporary sandbox path:

```text
C:/Users/example/Downloads/Q_GameGhost_Steam_Repair.md
```

Codex starts implementation from that file, but the file is never saved under:

```text
docs/requests/<project>/<status>/
```

Problem:

- the request is easy to lose after the chat session;
- the completion report has no stable workspace beside the source Q;
- reviewers cannot rely on Git history to find the approved request;
- follow-up Q files cannot link to a durable source artifact.

Result:

The Q exists as a file, but it is not an official Task Artifact Workspace
record.

## Bad Example: Ambiguous Flat File

A Q file is saved as:

```text
docs/requests/steam_ocr.md
```

Problem:

- Target Project is not visible from the path;
- workflow status is not visible from the path;
- related completion report location is unclear;
- notes and attachments have no obvious home;
- future reviewers cannot tell whether the request was draft, approved,
  completed, or archived.

Result:

The artifact exists, but humans and AI still have to guess its status and
context.

## Good Example: Saved Q Artifact

Full task workspace form:

```text
docs/requests/gameghost/completed/GG-STEAM-OCR-001_steam_ocr/
  request.md
  completion_report.md
  notes.md
  attachments/
```

The Q is saved before implementation as:

```text
docs/requests/gameghost/approved/GG-STEAM-OCR-001_steam_ocr/request.md
```

The minimum workspace files are:

```text
docs/requests/gameghost/approved/GG-STEAM-OCR-001_steam_ocr/
  request.md
  completion_report.md
  notes.md
  attachments/
```

If human review is expected, also generate:

```text
docs/requests/gameghost/approved/GG-STEAM-OCR-001_steam_ocr/request.docx
```

The chat body says:

```text
Q artifact saved:
docs/requests/gameghost/approved/GG-STEAM-OCR-001_steam_ocr/request.md

Use that file as the authoritative request for Codex.
```

Result:

Codex receives the full request, reviewers can inspect the same source, and the
Q can be committed or reused later.

## Good Example: Completion Report Artifact

After implementation, the completion report is saved beside the Q:

```text
docs/requests/gameghost/completed/GG-STEAM-OCR-001_steam_ocr/completion_report.md
```

The completion report records:

- Source Q File;
- Output Artifacts;
- Generated Files;
- Changed Files;
- Verification;
- Commit Hash, if a commit exists;
- Follow-up Q.

Result:

The implementation has a durable audit trail:

```text
Q Artifact
  -> Codex
  -> Completion Report Artifact
  -> Review
  -> Commit
  -> Knowledge Promotion
```

## Good Example: Notes And Attachments

Use `notes.md` for review notes, migration uncertainty, or context that should
not clutter the Q itself:

```text
docs/requests/gameghost/completed/GG-STEAM-OCR-001_steam_ocr/notes.md
```

Use `attachments/` for task-specific supporting files:

```text
docs/requests/gameghost/completed/GG-STEAM-OCR-001_steam_ocr/attachments/
```

Result:

The source Q, completion report, notes, and supporting files stay together
when the workspace moves from `approved` to `completed` or `archived`.

## Good Example: Related Commit

The Q says:

```text
Related Commit: Commit only when explicitly requested.
```

The completion report says:

```text
Commit Hash: Not created.
```

After a reviewed commit exists, the completion report may be updated with:

```text
Commit Hash: abc1234
```

Result:

Commit policy and commit evidence remain linked to the request.

## Good Example: Simple Allowed Form

When the project is not ready for full task folders or the task has no related
attachments yet, this simpler form is allowed:

```text
docs/requests/gameghost/completed/Q_GG-STEAM-OCR-001_steam_ocr_JP.md
docs/requests/gameghost/completed/Q_GG-STEAM-OCR-001_steam_ocr_JP_completion_report.md
```

This is acceptable when:

- the Q is small;
- there are no attachments;
- a Q ID is available and the task does not yet need a full workspace;
- `notes.md` is not needed.

If the task later gains notes, attachments, review copies, or multiple addenda,
promote it to full task workspace form.

## Good Example: Movement

Start in draft:

```text
docs/requests/gameghost/draft/GG-STEAM-OCR-001_steam_ocr/request.md
```

After approval:

```text
docs/requests/gameghost/approved/GG-STEAM-OCR-001_steam_ocr/request.md
```

After completion and review:

```text
docs/requests/gameghost/completed/GG-STEAM-OCR-001_steam_ocr/
  request.md
  completion_report.md
  notes.md
  attachments/
```

When old or superseded:

```text
docs/requests/gameghost/archived/GG-STEAM-OCR-001_steam_ocr/
```

Move the whole workspace folder so request, report, notes, and attachments stay
together.

## Related Documents

- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_naming_rules.md`
- `docs/rules/q_file_template_rules.md`
- `docs/requests/README.md`
- `examples/q_file_examples.md`
- `docs/templates/q_file_template.md`
- `docs/templates/completion_report_template.md`
