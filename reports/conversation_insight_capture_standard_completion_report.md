# Conversation Insight Capture Standard Completion Report

## Priority Summary

- Summary: Conversation Insight を GDS の正式な Rule / Workflow / pre-promotion Knowledge Source として追加し、Startup Procedureへ統合した。
- Verification: Green.
- Remaining Issues: Command Center自動検出、Insight Promotion Review、Knowledge Mining DashboardはFuture Candidate。
- Recommended Next Q: `Q_GDS_Conversation_Insight_Promotion_Review_Template_JP.md`

## Source Q File

- Q artifact path: `docs/requests/gds/draft/GDS-CONVERSATION-INSIGHT-001_capture_standard/request.md`
- Q artifact format: Markdown
- Q artifact version: 1.0
- Q artifact status: Draft
- Q saved in Task Artifact Workspace before implementation: Yes

## Artifact Workspace

- Artifact Workspace path: `docs/requests/gds/draft/GDS-CONVERSATION-INSIGHT-001_capture_standard/`
- Status folder: `draft`
- Request ID / Task ID: `GDS-CONVERSATION-INSIGHT-001`
- Task workspace form: Full workspace
- `request.md` present: Yes
- `completion_report.md` saved beside `request.md`: Yes
- `notes.md` present or intentionally omitted: Present
- `attachments/` present or intentionally omitted: Present

## Changed Files

- `README.md`
- `docs/README.md`
- `docs/ai_repository_index.md`
- `docs/rules/README.md`
- `docs/rules/rules.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/knowledge/README.md`
- `docs/knowledge/conversation_insights/README.md`
- `docs/workflow/README.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/startup_checklist_workflow.md`
- `docs/workflow/conversation_insight_capture_workflow.md`
- `templates/README.md`
- `templates/startup_checklist_template.md`
- `templates/conversation_insight_template.md`
- `examples/README.md`
- `examples/conversation_insight_examples.md`
- `reports/repository_quality_report.md`
- `reports/conversation_insight_capture_standard_completion_report.md`
- `docs/requests/gds/draft/GDS-CONVERSATION-INSIGHT-001_capture_standard/request.md`
- `docs/requests/gds/draft/GDS-CONVERSATION-INSIGHT-001_capture_standard/notes.md`
- `docs/requests/gds/draft/GDS-CONVERSATION-INSIGHT-001_capture_standard/completion_report.md`

## Output Artifacts

- Workflow:
  `docs/workflow/conversation_insight_capture_workflow.md`
- Rule:
  `docs/rules/conversation_insight_capture_rules.md`
- Storage README:
  `docs/knowledge/conversation_insights/README.md`
- Template:
  `templates/conversation_insight_template.md`
- Examples:
  `examples/conversation_insight_examples.md`
- Completion report:
  `reports/conversation_insight_capture_standard_completion_report.md`

## Summary

Conversation Insight を、Research MissionやCASEになる前のpre-promotion knowledge
として定義した。

Revisionで、Conversation Insight Capture Rulesを正式追加し、AI Startup Procedure、
Startup Checklist Rules、Startup Checklist Workflow、Startup Checklist Templateへ
Conversation Insight Detectionを統合した。

標準フロー:

```text
Conversation
  -> Conversation Insight Candidate
  -> Human Approval To Draft
  -> Conversation Insight Artifact
  -> Review
  -> Future Candidate
  -> Rule / Architecture / Workflow / Roadmap / Concept / CASE
```

## AI Behavior

- AI may propose candidates.
- AI must not auto-save.
- Draft generation requires explicit Human Approval such as `保存して` or `書いといて`.
- AI must not preserve full chat logs.
- Draft Conversation Insights are separated from approved knowledge.

## Future Candidates

- Command Centerによる Candidate 自動検出。
- Insight Promotion Review。
- Knowledge Mining Dashboard。

## Verification

```text
PASS: python scripts/generate_ai_repository_index.py --write
PASS: python scripts/generate_ai_repository_index.py --validate
PASS: python scripts/repository_quality_audit.py
PASS: Repository Quality Audit Green (10 passed, 0 warnings, 0 errors)
```

## Improvement Review

良かった点:

- 通常のQやResearch Missionになりにくい設計思想を保存する経路を作れた。
- AI自動保存を禁止し、Human Approvalを明示できた。
- Future Candidateとapproved scopeを分離できた。

注意点:

- 保存対象が広がりすぎるとKnowledge noiseになる。
- Duplicate Checkを怠ると既存RuleやWorkflowと重複する。

## Recommended Improvements

- Conversation Insight Promotion Review Templateを追加する。
- Conversation Insight ID namingを必要に応じて標準化する。
- Command Centerが候補を提案する場合も、Human Approval必須を維持する。
- Startup Checklistの実運用例にConversation Insight Detectionの記入例を追加する。

## Remaining Issues

- Command Center自動検出は未実装。
- Insight Promotion Reviewは未整備。
- Knowledge Mining Dashboardは未整備。

## Recommended Next Q

```text
Q_GDS_Conversation_Insight_Promotion_Review_Template_JP.md
```

## Suggested Commit Message

```text
docs: add conversation insight capture standard
```
