# Beginner & Future Self Test Rules

## Purpose

Beginner & Future Self Test は、GDS の管理対象 artifact が、現在の熟練した
作成者だけでなく、初心者、新しく開始した AI session、未来の担当者、長期中断後に
戻ってきた project owner、そして未来の自分にも理解できるかを確認する品質基準です。

初出時は `Beginner & Future Self Test` と書き、以後は `BFS Test` と略してよいです。

## Core Rule

管理対象 artifact は、hidden chat context や author memory を前提にしないで
理解できる必要があります。

BFS Test は、次を短時間で判断できるかを確認します。

1. この artifact は何か。
2. なぜ存在するのか。
3. どの project / domain に属するのか。
4. 現在位置はどこか。
5. どの decision / evidence からここへ来たのか。
6. 次に期待される action は何か。
7. authoritative supporting source はどこか。

BFS Test は判断を支援するための基準です。不要な重複説明や長文化を推奨しません。

BFS Test is the practical quality check for the Context Recovery Principle.
Context Recovery Principle is the underlying design principle; BFS Test
verifies whether it works for a concrete artifact.

## Required Test Questions

- 初心者が artifact purpose を数秒で識別できるか。
- 新しい AI session が project、domain、artifact type、authority を識別できるか。
- project owner が数か月後に戻っても current position を回復できるか。
- reader が current decision / design の理由を trace できるか。
- reader が next expected action を識別できるか。
- reader が current work、completed work、future candidates を区別できるか。
- reader が chat history に頼らず authoritative related sources へ辿れるか。

## Review Outcomes

結果は次のいずれかで記録します。

- `PASS`
- `PASS WITH MINOR IMPROVEMENTS`
- `FAIL`
- `NOT APPLICABLE`

`PASS` 以外では、次を記録します。

- failed question。
- evidence。
- smallest recommended correction。
- affected artifact。
- correction が blocking か non-blocking か。

## Artifact-Specific Expectations

### Product Blueprint

初心者が次を理解できること。

- Vision。
- Mission。
- Product Identity。
- Principles。
- Scope In / Out。
- Success Definition。

Product Blueprint は安定した identity / scope を扱います。急速に変わる
Current Position を含めてはいけません。

### Master Roadmap

reader が数秒で次を理解できること。

- Current Mission。
- Current Phase。
- Overall Progress。
- Next Milestone。
- Known Blockers。
- Current Owner。
- Last Updated。

Current Position は Master Roadmap が所有します。

### Domain / Execution Roadmap

reader が次を理解できること。

- domain または workstream。
- dependencies。
- current status。
- exit criteria。
- next milestone。
- Master Roadmap との関係。

### Decision Record

reader が次を理解できること。

- Decision。
- Alternatives。
- Rationale。
- Evidence。
- Expected Impact。
- Related Q。
- Promotion Target。

### Q Document

reader が次を理解できること。

- repository と working directory。
- target / non-target project。
- purpose と background。
- allowed / forbidden scope。
- deliverables。
- verification。
- Commit / Push policy。
- safe commit set。

### Completion Report

reader が次を理解できること。

- what changed。
- what was verified。
- Q が成功したか。
- remaining issues。
- lessons learned。
- improvement / promotion candidates。
- recommended next work。
- Commit / Push status。

## Hidden Chat Context

次の場合は BFS Test の失敗候補です。

- 文書だけでは目的、対象、現在位置、次 action が分からない。
- 「前に話した通り」「さっきの件」など chat memory を前提にする。
- decision の理由が Q、Completion Report、Decision Record、Roadmap へ辿れない。
- Future Candidate と approved scope が混在している。

## Duplication Guard

BFS Test は、すべての背景を全文再掲する要求ではありません。

良い対応:

- authoritative source への link を置く。
- Current Position や Related Documents を短く示す。
- decision / evidence / next action を要約する。

悪い対応:

- Product Blueprint に日々変わる状態を貼り付ける。
- Q、Completion Report、Roadmap の全文を相互に複製する。
- 読みやすさのためではなく不安から説明を増やす。

## Integration Points

BFS Test は次の既存surfaceで使用します。

- documentation review checklist。
- completion checklist。
- Completion Report Improvement Review。
- Q template completion criteria。
- Product Documentation Hierarchy guidance。
- Startup / AI Response surfaces の軽量 reminder。

既存の Platform Discoverability、Q Naming、Completion Report、Current Position、
Decision Record standard を置き換えません。これらを読者視点で確認する横断的品質基準です。

## Commit OK Command Reference

review result が `Commit OK` で、commit が必要な場合、AI は既存の
AI Collaboration Rules に従い、reviewed safe commit set に対する copy-paste-ready
Git Bash commands を提示します。

BFS Test はこの commit command rule を複製しません。発見可能性を確認するだけです。

## Related Documents

- `docs/workflow/beginner_future_self_test_workflow.md`
- `templates/beginner_future_self_test_template.md`
- `examples/beginner_future_self_test_examples.md`
- `docs/rules/quality_rules.md`
- `templates/review_checklist.md`
- `templates/completion_checklist_template.md`
- `docs/architecture/product_document_hierarchy_v2.md`
- `docs/rules/ai_collaboration_rules.md`
