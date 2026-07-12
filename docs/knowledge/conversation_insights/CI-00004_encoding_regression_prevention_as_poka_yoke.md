# CI-00004 Encoding Regression Prevention as Poka-Yoke

Status: Approved Insight
Source Type: Conversation Insight
Human Approval: Approved
Created Date: 2026-07-13

## Summary

文字化け再発防止は、人やAIへ注意を促すだけでは不十分である。

既存Markdownを誤ったEncodingで読み込み、全文を書き戻すことで、
正常なUTF-8日本語が大量に文字化けするEncoding Regressionが実際に発生した。

そのためGDSでは、次の仕組みを組み合わせる。

- UTF-8明示
- 長文Markdownの全文再保存を避ける
- diffベースの文字化け増分検査
- pre-commit Gate
- CI Encoding Gate
- Human Diff Review

## Key Insight

中心思想は次のとおり。

```text
気をつける
```

ではなく、

```text
壊れた状態ではCommitできない
```

という仕組みにする。

## Prevention Rules

### Explicit UTF-8

Python:

```python
path.read_text(encoding="utf-8")
path.write_text(text, encoding="utf-8")
```

PowerShell:

```powershell
Get-Content -Encoding UTF8
Set-Content -Encoding UTF8
```

Encoding指定なしの読み書きを避ける。

### Avoid Full-File Rewrite

README、Rules、Workflow、Historyなどの長文Markdownは、
全文再生成ではなく必要箇所だけをPatchする。

### Diff-Based Mojibake Gate

Repository全体の既存警告数ではなく、
今回の変更で文字化け候補が増えていないかを検査する。

代表候補:

```text
縺
繧
蜈
譁
螟
逕
謖
驥
�
<U+0080>
<U+F8F0>
```

```text
Before candidate count < After candidate count
```

ならCommit不可とする。

### Human Diff Review

大量Markdown変更時はCommit前に確認する。

```bash
git diff --cached --check
git diff --cached --word-diff
git diff --cached -- README.md docs/
```

### Pre-Commit / CI

Local GateとCI Gateで以下を確認する。

- UTF-8として読み取れる
- 置換文字が増えていない
- Mojibake Patternが増えていない
- 異常な大量再書き換えがない
- Generated file以外の全文置換がない

### Editor Configuration

`.editorconfig`等でUTF-8を明示する。

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true

[*.md]
charset = utf-8
```

## Why Preserve

このInsightは以下へ影響する。

- Repository Quality
- AI Knowledge Quality
- Documentation System v2
- AI Response Checklist
- Completion Checklist
- Commit Safety
- Pre-commit Validation
- CI Validation
- Long-term Knowledge Preservation

## Promotion Candidates

- Encoding Regression Prevention Rule
- UTF-8 Read / Write Rule
- Diff-Based Mojibake Gate
- Pre-Commit Encoding Validator
- CI Encoding Gate
- Markdown Full-Rewrite Restriction
- Repository Quality Audit Enhancement

## Non-Goals

- 既存文字化けの推測修復
- 全Markdownの一括変換
- 警告の無理なGreen化
- Commit / Pushの自動実行

## Review Status

Approved Insight

Rule / Workflow / Validator / CIへのPromotionは、
別途Human ReviewとQを経て決定する。
