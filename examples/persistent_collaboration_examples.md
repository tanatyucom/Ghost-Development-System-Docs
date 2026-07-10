# Persistent Collaboration Examples

## Purpose

This document shows examples for applying Persistent Collaboration rules across
ChatGPT, Codex, Claude, Gemini, human review, Q files, and repository updates.

Examples are references. When an example conflicts with a rule, follow the rule.

## Good Examples

### Command Presentation

Good:

```powershell
cd C:\GitHub\Ghost-Development-System-Docs
python scripts\repository_quality_audit.py
```

Why it is good:

- The command starts from the intended repository.
- The block is copy-pasteable.
- The user does not need to infer the working directory.

Bad:

```powershell
python scripts\repository_quality_audit.py
```

Why it is bad:

- The command may run from the wrong repository.
- In multi-repository work, this can cause false errors or unintended edits.

### Review Conclusion

Good:

```text
Conclusion: Commit OK

Reason:
- Repository Quality Audit passed.
- AI Repository Index validation passed.
- No remaining issues affect the requested scope.
```

Good:

```text
Conclusion: Revision Recommended

Reason:
- The README route is missing.
- The completion report does not list verification evidence.
```

Bad:

```text
Looks fine.
```

Why it is bad:

- It does not tell the user whether commit is recommended.
- It does not separate evidence from impression.

### Download First

Good:

```text
The Q is saved as:
docs/requests/gameghost/ready/2026-07-11_gameghost_steam_ocr_review.md

Chat summary:
- Scope: Steam OCR review.
- Output: review report and debug artifact list.
- Commit: do not commit.
```

Why it is good:

- The reusable Q is stored as an artifact.
- Chat contains only a summary.
- Another AI can consume the same source without copy loss.

Bad:

```text
Paste the full Q into chat and ask the next AI to continue from memory.
```

Why it is bad:

- Long chat content can be truncated.
- The original request may be lost.
- The result is hard to review or commit.

### Repository First

Good:

```text
Decision order:
1. docs/ai_repository_index.md
2. docs/rules/ai_collaboration_rules.md
3. docs/workflow/ai_daily_operation_cycle.md
4. Current Q file
5. Chat clarification
```

Why it is good:

- Adopted repository knowledge controls the work.
- Chat is used for current clarification, not as the long-term source of truth.

Bad:

```text
The chat said something different last week, so ignore the repository rule.
```

Why it is bad:

- Chat memory is temporary.
- Adopted rules must be updated in the repository if they need to change.

### Platform First

Good:

```text
Finding:
This behavior appears useful across GameGhost, ComicGhost, and future Ghosts.

Proposal:
Classify it as a GDS Platform candidate before adding a project-only rule.
```

Why it is good:

- Shared behavior is evaluated as a platform concern.
- Domain-specific implementation can still remain in the target project.

Bad:

```text
Add the same collaboration rule separately to every Ghost project.
```

Why it is bad:

- Duplicate rules drift.
- Future AI sessions must rediscover the same standard.

### AI Collaboration

Good:

```text
Proposal:
I found a recurring review pattern that may belong in GDS.

Evidence:
- It appears in three completion reports.
- It is not project-specific.
- It reduces repeated manual checks.

Request:
Should I draft a GDS rule candidate, or keep it as a Future Candidate?
```

Why it is good:

- AI proposes, but does not silently expand scope.
- Evidence and decision request are separated.
- Human approval remains explicit.

Bad:

```text
I noticed a better system, so I changed the rules, workflow, and templates.
```

Why it is bad:

- It bypasses human approval.
- It mixes proposal and implementation.
- It may create scope drift.

### Completion Report Priority

Good:

```text
Priority Summary:
- Summary: Persistent Collaboration examples were added.
- Verification: Repository Quality Audit passed.
- Remaining Issues: None.
- Recommended Next Q: Add a multi-AI handoff checklist if needed.
```

Why it is good:

- The most important review information appears first.
- The user can decide next action quickly.

Bad:

```text
Detailed chronology first, verification buried near the end.
```

Why it is bad:

- Human review takes longer.
- Important remaining issues can be missed.

## Anti-Patterns

- Treating chat memory as stronger than repository rules.
- Creating long reusable prompts only in chat.
- Presenting commands without repository context.
- Reporting review results without `Commit OK` or `Revision Recommended` when
  evidence is sufficient.
- Adding project-specific copies of behavior that should be evaluated as GDS
  Platform behavior.
- Applying proactive AI proposals without separating proposal, evidence, and
  human decision.

## Related Documents

- `docs/rules/ai_collaboration_rules.md`
- `docs/rules/core_principles.md`
- `docs/rules/artifact_first_rules.md`
- `docs/rules/quality_rules.md`
- `templates/completion_report_template.md`
- `docs/workflow/ai_daily_operation_cycle.md`
