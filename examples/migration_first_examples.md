# Migration First Examples

## Purpose

この文書は、内部 architecture を変更するときに Migration First をどう使うかを
示す例です。

Examples は参考資料です。正式な判断は `docs/rules/migration_first_rules.md`
と Q の Scope Guard に従います。

## Bad: Chat Only Internal Rename

Bad:

```text
チャットで「old_scripts を new_scripts に変えて」とだけ依頼する。
旧 path 参照を探さない。
旧 path fallback を残す。
Completion Report に Remaining Legacy を書かない。
```

Problem:

- Codex が旧 path を参照し続ける。
- どの構造が標準かわからない。
- fallback が恒久化する。
- 後から削除条件が追えない。

## Good: Q Artifact With Migration Plan

Good:

```text
Q artifact:
  New Standard: scripts/review/
  Migration Plan: old review scripts を scripts/review/ に移す
  Reference Update: README, workflow, templates, tests, examples を更新する
  Verification: rg old_scripts, test, dry-run
  Legacy Removal: old_scripts fallback を削除する
  Public Compatibility Impact: None
  Remaining Legacy: None expected
  Restore / Rollback Guidance: git restore <changed files>
```

Result:

- 新標準が明確になる。
- 旧参照の更新漏れを検出できる。
- legacy removal が completion criteria になる。
- completion report で migration result を確認できる。

## Bad: Permanent Internal Fallback

Bad:

```text
新しい artifact workspace を追加する。
古い workspace も無期限で読み続ける。
なぜ残すかを書かない。
削除予定を書かない。
Public Compatibility と internal convenience を混同する。
```

Problem:

- internal convenience が public contract のように扱われる。
- Queue Manager や Artifact Manager が二重構造になる。
- AI が古い workspace を正しい入力として扱う。

## Good: Temporary Fallback With Removal Plan

Good:

```text
Temporary legacy fallback:
  Reason: 既存 approved Q の completion report がまだ旧 workspace を参照している
  Removal plan: 参照更新後に fallback を削除する
  Completion criteria: rg で旧 workspace 参照がないことを確認する
  Remaining Legacy: completion report に残件として報告する
  Follow-up Q: 旧 workspace 参照削除 Q を作る
```

Result:

- fallback が一時的であることが明確になる。
- 削除条件が残る。
- 次の Q へつながる。

## Bad: Public Compatibility Overreach

Bad:

```text
内部 prototype script の名前を変えるだけなのに、全旧 command を永久維持する。
```

Problem:

- public API / CLI ではない内部 helper まで互換対象になる。
- script architecture が複雑化する。

## Good: Public Compatibility Boundary

Good:

```text
Public Compatibility Impact:
  public CLI: No impact
  documented external workflow: No impact
  exported artifact schema: No impact
  DB schema: No impact
  user-facing data format: No impact

Internal change:
  prototype script path を新標準へ移行する
  old prototype path は削除する
```

Result:

- 守るべき公開 contract と、移行してよい内部構造が分かれる。
- レビュー範囲が小さくなる。

## Completion Report Example

```text
Migration First Review

- Migration First applies: Yes
- New Standard: docs/requests/<project>/<status>/<Q_ID>_<short_topic>/
- Migration Plan result: completed
- Reference Update result: README, templates, workflow updated
- Verification result: rg old path returned no active references
- Legacy Removal result: old fallback removed
- Public Compatibility Impact: None
- Remaining Legacy: None
- Restore / Rollback Guidance: git restore <changed files>
```
