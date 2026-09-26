source: https://github.com/vllm-project/guidellm/commit/db6ec4ee7d7b78ed7f1029c5977f2cd17492b842

# Commit db6ec4e

committed

fix(metrics): preserve all cancellations in final scheduler counts

Address PR [#1102](https://github.com/vllm-project/guidellm/pull/1102)review feedback: scheduler requests_made includes every cancellation, with the shared incomplete field representing cancelled. Filtered measurement-window counts remain in metrics.request_totals. Compile scheduler outcomes from the final SchedulerState. The cached accumulator can be stale when the last event is a queued cancellation, because that event returns before updating scheduler metric counts. Document the distinction without changing the serialized field names. Regression evidence: restoring the original cached-count implementation produced 5 failures (four trailing-cancellation permutations and the all-queued-cancelled case). The corrected path passes all permutations of queued cancellation, started cancellation, and completion/error. Validation: - tox focused benchmark and worker checks: 153 passed, 12 deselected. - tox lint-check and type-check: passed (222 source files). - Broader benchmark/scheduler run: 700 passed, 16 xfailed, 5 failed. The five failures occur at multiprocessing.Manager startup in this sandbox. A representative case also fails with the original metrics implementation: PermissionError creating a socket, followed by EOFError. - git diff --check: passed. Generated-by: OpenAI Codex Signed-off-by: Divyam Talwar <divyamtalwar0@gmail.com>

1 parent[7c2d3ed]commit db6ec4e

3 files changed

Lines changed: 88 additions & 59 deletions

## File tree

- docs/guides
- src/guidellm/benchmark/schemas
- tests/unit/benchmark/schemas

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`17` | `17` |
| |
`18` | `18` |
| |
`19` | `19` |
| |
| `20` | `+` | |
| `21` | `+` | |
| `22` | `+` | |
| `23` | `+` | |
| `24` | `+` | |
`20` | `25` |
| |
`21` | `26` |
| |
`22` | `27` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`84` | `84` |
| |
`85` | `85` |
| |
`86` | `86` |
| |
`87` |
| `-` | |
| `87` | `+` | |
| `88` | `+` | |
| `89` | `+` | |
| `90` | `+` | |
`88` | `91` |
| |
`89` | `92` |
| |
`90` | `93` |
| |
| |||
`138` | `141` |
| |
`139` | `142` |
| |
`140` | `143` |
| |
`141` |
| `-` | |
| `144` | `+` | |
| `145` | `+` | |
`142` | `146` |
| |
`143` |
| `-` | |
`144` |
| `-` | |
`145` |
| `-` | |
| `147` | `+` | |
| `148` | `+` | |
| `149` | `+` | |
`146` | `150` |
| |
`147` |
| `-` | |
`148` |
| `-` | |
`149` |
| `-` | |
| `151` | `+` | |
| `152` | `+` | |
| `153` | `+` | |
`150` | `154` |
| |
`151` | `155` |
| |
`152` | `156` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`5` | `5` |
| |
`6` | `6` |
| |
`7` | `7` |
| |
| `8` | `+` | |
| `9` | `+` | |
| `10` | `+` | |
`8` | `11` |
| |
`9` | `12` |
| |
`10` | `13` |
| |
| |||
`23` | `26` |
| |
`24` | `27` |
| |
`25` | `28` |
| |
`26` |
| `-` | |
`27` | `29` |
| |
`28` | `30` |
| |
`29` | `31` |
| |
| `32` | `+` | |
`30` | `33` |
| |
`31` | `34` |
| |
`32` | `35` |
| |
| |||
`284` | `287` |
| |
`285` | `288` |
| |
`286` | `289` |
| |
`287` |
| `-` | |
`288` |
| `-` | |
`289` |
| `-` | |
| `290` | `+` | |
| `291` | `+` | |
| `292` | `+` | |
| `293` | `+` | |
| `294` | `+` | |
| `295` | `+` | |
`290` | `296` |
| |
`291` | `297` |
| |
`292` | `298` |
| |
`293` | `299` |
| |
`294` |
| `-` | |
| `300` | `+` | |
`295` | `301` |
| |
`296` |
| `-` | |
`297` | `302` |
| |
`298` |
| `-` | |
`299` |
| `-` | |
`300` |
| `-` | |
`301` |
| `-` | |
`302` |
| `-` | |
`303` |
| `-` | |
`304` |
| `-` | |
`305` |
| `-` | |
`306` |
| `-` | |
`307` |
| `-` | |
`308` |
| `-` | |
`309` |
| `-` | |
`310` |
| `-` | |
`311` |
| `-` | |
`312` |
| `-` | |
`313` |
| `-` | |
`314` |
| `-` | |
`315` |
| `-` | |
`316` |
| `-` | |
`317` |
| `-` | |
`318` |
| `-` | |
`319` |
| `-` | |
| `303` | `+` | |
| `304` | `+` | |
`320` | `305` |
| |
`321` |
| `-` | |
`322` |
| `-` | |
`323` |
| `-` | |
`324` |
| `-` | |
`325` |
| `-` | |
| `306` | `+` | |
| `307` | `+` | |
| `308` | `+` | |
`326` | `309` |
| |
`327` | `310` |
| |
`328` |
| `-` | |
`329` |
| `-` | |
`330` |
| `-` | |
| `311` | `+` | |
| `312` | `+` | |
| `313` | `+` | |
`331` | `314` |
| |
`332` | `315` |
| |
`333` |
| `-` | |
| `316` | `+` | |
| `317` | `+` | |
| `318` | `+` | |
| `319` | `+` | |
| `320` | `+` | |
| `321` | `+` | |
| `322` | `+` | |
| `323` | `+` | |
| `324` | `+` | |
| `325` | `+` | |
| `326` | `+` | |
| `327` | `+` | |
| `328` | `+` | |
| `329` | `+` | |
| `330` | `+` | |
| `331` | `+` | |
| `332` | `+` | |
| `333` | `+` | |
| `334` | `+` | |
| `335` | `+` | |
| `336` | `+` | |
| `337` | `+` | |
| `338` | `+` | |
| `339` | `+` | |
`334` | `340` |
| |
`335` |
| `-` | |
`336` |
| `-` | |
| `341` | `+` | |
| `342` | `+` | |
| `343` | `+` | |
| `344` | `+` | |
| `345` | `+` | |
| `346` | `+` | |
| `347` | `+` | |
| `348` | `+` | |
| `349` | `+` | |
| `350` | `+` | |
| `351` | `+` | |
| `352` | `+` | |
| `353` | `+` | |
| `354` | `+` | |
| `355` | `+` | |
| `356` | `+` | |
| `357` | `+` | |
| `358` | `+` | |
| `359` | `+` | |
`337` | `360` |
| |
`338` | `361` |
| |
`339` |
| `-` | |
`340` |
| `-` | |
`341` |
| `-` | |
`342` |
| `-` | |
`343` |
| `-` | |
`344` |
| `-` | |
`345` |
| `-` | |
| `362` | `+` | |
| `363` | `+` | |
| `364` | `+` | |
| `365` | `+` | |
`346` | `366` |
| |
`347` | `367` |
| |
`348` |
| `-` | |
| `368` | `+` | |
`349` | `369` |
| |
`350` |
| `-` | |
`351` |
| `-` | |
`352` |
| `-` | |
`353` |
| `-` | |
| `370` | `+` | |
| `371` | `+` | |
| `372` | `+` | |
| `373` | `+` | |
`354` | `374` |
| |
`355` | `375` |
| |
`356` | `376` |
| |
|

## 0 commit comments