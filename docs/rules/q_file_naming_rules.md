# Q File Naming Rules

**Version:** 1.0

**Last Updated:** 2026-07-13

## Purpose

This rule standardizes Q ID, Q filename, request folder, status, and date usage
so humans and AI can identify a Q's project, domain, topic, language, and
identity without relying on chat memory.

## Core Principle

Q names should be understandable in three seconds from the ID and topic.

Date is not the default identity for a Q. Q identity is carried by the Q ID,
folder name, and metadata inside `request.md`.

## Canonical Q ID Format

Use this format for new official Q artifacts:

```text
<PROJECT>-<DOMAIN>-<NUMBER>
```

Recommended project prefixes:

- `GDS`
- `GG`
- `ANIME`
- `COMIC`

Examples:

```text
GDS-PLUGIN-ARCH-001
GDS-CONVERSATION-INSIGHT-002
GG-STEAM-OCR-003
ANIME-ANILIST-001
```

If a repository already has a stronger local ID standard, keep the local
standard and document the exception in the Q or project profile.

## Canonical Markdown Filename

Use this pattern for standalone Q Markdown files:

```text
Q_<Q_ID>_<short_topic>_JP.md
```

Examples:

```text
Q_GDS-PLUGIN-ARCH-001_plugin_architecture_standard_JP.md
Q_GG-STEAM-OCR-003_human_review_gate_clearance_JP.md
```

Use lowercase ASCII snake case for `<short_topic>`.

The language suffix is required when the Q is language-specific:

- `_JP.md`
- `_EN.md`

## Date Rule

Default:

```text
Do not put a date in the Q filename.
```

Reason:

- Q ID provides identity.
- Created Date and Last Updated Date belong in Q metadata.
- Qs often live longer than one day.
- Removing date from filenames reduces later rename churn.

Allowed date exceptions:

- Daily snapshot.
- Date-specific incident.
- Release-specific record.
- Migration executed on a specific date.
- External event tied to a concrete date.
- Temporary handoff package where date is the primary identity.

Example:

```text
2026-07-13_repository_migration_snapshot.md
```

Do not use date by default for ordinary Q files:

```text
Q_GDS_Knowledge_Suggestion_Assistant_JP.md
Q_GG_Steam_OCR_Human_Review_Gate_Clearance_JP.md
```

## Metadata Date

Every official Q should include:

```text
Created Date: YYYY-MM-DD
Last Updated Date: YYYY-MM-DD
```

Metadata dates are the source of truth for creation and update timing.

## Canonical Request Folder

Use this folder pattern for official task workspaces:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/
```

Example:

```text
docs/requests/gds/draft/GDS-PLUGIN-ARCH-001_plugin_architecture_standard/
```

The folder name, `request.md` Q ID, and completion report Source Q File must
match.

## Required Artifact Set

Each official Q workspace should contain:

```text
request.md
notes.md
completion_report.md
attachments/
```

Rules:

- `request.md` is the authoritative Q.
- `notes.md` records working notes, uncertainty, review comments, or migration
  context.
- `completion_report.md` records final result, verification, and follow-up.
- `attachments/` is optional but should exist when supporting files are used.

If any artifact is not applicable, record `Not Applicable` in the Q or
completion report.

## Simple File Form

Simple file form is allowed only for small, temporary, or legacy-compatible Qs
that do not need a full workspace yet.

Preferred simple form:

```text
docs/requests/<project>/<status>/Q_<Q_ID>_<short_topic>_JP.md
```

Legacy date form remains readable but is not the default for new Qs:

```text
docs/requests/<project>/<status>/YYYY-MM-DD_<project>_<short_topic>.md
```

Do not mass-rename existing Qs just to satisfy this rule.

## Status Rule

Allowed Q statuses:

```text
Draft
Approved
In Progress
Review
Completed
Archived
Rejected
```

Folder status should not contradict the Q metadata status.

Recommended folder names:

```text
draft
approved
in_progress
review
completed
archived
rejected
```

Existing repositories may keep current folders such as `draft`, `approved`,
`completed`, and `archived` until a migration Q explicitly expands them.

## Revision / Addendum Rule

When requirements change:

```text
Small scope extension
  -> addendum_vX.Y.md

Materially different objective
  -> new Q

Correction before execution
  -> revise request.md / Q file
```

Do not create new Qs for every small clarification.

Do not overwrite completed Q history without a review note or addendum.

## Discoverability Rule

The Q filename, folder name, and title must make these visible quickly:

- Project.
- Domain.
- Topic.
- Q identity.
- Language.
- Status through folder or metadata.

Avoid vague names:

```text
Q_fix.md
Q_review.md
Q_update.md
```

Prefer purpose-oriented names:

```text
Q_GG-STEAM-OCR-003_human_review_gate_clearance_JP.md
Q_GDS-QTEMPLATE-001_q_template_and_naming_standard_JP.md
```

## Migration Policy

Do not mass-rename existing Q files.

Apply this rule as follows:

```text
New Q
  -> New standard required

Existing Q modified
  -> Naming review

Promotion / Archive
  -> Canonical folder and metadata alignment

Repository reorganization
  -> Separate migration Q
```

## Completion Report Requirement

Completion reports must include:

- Source Q File.
- Q ID.
- Changed Files.
- Safe Commit Set.
- Commit Status.
- GameGhost Edit Status, when GameGhost is non-target.
- Suggested Commit Message.

The Safe Commit Set should match the final changed files or explicitly explain
why a changed file is excluded.
