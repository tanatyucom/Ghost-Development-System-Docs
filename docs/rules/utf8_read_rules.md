# UTF-8 Read Rules

## Purpose

UTF-8 Read Rules prevent mojibake when humans or AI read Japanese Markdown,
Q files, request artifacts, completion reports, and other text artifacts on
Windows.

The rule exists because Windows PowerShell 5.1 can misread UTF-8 files without
BOM when `Get-Content` is used without an explicit encoding.

## Core Rule

When reading Markdown, Q files, request artifacts, completion reports, or other
Japanese text artifacts with Windows PowerShell 5.1, always specify UTF-8.

Correct:

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
```

Incorrect:

```powershell
Get-Content -LiteralPath <path>
```

Codex and other AI agents must not use plain `Get-Content` for Q file reading
when the file may contain Japanese text.

## Applies To

- Q files.
- Markdown documentation.
- Request artifacts.
- Completion reports.
- Review artifacts.
- Templates.
- Roadmap, rules, workflow, examples, PIP, project profile, and history files.

## Mojibake Detection Rule

If mojibake is reported, the report must include:

- file name;
- line number;
- mojibake string;
- expected string;
- command used to read the file;
- inferred cause.

If the file can be read correctly with `Get-Content -Encoding UTF8` or Python
UTF-8 strict decoding, and no concrete line number plus mojibake string can be
shown, report:

```text
文字化けなし。過去報告はテンプレートまたは表示上の問題の可能性。
```

## Verification Commands

PowerShell UTF-8 read:

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
```

Python UTF-8 strict decode:

```bash
python -c "from pathlib import Path; Path('<path>').read_text(encoding='utf-8')"
```

Repository mojibake pattern scan:

```bash
python -c "from pathlib import Path; pats=('縺','繧','譁','荳','螟','蜿','�'); print([str(p) for p in Path('.').rglob('*.md') if any(x in p.read_text(encoding='utf-8', errors='replace') for x in pats)])"
```

## Repair Policy

Mojibake repair is allowed only when the expected original text is clear enough
to review.

Do:

- repair only verified lines;
- preserve line intent;
- record repaired files in the completion report;
- record uncertain findings in a Mojibake Audit Report.

Do not:

- perform broad one-shot encoding conversion;
- guess text when the original cannot be inferred;
- treat terminal display mojibake as file corruption without UTF-8 verification;
- edit GameGhost or another reference-only repository from a GDS Docs task.

## Decision Background

Recent Q files were valid UTF-8, but plain Windows PowerShell 5.1
`Get-Content` displayed Japanese text as mojibake such as `縺`, `繧`, and `譁`.

The files were not damaged. The reading command was wrong.

This rule turns that discovery into a repeatable safeguard so future Codex and
AI work does not report false file corruption or implement from misread Q text.

## Related Documents

- `docs/rules/language_rules.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/workflow/ai_startup_procedure.md`
- `templates/q_file_template.md`
- `templates/startup_checklist_template.md`
- `templates/completion_report_template.md`
- `docs/history/mojibake_audit_report_2026-07-10.md`
