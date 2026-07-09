# Evidence Feedback Loop Example

## Purpose

This example shows how to turn implementation results into metrics, reviewed
evidence, and the next Ghost Development System improvement.

## Principle

Evidence First becomes stronger when evidence can be measured.

Metrics should answer:

```text
What changed in real operation?
```

They should not answer:

```text
Can we skip review or human approval?
```

## Good Flow

```text
Implementation
  -> Review
  -> Metrics
  -> Knowledge
  -> Rule
  -> Next Improvement
```

## Example: OCR Improvement

Context:

GameGhost OCR results improved after Alias Review, Safe Alias, Unicode
Normalizer, Golden Samples, Review GUI, and Human Approval were introduced.

Useful metrics:

| Metric | Example Use |
|---|---|
| Success Rate | Compare successful OCR/import results before and after approved aliases. |
| Review Rate | Check whether fewer OCR results require manual review. |
| Alias Improvement | Count failures resolved by approved aliases. |
| Unicode Improvement | Count mismatches resolved by Unicode normalization. |
| Golden Sample Accuracy | Compare expected titles against OCR output for stable samples. |

Good evidence statement:

```text
Alias Review reduced repeated OCR ambiguity for the measured sample.
The source sample, review period, and remaining manual review cases are listed.
```

Weak evidence statement:

```text
OCR feels better now.
```

## Example: Development Workflow

Useful metrics:

| Metric | Example Use |
|---|---|
| Q Completion Time | Measure whether the workflow helps finish Q files faster or more predictably. |
| Review Iterations | Count how many review/fix cycles were needed before completion. |
| Duplicate Prevention | Count avoided duplicate docs or duplicate roadmap ideas. |
| Documentation Reuse | Count reused rules, templates, examples, or architecture notes. |
| Knowledge Promotion Count | Count promoted rules, workflow notes, examples, templates, or Knowledge Assets. |

## Example: Workflow Operation

Useful metrics:

| Metric | Example Use |
|---|---|
| Reused Knowledge Assets | Count existing Knowledge Assets used in the task. |
| New Knowledge Assets | Count new asset candidates created by the task. |
| Human Review Time | Record time spent on review or approval when available. |
| Automation Rate | Estimate how much work automation handled compared with manual review. |

## Review Checklist

- Is the metric source clear?
- Is the sample or period clear?
- Is the interpretation separated from the raw number?
- Are unmeasured items listed?
- Does the evidence support a recommended improvement?
- Does the recommendation still respect Human Approval Gate?
- Should the result become a rule, workflow update, roadmap item, template, or
  Knowledge Asset?

## Good Output Shape

```text
Metrics / Evidence

- Metrics checked: Review Iterations, Documentation Reuse.
- Evidence source: Q completion report and changed docs.
- Interpretation: Existing templates prevented duplicate structure work.
- Not measured: Human Review Time.

Improvement Review

- Recommended: Add Metrics / Evidence to completion report template.
- Future Candidate: Evidence Dashboard.
```
