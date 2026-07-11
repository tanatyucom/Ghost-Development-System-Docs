# Steam OCR Existing Debug Rule Update Completion Report

## Summary

Steam OCR Knowledge Promotion Candidate Reviewで承認対象となったDebug Rule更新候補を、新規Ruleとして増やさず、既存Ruleへ統合しました。

Commit / Pushは実行していません。GameGhostも編集していません。

## Updated Files

```text
docs/rules/debug_artifact_review_rules.md
docs/rules/debug_escalation_ladder_rules.md
docs/rules/audit_before_repair_rules.md
docs/rules/quality_rules.md
docs/rules/repository_root_validation_rules.md
docs/rules/git_rules.md
docs/rules/core_principles.md
docs/workflow/first_broken_step_methodology.md
reports/repository_quality_report.md
reports/steam_ocr_existing_debug_rule_update_mapping.md
reports/steam_ocr_existing_debug_rule_update_completion_report.md
```

## Classification Decisions

| Area | Decision |
|---|---|
| Metrics / Human Observation conflict | Existing Rule Update |
| Trace Before Tune | Existing Rule / Methodology Merge |
| First Broken Step | Existing Rule / Methodology Merge |
| Intermediate Artifact Review | Existing Rule Update |
| Representative Sample / Dataset | Quality Rule Update |
| Detection / Recognition separation | Debug Escalation / Audit Rule Update |
| Negative Result preservation | Core / Debug / Audit Rule Update |
| Repository / Branch / Remote before Git commands | Repository Root / Git Rule Update |
| OCR-specific parameters | Excluded from GDS common Rule |

## Why No New Rule Was Needed

既存Ruleで表現できたため、新規Ruleは不要と判断しました。

- Debug Artifact Review RulesはIntermediate Artifact、Review Entry Point、Expected Stateを受け止められる。
- Debug Escalation Ladder RulesはTrace Before Tune、First Broken Step、Root Cause前Gateを受け止められる。
- Audit Before Repair Rulesはrepair前の監査・分離・evidence保存を受け止められる。
- Quality RulesはRepresentative Sample / Datasetを受け止められる。
- Repository Root Validation Rules / Git RulesはGit操作前確認を受け止められる。
- Core PrinciplesはMetrics、Human Approval、Negative Resultの哲学的な受け止め先になる。

## Important Wording Decision

避けた表現:

```text
人間の目視判断がMetricsより常に優先される、という趣旨の表現
```

採用表現:

```text
MetricsとHuman Observationが矛盾した場合は、どちらかを即時に正しいと判断しない。
採用を停止し、Pipeline Traceと再検証を行う。
```

## Verification

```text
python scripts\generate_ai_repository_index.py --validate: PASS
python scripts\repository_quality_audit.py: PASS / Green (10 passed, 0 warnings, 0 errors)
git diff --check: PASS
git status --short: PASS / expected uncommitted documentation changes only
dangerous wording check: PASS
OCR-specific parameter exclusion check: PASS
GameGhost edit check: PASS / no GameGhost files edited
Commit / Push: not executed
```

`git diff --check`では、既存tracked Markdownに対するLF/CRLF warningのみ表示されました。空白エラーはありません。

## Navigation / Index Decision

本Qでは新規Ruleを増やさず、既存Rule本文へ統合しました。

`python scripts\generate_ai_repository_index.py --validate` はPASSしています。今回追加したreport名は `docs/ai_repository_index.md` の直接エントリとしては表示されていませんが、Repository Index validation上の不整合はありません。

## Improvement Review

良かった点:

- Steam OCR固有のcrop値やscore値をGDS共通Ruleへ混ぜずに済んだ。
- Human ObservationをMetricsより上位に置く危険な表現を避けられた。
- Candidate Generation、Detection、Recognition、Scoring、Selectionを分ける観点を既存Debug導線へ統合できた。

注意点:

- Candidate Generation Before Scoringは、今後さらに汎用Methodology化できる余地があります。
- Human Approval Artifactの標準形式は今回のScope外です。

## Recommended Improvements

- Human Review / Approval Artifactの標準テンプレート化。
- Research Mission Workflowで、metric conflict時の再調査依頼フォーマットを整備。
- Knowledge Promotion Request Templateに「既存RuleへのMerge候補」欄を追加。

## Future Candidates

- GDS Research Mission Workflow and Template
- GDS Knowledge Promotion Request Template
- Steam OCR CASE Finalization

## Remaining Issues

- Steam OCR CASE最終化は未実施。
- Platform Registry更新は未実施。
- New Template / New Workflow追加はScope外のため未実施。

## Recommended Next Q

```text
Q_GDS_Steam_OCR_CASE_Finalization_JP
```

または:

```text
Q_GDS_Research_Mission_Workflow_and_Template_JP
Q_GDS_Knowledge_Promotion_Request_Template_JP
```

## Suggested Commit Message

```text
docs: update existing debug rules from steam ocr knowledge
```
