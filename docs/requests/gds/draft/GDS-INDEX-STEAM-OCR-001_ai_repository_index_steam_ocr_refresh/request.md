# Q: AI Repository Index Steam OCR Knowledge Promotion Refresh

Version: 1.0

Status: Draft

Workflow: Documentation Maintenance / Knowledge Access

Category: Repository Index / Knowledge Promotion

Priority: High

Commit:

```text
明示的な指示があるまで Commit しない。
Suggested Commit Message を提示する。
```

## Output Format

この Q 自体、およびこの Q から生成される再利用・レビュー・Git 管理対象の成果物は、
原則としてチャット本文ではなくファイル Artifact として生成します。

標準形式:

- Markdown `.md`

チャット本文には、目的の要約、Artifact のパス、検証結果、残課題のみを記載します。

## Required Artifacts

```text
Markdown required: Yes
.docx required when human review is expected: No
PDF required: No
CSV / XLSX / PPTX required: No
Chat body should contain summary only: Yes
```

## Artifact Output

この Q は保存済み Artifact を authoritative source とします。

Required:

- Markdown `.md`

## Audit Before Repair

- Audit Before Repair applies: Yes
- Source audit artifact:
  - Current `docs/ai_repository_index.md`
  - `scripts/generate_ai_repository_index.py`
  - newly added Steam OCR knowledge files
- Audit command or method:
  - inspect repository status
  - inspect generator behavior
  - run index validation before modification
  - compare Markdown inventory against generated index coverage
- Classification used:
  - `fix_candidate`: public Markdown knowledge files missing from the generated index
  - `needs_human_review`: files whose category, priority, title, or purpose cannot be determined safely
  - `generated_artifact`: `docs/ai_repository_index.md`
  - `raw_data`: source Markdown knowledge files scanned by the generator
  - `false_positive`: non-public, temporary, attachment, generated report, or excluded Markdown files not intended for the AI index
- Repair target scope:
  - generator configuration or metadata needed to include approved Steam OCR knowledge assets
  - regenerated `docs/ai_repository_index.md`
- Explicit exclusions:
  - do not manually patch only the generated table if the generator would remove the change
  - do not edit Steam OCR research contents unless an indexability defect requires a minimal metadata correction
- Evidence to review:
  - before/after validation output
  - before/after index entries
  - list of newly indexed files
- Human Review required before repair: No
- Verification method:
  - generator `--validate`
  - regenerate with `--write`
  - rerun `--validate`
  - inspect Raw URLs and representative fetchability
- Safe commit set:
  - index generator/configuration changes, if required
  - regenerated `docs/ai_repository_index.md`
  - task completion report
- Restore / rollback guidance:
  - restore changed files from Git if validation fails or generated coverage regresses

## Request ID / Task ID

```text
GDS-INDEX-STEAM-OCR-001
```

## Save Location

```text
docs/requests/
```

## Artifact Workspace

Preferred full task workspace:

```text
docs/requests/gds/draft/GDS-INDEX-STEAM-OCR-001_ai_repository_index_steam_ocr_refresh/
  request.md
  completion_report.md
  notes.md
  attachments/
```

Artifact Workspace path:

```text
docs/requests/gds/draft/GDS-INDEX-STEAM-OCR-001_ai_repository_index_steam_ocr_refresh/
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
docs/requests/gds/draft/GDS-INDEX-STEAM-OCR-001_ai_repository_index_steam_ocr_refresh/request.md
```

Rule:

```text
Do not start Codex / AI implementation until request.md is saved in this workspace.
```

## Status Folder

```text
draft
```

Status meaning:

- `draft`: Q is being prepared and is not approved for execution.

## File Naming

```text
2026-07-12_gds_ai_repository_index_steam_ocr_refresh.md
```

## Related Completion Report

Expected completion report artifact:

```text
docs/requests/gds/draft/GDS-INDEX-STEAM-OCR-001_ai_repository_index_steam_ocr_refresh/completion_report.md
```

Status:

```text
Planned
```

Completion report workspace rule:

```text
Save completion_report.md in the same Task Artifact Workspace as request.md.
```

## Output Artifacts

Expected output artifacts:

- Request artifact:
  - `docs/requests/gds/draft/GDS-INDEX-STEAM-OCR-001_ai_repository_index_steam_ocr_refresh/request.md`
- Completion report artifact:
  - `docs/requests/gds/draft/GDS-INDEX-STEAM-OCR-001_ai_repository_index_steam_ocr_refresh/completion_report.md`
- Human review artifact:
  - Not required
- Notes artifact:
  - `docs/requests/gds/draft/GDS-INDEX-STEAM-OCR-001_ai_repository_index_steam_ocr_refresh/notes.md`
- Attachments folder:
  - `docs/requests/gds/draft/GDS-INDEX-STEAM-OCR-001_ai_repository_index_steam_ocr_refresh/attachments/`

## Expected Review Entry Point

1. Completion report summary
2. Newly generated Steam OCR entries in `docs/ai_repository_index.md`
3. Final `--validate` output
4. Representative Raw URL fetch verification

## Related Commit

Commit policy:

```text
Do not commit.
Commit only when explicitly requested after human review.
```

Commit hash:

```text
Not created.
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

Move the whole task workspace folder when status changes.

## Repository Information

### Target Project

```text
Ghost Development System
```

### Project Profile

- Project Profile applies: No
- Project Profile path: Not applicable
- Project Profile reviewed before implementation: Not applicable
- Project Profile conflicts with Q: None
- Conflict resolution: Not applicable

### Repository

```text
Ghost-Development-System-Docs
```

### Working Directory

```text
C:\GitHub\Ghost-Development-System-Docs
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
Ghost Development System Docs repository on the current checked-out branch.
```

### Related Repository

```text
GameGhost

参照のみ。
編集、同期、コピー、移行しない。
```

### Cross Project Impact

```text
Reference Only
```

GameGhost / Steam OCR knowledge is indexed as public GDS knowledge, but GameGhost runtime
and repository contents are outside this Q.

### Scope Guard

- Edit only `Ghost-Development-System-Docs`.
- Treat GameGhost as reference only.
- Do not update, sync, copy, or migrate GameGhost files.
- Do not modify runtime code.
- Do not edit unrelated knowledge content.
- Do not manually maintain generated output in a way that conflicts with the generator.
- Do not commit.

## Startup Checklist

- AI Daily Operation Cycle applies: Yes
- Current Q Review completed: Required
- Expected Knowledge Update:
  - Steam OCR milestone, final archive package, CASE-0008, Knowledge Inventory,
    Promotion Decision, Next Q Plan, and updated Rule entry points become discoverable
    through the canonical AI Repository Index.
- Expected Repository Update:
  - generator/configuration only if required
  - regenerated `docs/ai_repository_index.md`
  - completion report
- Expected Next Q Planning:
  - review whether automatic index freshness should be checked by Completion Checklist or CI
- AI Startup Procedure applies: Yes
- AI Repository Index read: Required
- Q File read with explicit UTF-8 when using Windows PowerShell 5.1: Required
- Q File mojibake check result: Record in completion report
- Repository Root Validation completed before implementation: Required
- GDS Core Rules / Workflow read: Required
- Target Project Profile read: Not applicable
- Current Q File confirmed as authoritative: Required
- Startup Checklist applies: Yes
- Working Repository confirmed: Required
- Repository Root Validation required: Yes
- Current Working Directory: Record before work
- Git repository root: Record before work
- Root matches Working Repository: Must be Yes
- Production / Backup / Reference Only boundaries confirmed: Required
- Current Phase: Knowledge Promotion / Repository Access Maintenance
- Current Goal: Refresh the canonical generated index so current Steam OCR knowledge is reachable
- Applicable Rules:
  - `docs/rules/core_principles.md`
  - `docs/rules/external_source_access_rules.md`
  - `docs/rules/repository_root_validation_rules.md`
  - `docs/rules/git_rules.md`
  - `docs/rules/completion_checklist_rules.md`
- Applicable Methodologies:
  - Audit Before Repair
  - Knowledge Promotion Pipeline
  - Repository Root Validation
- Q Artifact / Download File status: Must be saved before execution
- Scope / Out of Scope confirmed: Required
- Dirty Workspace checked: Required
- Commit policy confirmed: Required
- Proactive Proposal check required: Yes
- Better approach / time saving / concern to report:
  - prefer generator-based correction over manual generated-file editing
- Collaborative Decision required when classification or design is uncertain: Yes
- Ready to start: Only after all required checks pass

## Completion Checklist

- Completion Checklist applies: Yes
- Verification required: Yes
- Review required: Yes
- Completion Report required: Yes
- Improvement Review required: Yes
- Commit decision required: Yes
- Tag decision required: No
- Release decision required: No
- Recommended Next Q required: Yes
- Workspace Clean Confirmation required: Yes

## Purpose

Steam OCR Root Cause Investigation により正式昇格したGDS知識を、
Canonical Knowledge Access入口である `docs/ai_repository_index.md` から
ChatGPT、Codex、Claude、Geminiその他のAIが確実に発見できる状態に更新します。

単にリンクを手作業で追記するのではなく、既存の生成・検証機構を使い、
今後の再生成でも欠落しない形で修正します。

## Background

Steam OCR Root Cause Investigation は、OCR固有の改善だけでなく、次のGDS共通知識を
確立した研究です。

- Problem Solving Framework
- Knowledge Promotion Pipeline
- Repository operation
- Research Mission
- Candidate Generation Before Scoring
- Metrics are evidence, not truth
- Human Observation as re-investigation trigger
- Negative Result as Knowledge Asset

成果は、Milestone、Final Archive Package、CASE-0008、Knowledge Inventory、
Promotion Decision、Next Q Plan、Rule更新として
`Ghost-Development-System-Docs` に正式保存されました。

しかし、現在の `docs/ai_repository_index.md` は生成時刻が古く、
これらの新規・更新知識がCanonical入口から発見できない可能性があります。

AI Repository Index自身のUpdate Ruleでは、Markdown knowledge fileの追加、
重要ファイルの移動・改名、Rules、History、CASE等のentry point変更時に
再生成することが定義されています。

このQは、そのKnowledge Accessの欠落を監査し、生成機構を通じて復旧します。

## Approved Decisions

- `docs/ai_repository_index.md` をAIのCanonical Knowledge Access入口として扱う。
- Steam OCR成果物はGDSの正式Knowledge Promotion成果として扱う。
- 生成物への一時的な手編集ではなく、generator-based updateを優先する。
- Commitは人間の明示承認まで行わない。
- GameGhostは参照のみであり、このQでは編集しない。

## Collaborative Decision

- Collaborative Decision applies: No
- AI Proposal: Not required
- User Proposal: Refresh the Raw index so the newly promoted Steam OCR knowledge is discoverable
- Evidence Review: Already approved by user
- Knowledge Classification: Repository Index / Knowledge Promotion
- Decision: Approved scope for Q creation
- Documentation Target:
  - `docs/ai_repository_index.md`
  - generator/configuration only if necessary
- Follow-up Q:
  - determine from completion report whether automatic freshness enforcement is needed

## Naming Policy

- Q title and public knowledge topics use purpose-oriented naming.
- `Steam OCR` remains as the source research identifier.
- `AI Repository Index Refresh` describes the repository maintenance purpose.
- Use lowercase ASCII and snake_case for files and workspace paths.

## Migration First / Internal Architecture

Migration First applies:

```text
No
```

New Standard:

```text
Not required
```

Migration Plan:

```text
なし
```

Reference Update:

```text
Regenerate and validate AI Repository Index.
```

Legacy Removal:

```text
なし
```

Public Compatibility Impact:

```text
documented external workflow
```

Remaining Legacy:

```text
None expected
```

Restore / Rollback Guidance:

```text
Revert changed generator/configuration and regenerated index files if validation regresses.
```

## Debug Artifact Review

Debug Artifact Review applies:

```text
No
```

Debug Mode required during development:

```text
No
```

Normal execution debug artifact policy:

```text
Do not generate debug artifacts during normal execution unless Debug Mode is explicitly requested.
```

Expected debug artifact save location:

```text
Not required
```

Expected Review Entry Point:

```text
Completion Report -> regenerated index entries -> validation output
```

Intermediate artifacts to review:

```text
Generator and validator command output only
```

Verification target:

```text
All intended public Steam OCR knowledge assets are indexed with valid Raw URLs.
```

Expected normal state:

```text
Generator write produces no unexpected omissions, validation passes, and a second generation is idempotent.
```

Review viewpoints:

```text
coverage, category, priority, purpose text, Raw URL validity, duplicate prevention, generated-file idempotency
```

AI review target artifacts:

```text
docs/ai_repository_index.md
completion_report.md
```

Debug artifact Git policy:

```text
Runtime-only, do not commit
```

## Scope

- Documentation and repository-index maintenance only.
- Audit current generated index coverage.
- Confirm how `scripts/generate_ai_repository_index.py` discovers and classifies files.
- Regenerate the canonical index.
- Correct generator metadata/configuration only when necessary.
- Validate coverage, duplication, path existence, Raw URL formatting, and idempotency.
- Produce a completion report.

## Do

1. Start in the repository root.

2. Confirm repository identity and working tree state.

3. Read:
   - `docs/ai_repository_index.md`
   - `scripts/generate_ai_repository_index.py`
   - `templates/q_file_template.md`
   - applicable Rules and Workflows listed in Startup Checklist.

4. Save this Q as the authoritative `request.md` before implementation.

5. Run the existing validation before modification:

   ```powershell
   cd C:\GitHub\Ghost-Development-System-Docs
   python scripts\generate_ai_repository_index.py --validate
   ```

6. Audit whether the following required Steam OCR knowledge entry points exist in the index:

   ### Milestone / Historical Archive

   - `docs/history/milestones/steam_ocr_knowledge_promotion_project.md`

   ### Final Archive Package

   - `docs/history/milestones/steam_ocr_final_archive_package/README.md`
   - all Markdown files inside the package that are intended as public knowledge entry points

   ### CASE

   - `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md`

   ### Knowledge Inventory

   - `docs/knowledge/inventory/README.md`
   - Steam OCR Knowledge Inventory
   - Steam OCR Promotion Decision / Decision Matrix
   - Steam OCR Next Q Plan
   - related inventory artifacts intended as public entry points

   ### Updated Rules

   - `docs/rules/debug_artifact_review_rules.md`
   - `docs/rules/audit_before_repair_rules.md`
   - `docs/rules/debug_escalation_ladder_rules.md`
   - `docs/rules/core_principles.md`
   - `docs/rules/repository_root_validation_rules.md`
   - `docs/rules/git_rules.md`

7. Discover exact filenames from the repository. Do not invent missing paths.

8. Determine why any intended Markdown file is missing:
   - index simply not regenerated
   - generator exclusion
   - missing metadata
   - unsupported directory/category
   - malformed Markdown title/purpose extraction
   - duplicate/conflict
   - file intentionally excluded

9. Prefer the smallest durable correction:
   - first try normal regeneration
   - modify generator/configuration only if normal regeneration cannot include approved assets correctly
   - do not manually patch generated rows as the primary solution

10. Generate or refresh the index:

   ```powershell
   cd C:\GitHub\Ghost-Development-System-Docs
   python scripts\generate_ai_repository_index.py --write
   ```

11. Validate:

   ```powershell
   cd C:\GitHub\Ghost-Development-System-Docs
   python scripts\generate_ai_repository_index.py --validate
   ```

12. Run `--write` a second time or otherwise verify idempotency.
    The second run must not create unexpected changes.

13. Inspect the generated entries for:
    - correct title
    - useful purpose
    - correct local path
    - correct GitHub URL
    - correct Raw URL
    - correct category
    - suitable priority
    - no duplicate entries

14. Perform representative Raw URL access checks for at least:
    - Steam OCR Knowledge Promotion Project
    - Final Archive Package README
    - CASE-0008
    - one Steam OCR Knowledge Inventory/Decision file
    - one updated Rule

15. Review `git diff` and ensure no unrelated changes are included.

16. Produce `completion_report.md`.

17. Do not commit.

## Do Not

- Do not change GameGhost runtime or repository files.
- Do not modify OCR implementation.
- Do not rewrite the Steam OCR research conclusions.
- Do not create new Rules merely to make indexing easier.
- Do not add duplicate manual index sections outside the generator.
- Do not hide validation failures.
- Do not mark a Raw URL as verified unless it was actually checked.
- Do not update unrelated documentation.
- Do not create a tag or release.
- Do not commit.
- Do not implement Future Candidates.

## Target Files

Primary:

- `docs/ai_repository_index.md`
- `scripts/generate_ai_repository_index.py` only if required
- generator metadata/configuration files discovered during audit, only if required

Required source review:

- `docs/history/milestones/steam_ocr_knowledge_promotion_project.md`
- `docs/history/milestones/steam_ocr_final_archive_package/`
- `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md`
- `docs/knowledge/inventory/`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/audit_before_repair_rules.md`
- `docs/rules/debug_escalation_ladder_rules.md`
- `docs/rules/core_principles.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/rules/git_rules.md`

Task artifacts:

- `docs/requests/gds/draft/GDS-INDEX-STEAM-OCR-001_ai_repository_index_steam_ocr_refresh/request.md`
- `docs/requests/gds/draft/GDS-INDEX-STEAM-OCR-001_ai_repository_index_steam_ocr_refresh/completion_report.md`
- `docs/requests/gds/draft/GDS-INDEX-STEAM-OCR-001_ai_repository_index_steam_ocr_refresh/notes.md`

## Completion Criteria

- Repository root validation passes.
- Current working tree state is reported.
- Existing index validation is run before changes.
- Exact Steam OCR target files are discovered from the repository.
- All approved public entry points are included in the generated index or an explicit,
  evidence-based exclusion is documented.
- Required Milestone, Final Archive README, CASE-0008, Inventory/Decision/Next Q,
  and updated Rule entries are discoverable.
- Generator-based update is used.
- Generator/configuration changes are minimal and justified.
- `python scripts/generate_ai_repository_index.py --validate` passes after update.
- Generated output is idempotent.
- Raw URL formatting is valid.
- Representative Raw URLs are actually fetched successfully.
- No duplicate entries are introduced.
- No unrelated files are changed.
- GameGhost is not edited.
- Runtime code is not changed.
- Commit is not created.
- Completion report includes:
  - Changed Files
  - Summary
  - Before/after evidence
  - Validation output
  - Newly indexed files
  - Explicit exclusions
  - Representative Raw access results
  - Improvement Review
  - Remaining Issues
  - Recommended Next Q
  - Suggested Commit Message

### Artifact Completion Criteria

- Q is saved under `docs/requests/`.
- Full Task Artifact Workspace is used.
- `request.md` is saved before implementation.
- `completion_report.md` is saved in the same workspace.
- Status folder is explicit.
- Movement instruction is explicit.
- Markdown artifact is authoritative.
- Chat output contains summary only.

## Review Requests

Review the result from these viewpoints:

- Canonical AI knowledge access completeness
- Knowledge Promotion Pipeline continuity
- public knowledge base clarity
- generated index durability
- category and priority correctness
- Raw URL reliability
- duplicate prevention
- generator idempotency
- long-term maintainability
- whether important entry points are distinguishable from supporting evidence
- whether the Final Archive Package README is the correct first entry point
- whether updated Rules remain easy for future AI sessions to discover
- whether Completion Checklist should prevent stale index generation in future

## Future Candidates

Do not implement in this Q:

- CI check that fails when `docs/ai_repository_index.md` is stale
- pre-commit validation for AI Repository Index
- automatic Completion Checklist integration
- automatic important-entry-point priority assignment
- repository knowledge dependency graph
- Command Center repository scan
- Information Package generation from indexed knowledge
- automatic Raw URL fetch health check
- incremental index generation

## Acceptance Criteria

- Steam OCR Knowledge Promotion成果がCanonical Indexから辿れる。
- Indexはgeneratorから再生成されている。
- Validationが成功している。
- 代表Raw URLの取得が確認されている。
- 手作業だけの一時修正になっていない。
- scopeとnon-scopeが守られている。
- GameGhostは参照のみである。
- Commitされていない。
- Completion Reportが生成されている。
- Future Candidatesは実装されていない。

### UTF-8 Read Criteria

Windows PowerShell 5.1を使用する場合:

```powershell
cd C:\GitHub\Ghost-Development-System-Docs
Get-Content -LiteralPath `
  "docs\requests\gds\draft\GDS-INDEX-STEAM-OCR-001_ai_repository_index_steam_ocr_refresh\request.md" `
  -Encoding UTF8
```

- plain `Get-Content` の文字化けをファイル破損と断定しない。
- 文字化け報告には、file name、line number、mojibake string、expected string、
  command used、inferred causeを含める。

## Deliverables

最終報告には以下を含めてください。

- Changed Files
- Summary
- Initial Audit Result
- Missing / Existing Index Entries
- Generator Behavior
- Validation
- Idempotency Result
- Representative Raw URL Access Results
- Metrics / Evidence
- Explicit Exclusions
- Improvement Review
- Recommended Improvements
- Future Candidates
- Remaining Issues
- Recommended Next Q
- Suggested Commit Message
- Commit Status

## Improvement Review

完了したworkから、次を改善すべきかreviewしてください。

- Documentation
- Templates
- Workflow
- Roadmap
- Rules
- Architecture
- Knowledge Base
- Metrics / Evidence
- AI Repository Index generation
- Completion Checklist integration

### Recommended Improvements

近いうちに採用すべき高価値な改善だけを記載してください。

### Future Candidates

将来候補は承認済みworkと分離してください。

## Suggested Commit Message

```text
docs: refresh AI repository index for Steam OCR knowledge promotion
```

## Writing Notes

- Ghost Development System DocsのQ fileは日本語を基本とする。
- Proper nouns、commands、paths、filenames、identifiers、commit messagesはEnglishのまま残してよい。
- Target Projectを実装前に宣言する。
- Cross Project Impactを明示する。
- Future Candidatesをapproved workから分離する。
- out-of-scope itemsを明示してscope driftを防ぐ。
- Knowledge evolves through implementation.
- Reusable knowledge should be promoted to templates, rules, examples, or documentation whenever practical.
