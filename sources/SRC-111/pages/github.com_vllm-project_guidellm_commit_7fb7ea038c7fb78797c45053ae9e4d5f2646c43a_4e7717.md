source: https://github.com/vllm-project/guidellm/commit/7fb7ea038c7fb78797c45053ae9e4d5f2646c43a

# Commit 7fb7ea0

committed

Replace InfoMixin w/ disdantic version

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>1 parent[42fc629]commit 7fb7ea0

12 files changed

Lines changed: 12 additions & 371 deletions

## File tree

- src/guidellm
- benchmark
- data
- loaders

- scheduler
- constraints

- utils

- tests/unit
- scheduler
- utils


| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`15` | `15` |
| |
`16` | `16` |
| |
`17` | `17` |
| |
| `18` | `+` | |
| `19` | `+` | |
`18` | `20` |
| |
`19` | `21` |
| |
`20` | `22` |
| |
| |||
`34` | `36` |
| |
`35` | `37` |
| |
`36` | `38` |
| |
`37` |
| `-` | |
`38` | `39` |
| |
`39` | `40` |
| |
`40` | `41` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`15` | `15` |
| |
`16` | `16` |
| |
`17` | `17` |
| |
`18` |
| `-` | |
| `18` | `+` | |
`19` | `19` |
| |
`20` | `20` |
| |
`21` | `21` |
| |
| |||
`49` | `49` |
| |
`50` | `50` |
| |
`51` | `51` |
| |
`52` |
| `-` | |
`53` | `52` |
| |
`54` | `53` |
| |
`55` | `54` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`2` | `2` |
| |
`3` | `3` |
| |
`4` | `4` |
| |
| `5` | `+` | |
`5` | `6` |
| |
`6` | `7` |
| |
`7` | `8` |
| |
| |||
`24` | `25` |
| |
`25` | `26` |
| |
`26` | `27` |
| |
`27` |
| `-` | |
`28` | `28` |
| |
`29` | `29` |
| |
`30` | `30` |
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
`8` | `9` |
| |
`9` | `10` |
| |
`10` | `11` |
| |
| |||
`20` | `21` |
| |
`21` | `22` |
| |
`22` | `23` |
| |
`23` |
| `-` | |
`24` | `24` |
| |
`25` | `25` |
| |
`26` | `26` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`35` | `35` |
| |
`36` | `36` |
| |
`37` | `37` |
| |
| `38` | `+` | |
`38` | `39` |
| |
`39` | `40` |
| |
`40` | `41` |
| |
`41` | `42` |
| |
`42` |
| `-` | |
`43` | `43` |
| |
`44` | `44` |
| |
`45` | `45` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`11` | `11` |
| |
`12` | `12` |
| |
`13` | `13` |
| |
| `14` | `+` | |
`14` | `15` |
| |
`15` | `16` |
| |
`16` | `17` |
| |
| |||
`28` | `29` |
| |
`29` | `30` |
| |
`30` | `31` |
| |
`31` |
| `-` | |
`32` | `32` |
| |
`33` | `33` |
| |
`34` | `34` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`23` | `23` |
| |
`24` | `24` |
| |
`25` | `25` |
| |
| `26` | `+` | |
| `27` | `+` | |
`26` | `28` |
| |
`27` | `29` |
| |
`28` | `30` |
| |
| |||
`33` | `35` |
| |
`34` | `36` |
| |
`35` | `37` |
| |
`36` |
| `-` | |
`37` | `38` |
| |
`38` | `39` |
| |
`39` | `40` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`24` | `24` |
| |
`25` | `25` |
| |
`26` | `26` |
| |
| `27` | `+` | |
`27` | `28` |
| |
`28` | `29` |
| |
`29` | `30` |
| |
`30` |
| `-` | |
`31` | `31` |
| |
`32` | `32` |
| |
`33` | `33` |
| |
|

This file was deleted.

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
`8` | `9` |
| |
`9` | `10` |
| |
`10` | `11` |
| |
| |||
`32` | `33` |
| |
`33` | `34` |
| |
`34` | `35` |
| |
`35` |
| `-` | |
`36` | `36` |
| |
`37` | `37` |
| |
`38` | `38` |
| |
|

## 0 commit comments