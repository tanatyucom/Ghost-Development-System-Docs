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
- Future Candidates が approved scope と混同されていない。
- Purpose-Oriented Naming が使われている。

## Documentation Quality

- 目的が private context なしで理解できる。
- 背景と理由が短く残っている。
- 文書の責務が 1 つに保たれている。
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
