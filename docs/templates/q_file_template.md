# Qファイルテンプレート

Status:

Workflow:

Category:

Priority:

Commit:

```text
Commit は行わないでください。レビュー待ちにしてください。
```

---

# 目的

この Q で何を達成したいかを短く書く。

人間が読み直したときに、作業のゴールがすぐ分かることを優先する。

---

# 背景

なぜこの Q が必要になったかを書く。

関連する Roadmap Review、Decision、Queue、Current Focus、過去の作業があれば
ここに書く。

---

# 決定事項

すでに Roadmap Review や設計レビューで承認済みの判断を書く。

未承認の案や迷っている内容は、ここではなく「レビュー依頼」または
「Future送り候補」に書く。

---

# 作業範囲

今回扱う範囲を書く。

例:

- Documentation update only.
- Roadmap review only.
- Template update only.
- Runtime code は変更しない。

---

# やること

Codex に実行してほしい具体的な作業を書く。

例:

- `docs/templates/q_file_template.md` を作成または更新する。
- `docs/templates/README.md` に参照を追加する。
- 既存テンプレートと重複しないように整理する。

---

# やらないこと

スコープ外を明確に書く。

例:

- Runtime code は変更しない。
- Git migration は行わない。
- ファイル移動は行わない。
- Commit は行わない。
- 未承認の Future 機能は実装しない。

---

# 対象ファイル

変更候補のファイルを書く。

例:

- `docs/templates/q_file_template.md`
- `docs/templates/ai_implementation_request.md`
- `docs/templates/README.md`
- `docs/queue/README.md`

対象外のファイルがある場合もここに書く。

---

# 納品物

Codex に報告してほしい項目を書く。

例:

- Changed Files
- 更新内容
- 既存テンプレートとの関係
- Workflow / Queue への反映内容
- Verification
- Remaining Issues
- Recommended Next Q
- Suggested Commit Message

---

# 受け入れ条件

完了判定に使う条件を書く。

例:

- 日本語 Q ファイルテンプレートが作成または更新されている。
- 目的 / 背景 / 作業範囲 / やること / やらないこと / 納品物 /
  受け入れ条件が含まれている。
- 推奨・任意事項と Future 送り候補を書ける欄がある。
- Commit しない方針が明記されている。
- Runtime code、Git migration、ファイル移動が行われていない。

---

# 推奨・任意事項

Codex が必要に応じて採用してよい改善案を書く。

採用する場合は、既存の Roadmap、Rules、Workflow、Queue、Templates と矛盾しない
ことを確認する。

複雑さが増える場合は、今回入れずに Future 送り候補へ回す。

---

# Future送り候補

今回は入れないが、将来検討してよい項目を書く。

例:

- Architecture Decision Record
- Plugin System
- Event Bus
- Module SDK
- Extension API
- Documentation Impact Analyzer
- Dead Documentation Detector
- Duplicate Idea Checker
- Improvement Collector
- Technical Debt Tracker

---

# レビュー依頼

Codex にレビューしてほしい観点を書く。

例:

- architectural consistency
- long-term maintainability
- documentation quality
- roadmap clarity
- responsibility boundaries
- implementation guardrails
- naming clarity
- workflow fit

---

# Commit方針

基本方針:

```text
Commit は行わないでください。レビュー待ちにしてください。
```

Suggested Commit Message:

```text
docs: add japanese q file template
```

---

# 記述ルール

- 本文は日本語を基本にする。
- 固有名詞、コマンド、ファイル名、識別子は英語のままでよい。
- 人間が読んで判断しやすいことを優先する。
- Codex 向けだけのブラックボックス的な指示にしない。
- Roadmap Review では、採用 / 追加 / Future 送りを判断しやすく書く。
- スコープ外を明確にして、暴走を防ぐ。
