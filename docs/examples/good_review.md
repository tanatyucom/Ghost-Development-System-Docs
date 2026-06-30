# Good Review Example

## Review Target

`docs/roadmap/roadmap.md`

## Repository Information Check

- Repository: Ghost-Development-System-Docs.
- Working Directory: `C:\GitHub\Ghost-Development-System-Docs`.
- Documentation Root: `C:\GitHub\Ghost-Development-System-Docs\docs`.
- Runtime Root: Not in scope.
- Related Repository: GameGhost is reference only.
- Scope Guard: Only public knowledge base documents may be edited.

Result: PASS.

## Review Perspective

- Public knowledge base clarity.
- Long-term maintainability.
- Purpose-oriented naming.
- Responsibility boundaries.
- Future Candidate separation.
- AI collaboration quality.

## Findings

### Finding 1: Public title should describe purpose before implementation

Severity: Medium.

The roadmap item title uses a specific implementation method even though the
actual goal is broader.

Current:

```text
Nintendo 3DS Activity Log Parser
```

Recommended:

```text
Legacy Play History Recovery
```

Reason:

The broader name covers Nintendo 3DS, Switch OCR, FF11 / FF14, Steam / PSN /
Console CSV, and manual recovery without locking the roadmap to one parser.

## Suggested Improvements

- Add a naming note explaining why the public title is purpose-oriented.
- Keep implementation details under Current Targets / Current Implementations.
- Add the naming principle to templates so future Q files use the same rule.

## Verification

- Checked roadmap item title.
- Checked whether legacy implementation details remain represented.
- Checked whether the new name supports future recovery methods.

## Remaining Issues

- Consider adding a dedicated naming guide under `docs/examples/`.

## Future Candidates

- Public Glossary.
- Authority Matrix.
- ADR example.
- Documentation Health Check.

## Recommended Next Q

```text
Purpose-Oriented Naming Examples - Roadmap Item Naming Guide
```
