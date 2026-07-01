# Language Rules

**Version:** 1.0

**Last Updated:** 2026-07-01

## Purpose

この文書は、Ghost Development System Docs の日本語運用ルールを定義します。

人間が判断、承認、レビューする文章は、日本語を基本とします。

## Japanese First

Ghost Development System のドキュメントは日本語を基本とします。

対象:

- Q ファイル。
- レビュー。
- テンプレート。
- ルール。
- ロードマップ。
- Completion Report。
- Codex 依頼文。
- Architecture 文書。
- Workflow 文書。
- Knowledge Base Index。

## English Allowed

次のものは英語のまま扱ってよいです。

- ソースコード。
- API。
- クラス名。
- 関数名。
- ファイル名。
- パス。
- Commit Message。
- Git コマンド。
- 固有名詞。
- 外部仕様で英語表記が必要なもの。
- 英語でないと意味が壊れる識別子。

## Human Approval Rule

人間が理解できない依頼文は Human Approval を満たしません。

AI は、人間が承認するための目的、背景、Scope Guard、Do、Do Not、
Completion Criteria、Improvement Review を日本語で書くことを基本とします。

## Decision Background

Japanese First の理由:

Human Approval は、人間が目的、背景、scope、risk、completion criteria を理解
したうえで判断することを前提とするため。

人間が理解できない依頼文やレビュー文は、形式上承認されても実質的な Human
Approval を満たしません。

## Mixed Language Policy

日本語本文の中で、ファイル名、コマンド、識別子、固有概念を英語のまま残すこと
は許可されます。

例:

- `docs/templates/q_file_template.md`
- `git status --short`
- Target Project
- Scope Guard
- Single Source Of Truth
- Future Candidate

ただし、英語の概念を使う場合でも、人間の判断に必要な説明は日本語で補足します。

## Template Rule

テンプレートは日本語を基本とします。

ただし、見出しやフィールド名は AI と既存文書の互換性を保つため、英語表記を
残してよいです。

例:

- Repository Information
- Target Project
- Cross Project Impact
- Deliverables
- Suggested Commit Message

## Update Policy

日本語運用で混乱が起きた場合、またはテンプレートや AI 依頼文で人間の承認が
難しくなった場合、このルールを更新します。
