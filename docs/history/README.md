# History

## Purpose

このフォルダは、Ghost Development System Knowledge Base 自身の進化を記録します。

Knowledge Base の version ごとに、何を追加したか、なぜ追加したか、Knowledge
Base がどのように成長したかを簡潔に残します。

## Contains

- `knowledge_base_history.md`: Knowledge Base 自身の version history。

## Does NOT Contain

- GameGhost の development history。
- runtime implementation history。
- release changelog。
- detailed Decision Log。
- Queue execution state。

## Responsibility Separation

Knowledge Base History は、Knowledge Base の構造、運用ルール、review quality、
navigation、project management の進化を記録します。

Decision Log は、個別の重要 decision、選択肢、理由、採用結果を記録するための
ものです。

Development History は、runtime development や project-specific implementation
の進行を記録するためのものです。

Knowledge Base History は、それらを置き換えません。Knowledge Base 自身がどう
進化したかを振り返るための軽量な履歴です。

## Update Policy

Knowledge Base の大きな更新後に追記します。

追記する内容:

- Version。
- Added。
- Reason。
- Evolution。

詳細な議論、代替案、承認経緯が必要な場合は、Decision Log または別 Q で扱います。

## Related Documents

- `docs/history/knowledge_base_history.md`
- `docs/README.md`
- `docs/rules/project_rules.md`
- `docs/rules/language_rules.md`
- `docs/roadmap/ghost_development_system_roadmap.md`
- `docs/templates/review_checklist.md`
