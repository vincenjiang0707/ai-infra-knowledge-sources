source: https://github.com/vllm-project/guidellm/commit/42fc62958d2af7ebcc20c3f17c919a8c9c8983cd

# Commit 42fc629

committed

Swapout PydanticClassRegistryMixin, RegistryMixin and ReloadableBaseModel with disdantic versions

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>1 parent[e9c993f]commit 42fc629

27 files changed

Lines changed: 67 additions & 1858 deletions

## File tree

- src/guidellm
- backends
- openai

- benchmark
- outputs
- profiles
- schemas

- data
- deserializers
- finalizers
- loaders
- preprocessors
- schemas
- tokenizers

- scheduler
- constraints

- schemas
- utils

- tests/unit
- backends
- openai

- schemas
- utils


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
`17` | `18` |
| |
`18` | `19` |
| |
`19` | `20` |
| |
`20` |
| `-` | |
| `21` | `+` | |
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
`27` | `27` |
| |
`28` | `28` |
| |
`29` | `29` |
| |
`30` | `30` |
| |
`31` |
| `-` | |
| `31` | `+` | |
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
`16` | `16` |
| |
`17` | `17` |
| |
`18` | `18` |
| |
| `19` | `+` | |
`19` | `20` |
| |
`20` | `21` |
| |
`21` | `22` |
| |
| |||
`26` | `27` |
| |
`27` | `28` |
| |
`28` | `29` |
| |
`29` |
| `-` | |
`30` | `30` |
| |
`31` | `31` |
| |
`32` | `32` |
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
| `18` | `+` | |
| `19` | `+` | |
`18` | `20` |
| |
`19` | `21` |
| |
`20` | `22` |
| |
| |||
`48` | `50` |
| |
`49` | `51` |
| |
`50` | `52` |
| |
`51` |
| `-` | |
`52` | `53` |
| |
`53` | `54` |
| |
`54` | `55` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`13` | `13` |
| |
`14` | `14` |
| |
`15` | `15` |
| |
| `16` | `+` | |
`16` | `17` |
| |
`17` | `18` |
| |
`18` | `19` |
| |
`19` |
| `-` | |
`20` | `20` |
| |
`21` | `21` |
| |
`22` | `22` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`8` | `8` |
| |
`9` | `9` |
| |
`10` | `10` |
| |
| `11` | `+` | |
| `12` | `+` | |
`11` | `13` |
| |
`12` | `14` |
| |
`13` | `15` |
| |
`14` | `16` |
| |
`15` | `17` |
| |
`16` | `18` |
| |
`17` | `19` |
| |
`18` |
| `-` | |
`19` | `20` |
| |
`20` | `21` |
| |
`21` | `22` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`16` | `16` |
| |
`17` | `17` |
| |
`18` | `18` |
| |
| `19` | `+` | |
`19` | `20` |
| |
`20` | `21` |
| |
`21` | `22` |
| |
| |||
`39` | `40` |
| |
`40` | `41` |
| |
`41` | `42` |
| |
`42` |
| `-` | |
`43` |
| `-` | |
`44` | `43` |
| |
`45` | `44` |
| |
`46` | `45` |
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
`8` |
| `-` | |
| `8` | `+` | |
`9` | `9` |
| |
`10` | `10` |
| |
`11` | `11` |
| |
`12` | `12` |
| |
`13` | `13` |
| |
`14` | `14` |
| |
`15` |
| `-` | |
| `15` | `+` | |
`16` | `16` |
| |
`17` | `17` |
| |
`18` | `18` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`19` | `19` |
| |
`20` | `20` |
| |
`21` | `21` |
| |
`22` |
| `-` | |
| `22` | `+` | |
`23` | `23` |
| |
`24` | `24` |
| |
`25` | `25` |
| |
`26` | `26` |
| |
`27` | `27` |
| |
`28` |
| `-` | |
| `28` | `+` | |
`29` | `29` |
| |
`30` | `30` |
| |
`31` | `31` |
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
`8` |
| `-` | |
| `8` | `+` | |
`9` | `9` |
| |
`10` | `10` |
| |
`11` | `11` |
| |
`12` | `12` |
| |
`13` | `13` |
| |
`14` | `14` |
| |
`15` | `15` |
| |
`16` |
| `-` | |
| `16` | `+` | |
`17` | `17` |
| |
`18` | `18` |
| |
`19` | `19` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`3` | `3` |
| |
`4` | `4` |
| |
`5` | `5` |
| |
| `6` | `+` | |
`6` | `7` |
| |
`7` | `8` |
| |
`8` | `9` |
| |
`9` |
| `-` | |
`10` | `10` |
| |
`11` | `11` |
| |
`12` | `12` |
| |
|

## 0 commit comments