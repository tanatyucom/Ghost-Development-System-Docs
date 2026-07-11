# Steam OCR Existing Debug Rule Update Mapping

## Purpose

Steam OCR Knowledge Promotion Candidate Reviewで `Update` / `Merge` と判断されたDebug関連の知見を、どの既存Ruleへ統合したかを記録します。

本ReportはRule更新の対応表であり、新規Rule追加ではありません。

## Mapping

| Candidate ID | Source Knowledge | Target Existing Rule | Decision | Added Wording Summary | Rejected OCR-Specific Detail | Remaining Risk |
|---|---|---|---|---|---|---|
| R-00001 | MetricsとHuman Observationの衝突 | `docs/rules/debug_artifact_review_rules.md`, `docs/rules/debug_escalation_ladder_rules.md`, `docs/rules/core_principles.md` | Update | 衝突時は採用を停止し、Pipeline Trace / Expected State / First Broken Step / 再検証へ進むGateを追加。 | Steam OCR固有のcrop幅、score値。 | Human Observationを絶対視しない運用確認が必要。 |
| R-00002 | Trace Before Tune | `docs/rules/debug_escalation_ladder_rules.md`, `docs/workflow/first_broken_step_methodology.md` | Merge | Tuning前にPipeline Traceを確認する原則を強化。 | OCR固有Pipeline名。 | 既存文書との重複を増やしすぎないこと。 |
| R-00003 | First Broken Step Identification | `docs/rules/debug_escalation_ladder_rules.md`, `docs/workflow/first_broken_step_methodology.md` | Merge | Root cause決定前にFirst Broken Stepを確認する位置づけを維持・強化。 | Steam OCRの具体工程名。 | 実運用でCompletion Reportに明記されるか。 |
| R-00004 | Do Not Optimize From Single Samples | `docs/rules/quality_rules.md` | Update | Representative Sample Ruleを追加。 | Steam OCR sample数、画像ID。 | 代表サンプル定義はタスクごとに必要。 |
| R-00005 | Candidate Generation Before Scoring | `docs/rules/debug_artifact_review_rules.md`, `docs/workflow/first_broken_step_methodology.md` | Partial Update | candidate generationとscoring / recognitionを分離し、正しい候補が存在するかを先に確認する文言を追加。 | `glyph_band_safe_padding`, `icon_gap0_r48`。 | 汎用Methodology化は別Qで検討。 |
| R-00006 | Review Intermediate Artifacts Before Conclusion | `docs/rules/debug_artifact_review_rules.md` | Merge | Intermediate Artifact Acceptance Ruleを追加。 | Steam OCR contact sheet固有構造。 | artifact種類が増えた時の入口整理。 |
| R-00007 | Negative Results Are Knowledge Assets | `docs/rules/debug_escalation_ladder_rules.md`, `docs/rules/audit_before_repair_rules.md`, `docs/rules/core_principles.md`, `docs/rules/quality_rules.md` | Update | Useful Negative ResultをCompletion Report / CASE / PIP / Knowledge Inventoryへ保存する方針を追加。 | OCR固有の失敗候補名。 | 何でも保存するとノイズになるため、有用なものに限定する。 |
| R-00008 | Separate Detection Failure From Recognition Failure | `docs/rules/debug_escalation_ladder_rules.md`, `docs/rules/audit_before_repair_rules.md`, `docs/workflow/first_broken_step_methodology.md` | Update | detection, candidate generation, recognition, scoring, selection, rendering failureを分離する文言を追加。 | OCR engine thresholdやgeometry。 | 各プロジェクトで用語変換が必要。 |
| R-00009 | Human Approval Before Standard Promotion | `docs/rules/core_principles.md` | Merge | Human Approval Gateは既存維持。Metrics衝突時も採用停止と調査へ接続。 | なし。 | Human Approval Artifactの標準化は別Q。 |
| R-00010 | Representative Dataset First | `docs/rules/quality_rules.md` | Update / Merge | Representative Sample Ruleへ統合。 | Steam OCR golden sampleの具体条件数。 | Dataset / sample 用語は今後整理余地あり。 |
| IR-00006 | Repository Context Verification Before Git Commands | `docs/rules/repository_root_validation_rules.md`, `docs/rules/git_rules.md` | Update | `git rev-parse --show-toplevel`, branch, remote, status確認をGit操作前Safetyへ統合。 | 個別Qのパス。 | Remote確認が不要なlocal-only作業とのバランス。 |

## Why No New Rule Was Needed

今回の知見は、既存の以下Rule群に自然に統合できました。

- Debug Artifact Review Rules
- Debug Escalation Ladder Rules
- Audit Before Repair Rules
- Quality Rules
- Repository Root Validation Rules
- Git Rules
- Core Principles
- First Broken Step Methodology

新規Ruleを作ると、Trace Before Tune、Debug Artifact Review、Human Approval Gate、Quality Rulesの責務が重複するため、既存RuleのUpdate / Mergeを優先しました。

## Excluded OCR-Specific Details

GDS共通Ruleへ入れなかったもの:

- pixel offset
- crop width
- `glyph_band_safe_padding`
- `icon_gap0_r48`
- Steam固有UI geometry
- OCR engine threshold
- row boundary個別score

これらはCASE、PIP、Improvement Record、またはGameGhost側の技術記録で扱うべき内容です。
