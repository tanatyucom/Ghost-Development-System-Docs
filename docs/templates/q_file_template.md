# Q File Template

Version:

Status:

Workflow:

Category:

Priority:

Commit:

```text
明示的な指示があるまで Commit しない。
Suggested Commit Message を提示する。
```

## Repository Information

実装内容を書く前に、対象プロジェクト、リポジトリ、編集境界を定義します。

### Target Project

この Q が扱うプロジェクト責務を記載します。

例:

```text
Ghost Development System
```

候補:

- Ghost Development System
- GameGhost
- AnimeGhost
- ComicGhost
- Other

Target Project が曖昧な場合、実装前に確認します。

### Repository

編集対象の repository name を記載します。

例:

```text
Ghost-Development-System-Docs
```

### Working Directory

AI が working directory として扱う repository root の absolute path を記載します。

例:

```text
C:\GitHub\Ghost-Development-System-Docs
```

### Documentation Root

documentation-related task の場合、documentation root の absolute path を記載します。

例:

```text
C:\GitHub\Ghost-Development-System-Docs\docs
```

### Runtime Root

runtime implementation が明示的に scope に入る場合のみ記載します。

documentation-only work の場合:

```text
対象外
```

### Single Source Of Truth

この Q で authoritative source として扱う repository または document set を
記載します。

例:

```text
Ghost Development System Docs
```

### Related Repository

参照するが編集しない repository、または scope に明示された場合のみ編集できる
repository を記載します。

例:

```text
GameGhost

参照のみ。
編集、同期、コピー、移行しない。
```

### Cross Project Impact

他 project への影響を記載します。

推奨値:

- None
- Reference Only
- Documentation Impact
- Runtime Impact
- Requires Separate Q

例:

```text
None
```

`None` 以外の場合、Related Repository と Scope Guard で編集可否を明確にします。

### Scope Guard

hard edit boundary を記載します。

例:

- Edit only `Ghost-Development-System-Docs/docs`.
- Treat GameGhost as reference only.
- Do not update files outside the listed target repository.
- Do not sync changes to related repositories.

## Purpose

この Q が達成する目的を記載します。

private context なしでも人間が期待結果を理解できるように書きます。

## Background

この Q が必要な理由を記載します。

必要に応じて、関連する roadmap review、decision、queue item、current focus、
previous work を含めます。

## Approved Decisions

すでに承認済みの decision を記載します。

未承認の idea はここに入れず、Review Requests または Future Candidates に置きます。

## Naming Policy

この Q に適用する naming rules を記載します。

推奨 default:

- roadmap item、Q title、public knowledge base topic は purpose-oriented name を
  優先する。
- implementation name は current target や method を明確にする場合のみ説明内で使う。
- legacy name や implementation-specific name は、必要に応じて Current Target、
  Current Implementation、Background として残す。

## Scope

この Q に含まれる work を記載します。

例:

- Documentation update only.
- Roadmap review only.
- Template update only.
- Rules review only.

## Do

具体的な work items を記載します。

例:

- Update `docs/roadmap/roadmap.md`.
- Review `docs/rules/`.
- Improve `docs/templates/q_file_template.md`.
- Align README purpose, scope, and repository structure.

## Do Not

out-of-scope items を明示します。

例:

- Do not change runtime code.
- Do not run Git migration.
- Do not update GitHub Actions.
- Do not create a release.
- Do not sync another repository.
- Do not commit.
- Do not implement Future Candidates.

## Target Files

想定する files または folders を記載します。

例:

- `README.md`
- `docs/roadmap/`
- `docs/rules/`
- `docs/templates/`

## Completion Criteria

完了条件を具体的に記載します。

例:

- Target Project が明記されている。
- Cross Project Impact が明記されている。
- Scope Guard が守られている。
- Runtime Code is not changed.
- Git Migration is not performed.
- Commit is not created.
- Related repositories are not updated, synced, or copied.
- Changed files and summary are reported.
- Remaining Issues, improvement proposals, Recommended Next Q, and Suggested
  Commit Message are included.

## Review Requests

レビュー観点を記載します。

例:

- long-term maintainability。
- AI collaboration quality。
- public knowledge base clarity。
- purpose-oriented naming。
- responsibility boundaries。
- roadmap consistency。
- workflow fit。
- template reusability。
- Cross Project Impact。
- Japanese-first readability。

## Future Candidates

この Q では実装しないが、将来検討すべき ideas を記載します。

例:

- Development Knowledge Platform.
- Development Knowledge DB.
- Dependency Index.
- Universal Project Search.
- Documentation Impact Analyzer.
- Architecture Viewer.
- Cross Project Impact Matrix.

## Acceptance Criteria

受け入れ条件を記載します。

例:

- Target documents are updated.
- Scope and non-scope are respected.
- Repository Information is complete enough to prevent repository or edit-target
  confusion.
- Target Project is clear enough to prevent project responsibility confusion.
- Cross Project Impact is reviewed.
- Public names describe purpose before implementation technique.
- Future Candidates remain separate from approved work.
- Rules, roadmap, templates, and README are consistent.
- Commit is not created when the Q says not to commit.

## Deliverables

最終報告に含める項目を記載します。

推奨:

- Changed Files.
- Summary.
- Verification.
- Metrics / Evidence.
- Improvement Review.
- Recommended Improvements.
- Future Candidates.
- Remaining Issues.
- Recommended Next Q.
- Suggested Commit Message.

## Improvement Review

完了した work から、次を改善すべきか review します。

- Documentation.
- Templates.
- Workflow.
- Roadmap.
- Rules.
- Architecture.
- Knowledge Base.
- Metrics / Evidence.

### Recommended Improvements

近いうちに採用すべき高価値な improvements を記載します。

### Future Candidates

将来採用すべき ideas を記載します。

## Suggested Commit Message

```text
docs: update ghost development system knowledge base
```

## Writing Notes

- Ghost Development System Docs の Q file は日本語を基本とする。
- Proper nouns、commands、paths、filenames、identifiers、commit messages は
  English のまま残してよい。
- Target Project を実装前に宣言する。
- Cross Project Impact を明示する。
- Future Candidates を approved work から分離する。
- out-of-scope items を明示して scope drift を防ぐ。
- Repository Information を Q の上部に置く。
- Knowledge evolves through implementation.
- Reusable knowledge should be promoted to templates, rules, examples, or
  documentation whenever practical.
