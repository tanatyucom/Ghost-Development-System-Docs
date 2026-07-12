# Encoding Regression Prevention Rules

## Purpose

Encoding Regression Prevention Rules turn the legacy mojibake recovery work into
a commit-time poka-yoke.

The goal is not "be careful." The goal is:

```text
Commit Not Allowed when Markdown encoding regression is detected.
```

## Core Rule

Canonical Markdown must remain valid UTF-8 and must not gain new mojibake
candidates, Unicode replacement characters, suspicious control characters, or
private-use characters.

This rule extends `utf8_read_rules.md`. UTF-8 Read Rules prevent false
corruption reports during reading. Encoding Regression Prevention prevents
damaged text from entering Git history.

## Explicit UTF-8 Read / Write

Scripts and documented commands that read or write canonical Markdown must
specify UTF-8 explicitly.

Python:

```python
path.read_text(encoding="utf-8")
path.write_text(text, encoding="utf-8")
```

PowerShell:

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
Set-Content -LiteralPath <path> -Encoding UTF8
```

Encoding-unspecified reads or writes are prohibited for canonical Markdown.

## Minimal Patch Default

For canonical Markdown such as README, rules, workflow, templates,
architecture, roadmap, history, and request artifacts, the default edit method
is a minimal patch.

Avoid:

```text
Read entire file
  -> Regenerate entire file
  -> Rewrite entire file
```

Prefer:

```text
Read target section
  -> Apply minimal patch
  -> Review diff
```

A full-file rewrite requires explicit justification in notes or the completion
report.

## Generated Files

Generated files must not be manually repaired.

Examples:

- `docs/ai_repository_index.md`
- `reports/repository_quality_report.md`

Repair the source document or generator logic, then regenerate the generated
file.

## Mojibake Increase Blocker

Existing historical evidence does not justify new regressions.

Before commit approval, compare the base state and staged state. If mojibake
candidates increase, commit is not allowed.

Required command:

```bash
python scripts/validate_encoding_regression.py --staged
```

Repository scan:

```bash
python scripts/validate_encoding_regression.py --all
```

## Replacement Character Blocker

New `U+FFFD` replacement characters are blockers unless they are in a narrowly
approved intentional evidence location.

Do not replace `U+FFFD` by guess. If it is true corruption, recover the original
text from trusted source history or human-approved replacement text.

## Intentional Evidence Exclusions

Audit samples and historical evidence may intentionally contain mojibake
patterns.

Exclusions must be:

- file-specific;
- pattern-specific;
- documented in `config/encoding_audit_exclusions.json`;
- reviewed;
- unable to hide unrelated source corruption.

Directory-wide exclusions are prohibited.

## Human Diff Review

Large Markdown changes require human diff review before commit approval.

Signals include:

- high changed-line count;
- whole-file rewrite ratio;
- multiple canonical documents rewritten in one task.

Recommended commands:

```bash
git diff --cached --check
git diff --cached --word-diff
git diff --cached -- README.md docs/
```

## Commit Gate

Encoding validation runs before commit approval.

Failure means:

```text
Commit Not Allowed
```

The validator does not commit, push, or repair files automatically.

## Related Documents

- `docs/rules/utf8_read_rules.md`
- `docs/rules/git_rules.md`
- `docs/workflow/encoding_regression_prevention_workflow.md`
- `docs/workflow/commit_safety_checklist.md`
- `scripts/validate_encoding_regression.py`
- `config/encoding_audit_exclusions.json`
- `tests/test_validate_encoding_regression.py`
