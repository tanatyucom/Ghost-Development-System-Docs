# Working Context Model Review

## Verdict

PASS WITH RECOMMENDATIONS.

Working Context should be adopted as a generated operational view for Command
Center, not as a persistent project asset or second source of truth.

## Architecture Proposal

Working Context is the bridge between repository evidence and Command Center's
AI Project Manager surface.

```text
Repository
  -> Repository Context Evidence
  -> Working Context
  -> Command Center
  -> Human Approval
  -> Approved action / handoff / review
```

The model gives the human and AI a shared current operating picture without
moving authority away from repository documents, evidence artifacts, or Human
Approval.

## Responsibility Boundaries

| Area | Responsibility |
| --- | --- |
| Repository | Canonical source of documents, reports, requests, templates, rules, roadmap, and history. |
| Repository Context Evidence | Proof of what was checked and when. |
| Working Context | Generated summary of the current operating picture. |
| Command Center | Displays Working Context, routes recommendations, and supports handoff. |
| Human Approval | Decides scope, priority, approval, rejection, and risk acceptance. |
| Codex / Execution Adapter | Executes only approved scoped work and produces evidence. |

## Recommended Contents

Working Context should include:

- Current Priority.
- Current Focus.
- Current Mission.
- Active Q.
- Repository Health.
- Approval Status.
- Completion Review Status.
- Deferred Items.
- Blocking Issues.
- Recommended Next Action.

Each item should link to the canonical source or evidence path that supports it.

## Refresh Model

Refresh should be triggered by:

- Startup completed.
- Repository Context Evidence changed.
- relevant repository change.
- Repository Quality or AI Repository Index state changed.
- Completion Review completed.
- Approval state changed.
- Current Mission changed.
- Active Q changed.
- blocker or SCW state changed.

If evidence is incomplete, the context should be labeled partial or stale.

## Lifecycle Proposal

```text
Not Generated
  -> Generated
  -> Presented
  -> Reviewed
  -> Used For Recommendation
  -> Refreshed / Superseded
  -> Discarded or Archived As Evidence
```

Default lifecycle should be temporary. Storage is allowed only for audit,
handoff, approval packet, or completion review needs.

## Review Question Answers

Should Working Context always be generated?

- No. Generate it when Command Center, Startup, handoff, approval, or
  completion review needs a current operating view.

Should it ever be stored?

- Yes, but only as evidence or handoff support. Stored Working Context is not
  canonical project state.

Should it only exist temporarily?

- Usually yes. Persistent snapshots should be exceptional and explicitly
  labeled.

What belongs in Working Context versus Repository Context Evidence?

- Working Context contains interpreted current-state summary.
- Repository Context Evidence contains source checks, paths, freshness, and
  validation facts.

What should never appear in Working Context?

- Hidden approval, secrets, unverifiable memory claims, unauthorized scope,
  stale facts without freshness status, or execution commands.

## Roadmap Recommendation

Add Working Context to the Command Center roadmap as:

- Architecture Candidate.
- Phase 1 manual / generated operational view.
- Future package format candidate.
- Future Repository Intelligence and Dashboard integration input.

Do not approve runtime generation, storage automation, scoring, UI, or adapter
orchestration in this Q.

## Promotion Readiness

| Item | Readiness | Notes |
| --- | --- | --- |
| Architecture term | Ready | Working Context is clearly distinct from evidence and repository truth. |
| Responsibility boundary | Ready | Human Approval and repository source-of-truth remain intact. |
| Roadmap clarification | Ready | Useful for Command Center Foundation. |
| Persistent artifact format | Future Candidate | Needs separate template / schema Q. |
| Runtime generation | Not ready | Requires implementation Q and freshness validation. |
| Priority scoring | Not ready | Must remain advisory and approval-gated. |
| UI / Dashboard | Not ready | Future Command Center work. |

## Final Assessment

Working Context should be adopted as a Command Center architecture concept. It
should remain generated, refreshable, evidence-backed, and non-canonical.
