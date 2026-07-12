# Startup Checklist Workflow

## Purpose

Startup Checklist Workflow 縺ｯ縲∵眠縺励＞ AI 繧ｻ繝・す繝ｧ繝ｳ縲，odex 螳溯｡後・繝ｬ繝薙Η繝ｼ縲∵枚譖ｸ譖ｴ譁ｰ縲＿ 螳溯｣・ｒ髢句ｧ九☆繧句燕縺ｫ縲；DS 縺ｮ蜑肴署繧堤｢ｺ隱阪☆繧区ｨ呎ｺ悶ヵ繝ｭ繝ｼ縺ｧ縺吶・
逶ｮ逧・・縲∵眠縺励＞繝ｫ繝ｼ繝ｫ繧貞｢励ｄ縺吶％縺ｨ縺ｧ縺ｯ縺ｪ縺上∵里蟄倥・ Rules縲仝orkflow縲・Methodology縲ヽepository Information 繧帝幕蟋区凾縺ｫ遒ｺ螳溘↓諤昴＞蜃ｺ縺吶％縺ｨ縺ｧ縺吶・
## Standard Flow

```text
Start
  -> AI Startup Procedure
  -> AI Repository Index Check
  -> Daily Knowledge Source Review
  -> Information Package Check, when provided
  -> Current Q Check
  -> Repository Root Validation
  -> Repository Confirmation
  -> Target Project Profile Confirmation
  -> Q / Artifact Confirmation
  -> Q ID / Naming Confirmation
  -> Q Template Required Fields Confirmation
  -> Applicable Rules Confirmation
  -> Applicable Methodologies Confirmation
  -> Scope / Out of Scope Confirmation
  -> Conversation Insight Detection
  -> Knowledge Suggestion Assistant Check
  -> Research Task Detection
  -> Proactive Proposal Check
  -> Dirty Workspace / Commit Policy Confirmation
  -> Checklist Complete
  -> Normal Implementation / Review Start, when not research
  -> Research Mission, when research
```

## Step Details

### AI Startup Procedure

Startup Checklist 縺ｮ蜑阪↓縲、I 縺ｯ AI Startup Procedure 縺ｫ蠕薙＞縲・AI Repository Index縲！nformation Package when provided縲，urrent Q File縲・Repository Root Validation縲；DS Core Rules / Templates縲ゝarget Project
Profile 繧帝・↓遒ｺ隱阪＠縺ｾ縺吶・
Details follow `ai_startup_procedure.md`.

### Information Package Check

Information Package 縺梧署萓帙＆繧後※縺・ｋ蝣ｴ蜷医・縲＿縺ｨ蜷医ｏ縺帙※迴ｾ蝨ｨ迥ｶ諷九ｒ遒ｺ隱阪＠縺ｾ縺吶・
遒ｺ隱阪☆繧九％縺ｨ:

- Current Status.
- Current Focus.
- Active Repository.
- Recent Decisions.
- Open Issues.
- Recent Artifacts.
- Recommended Next Q.
- Research Task縺九←縺・°縲・
### AI Repository Index Check

蜈ｬ髢・GDS knowledge 繧剃ｽｿ縺・ｴ蜷医・ `docs/ai_repository_index.md` 繧帝幕蟋狗せ縺ｫ縺励∪縺吶・
遒ｺ隱阪☆繧九％縺ｨ:

- Index read.
- Required document found.
- Raw URL or local path usable.
- Index regeneration needed after this Q.

### Daily Knowledge Source Review

蟆代↑縺上→繧・譌･1蝗槭∽ｸｻ隕√↑Project菴懈･ｭ縺ｾ縺溘・驥崎ｦ√↑謠先｡医ｒ陦後≧蜑阪↓縲・Canonical Knowledge Source繧堤｢ｺ隱阪＠縺ｾ縺吶・
Canonical daily entry point:

```text
docs/ai_repository_index.md
```

Minimum targets:

- AI Repository Index縲・- Current Information Package縲・- Current Project Profile縲・- Current Roadmap縲・- Conversation Insights縲・- Future Candidates縲・- Research Missions縲・- Improvement Records縲・- Relevant CASE / Rule / Architecture / Workflow縲・
縺薙ｌ縺ｯ閾ｪ蜍慕ｷｨ髮・∬・蜍姫romotion縲∬・蜍媛逕滓・縲∬・蜍募ｮ溯｣・∬・蜍匹ommit縺ｮ讓ｩ髯舌ｒ
荳弱∴縺ｾ縺帙ｓ縲・
### Repository Root Validation

菴懈･ｭ髢句ｧ句燕縺ｫ縲∫樟蝨ｨ縺ｮ shell 縺梧ｭ｣縺励＞ Git repository root 縺ｫ縺・ｋ縺狗｢ｺ隱阪＠縺ｾ縺吶・
```bash
pwd
git rev-parse --show-toplevel
git status
```

遒ｺ隱阪☆繧矩・岼:

- Current Working Directory.
- Git repository root.
- Expected Working Repository.
- Root matches Working Repository.
- Production Repository.
- Backup / Reference Repository.
- Safe to start.

### Repository Confirmation

遒ｺ隱阪☆繧矩・岼:

- Target Project.
- Working Repository.
- Documentation Root.
- Runtime Root, when needed.
- Single Source Of Truth.
- Related Repository.
- Cross Project Impact.
- Scope Guard.

### Target Project Profile Confirmation

Target Project 縺ｫ Project Profile 縺後≠繧句ｴ蜷医・縲＿ 螳溯｡悟燕縺ｫ隱ｭ縺ｿ縺ｾ縺吶・
遒ｺ隱阪☆繧九％縺ｨ:

- Project Profile path.
- Repository and edit boundary.
- Project-specific rules.
- Project-specific workflow.
- AI context.
- Completion policy.
- Conflict with Q.

### Q / Artifact Confirmation

遒ｺ隱阪☆繧矩・岼:

- Q 縺・Artifact First 蟇ｾ雎｡縺九・- Q 縺・`docs/requests/` 驟堺ｸ九↓菫晏ｭ俶ｸ医∩縺九・- `request.md` 縺悟ｭ伜惠縺吶ｋ縺九・- completion report 縺ｮ菫晏ｭ伜・縺梧ｱｺ縺ｾ縺｣縺ｦ縺・ｋ縺九・- 豺ｻ莉倥ヵ繧｡繧､繝ｫ縲‥ownload file縲∝､夜Κ artifact 縺悟盾辣ｧ縺ｮ縺ｿ縺狗ｷｨ髮・ｯｾ雎｡縺九・
### Q ID / Naming Confirmation

Confirm:

- Q ID exists for official reusable Q artifacts.
- Filename follows `Q_<Q_ID>_<short_topic>_JP.md` when a simple file form is used.
- Task workspace follows `docs/requests/<project>/<status>/<Q_ID>_<short_topic>/` when a workspace is used.
- Date in filename is used only for snapshot, incident, release, migration, external event, or temporary handoff artifacts.
- Addendum versus new Q decision follows `docs/workflow/q_revision_addendum_workflow.md`.

### Q Template Required Fields Confirmation

Confirm:

- Repository Context is complete.
- Commit / Push Policy is explicit.
- Purpose, Background, Scope, and Out of Scope are separated.
- Existing Knowledge / Dependencies are reviewed.
- Deliverables and Validation are defined.
- AI Repository Index Update Gate is decided.
- Completion Report Requirements and Safe Commit Set are required.

### Applicable Rules Confirmation

菴懈･ｭ蜀・ｮｹ縺ｫ蠢懊§縺ｦ遒ｺ隱阪☆繧・rules:

- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/rules/language_rules.md`
- `docs/rules/artifact_first_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_naming_rules.md`
- `docs/rules/q_file_template_rules.md`
- `docs/rules/audit_before_repair_rules.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/debug_escalation_ladder_rules.md`
- `docs/rules/migration_first_rules.md`
- `docs/rules/git_rules.md`

### Applicable Methodologies Confirmation

菴懈･ｭ蜀・ｮｹ縺ｫ蠢懊§縺ｦ遒ｺ隱阪☆繧・methodology:

- First Broken Step Methodology.
- Research Mission.
- Trace Before Tune.
- Human Review before broad repair or adoption.
- Knowledge Before Automation.
- Evidence Feedback Loop.
- Concept Promotion.
- PIP Case Knowledge Base.
- Roadmap2 Knowledge Salvage.

### Scope / Out of Scope Confirmation

遒ｺ隱阪☆繧矩・岼:

- 邱ｨ髮・ｯｾ雎｡縲・- 蜿ら・縺ｮ縺ｿ縺ｮ repository縲・- runtime code 縺ｮ謇ｱ縺・・- generated artifact 縺ｮ謇ｱ縺・・- Debug Artifact 縺ｮ Git policy縲・- Commit policy縲・
### Conversation Insight Detection

Scope / Out of Scope遒ｺ隱榊ｾ後，onversation Insight Candidate縺後≠繧九°繧貞愛螳壹＠縺ｾ縺吶・
讀懷・蟇ｾ雎｡:

- 驥崎ｦ√↑險ｭ險域晄Φ縲・- 驕狗畑譁ｹ驥昴・- 菫晏ｮ域婿驥昴・- Migration謌ｦ逡･縲・- Command Center讒区Φ縲・- 髟ｷ譛滄°逕ｨ譁ｹ驥昴・- 蟆・擂讒区Φ縲・
蛻・ｲ・

```text
Conversation Insight Candidate: No
  -> Continue startup checklist

Conversation Insight Candidate: Yes
  -> Propose candidate
  -> Explain repository value briefly
  -> Do not auto-save
  -> Wait for explicit Human Approval To Draft
```

譏守､ｺ謇ｿ隱阪・萓・

- `譖ｸ縺・→縺・※`
- `菫晏ｭ倥＠縺ｦ`
- `Repository縺ｸ霑ｽ蜉`
- `Q蛹悶＠縺ｦ`
- `Conversation Insight縺ｨ縺励※谿九＠縺ｦ`

AI 縺ｯ繝√Ε繝・ヨ蜈ｨ譁・ｒ菫晏ｭ倥＠縺ｾ縺帙ｓ縲・raft縺ｯapproved knowledge縺ｧ縺ｯ縺ｪ縺上・Promotion縺ｫ縺ｯ蛻･騾排eview縺ｨ隧ｲ蠖努orkflow縺悟ｿ・ｦ√〒縺吶・
### Knowledge Suggestion Assistant Check

Startup縺ｾ縺溘・蠖捺律譛蛻昴・驕ｩ蛻・↑Project interaction縺ｧ縲・未騾｣Knowledge繧堤洒縺乗署譯医〒縺阪∪縺吶・
遒ｺ隱阪☆繧矩・岼:

- Outstanding Review縲・- Related Knowledge Suggestions縲・- Promotion Candidates縲・- Future Candidates縲・
Outstanding Review Notification 縺ｨ Reviewed / Approved Knowledge 縺ｮ
Context-Aware Re-Suggestion 縺ｯ蛹ｺ蛻･縺励∪縺吶・
Reviewed / Approved Knowledge 繧ゅ∫樟蝨ｨ縺ｮ莨夊ｩｱ縲∽ｽ懈･ｭ縲ヽepository迥ｶ豕√→鬮倥＞髢｢騾｣諤ｧ縺・縺ゅｋ蝣ｴ蜷医・蜀肴署譯医〒縺阪∪縺吶・
AI 縺ｯ謠先｡医・縺ｿ陦後＞縲ヽoadmap霑ｽ蜉縲＿蛹悶，odex螳溯｣・ｾ晞ｼ縲ヽule蛹悶、rchitecture蛹悶・Workflow蛹悶、rchive縲ヽeject縲¨o Action 縺ｯ莠ｺ髢薙′蛻､譁ｭ縺励∪縺吶・
### Research Task Detection

Scope / Out of Scope遒ｺ隱榊ｾ後・壼ｸｸ螳溯｣・∈騾ｲ繧蜑阪↓Research Task縺九←縺・°繧貞愛螳壹＠縺ｾ縺吶・
Research Task 縺ｮ莉｣陦ｨ萓・

- 蜴溷屏縺梧悴遒ｺ螳壹・- Root Cause遒ｺ隱阪・- 莉ｮ隱ｬ豈碑ｼ・・- Evidence collection縲・- Knowledge gap蛻・｡槭・- Debug / review邨先棡縺九ｉ谺｡縺ｮ蛻､譁ｭ譚先侭繧帝寔繧√ｋ菴懈･ｭ縲・- First Broken Step迚ｹ螳壹′蠢・ｦ√・
蛻・ｲ・

```text
Research Task: No
  -> Normal Implementation / Review Start

Research Task: Yes
  -> Read/Create Research Mission
  -> Goal / Scope / Out of Scope
  -> Evidence / Validation
  -> Research Mission Workflow
```

Research Task 縺・Yes 縺ｮ蝣ｴ蜷医・縲～templates/research_mission_template.md` 繧剃ｽｿ縺・・Goal縲ヾcope縲＾ut of Scope縲ヽequired Evidence縲〃alidation Method繧呈・遉ｺ縺励※縺九ｉ
隱ｿ譟ｻ繧帝幕蟋九＠縺ｾ縺吶・
### Proactive Proposal Check

AI 縺ｯ縲√ｈ繧雁ｮ牙・縺ｾ縺溘・遏ｭ縺・ｲ繧∵婿縲〉epository / scope conflict縲〉ule conflict縲・methodology conflict縲［aintenance risk縲〔nowledge opportunity 繧呈､懃衍縺励◆蝣ｴ蜷医・蜍晄焔縺ｫ螳溯｣・､画峩縺帙★縲∵ｹ諡縺ｨ蠖ｱ髻ｿ繧呈ｷｻ縺医※謠先｡医＠縺ｾ縺吶・
## Minimal Startup Checklist

遏ｭ縺・ｽ懈･ｭ縺ｧ縺ｯ縲∽ｻ･荳九・譛蟆丞ｽ｢蠑上〒繧医＞縺ｧ縺吶・
```text
Startup Checklist:
- AI index:
- Project profile:
- Repository:
- Root:
- Scope:
- Rules:
- Methodology:
- Q artifact:
- Proposal:
- Conversation Insight:
- Knowledge Suggestions:
- Commit:
- Ready:
```

## Full Startup Checklist

髟ｷ縺・Q縲∬､・焚 repository縲〉eview artifact縲‥ebug artifact縲〉epair縲［igration縲・commit review 繧貞性繧菴懈･ｭ縺ｧ縺ｯ `templates/startup_checklist_template.md` 繧剃ｽｿ縺・∪縺吶・
## Chat Policy

繝√Ε繝・ヨ縺ｫ縺ｯ checklist 縺ｮ隕∫ｴ・□縺代ｒ譖ｸ縺阪∪縺吶・
Checklist 閾ｪ菴薙′蜀榊茜逕ｨ縲√Ξ繝薙Η繝ｼ縲；it 邂｡逅・ｯｾ雎｡縺ｫ縺ｪ繧句ｴ蜷医・縲’ile artifact 縺ｨ縺励※
菫晏ｭ倥＠縺ｾ縺吶・
## Completion Criteria

- Working Repository 縺檎｢ｺ隱阪＆繧後※縺・ｋ縲・- Related Repository 縺ｮ邱ｨ髮・庄蜷ｦ縺檎｢ｺ隱阪＆繧後※縺・ｋ縲・- Applicable Rules 縺檎｢ｺ隱阪＆繧後※縺・ｋ縲・- Applicable Methodologies 縺檎｢ｺ隱阪＆繧後※縺・ｋ縲・- Q Artifact / Download File 縺ｮ謇ｱ縺・′遒ｺ隱阪＆繧後※縺・ｋ縲・- Scope / Out of Scope 縺檎｢ｺ隱阪＆繧後※縺・ｋ縲・- Research Task Detection 縺檎｢ｺ隱阪＆繧後※縺・ｋ縲・- Conversation Insight Detection 縺檎｢ｺ隱阪＆繧後※縺・ｋ縲・- Daily Knowledge Source Review 縺檎｢ｺ隱阪＆繧後※縺・ｋ縲・- Outstanding Review Notification 縺ｨ Related Knowledge Suggestions 縺ｮ隕∝凄縺檎｢ｺ隱阪＆繧後※縺・ｋ縲・- Research Task 縺ｮ蝣ｴ蜷医ヽesearch Mission 縺ｮ蜈･蜿｣縺檎｢ｺ隱阪＆繧後※縺・ｋ縲・- Commit policy 縺檎｢ｺ隱阪＆繧後※縺・ｋ縲・- Checklist 螳御ｺ・ｾ後↓ implementation / review 繧帝幕蟋九〒縺阪ｋ縲・
## Related Documents

- `docs/rules/startup_checklist_rules.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/rules/research_mission_rules.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/workflow/research_mission_workflow.md`
- `docs/workflow/conversation_insight_capture_workflow.md`
- `docs/architecture/context_aware_knowledge_suggestion_assistant.md`
- `templates/research_mission_template.md`
- `templates/conversation_insight_template.md`
- `templates/information_package_template.md`
- `templates/startup_checklist_template.md`
- `examples/startup_checklist_examples.md`
- `docs/workflow/README.md`
- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/rules/ai_proactive_proposal_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/workflow/commit_safety_checklist.md`
