# Startup Completion Evidence

## Purpose

Startup Completion Evidence は、AI が記憶や過去の会話だけに頼らず、
作業前に canonical repository source を確認したことを示す証跡です。

AI Startup Procedure と Startup Checklist は「何を確認するか」を定義します。
Startup Completion Evidence は「確認したことをどう示すか」を定義します。

## Core Rule

実装、レビュー、文書更新、Q 作成、Q 実行を始める前に、AI は Startup Completion
Gate を通過できるだけの証跡を残します。

証跡は長文ログではなく、確認対象、確認結果、使用した入口、未確認理由を短く
記録します。

## Required Evidence

- Memory Check completed.
- Memory Capability recorded:
  - Read: PASS / UNAVAILABLE / UNKNOWN.
  - Write: PASS / UNAVAILABLE / UNKNOWN.
- AI Startup Procedure reviewed.
- AI Repository Index reviewed.
- Current Mission or Current Q reviewed.
- Canonical `Q_TEMPLATE.md` reviewed, when Q creation or Q revision is involved.
- Related Rules reviewed.
- Related Workflows reviewed.
- Related ADRs or architecture docs reviewed, when relevant.
- Repository Root Validation completed.
- Scope / Out of Scope confirmed.
- Constraint Check completed.

## Repository Context Evidence

Startup Completion Evidence must distinguish between:

```text
AI knows that a repository exists
```

and:

```text
AI opened and resolved the current canonical assets required for this task
```

For repository-governed work, record the minimum repository context that
governs the response or artifact:

- repository name;
- working directory;
- git root or repository root evidence;
- branch or revision when available;
- AI Repository Index path and validation / freshness state;
- Current Q, Current Mission, or Information Package path;
- canonical template path and revision source when a template is used;
- related rules, workflows, ADRs, architecture, standards, or registries read;
- unavailable or unresolved assets;
- conflict status;
- Startup result timestamp or task identifier when useful.

AI memory, previous chat summaries, uploaded copies, and remembered template
shapes are not sufficient repository context evidence by themselves.

## Memory Capability Evidence

Startup evidence must avoid ambiguous wording such as `Memory Available` when
memory is relevant.

Use:

```text
Memory Capability:
- Read: PASS / UNAVAILABLE / UNKNOWN
- Write: PASS / UNAVAILABLE / UNKNOWN
- Limitation:
- Repository-backed alternative:
```

Memory Read means existing memory may be visible as non-authoritative context.
Memory Write means the current AI surface can create or update memory. These
are independent capabilities.

If Memory Write is unavailable, durable knowledge should be captured through
repository-backed artifacts such as Conversation Insight, Pending Insight, Q
artifact, ADR, Rule, Architecture, Workflow, or Roadmap update after the
required Human Approval.

## Evidence Format

Evidence は次の粒度で記録します。

```text
- Evidence item:
- Source checked:
- Result:
- Gap / limitation:
- Action:
```

短い作業ではチャット上の要約で十分です。再利用、レビュー、Git 管理、handoff を
前提とする場合は、`templates/startup_verification_checklist.md` を使って file
artifact として保存します。

## Freshness And Invalidation

Startup evidence becomes stale when the repository-governed context changes or
the task moves to a new governance state.

Refresh Startup evidence, run a task-specific context refresh, or explicitly
record a limitation when:

- a new chat or AI session begins;
- repository files changed after the last Startup evidence;
- Codex or another actor completed work that affects canonical rules,
  workflows, templates, ADRs, roadmap, registries, or indexes;
- the task type changes, such as Architecture Review -> Q Creation ->
  Completion Review -> Approval Request -> Execution;
- workflow state, approval state, or Pending Action state changes;
- the user reports that the AI response conflicts with repository policy;
- the AI identifies missing, stale, or conflicting canonical context;
- the human explicitly requests repository verification;
- a required canonical asset cannot be found or opened.

If a required refresh cannot be completed, do not claim Startup PASS. Record
`PASS_WITH_LIMITATION`, `BLOCKED`, or `SCW_REQUIRED` according to the risk.

## Gate Position

```text
AI Startup Procedure
  -> Startup Checklist
  -> Startup Completion Evidence
  -> Startup Completion Gate
  -> Q Creation / Implementation / Review
```

## Failure Conditions

次の場合、Gate は Pass にできません。

- Current Q を読んでいない。
- AI Repository Index を確認していない。
- 作業対象 repository root を確認していない。
- 関連 rules / workflows / ADRs の確認要否を判断していない。
- Scope / Out of Scope または commit policy が未確認。
- Q 作成なのに canonical `templates/Q_TEMPLATE.md` を確認していない。
- 未確認事項を「記憶しているはず」として扱っている。
- repository context evidence が古い、欠落している、または会話記憶だけに
  依存している。
- task type、approval state、repository state の変化後に必要な context refresh を
  行っていない。

## Not A Log Dump

Startup Completion Evidence は、チャット全文、巨大な command output、または
全ファイルの読み取りログではありません。

残すべきものは、未来の人間や新しい AI session が「どの公式入口を確認し、
どこに制約や未確認が残っていたか」を復元できる最小限の証跡です。

## Related Documents

- `docs/workflow/startup_completion_gate.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/startup_checklist_workflow.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `templates/startup_verification_checklist.md`
- `templates/startup_checklist_template.md`
- `templates/Q_TEMPLATE.md`
