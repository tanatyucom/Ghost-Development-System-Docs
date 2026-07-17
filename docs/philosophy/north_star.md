# GDS North Star

**Status:** Draft Philosophy Standard

**Last Updated:** 2026-07-17

## North Star

AIは判断と推奨を支援する。

実行前には、対象Actionを明示して人間へ承認を求める。

人間の承認は、直前の有効なApproval Requestだけに適用される。

## Plain Japanese

GDSの目的は、AIに勝手に実行させることではありません。

AIがRepository状態、Evidence、Workflow、Review結果を読み、人間に分かる形で
推奨し、危険な実行前には必ず「何をしてよいか」を確認する共同作業を作ることです。

## Non-Negotiable Principles

- Review PASS is not Human Approval.
- Ready is not Execution.
- Commit OK is not Push OK.
- Human Approval applies only to the latest valid Approval Request.
- Repository state changes invalidate pending approval.
- BLOCK and SCW_REQUIRED must not produce an execution request.
- AI may propose and prepare; humans decide and approve.

## Vision Scenario

```text
AI:
Completion Review: PASS
Repository Quality: Green

コミットしても良いですか？

Human:
お願いします

AI:
Commit completed.

Pushしても良いですか？
```

This scenario is an Experience Contract test input, not just an example.

## Related Documents

- `docs/philosophy/human_ai_collaboration_model.md`
- `docs/architecture/experience_layer.md`
- `docs/architecture/design_intent_preservation.md`
- `templates/VISION_SCENARIO_TEMPLATE.md`
