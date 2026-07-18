# Repository Recommendation Examples

## Purpose

These examples show how Codex should produce evidence-backed Repository
Recommendation blocks for ChatGPT Completion Review and Workflow
Recommendation.

## Case 1: Normal Commit Recommendation

```text
Repository Recommendation

Repository:
Ghost-Development-System-Docs

Branch:
main

Request / Q:
GDS-EXAMPLE-001

Completion Status:
PASS

Repository Quality:
Green

Scope Review:
Clean

Repository State:
Dirty

Remote State:
ahead

Safe Commit Set:
- docs/rules/example_rule.md
- templates/example_template.md
- docs/ai_repository_index.md

Validation Summary:
- git diff --check: PASS
- AI Repository Index: PASS
- Encoding Regression: PASS
- Repository Quality Audit: PASS

Approval Units:
- Commit: Recommended
- Push: Hold
- Tag: Hold

Reasons:
- Requested documentation scope is complete.
- Changed files match the safe commit set.
- Required validation passed.

Known Warnings:
- None

Remaining Issues:
- None

Review Boundary:
ChatGPT Completion Review / Workflow Recommendation required.
```

## Case 2: Validation Failure

```text
Approval Units:
- Commit: Hold
- Push: Hold
- Tag: Hold

Reasons:
- Required validation failed.
- Commit recommendation cannot be made until failure is repaired or explicitly
  reviewed.
```

## Case 3: Mixed Scope

```text
Scope Review:
Mixed Scope

Safe Commit Set:
- docs/rules/request_scope_rule.md

Known Warnings:
- Unrelated dirty file exists: docs/roadmap/unrelated.md

Approval Units:
- Commit: Recommended
- Push: Hold
- Tag: Hold
```

If separation is not safe:

```text
Approval Units:
- Commit: Hold
- Push: Hold
- Tag: Hold

Reasons:
- Safe Commit Set cannot be established.
- SCW required.
```

## Case 4: Commit Complete, Push Review

```text
Repository State:
Clean

Remote State:
ahead

Safe Commit Set:
Commit already created: abc1234

Approval Units:
- Commit: Not Applicable
- Push: Recommended
- Tag: Hold

Reasons:
- Commit identity is known.
- Remote state was checked.
- No unresolved execution issue remains.
```

## Case 5: Push Held Because Branch Is Diverged

```text
Remote State:
diverged

Approval Units:
- Commit: Not Applicable
- Push: Hold
- Tag: Hold

Reasons:
- Branch is diverged.
- Push requires repository review before recommendation.
```

## Case 6: Tag Recommendation

```text
Approval Units:
- Commit: Not Applicable
- Push: Hold
- Tag: Recommended

Reasons:
- Milestone condition is met.
- Tag name is known: v1.2.0
- Target commit is known: abc1234
- Tag remains a separate Approval Unit from Push.
```

## Case 7: Stale Recommendation

```text
Approval Units:
- Commit: Hold
- Push: Hold
- Tag: Hold

Reasons:
- Diff changed after Repository Recommendation.
- Previous recommendation is invalidated.
- Re-review required.
```

## Case 8: Insufficient Evidence

```text
Repository Quality:
Unknown

Remote State:
unknown

Safe Commit Set:
Unknown

Validation Summary:
- git diff --check: NOT RUN
- Repository Quality Audit: NOT RUN

Approval Units:
- Commit: Hold
- Push: Hold
- Tag: Hold

Reasons:
- Validation, branch, or safe commit scope could not be confirmed.
- No optimistic recommendation is allowed under insufficient evidence.
```
