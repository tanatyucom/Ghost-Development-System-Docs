# AI Repository Index Freshness Gate

## Purpose

Prevent a structurally valid but stale `docs/ai_repository_index.md` from
passing completion or CI validation.

## Meanings

- Structurally valid: the current inventory and targets satisfy the Canonical
  validator.
- Deterministic: identical repository state produces byte-identical output.
- Fresh: the tracked generated file exactly matches Canonical regeneration.

These meanings are independent. Structural validity does not prove freshness,
and deterministic generation does not prove that generation ran before commit.

## Canonical local sequence

Run from the repository root:

```powershell
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/validate_encoding_regression.py --all
git diff --check
git diff --exit-code -- docs/ai_repository_index.md
```

The final command is the freshness check. During authorized documentation work,
a regenerated Index diff must be reviewed and included in the Safe Commit Set;
after that commit, rerunning the sequence must produce no Index diff.

## Applicability

The gate is mandatory when a Safe Commit Set contains Indexable Markdown,
generator or parser code, routing/category configuration, Index documentation,
or CI that affects Index generation. Otherwise record `NOT_APPLICABLE` and the
reason; never silently omit the decision.

## Failure

`AI_REPOSITORY_INDEX_STALE` means Canonical regeneration changed the generated
file. CI must fail closed and must not commit it automatically.

Remediation:

1. Run Canonical generation.
2. Review `docs/ai_repository_index.md`.
3. Run structural and Encoding Regression validation.
4. Regenerate again and confirm byte-identical output.
5. Include the generated file in the Safe Commit Set.

Structural errors, nondeterministic output, freshness differences, and encoding
regressions are separate failure classes and must be reported separately.
