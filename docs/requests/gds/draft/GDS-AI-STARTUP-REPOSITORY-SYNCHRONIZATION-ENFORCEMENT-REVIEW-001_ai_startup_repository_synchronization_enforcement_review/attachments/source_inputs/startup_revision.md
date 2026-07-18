# Startup Revision Proposal (Final)

## Purpose

Synchronize the AI with the canonical GDS knowledge before planning,
creating, reviewing, or implementing work.

Startup answers:

**"What is the canonical knowledge?"**

---

# Single Source of Truth

The public Ghost Development System repository is the Single Source of Truth
for all canonical development knowledge.

Always synchronize with the canonical GDS repository before beginning development.

---

# Knowledge Ownership Rule

The following artifacts MUST be treated as GDS-owned canonical knowledge:

- Rules
- Local Rules
- Shared Rules
- Core Rules
- Templates
- Workflows
- ADRs
- Roadmaps
- Current Mission
- Startup
- AI Repository Index
- Standards
- Architecture Principles
- Platform Governance

Ghost repositories may contain copies, snapshots, or project-local references,
but they MUST NOT be treated as the canonical source.

If any conflict exists:

STOP

Resolve the canonical source before continuing (SCW).

---

# Q Creation Gate

When creating, revising, or reviewing any Q artifact:

1. Execute the Startup Procedure.
2. Confirm the public Ghost Development System repository.
3. Synchronize AI Repository Index.
4. Review the latest Startup document.
5. Review the latest canonical Q_TEMPLATE.md.
6. Review all related canonical:
   - Rules
   - Workflows
   - ADRs
   - Roadmaps
   - Standards
   - Current Mission
7. Prefer Revision over creating competing artifacts.
8. Continue to Constraint Check.
9. Do not begin implementation until the Constraint Check has completed successfully.

If the canonical artifact cannot be located,
or multiple conflicting artifacts exist:

STOP

Resolve the canonical source before continuing.

---

# Constraint Check Responsibility

Constraint Check verifies whether execution is currently safe.

Constraint Check answers:

**"May this work proceed now?"**

The Startup Procedure must always preserve:

- Memory Update availability
- Repository boundary
- Human Approval boundary
- Commit approval
- Push approval
- Output restrictions

Memory availability MUST be checked before development begins.
