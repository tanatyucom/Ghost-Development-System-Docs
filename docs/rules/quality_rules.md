# Quality Rules

**Version:** 2.4

**Last Updated:** 2026-07-13

## Purpose

This document defines quality standards for Ghost Development System Docs.

## Quality Philosophy

### Quality Is Built During Work

Quality is not a final cleanup step. It is built through clear scope, readable
documents, review, verification, and continuous improvement.

### Maintainability Over Speed

Prefer documents that remain understandable months later over documents that are
quick but ambiguous.

### Human And AI Readability

Documents should be explicit enough that AI does not need to guess and humans do
not need private context.

### Beginner And Future Self Readability

Managed artifacts should pass the Beginner & Future Self Test, abbreviated as
BFS Test after first use, when they are important for review, handoff,
resumption, roadmap tracking, or knowledge promotion.

BFS Test asks whether a beginner, a new AI session, a future contributor, a
returning project owner, or the future self of the author can understand the
artifact purpose, project / domain, current position, evidence, next action,
and authority without hidden chat context.

## Review Standards

Review documentation for:

- purpose;
- scope;
- ownership;
- BFS Test result, when applicable;
- terminology;
- consistency with roadmap and rules;
- missing related updates;
- future candidate handling;
- acceptance criteria.
- artifact location;
- source Q path;
- completion report pairing;
- correct project/status workspace.
- debug artifact location, when Debug Mode applies;
- expected normal state for intermediate artifacts;
- whether normal execution avoids debug artifact generation.

When evidence allows, reviews should end with:

- `Commit OK`; or
- `Revision Recommended`.

If neither is possible, state the blocker and the minimum next evidence needed.
Platform Era reviews should include a Recommended Next Q when a useful next
step is visible.

## Error Prevention

Prevent common errors by:

- writing explicit out-of-scope sections;
- separating Future Candidates from approved work;
- requiring Human Approval Gate for high-impact changes;
- keeping templates current;
- checking related documents when rules or workflow change.
- treating missing Q artifact paths as review issues;
- storing completion reports beside the source Q artifact;
- keeping notes and attachments in the task workspace.
- requiring intermediate artifact review for AI, OCR, recommendation,
  auto-detection, candidate extraction, fuzzy matching, or visual processing
  work when Debug Mode applies;
- reviewing process unit, data flow, and responsibility boundary before code
  edits when debug artifacts feel wrong or ambiguous.
- avoiding optimization from a single sample when the behavior is expected to
  generalize across multiple records, screens, documents, users, projects, or
  runtime states;
- using representative samples, golden samples, or known-good examples before
  accepting tuning, scoring, extraction, or recognition changes;
- preserving useful negative results when they explain why an attractive fix,
  metric, or candidate was not accepted.

## Beginner & Future Self Test

Use `docs/rules/beginner_future_self_test_rules.md` when a document must remain
understandable across time, AI sessions, or project handoff.

Accepted outcomes:

- `PASS`
- `PASS WITH MINOR IMPROVEMENTS`
- `FAIL`
- `NOT APPLICABLE`

For non-PASS results, record the failed question, evidence, smallest recommended
correction, affected artifact, and whether the correction is blocking.

## Evidence First

Do not rely on memory when reviewing. Check the actual document, folder, or
request whenever possible.

## Representative Sample Rule

単一サンプルだけで最適化してはいけません。

例外は、Qが単一対象修正であり、横展開しないこと、検証対象、回帰リスク、
適用範囲を明記している場合に限ります。

共通ルール、workflow、template、OCR、import、DB repair、recommendation、
classification、UI review、AI output tuning など、複数対象へ影響する作業では、
代表サンプル、golden sample、既知の正常例、失敗例、境界例を確認します。

Completion Report には、代表サンプルの範囲、除外したサンプル、単一サンプルで
止めた場合の理由を記録します。

## Goal

Quality means the knowledge base can be trusted, resumed, reviewed, and evolved
without losing architectural intent.
