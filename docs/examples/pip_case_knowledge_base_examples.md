# PIP Case Knowledge Base Examples

## Good Example: Completion Report To PIP Case

Situation:

- Steam OCR review found that automated metrics passed.
- Human visual review found two-row mixing.
- Target row trace showed where the first broken step happened.

Good handling:

1. Save the source Q and completion report.
2. Link the review artifacts from the completion report.
3. Create a PIP Case under `pip/cases/`.
4. Use `pip/templates/case_template.md`.
5. Add tags:
   - Project: `Steam`
   - Category: `OCR`, `Review`
   - Methodology: `First Broken Step`, `Human Review`, `Pipeline Trace`
   - Priority: `P1`
   - Lifecycle: `Validated`
6. Update `pip/case_index.md`.
7. Promote repeated lessons to Rule Story or Best Practice when approved.

Why this is good:

- The original task remains traceable.
- Evidence stays in its artifact workspace.
- The reusable lesson becomes searchable.
- Future AI and humans can find the case by project, method, priority, or rule.

## Bad Example: Completion Report Only

Situation:

- A difficult OCR bug was investigated.
- The completion report includes the useful lesson.
- No PIP Case is created.
- No tags or index entry are added.

Bad result:

- Later work cannot find the lesson by `First Broken Step`.
- Similar bugs repeat the same investigation.
- Human reviewers must search chat history or old reports.
- The lesson never becomes a rule story, best practice, or workflow update.

## Good Example: Rule Story Candidate

Situation:

- Multiple cases show that tuning parameters before tracing the pipeline causes wasted work.

Good handling:

1. Link the related PIP Cases.
2. Create or update a Rule Story under `pip/rule_stories/`.
3. Connect it to `Trace Before Tune`.
4. If repeated enough, promote to official rule or workflow documentation through Human Approval Gate.

## Bad Example: Tag Drift

Bad tags:

```text
SteamOCR, OCRDebug, important, maybe-fixed, review-ish
```

Problem:

- Tags are not standardized.
- They cannot be reliably searched or filtered.
- AI may treat near-duplicates as different concepts.

Good tags:

```text
Project: Steam
Category: OCR, Debug, Review
Methodology: Trace Before Tune, First Broken Step
Priority: P1
Lifecycle: Validated
```
