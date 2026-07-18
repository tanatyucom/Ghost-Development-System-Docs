# Repository Action Status Examples

## Purpose

These examples show how to separate execution status, recommendation, approval,
suggested action details, and execution evidence.

## Good: Commit Recommended But Not Executed

```text
## Execution Status

- Commit Status: Not Executed
- Push Status: Not Executed
- Tag Status: Not Executed

## Repository Recommendation

- Commit: Recommended
- Push: Hold
- Tag: Hold

## Approval Status

- Commit: Not Requested
- Push: Not Requested
- Tag: Not Requested

## Suggested Action Details

Suggested Commit Message:

docs: define command center working context model

Note: This is a proposed commit message. It is not execution evidence.
```

Why good:

- Actual state appears before the recommendation.
- Suggested message is clearly a proposal.
- No commit is implied.

## Good: Commit Completed, Push Held

```text
## Execution Status

- Commit Status: Completed
- Commit ID: 1fe3d89
- Push Status: Not Executed
- Tag Status: Not Executed

## Repository Recommendation

- Commit: Not Applicable
- Push: Recommended
- Tag: Hold

## Approval Status

- Commit: Approved
- Push: Pending Human Approval
- Tag: Not Requested

## Execution Evidence

- Commit ID: 1fe3d89
- Commit Subject: docs: define command center working context model
- Repository: Ghost-Development-System-Docs
- Branch: main
```

Why good:

- Completed commit is proven by evidence.
- Push remains separate.
- Suggested Commit Message is omitted because the commit already happened.

## Good: Push Blocked

```text
## Execution Status

- Commit Status: Completed
- Commit ID: abcdef1
- Push Status: Blocked
- Tag Status: Not Executed

## Repository Recommendation

- Commit: Not Applicable
- Push: Hold
- Tag: Hold

## Approval Status

- Commit: Approved
- Push: Not Requested
- Tag: Not Requested

## Execution Evidence

- Commit ID: abcdef1
- Push Evidence: None
- Blocker: Push approval was not requested.
```

Why good:

- Push is not called failed because it was not attempted.
- The blocker is explicit.

## Good: Tag Failed

```text
## Execution Status

- Commit Status: Completed
- Push Status: Completed
- Tag Status: Failed

## Approval Status

- Tag: Approved

## Execution Evidence

- Tag Name: gds-v1.1-platform-foundation
- Target Commit: abcdef1
- Command: git tag gds-v1.1-platform-foundation abcdef1
- Result: Failed
- Error: tag already exists
```

Why good:

- Failure is used only because tag execution was attempted.
- Error evidence is preserved.

## Bad: Suggested Commit Message Without Status

```text
## Suggested Commit Message

docs: define command center working context model
```

Why bad:

- A reviewer may confuse the suggestion with an executed commit.
- Commit / Push / Tag status is not visible.
- Approval state is unknown.

## Bad: Completed Without Evidence

```text
## Execution Status

- Commit Status: Completed
```

Why bad:

- `Completed` requires a commit ID or equivalent evidence.
- The repository, branch, and execution result are missing.

## Bad: Recommendation Uses Approved

```text
## Repository Recommendation

- Commit: Approved
```

Why bad:

- Repository Recommendation must not use `Approved`.
- `Approved` belongs to Human Approval or Approval Unit state.

## Bad: Partial Execution Hidden

```text
## Execution Status

- Repository Action Status: Completed
```

Why bad:

- Commit, Push, and Tag are independent approval units.
- Partial completion must be shown per action.
