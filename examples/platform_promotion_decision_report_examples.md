# Platform Promotion Decision Report Examples

## Purpose

この文書は、Platform Promotion Decision Report Template の実運用例を示します。

正式な template は `templates/platform_promotion_decision_report_template.md` です。
この examples は、Promote、Revise、Reject、Archive の判断基準を揃えるための参考です。

## Example 1: Repository Quality Audit -> Promote

### Innovation Summary

Repository Quality Audit は、UTF-8、mojibake、AI Repository Index、GDS Health、
broken links、README、history、project profile、Markdown structure を横断確認する
repository-wide quality check です。

### Validation Results

- `scripts/repository_quality_audit.py` で Green / Yellow / Red を出力できた。
- `reports/repository_quality_report.md` を自動生成できた。
- repeated completion reports の validation drift を減らした。

### Promotion Criteria

| Criteria | Result | Evidence / Notes |
|---|---|---|
| 複数 project で再利用可能 | PASS | future Ghost project docs に適用可能 |
| Rule / Workflow / Template / Architecture のいずれかへ分類できる | PASS | Workflow / generated report |
| 長期保守可能 | PASS | script と report の責務が明確 |
| Platform 価値がある | PASS | repository health を 1 command で説明できる |
| Human Approval Gate を通せる | PASS | report を人間が review できる |
| project-specific runtime responsibility を侵食しない | PASS | docs repository quality に限定 |
| evidence、limitation、rollback / archive 方針がある | PASS | report と history に残る |

### Architecture Impact

- Platform quality boundary を補強する。
- runtime architecture は変更しない。

### Repository Impact

- GDS Docs repository に script / report / workflow を追加。
- GameGhost は reference only。

### Health Impact

- GDS Health と Repository Quality を接続する。
- Health status の根拠を補強する。

### Documentation Impact

- workflow、README、completion report template、history を更新する。

### Human Review

- Review result: Approved.
- Reason: validation が repeatable で、Platform-wide docs quality に有効。

### Final Decision

Promote.

### Lessons Learned

- repeated manual validation は platform check に昇格できる。
- generated report は人間が読める日本語出力にする必要がある。

### Recommended Next Q

`Q_GDS_Repository_Quality_CI_Gate_JP.md`

## Example 2: Health Dashboard -> Promote

### Innovation Summary

GDS Health Dashboard は、Repository Health、Knowledge Health、Rule Coverage、
Workflow Coverage、Template Coverage、Example Coverage、Automation Coverage、
CI Status、Project Profile Coverage を見える化する dashboard です。

### Validation Results

- `docs/health/gds_health_dashboard.md` で GDS の運用状態を一覧化できた。
- `scripts/validate_gds_health.py` で structure を検証できた。
- Daily Operation と Completion Report から Health 更新要否を確認できる。

### Promotion Criteria

| Criteria | Result | Evidence / Notes |
|---|---|---|
| 複数 project で再利用可能 | PASS | future project profile health に展開可能 |
| Rule / Workflow / Template / Architecture のいずれかへ分類できる | PASS | Workflow / dashboard / validation |
| 長期保守可能 | PASS | update workflow と validation script がある |
| Platform 価値がある | PASS | blind spots を見える化する |
| Human Approval Gate を通せる | PASS | status は人間 review 前提 |
| project-specific runtime responsibility を侵食しない | PASS | GDS operating health に限定 |
| evidence、limitation、rollback / archive 方針がある | PASS | status notes と validation output |

### Architecture Impact

- Platform operating state の observation layer として扱う。
- Health は release approval の代替ではない。

### Repository Impact

- `docs/health/` と validation script を維持する。
- project runtime には影響しない。

### Health Impact

- Health 自身が Health update workflow の対象になる。

### Documentation Impact

- README、docs index、workflow、completion checklist へ導線が必要。

### Human Review

- Review result: Approved.
- Reason: responsibility boundary が明確で、継続改善に役立つ。

### Final Decision

Promote.

### Lessons Learned

- dashboard は判断を自動化しない。人間が状態を理解するための入口にする。

### Recommended Next Q

`Q_GDS_Health_Dashboard_Project_Profile_Extension_JP.md`

## Example 3: Ghost OCR Prototype -> Revise

### Innovation Summary

GameGhost の OCR review artifact、crop evidence、golden sample、metrics を
Platform-wide visual review standard として昇格できるか検討する prototype。

### Validation Results

- GameGhost Steam OCR では crop、overlay、human review が有効だった。
- ただし OCR domain に強く依存しており、AnimeGhost / ComicGhost で同じ形が
  使えるか未検証。

### Promotion Criteria

| Criteria | Result | Evidence / Notes |
|---|---|---|
| 複数 project で再利用可能 | PARTIAL | visual review は再利用可能だが OCR 固有部分が多い |
| Rule / Workflow / Template / Architecture のいずれかへ分類できる | PASS | Debug Artifact Review / visual evidence pattern |
| 長期保守可能 | UNKNOWN | sample 管理と artifact storage の負荷が未評価 |
| Platform 価値がある | PASS | visual evidence review は価値がある |
| Human Approval Gate を通せる | PASS | review artifact がある |
| project-specific runtime responsibility を侵食しない | PARTIAL | OCR implementation に踏み込みすぎる危険がある |
| evidence、limitation、rollback / archive 方針がある | PARTIAL | limitation はあるが cross-project evidence 不足 |

### Architecture Impact

- visual evidence boundary の候補。
- Ghost SDK 実装へ進めるには早い。

### Repository Impact

- GameGhost artifact structure を GDS にコピーしない。
- GDS 側には review pattern と decision report のみ残す。

### Health Impact

- current Health impact はなし。
- future Example Coverage / Workflow Coverage に影響する可能性あり。

### Documentation Impact

- Debug Artifact Review examples の補強候補。
- Innovation Pipeline record を追加する余地あり。

### Human Review

- Review result: Needs revision.
- Reason: cross-project validation が不足している。

### Final Decision

Revise.

### Lessons Learned

- field project で有効でも、Platform Standard には cross-project evidence が必要。
- implementation ではなく review pattern として切り出すと昇格しやすい。

### Recommended Next Q

`Q_GDS_Visual_Evidence_Review_Cross_Project_Validation_JP.md`

## Example 4: Experimental Tool -> Archive

### Innovation Summary

Health warning を検出したら、AI が自動で Q を作成し、Codex 実行まで進める
experimental tool idea。

### Validation Results

- Health warning から Draft Q candidate を作る価値はある。
- しかし Human Approval を省略して Codex execution まで進む設計は GDS ルールに反する。
- scope drift と unwanted edits の risk が高い。

### Promotion Criteria

| Criteria | Result | Evidence / Notes |
|---|---|---|
| 複数 project で再利用可能 | PARTIAL | Draft Q idea は再利用可能 |
| Rule / Workflow / Template / Architecture のいずれかへ分類できる | PARTIAL | Automation Server candidate |
| 長期保守可能 | FAIL | false positive / approval bypass risk が高い |
| Platform 価値がある | PARTIAL | issue detection は価値あり |
| Human Approval Gate を通せる | FAIL | original idea は approval bypass |
| project-specific runtime responsibility を侵食しない | UNKNOWN | execution automation が危険 |
| evidence、limitation、rollback / archive 方針がある | PASS | limitation は明確 |

### Architecture Impact

- Human Approval Gate を破るため、そのままでは不可。
- Draft Q Generator だけなら future candidate として分離可能。

### Repository Impact

- 自動編集や自動実行を含む場合、repository safety risk が高い。

### Health Impact

- Health warning の検出には価値がある。
- Health から execution まで直結してはいけない。

### Documentation Impact

- Automation Server candidate の cautionary example として保存できる。

### Human Review

- Review result: Rejected for promotion.
- Reason: Human Approval Required に反する。

### Final Decision

Archive.

Note:

- Draft Q Generator concept は Future Candidate として切り出してよい。
- automatic Codex execution は archive する。

### Lessons Learned

- automation の便利さより Human Approval が優先。
- Archive は失敗ではなく、危険な形を再利用しないための knowledge である。

### Recommended Next Q

`Q_GDS_Draft_Q_Generator_Human_Approval_Boundary_JP.md`

## Good Decision Shape

```text
Validation evidence
  -> Criteria checklist
  -> Impact review
  -> Human Review
  -> Promote / Revise / Reject / Archive
  -> Recommended Next Q
```

## Bad Decision Shape

```text
Looks useful
  -> Promote
  -> Implement everywhere
```

Why bad:

- validation がない。
- impact review がない。
- Human Approval がない。
- project-specific 成功を Platform Standard と誤認する。

## Related Documents

- `templates/platform_promotion_decision_report_template.md`
- `docs/workflow/innovation_pipeline_workflow.md`
- `templates/innovation_pipeline_template.md`
- `examples/innovation_pipeline_examples.md`
