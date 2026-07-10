# Q_GDS_Structured_Artifact_Metadata_Template_JP

Version: Draft 1.0  
Status: Draft  
Workflow: Platform Integration / Architecture Design  
Category: Architecture / Template  
Priority: High  
Commit:

```text
明示的な指示があるまで Commit しない。
Suggested Commit Message を提示する。
```

## Output Format

この Q 自体、およびこの Q から生成される再利用・レビュー・Git 管理対象の成果物は、
原則としてチャット本文ではなくファイル Artifact として生成する。

標準形式:

- Markdown `.md`

今回は Metadata 標準候補の設計が目的であり、
人間レビュー用 `.docx` は必須としない。

## Required Artifacts

```text
Markdown required: Yes
.docx required when human review is expected: No
PDF required: No
CSV / XLSX / PPTX required: No
Chat body should contain summary only: Yes
```

## Artifact Output

この Q は保存済み Markdown Artifact を authoritative source とする。

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

Q file artifacts are saved under:

```text
docs/requests/
```

## Artifact Workspace

Preferred full task workspace:

```text
docs/requests/draft/gds/2026-07-11_structured_artifact_metadata_template/
```

Artifact Workspace path:

```text
docs/requests/draft/gds/2026-07-11_structured_artifact_metadata_template/
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
docs/requests/draft/gds/2026-07-11_structured_artifact_metadata_template/request.md
```

## Status Folder

```text
draft
```

## File Naming

```text
2026-07-11_gds_structured_artifact_metadata_template.md
```

## Related Completion Report

Expected completion report artifact:

```text
docs/requests/draft/gds/2026-07-11_structured_artifact_metadata_template/completion_report.md
```

Status:

```text
Planned
```

## Output Artifacts

Expected output artifacts:

- Request artifact:
  - `docs/requests/draft/gds/2026-07-11_structured_artifact_metadata_template/request.md`
- Completion report artifact:
  - `docs/requests/draft/gds/2026-07-11_structured_artifact_metadata_template/completion_report.md`
- Structured Artifact Metadata Template:
  - recommended path under `templates/`
- Architecture update:
  - `docs/architecture/artifact_schema_standard.md`
- Notes artifact:
  - `docs/requests/draft/gds/2026-07-11_structured_artifact_metadata_template/notes.md`
- Attachments folder:
  - `docs/requests/draft/gds/2026-07-11_structured_artifact_metadata_template/attachments/`

## Expected Review Entry Point

1. Structured Artifact Metadata Template
2. Artifact Schema Standard integration
3. Compatibility / migration notes
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

## Movement Instructions

Expected movement:

```text
draft -> approved -> completed -> archived
```

Current movement instruction:

```text
Create in draft
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
GameGhost 参照のみ。
編集、同期、コピー、移行しない。
```

### Cross Project Impact

```text
Documentation Impact
```

将来の各Ghostが同じArtifact Metadataを利用できる可能性があるが、
本QではGDS Docs以外を変更しない。

### Scope Guard

- Edit only `Ghost-Development-System-Docs`.
- Treat GameGhost and other Ghost repositories as reference only.
- Do not modify runtime code.
- Do not implement Command Center.
- Do not implement Ghost SDK.
- Do not implement a parser, validator, database, API, CLI, or automation.
- Do not commit.
- Do not create a tag or release.

---

## Startup Checklist

- AI Daily Operation Cycle applies: Yes
- Current Q Review completed: Required
- Expected Knowledge Update: Structured Artifact Metadata knowledge
- Expected Repository Update: Architecture / Template / README / Index / History / Completion Report
- Expected Next Q Planning: Required
- AI Startup Procedure applies: Yes
- AI Repository Index read: Required
- Q File read with explicit UTF-8 when using Windows PowerShell 5.1: Required
- Q File mojibake check result: Required
- Repository Root Validation completed before implementation: Required
- GDS Core Rules / Workflow read: Required
- Target Project Profile read: Not required
- Current Q File confirmed as authoritative: Required
- Startup Checklist applies: Yes
- Working Repository confirmed: Required
- Repository Root Validation required: Yes
- Current Working Directory: `C:\GitHub\Ghost-Development-System-Docs`
- Git repository root: Must match Working Directory
- Root matches Working Repository: Required
- Production / Backup / Reference Only boundaries confirmed: Required
- Current Phase: Platform Integration Era
- Current Goal: Structured Artifact Metadata Template
- Applicable Rules:
  - Repository First
  - Platform First
  - Template First
  - Artifact First
  - Persistent Collaboration
  - Human Approval Required
- Applicable Methodologies:
  - Schema First
  - Migration First review
- Q Artifact / Download File status: Artifact required
- Scope / Out of Scope confirmed: Required
- Dirty Workspace checked: Required
- Commit policy confirmed: Required
- Proactive Proposal check required: Yes
- Better approach / time saving / concern to report: Required
- Collaborative Decision required when classification or design is uncertain: Yes
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

Artifact Schema Standardで定義した共通構造を、
人間とAIが読みやすく、将来Command Centerが機械処理しやすいMetadata Templateへ落とし込む。

本文とMetadataの責務を分離し、
Artifact識別、Lifecycle管理、関連Artifact参照、Human Approval、Verification、
Recommended Next Actionを一貫した形式で記録できる標準候補を作る。

## Background

Artifact Schema Standardでは、以下の共通構造が定義された。

- Metadata
- Lifecycle
- Status
- Repository Information
- Related Rules
- Related Templates
- Related Artifacts
- Inputs
- Outputs
- Human Approval
- Verification
- Recommended Next Action

また、Canonical Metadata Blockが定義されたが、
現時点ではMarkdown本文中のtext blockであり、
Command CenterやTemplate Engineが機械処理するための具体的な表現形式は未定義である。

Component Interfaceより前にMetadata表現を整理することで、
将来のTemplate Engine、Artifact Validator、Decision Engine、
Command Center、Ghost SDKが同じ前提を利用できるようにする。

## Approved Decisions

- Artifact Schema Standardを上位のauthoritative architecture standardとして扱う。
- MetadataはArtifact本文を置き換えない。
- Human ApprovalはSchema completenessから自動承認されない。
- Draft Artifactは実行命令ではない。
- RepositoryはSingle Source of Truthである。
- 本Qではruntime contractを実装しない。
- YAML / JSON / DB schemaの正式採用は、このQのレビュー結果なしに確定しない。
- 既存Artifactを一括変換しない。

## Collaborative Decision

```text
Collaborative Decision applies: Yes
AI Proposal: Markdown YAML front matterをStructured Metadataの第一候補として検討する。
User Proposal: Artifact Templateを育て、将来Command Centerから自動生成できる基盤にする。
Evidence Review: Artifact Schema Standard、Q File Template、Completion Report Template、Information Package Template、Multi-AI Handoff Template。
Knowledge Classification: Platform Architecture / Template Standard
Decision: 本Qでは表現形式を比較し、推奨形式と標準Templateを設計する。即時runtime implementationは行わない。
Documentation Target: docs/architecture / templates
Follow-up Q: Metadata validationまたはtemplate coverage reviewを別Qで判断する。
```

## Naming Policy

- Public名称は目的が3秒以内に分かる名前を優先する。
- `Structured Artifact Metadata Template` を標準候補名とする。
- Field nameは機械処理を想定し、lowercase ASCII snake_caseを第一候補とする。
- 人間向け表示名とmachine keyを混同しない。
- Lifecycle値、Status値、Approval値は既存標準と整合させる。
- 実装技術名をPlatform概念名に昇格させない。

## Migration First / Internal Architecture

Migration First applies:

```text
Yes
```

New Standard:

```text
Structured Artifact Metadata Template
```

Migration Plan:

```text
既存Artifactは即時一括変換しない。
新規Templateでoptional adoptionから開始し、
coverage reviewとvalidation設計後に段階的移行を検討する。
```

Reference Update:

```text
Artifact Schema Standard、Templates README、Architecture README、
README、docs/README、AI Repository Index、Historyを更新する。
```

Legacy Removal:

```text
なし
```

Public Compatibility Impact:

```text
exported artifact schema
```

Remaining Legacy:

```text
既存Artifact内の自由形式Metadata block
```

Restore / Rollback Guidance:

```text
Metadata Templateと関連document diffをrevertする。
既存Artifact本文は変更しないためruntime rollbackは不要。
```

## Debug Artifact Review

```text
Debug Artifact Review applies: No
```

## Scope

- Structured Artifact Metadataの表現方式を比較する。
- 推奨Metadata Templateを追加する。
- Artifact Schema Standardとのmappingを定義する。
- Field names、required / optional、allowed values、null / unknown表現を定義する。
- Lifecycle、Status、Human Approval、Verificationの値を既存標準と整合させる。
- Related Artifact参照方式を定義する。
- Schema versioning方針を定義する。
- 人間向け本文との責務境界を定義する。
- 新規Artifactでのoptional adoption方針を定義する。
- 既存Templateへの影響をreviewする。
- 将来のvalidation / parser / Command Center利用候補を整理する。

## Do

1. 以下の表現方式を比較する。
   - YAML front matter
   - JSON code block
   - Markdown key-value block
2. 比較観点を明記する。
   - Human readability
   - AI readability
   - Machine parseability
   - Git diff readability
   - Markdown compatibility
   - Schema evolution
   - Validation ease
   - Cross-platform tooling
3. 推奨方式を1つ選ぶか、採用保留理由を明記する。
4. Structured Artifact Metadata Templateを追加する。
5. 最低限、以下のfieldを定義する。
   - `artifact_type`
   - `artifact_id`
   - `title`
   - `schema_version`
   - `artifact_version`
   - `status`
   - `lifecycle_state`
   - `created_date`
   - `updated_date`
   - `owner`
   - `target_project`
   - `working_repository`
   - `source_of_truth`
   - `human_approval`
   - `related_q`
   - `related_completion_report`
   - `related_handoff`
   - `related_registry_update`
   - `related_rules`
   - `related_templates`
   - `related_artifacts`
   - `inputs`
   - `outputs`
   - `verification_status`
   - `recommended_next_action`
6. 各fieldについて以下を定義する。
   - Type
   - Required / Optional
   - Allowed values or format
   - Purpose
   - Example
7. Human Approval valuesをArtifact Schema Standardと整合させる。
8. Lifecycle valuesをArtifact Schema Standardと整合させる。
9. `unknown`、`not_applicable`、空配列、未設定の扱いを定義する。
10. Metadata本文とMarkdown本文の重複を最小化する。
11. Template Engineが使う際の基本mappingを文書化する。
12. Command CenterがMetadata completenessをautomatic approvalに使えないことを再確認する。
13. README、docs index、architecture index、templates index、history、AI Repository Indexへ導線を追加する。
14. Completion Reportを作成する。

## Do Not

- Parserを実装しない。
- Validatorを実装しない。
- JSON Schemaを正式実装しない。
- Pydantic modelを実装しない。
- Database schemaを作らない。
- API contractを作らない。
- Command Centerを実装しない。
- Ghost SDKを実装しない。
- 既存Artifactを一括変換しない。
- 全Templateへ強制適用しない。
- GameGhostを編集しない。
- Human Approvalを自動化しない。
- Commit、tag、releaseを行わない。

## Target Files

Expected candidates:

- `docs/architecture/artifact_schema_standard.md`
- new metadata architecture or standard document under `docs/architecture/`
- new metadata template under `templates/`
- `docs/architecture/README.md`
- `templates/README.md`
- `README.md`
- `docs/README.md`
- `docs/history/knowledge_base_history.md`
- `docs/ai_repository_index.md`
- `reports/repository_quality_report.md`
- task workspace files under `docs/requests/`

Exact filename should follow existing repository naming conventions.

## Completion Criteria

- Structured Artifact Metadataの推奨表現方式が明記されている。
- YAML / JSON / Markdown key-valueの比較が記録されている。
- Metadata Templateが追加されている。
- Artifact Schema Standardの各共通fieldとのmappingが説明されている。
- Required / Optionalが定義されている。
- Allowed valuesまたはformatが定義されている。
- Lifecycle、Status、Human Approvalが既存標準と整合している。
- Unknown / Not Applicable / Emptyの扱いが明確である。
- Schema versioning方針が明確である。
- MetadataとMarkdown本文の責務境界が明確である。
- 既存Artifactの一括移行を行っていない。
- Command CenterやGhost SDKを実装していない。
- GameGhostを変更していない。
- Commitを作成していない。
- README / Index / History導線が更新されている。
- Completion ReportにChanged Files、Summary、Verification、Improvement Review、
  Remaining Issues、Recommended Next Q、Suggested Commit Messageが含まれる。

### Artifact Completion Criteria

- Output Format is specified.
- Required Artifacts are specified.
- Artifact Output is specified.
- Artifact Workspace path is specified.
- Status Folder is specified.
- Save Location is under `docs/requests/`.
- File Naming follows the Q File Artifact Standard.
- Related Completion Report is specified.
- Output Artifacts are specified.
- Related Commit policy is specified.
- Movement Instructions are specified.
- Markdown `.md` is generated.
- Chat body contains summary only.

## Review Requests

- Artifact Schema Standardとの整合性
- Repository Firstとの整合性
- Platform Firstとの整合性
- Template First / Artifact Firstとの整合性
- YAML front matter採用の妥当性
- Human readabilityとmachine parseabilityのバランス
- Git diff readability
- Cross-platform互換性
- Schema versioningの妥当性
- Required fieldが過剰でないか
- Optional fieldが曖昧すぎないか
- Metadataと本文の重複
- Migration負担
- Command Center利用への拡張性
- Ghost SDK利用への拡張性
- Human Approval境界の維持
- Overengineeringになっていないか

## Future Candidates

- Artifact Metadata Validation Rules
- Artifact Metadata Validator
- JSON Schema export
- Pydantic artifact models
- Template-to-Schema Coverage Audit
- Artifact Schema Registry
- Metadata migration assistant
- Command Center artifact classifier
- Template Engine metadata injection
- Ghost SDK artifact contracts
- Repository-wide artifact search
- Artifact relationship graph

## Acceptance Criteria

- Target documents are updated.
- Scope and non-scope are respected.
- Repository Information is complete.
- Cross Project Impact is reviewed.
- Public names describe purpose before implementation technique.
- Future Candidates remain separate from approved work.
- Artifact Schema Standard remains authoritative.
- Metadata completeness is not treated as approval.
- Draft remains not command.
- Human Approval values remain explicit.
- ExistingArtifact mass migration is not performed.
- Runtime code is not changed.
- GameGhost is not changed.
- Commit is not created.
- Output Format、Artifact Workspace、Completion Report、Commit Policyが明確である。
- Migration Plan、Public Compatibility Impact、Remaining Legacy、Rollback Guidanceが記載されている。

## Deliverables

- Changed Files
- Structured Artifact Metadata comparison
- Structured Artifact Metadata Template
- Artifact Schema mapping
- Migration / compatibility notes
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

- Metadata Validation Qを次に進めるべきか
- Artifact Metadata Reference Examplesが先か
- Template-to-Schema Coverage Auditが先か
- Component Interface Specificationへ進める状態か
- Artifact Schema Registryが必要か
- YAML front matterをPlatform Standard RegistryへCandidate登録すべきか
- Q / Completion Report / Information Packageへのpilot adoptionを別Qで行うべきか

### Recommended Improvements

近いうちに採用すべき高価値なimprovementを記載する。

### Future Candidates

将来採用すべきideaを記載する。

## Suggested Commit Message

```text
docs: add structured artifact metadata template
```

## Writing Notes

- 日本語を基本とする。
- Commands、paths、filenames、identifiers、field keys、commit messagesはEnglishのまま残してよい。
- SchemaとTemplateとruntime implementationを分離する。
- Approved DecisionsとFuture Candidatesを混在させない。
- Metadata fieldを増やしすぎず、最小限の共通構造を優先する。
- 既存Artifactとの後方互換性と段階移行を優先する。
- Knowledge evolves through implementation.
- Reusable knowledge should be promoted to templates, rules, examples, or documentation whenever practical.
