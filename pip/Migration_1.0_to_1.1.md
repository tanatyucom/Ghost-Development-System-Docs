# Migration Guide: PIP v1.0 To v1.1

## Purpose

この文書は、既存の PIP v1.0 package を PIP v1.1 Stable へ移行する方法を説明します。

## Migration Summary

PIP v1.0 は project briefing package の concept を導入しました。

PIP v1.1 は次を追加して stable 化します。

- GitHub Docs と Information Package からの明確な役割分離。
- Required Improvement History。
- Required Decision History。
- Explicit AI collaboration flow。
- Command Center と future GIP の関係。
- Stable update rules。

## Required Changes

1. `00_README.md` を追加または更新する。
2. Current project status と priorities を確認する。
3. `06_DECISIONS.md` または Decision History section を追加する。
4. `07_LESSONS_LEARNED.md` または Improvement History section を追加する。
5. Source Documents を追加する。
6. Known Issues と Next Task を追加する。
7. AI Collaboration Notes を追加する。
8. 必要に応じて Command Center / future GIP notes を追加する。

## Mapping

| PIP v1.0 Concept | PIP v1.1 Concept |
|---|---|
| Project status | Project Status |
| Current priorities | Current Priorities |
| Changelog summary | Improvement History plus Changelog Summary |
| Decisions | Decision History |
| Lessons learned | Improvement History |
| AI collaboration | AI Collaboration Notes |
| Command Center vision | Command Center / GIP Relationship |

## Verification

PIP package を v1.1 として扱う前に、次を確認します。

- GitHub Docs が Single Source of Truth のままになっている。
- PIP は要約とリンクを提供しており、すべての rule を重複していない。
- Information Package は evidence-focused のままになっている。
- Improvement History に reviewed entry がある、または未記録であることを明示している。
- Decision History に accepted decisions がある、または未記録であることを明示している。
- Next Task が現在の状態を示している。
- Known Issues が現在の状態を示している。
- AI が次に読むべき文書を理解できる。

## Non-Goals

この migration では次を変更しません。

- runtime code。
- DB schema。
- Import / Apply behavior。
- Command Center implementation。
- GIP stable package definition。

## Suggested Completion Report Notes

PIP migration の完了報告には次を含めます。

- source PIP version。
- changed files。
- added Improvement History entries。
- added Decision History entries。
- unresolved stale sections。
- next Q。
