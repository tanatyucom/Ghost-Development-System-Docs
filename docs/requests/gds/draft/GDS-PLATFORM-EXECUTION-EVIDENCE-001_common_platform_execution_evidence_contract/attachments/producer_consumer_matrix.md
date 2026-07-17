# Producer / Consumer Matrix

| Capability | Produces | Consumes | Must Not Do |
| --- | --- | --- | --- |
| Intent Engine | Interpreted intent, selected workflow, Pending Action evidence | Repository state, canonical source, Human Approval state | Execute action or approve on behalf of human |
| Startup Enforcement | Gate evidence before managed artifact generation | Intent, workflow, knowledge, repository, template, constraints | Generate artifact body or mutate repository |
| Repository Quality | Quality status, warnings, errors, report path | Repository files, validators, AI Repository Index | Treat Green as approval for execution |
| Command Center | Orchestration evidence, recommendation, display summary | Intent, Startup, Quality, Completion, Knowledge evidence | Own domain truth or replace Human Approval |
| Completion Review | Validation evidence, Safe Commit Set, remaining issues, next Q | Changed files, quality report, task results | Promote knowledge or commit automatically |
| Knowledge Promotion | Candidate classification, duplicate check, promotion recommendation | Completion Review, user decisions, canonical sources | Canonicalize without Human Approval |
| Template Engine | Draft artifact from canonical template and approved evidence | Template, evidence record, user-approved scope | Treat template completion as approval |

## Matrix Conclusion

The common contract is needed because Command Center and Completion Review must
consume evidence from multiple producers without each producer inventing a
separate incompatible structure.
