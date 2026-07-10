# AI Daily Operation Cycle

## Purpose

AI Daily Operation Cycle は、AI と人間が同じ運用サイクルで GDS 作業を
開始し、実装し、検証し、完了し、知識を更新し、次の Q へ進むための
標準 workflow です。

この文書は新しい単独ルールを増やすものではありません。既存の AI Startup
Procedure、Startup Checklist、Completion Checklist、Knowledge Poka-Yoke、
AI Proactive Proposal、Collaborative Decision、AI Repository Index、
Project Profile を 1 本の運用サイクルとして接続します。

## Standard Cycle

```text
AI Startup Procedure
  -> Current Q Review
  -> Implementation
  -> Verification
  -> Human Review
  -> Completion Checklist
  -> Commit / Push
  -> Knowledge Update
  -> Repository Update
  -> Next Q Planning
  -> Next Startup
```

## Step Details

### 1. AI Startup Procedure

作業開始前に AI Startup Procedure を実行します。

確認すること:

- AI Repository Index.
- Repository Root Validation.
- GDS Core Rules / Workflow.
- Target Project Profile.
- Current Q File.
- Startup Checklist.
- Scope / Out of Scope.

### 2. Current Q Review

Current Q を読み、今回の作業範囲を確定します。

確認すること:

- Target Project.
- Working Repository.
- Single Source Of Truth.
- Related Repository.
- Scope Guard.
- Do / Do Not.
- Completion Criteria.
- Commit policy.
- Required artifacts.

Q が Artifact First 対象の場合、保存済み artifact を authoritative source とします。

### 3. Implementation

受け入れられた scope のみを実装します。

AI は、より良い方法、時間短縮、repository / scope conflict、rule conflict、
methodology conflict、maintenance risk、knowledge opportunity を見つけた場合、
AI Proactive Proposal として報告します。勝手に scope を広げません。

判断が分かれる場合は Collaborative Decision を使います。

### 4. Verification

変更後に、Q の Completion Criteria に対して検証します。

確認すること:

- changed files.
- scope boundary.
- out-of-scope files.
- generated artifacts.
- index / template / workflow consistency.
- `git diff --check`.
- task-specific validation command.

### 5. Human Review

人間の確認が必要な成果物、設計判断、修正候補、Debug Artifact、release 判断、
rule standardization は Human Review を通します。

レビュー入口が複数ある場合、Completion Report に Review Entry Point を記録します。

### 6. Completion Checklist

作業完了前に Completion Checklist を実行します。

確認すること:

- verification result.
- review result.
- completion report.
- Improvement Review.
- commit required / executed.
- tag required / executed.
- release required / published.
- Recommended Next Q.
- workspace clean state.

### 7. Commit / Push

Q が commit を許可している場合のみ commit / push します。

確認すること:

- dirty workspace review.
- unrelated files.
- safe commit set.
- commit message.
- push policy.

Q が `Do not commit` の場合、commit / push は実行しません。

### 8. Knowledge Update

作業から再利用可能な学びが出た場合、適切な場所へ昇格または候補化します。

候補:

- Rule.
- Workflow.
- Template.
- Example.
- Architecture.
- Glossary.
- PIP Case.
- Concept.
- Roadmap Future Candidate.

Knowledge Poka-Yoke の観点で、繰り返し忘れそうな手順は checklist、template、
validation、artifact、review、automation candidate に変換します。

### 9. Repository Update

公開 knowledge entry point が増えた場合、AI Repository Index を再生成・検証します。

標準コマンド:

```bash
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
```

Repository Update には、README / docs index / workflow index / rules index /
history / template references の整合確認も含みます。

### 10. Next Q Planning

未解決項目、推奨改善、Future Candidate、次に実行すべき作業を整理します。

出力すること:

- Remaining Issues.
- Recommended Improvements.
- Future Candidates.
- Recommended Next Q.
- Suggested Commit Message.

### 11. Next Startup

次の Q は、前回の Completion Report、Recommended Next Q、更新された
Knowledge Base を入力として、再び AI Startup Procedure から開始します。

## Cycle Boundaries

AI Daily Operation Cycle は、日次または連続作業の運用モデルです。

It does not replace:

- AI Startup Procedure.
- Startup Checklist.
- Completion Checklist.
- Project Profile.
- Q File.
- Human Approval Gate.
- Commit approval.
- Release approval.

## Future Extension

将来、次の機能と接続できます。

- Command Center.
- Daily Health Dashboard.
- Repository Health Score.
- Automation Tasks.
- Release Workflow.

これらは Future Extension であり、この workflow だけでは実装承認になりません。

## Related Documents

- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/startup_checklist_workflow.md`
- `docs/workflow/completion_checklist_workflow.md`
- `docs/workflow/collaborative_decision_workflow.md`
- `docs/workflow/commit_safety_checklist.md`
- `docs/rules/workflow_rules.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/rules/completion_checklist_rules.md`
- `docs/rules/ai_proactive_proposal_rules.md`
- `docs/rules/core_principles.md`
- `docs/ai_repository_index.md`
- `project_profiles/README.md`
- `templates/q_file_template.md`
- `templates/completion_report_template.md`
