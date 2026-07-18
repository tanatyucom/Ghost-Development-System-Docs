# Startup Completion Gate

## Purpose

Startup Completion Gate は、Startup の確認結果が揃ってから Q 作成、実装、
レビュー、文書更新へ進むための verification gate です。

目的は自動強制ではなく、作業開始前に「確認済み」と「未確認」を人間と AI が
同じ状態で見られるようにすることです。

## Standard Flow

```text
Start
  -> Memory Check
  -> AI Startup Procedure
  -> AI Repository Index
  -> Current Mission / Current Q
  -> Repository Root Validation
  -> Related Rules / Workflows / ADRs
  -> Artifact Creation Startup Enforcement, when managed artifact generation is requested
  -> Constraint Check
  -> Startup Completion Evidence
  -> Gate Decision
  -> Q Creation / Implementation / Review
```

## Gate Decision

### PASS

次を満たす場合、Gate は PASS です。

- Required Evidence が揃っている。
- Repository Context Evidence が今回の作業範囲に対して十分である。
- 未確認事項がない、または未確認理由と次Actionが明記されている。
- Scope / Out of Scope が今回の作業に対して十分に明確。
- Commit / Push policy が明確。
- Q 作成または revision では canonical `templates/Q_TEMPLATE.md` を確認済み。
- 管理対象artifact生成では Artifact Creation Startup Enforcement が完了している。
- `PASS_WITH_LIMITATION` の場合、limitation と next action が記録されている。

### PASS WITH LIMITATION

次の場合、制約つきで開始できます。

- 関連文書の一部が存在しない。
- Project Profile が存在しないが、Q と repository root で範囲が確認できる。
- ADR が不要と判断できる。
- ユーザーの指示が短く、最小Startupで足りる。
- Repository Context Evidence の一部に freshness limitation があるが、今回の
  出力を無効化しない理由が記録されている。

この場合でも、limitation と理由を記録します。

### BLOCKED

次の場合、作業開始を止めます。

- repository root が不一致。
- Target Project または Working Repository が不明。
- Current Q / Mission が読めない。
- Commit禁止とCommit要求など、重大な指示矛盾がある。
- Related repository の編集可否が不明。
- Human Approval が必要な作業で承認がない。
- Artifact Creation Startup Enforcement が `BLOCK` または `SCW_REQUIRED`。
- Repository Context Evidence が欠落している。
- AI Repository Index、Current Q、canonical template、または関連rule /
  workflowを読めないままrepository-governed outputを出そうとしている。
- repository state、workflow state、approval stateが変化した後に必要な
  context refresh が行われていない。

## Required Output

Gate の結果は Completion Report または該当 artifact に記録します。

```text
Startup Completion Gate:
- Gate result:
- Evidence artifact:
- Repository context evidence:
- Freshness / invalidation check:
- Missing evidence:
- Constraint check:
- Artifact Creation Startup Enforcement:
- Ready to start:
```

## Relationship To Completion Report

Completion Report には、開始時点で Startup Completion Gate が通過したか、
どの証跡を根拠にしたかを記録します。

これにより、作業後に「AI がどの公式文書を確認した前提で作業したか」を
追跡できます。

## Out Of Scope

- 自動 enforcement。
- 自動 repository access。
- 自動 Q generation。
- 自動 commit / push。
- Startup Procedure の再設計。
- Runtime Startup Enforcement implementation.

## Related Documents

- `docs/workflow/startup_completion_evidence.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/startup_checklist_workflow.md`
- `templates/startup_verification_checklist.md`
- `templates/completion_report_template.md`
- `docs/workflow/artifact_creation_startup_enforcement_workflow.md`
- `docs/rules/artifact_creation_startup_enforcement_rules.md`
