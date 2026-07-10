# UTF-8 Read Rules

## Purpose

UTF-8 Read Rules は、人間または AI が Windows 上で日本語 Markdown、Q file、
request artifact、completion report、その他の text artifact を読むときの
文字化けを防ぐためのルールです。

Windows PowerShell 5.1 では、BOM なし UTF-8 file を `Get-Content` だけで読むと
誤った encoding として解釈されることがあります。

## Core Rule

Windows PowerShell 5.1 で Markdown、Q file、request artifact、completion report、
その他の日本語 text artifact を読む場合は、必ず UTF-8 を明示します。

正しい例:

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
```

避ける例:

```powershell
Get-Content -LiteralPath <path>
```

Codex や他の AI agent は、日本語を含む可能性がある Q file を読むときに
plain `Get-Content` を使ってはいけません。

## Applies To

- Q file。
- Markdown documentation。
- Request artifact。
- Completion report。
- Review artifact。
- Template。
- Roadmap、rules、workflow、examples、PIP、project profile、history file。

## Mojibake Detection Rule

文字化けを報告する場合は、必ず次を含めます。

- file name。
- line number。
- mojibake string。
- expected string。
- command used to read the file。
- inferred cause。

`Get-Content -Encoding UTF8` または Python UTF-8 strict decoding で正しく読め、
具体的な line number と mojibake string を提示できない場合は、次のように報告します。

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

mojibake repair は、期待される原文が review 可能な程度に明確な場合だけ行います。

Do:

- verified line だけを修正する。
- 行の意図を維持する。
- repaired files を Completion Report に記録する。
- 推定不能な finding は Mojibake Audit Report に記録する。

Do Not:

- broad one-shot encoding conversion を行わない。
- 原文を推定できない text を推測で修正しない。
- UTF-8 verification なしに terminal display mojibake を file corruption と扱わない。
- GDS Docs task から GameGhost や reference-only repository を編集しない。

## Decision Background

直近の Q file は valid UTF-8 でしたが、Windows PowerShell 5.1 の plain
`Get-Content` により、日本語が `縺`、`繧`、`譁` などの mojibake として表示されました。

file は破損していませんでした。誤っていたのは reading command です。

このルールは、その発見を再利用可能な safeguard にし、将来の Codex / AI 作業で
false file corruption report や misread Q text に基づく実装を防ぐためのものです。

## Related Documents

- `docs/rules/language_rules.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/workflow/ai_startup_procedure.md`
- `templates/q_file_template.md`
- `templates/startup_checklist_template.md`
- `templates/completion_report_template.md`
- `docs/history/mojibake_audit_report_2026-07-10.md`
