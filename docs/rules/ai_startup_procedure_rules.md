# AI Startup Procedure Rules

## Purpose

AI Startup Procedure は、AI が GDS 作業を始める前に読む順番と確認順を
標準化するルールです。

目的は AI を縛ることではなく、人間と AI が毎回同じ前提で安全に作業を
始められるようにすることです。

## Core Rule

AI は実装、レビュー、文書更新、Q 実行を始める前に、次の順番で前提を確認します。

```text
AI Repository Index
  -> Repository Root Validation
  -> GDS Core Rules / Workflow
  -> Target Project Profile
  -> Current Q File
  -> Startup Checklist
  -> Scope / Out of Scope
  -> Implementation / Review Start
```

この順番は、Q の内容を読む前に必要なすべての文書を丸暗記するためのものでは
ありません。対象リポジトリ、対象プロジェクト、適用ルール、作業範囲を
取り違えないための開始手順です。

## Required Checks

### AI Repository Index

公開 GDS knowledge を読む場合、最初に `docs/ai_repository_index.md` を確認します。

確認すること:

- 必要な Markdown 文書が Index に存在する。
- Raw URL または local path から対象文書へ辿れる。
- 新しい公開入口を追加した場合、Index を再生成・検証する。

### Repository Root Validation

作業開始前に、宣言された Working Repository と実際の Git root が一致することを
確認します。

標準確認:

```bash
pwd
git rev-parse --show-toplevel
git status
```

Git root が Q の Working Repository と一致しない場合、編集、レビュー、commit を
開始してはいけません。

### GDS Core Rules / Workflow

AI は対象作業に応じて GDS 共通ルールと workflow を確認します。

最低限の入口:

- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/workflow/README.md`

作業内容に応じて Artifact First、Audit Before Repair、Debug Artifact Review、
Migration First、Completion Checklist などを追加で確認します。

### Target Project Profile

Target Project に Project Profile がある場合、Q 実行前に必ず読みます。

例:

```text
project_profiles/gameghost/README.md
```

Project Profile は Q File を置き換えません。Project Profile は安定した
プロジェクト前提を示し、Q File は今回の作業範囲を示します。

Project Profile と Q File が矛盾する場合は、作業を止めてユーザーに確認します。

### Current Q File

Current Q File で確認すること:

- Target Project
- Working Repository
- Single Source Of Truth
- Related Repository
- Scope Guard
- Do / Do Not
- Completion Criteria
- Commit policy

Windows PowerShell 5.1 で Q File を読む場合は、必ず UTF-8 を明示します。

```powershell
Get-Content -LiteralPath <Q file> -Encoding UTF8
```

Plain `Get-Content` で表示された mojibake を、UTF-8検証なしにファイル破損として
扱ってはいけません。

Q が Artifact First 対象の場合、`docs/requests/` 配下の authoritative artifact を
確認します。Chat 本文だけを正式な作業入力として扱ってはいけません。

### Startup Checklist

Startup Checklist は AI Startup Procedure の確認結果を、作業開始直前に
チェック可能な形へ落とし込む gate です。

確認すること:

- AI Repository Index read?
- Target Project identified?
- Project Profile read?
- Repository Root validated?
- Core Rules read?
- Current Q read?
- Scope / Out of Scope confirmed?
- Session Health checked?

## Stop Conditions

次の場合は実装や文書更新を始めず、確認を求めます。

- Working Repository と actual Git root が一致しない。
- Target Project が不明。
- Project Profile が必要だが未確認。
- Q File と Project Profile が矛盾している。
- Related Repository が editable か reference only か不明。
- Scope / Out of Scope が曖昧。
- Commit policy が不明。
- Chat-only Q で、Artifact First 対象なのに保存先がない。

## Decision Background

GDS は Startup Checklist、Repository Root Validation、AI Repository Index、
Project Profile、Q Artifact を持つようになりました。

しかし、これらを「どの順番で読むか」が曖昧だと、AI は正しい文書を持っていても
作業開始時に参照漏れを起こします。

AI Startup Procedure は、開始前の参照順を固定し、Repository 誤認、Scope drift、
Project Profile 読み漏れ、Q 欠落を防ぐための Knowledge Poka-Yoke です。

## Related Documents

- `docs/ai_repository_index.md`
- `docs/rules/utf8_read_rules.md`
- `docs/rules/external_source_access_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/rules/project_rules.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/startup_checklist_workflow.md`
- `templates/startup_checklist_template.md`
- `project_profiles/README.md`
