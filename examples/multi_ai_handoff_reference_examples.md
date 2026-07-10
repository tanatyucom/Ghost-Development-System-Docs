# Multi-AI Handoff Reference Examples

## Purpose

This document provides reference examples for
`templates/multi_ai_handoff_template.md`.

Use these examples when handing work between ChatGPT, Codex, Claude, Gemini, or
human review.

Examples are references. Rules and templates remain authoritative.

## Good Examples

### New Feature Implementation

```text
Current Status:
- Feature documentation was added.
- Completion report was generated.
- Commit has not been created.

Current Focus:
- Human review should confirm the new template wording and README routes.

Scope:
- In: Ghost-Development-System-Docs documentation and templates.
- Out: GameGhost runtime code, private project data, commit creation.

Repository:
- Working repository: C:\GitHub\Ghost-Development-System-Docs
- Source of Truth: docs/ai_repository_index.md, repository Markdown, completion report.
- Completion Report: reports/new_feature_completion_report.md

Related Rules / Templates:
- docs/rules/ai_collaboration_rules.md
- templates/multi_ai_handoff_template.md
- templates/completion_report_template.md

Changed Files:
- Created: templates/example_template.md
- Updated: README.md, docs/README.md, templates/README.md

Verification:
- Repository Quality Audit: Green.
- AI Repository Index validation: OK.
- UTF-8 strict decode: OK.
- git diff --check: OK.

Remaining Issues:
- None.

Recommended Next Q:
- Add reference examples if human reviewers need usage samples.

Suggested Commit Message:
docs: add example feature template
```

Why it is good:

- It names the repository, scope, changed files, verification, and next action.
- It does not require chat history to understand the task.

### Review After Documentation Change

```text
Current Status:
- Documentation review completed.
- Conclusion: Revision Recommended.

Current Focus:
- Fix missing README route and rerun repository quality audit.

Scope:
- In: README route, docs index route, completion report update.
- Out: Rewriting the accepted rule content.

Repository:
- Working repository: C:\GitHub\Ghost-Development-System-Docs
- Source of Truth: repository documents, review report, completion report.

Changed Files:
- Updated: docs/README.md
- Intentionally not changed: docs/rules/ai_collaboration_rules.md

Verification:
- Repository Quality Audit: failed before route fix.
- git diff --check: not rerun yet.

Remaining Issues:
- README route missing.
- Verification must be rerun after fix.

Recommended Next Q:
- None. Complete the revision in the current task.
```

Why it is good:

- It keeps review conclusion visible.
- It names what is not yet verified.
- It avoids presenting incomplete work as commit-ready.

### Bug Fix

```text
Current Status:
- Bug fix implemented.
- Regression test passed.
- Commit not created.

Current Focus:
- Receiver should review the diff and confirm safe commit set.

Scope:
- In: affected bug fix files and tests.
- Out: unrelated refactor and generated runtime cache.

Repository:
- Working repository: C:\GitHub\Ghost-Development-System-Docs
- Source of Truth: current Q file and completion report.

Changed Files:
- Updated: scripts/repository_quality_audit.py
- Updated: reports/repository_quality_report.md
- Intentionally not changed: GameGhost repository.

Verification:
- Repository Quality Audit: Green.
- Targeted script validation: passed.
- git diff --check: OK.

Remaining Issues:
- None.

Recommended Next Q:
- Add audit rule example if this bug pattern repeats.

Suggested Commit Message:
fix: validate repository quality audit edge case
```

Why it is good:

- It separates the safe commit set from unrelated files.
- It names reference-only boundaries.

### Investigation Only

```text
Current Status:
- Investigation completed.
- No file repair performed.
- Findings were recorded in a report.

Current Focus:
- Human should decide whether a repair Q is needed.

Scope:
- In: investigation report and evidence summary.
- Out: direct repair, broad cleanup, generated artifact deletion.

Repository:
- Working repository: C:\GitHub\Ghost-Development-System-Docs
- Source of Truth: investigation report.

Changed Files:
- Created: reports/example_investigation_report.md
- Intentionally not changed: source documents under review.

Verification:
- UTF-8 strict decode: OK.
- Repository Quality Audit: Green.

Remaining Issues:
- Three repair candidates need human review.

Recommended Next Q:
- Create scoped repair Q from the investigation report.
```

Why it is good:

- It makes clear that investigation is not repair.
- It gives the next AI a safe next step.

### Dirty Workspace / Uncommitted State

```text
Current Status:
- Work is complete but uncommitted.
- Dirty workspace contains both task files and unrelated local files.

Current Focus:
- Receiver should stage only the safe commit set after human approval.

Scope:
- In: documentation files listed in the completion report.
- Out: unrelated local notes, cache files, reference-only repositories.

Repository:
- Working repository: C:\GitHub\Ghost-Development-System-Docs
- Source of Truth: completion report and git status.

Changed Files:
- Safe commit set: README.md, docs/README.md, templates/example.md
- Do not stage: local_notes.md, tmp/

Verification:
- Repository Quality Audit: Green.
- AI Repository Index validation: OK.
- git diff --check: OK.

Remaining Issues:
- Human approval needed before commit.

Recommended Next Q:
- None before commit. Use commit safety checklist first.

Suggested Commit Message:
docs: add example template
```

Why it is good:

- It protects unrelated dirty files.
- It gives the receiver an explicit staging boundary.

## Bad Examples

### Scope Missing

```text
Continue the work. It should be obvious from the chat.
```

Why it is bad:

- The receiver does not know what is editable.
- Reference-only repositories may be edited by mistake.

### Verification Missing

```text
I changed the files and it looks good.
```

Why it is bad:

- It does not name audit, index validation, tests, or diff checks.
- The receiver cannot judge whether the work is complete.

### Repository Missing

```text
The docs repo was updated.
```

Why it is bad:

- Multi-repository work requires the exact repository path.
- The receiver may run commands in the wrong root.

### Next Q Missing

```text
Done.
```

Why it is bad:

- The next action is unclear.
- Future Candidates may be lost.

### Chat Dependent

```text
Use the plan we discussed above.
```

Why it is bad:

- Chat context may be unavailable, truncated, or copied incompletely.
- Repository evidence should be the source of truth.

## Review Checklist

- Current Status is explicit.
- Current Focus is explicit.
- Scope includes In / Out.
- Repository and Source of Truth are named.
- Related Rules / Templates are named.
- Changed Files are grouped clearly.
- Verification result is concrete.
- Remaining Issues are explicit.
- Recommended Next Q is present or intentionally omitted with reason.
- Suggested Commit Message is present when the change set is commit-ready.
- The handoff can be understood without chat history.

## Related Documents

- `templates/multi_ai_handoff_template.md`
- `templates/multi_ai_handoff_checklist_template.md`
- `docs/rules/ai_collaboration_rules.md`
- `templates/completion_report_template.md`
- `examples/persistent_collaboration_examples.md`
