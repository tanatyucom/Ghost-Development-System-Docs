# Migration First Internal Architecture Rules

**Version:** 1.0

**Last Updated:** 2026-07-04

## Purpose

Ghost Development System の内部構造を変更するときは、互換 fallback を
積み増す前に、標準構造へ一度移行する方針を優先する。

内部開発向けの構造は、古い path、古い script、古い interface を長期的に
抱え続けない。必要な場合は migration plan を作り、参照を更新し、検証後に
legacy を削除する。

## Core Rule

内部 architecture の変更は原則として次の順序で行う。

```text
New Standard
  -> Migration Plan
  -> Reference Update
  -> Verification
  -> Legacy Removal
```

旧構造との互換 fallback は、恒久的な設計ではなく、一時的な移行支援として
扱う。

## Applies To

このルールは、Ghost Development System と関連 implementation repositories
の内部開発構造に適用する。

- internal folder structure
- internal script layout
- adapter internal interface
- prototype scripts
- shared utility location
- artifact workspace layout
- queue / request internal structure
- future GhostCore / GDS internal modules

## Public Compatibility Boundary

Public Compatibility は、外部利用者や公開された workflow を壊さないために
必要な範囲へ限定する。

Public Compatibility を優先してよい対象:

- public release
- public API
- public CLI
- documented external workflow
- exported artifact schema
- DB schema
- user-facing data format

内部 folder、内部 script、prototype path、review helper、temporary adapter は、
公開 contract として文書化されていない限り、恒久互換の対象にしない。

## Legacy Rule

Legacy code、legacy path、compatibility fallback は次の条件を満たす場合のみ
一時的に許可する。

- 残す理由を Q、実装依頼、または completion report に明記する。
- 削除計画を `Legacy Removal` として明記する。
- completion criteria に legacy removal または remaining legacy review を含める。
- 恒久互換として扱わない。
- completion report に remaining legacy の有無を報告する。

理由、削除計画、検証方法がない legacy fallback は追加しない。

## Human Approval Gate

Migration work は Human Approval Gate の対象である。

次の場合は、実装前に approval または明示的な Q が必要になる。

- internal architecture standard を変更する。
- 既存 folder / script / interface を移動または削除する。
- public compatibility に影響する可能性がある。
- rollback / restore guidance が必要な変更を行う。

## Required Q Fields

内部 architecture の変更を含む Q には、次を含める。

- Migration Plan
- Reference Update
- Legacy Removal
- Public Compatibility Impact
- Remaining Legacy
- Restore / Rollback Guidance

## Required Completion Report Fields

Migration First が関係する completion report には、次を報告する。

- Source Q File
- New Standard
- Migration Plan result
- Reference Update result
- Verification result
- Legacy Removal result
- Public Compatibility Impact
- Remaining Legacy
- Restore / Rollback Guidance

## Decision Background

内部構造に compatibility fallback を重ね続けると、AI が古い path や旧 interface
を誤って使い、レビュー対象が増え、将来の Command Center、Queue Manager、
Artifact Manager、Automation が複雑になる。

GDS の内部 architecture は、公開互換性を守る場所と、移行して単純化する場所を
分けて扱う。

## Goal

Migration First は、Human Approval を支え、コピペ事故や古い参照の残留を防ぎ、
Git 管理しやすく、Knowledge 化しやすい内部構造を維持するためのルールである。
