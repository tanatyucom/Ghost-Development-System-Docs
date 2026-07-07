# Knowledge Base History

## Purpose

この文書は、Ghost Development System Knowledge Base 自身の進化を記録します。

GameGhost の CHANGELOG、Development History、Decision Log ではありません。
Knowledge Base の構造、運用、review quality、project management、AI
collaboration がどのように改善されたかを簡潔に残します。

## Ver1.0

### Added

- Knowledge Base Index。
- 目的別 navigation。
- AI Entry Points。
- Authority Order。
- Knowledge Promotion guidance。
- Scaling Policy。

### Reason

Architecture、Workflow、Roadmap、Rules、Templates、Examples、Glossary が増え、
人間と AI がどこから読めばよいか分かりにくくなったため。

### Evolution

Knowledge Base が単なる folder collection から、目的別に読める公式入口を持つ
documentation system へ進化した。

## Ver1.1

### Added

- Project First Principle。
- Japanese First。
- Cross Project Impact。
- Project Rules。
- Language Rules。
- Ghost Development System Roadmap。
- Target Project を含む Q file template。

### Reason

Ghost Development System を GameGhost から独立した親の開発基盤として扱う必要が
明確になったため。

人間が理解できない依頼文は Human Approval を満たせず、Target Project が曖昧な
Q は誤編集や scope drift を起こす可能性があるため。

### Evolution

Knowledge Base が、GameGhost 補助文書ではなく、複数 project を支える開発基盤の
ルールセットへ進化した。

## Ver1.2

### Added

- Roadmap README の roadmap 一覧。
- Project Hierarchy。
- 強化された Review Checklist。
- Decision Background の軽量な記録方針。
- Knowledge Base History。

### Reason

Ver1.1 で追加した Project First、Japanese First、Cross Project Impact を、review
品質と navigation の中で安定して使えるようにする必要があったため。

Knowledge Base 自身の進化を振り返れる場所がないと、なぜ現在の構造になったのか
が将来分かりにくくなるため。

### Evolution

Knowledge Base が、入口とルールを持つ状態から、review quality と自己履歴を持つ
保守可能な documentation platform へ進化した。

## Ver1.3

### Added

- Artifact First / File Generation First rule.
- Output Policy for Chat versus Artifact decisions.
- Output Layer architecture boundary.
- Q template Output Format and Required Artifacts sections.
- Artifact First examples for long Q files, design documents, AI requests,
  review requests, and roadmap proposals.

### Reason

Long Q files, design documents, review requests, Codex requests, roadmap
proposals, and specifications can be truncated, copied incompletely, or lose
Markdown structure when they exist only in chat.

Reusable and Git-managed work needs durable file artifacts so humans and AI
review the same complete source.

### Evolution

Knowledge Base evolved from conversation-supported documentation into a
file-first artifact system for reusable requests, human approval, AI handoff,
and Knowledge Promotion.

## Ver1.4

### Added

- Q File Artifact Standard.
- Standard Q artifact save location: `docs/requests/`.
- Q artifact file naming pattern:
  `YYYY-MM-DD_<target_project>_<short_title>.md`.
- Completion report artifact naming pattern:
  `YYYY-MM-DD_<target_project>_<short_title>_completion_report.md`.
- Q template sections for Artifact Output, Save Location, File Naming,
  Related Completion Report, and Related Commit.
- Completion report template sections for Source Q File, Output Artifacts,
  Generated Files, Commit Hash, and Follow-up Q.
- Q File Artifact Workflow examples.

### Reason

Artifact First made file generation the general rule. Q files also need a
specific save location, naming standard, and completion report linkage so the
original request can be found after implementation.

### Evolution

Knowledge Base evolved from file-first output policy into a request artifact
workflow where Q, Codex execution, completion report, review, commit, and
Knowledge Promotion can be followed as one chain.

## Ver1.5

### Added

- Task Artifact Workspace standard.
- Project folders under `docs/requests/`.
- Status folders: `draft`, `approved`, `completed`, and `archived`.
- Full task workspace shape with `request.md`, `completion_report.md`,
  `notes.md`, and `attachments/`.
- Movement rules for `draft -> approved -> completed -> archived`.
- Review quality rule that missing Q artifact path is a review issue.
- Migration guidance for moving existing flat request artifacts safely.

### Reason

The flat `docs/requests/` model is useful at first, but it becomes hard to scan
as Q artifacts grow. Humans and AI need path-level signals for Target Project,
workflow status, task purpose, related completion report, notes, and
attachments.

### Evolution

Knowledge Base evolved from saved Q files into task workspaces that preserve
the whole request-to-review chain.

## Ver1.6

### Added

- Dirty Workspace Policy.
- File classification table for commit review.
- Commit Safety Checklist.
- Completion report fields for dirty workspace state, unrelated files,
  suggested restore commands, and safe commit set.
- Dirty workspace examples for restoring unrelated runtime files and keeping
  commits scoped.

### Reason

Local runtime files, generated reports, cache, and temporary outputs can remain
modified after successful work. Without a standard safety check, unrelated
files may be accidentally committed with documentation or implementation
changes.

### Evolution

Knowledge Base evolved from artifact traceability into commit safety practice:
every changed file should be classified before commit, and the safe commit set
should be explicit.

## Ver1.7

### Added

- Debug Artifact Review Rules.
- Debug Artifact Review Workflow.
- Q template fields for Debug Mode, intermediate artifacts, expected normal
  state, review viewpoints, AI review targets, and debug artifact Git policy.
- Completion report fields for debug artifact save location, verification
  target, expected normal state, review viewpoints, and follow-up Fix Q.
- Codex / AI implementation and review template guidance for Debug Mode.
- Debug Artifact Review examples.
- Glossary terms for Debug Artifact Review and Debug Artifact.

### Reason

AI, OCR, recommendation, auto-detection, candidate extraction, fuzzy matching,
and visual processing work can look successful in final output while
intermediate behavior is wrong.

Debug artifacts make the process inspectable, but they must not pollute normal
execution or enter Git accidentally.

### Evolution

Knowledge Base evolved from artifact traceability and commit safety into
development-time evidence review: intermediate artifacts can support human
approval, AI review, design review, and future Fix Q drafting without becoming
normal output.

## Ver1.8

### Added

- Audit Before Repair Rules.
- Audit Before Repair Workflow.
- Q template fields for source audit artifact, classification, repair scope,
  exclusions, evidence review, verification, safe commit set, and restore
  guidance.
- Completion report fields for Source Audit Artifact, Classification Summary,
  Repair Scope, Excluded Items, Fixed Files, Remaining Candidates, Safe Commit
  Set, and Suggested Restore Commands.
- AI collaboration guidance for audit-first repair handoff.
- Audit Before Repair examples.
- Glossary terms for Audit Before Repair and Repair Q.

### Reason

Repair work can damage source data, generated artifacts, DB files, OCR raw
evidence, or unrelated dirty workspace changes when the target is not audited
and classified first.

### Evolution

Knowledge Base evolved from development-time evidence review into
audit-first repair practice: repair work now starts from visible evidence and a
scoped Repair Q instead of broad one-shot modification.

## Ver1.9

### Added

- Review Entry Point Rule for Debug Artifact Review.
- Completion Report Template section for first artifact path, reason, and
  priority.
- Q File Template field for expected Review Entry Point.
- Codex Review Template checks for Review Entry Point.
- Steam OCR example showing contact sheet, overlay, crop, CSV, and Markdown
  report review order.
- PIP Rule Story candidate: Review Entry Point Rule / Too Many Artifacts.

### Reason

Debug Artifact Review can generate many artifacts: contact sheets, overlays,
crops, CSV files, and Markdown reports. Without a clear entry point, humans and
AI reviewers may not know where to start.

### Evolution

Knowledge Base evolved from "generate evidence" into "make evidence reviewable":
Completion Reports now identify the first artifact to inspect before listing
the full artifact set.

## Update Notes

この文書は詳細な Decision Log ではありません。

重要 decision の詳細な選択肢、却下理由、承認経緯が必要な場合は、別途 Decision
Log または ADR を作成します。
