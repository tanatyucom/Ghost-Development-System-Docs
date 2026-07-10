# Mojibake Audit Report 2026-07-10

## Purpose

この report は、Windows PowerShell 5.1 が `Get-Content` を `-Encoding UTF8`
なしで実行した場合に、UTF-8 日本語 Q file を文字化け表示することがあると
確認した後に実施した mojibake audit を記録します。

## Scope

監査対象 Markdown:

- `README.md`
- `docs/**/*.md`
- `roadmap/**/*.md`
- `templates/**/*.md`
- `examples/**/*.md`
- `pip/**/*.md`
- `project_profiles/**/*.md`
- `requests/**/*.md`

GameGhost と `C:\SteamAI` は scope 外であり、編集していません。

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

監査では、よくある日本語 mojibake marker として次を検索しました。

- `縺`
- `繧`
- `譁`
- `荳`
- `螟`
- `蜿`
- `�`

## Result

repository Markdown files には mojibake candidate は検出されませんでした。

```text
files_with_hits= 0
total_hit_lines= 0
```

UTF-8 Read Rule とこの report を追加した後は、literal detection pattern が
意図的な例として次の文書に含まれます。

- `docs/rules/utf8_read_rules.md`
- `docs/history/mojibake_audit_report_2026-07-10.md`

将来の repository-wide candidate count では、この2ファイルは除外します。
rule text 自体を監査する場合だけ対象にします。

## Repaired Files

なし。

この監査では、mojibake repair が必要な Markdown file はありませんでした。

## Unrepaired / Need Confirmation

なし。

UTF-8 verification と repository scan の結果、具体的な file、line number、
mojibake string は残りませんでした。

## Interpretation

過去の「Q本文が一部文字化け」報告は、damaged Q file や damaged repository
Markdown が原因ではなく、reading command が原因でした。

Windows PowerShell 5.1 では次を使います。

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
```

explicit UTF-8 reading で確認する前に、plain `Get-Content` の mojibake 表示を
file corruption と扱ってはいけません。

## Follow-up

UTF-8 Read Rule を追加しました。

- `docs/rules/utf8_read_rules.md`

今後の Q reading では、template と startup guidance に UTF-8 handling と
mojibake check を記録します。
