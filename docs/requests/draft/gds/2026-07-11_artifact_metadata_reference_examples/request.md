# Q_GDS_Artifact_Metadata_Reference_Examples_JP

Version: Draft 1.0  
Status: Draft  
Workflow: Platform Integration / Template Validation  
Category: Examples / Architecture  
Priority: High  
Commit:

```text
明示的な指示があるまで Commit しない。
Suggested Commit Message を提示する。
```

## Output Format

このQ自体、および本Qから生成される再利用・レビュー・Git管理対象の成果物は、
原則としてチャット本文ではなくMarkdown Artifactとして生成する。

- Markdown `.md`: Required
- Word `.docx`: Not required
- Chat body should contain summary only: Yes

## Required Artifacts

```text
Markdown required: Yes
.docx required when human review is expected: No
PDF required: No
CSV / XLSX / PPTX required: No
Chat body should contain summary only: Yes
```

## Artifact Output

このQは保存済みMarkdown Artifactをauthoritative sourceとする。

Required:

- Markdown `.md`

## Audit Before Repair

```text
Audit Before Repair applies: No
```

## Request ID / Task ID

```text
Not assigned
```

## Save Location

```text
docs/requests/
```

## Artifact Workspace

Preferred full task workspace:

```text
docs/requests/draft/gds/2026-07-11_artifact_metadata_reference_examples/
```

Artifact Workspace path:

```text
docs/requests/draft/gds/2026-07-11_artifact_metadata_reference_examples/
```

Workspace save required:

```text
Yes
```

Workspace save verification:

```text
request.md saved before implementation
```

Authoritative request file:

```text
docs/requests/draft/gds/2026-07-11_artifact_metadata_reference_examples/request.md
```

## Status Folder

```text
draft
```

Expected movement:

```text
draft -> approved -> completed -> archived
```

Current movement instruction:

```text
Create in draft
```

## File Naming

```text
2026-07-11_gds_artifact_metadata_reference_examples.md
```

## Related Completion Report

Expected completion report artifact:

```text
docs/requests/draft/gds/2026-07-11_artifact_metadata_reference_examples/completion_report.md
```

Status:

```text
Planned
```

## Output Artifacts

- Request artifact:
  - `docs/requests/draft/gds/2026-07-11_artifact_metadata_reference_examples/request.md`
- Completion report artifact:
  - `docs/requests/draft/gds/2026-07-11_artifact_metadata_reference_examples/completion_report.md`
- Reference examples:
  - recommended path under `examples/`
- Notes artifact:
  - `docs/requests/draft/gds/2026-07-11_artifact_metadata_reference_examples/notes.md`
- Attachments folder:
  - `docs/requests/draft/gds/2026-07-11_artifact_metadata_reference_examples/attachments/`

## Expected Review Entry Point

1. Good metadata examples
2. Bad / anti-pattern examples
3. Field pressure review
4. Completion Report

## Related Commit

Commit policy:

```text
Do not commit
```

Commit hash:

```text
Not created
```

---

## Repository Information

### Target Project

```text
Ghost Development System
```

### Project Profile

```text
Project Profile applies: No
Project Profile path: Not required
Project Profile reviewed before implementation: Not required
Project Profile conflicts with Q: None
Conflict resolution: Not required
```

### Repository

```text
Ghost-Development-System-Docs
```

### Working Directory

```text
C:\GitHub\Ghost-Development-System-Docs
```

Git Bash entry command:

```bash
cd /c/GitHub/Ghost-Development-System-Docs
```

### Documentation Root

```text
C:\GitHub\Ghost-Development-System-Docs\docs
```

### Runtime Root

```text
対象外
```

### Single Source Of Truth

```text
Ghost Development System Docs
```

AI entry point:

```text
https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/ai_repository_index.md
```

### Related Repository

```text
GameGhost is reference only.
Do not edit, sync, copy, or migrate GameGhost.
```

### Cross Project Impact

```text
Documentation Impact
```

将来のGhost群が同一Metadataを採用する可能性はあるが、
本QではGDS Docs以外を変更しない。

### Scope Guard

- Edit only `Ghost-Development-System-Docs`.
- Treat GameGhost and other Ghost repositories as reference only.
- Do not modify runtime code.
- Do not implement parser, validator, API, DB, CLI, or automation.
- Do not mass-migrate existing artifacts.
- Do not commit.
- Do not create a tag or release.

---

## Startup Checklist

- AI Daily Operation Cycle applies: Yes
- Current Q Review completed: Required
- Expected Knowledge Update: Artifact Metadata example knowledge
- Expected Repository Update: Examples / Template links / README / Index / History / Completion Report
- Expected Next Q Planning: Required
- AI Startup Procedure applies: Yes
- AI Repository Index read: Required
- Q File read with explicit UTF-8 when using Windows PowerShell 5.1: Required
- Q File mojibake check result: Required
- Repository Root Validation completed before implementation: Required
- GDS Core Rules / Workflow read: Required
- Structured Artifact Metadata Template read: Required
- Artifact Schema Standard read: Required
- Current Q File confirmed as authoritative: Required
- Startup Checklist applies: Yes
- Working Repository confirmed: Required
- Repository Root Validation required: Yes
- Current Working Directory: `C:\GitHub\Ghost-Development-System-Docs`
- Git repository root: Must match Working Directory
- Production / Backup / Reference Only boundaries confirmed: Required
- Current Phase: Platform Integration Era
- Current Goal: Artifact Metadata Reference Examples
- Applicable Rules:
  - Repository First
  - Platform First
  - Template First
  - Artifact First
  - Persistent Collaboration
  - Human Approval Required
- Q Artifact / Download File status: Artifact required
- Scope / Out of Scope confirmed: Required
- Dirty Workspace checked: Required
- Commit policy confirmed: Required
- Proactive Proposal check required: Yes
- Better approach / time saving / concern to report: Required
- Collaborative Decision required when field design is uncertain: Yes
- Ready to start: Only after `request.md` is saved

## Completion Checklist

- Completion Checklist applies: Yes
- Verification required: Yes
- Review required: Yes
- Completion Report required: Yes
- Improvement Review required: Yes
- Commit decision required: Yes
- Tag decision required: Yes
- Release decision required: Yes
- Recommended Next Q required: Yes
- Workspace Clean Confirmation required: Yes

---

## Purpose

Structured Artifact Metadata Templateの実運用例を追加し、
異なるArtifact種別へ同じYAML front matterを適用した際の可読性、
field過不足、Lifecycle整合性、Human Approval境界を確認できるようにする。

Validatorやparserを実装する前に、
Exampleを通じてSchemaとTemplateの違和感を検出する。

## Background

Structured Artifact Metadata Templateでは、
YAML front matterを推奨形式として採用し、以下を定義した。

- Required / Optional fields
- Allowed values
- `unknown`
- `not_applicable`
- `null`
- `[]`
- Human Approval
- Verification Status
- Lifecycle State
- Related Artifact references

ただし、Template単体では以下を十分に確認できない。

- Required fieldが多すぎないか
- Artifact種別ごとに不要fieldが多くならないか
- `unknown`や`null`が乱用されないか
- Metadataと本文が重複しないか
- Human ApprovalとLifecycleが矛盾しないか
- Related Artifact参照が実用的か
- Git diffが読みやすいか

そのため、実例と失敗例を追加し、
Validation RuleやComponent Interfaceへ進む前にfield設計をreviewする。

## Approved Decisions

- YAML front matterを推奨形式として使用する。
- YAML front matterは現時点でruntime APIではない。
- Metadata completenessはapprovalを意味しない。
- Draft Artifactは実行命令ではない。
- Human Approvalを維持する。
- 既存Artifactの一括移行は行わない。
- Reference Examplesは新規Artifact向けの利用指針とする。
- Structured Artifact Metadata Templateをauthoritative templateとして扱う。

## Collaborative Decision

```text
Collaborative Decision applies: Yes
AI Proposal: Good / Bad examplesでfield pressureを確認してからValidatorへ進む。
User Proposal: Templateを育て、Command Center自動Artifact生成へ接続する。
Evidence Review: Artifact Schema Standard、Structured Artifact Metadata Template、既存Q / Completion Report / Information Package / Handoff templates。
Knowledge Classification: Platform Example / Schema Validation
Decision: Reference Examplesを追加し、field設計の改善候補を記録する。
Documentation Target: examples
Follow-up Q: Example review結果に基づきValidation RulesまたはTemplate revisionを判断する。
```

## Naming Policy

- Example名はArtifact種別と状態が3秒以内に分かる名称を使う。
- Metadata field keyは既存Templateどおりlowercase ASCII snake_caseを維持する。
- `Good Example`、`Bad Example`、`Anti-pattern`を明確に区別する。
- 実在のsecret、token、個人情報、private repository pathをExampleへ入れない。
- Pathは公開Repository内の相対pathを優先する。

## Migration First / Internal Architecture

Migration First applies:

```text
Yes
```

New Standard:

```text
Artifact Metadata Reference Examples
```

Migration Plan:

```text
既存Artifactは変更しない。
新規Artifact作成時の参照例としてoptional adoptionする。
Example review後に必要ならMetadata Templateを別Qで改訂する。
```

Reference Update:

```text
Structured Artifact Metadata Template、Examples README、
README、docs/README、AI Repository Index、Historyを更新する。
```

Legacy Removal:

```text
なし
```

Public Compatibility Impact:

```text
exported artifact example standard
```

Remaining Legacy:

```text
既存Artifactのfree-form metadata
```

Restore / Rollback Guidance:

```text
Reference Examplesと関連リンクのdiffをrevertする。
既存Artifact本文は変更しない。
```

## Debug Artifact Review

```text
Debug Artifact Review applies: No
```

## Scope

- Structured Artifact MetadataのGood Examplesを追加する。
- Bad Examples / Anti-patternsを追加する。
- Artifact種別ごとのfield適合性を確認する。
- `unknown` / `not_applicable` / `null` / `[]` の正しい使い分けを例示する。
- Human ApprovalとLifecycleの整合例を示す。
- Related Artifact参照例を示す。
- Metadataと本文の責務分離を例示する。
- Exampleから見つかったfield改善候補を記録する。
- Template / Schema改訂が必要かをImprovement Reviewで判断する。
- README / Index導線を追加する。

## Do

1. 少なくとも以下のGood Examplesを追加する。
   - Q Artifact
   - Completion Report
   - Information Package
   - Multi-AI Handoff
   - Registry Update
   - Health Report
2. 各Good Exampleに以下を含める。
   - YAML front matter
   - 最小限のMarkdown本文
   - Why this metadata is valid
   - Required / Optional field explanation
   - Approval / Lifecycle explanation
3. 少なくとも以下の状態差を含める。
   - Draft / pending approval
   - Approved
   - Completed / verification passed
   - Archived
4. 以下の値の正しい利用例を含める。
   - `unknown`
   - `not_applicable`
   - `null`
   - `[]`
5. 少なくとも以下のBad Examples / Anti-patternsを追加する。
   - Required field missing
   - Invalid lifecycle / status combination
   - `human_approval: approved`なのにDraft
   - Metadata completenessをapproval扱い
   - `unknown`の乱用
   - Optional single referenceに空文字を使用
   - Optional listに`null`を使用
   - Metadataへ長文本文を複製
   - Absolute local pathへの過度な依存
   - Draft Artifactをexecution commandとして扱う
6. 各Bad Exampleに以下を含める。
   - Problem
   - Risk
   - Corrected Example
7. Field Pressure Reviewを追加する。
   - Artifact種別ごとに不要なRequired fieldはないか
   - `owner`の意味は明確か
   - `status`と`lifecycle_state`が重複しすぎていないか
   - `source_of_truth`のallowed valuesは十分か
   - Related fieldsが多すぎないか
   - Date fieldの扱いは実用的か
8. Example結果を基に、Template変更が必要ならRecommendationだけを記録する。
9. 本Q内でTemplateを大幅改訂しない。
10. Structured Artifact Metadata TemplateからExampleへの導線を追加する。
11. README、docs index、templates index、examples index、history、AI Repository Indexへ必要な導線を追加する。
12. Completion Reportを作成する。

## Do Not

- Parserを実装しない。
- Validatorを実装しない。
- JSON Schemaを実装しない。
- Pydantic modelを実装しない。
- Command Centerを実装しない。
- Ghost SDKを実装しない。
- Existing Artifactを一括変換しない。
- 既存ArtifactへMetadataを強制追加しない。
- Metadata Templateを無断で破壊的変更しない。
- GameGhostを編集しない。
- Human Approvalを自動化しない。
- Commit、tag、releaseを行わない。

## Target Files

Expected candidates:

- `examples/artifact_metadata_reference_examples.md`
- `examples/README.md`
- `templates/structured_artifact_metadata_template.md`
- `templates/README.md`
- `docs/architecture/artifact_schema_standard.md`
- `README.md`
- `docs/README.md`
- `docs/history/knowledge_base_history.md`
- `docs/ai_repository_index.md`
- `reports/repository_quality_report.md`
- task workspace files under `docs/requests/`

Exact filenames should follow existing repository naming conventions.

## Completion Criteria

- 6種以上のGood Examplesが追加されている。
- 4段階以上のLifecycle / approval状態が例示されている。
- `unknown` / `not_applicable` / `null` / `[]` が正しく例示されている。
- 8種以上のBad Examples / Anti-patternsが追加されている。
- 各Bad ExampleにProblem / Risk / Corrected Exampleがある。
- Metadataと本文の責務分離が理解できる。
- Field Pressure Reviewが記録されている。
- Template改訂候補とValidator候補が区別されている。
- 既存Artifactの一括移行を行っていない。
- Parser / Validator / Command Center / Ghost SDKを実装していない。
- GameGhostを変更していない。
- Commitを作成していない。
- README / Index / History導線が更新されている。
- Completion ReportにChanged Files、Summary、Verification、Improvement Review、
  Remaining Issues、Recommended Next Q、Suggested Commit Messageが含まれる。

### Artifact Completion Criteria

- Output Format is specified.
- Required Artifacts are specified.
- Artifact Workspace path is specified.
- Status Folder is specified.
- Save Location is under `docs/requests/`.
- File Naming follows the Q File Artifact Standard.
- Related Completion Report is specified.
- Related Commit policy is specified.
- Movement Instructions are specified.
- Markdown `.md` is generated.
- Chat body contains summary only.

## Review Requests

- Artifact Schema Standardとの整合性
- Structured Artifact Metadata Templateとの整合性
- Repository First / Platform Firstとの整合性
- Template First / Artifact Firstとの整合性
- Good Exampleの現実性
- Anti-patternの十分性
- Required field数が過剰でないか
- `status`と`lifecycle_state`の役割分離
- `owner`の実用性
- `source_of_truth` allowed valuesの妥当性
- `unknown` / `not_applicable`の乱用防止
- Metadataと本文の重複
- Git diff readability
- Human Approval境界の維持
- Validator実装前にSchema変更が必要か
- Overengineeringになっていないか

## Future Candidates

- Artifact Metadata Validation Rules
- Artifact Metadata Validator
- Artifact Metadata Reference Example Generator
- Template-to-Schema Coverage Audit
- Artifact Schema Registry
- JSON Schema export
- Pydantic artifact models
- Metadata migration assistant
- Command Center metadata classifier
- Artifact relationship graph
- Cross-Ghost metadata profile

## Acceptance Criteria

- Target documents are updated.
- Scope and non-scope are respected.
- Repository Information is complete.
- Cross Project Impact is reviewed.
- Public names describe purpose before implementation technique.
- Future Candidates remain separate from approved work.
- Metadata completeness is not treated as approval.
- Draft remains not command.
- Human Approval remains explicit.
- Existing Artifact mass migration is not performed.
- Runtime code is not changed.
- GameGhost is not changed.
- Commit is not created.
- Good / Bad examples are both present.
- Field Pressure Review is present.
- Migration Plan、Public Compatibility Impact、Remaining Legacy、Rollback Guidanceが記載されている。

## Deliverables

- Changed Files
- Artifact Metadata Good Examples
- Artifact Metadata Bad Examples / Anti-patterns
- Corrected Examples
- Field Pressure Review
- Template improvement recommendations
- Summary
- Verification
- Metrics / Evidence
- Improvement Review
- Recommended Improvements
- Future Candidates
- Remaining Issues
- Recommended Next Q
- Suggested Commit Message

## Improvement Review

完了後に以下をreviewする。

- Metadata Template改訂が必要か
- Validation Rulesへ進める状態か
- Component Interface Specificationへ進める状態か
- `status`と`lifecycle_state`の両方が必要か
- `owner`をRequiredのまま維持すべきか
- Related fieldsをまとめるべきか
- Artifact種別別Profileが必要か
- Reference ExamplesをPlatform Standard RegistryへCandidate登録すべきか

### Suggested Commit Message

```text
docs: add artifact metadata reference examples
```

## Writing Notes

- 日本語を基本とする。
- Commands、paths、filenames、identifiers、field keys、commit messagesはEnglishのまま残してよい。
- Good ExampleとBad Exampleを明確に分離する。
- Metadataと本文を重複させない。
- 実装ではなくExampleとreviewに限定する。
- Schema / Template変更候補はRecommendationとして記録し、本Q内で破壊的変更しない。
