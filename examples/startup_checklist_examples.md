# Startup Checklist Examples

## Purpose

この文書は、Startup Checklist System の良い例と悪い例を示します。

Examples は参考資料です。正式なルールは `docs/rules/startup_checklist_rules.md`
に従います。

## Good Example: Documentation Q

```text
Startup Checklist:
- Repository: C:\GitHub\Ghost-Development-System-Docs
- Root: C:/GitHub/Ghost-Development-System-Docs matches Working Repository
- Scope: docs/rules, docs/workflow, templates, examples, README only
- Related Repository: GameGhost is reference only
- Rules: Project First, Japanese First, Artifact First, Q File Artifact Standard
- Methodology: Knowledge Promotion
- Q artifact: request.md saved in docs/requests/gds/approved/...
- Proposal: no scope conflict; no better approach requiring user decision
- Commit: Do not commit
- Ready: Yes
```

良い理由:

- 編集対象 repository が明確。
- GameGhost を参照のみにしている。
- Q artifact の保存状態を確認している。
- Commit 禁止を開始前に確認している。
- Git root が Working Repository と一致している。
- Proactive Proposal の有無を確認している。

## Good Example: Debug / OCR Review Q

```text
Startup Checklist:
- Repository: C:\SteamAI
- Root: C:/SteamAI matches Working Repository
- Scope: review artifact generation only
- Related Repository: Ghost-Development-System-Docs is reference only
- Rules: Debug Artifact Review, Debug Escalation Ladder, Audit Before Repair
- Methodology: First Broken Step, Trace Before Tune
- Q artifact: request.md saved
- Review Entry Point: contact sheet first, then overlay, then CSV
- Proposal: algorithm change should wait until first broken step is confirmed
- Commit: Do not commit
- Ready: Yes
```

良い理由:

- Debug Artifact の review entry point が先に決まっている。
- tuning より先に trace / first broken step を確認している。
- production adoption や DB apply を暗黙に含めていない。

## Bad Example: Repository Confusion

```text
Q を見たので作業開始。
GameGhost と GDS Docs の両方を少し更新。
```

問題:

- Working Repository が確認されていない。
- Related Repository の編集可否が不明。
- Cross Project Impact が確認されていない。
- Scope Guard がない。

## Bad Example: Chat-Only Q

```text
長文 Q をチャットに貼った。
保存せずに Codex が実装した。
Completion Report に Source Q File がない。
```

問題:

- Artifact First に反している。
- Q の原文が後から確認できない。
- AI 入力欠落やコピー漏れを検出できない。

## Bad Example: Rule Skip

```text
OCR の数字が悪いので、すぐにアルゴリズムを変更した。
```

問題:

- Debug Escalation Ladder を飛ばしている。
- Human Review と Debug Artifact Review がない。
- First Broken Step が特定されていない。
- 変更理由を人間が確認できない。

## Review Checklist

- Startup Checklist が作業開始前に確認されているか。
- Repository と Scope Guard が明確か。
- Q artifact が保存されているか。
- Applicable Rules が作業内容に合っているか。
- Applicable Methodologies が作業内容に合っているか。
- Commit policy が守られているか。
