# Completion Report Rules

**Version:** 1.0

**Last Updated:** 2026-07-13

## Purpose

Completion Report Rules define the required structure and quality bar for completion reports in Ghost Development System Docs.

A Completion Report is the durable record that connects a Source Q File to changed files, verification, Safe Commit Set, project edit boundaries, reusable learning, and the recommended next Q.

In Product Documentation Hierarchy v2, Completion Report is the official
implementation completion layer after Q Documents. It records implementation
results, verification, evidence, lessons learned, promotion candidates,
remaining issues, and recommended next work.

## Core Rule

Every substantial Q should produce a Completion Report artifact when the work is completed, reviewed, or handed off.

The report should be saved as Markdown and should be easy to review without reading the whole chat history.

## Required Sections

Completion Report v2 requires these sections:

1. Identity
2. Changed Files
3. Summary
4. Implementation Results
5. Verification
6. Evidence, when distinct from verification output
7. Safe Commit Set
8. Commit / Push Status
9. Project Edit Status
10. Improvement Review
11. Beginner & Future Self Test Review, when applicable
12. Lessons Learned
13. Reusable Assets Created
14. Promotion Candidates, when applicable
15. Remaining Issues
16. Recommended Improvements
17. Future Candidates
18. Recommended Next Q
19. Suggested Commit Message
20. Pending Insight Review, when Pending Insight was created, updated, reviewed, or used as Q source

A section may be marked `Not Applicable`, but it should not be silently omitted.

## Identity Rule

The report must identify:

- Source Q ID.
- Source Q File.
- Target Project.
- Working Repository.
- Working Directory.
- Report Status.
- Created Date / Last Updated Date.

## Changed Files Rule

Changed Files must separate:

- files created;
- files updated;
- files deleted;
- files intentionally not changed.

The list should match `git status` and the Safe Commit Set unless exclusions are explained.

## Verification Rule

Verification must record:

- commands or methods used;
- result;
- not verified items;
- limitations.

For GDS Docs, standard candidates are:

```powershell
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py
git diff --check
git status --short --untracked-files=all
```

## Safe Commit Set Rule

Safe Commit Set is mandatory.

It must answer:

- Which files are safe to commit together?
- Which changed files are excluded?
- Why are they excluded?
- Are there unrelated dirty files?
- Were generated, debug, temporary, or runtime files excluded?

Safe Commit Set must match Changed Files or explicitly explain every difference.

## Commit / Push Status Rule

Commit and Push status must be explicit.

Record:

- policy from the Q;
- whether commit was required;
- whether commit was executed;
- commit hash when created;
- whether push was required;
- whether push was executed.

If the Q says `Do not commit`, the report must say `Commit executed: No`.

## Project Edit Status Rule

The report must state whether target and non-target projects were edited.

When GameGhost is not the target project, include:

```text
GameGhost edit status: Not edited.
```

Runtime code, production data, and reference-only repositories must be called out when relevant.

## Improvement Review Rule

Completion is not only output delivery. The report must review whether reusable improvements were found for:

- Documentation.
- Templates.
- Workflow.
- Rules.
- Architecture.
- Knowledge Base.
- Automation / Validation.
- Metrics / Evidence.

When the task creates or updates durable documentation, roadmap, decision,
handoff, Q, or review artifacts, the report should record the Beginner &
Future Self Test result or explain why it is not applicable.

## Lessons Learned Rule

The report should preserve practical lessons discovered during execution.

Lessons Learned should be short and reusable, not a diary of the whole session.

## Reusable Assets Created Rule

The report must list reusable assets created or updated, such as:

- rules;
- workflows;
- templates;
- examples;
- reports;
- validators;
- knowledge entries.

If none were created, write `None`.

## Remaining Issues And Future Candidates Rule

Separate:

- Remaining Issues: known current problems, warnings, or blockers.
- Recommended Improvements: near-term follow-up improvements.
- Future Candidates: useful ideas that are not approved scope yet.

Do not mix Future Candidates into completed scope.

## Recommended Next Q Rule

When follow-up work is useful, the report should propose one Recommended Next Q with:

- title;
- purpose;
- suggested Q ID, when practical;
- priority.

## AI Repository Index Rule

If public AI knowledge entry points changed, the report must record whether `docs/ai_repository_index.md` was regenerated and validated.

## Pending Insight Review Rule

When a task creates, updates, reviews, resolves, or converts a Pending Insight,
the report must record:

- Pending Insight definition and storage.
- Review decision.
- Codex execution restriction.
- Startup / Daily Review integration.
- Cleanup status.
- Remaining pending items.

## Repository Quality Rule

When documentation structure, rules, workflow, templates, examples, reports, or AI Repository Index changed, run or explicitly defer Repository Quality Audit.

## Completion Decision Rule

The report should end with a completion decision:

```text
Work can be treated as complete: Yes / No / Revision Recommended
```

This does not authorize commit or push unless the Q or user explicitly allows it.

## Related Documents

- `templates/completion_report_template.md`
- `docs/workflow/completion_report_workflow.md`
- `docs/rules/beginner_future_self_test_rules.md`
- `templates/beginner_future_self_test_template.md`
- `templates/completion_checklist_template.md`
- `docs/rules/completion_checklist_rules.md`
- `docs/workflow/completion_checklist_workflow.md`
- `docs/rules/git_rules.md`
- `docs/workflow/commit_safety_checklist.md`
