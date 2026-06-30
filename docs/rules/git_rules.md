# Git Rules

**Version:** 2.0

**Last Updated:** 2026-06-27

---

# Purpose

このドキュメントは Gray Ghost Archive における Git の運用ルールを定義する。

履歴を資産として管理し、将来の自分とAIが変更履歴を容易に理解できることを目的とする。

---

# Git Philosophy

## Git is History

Git は単なるバックアップではない。

設計・改善・開発の履歴を記録するための資産である。

---

## One Commit One Purpose

1つのコミットには1つの目的だけを含める。

複数の目的を混在させない。

---

## Meaningful Commit

コミットメッセージは

「何をしたか」

だけではなく、

「何が完成したか」

が分かる内容とする。

---

## Small Commit

コミットは小さく行う。

大規模な変更を一つのコミットへまとめない。

---

# Commit Workflow

## Review Before Commit

レビュー完了後に Commit を行う。

レビュー前の成果物は正式版として扱わない。

---

## Complete Before Commit

完成していない成果物は Commit しない。

途中保存ではなく、

意味のある区切りで Commit を行う。

---

## Commit Story Rule

コミット履歴は、

一冊の本を読むように理解できる構成を目指す。

各コミットは一つの章として意味を持つよう設計する。

---

# Branch Policy

## Stable Development

基本開発は develop ブランチで行う。

安定版は main ブランチで管理する。

---

## Logical History

履歴を書き換えることよりも、

履歴の分かりやすさを重視する。

---

# Verification

## Git Status First

Commit 前には必ず

```bash
git status
```

を確認する。

不要なファイルが含まれていないことを確認する。

---

## Diff Review

Commit 前には必要に応じて

```bash
git diff
```

または

```bash
git diff --cached
```

を確認する。

レビュー可能な状態で Commit を行う。

---

# Documentation

Rules・README・設計書の変更も、

コードと同じ品質で Commit を行う。

ドキュメントだけ後回しにしない。

---

# Goal

Git を単なる履歴管理ツールではなく、

Gray Ghost Archive の成長記録として活用する。

人にもAIにも変更履歴が読みやすく、

長期運用できる Git 履歴を維持する。
