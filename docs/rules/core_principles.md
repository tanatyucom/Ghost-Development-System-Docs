# Core Principles

**Version:** 2.0

**Last Updated:** 2026-06-27

---

# Purpose

このドキュメントは Gray Ghost Archive の開発における基本思想を定義する。

すべての設計・実装・運用は、本ドキュメントの原則を基準として判断する。

---

# Core Principles

## Future Self First

数か月後・数年後の自分が理解できることを最優先とする。

現在の作業効率よりも、長期的な保守性を重視する。

---

## Human & AI Friendly

人にもAIにも理解しやすい構造を目指す。

可読性・責務分離・命名・レビューしやすさを重視する。

AIが推測ではなく、構造から正しく判断できる設計を目指す。

---

## One File One Theme

1つのMarkdownには1つのテーマだけを書く。

内容が大きくなった場合は、新しいMarkdownへ分割する。

---

## One Folder One Responsibility

1つのフォルダには1つの役割だけを持たせる。

異なる責務を混在させない。

---

## Single Entry Principle

利用者が最初に触る入口は可能な限り一つとする。

起動方法・入口・導線を分散させない。

---

## Three Second Rule

初めて見る人でも、3秒以内に

* 目的
* 役割
* 起動方法

がおおよそ理解できる構造を目指す。

---

## Clear Naming

名前だけで役割が分かる命名を採用する。

省略形よりも分かりやすさを優先する。

---

## Separation of Development and Operation

開発用と運用用を明確に分離する。

利用者向け入口と内部実装を混在させない。

---

## Documentation First

設計・運用・構造を変更した場合は、ドキュメントも同時に更新する。

ドキュメントを後回しにしない。

---

## Incremental Development

小さく改善し、小さくレビューし、小さく完成させる。

一度に大規模な変更を行わない。

各工程はレビュー・承認を経て次工程へ進む。

---

## Review Before Standardization

改善案はまず実際に運用する。

有効性が確認できたものだけを標準ルールとして採用する。

---

## Continuous Improvement

Gray Ghost Archive は完成して終わるプロジェクトではない。

実際の運用から得られた知見を継続的に反映し、品質向上を続ける。

---

# Development Philosophy

Gray Ghost Archive はコードを書くことを目的としない。

人生のアーカイブを長期的に維持できる仕組みを構築することを目的とする。

コードを書くことよりも、品質を積み重ねることを重視する。

そのために、

* 設計
* 品質
* 保守性
* 可読性
* 標準化

を継続的に改善する。

---

# Goal

Gray Ghost Archive は、

確かな仕事の積み重ねにより、

人にもAIにも理解しやすく、

長期運用できる個人アーカイブを構築する。
