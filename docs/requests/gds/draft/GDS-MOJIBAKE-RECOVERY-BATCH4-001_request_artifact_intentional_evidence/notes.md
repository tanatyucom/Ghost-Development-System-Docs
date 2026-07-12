# Notes - GDS-MOJIBAKE-RECOVERY-BATCH4-001

## Source Q

- `C:\Users\tanat\Downloads\Q_GDS_Legacy_Document_Mojibake_Recovery_Batch4_Request_Artifacts_JP.md`

## Target Warning

- File: `docs/requests/gds/draft/GDS-MOJIBAKE-AUDIT-001_legacy_document_mojibake_audit_and_repair/request.md`
- Line: 127
- Detected text: `- Unicode replacement character: U+FFFD`

## Investigation Result

- Root cause classification: intentional evidence / detection sample.
- The line appears under `Required Detection Targets`.
- The source Q in Downloads contains the same line.
- Related completion report states that mojibake evidence artifacts intentionally contain mojibake source text.
- This is not unrecoverable text corruption.

## Repair Decision

- The historical request artifact body was not rewritten.
- `scripts/repository_quality_audit.py` was updated with a narrow file-level intentional evidence exclusion for the source request artifact.
- `reports/repository_quality_report.md` was also excluded from Mojibake scanning to prevent generated self-reference noise.

## Counts

- Target request replacement character count before: 1
- Target request replacement character count after: 1
- Repository Quality Mojibake warnings after audit exception: 0
