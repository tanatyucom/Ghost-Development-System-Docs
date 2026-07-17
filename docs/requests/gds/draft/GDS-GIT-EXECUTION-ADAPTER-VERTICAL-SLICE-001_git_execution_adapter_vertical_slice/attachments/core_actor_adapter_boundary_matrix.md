# Core / Actor / Adapter Boundary Matrix

| Responsibility | GDS Core | AI Actor | Git Adapter |
| --- | --- | --- | --- |
| Human approval state | Owns | Explains / records | Does not own |
| Intent resolution | Owns | Interprets / proposes | Does not own |
| Queue state | Owns | Displays / updates from evidence | Does not own |
| Capability selection | Owns | Suggests | Advertises capabilities |
| Git command translation | Does not own | Delegates | Owns |
| Git execution evidence | Reconciles | Summarizes | Produces |
| Completion judgment | Owns | Reports | Does not own |
| Credential handling | Policy only | Does not own | Future target-specific concern |
| Vendor-specific behavior | Must not depend on | May vary | Must remain contract-compatible |

## Boundary Statement

AI can be replaced without changing GDS Core semantics. Git adapter
implementation can be replaced without changing Approval, Intent, Queue, or
Evidence contracts.
