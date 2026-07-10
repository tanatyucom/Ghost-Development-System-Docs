# GameGhost Completion Policy

## Completion Report Expectations

GameGhost completion reports should include:

- Source Q File.
- Working Repository and Git root.
- Changed Files.
- Generated Files.
- Verification.
- Review Entry Point, when review artifacts exist.
- Debug Artifact Review, when applicable.
- Audit Before Repair result, when applicable.
- Safe Commit Set.
- Files intentionally excluded.
- Commit / tag / release decision.
- Remaining Issues.
- Recommended Next Q.

## Verification Expectations

Verification should match the Q scope.

Examples:

- documentation-only work: link and Markdown checks;
- OCR / visual work: artifact review, metrics, and human review when needed;
- repair work: audit classification, targeted repair, and before / after
  evidence;
- runtime work: relevant tests or executable checks named in the Q.

## Commit Policy

Do not commit GameGhost work unless the Q or user explicitly requests it.

When commit is requested, classify changed files before staging and report the
safe commit set.

## Release Policy

Do not tag or release GameGhost work unless the Q or user explicitly requests
release handling and Human Approval Gate is satisfied.

