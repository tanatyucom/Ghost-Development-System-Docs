# Mojibake Audit Report 2026-07-10

## Purpose

This report records the mojibake audit performed after identifying that
Windows PowerShell 5.1 can misread UTF-8 Japanese Q files when `Get-Content`
is used without `-Encoding UTF8`.

## Scope

Audited Markdown files under:

- `README.md`
- `docs/**/*.md`
- `roadmap/**/*.md`
- `templates/**/*.md`
- `examples/**/*.md`
- `pip/**/*.md`
- `project_profiles/**/*.md`
- `requests/**/*.md`

GameGhost and `C:\SteamAI` were out of scope and were not edited.

## Commands Used

Q file UTF-8 read:

```powershell
Get-Content -LiteralPath C:\Users\tanat\Downloads\Q_GDS_UTF8_Read_Rule_and_Mojibake_Audit_JP.md -Encoding UTF8
```

Repository mojibake pattern scan:

```bash
python -c "from pathlib import Path; pats=('縺','繧','譁','荳','螟','蜿','�'); files=[]; hits=[]; ..."
```

Python UTF-8 strict decode check:

```bash
python -c "from pathlib import Path; [p.read_text(encoding='utf-8') for p in Path('.').rglob('*.md')]"
```

## Detection Patterns

The scan searched for common Japanese mojibake markers:

- `縺`
- `繧`
- `譁`
- `荳`
- `螟`
- `蜿`
- `�`

## Result

No mojibake candidates were detected in repository Markdown files.

```text
files_with_hits= 0
total_hit_lines= 0
```

After adding the UTF-8 Read Rule and this report, the literal detection
patterns appear intentionally in:

- `docs/rules/utf8_read_rules.md`
- `docs/history/mojibake_audit_report_2026-07-10.md`

Those intentional examples should be excluded from future repository-wide
candidate counts unless the audit is specifically checking the rule text
itself.

## Repaired Files

None.

No Markdown file required mojibake repair during this audit.

## Unrepaired / Need Confirmation

None.

No concrete file, line number, or mojibake string remained after UTF-8
verification and repository scan.

## Interpretation

The previous "Q本文が一部文字化け" reports were caused by the reading command,
not by damaged Q files or damaged repository Markdown.

For Windows PowerShell 5.1, use:

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
```

Do not treat plain `Get-Content` mojibake as file corruption until the file has
also been checked with explicit UTF-8 reading.

## Follow-up

The UTF-8 Read Rule was added as:

- `docs/rules/utf8_read_rules.md`

Templates and startup guidance were updated so future Q reading records UTF-8
handling and mojibake checks.
