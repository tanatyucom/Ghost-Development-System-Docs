# Dirty Workspace Examples

## Purpose

This document shows good and bad examples for dirty workspace handling and
commit safety.

## Bad Example: Runtime Data Committed With Docs

A documentation Q updates:

```text
docs/rules/git_rules.md
docs/workflow/commit_safety_checklist.md
```

The workspace also contains:

```text
data/metadata.json
```

Bad action:

```bash
git add .
git commit -m "docs: update workflow"
```

Problem:

- runtime data is unrelated to the documentation Q;
- review is noisy;
- commit history mixes documentation and runtime state;
- future rollback becomes risky.

## Good Example: Restore Unrelated Runtime File

The developer runs:

```bash
git status
```

They classify:

| File | Class | Action |
|---|---|---|
| `docs/rules/git_rules.md` | Documentation | Commit normally |
| `docs/workflow/commit_safety_checklist.md` | Documentation | Commit normally |
| `data/metadata.json` | Runtime Data | Do not commit |

Suggested restore command:

```bash
git restore -- data/metadata.json
```

Then:

```bash
git diff --check
```

Result:

Only requested documentation files are included in the safe commit set.

## Good Example: Preserve Unrelated User Work

The workspace includes an unrelated edited file:

```text
docs/roadmap/roadmap.md
```

The current Q does not mention roadmap edits.

Good action:

- do not stage it;
- do not restore it without approval;
- report it as unrelated existing work.

Result:

User work is protected and the current commit remains scoped.

## Good Example: Commit Review Output Conditionally

A review screenshot belongs to an approved task workspace:

```text
docs/requests/gameghost/completed/GG-0001_steam_ocr/attachments/review.png
```

This may be committed when:

- the Q expects review attachments;
- the file is not private;
- the completion report references it.

Result:

Review output is preserved as a durable artifact without leaking unrelated
local files.

## Related Documents

- `docs/rules/git_rules.md`
- `docs/workflow/commit_safety_checklist.md`
- `docs/templates/completion_report_template.md`
