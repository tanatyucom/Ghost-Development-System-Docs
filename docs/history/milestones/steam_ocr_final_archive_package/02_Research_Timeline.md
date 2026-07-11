# 02 Research Timeline

## Phase -1

1行ずつOCRしていると思っていたが、実際には全体スクリーンショットへ複数Profileを当てていた。

## Phase 0

OCR Engine、OCR辞書、Crop sizeが初期仮説だった。

## Phase 1

Title Start Offset。`-20px`で一部改善したが根本解決ではなかった。

## Phase 2

Title Cell OCR。Production ReadyではなくDebug Onlyだった。

## Phase 3

Contact Sheetを人間が見て、2行混在への違和感が生まれた。

## Phase 4

Geometry ReviewでPrevious Row Overlapを確認した。

## Phase 5

Down4などの比較で改善は見えたが、人間は採用しなかった。

## Phase 6

Row Center / Pitchへ移ったが、Metricsだけでは足りなかった。

## Phase 7

AIはsingle_row_ok、人間は2行混在を確認した。

## Phase 8

Adaptive Crop。Band 75は数値上良かったが、空cropや文字欠けが残った。

## Phase 9

Root Cause Investigationへ転換した。

## Phase 10

Target Row TracingでPipelineを追跡した。

## Phase 11

Tight Title BBox Traceは`bbox_good = 0`。Negative Resultとして保存した。

## Phase 12

Scoring prototypeを作ったが、目視とずれた。

## Phase 13

Human Review GUIで確認作業を継続可能にした。

## Phase 14

PASSは2行、FAILは3行、正常1行なし。Scoring ProblemではなくCandidate Generation Problemだと分かった。

## Phase 15

Candidate Generation Reworkで92 / 92 single-rowへ到達した。

## Phase 16

Horizontal Boundsへ問題が移った。左欠けは解消し、右欠けは残った。

## Phase 17

Knowledge Inventory、Promotion Review、Existing Rule Update、CASE-0008へ昇格した。
