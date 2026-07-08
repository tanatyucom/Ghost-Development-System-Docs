# PIP Case Index

## Purpose

この文書は、PIP に保存する改善事例の index です。

PIP case は、単発の作業記録ではありません。再利用できる失敗パターン、調査手順、
review method、再発防止知識を短く参照できるようにするための entry です。

## Source Evidence

- `PIP_v1.0_stable.zip`
- `GDS_PIP_v1.1_delta_package_20260708.zip`

## Steam OCR v2 Debugging Sequence

### Metrics Said Single Row, Human Saw Two Rows

Summary:

Automated geometry metrics reported a single-row condition, but human visual
review found two-row mixing.

Reusable Lesson:

Metrics can pass while visual containment fails. Visual containment must be
reviewed with contact sheets or overlays when row boundaries matter.

Related Methodology:

- Human Visual Review。
- Evaluate What Actually Matters。
- Review Entry Point。

### Root Cause Was The Algorithm

Summary:

OCR failure was traced back to row boundary algorithm assumptions rather than
only OCR recognition quality.

Reusable Lesson:

When downstream output is wrong, trace the pipeline before tuning parameters.

Related Methodology:

- Trace Before Tune。
- First Broken Step。
- Target Row Trace / Pipeline Trace。

### Good Crop Score But Text Was Missing

Summary:

Crop quality scoring selected a candidate that could still miss the actual
title text.

Reusable Lesson:

A metric must evaluate the real quality target, not a proxy that accidentally
passes.

Related Methodology:

- Evaluate What Actually Matters。
- Human Visual Review。
- Review Entry Point。

### Target Row Identity Drift

Summary:

The target row identity drifted before crop, bbox, or OCR. Downstream steps
then worked on a confused target.

Reusable Lesson:

Target row identity must be traced before judging crop, bbox, or OCR quality.

Related Methodology:

- First Broken Step。
- Target Row Trace / Pipeline Trace。
- Trace Before Tune。

### First Broken Step Was Title BBox

Summary:

Target Row Tracing identified rows where the first broken step was Title Text
BBox, plus rows where Target Row Identity broke first.

Reusable Lesson:

Title bbox and target row identity should be separated in review. Fixing OCR
or crop scoring first can hide the actual break point.

Related Methodology:

- First Broken Step。
- Trace Before Tune。
- Review Entry Point。

## Future Use

Future PIP template work should include a Case Index section and a standard
case entry format.
