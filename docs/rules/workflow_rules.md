# Workflow Rules

**Version:** 2.0

**Last Updated:** 2026-06-27

---

# Development Workflow Version 2.0 Trial

Development Workflow Version 2.0 is in trial for Ver1.4.

Reference:

```text
docs/workflow/development_workflow_v2_trial.md
```

The trial may be used for Ver1.4 operations, but it is not yet promoted to
permanent workflow rules. Promote it only after retrospective evidence shows
that it reduces operational mistakes and improves resume quality.

During the trial:

- update Current Focus when creating a Queue item;
- update Current Focus after completing a Queue item;
- move completed Queue items before moving Current Focus to the next task;
- run a short retrospective after completion;
- record proposed rule/template/workflow improvements as future candidates
  unless the active specification explicitly includes them.

---

# Purpose

このドキュメントは Gray Ghost Archive の標準開発フローを定義する。

すべての開発は、本ドキュメントの手順を基本として進める。

---

# Development Workflow

## Incremental Development

開発は小さな単位で進める。

一度に大規模な変更を行わず、

* 作成
* レビュー
* 修正
* 完成

を繰り返しながら品質を高める。

---

## Scope Freeze Rule

現在の工程に集中する。

次工程の内容を先取りしない。

改善案は記録し、現在の工程完了後に反映する。

---

## Critical Improvement Rule

ただし、

後工程で大きな手戻りが発生すると判断した場合は例外とする。

その場合は

* 問題点
* 後回しにした場合のリスク
* 今対応する理由

を説明した上で、

現在の工程を一時停止して改善を優先する。

改善後は元の工程へ戻る。

---

## Review Gate Rule

レビューを完了してから次工程へ進む。

未レビューの成果物を正式版として扱わない。

---

## Completed Draft Rule

レビュー用ではなく、

最初から完成版を提示する。

部分的な差分ではなく、

ファイル全体を提示することで、

コピペミスや編集漏れを防止する。

---

## Copy & Paste Safety Rule

修正は可能な限り一括コピペで行う。

部分修正よりも、

ファイル全体の置き換えを優先する。

ヒューマンエラーを最小限に抑えることを目的とする。

---

## Feedback Loop Rule

成果物をレビューし、

改善点を洗い出し、

必要に応じて修正する。

レビュー結果は次回以降の標準フローへ反映する。

---

## Standardization Rule

改善方法は、

実際に効果が確認できたものだけを標準ルールとする。

机上の理論ではなく、

運用実績を重視する。

---

## Verification Rule

各工程は以下の流れで進める。

1. 作成
2. レビュー
3. 修正
4. 再レビュー
5. 完了判定
6. Commit

「完成した」と判断する前に、必ずレビューを実施する。

レビューで問題が見つかった場合は、修正後に再レビューを行う。

---

# Development Cycle

標準的な開発手順は以下とする。

1. 完成版を作成する
2. 一括コピペで反映する
3. レビューを実施する
4. 必要に応じて完成版を再生成する
5. 再レビューを行う
6. Commitする
7. 次の工程へ進む

---

# AI Collaboration

AI は改善提案を歓迎する。

ただし、

Scope Freeze Rule を基本とし、

重大な手戻りを防ぐ場合のみ例外として改善を提案する。

推測ではなく、

実際の構造・ファイル・レビュー結果を基に判断する。

---

# Goal

開発品質を継続的に向上させ、

人にもAIにも分かりやすく、

安全かつ再現性の高い開発フローを維持する。

本フローは、人・AIを問わず同じ品質基準で運用する。
