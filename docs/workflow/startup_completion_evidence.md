# Startup Completion Evidence

## Purpose

Startup Completion Evidence は、AI が記憶や過去の会話だけに頼らず、
作業前に canonical repository source を確認したことを示す証跡です。

AI Startup Procedure と Startup Checklist は「何を確認するか」を定義します。
Startup Completion Evidence は「確認したことをどう示すか」を定義します。

## Core Rule

実装、レビュー、文書更新、Q 作成、Q 実行を始める前に、AI は Startup Completion
Gate を通過できるだけの証跡を残します。

証跡は長文ログではなく、確認対象、確認結果、使用した入口、未確認理由を短く
記録します。

## Required Evidence

- Memory Check completed.
- AI Startup Procedure reviewed.
- AI Repository Index reviewed.
- Current Mission or Current Q reviewed.
- Canonical `Q_TEMPLATE.md` reviewed, when Q creation or Q revision is involved.
- Related Rules reviewed.
- Related Workflows reviewed.
- Related ADRs or architecture docs reviewed, when relevant.
- Repository Root Validation completed.
- Scope / Out of Scope confirmed.
- Constraint Check completed.

## Evidence Format

Evidence は次の粒度で記録します。

```text
- Evidence item:
- Source checked:
- Result:
- Gap / limitation:
- Action:
```

短い作業ではチャット上の要約で十分です。再利用、レビュー、Git 管理、handoff を
前提とする場合は、`templates/startup_verification_checklist.md` を使って file
artifact として保存します。

## Gate Position

```text
AI Startup Procedure
  -> Startup Checklist
  -> Startup Completion Evidence
  -> Startup Completion Gate
  -> Q Creation / Implementation / Review
```

## Failure Conditions

次の場合、Gate は Pass にできません。

- Current Q を読んでいない。
- AI Repository Index を確認していない。
- 作業対象 repository root を確認していない。
- 関連 rules / workflows / ADRs の確認要否を判断していない。
- Scope / Out of Scope または commit policy が未確認。
- Q 作成なのに canonical `templates/Q_TEMPLATE.md` を確認していない。
- 未確認事項を「記憶しているはず」として扱っている。

## Not A Log Dump

Startup Completion Evidence は、チャット全文、巨大な command output、または
全ファイルの読み取りログではありません。

残すべきものは、未来の人間や新しい AI session が「どの公式入口を確認し、
どこに制約や未確認が残っていたか」を復元できる最小限の証跡です。

## Related Documents

- `docs/workflow/startup_completion_gate.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/startup_checklist_workflow.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `templates/startup_verification_checklist.md`
- `templates/startup_checklist_template.md`
- `templates/Q_TEMPLATE.md`
