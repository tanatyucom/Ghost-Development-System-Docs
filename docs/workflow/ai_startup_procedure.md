# AI Startup Procedure

## Purpose

AI Startup Procedure は、AI が GDS 作業を開始する前に読む順番と確認順を
定義する workflow です。

Startup Checklist が「開始直前のチェックリスト」なら、AI Startup Procedure は
「チェックリストへ進む前の読み込み手順」です。

## Standard Flow

```text
Start
  -> AI Repository Index Check
  -> Repository Root Validation
  -> GDS Core Rules / Workflow Check
  -> Target Project Profile Check
  -> Current Q File Check
  -> Startup Checklist
  -> Scope / Out of Scope Confirmation
  -> Implementation / Review Start
```

## Step Details

### 1. AI Repository Index Check

公開 GDS knowledge を参照する場合、`docs/ai_repository_index.md` から開始します。

確認すること:

- 必要な文書が Index に登録されている。
- Raw URL または local path が使える。
- 新規 Markdown を追加する作業では、最後に Index 再生成が必要か確認する。

### 2. Repository Root Validation

作業対象 repository を実測します。

```bash
pwd
git rev-parse --show-toplevel
git status
```

確認すること:

- Current Working Directory
- Actual Git root
- Expected Working Repository
- Production / backup / reference-only boundary
- Dirty workspace state

### 3. GDS Core Rules / Workflow Check

最低限、次の入口を確認します。

- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/workflow/README.md`

作業内容に応じて、次の文書を追加確認します。

- Artifact First / Q File Artifact Standard
- Audit Before Repair
- Debug Artifact Review
- Debug Escalation Ladder
- Migration First
- Completion Checklist
- Commit Safety

### 4. Target Project Profile Check

Target Project に profile がある場合、対象 profile を読みます。

例:

```text
project_profiles/gameghost/README.md
```

確認すること:

- repository location
- edit boundary
- project-specific rules
- project-specific workflow
- AI context
- completion policy

### 5. Current Q File Check

Q File から今回の作業範囲を確認します。

確認すること:

- Target Project
- Repository Information
- Scope Guard
- Do / Do Not
- Completion Criteria
- Commit policy
- Required artifacts

Q が Artifact First 対象の場合、保存済み Q artifact を authoritative source として
扱います。

### 6. Startup Checklist

読み込み結果を Startup Checklist に反映します。

最低限の確認:

```text
Startup Checklist:
- AI Repository Index read:
- Target Project identified:
- Project Profile read:
- Repository Root validated:
- Core Rules read:
- Current Q read:
- Scope / Out of Scope confirmed:
- Session Health checked:
- Ready:
```

### 7. Scope / Out of Scope Confirmation

実装・レビュー・文書更新を始める直前に、今回触ってよい対象と触ってはいけない対象を
確認します。

特に確認すること:

- related repository は reference only か editable か。
- runtime code は scope に入っているか。
- generated artifacts を Git 管理対象にするか。
- commit してよい Q か。

## Stop Conditions

次の状態では Implementation / Review Start に進みません。

- Git root が Working Repository と一致しない。
- Project Profile が必要なのに読めていない。
- Q と Project Profile が矛盾している。
- Scope Guard が曖昧。
- Commit policy が曖昧。
- authoritative Q artifact が必要なのに保存されていない。

## Relationship To Startup Checklist

AI Startup Procedure:

- 読む順番を決める。
- 参照漏れを防ぐ。
- Project Profile と Q File の前後関係を決める。

Startup Checklist:

- 読んだ結果をチェック項目として記録する。
- 実装開始前の gate として使う。
- 必要に応じて artifact として保存する。

## Related Documents

- `docs/rules/ai_startup_procedure_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/workflow/startup_checklist_workflow.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/workflow/repository_root_validation_workflow.md`
- `docs/rules/external_source_access_rules.md`
- `docs/ai_repository_index.md`
- `project_profiles/README.md`
- `templates/startup_checklist_template.md`
