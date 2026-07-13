# Completion Report Workflow

**Version:** 1.0

**Last Updated:** 2026-07-13

## Purpose

This workflow explains how to create a Completion Report v2 after a Q, review, documentation update, or implementation task.

In Product Documentation Hierarchy v2, Completion Report is the official layer
after Q Documents. It feeds future Improvement Records and Promotion decisions.

## Standard Flow

```text
Source Q
  -> Implementation / Documentation Update
  -> Changed Files Review
  -> Verification
  -> Evidence Review
  -> Safe Commit Set
  -> Project Edit Status
  -> Improvement Review
  -> Beginner & Future Self Test Review, when applicable
  -> Lessons Learned
  -> Reusable Assets Created
  -> Promotion Candidates
  -> Pending Insight Review, when applicable
  -> Remaining Issues
  -> Recommended Next Q
  -> Completion Report Artifact
  -> Completion Checklist
  -> Commit / Push Decision
```

## Step 1: Confirm Source Q

Record:

- Source Q ID.
- Source Q File.
- Target Project.
- Working Repository.
- Working Directory.

If no Source Q exists, record the user request or artifact that authorized the work.

## Step 2: Review Changed Files

Use `git status --short --untracked-files=all` or equivalent.

Classify:

- created;
- updated;
- deleted;
- intentionally not changed;
- unrelated dirty files.

## Step 3: Run Verification

Run task-appropriate validation.

For GDS Docs, standard candidates are:

```powershell
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py
git diff --check
```

Record not-run checks with reasons.

Also record evidence that should feed future Improvement Records or Promotion
decisions.

## Step 4: Identify Safe Commit Set

List files that are safe to commit together.

Exclude unrelated files, runtime data, temporary files, generated debug artifacts, and files outside the Q scope.

## Step 5: Record Commit / Push Status

Record the Q policy and actual execution state.

Commit and push are never implied by Completion Report creation.

## Step 6: Record Project Edit Status

Confirm target and non-target project boundaries.

If GameGhost is non-target, state whether GameGhost was edited.

## Step 7: Improvement Review

Review whether the work produced reusable learning for:

- Documentation.
- Templates.
- Workflow.
- Rules.
- Architecture.
- Knowledge Base.
- Automation / Validation.
- Metrics / Evidence.

If the task creates or updates durable documentation, roadmap, decision,
handoff, Q, Completion Report, or README / index artifacts, run or explicitly
mark the Beginner & Future Self Test as not applicable.

Record:

- perspective;
- result;
- blocking / non-blocking issues;
- smallest recommended improvement;
- whether excessive duplication was avoided.

## Step 8: Separate Follow-up Buckets

If Pending Insight was created, updated, reviewed, resolved, or used as Q source,
record:

- Pending Insight decision.
- Codex execution restriction.
- Startup / Daily Review integration.
- Cleanup status.
- Remaining pending items.

Use separate sections:

- Remaining Issues.
- Recommended Improvements.
- Future Candidates.
- Recommended Next Q.

## Step 9: Save Completion Report Artifact

Save the report beside the Source Q when a task workspace exists:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/completion_report.md
```

For repository-wide documentation tasks without a request workspace, save a report under:

```text
reports/<short_topic>_completion_report.md
```

## Step 10: Completion Checklist

After the report is written, complete the Completion Checklist and record:

- verification status;
- review status;
- AI Repository Index decision;
- Repository Quality result;
- commit / push state;
- workspace status;
- next Q.

## Related Documents

- `docs/rules/completion_report_rules.md`
- `templates/completion_report_template.md`
- `docs/rules/beginner_future_self_test_rules.md`
- `docs/workflow/beginner_future_self_test_workflow.md`
- `docs/rules/completion_checklist_rules.md`
- `docs/workflow/completion_checklist_workflow.md`
- `docs/rules/pending_conversation_insight_review_rules.md`
- `docs/workflow/pending_conversation_insight_review_workflow.md`
- `templates/completion_checklist_template.md`
- `docs/workflow/commit_safety_checklist.md`
