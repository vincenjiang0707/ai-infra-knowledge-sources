source: https://github.com/vllm-project/guidellm/commit/e95d4c26d0e74238fdbd16bcc5eec7251d4f6fe3

# Commit e95d4c2

committed

feat: add OrcaRouter HTTP backend

Add a first-class `orcarouter_http` backend that mirrors the existing
`openai_http` backend and targets the OrcaRouter API, an OpenAI-compatible
AI gateway. OrcaRouter exposes a provider/model namespace across many models
with adaptive routing and automatic failover, so users can benchmark through
it directly instead of configuring an anonymous custom base URL.
The backend reuses the OpenAI-compatible request machinery, specializes the
validation probe to the `/v1/models` endpoint (OrcaRouter has no `/health`
route), and defaults the model to `orcarouter/auto` when none is configured.
Documentation and unit tests are included.
Generated-by: Claude
Signed-off-by: nissrin2020ali-ux <nissrin2020ali-ux@users.noreply.github.com>1 parent[7cc46d6]commit e95d4c2

8 files changed

Lines changed: 363 additions & 0 deletions

## File tree

- docs/guides
- src/guidellm
- backends
- orcarouter

- schemas/backends

- tests/unit/backends/orcarouter

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`36` | `36` |
| |
`37` | `37` |
| |
`38` | `38` |
| |
| `39` | `+` | |
| `40` | `+` | |
| `41` | `+` | |
| `42` | `+` | |
| `43` | `+` | |
| `44` | `+` | |
| `45` | `+` | |
| `46` | `+` | |
| `47` | `+` | |
| `48` | `+` | |
| `49` | `+` | |
| `50` | `+` | |
| `51` | `+` | |
| `52` | `+` | |
| `53` | `+` | |
| `54` | `+` | |
| `55` | `+` | |
| `56` | `+` | |
`39` | `57` |
| |
`40` | `58` |
| |
`41` | `59` |
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
| `22` | `+` | |
`22` | `23` |
| |
`23` | `24` |
| |
`24` | `25` |
| |
| |||
`33` | `34` |
| |
`34` | `35` |
| |
`35` | `36` |
| |
| `37` | `+` | |
`36` | `38` |
| |
`37` | `39` |
| |
`38` | `40` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
| `1` | `+` | |
| `2` | `+` | |
| `3` | `+` | |
| `4` | `+` | |
| `5` | `+` | |
| `6` | `+` | |
| `7` | `+` |

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
| `1` | `+` | |
| `2` | `+` | |
| `3` | `+` | |
| `4` | `+` | |
| `5` | `+` | |
| `6` | `+` | |
| `7` | `+` | |
| `8` | `+` | |
| `9` | `+` | |
| `10` | `+` | |
| `11` | `+` | |
| `12` | `+` | |
| `13` | `+` | |
| `14` | `+` | |
| `15` | `+` | |
| `16` | `+` | |
| `17` | `+` | |
| `18` | `+` | |
| `19` | `+` | |
| `20` | `+` | |
| `21` | `+` | |
| `22` | `+` | |
| `23` | `+` | |
| `24` | `+` | |
| `25` | `+` | |
| `26` | `+` | |
| `27` | `+` | |
| `28` | `+` | |
| `29` | `+` | |
| `30` | `+` | |
| `31` | `+` | |
| `32` | `+` | |
| `33` | `+` | |
| `34` | `+` | |
| `35` | `+` | |
| `36` | `+` | |
| `37` | `+` | |
| `38` | `+` | |
| `39` | `+` | |
| `40` | `+` | |
| `41` | `+` | |
| `42` | `+` | |
| `43` | `+` | |
| `44` | `+` | |
| `45` | `+` | |
| `46` | `+` | |
| `47` | `+` | |
| `48` | `+` | |
| `49` | `+` | |
| `50` | `+` | |
| `51` | `+` | |
| `52` | `+` | |
| `53` | `+` | |
| `54` | `+` | |
| `55` | `+` | |
| `56` | `+` | |
| `57` | `+` | |
| `58` | `+` | |
| `59` | `+` | |
| `60` | `+` | |
| `61` | `+` | |
| `62` | `+` | |
| `63` | `+` | |
| `64` | `+` | |
| `65` | `+` | |
| `66` | `+` | |
| `67` | `+` | |
| `68` | `+` | |
| `69` | `+` | |
| `70` | `+` | |
| `71` | `+` | |
| `72` | `+` | |
| `73` | `+` | |
| `74` | `+` | |
| `75` | `+` | |
| `76` | `+` | |
| `77` | `+` | |
| `78` | `+` | |
| `79` | `+` | |
| `80` | `+` | |
| `81` | `+` | |
| `82` | `+` | |
| `83` | `+` | |
| `84` | `+` | |
| `85` | `+` | |
| `86` | `+` | |
| `87` | `+` | |
| `88` | `+` | |
| `89` | `+` | |
| `90` | `+` | |
| `91` | `+` | |
| `92` | `+` | |
| `93` | `+` | |
| `94` | `+` | |
| `95` | `+` | |
| `96` | `+` | |
| `97` | `+` | |
| `98` | `+` | |
| `99` | `+` | |
| `100` | `+` | |
| `101` | `+` |

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`7` | `7` |
| |
`8` | `8` |
| |
`9` | `9` |
| |
| `10` | `+` | |
`10` | `11` |
| |
`11` | `12` |
| |
`12` | `13` |
| |
`13` | `14` |
| |
`14` | `15` |
| |
`15` | `16` |
| |
`16` | `17` |
| |
| `18` | `+` | |
`17` | `19` |
| |
`18` | `20` |
| |
`19` | `21` |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
| `1` | `+` | |
| `2` | `+` | |
| `3` | `+` | |
| `4` | `+` | |
| `5` | `+` | |
| `6` | `+` | |
| `7` | `+` | |
| `8` | `+` | |
| `9` | `+` | |
| `10` | `+` | |
| `11` | `+` | |
| `12` | `+` | |
| `13` | `+` | |
| `14` | `+` | |
| `15` | `+` | |
| `16` | `+` | |
| `17` | `+` | |
| `18` | `+` | |
| `19` | `+` | |
| `20` | `+` | |
| `21` | `+` | |
| `22` | `+` | |
| `23` | `+` | |
| `24` | `+` | |
| `25` | `+` | |
| `26` | `+` | |
| `27` | `+` | |
| `28` | `+` | |
| `29` | `+` | |
| `30` | `+` | |
| `31` | `+` | |
| `32` | `+` | |
| `33` | `+` | |
| `34` | `+` | |
| `35` | `+` | |
| `36` | `+` | |
| `37` | `+` | |
| `38` | `+` | |
| `39` | `+` | |
| `40` | `+` | |
| `41` | `+` | |
| `42` | `+` | |
| `43` | `+` | |
| `44` | `+` | |
| `45` | `+` | |
| `46` | `+` |

Whitespace-only changes.

## 0 commit comments