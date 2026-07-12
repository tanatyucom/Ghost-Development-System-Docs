# Migration First Examples

## Purpose

縺薙・譁・嶌縺ｯ縲∝・驛ｨ architecture 繧貞､画峩縺吶ｋ縺ｨ縺阪↓ Migration First 繧偵←縺・ｽｿ縺・°繧・遉ｺ縺吩ｾ九〒縺吶・
Examples 縺ｯ蜿り・ｳ・侭縺ｧ縺吶よｭ｣蠑上↑蛻､譁ｭ縺ｯ `docs/rules/migration_first_rules.md`
縺ｨ Q 縺ｮ Scope Guard 縺ｫ蠕薙＞縺ｾ縺吶・
## Bad: Chat Only Internal Rename

Bad:

```text
繝√Ε繝・ヨ縺ｧ縲経ld_scripts 繧・new_scripts 縺ｫ螟峨∴縺ｦ縲阪→縺縺台ｾ晞ｼ縺吶ｋ縲・譌ｧ path 蜿ら・繧呈爾縺輔↑縺・・譌ｧ path fallback 繧呈ｮ九☆縲・Completion Report 縺ｫ Remaining Legacy 繧呈嶌縺九↑縺・・```

Problem:

- Codex 縺梧立 path 繧貞盾辣ｧ縺礼ｶ壹￠繧九・- 縺ｩ縺ｮ讒矩縺梧ｨ呎ｺ悶°繧上°繧峨↑縺・・- fallback 縺梧￡荵・喧縺吶ｋ縲・- 蠕後°繧牙炎髯､譚｡莉ｶ縺瑚ｿｽ縺医↑縺・・
## Good: Q Artifact With Migration Plan

Good:

```text
Q artifact:
  New Standard: scripts/review/
  Migration Plan: old review scripts 繧・scripts/review/ 縺ｫ遘ｻ縺・  Reference Update: README, workflow, templates, tests, examples 繧呈峩譁ｰ縺吶ｋ
  Verification: rg old_scripts, test, dry-run
  Legacy Removal: old_scripts fallback 繧貞炎髯､縺吶ｋ
  Public Compatibility Impact: None
  Remaining Legacy: None expected
  Restore / Rollback Guidance: git restore <changed files>
```

Result:

- 譁ｰ讓呎ｺ悶′譏守｢ｺ縺ｫ縺ｪ繧九・- 譌ｧ蜿ら・縺ｮ譖ｴ譁ｰ貍上ｌ繧呈､懷・縺ｧ縺阪ｋ縲・- legacy removal 縺・completion criteria 縺ｫ縺ｪ繧九・- completion report 縺ｧ migration result 繧堤｢ｺ隱阪〒縺阪ｋ縲・
## Bad: Permanent Internal Fallback

Bad:

```text
譁ｰ縺励＞ artifact workspace 繧定ｿｽ蜉縺吶ｋ縲・蜿､縺・workspace 繧ら┌譛滄剞縺ｧ隱ｭ縺ｿ邯壹￠繧九・縺ｪ縺懈ｮ九☆縺九ｒ譖ｸ縺九↑縺・・蜑企勁莠亥ｮ壹ｒ譖ｸ縺九↑縺・・Public Compatibility 縺ｨ internal convenience 繧呈ｷｷ蜷後☆繧九・```

Problem:

- internal convenience 縺・public contract 縺ｮ繧医≧縺ｫ謇ｱ繧上ｌ繧九・- Queue Manager 繧・Artifact Manager 縺御ｺ碁㍾讒矩縺ｫ縺ｪ繧九・- AI 縺悟商縺・workspace 繧呈ｭ｣縺励＞蜈･蜉帙→縺励※謇ｱ縺・・
## Good: Temporary Fallback With Removal Plan

Good:

```text
Temporary legacy fallback:
  Reason: 譌｢蟄・approved Q 縺ｮ completion report 縺後∪縺譌ｧ workspace 繧貞盾辣ｧ縺励※縺・ｋ
  Removal plan: 蜿ら・譖ｴ譁ｰ蠕後↓ fallback 繧貞炎髯､縺吶ｋ
  Completion criteria: rg 縺ｧ譌ｧ workspace 蜿ら・縺後↑縺・％縺ｨ繧堤｢ｺ隱阪☆繧・  Remaining Legacy: completion report 縺ｫ谿倶ｻｶ縺ｨ縺励※蝣ｱ蜻翫☆繧・  Follow-up Q: 譌ｧ workspace 蜿ら・蜑企勁 Q 繧剃ｽ懊ｋ
```

Result:

- fallback 縺御ｸ譎ら噪縺ｧ縺ゅｋ縺薙→縺梧・遒ｺ縺ｫ縺ｪ繧九・- 蜑企勁譚｡莉ｶ縺梧ｮ九ｋ縲・- 谺｡縺ｮ Q 縺ｸ縺､縺ｪ縺後ｋ縲・
## Bad: Public Compatibility Overreach

Bad:

```text
蜀・Κ prototype script 縺ｮ蜷榊燕繧貞､峨∴繧九□縺代↑縺ｮ縺ｫ縲∝・譌ｧ command 繧呈ｰｸ荵・ｶｭ謖√☆繧九・```

Problem:

- public API / CLI 縺ｧ縺ｯ縺ｪ縺・・驛ｨ helper 縺ｾ縺ｧ莠呈鋤蟇ｾ雎｡縺ｫ縺ｪ繧九・- script architecture 縺瑚､・尅蛹悶☆繧九・
## Good: Public Compatibility Boundary

Good:

```text
Public Compatibility Impact:
  public CLI: No impact
  documented external workflow: No impact
  exported artifact schema: No impact
  DB schema: No impact
  user-facing data format: No impact

Internal change:
  prototype script path 繧呈眠讓呎ｺ悶∈遘ｻ陦後☆繧・  old prototype path 縺ｯ蜑企勁縺吶ｋ
```

Result:

- 螳医ｋ縺ｹ縺榊・髢・contract 縺ｨ縲∫ｧｻ陦後＠縺ｦ繧医＞蜀・Κ讒矩縺悟・縺九ｌ繧九・- 繝ｬ繝薙Η繝ｼ遽・峇縺悟ｰ上＆縺上↑繧九・
## Completion Report Example

```text
Migration First Review

- Migration First applies: Yes
- New Standard: docs/requests/<project>/<status>/<Q_ID>_<short_topic>/
- Migration Plan result: completed
- Reference Update result: README, templates, workflow updated
- Verification result: rg old path returned no active references
- Legacy Removal result: old fallback removed
- Public Compatibility Impact: None
- Remaining Legacy: None
- Restore / Rollback Guidance: git restore <changed files>
```
