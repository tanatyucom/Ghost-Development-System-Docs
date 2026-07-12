# Encoding Regression Prevention Workflow

## Purpose

This workflow prevents mojibake and invalid encoding regressions from entering
GDS Docs history.

It is a commit gate and review workflow, not an automatic repair workflow.

## Standard Flow

```text
Markdown Change
  -> Explicit UTF-8 Read / Write
  -> Minimal Patch
  -> Encoding Regression Validator
  -> Human Diff Review, when large Markdown change is detected
  -> Repository Quality Audit
  -> Completion Report
  -> Commit Approval Decision
```

## Validator Commands

Repository scan:

```bash
python scripts/validate_encoding_regression.py --all
```

Staged commit gate:

```bash
python scripts/validate_encoding_regression.py --staged
```

Range investigation:

```bash
python scripts/validate_encoding_regression.py --base <commit> --target <commit-or-worktree>
```

## Local Pre-Commit Gate

Manual command:

```bash
python scripts/pre_commit_quality_gate.py
```

The local gate runs:

- `python scripts/validate_encoding_regression.py --staged`
- `git diff --cached --check`

Do not silently install Git hooks. Hook installation requires explicit human
approval.

## Bypass Policy

Bypass is allowed only with:

- explicit human approval;
- documented reason;
- completion report note;
- follow-up Q when risk remains.

## CI Gate

GitHub Actions should run the validator for push and pull request checks.

The CI gate must:

- validate UTF-8;
- reject newly introduced mojibake;
- report exact files and lines;
- respect narrow intentional evidence exclusions;
- avoid modifying files;
- avoid committing automatically.

## Editor And Line Ending Policy

`.editorconfig` defines UTF-8 and LF defaults for text files.

`.gitattributes` may define text normalization for Markdown and Python files.
Do not normalize the entire repository as an incidental side effect. If broad
line-ending churn appears, stop and create a migration Q.

## Completion Report Requirements

Record:

- validator command and result;
- before / after warning behavior;
- intentional evidence exclusions used;
- large Markdown diff review result;
- Repository Quality result;
- commit / push status.

## Related Documents

- `docs/rules/encoding_regression_prevention_rules.md`
- `docs/rules/utf8_read_rules.md`
- `docs/workflow/commit_safety_checklist.md`
- `.github/workflows/encoding-regression-validation.yml`
- `config/encoding_audit_exclusions.json`
