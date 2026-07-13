# Beginner & Future Self Test Workflow

## Purpose

Beginner & Future Self Test Workflow は、documentation review、completion
review、Q review、roadmap / decision review の中で BFS Test を軽量に実行するための
標準手順です。

BFS Test は新しい大規模 review system ではありません。既存の review checklist、
completion checklist、Completion Report Improvement Review に差し込む品質確認です。

## Standard Flow

```text
Select Artifact
  -> Identify Artifact Type
  -> Identify Reader Perspective
  -> Run BFS Test Questions
  -> Record Outcome
  -> Recommend Smallest Correction
  -> Update Artifact Or Record Non-Blocking Improvement
  -> Completion / Review Report Reflection
```

## Step Details

### Select Artifact

BFS Test は、次の artifact で特に有効です。

- Product Blueprint。
- Master Roadmap。
- Domain Roadmap。
- Execution Roadmap。
- Decision Record。
- Q Document。
- Completion Report。
- Multi-AI handoff。
- Information Package。
- major README / index。

短い一時メモ、内部作業ログ、生成途中の scratch file では `NOT APPLICABLE` にできます。

### Identify Artifact Type

artifact type を明示します。

例:

```text
Artifact Type: Completion Report
```

type が曖昧な場合、BFS Test の前に Product Documentation Hierarchy v2 または
Artifact Schema Standard で分類します。

### Identify Reader Perspective

最低1つ、必要に応じて複数選びます。

- Beginner。
- New AI Session。
- Future Self。
- Project Owner Returning After Interruption。
- Human Reviewer。

### Run BFS Test Questions

次を確認します。

- Purpose Discoverable。
- Project / Domain / Authority Discoverable。
- Current Position Discoverable。
- Why / Evidence Traceable。
- Next Action Discoverable。
- Current / Completed / Future Candidate Separation。
- Authority / Related Sources Discoverable。
- Hidden Chat Dependency。

### Record Outcome

結果は次のいずれかです。

- `PASS`
- `PASS WITH MINOR IMPROVEMENTS`
- `FAIL`
- `NOT APPLICABLE`

`PASS WITH MINOR IMPROVEMENTS` は、理解は可能だが、link、title、short summary、
Current Position、next action などの小さな改善で復帰コストを下げられる場合に使います。

`FAIL` は、artifact だけでは purpose、authority、current position、decision reason、
next action のいずれかが判断できない場合に使います。

### Recommend Smallest Correction

修正提案は最小にします。

推奨される小さな修正:

- H1 / title を明確にする。
- Purpose を1文追加する。
- Related Documents を追加する。
- Current Position を Master Roadmap に追加または更新する。
- Completion Report に Remaining Issues / Recommended Next Q を追加する。
- Future Candidates を approved scope から分離する。

避ける修正:

- すべての関連文書を全文複製する。
- Product Blueprint に一時的な進捗を追加する。
- BFS Test のためだけに別の重い review artifact を作る。

## Completion Report Reflection

BFS Test を実行した場合、Completion Report には次を記録します。

- BFS Test result。
- perspective。
- blocking / non-blocking issues。
- smallest correction applied or recommended。
- duplication avoided。

## Commit OK Review Alignment

review result が `Commit OK` で commit が必要な場合、既存の
AI Collaboration Rules に従い、AI は copy-paste-ready Git Bash commands を提示します。

この workflow は commit command rule を再定義しません。review completion 時に
既存ルールが見つかることを確認します。

## Related Documents

- `docs/rules/beginner_future_self_test_rules.md`
- `templates/beginner_future_self_test_template.md`
- `examples/beginner_future_self_test_examples.md`
- `templates/review_checklist.md`
- `templates/completion_checklist_template.md`
- `docs/workflow/completion_checklist_workflow.md`
- `docs/rules/ai_collaboration_rules.md`
