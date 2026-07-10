# Collaborative Decision Workflow

## Purpose

Collaborative Decision Workflow は、AI とユーザーが互いの違和感、提案、分類案を持ち寄り、
議論、証拠確認、知識分類確認を通じて、保守性、再利用性、理解しやすさの高い決定へ到達するための標準フローです。

この workflow は AI Proactive Proposal Rule を補完します。

## Standard Flow

```text
Idea
  -> AI Proposal
  -> User Proposal
  -> Discussion
  -> Evidence Review
  -> Knowledge Classification Review
  -> Decision
  -> Documentation
```

## Discussion Principles

AI は次を積極的に提示してよいです。

- 分類への違和感。
- Rule との整合性。
- CASE 化の提案。
- Concept 化の提案。
- Workflow 化の提案。
- Methodology 化の提案。
- Template 化の提案。
- Human Approval Gate の必要性。
- Future Candidate として残す案。

ユーザーは AI 提案へ自由に改善案、異議、追加案、却下理由を提示してよいです。

## Decision Principles

目的は「AI が正しい」または「ユーザーが正しい」を決めることではありません。

目的は、共同で以下を満たす設計または知識分類を見つけることです。

- 保守性が高い。
- 再利用しやすい。
- 人間が理解しやすい。
- 既存 GDS rules / workflow / methodology と整合する。
- Future Candidate と approved scope が分離されている。
- 必要な Human Approval Gate が残っている。

## Knowledge Classification Review

議論の結果、知識をどこへ置くべきか確認します。

候補:

- Rule.
- Workflow.
- Methodology.
- CASE.
- Concept.
- Template.
- Example.
- Glossary.
- Architecture.
- PIP Decision History.
- Future Candidate.
- No documentation needed.

## Decision Output

推奨形式:

```text
Collaborative Decision:
- Topic:
- AI Proposal:
- User Proposal:
- Evidence Reviewed:
- Classification:
- Decision:
- Rationale:
- Documentation Target:
- Follow-up:
```

## Boundaries

Collaborative Decision Workflow は以下を意味しません。

- AI が最終承認者になる。
- 議論だけで Human Approval Gate を通過した扱いにする。
- Future Candidate を approved implementation として扱う。
- Evidence なしに rule / workflow / methodology へ昇格する。

## Related Documents

- `docs/rules/ai_proactive_proposal_rules.md`
- `docs/rules/ai_collaboration_rules.md`
- `docs/rules/pip_case_knowledge_base_rules.md`
- `docs/workflow/concept_promotion_workflow.md`
- `docs/workflow/pip_case_knowledge_base_workflow.md`
- `templates/collaborative_decision_template.md`
- `templates/decision_template.md`
- `examples/collaborative_decision_examples.md`
