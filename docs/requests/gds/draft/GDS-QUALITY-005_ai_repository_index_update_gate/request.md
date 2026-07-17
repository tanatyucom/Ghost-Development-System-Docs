# Q-GDS-QUALITY-005 AI Repository Index Update Gate

Status: Draft

Workflow: Q Creation / Q Completion / Repository Synchronization

Category: Quality / AI Collaboration / Repository Governance

Priority: High

Commit:

```text
Commit は行わないでください。レビュー待ちにしてください。
```

---

# 目的

Qファイルの実行によってGDS Repository内のKnowledge Assetが追加・変更・削除された場合、
Completion前にCanonical AI Repository Indexを必ず再生成・検証する
`AI Repository Index Update Gate` を正式な運用候補として追加する。

ローカルRepositoryと公開Raw Indexの不整合を防ぎ、
次回Startup時にAIが最新のCanonical Template、Rule、Workflow、Roadmap、
Requestその他のKnowledge Assetへ到達できる状態を維持する。

---

# 背景

GDS-QUALITY-003およびGDS-QUALITY-004の検証中、
StartupはCanonical AI Repository Indexを参照できたものの、
Indexから辿るCanonical Q Templateの個別Raw URL取得に失敗し、
Q Creation GateがSTOPした事例が発生した。

この事例では、AIが記憶からQを作成せず、
「Templateの場所を知っていること」と
「Template本文を実際に開いたこと」を区別したため、
Q Creation Gate自体は正常に機能した。

一方で、Q完了時にRepository Indexの再生成・検証・Commit対象化が
必須手順として十分固定されていない場合、以下が発生し得る。

- 新規Knowledge AssetがIndexへ登録されない
- 変更後のパスやRevisionがIndexへ反映されない
- ローカルIndexと公開Raw Indexが一致しない
- 次回StartupでCanonical Artifactを取得できない
- AI側の同期失敗とRepository側の公開不整合を切り分けにくい

このため、Q成果物のCompletion条件として
AI Repository Index更新を明示的な品質ゲートにする必要がある。

---

# 決定事項

以下を採用する。

1. QによってIndex対象Knowledge Assetを変更した場合、
   Completion前にCanonical AI Repository Indexを再生成する。
2. 再生成後にIndex Validationを実行する。
3. `git diff --check`および`git status --short --untracked-files=all`を確認する。
4. `docs/ai_repository_index.md`の変更が必要な場合、
   同一QのSafe Commit Setへ含める。
5. Index生成またはValidationに失敗した場合はSCWを適用し、
   Completion扱いにしない。
6. Commit / Pushは従来どおりHuman Approval Requiredとする。
7. 公開Raw Indexへの反映完了はCommit / Push後であることを明記する。
8. 自動Commit・自動Pushは行わない。

---

# 作業範囲

今回扱う範囲:

- Canonical Q Templateの改訂
- Q Completion Workflowまたは関連Workflowの改訂
- Workflow / Template READMEへの参照追加
- RoadmapへのFuture Candidate登録または進捗反映
- Canonical AI Repository Indexの再生成・検証
- Q Request / Completion Reportの作成

Documentation update only.

Runtime code、SDK、Ghost Repository固有機能は変更しない。

---

# やること

## 1. Canonical Q TemplateへGateを追加する

Canonical `templates/Q_TEMPLATE.md` のVerification、
Completion Requirements、Acceptance Criteria、または適切な節へ、
以下の内容を追加する。

### AI Repository Index Update Gate

Repository内のIndex対象Knowledge Assetを追加・変更・削除した場合、
Completion前にCanonical AI Repository Indexを再生成・検証する。

対象例:

- `docs/`
- `templates/`
- `rules/`
- `schemas/`
- `workflow/` または `workflows/`
- `roadmap/`
- `registries/`
- `requests/`
- ADR
- Standards
- Current Mission
- Startup
- AIがStartupまたは実行時に参照するその他のKnowledge Asset

Repositoryの実際の構造とIndex生成スクリプトの対象範囲を確認し、
存在しないパスを固定的に追加しないこと。

---

## 2. Required Commandsを定義する

GDS Repositoryで以下をCompletion前の標準確認として実行する。

```bash
cd /c/GitHub/Ghost-Development-System-Docs

python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
git diff --check
git status --short --untracked-files=all
```

Windows側の実Repositoryパス表記が必要な文書では、
既存GDS運用のCanonical表記に合わせること。

---

## 3. Required Evidenceを定義する

Completion Reportに最低限、以下を記録する。

- Index generation result
- Generated entry count
- Index validation result
- `git diff --check` result
- `docs/ai_repository_index.md`の変更有無
- Index変更がSafe Commit Setへ含まれているか
- Commit未承認状態
- Push未承認状態
- 公開Raw IndexはPush後に更新されること

単なる「Index確認済み」ではなく、
実行結果をEvidenceとして残すこと。

---

## 4. Failure Actionを定義する

以下の場合はSCWを適用する。

- Index生成失敗
- Index Validation失敗
- Index対象Knowledge Assetが登録されない
- Indexに重複・欠落・不正なRaw URLが疑われる
- Canonical pathを解決できない
- Repository境界が不明
- Safe Commit Setへ既存dirtyが混入する可能性がある

SCW時は推測で修正・Commit・Pushを続行しない。

---

## 5. Completion Workflowへ反映する

既存のQ Completion Workflow、
Completion Report Template、
Startup Completion Evidence、
Repository synchronization関連Workflowを確認する。

重複した新規Workflowを作成する前に、
既存ArtifactへのRevisionで対応可能かを優先する。

役割分担は以下を維持する。

- Startup / Q Creation Gate:
  作業開始前にCanonical Knowledgeを実読できたか確認する
- AI Repository Index Update Gate:
  作業完了前にRepository変更をIndexへ反映したか確認する
- GDS-QUALITY-003:
  Context Synchronizationの運用対策
- GDS-QUALITY-004:
  Execution Contextの継続維持

---

## 6. Raw公開条件を明記する

以下を明確に区別する。

```text
Index生成
  -> ローカルIndex更新

Commit
  -> Git履歴へ登録

Push
  -> GitHub mainへ反映

Raw取得
  -> 公開Canonical Index / Artifactとして参照可能
```

Index生成成功だけを、
公開Raw Index更新完了として報告しないこと。

---

# やらないこと

- Commitは行わない。
- Pushは行わない。
- 自動Commitを実装しない。
- 自動Pushを実装しない。
- Human Approval Boundaryを緩和しない。
- Q実行時に無条件で全Repositoryを変更しない。
- GameGhost、AnimeGhost、ComicGhost固有Repositoryを変更しない。
- Index生成スクリプトの大規模改修は行わない。
- 新しい一括Validationスクリプトを今回実装しない。
- ChatGPT、Codex、GitHub Rawの外部仕様変更を前提にしない。
- Index生成失敗時に記憶や推測でCompletion扱いにしない。

---

# 対象ファイル

実Repositoryを確認したうえで、Revision Firstで対象を確定する。

変更候補:

- `templates/Q_TEMPLATE.md`
- Q Completion Workflow
- Completion Report Template
- Workflow README
- Template README
- `roadmap/ghost_development_system_roadmap.md`
- `docs/ai_repository_index.md`
- `docs/requests/gds/draft/GDS-QUALITY-005_ai_repository_index_update_gate/request.md`
- `docs/requests/gds/draft/GDS-QUALITY-005_ai_repository_index_update_gate/completion_report.md`

対象外:

- Ghost Repository側の採用版Template
- Runtime code
- SDK
- Adapter
- Database
- CI/CD設定

Ghost Repositoryへの採用は、
GDS側Canonical Revision完了後の別Qまたは正式なAdoption Workflowで扱う。

---

# 納品物

Codexは以下を報告する。

- Changed Files
- Summary
- Q Templateへの追加内容
- Completion Workflowへの追加内容
- Existing ArtifactをRevisionしたか、新規Artifactを作成したか
- AI Repository Index generation result
- Generated entry count
- AI Repository Index validation result
- `git diff --check` result
- `git status --short --untracked-files=all`確認結果
- Safe Commit Set
- Remaining Issues
- Future Candidates
- Suggested Commit Message

---

# 受け入れ条件

- Canonical Q TemplateにAI Repository Index Update Gateが追加されている。
- Index対象Knowledge Asset変更時の再生成条件が明記されている。
- Required Commandsが明記されている。
- Required Evidenceが明記されている。
- Failure ActionとしてSCWが定義されている。
- Commit / PushがHuman Approval Requiredのまま維持されている。
- ローカルIndex更新と公開Raw反映が区別されている。
- Index変更が必要な場合、Safe Commit Setへ含めることが明記されている。
- Completion ReportまたはCompletion WorkflowからGateを確認できる。
- Existing ArtifactへのRevision Firstが守られている。
- 新規一括Validationスクリプトは実装されていない。
- Runtime code、SDK、Ghost Repositoryは変更されていない。
- Canonical AI Repository Indexが再生成・検証されている。
- Commit / Push / Stageは行われていない。

---

# 推奨・任意事項

- Index更新不要だった場合も、
  「生成・検証を実行したが差分なし」とEvidenceへ記録してよい。
- Index対象パスの説明は、現在の生成スクリプトと実Repository構造に合わせて調整してよい。
- 既存Completion Report Templateへ自然に統合できる場合は、
  重複する専用Artifactを増やさない。
- Raw URLの到達確認を追加する場合は、
 ネットワーク制約やGitHub反映遅延を考慮し、
 必須Gateへ即時昇格させずEvidence収集から始める。
- GDS-QUALITY-003およびGDS-QUALITY-004との参照関係を明記してよい。

---

# Future送り候補

## 1. Complete Q Validation Script

以下を一括実行する共通スクリプトを将来検討する。

- AI Repository Index生成
- AI Repository Index検証
- `git diff --check`
- 文字化けマーカー検索
- Runtime temp / pycache確認
- Git status確認
- Safe Commit Set候補出力

候補名:

```text
scripts/complete_q_validation.py
```

または既存Validation Commandへの統合。

---

## 2. Repository Raw Availability Check

Commit / Push後に以下を検証する仕組み。

- Raw Index取得
- Critical Template Raw URL取得
- HTTP status
- Expected Revision
- Expected path
- Index entryと実Artifactの整合性

外部公開遅延を考慮し、
即時失敗をRepository corruptionと断定しない。

---

## 3. Completion Gate Automation

Command CenterまたはArtifact Pipelineから、
Q Completion前にIndex Update Gateを自動実行する機能。

---

## 4. Repository Synchronization Monitor

Local Repository、GitHub main、Raw content間の
同期状態を可視化するFuture Candidate。

---

# レビュー依頼

以下をレビューする。

- Q Completion責務として妥当か
- Q TemplateとCompletion Workflowの役割分担
- Startup / Q Creation Gateとの重複有無
- GDS-QUALITY-003 / 004との責務境界
- Repository Index対象範囲の表現
- Human Approval Boundaryの維持
- Safe Commit Setとの整合性
- SCW発動条件
- Raw公開条件の正確性
- 将来のAutomationへ過剰に踏み込んでいないか
- documentation quality
- long-term maintainability
- workflow fit

---

# Commit方針

基本方針:

```text
Commit は行わないでください。レビュー待ちにしてください。
```

Suggested Commit Message:

```text
docs: add ai repository index update gate
```

---

# 記述ルール

- 本文は日本語を基本にする。
- コマンド、パス、ファイル名、識別子は英語のままでよい。
- Canonical Repositoryの実構造を確認してからパスを確定する。
- 存在しないArtifactやRevisionを推測で記述しない。
- 「確認した」と「実行結果をEvidenceとして取得した」を区別する。
- Index生成成功と公開Raw反映完了を区別する。
- Q Completionを宣言する前にGate結果を確認する。
- 既存dirtyをSafe Commit Setへ混ぜない。
- Repository境界を越えない。
- Human ApprovalなしでCommit / Pushを行わない。

---

# Migration First

今回の変更はDocumentation Workflow Revisionであり、
Runtime migrationは行わない。

Canonical Template改訂後にGhost Repository側へ採用する場合は、
別途以下を扱う。

- Adoption Plan
- Version / Snapshot更新
- Reference Update
- Validation
- Legacy copied templateの整理
- Rollback / Restore guidance

---

# Temporary Workspace / Pycache Check

Documentation-only作業を基本とする。

検証スクリプト実行時に一時ファイルやpycacheが生成される可能性がある場合は、
既存GDS RepositoryのRuntime / Temporary Workspace Ruleに従う。
