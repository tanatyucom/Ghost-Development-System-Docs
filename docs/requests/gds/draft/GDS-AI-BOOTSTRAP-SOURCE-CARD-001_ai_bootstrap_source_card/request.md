# GDS-AI-BOOTSTRAP-SOURCE-CARD-001 Request

## Title

AI Bootstrap Source Card

## Purpose

新しいAIチャットやmemory / repository contextが不明なAI sessionが、最初にどこを
見に行くべきかを迷わないように、薄いBootstrap情報源を追加する。

## Scope

- Memory availability check.
- Repository as Single Source of Truth.
- First-read source order.
- Task-specific next source hints.
- SCW conditions when repository context is unavailable.
- README / docs index route.

## Out of Scope

- Runtime implementation.
- Validator implementation.
- New Startup architecture.
- GameGhost changes.
- Commit / Push / Tag.

## Completion Criteria

- Bootstrap Source Card exists.
- README / docs/READMEから辿れる。
- Startup Procedureから関連文書として辿れる。
- AI Repository Indexが更新される。
- Repository QualityがGreen。
- Commit / Push / Tagは実行しない。

## Suggested Commit Message

```text
docs: add AI bootstrap source card
```
