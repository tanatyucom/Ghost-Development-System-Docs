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
  -> Knowledge Promotion Candidate Review
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

## Step 4: Knowledge Promotion Candidate Review

Before Safe Commit Set, check whether the work produced reusable knowledge that
should enter Knowledge Promotion Engine.

Record:

- candidate type;
- evidence;
- duplicate / canonical source check;
- proposed promotion target;
- Knowledge Carry-Forward target;
- Human Approval requirement;
- application target.

This review does not approve canonical promotion, ADR acceptance, Rule changes,
commit, push, tag, release, or cross-repository mutation.

## Step 5: Identify Safe Commit Set

List files that are safe to commit together.

Exclude unrelated files, runtime data, temporary files, generated debug artifacts, and files outside the Q scope.

## Step 6: Record Commit / Push Status

Record the Q policy and actual execution state.

Commit and push are never implied by Completion Report creation.

## Step 7: Record Project Edit Status

Confirm target and non-target project boundaries.

If GameGhost is non-target, state whether GameGhost was edited.

## Step 8: Improvement Review

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

## Step 9: Separate Follow-up Buckets

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

## Step 10: Save Completion Report Artifact

Save the report beside the Source Q when a task workspace exists:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/completion_report.md
```

For repository-wide documentation tasks without a request workspace, save a report under:

```text
reports/<short_topic>_completion_report.md
```

## Step 11: Completion Checklist

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

## AI Repository Index Update Gate

GDS-QUALITY-005 formalizes the AI Repository Index Update Gate as a completion responsibility.

Use this gate after Verification and before the final Completion Report / Completion Checklist decision when a Q changes index-target Knowledge Assets.

```text
Knowledge Asset changed
  -> Regenerate docs/ai_repository_index.md
  -> Validate index
  -> Run git diff --check
  -> Check git status --short --untracked-files=all
  -> Record generated entry count and Safe Commit Set decision
  -> Human Review / Commit decision
```

Failure action:

- If generation or validation fails, apply SCW and do not mark the Q complete.
- If repository boundary, canonical path, duplicate entry, missing entry, or dirty workspace scope is unclear, stop and request review.
- Do not continue by relying on memory or inferred Raw URLs.

Raw publication boundary:

```text
Index generation -> local index update
Commit -> Git history
Push -> GitHub main
Raw retrieval -> public Canonical Index / Artifact availability
```

This gate complements Startup / Q Creation Gate. Startup proves canonical knowledge was readable before work starts; AI Repository Index Update Gate proves repository changes were reflected before completion.
