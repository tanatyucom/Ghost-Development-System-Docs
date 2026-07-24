# Architecture Decision Matrix

| Criterion | A: GDS Runtime package | B: Independent GDO | C: Monorepo apps |
|---|---|---|---|
| Responsibility clarity | Low | High | Medium |
| Fault isolation | Low | High | Medium |
| Security isolation | Low | High; separate Gateway later | Medium |
| Initial complexity | Low | Medium | Medium |
| Operational complexity | Medium hidden coupling | Medium explicit | Medium |
| Reuse | Medium | High | Medium |
| Release coupling | High | Low | High |
| Repository coupling | High | Low via contracts | High |
| Migration cost | High after growth | Medium at bootstrap | High extraction later |
| Verdict | Rejected | **Recommended** | Transitional only |

Option B is the only option that preserves the accepted Policy Provider/Consumer
boundary physically as well as logically. Its additional repository and contract
coordination cost is known and bounded. Option A creates privilege and recovery
coupling. Option C delays rather than removes that coupling.
