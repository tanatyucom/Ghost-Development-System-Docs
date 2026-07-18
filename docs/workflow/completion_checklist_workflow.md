# Completion Checklist Workflow

## Purpose

Completion Checklist Workflow は、作業終了時に verification、review、
completion report、Improvement Review、commit / tag / release 判断、次の Q、
workspace clean confirmation を確認する標準フローです。

Startup Checklist が開始時の確認を担当し、Completion Checklist が終了時の確認を
担当します。

Completion Checklist の結果を Platform Execution Evidence として扱う場合は、
`docs/architecture/completion_review_execution_evidence_specialization.md` に従います。
このspecializationでは、Completion Reportを人間向けartifact、Completion Review
Evidenceをplatform判断用の記録として分離します。

## Standard Flow

```text
Implementation
  -> Verification
  -> Review
  -> Completion Report
  -> Completion Report v2 Section Check
  -> Completion Checklist
  -> End-of-Session Review / Memory Candidate Check
  -> Pre-Response Verification Gate
  -> Commit / Tag / Release Decision
  -> Recommended Next Q
  -> End
```

## Step Details

### Verification

実行結果、未実行項目、失敗項目、未測定項目を記録します。

### Review

人間レビュー、Debug Artifact Review、Human Approval Gate、Future Candidate 分離が
必要か確認します。

重要な documentation artifact、roadmap、decision、Q、Completion Report、
handoff、README / index では、Beginner & Future Self Test が必要か確認します。
必要な場合は `PASS`、`PASS WITH MINOR IMPROVEMENTS`、`FAIL`、`NOT APPLICABLE`
のいずれかを記録します。

Context Recovery Principle の観点で、何も覚えていない人や新しい AI session が
safe resume できるか確認します。できない場合は、Current Position、Decision
Record、Completion Report、canonical entry point、README navigation、recovery
procedure、explicit next action、Human Approval boundary、known blocker、last
verified state など、最小の recovery aid を記録します。

### Completion Report

Completion Report が必要な作業では、`templates/completion_report_template.md` と
`docs/rules/completion_report_rules.md` に従い、Identity、Changed Files、Summary、
Verification、Safe Commit Set、Commit / Push Status、Project Edit Status、Improvement
Review、Lessons Learned、Reusable Assets Created、Remaining Issues、Recommended
Improvements、Future Candidates、Recommended Next Q、Suggested Commit Message を記録します。

### Completion Checklist

完了前に `templates/completion_checklist_template.md` または Completion Report 内の
Completion Checklist 欄を確認します。

AI Repository Index update decision は必ず確認します。
Documentation Synchronization Gate も、Markdown文書を追加・移動・改名・大幅更新
した場合は必ず確認します。
Pending Insight を作成・更新・解消した場合は、Pending状態でCodex実行していないこと、
Human Review decision、cleanup confirmation を必ず確認します。
セッション終了時に Lost Context Risk がある場合は、Memory Candidate の作成、
保留、不要判断を記録します。

```text
Public AI knowledge entry point changed?
  -> Yes: regenerate docs/ai_repository_index.md and validate
  -> No: record not required reason
  -> Review Required: stop and request review before completion
```

```text
Documentation entry point changed?
  -> Yes: update README / folder index, regenerate AI Repository Index,
          run Repository Quality Audit
  -> No: record not required reason
  -> Review Required: stop before commit approval
```

```text
Pending Insight changed?
  -> Yes: record decision, Codex restriction, and cleanup status
  -> No: record not required reason
  -> Review Required: stop before Codex execution or commit approval
```

### Pre-Response Verification Gate

Completion Checklist の後、最終回答を出す直前に
`docs/workflow/pre_response_verification_gate.md` を確認します。

確認すること:

- Startup Completion Evidence が通過済み、または制約が記録されている。
- repository scope、output format、language preference が合っている。
- Revision-first policy、Human Approval boundary、Commit / Push boundary が守られている。
- Scope creep がない。
- Constraint Check がまだ有効。
- Changed Files、verification result、remaining issues が最終回答と一致している。

### Commit / Tag / Release Decision

Commit、Tag、Release は自動的に実行しません。Q、Human Approval、release policy、
repository state に基づいて必要性と実行有無を分けて記録します。

### Recommended Next Q

残課題、Future Candidate、追加レビュー、次の実装単位がある場合、Recommended Next Q
を明示します。

## Minimal Completion Checklist

短い作業では、以下の最小形式でよいです。

```text
Completion Checklist:
- Verification Completed:
- Review Completed:
- Completion Report Completed:
- Completion Report v2 Required Sections Checked:
- Improvement Review Completed:
- Commit Required:
- Commit Executed:
- Tag Required:
- Tag Executed:
- Release Required:
- Release Published:
- Recommended Next Q:
- Workspace Clean Confirmation:
- AI Repository Index Update Decision:
- AI Repository Index Regenerated:
- AI Repository Index Validation Passed:
- Documentation Synchronization Required:
- Documentation Synchronization Gate Passed:
- Pending Insight Review Required:
- Pending Insight Decision:
- Pending Insight Cleanup:
- End-of-Session Review Completed:
- Lost Context Risk:
- Memory Candidate Review Required:
- Memory Candidates Captured:
- MC required before closing:
- Beginner & Future Self Test Required:
- Beginner & Future Self Test Result:
- Context Recovery Principle Reviewed:
- Missing Recovery Aid:
- Pre-Response Verification Gate:
- Final Response Ready:
```

## Completion Criteria

- Verification が完了または未実行理由付きで記録されている。
- Review が完了または必要性なしとして記録されている。
- BFS Test が必要な artifact では、結果と blocking / non-blocking issue が
  記録されている。
- Completion Report が必要な場合、完了している。
- Improvement Review が完了している。
- Commit / Tag / Release の必要性と実行有無が分かれている。
- Recommended Next Q がある場合、明示されている。
- Workspace clean confirmation または dirty state が記録されている。
- AI Repository Index update decision が Yes / No / Review Required のいずれかで記録されている。
- public AI knowledge entry point が変わった場合、`docs/ai_repository_index.md` が再生成・検証されている。
- documentation entry point が変わった場合、README / index 更新、AI Repository Index、Repository Quality Audit の同期結果が記録されている。
- Pending Insight が変わった場合、Human Review decision、Codex execution restriction、cleanup status が記録されている。
- Lost Context Risk がある場合、Memory Candidate の作成、保留、不要判断が記録されている。
- Pre-Response Verification Gate が PASS または PASS WITH LIMITATION になっている。

## Related Documents

- `docs/rules/completion_checklist_rules.md`
- `docs/architecture/completion_review_execution_evidence_specialization.md`
- `templates/completion_checklist_template.md`
- `examples/completion_checklist_examples.md`
- `templates/completion_report_template.md`
- `docs/rules/completion_report_rules.md`
- `docs/workflow/completion_report_workflow.md`
- `docs/workflow/documentation_synchronization_workflow.md`
- `docs/workflow/pending_conversation_insight_review_workflow.md`
- `docs/rules/pending_conversation_insight_review_rules.md`
- `docs/workflow/memory_candidate_workflow.md`
- `docs/rules/memory_candidate_rules.md`
- `templates/memory_candidate_template.md`
- `docs/workflow/pre_response_verification_gate.md`
- `examples/completion_report_examples.md`
- `templates/review_checklist.md`
- `docs/rules/beginner_future_self_test_rules.md`
- `docs/workflow/beginner_future_self_test_workflow.md`
- `templates/beginner_future_self_test_template.md`
- `docs/workflow/commit_safety_checklist.md`
- `templates/ai_response_checklist_v2.md`
- `templates/response_verification_checklist.md`
- `docs/rules/git_rules.md`
- `docs/workflow/startup_checklist_workflow.md`
