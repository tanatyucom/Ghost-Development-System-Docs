# Template Synchronization Guidelines

## When To Check

次の作業を開始する前にCanonical Template Synchronizationを確認する。

- Q作成
- ADR作成
- Roadmap更新
- Completion Report作成
- Startup evidence作成
- 外部Raw URLまたはローカルコピーからテンプレートを参照する作業

## Minimum Procedure

1. Startupが完了していることを確認する。
2. AI Repository Indexから正本導線を確認する。
3. Current Missionを確認し、今回の作業目的とスコープを合わせる。
4. 使用テンプレートの正本パスと版を確認する。
5. Canonical Repositoryが期待するRepositoryであることを確認する。
6. Raw URLや外部コピーを使う場合は鮮度を確認する。
7. 不一致があれば、採用したActionを記録する。

## Mismatch Actions

| Action | Use When |
| --- | --- |
| Use canonical template | ローカルコピーより正本テンプレートを優先できる。 |
| Update local copy | ローカルコピーが古く、正本へ合わせる必要がある。 |
| Create revision Q | テンプレート自体の改善が必要。 |
| Record limitation | 参照できない理由を残して作業を進める。 |
| Not applicable | Raw参照や外部コピーを使っていない。 |

## Human Approval

テンプレート同期確認は、作業開始前の品質ゲートである。ただし、自動更新、自動Q生成、自動Commitの承認ではない。

同期不一致が作業範囲に影響する場合は、人間に判断可能な形で理由と選択肢を提示する。

## Review Notes

- Raw URLは便利だが、正本Repository内のファイルより優先しない。
- 古いテンプレートから作られたArtifactは、そのまま修正せず、必要ならRevision Qとして扱う。
- Current Missionと矛盾するテンプレート項目がある場合は、テンプレートではなくMissionを正本として扱い、差分をCompletion Reportに記録する。
