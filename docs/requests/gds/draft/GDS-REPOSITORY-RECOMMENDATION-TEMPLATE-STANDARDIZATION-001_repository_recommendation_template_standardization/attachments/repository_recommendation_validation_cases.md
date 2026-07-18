# Repository Recommendation Validation Cases

## Case 1: Normal Commit Recommendation

- Expected: `Commit: Recommended`, `Push: Hold`, `Tag: Hold`.
- Required evidence: clean requested scope, clear Safe Commit Set, validation
  passed, repository quality recorded.
- Result: documented in `examples/repository_recommendation_examples.md`.

## Case 2: Validation Failure

- Expected: `Commit: Hold`, `Push: Hold`, `Tag: Hold`.
- Required behavior: failed validation blocks optimistic recommendation.
- Result: documented.

## Case 3: Mixed Scope

- Expected: Scope Review identifies `Mixed Scope`.
- If safe separation is possible, Safe Commit Set is explicit.
- If safe separation is not possible, Commit is `Hold` and SCW is required.
- Result: documented.

## Case 4: Commit Complete, Push Review

- Expected: `Commit: Not Applicable`, `Push: Recommended`, `Tag: Hold`.
- Required evidence: commit SHA or commit identity known and remote state
  checked.
- Result: documented.

## Case 5: Push Held Because Branch Is Diverged

- Expected: `Push: Hold`.
- Required evidence: remote state is `diverged` and required repository action
  is clear.
- Result: documented.

## Case 6: Tag Recommendation

- Expected: `Tag: Recommended` only when tag name and target commit are known.
- Required behavior: Tag remains independent from Push.
- Result: documented.

## Case 7: Stale Recommendation

- Expected: recommendation invalidated and re-review required.
- Required behavior: previous recommendation is not reused after diff, branch,
  HEAD, validation, remote state, or unrelated workspace state changes.
- Result: documented.

## Case 8: Insufficient Evidence

- Expected: affected approval units are `Hold`.
- Required behavior: no inference or optimistic recommendation when validation,
  branch, or Safe Commit Set cannot be confirmed.
- Result: documented.
