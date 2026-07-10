# AI Proactive Proposal Rules

## Purpose

AI Proactive Proposal Rule は、AI が単に指示を実行するだけでなく、根拠のある改善案、
時間短縮案、リスク、衝突、知識化機会を人間へ共有できるようにするための協働ルールです。

AI は勝手に実装を変更しません。提案は根拠とともに行い、最終判断はユーザーが行います。

## Core Rule

AI は、作業前または作業中に以下を検知した場合、簡潔に提案または懸念を共有してよいです。

- Time Saving Opportunity.
- Better Technical Approach.
- Repository / Scope Conflict.
- Rule Conflict.
- Methodology Conflict.
- Future Maintenance Risk.
- Knowledge Opportunity.
- Concept / CASE / Rule / Workflow candidate.
- Human Review が望ましい箇所.
- 違和感、短縮、確認事項.

## Proposal Principles

AI の提案は以下に従います。

- 勝手に実装を変更しない。
- 提案と実装を分ける。
- 根拠を示す。
- 判断をユーザーに残す。
- 緊急性または影響度を短く示す。
- 既存ルール、workflow、methodology と衝突しない形で提案する。
- 作業を止めるほどではない提案は、Recommended Improvements または Future Candidates に残す。

## When To Propose Before Implementation

実装前に提案すべき例:

- Working Repository と実際の Git root が一致しない。
- Related Repository を編集しそうになっている。
- Q が Artifact First 対象だが保存されていない。
- Audit Before Repair が必要なのに repair が始まりそう。
- Debug Escalation Ladder を飛ばして algorithm change へ進みそう。
- Migration First が必要なのに fallback を増やしそう。
- 別の短い方法で同じ目的を安全に達成できる。

## When To Propose During Implementation

実装中に提案すべき例:

- 既存文書に重複するルールがある。
- 新規追加より既存文書拡張の方が自然。
- 変更対象が当初 scope より広がっている。
- future candidate と approved work が混ざりそう。
- Completion Checklist 上、commit / tag / release 判断が曖昧。

## Proposal Output

推奨形式:

```text
Proactive Proposal:
- Observation:
- Evidence:
- Proposal:
- Impact:
- User decision needed:
```

軽い提案はチャットの短い一文でよいです。再利用可能な知識やレビュー対象になる提案は
file artifact、Recommended Improvements、Future Candidates、Concept、CASE、Rule、
Workflow 候補として残します。

## Boundaries

AI Proactive Proposal は以下を意味しません。

- AI が勝手に scope を拡張する。
- AI が Human Approval Gate を代替する。
- AI が commit / tag / release を独断で行う。
- AI が Future Candidate を approved work として実装する。
- AI がユーザーの明示指示を無視する。

## Startup Checklist Integration

Startup Checklist では以下を確認します。

- Better approach available?
- Significant time saving possible?
- Repository / Scope concern?
- Rule conflict?
- Methodology conflict?
- Knowledge opportunity detected?
- Any constructive concern?

## Related Documents

- `docs/rules/ai_collaboration_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/workflow/startup_checklist_workflow.md`
- `templates/startup_checklist_template.md`
- `templates/review_checklist.md`
- `docs/rules/completion_checklist_rules.md`
