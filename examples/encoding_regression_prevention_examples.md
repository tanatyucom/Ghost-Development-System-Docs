# Encoding Regression Prevention Examples

## Bad: Full File Rewrite With Implicit Encoding

```text
Read README without specifying UTF-8.
Regenerate the whole file.
Write it back with platform default encoding.
Commit because the visible diff looks like a documentation update.
```

Problem:

- Normal Japanese text can become mojibake.
- The diff can be too large for humans to notice every corrupted line.
- The broken text enters Git history.

## Good: Minimal Patch With Validator

```text
Read the target section with UTF-8.
Apply a minimal patch.
Run:
  python scripts/validate_encoding_regression.py --staged
  git diff --cached --check
Review the diff before commit approval.
```

Result:

- New mojibake candidates block the commit.
- Human review focuses on the actual change.
- Generated reports and intentional evidence remain controlled by narrow
  exclusions.

## Bad: Broad Directory Exclusion

```text
Exclude all reports/ or docs/requests/ from mojibake scanning.
```

Problem:

- Real corruption can hide in request artifacts or reports.
- Future tasks inherit a blind spot.

## Good: Narrow Intentional Evidence Exclusion

```text
config/encoding_audit_exclusions.json:
  file: reports/legacy_document_mojibake_audit.md
  patterns: mojibake, U+FFFD
  reason: audit evidence report intentionally preserves matched samples
```

Result:

- Known evidence is preserved.
- Unrelated files remain protected by the validator.
