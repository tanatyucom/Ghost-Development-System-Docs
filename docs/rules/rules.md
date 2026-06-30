# Gray Ghost Archive Rules

**Version:** 2.0

**Last Updated:** 2026-06-27

---

## Purpose

このドキュメントは Gray Ghost Archive の Rules 全体における総則・目次である。

Rules は Gray Ghost Archive の開発・運用における最上位設計書であり、他のドキュメントより優先される。

本プロジェクトでは、ルールを一つの巨大ファイルへ集約せず、役割ごとに分割して管理する。

---

## Rule Priority

Rules は以下のドキュメントより優先される。

1. Rules
2. Workflow
3. Architecture
4. Roadmap
5. Status
6. Queue
7. Research

他ドキュメントと矛盾が発生した場合は、Rules を優先し、必要に応じて該当ドキュメントを更新する。

---

## Rule Organization

Rules は「One File One Theme Rule」を基本とする。

各ルールは独立した Markdown として管理し、役割ごとに分割する。

`rules.md` は Rules 全体の入口および目次として機能する。

新しいルールを追加する場合は、既存ファイルへ統合できないかを最初に検討する。

統合できない場合のみ、新しい Rule ファイルを作成する。

---

## Rule Documents

### Core Rules

* `core_principles.md`

Gray Ghost Archive の基本思想・開発憲章を管理する。

---

### Documentation Rules

* `documentation_rules.md`

ドキュメント構造・README・命名・フォルダ運用を管理する。

---

### Workflow Rules

* `workflow_rules.md`

開発手順・レビューゲート・標準開発フローを管理する。

---

### Git Rules

* `git_rules.md`

コミット・ブランチ・差分確認・履歴管理を管理する。

---

### Quality Rules

* `quality_rules.md`

品質保証・安全運転・動作確認・長期運用性を管理する。

---

### AI Collaboration Rules

* `ai_collaboration_rules.md`

ChatGPT・Codex・Gemini・Claude 等との共同開発ルールを管理する。

---

## One File One Theme Rule

1つのMarkdownには、1つのテーマだけを記載する。

異なる目的の内容を同一ファイルへ混在させない。

内容が大きくなった場合は、新しいMarkdownへ分割する。

これにより、以下を向上させる。

* レビューしやすさ
* Git管理
* AI共同開発
* 保守性
* 一括コピペ時の安全性

---

## Rule Creation Policy

新しい Rule は思いつきで追加しない。

以下の流れで標準化する。

1. 実際に運用する
2. 有効性を確認する
3. 問題点を整理する
4. Rules へ反映する

実績に基づいた改善のみを正式な Rule とする。

---

## Rule Change Policy

ルールを追加・変更・削除する場合は、以下を確認する。

* 変更理由
* 期待される効果
* 影響範囲
* 既存ルールとの整合性

必要に応じて Decision Log へ変更理由を記録する。

---

## Standardization Rule

新しい設計や運用方法は、実際に運用して有効性を確認してから標準化する。

標準化は目的ではなく、改善結果を定着させる手段である。

机上の理論ではなく、実績を基にルール化する。

---

## Update Policy

Rules は安易に変更しない。

新しいルールを追加する場合は、既存ルールへ統合できないか確認する。

ルールが肥大化した場合は、One File One Theme Rule に従って分割する。

改善提案は歓迎する。

ただし、以下のいずれかに該当する場合を除き、現在の工程を完了してから反映する。

* 後工程で大規模な手戻りが発生する
* 土台となる設計に問題がある
* 後回しにすることで品質低下や重大な混乱が発生する

このような場合は、Critical Improvement Rule を適用し、現在の工程を一時停止して改善を優先する。

---

## Goal

Rules を分割管理することで、将来の自分とAIが迷わず参照できる開発憲章を維持する。

Gray Ghost Archive は、確かな仕事の積み重ねにより、人にもAIにも分かりやすく、長期運用できる個人アーカイブを構築する。
