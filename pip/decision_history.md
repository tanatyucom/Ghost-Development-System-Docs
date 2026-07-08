# PIP Decision History

## Purpose

この文書は、Ghost Development System における PIP-level decisions を記録します。

Decision History は、PIP が現在の構造になっている理由と、人間、AI assistant、
future tools が PIP をどう使うべきかを説明します。

## Decision Entry Format

```text
Decision:
Status:
Reason:
Impact:
Not Included:
Follow-up:
```

## Decisions

### Adopt PIP v1.1 As Stable

Decision:

PIP v1.1 Stable を、GDS の正式な project briefing standard として採用します。

Status:

Accepted。

Reason:

PIP v1.0 は concept を作りましたが、現場作業の結果、current state、Improvement
History、Decision History、AI handoff guidance を持つ stable briefing layer が必要だと
分かりました。

Impact:

- PIP は README と Knowledge Base Index から参照されます。
- PIP v1.1 は briefing、evidence、official documentation の役割を分離します。
- 将来の project briefing は v1.1 structure に従います。

Not Included:

- Runtime code。
- DB changes。
- Import / Apply changes。
- Command Center implementation。

Follow-up:

今後の GDS および project-level handoff package で PIP v1.1 を使います。

### Keep GitHub Docs As Single Source Of Truth

Decision:

PIP は official documents を要約し、参照先を示します。Rules、Workflow、
Architecture、Roadmap、Templates、Examples、Glossary を置き換えません。

Status:

Accepted。

Reason:

PIP は briefing に最適化されています。Official GDS Docs は source of truth、
review、Git-managed knowledge に最適化されています。

Impact:

PIP は読みやすく簡潔に保ちながら、詳細な標準は適切な folder に残せます。

Not Included:

既存の authority order の変更。

Follow-up:

Official GDS Docs が変わった場合、PIP が古くなっていないか review します。

### Reserve GIP As Future Concept

Decision:

PIP を stable project-level package として使います。GIP は、別Qで正式定義されるまで
future concept として扱います。

Status:

Accepted as direction。

Reason:

まず stable PIP が必要です。GIP を早く定義しすぎると、PIP、Information Package、
Command Center、Knowledge Asset Layer の責務が曖昧になります。

Impact:

Command Center は PIP を利用できますが、現在の workflow で GIP を前提にしません。

Not Included:

Formal GIP specification。

Follow-up:

PIP が複数 project context で検証された後、GIP 用のQを作ります。

### Adopt Trace Before Tune As Review Methodology

Decision:

PIP v1.1 に Trace Before Tune を review methodology として追加します。

Status:

Accepted。

Reason:

Roadmap2 の OCR review では、最終結果から直接修正すると、row boundary、crop、bbox、
candidate selection など、最初に壊れた step を見落とす危険がありました。

Impact:

PIP は、改善前に trace artifact と expected state を確認する考え方を briefing に含めます。

Not Included:

OCR logic、DB、Import / Apply、Production logic の変更。

Follow-up:

Trace Before Tune を future templates と review checklist に反映します。

### Adopt First Broken Step

Decision:

PIP v1.1 に First Broken Step を正式な review viewpoint として追加します。

Status:

Accepted。

Reason:

後段の失敗は、前段の geometry、boundary、crop、identity、classification の失敗から
派生することがあります。最初に壊れた step を見つけることで、不要な調整を避けられます。

Impact:

PIP と completion-style reports は、原因調査時に最初の破綻点を説明するべきです。

Not Included:

特定 project の runtime implementation。

Follow-up:

Debug Artifact Review と Audit Before Repair の future update 候補にします。

### Standardize Review Entry Point

Decision:

artifact が多い review では、Review Entry Point を標準の review handoff として扱います。

Status:

Accepted。

Reason:

contact sheet、overlay、crop、CSV、Markdown report が増えると、人間や別AIがどこから
見ればよいか分からなくなります。

Impact:

PIP、Completion Report、review package は、最初に見る artifact と理由を示すべきです。

Not Included:

全 artifact の Git 管理義務化。

Follow-up:

Review Entry Point を PIP template set に反映します。

### Preserve Human Visual Review As Quality Gate

Decision:

visual quality が関係する処理では、Human Visual Review を品質保証プロセスとして扱います。

Status:

Accepted。

Reason:

AI score や自動分類だけでは、切り出し位置、対象行、見切れ、過剰範囲、視覚的妥当性を
十分に判断できない場合があります。

Impact:

PIP は visual artifact と人間レビューの関係を briefing に含めます。

Not Included:

Human Approval の自動置換。

Follow-up:

Command Center / review UI が PIP の Review Entry Point を読める形を検討します。

### Adopt Evaluate What Actually Matters

Decision:

PIP v1.1 に Evaluate What Actually Matters を review methodology として追加します。

Status:

Accepted。

Reason:

Roadmap2 delta package では、metric が proxy を評価していても、実際の品質対象である
title text、visual containment、target identity が壊れる可能性が示されました。

Impact:

PIP は、metric が何を評価しているかと、実際に守るべき品質対象が一致しているかを
review viewpoint として扱います。

Not Included:

Metric implementation の変更。

Follow-up:

Review checklist と PIP template set に反映します。

### Adopt Target Row Trace / Pipeline Trace As Standard Artifact Option

Decision:

PIP v1.1 では、Target Row Trace / Pipeline Trace を complex debugging の standard
artifact option として扱います。

Status:

Accepted。

Reason:

Target Row Identity、Title BBox、crop、OCR のどこで壊れたかを分けないと、後段の
調整で前段の破綻を隠してしまうためです。

Impact:

難しい debug Q では、First Broken Step と trace artifact を completion report や PIP
candidate に残すべきです。

Not Included:

Trace artifact の常時生成。

Follow-up:

Debug Artifact Review Workflow の future update 候補にします。

### Add Steam OCR v2 Case Index

Decision:

Steam OCR v2 debugging sequence を PIP case index として保存します。

Status:

Accepted。

Reason:

Roadmap2 delta package は、Trace Before Tune、Human Visual Review、Review Entry
Point、First Broken Step の実例を複数含んでいます。

Impact:

PIP は抽象ルールだけでなく、再利用可能な case として改善知識を残します。

Not Included:

GameGhost runtime への変更。

Follow-up:

将来の PIP template set に Case Index format を追加します。
