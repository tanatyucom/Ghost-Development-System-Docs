# Validation Strategy

## Required Checks

```powershell
python scripts/validate_encoding_regression.py --all
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py
git diff --check
git status --short --untracked-files=all
```

## Staged Validation

Staged validation is only required when files are staged. This Q does not stage,
commit, push, or tag files.

## Content Checks

- `templates/Q_TEMPLATE.md` includes Artifact Creation Startup Enforcement
  evidence fields.
- `templates/completion_report_template.md` records the enforcement result.
- `templates/startup_verification_checklist.md` includes startup evidence for
  the enforcement gate.
- Gate values use `PASS`, `PASS_WITH_LIMITATION`, `BLOCK`, and `SCW_REQUIRED`.
- Q file rules and workflows reference the enforcement evidence.
- README / index files can lead users to the relevant templates and workflows.

## Encoding / Mojibake Confirmation

- `docs/workflow/startup_completion_gate.md` may look mojibake when read with
  Windows PowerShell `Get-Content` without `-Encoding UTF8`.
- UTF-8 explicit reading and Git content inspection confirm the file itself is
  not mojibake.
- Intentional mojibake examples in `docs/rules/utf8_read_rules.md` are retained
  as documentation examples.
