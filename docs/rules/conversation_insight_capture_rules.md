# Conversation Insight Capture Rules

## Purpose

Conversation Insight Capture Rules は、会話の中で生まれた重要な設計思想、
運用方針、保守方針、Migration戦略、Command Center構想、長期ビジョンを、
GDS Knowledge Base の pre-promotion knowledge として安全に扱うための
正式ルールです。

このルールの目的は、会話全文を保存することではありません。通常の Q、
Research Mission、CASE、Completion Report になりにくいが、将来の Rule、
Architecture、Workflow、Roadmap、Concept、CASE へ昇格する可能性がある
知見を、人間の承認後に artifact 化することです。

## Core Rule

AI は、Repositoryへ残す価値が高い会話由来の知見を検出した場合、
Conversation Insight Candidate として提案できます。

AI は自動保存してはいけません。

AI はチャット全文を保存してはいけません。

Conversation Insight Draft は、人間が明示的に承認した場合のみ生成します。

## Candidate Criteria

Conversation Insight Candidate として提案できる条件:

- GDSの設計思想、Platform思想、開発理念に関わる。
- 運用方針、保守方針、Migration戦略、Command Center構想、長期運用方針、
  将来構想に関わる。
- 複数回の作業、複数Project、または将来のAI / human collaborationで
  再利用できる可能性がある。
- Q、Research Mission、CASE、Completion Reportだけでは拾いにくい。
- Rule、Architecture、Workflow、Roadmap、Concept、CASE、Template、Example
  へ昇格する可能性がある。
- 既存Knowledgeと完全重複していない。

Candidate として提案しない条件:

- 日常雑談。
- 一時的な感情や感想。
- 単なる会話ログ。
- 既存Rule、Workflow、Architecture、Template、Example、CASE、Conceptと
  実質的に重複する内容。
- private context、個人情報、非公開情報に依存する内容。
- 具体的な実装作業であり、通常の Q として扱うべき内容。

## Human Approval To Draft

AI は、次のような明示承認がある場合のみ Conversation Insight Draft を作成します。

- `書いといて`
- `保存して`
- `Repositoryへ追加`
- `Q化して`
- `Conversation Insightとして残して`

明示承認がない場合、AI は候補提案と理由説明に留めます。

## No Automatic Save

AI は Conversation Insight Candidate を自動保存してはいけません。

禁止:

- 会話中の判断で勝手に repository へ保存する。
- 人間の承認なしに draft artifact を作る。
- Future Candidate を approved knowledge として扱う。
- 自動検出を Human Approval の代替にする。

Command Center、Knowledge Mining Dashboard、その他の自動検出機能が将来追加されても、
Human Approval To Draft は維持します。

## No Full Chat Capture

Conversation Insight は、チャット全文保存の仕組みではありません。

禁止:

- 会話全文をそのまま保存する。
- 雑談や一時的な感情をKnowledgeとして保存する。
- 必要範囲を超えて個人情報、private context、未承認情報を保存する。

保存する場合は、insight summary、capture reason、applicable scope、
out of scope、duplicate check、promotion path を要約して記録します。

## Scope

対象:

- 設計思想。
- Platform思想。
- 開発理念。
- 保守方針。
- Migration戦略。
- Command Center構想。
- 長期運用方針。
- 将来構想。
- 既存RuleやWorkflowへ昇格する前の哲学的・運用的判断材料。

対象外:

- 日常雑談。
- 一時的な感想。
- 単なる雑談。
- 既存Knowledgeと重複する内容。
- 具体的な実装指示。
- Human ApprovalなしのRepository保存。

## Draft And Approved Knowledge Separation

Conversation Insight Draft は、承認済み Rule、Architecture、Workflow、
Template、CASE、Platform Standard ではありません。

Draft の扱い:

- 保存先は `docs/knowledge/conversation_insights/`。
- Human Approval To Draft を記録する。
- Duplicate Check を記録する。
- Promotion candidate type を記録する。
- Review result または next action を記録する。

Approved Knowledge になるには、対象の promotion workflow、review、必要な
Human Approval、completion report を経由します。

Approved Insight は、Human Approval済みの Conversation Insight artifact です。
Approved Insight は保存対象として承認されていますが、Rule、Architecture、
Workflow、Roadmap、Concept、CASEへの昇格を自動承認するものではありません。

## ID Standard

Conversation Insight ID は `CI-` と5桁ゼロパディングの連番を使います。

Examples:

```text
CI-00001
CI-00002
CI-00003
```

Recommended filename:

```text
CI-00000_<short_title>.md
```

Canonical save location:

```text
docs/knowledge/conversation_insights/
```

## Promotion Destinations

Conversation Insight の昇格先候補:

- `docs/rules/`
- `docs/workflow/`
- `docs/architecture/`
- `roadmap/`
- `pip/concepts/`
- `pip/cases/`
- `docs/knowledge/inventory/`
- `templates/`
- `examples/`

昇格には、該当する workflow を使います。

- Concept Promotion Workflow。
- Innovation Pipeline Workflow。
- Platform Promotion Decision Report。
- Knowledge Inventory。
- Standard Q and Completion Report。

## Duplicate Knowledge Control

AI は Conversation Insight Candidate を提案する前、または Draft を作る前に、
既存Knowledgeとの重複を確認します。

確認対象:

- `docs/rules/`
- `docs/workflow/`
- `docs/architecture/`
- `docs/README.md`
- `docs/knowledge/`
- `pip/concepts/`
- `pip/cases/`
- `templates/`
- `examples/`

重複している場合:

- 新規追加ではなく既存文書の更新候補として提案する。
- 重複理由を短く説明する。
- 同じ内容のConversation Insightを増やさない。

## Startup Detection

AI Startup Procedure と Startup Checklist では、Conversation Insight Detection を確認します。

確認すること:

- 重要な設計思想、運用方針、保守方針が含まれるか。
- Migration戦略、Command Center構想、長期ビジョンが含まれるか。
- Repositoryへ残す価値があるか。
- Candidateとして提案すべきか。
- 保存価値の理由を短く説明できるか。
- 自動保存していないか。
- 明示承認後のみ Draft 生成に進むか。

## Related Documents

- `docs/workflow/conversation_insight_capture_workflow.md`
- `docs/knowledge/conversation_insights/README.md`
- `templates/conversation_insight_template.md`
- `examples/conversation_insight_examples.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/startup_checklist_workflow.md`
- `templates/startup_checklist_template.md`
