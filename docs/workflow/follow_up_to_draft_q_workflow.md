# Follow-up to Canonical Draft Q Workflow

**Version:** 2.0

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

## Generation Steps

1. Admit only an Enriched candidate and identify source Q/completion.
2. Validate source freshness and field-level provenance.
3. Resolve Repository ID through the canonical Registry.
4. Apply field precedence and invalidate stale context.
5. Apply only safe unique corrections and record them.
6. Classify every missing input.
7. Map fields to Canonical Q sections and attach Generator Metadata.
8. Apply the non-executable Draft envelope.
9. Route to Draft Ready, Review Required, or Incomplete.

Current workspace/branch/remote/credential/runtime state is never inherited as
current truth; it is checked later by Startup.
