# Review Checklist

この checklist は、Ghost Development System Docs の documentation review 品質を
一定に保つために使います。

## Repository And Project

- Target Project が明記されている。
- Repository が明記されている。
- Working Directory が明記されている。
- Documentation Root が明記されている。
- Runtime Root が対象外または対象として明記されている。
- Single Source Of Truth が明記されている。
- Related Repository の扱いが editable / reference only / forbidden のどれか
  分かる。
- Cross Project Impact が明記されている。
- Cross Project Impact が `None` 以外の場合、別 Q または Human Approval Gate が
  必要か確認されている。

## Startup Checklist

- Startup Checklist が作業開始前に確認されている。
- Working Repository が確認されている。
- Repository Root Validation が実行されている。
- Git repository root が Working Repository と一致している。
- backup / reference-only repository で作業していない。
- Production / Backup / Reference Only boundaries が確認されている。
- Current Phase と Current Goal が確認されている。
- Applicable Rules が作業内容に合っている。
- Applicable Methodologies が作業内容に合っている。
- Q Artifact / Download File の扱いが確認されている。
- Scope / Out of Scope が確認されている。
- Commit policy が確認されている。
- Better approach / time saving / concern / knowledge opportunity がある場合、
  AI が勝手に実装せず提案として分離している。

## Completion Checklist

- Completion Checklist が作業完了前に確認されている。
- Verification Completed が記録されている。
- Review Completed が記録されている。
- Completion Report Completed が記録されている。
- Improvement Review Completed が記録されている。
- Commit Required と Commit Executed が分離されている。
- Tag Required と Tag Executed が分離されている。
- Release Required と Release Published が分離されている。
- Recommended Next Q が記録されている。
- Workspace Clean Confirmation または dirty state が記録されている。

## Scope Guard

- Scope Guard が具体的である。
- 編集対象と編集禁止対象が分かれている。
- Runtime Code が out of scope の場合、変更されていない。
- GameGhost など related repository が reference only の場合、編集、同期、
  コピー、移行されていない。
- Git Migration、GitHub Actions、Release が out of scope の場合、変更されて
  いない。
- Commit 禁止の Q で commit されていない。

## Rules And Authority

- `docs/rules/rules.md` の authority order に従っている。
- Project First Principle が守られている。
- Japanese First が守られている。
- Human Approval が必要な事項を AI が勝手に昇格していない。
- Authority-Driven Responsibility Principle が必要な設計で確認されている。
- Execution Authority Registry が必要な設計で参照されている。
- Responsibility と Authority が一致している。
- Actor が実行不可能な操作の許可を求めていない。
- Review Actor が Execution Actor を代行していない。
- Human Approval の対象 Action が明確である。
- Approval Unit と Execution Unit が一致している。
- 実行後 Evidence の生成主体が明確である。
- 権限不明時は SCW に従い停止する。
- Future Candidates が approved scope と混同されていない。
- Purpose-Oriented Naming が使われている。

## Documentation Quality

- 目的が private context なしで理解できる。
- 背景と理由が短く残っている。
- 文書の責務が 1 つに保たれている。
- Beginner & Future Self Test が必要な artifact で実施されている。
- 初心者、新しい AI session、未来の担当者が purpose、project / domain、
  current position、evidence、next action、authority を追える。
- Context Recovery Principle の観点で、何も覚えていない人や AI が安全に
  resume できる。
- current position、completion report、decision record、next action、
  Human Approval boundary、known blocker、last verified state など、必要な
  recovery aid がある。
- hidden chat context に依存していない。
- BFS Test のために authoritative source を過剰複製していない。
- Folder README の構成が必要に応じて `Purpose / Contains / Does NOT Contain /
  Update Policy / Related Documents` に近い。
- README 更新が必要な場合、導線が追加されている。
- docs 更新が必要な場合、関連文書が整合している。

## Workflow And Verification

- Workflow Rev.2 Trial status が必要に応じて尊重されている。
- Current Focus が必要な作業では resume point が明確である。
- `run_all.py` が必要な作業では確認されている。
- `tool.py health` が必要な作業では確認されている。
- schema validation が必要な作業では確認されている。
- documentation-only work では、Markdown と参照パスの確認が行われている。

## Metrics And Evidence

- Metrics が利用できる場合、source、sample、period、interpretation が明示されている。
- OCR quality、review workload、documentation reuse、automation rate などの変化が
  必要に応じて確認されている。
- raw metrics が Human Approval Gate や rule standardization を自動的に置き換えて
  いない。
- 測定していない項目は Remaining Issues または Not measured として明示されている。

## Improvement Review

- Improvement Review が含まれている。
- Recommended Improvements と Future Candidates が分離されている。
- 再利用できる知識が rules、templates、examples、workflow、architecture、
  roadmap、history、または documentation に昇格すべきか確認されている。
- Suggested Commit Message が明確である。

## Final Report

- Changed Files が含まれている。
- Summary が含まれている。
- Verification が含まれている。
- Remaining Issues が含まれている。
- Recommended Next Q が含まれている。
- Suggested Commit Message が含まれている。
