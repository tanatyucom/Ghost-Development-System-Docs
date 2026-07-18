# Q_GDS_MEMORY_CANDIDATE_GOVERNANCE_INTEGRATION_00003

# Title

Memory Candidate (MC) Governance Integration

---

# Background

MC Framework v1.0 has completed two independent reviews.

Final Result:

PASS / GO

MC is approved for adoption into GDS Governance.

This Q integrates MC into the GDS governance model.

---

# Objectives

Integrate Memory Candidate into GDS by:

- Adding Governance Rules
- Creating the standard MC template
- Updating End-of-Session Review
- Defining Repository integration
- Registering MC Retrospective as a Future Candidate

---

# Governance Rules

Memory Candidate (MC) is the official GDS Knowledge Inbox mechanism.

MC captures valuable conversation-born knowledge before promotion to:

- Memory
- Q
- Repository Knowledge

MC is NOT Canonical Knowledge.

Repository remains the Single Source of Truth.

MC must never be used directly as implementation authority.

Automatic promotion is prohibited.

Every MC must end in one of:

- Repository Registered
- Closed
- Rejected
- Duplicate
- Deferred
- Expired

Deferred items require periodic Deferred Review.

---

# Standard Lifecycle

Conversation
↓
Captured
↓
Triaged
├─ Memory Saved
├─ Q Created
├─ Repository Drafted
├─ Rejected
├─ Duplicate
├─ Deferred
└─ Expired
↓
Repository Registered
↓
Closed

---

# Standard Template

Required fields:

- MC ID
- Title
- Origin
- Captured Date
- Owner
- Review By
- Priority
- Status
- Decision
- Promotion Target
- Target Repository
- Related Q
- Related ADR
- Related Rule / Workflow
- Evidence Level
- Closure Reason

Numbering:

MC-00001
MC-00002
...

---

# End-of-Session Review

Add:

- Repository Registered
- Q Created
- Memory Saved
- Memory Save Failed
- Memory Candidates Captured
- Codex Pending
- Repository Pending
- Rejected
- Duplicate
- Deferred
- Lost Context Risk

If Lost Context Risk = YES

→ Create MC before ending the session.

---

# Repository Integration

MC is a governance mechanism.

Repository remains the canonical destination.

MC itself is temporary and must eventually be resolved.

---

# Future Candidate

MC Retrospective

Purpose:

Review historical conversations and recover valuable conversation-born knowledge as Memory Candidates.

This is intentionally managed as a separate future project.

---

# Expected Deliverables

- Governance Rule
- MC Template
- End-of-Session Review update
- Documentation update
- AI Repository Index update
