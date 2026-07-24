# Follow-up to Canonical Draft Q Workflow

**Version:** 1.0

## Completion-side Flow

```text
Opportunity Found
  -> Create Observed Candidate
  -> Add Mandatory Contract Fields
  -> Link Source Q / Completion / Handover
  -> Validate Repository Assignment and Missing Inputs
  -> Enriched Candidate
```

## Next-Q Flow

```text
Enriched Candidate
  -> Verify source freshness
  -> Inherit context with provenance
  -> Inspect current repository state read-only
  -> Ask only unresolved human-dependent questions
  -> Generate Canonical Draft Q
  -> Template Validation
  -> Human Approval
  -> Approved Q
```

The workflow never converts a candidate directly into execution authority.
Source conflicts and invalidated context are surfaced in Missing Inputs. If a
required value remains unknown, the draft remains non-executable.
