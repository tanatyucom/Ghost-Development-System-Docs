# Documentation Rules

**Version:** 2.0

**Last Updated:** 2026-06-27

---

# Purpose

このドキュメントは Gray Ghost Archive のドキュメント管理・構造・運用ルールを定義する。

すべての設計書・README・仕様書は、本ルールに従って管理する。

---

# Documentation Principles

## Documentation is Code

コードとドキュメントは同じ品質で管理する。

仕様変更・構成変更・運用変更を行った場合は、対応するドキュメントも同時に更新する。

コードだけ、またはドキュメントだけが古い状態を作らない。

---

## Documentation First

新しい仕組みや構造を導入する場合は、必要なドキュメントを先に整備する。

設計を明確にしてから実装へ進む。

---

## One Document One Purpose

1つのMarkdownには1つの目的だけを書く。

内容が肥大化した場合は、新しいMarkdownへ分割する。

---

# README Rules

## README Purpose

各フォルダには README を配置する。

README は説明書ではなく、そのフォルダの運用ルールとする。

---

## README Standard

README には最低限、以下を記載する。

* Purpose
* Contains
* Does NOT Contain
* Update Policy
* Related Documents

---

## README Maintenance

フォルダ構成や運用方法が変更された場合は、README を最優先で更新する。

README と実際の構成を一致させる。

---

# Documentation Structure

## Folder Responsibility

ドキュメントは役割ごとに分離する。

* architecture
* rules
* workflow
* roadmap
* status
* decisions
* queue
* schema
* research

各ドキュメントは責務を明確にし、複数の役割を持たせない。

役割が曖昧になった場合は、新しいドキュメントへの分割を検討する。

役割が重複する場合は、新しいドキュメントを作る前に既存ドキュメントとの統合を検討する。

---

## Queue Rule

Queue は作業管理専用とする。

仕様・設計・実装内容を書かない。

実装方法は別ドキュメントで管理する。

将来的には

> 1 Task = 1 Markdown

を基本とする。

---

## Research Rule

Research は調査資料を保存する場所である。

調査結果をそのまま正式仕様へ採用しない。

Decision を経由して採用を判断する。

---

## Decision Rule

Decision は

「何を変更したか」

ではなく

「なぜ変更したか」

を残す。

---

## Roadmap Rule

Roadmap は将来計画のみを書く。

設計・仕様・実装内容を書かない。

---

## Status Rule

Current Focus は現在進行中の内容のみを書く。

完了した内容は History・Decision・Queue など適切な場所へ移動する。

---

# Documentation Update

## Update Timing

ドキュメントは開発完了後ではなく、開発と並行して更新する。

---

## Review

ドキュメントもコードと同様にレビュー対象とする。

レビュー完了後に正式版として採用する。

---

## Incremental Documentation

ドキュメントも小さく作成し、小さくレビューし、小さく完成させる。

大規模な一括更新を避ける。


---

## Documentation Delivery

レビュー完了後のドキュメントは、
差分ではなく最新版ファイルとして納品する。

既存ファイルは最新版で上書きし、
履歴管理は Git を唯一の正とする。

Documentation は常に最新版のみを運用対象とする。

---

# Goal

ドキュメントを資産として管理し、

人にもAIにも迷いのない構造を維持する。

ドキュメントはコードを補足するものではなく、

Gray Ghost Archive の設計・運用・品質を支える重要な構成要素とする。

ドキュメントは、人にもAIにも迷いなく理解できる構造を維持するための資産である。
