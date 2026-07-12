# Legacy Document Mojibake Repair Result

- Date: 2026-07-13
- Repair execution status: canonical document repair was not executed.
- 日本語要約: 安全に自動修復できる候補が確認できなかったため、既存Markdown本文の修復は実行していません。

## Result Summary

- Scanned candidate lines: 598
- Repaired files: 0
- Repaired lines: 0
- Unresolved true candidate lines: 588
- False positive / intentional evidence lines: 10

## Reason

- AUTO_SAFE として採用できる修復候補はありませんでした。
- 代表行の逆変換テストでは、デコード失敗または句読点・文字の欠落が残りました。
- 原文ソースなしで置換すると推測修復になるため、修復は見送りました。

## Next Required Action

- P1 Critical の入口文書、Rules、Workflow、Templates から人間レビューしてください。
- 信頼できる原文または人間承認済み置換案を使い、行単位で再構築するFollow-up Qを作成してください。

## Batch 1 Manual Repair Result

- Date: 2026-07-13
- Source Q: `Q_GDS_Legacy_Document_Mojibake_Manual_Repair_Batch1_JP.md`
- Policy: Audit Before Repair / no guessed broad repair / repair only human-verifiable lines.
- Repaired files:
  - `README.md`
  - `docs/README.md`
- Repaired candidate lines: 20
- `README.md` mojibake candidate count: 185 -> 169
- `docs/README.md` mojibake candidate count: 246 -> 242
- `docs/history/knowledge_base_history.md` mojibake candidate count: 63 -> 63

### Batch 1 Repair Scope

- Repaired stable entry-point wording in `README.md`.
- Repaired UTF-8 reading guidance in `README.md`.
- Repaired short standard-flow labels in `README.md`.
- Repaired Japanese documentation policy wording in `docs/README.md`.
- Repaired explicit Conversation Insight approval examples in `README.md` and `docs/README.md`.

### Batch 1 Remaining Issues

- Large paragraphs with lossy reverse-conversion artifacts remain unresolved.
- Lines that produced `、E`, `めE`, or other missing-character traces were not repaired.
- `docs/history/knowledge_base_history.md` was not repaired in Batch 1 because candidate lines require stronger source confirmation.

## Batch 2 Manual Repair Result

- Date: 2026-07-13
- Source Q: `Q_GDS_Legacy_Document_Mojibake_Manual_Repair_Batch2_JP.md`
- Policy: Audit Before Repair / no guessed repair / restore only from trusted repository history.
- Trusted source: commit `8e6f700` (`docs: add daily knowledge review and context-aware suggestions`) because target files had 0 mojibake candidates there.
- Repaired files:
  - `README.md`
  - `docs/README.md`
  - `docs/history/knowledge_base_history.md`
- Batch2 target candidate counts:
  - `README.md`: 169 -> 0
  - `docs/README.md`: 242 -> 0
  - `docs/history/knowledge_base_history.md`: 63 -> 0
- Total Batch2 target candidates repaired or removed by trusted restore: 474

### Batch 2 Repair Scope

- Restored `README.md` from the trusted clean history version and preserved the current `Completion Report Standard v2` and `Q File Template And Naming Standard` sections.
- Restored `docs/README.md` from the trusted clean history version and preserved the current `Completion Report Standard v2 Index` and `Q File Template And Naming Standard Index` sections.
- Restored `docs/history/knowledge_base_history.md` from the trusted clean history version because the current file's mojibake was introduced in the later completion-report update commit.

### Batch 2 Remaining Issues

- Other files outside the Batch2 priority scope may still contain mojibake candidates.
- Completion Report v2 historical narrative from the broken history update was not reconstructed in `docs/history/knowledge_base_history.md`; the safe record for this repair is kept in this repair result and the Batch2 completion report.

## Batch 3 Recovery Result - Rules / Workflow

Date: 2026-07-13

Scope:

- `docs/workflow/startup_checklist_workflow.md`
- `docs/workflow/README.md`
- `docs/rules/rules.md`
- `examples/migration_first_examples.md`

Method:

- Trusted Git history versions were used as source of truth.
- No inference-based Japanese reconstruction was used.
- Valid additions from regression commits were manually preserved when they were clear from the diff.

| File | Section / Line Range | Regression Commit | Trusted Source Commit | Restored Text Source | Later Changes Preserved | Human Review Result |
| --- | --- | --- | --- | --- | --- | --- |
| `docs/workflow/startup_checklist_workflow.md` | Whole file, especially Purpose, checklist steps, Q/Artifact, Conversation Insight, Knowledge Suggestion, Research Task, Completion Criteria | `9bb3344` | `9bb3344^` | Clean parent text merged with valid `9bb3344` Q naming additions | Q ID / Naming Confirmation, Q Template Required Fields, q_file_naming_rules, q_file_template_rules, Q workflow links | Restored from trusted history; no mojibake candidates remain |
| `docs/workflow/README.md` | Contains list, Standard Development Flow, Debug Artifact Review, Q Artifact Workflow, PIP Update, Related Documents | `eb80ac1` | `eb80ac1^` | Clean parent text merged with valid `eb80ac1` and `9bb3344` workflow references | Completion Report v2, Q File Creation Workflow, Q Revision / Addendum Workflow, updated request workspace naming | Restored from trusted history; no mojibake candidates remain |
| `docs/rules/rules.md` | Rule Organization, Official Rule Documents, Conversation Insight Capture, Project First, Japanese First | `9bb3344` | `9bb3344^` | Clean parent text merged with valid `9bb3344` rule index additions | Completion Report Standard, Q File Artifact Standard, Q File Naming, Q File Template Standard | Restored from trusted history; no mojibake candidates remain |
| `examples/migration_first_examples.md` | Whole file and Completion Report Example | `9bb3344` | `9bb3344^` | Clean parent text merged with valid request workspace naming update | `docs/requests/<project>/<status>/<Q_ID>_<short_topic>/` example | Restored from trusted history; no mojibake candidates remain |

Candidate count:

| File | Before | After |
| --- | ---: | ---: |
| `docs/workflow/startup_checklist_workflow.md` | 366 | 0 |
| `docs/workflow/README.md` | 80 | 0 |
| `docs/rules/rules.md` | 89 | 0 |
| `examples/migration_first_examples.md` | 205 | 0 |
