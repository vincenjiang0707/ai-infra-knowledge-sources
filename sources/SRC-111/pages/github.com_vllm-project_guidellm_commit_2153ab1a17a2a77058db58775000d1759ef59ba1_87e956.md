source: https://github.com/vllm-project/guidellm/commit/2153ab1a17a2a77058db58775000d1759ef59ba1

# Commit 2153ab1

committed

Fix shared mutable fill values in argument parsing

ArgStringParser evaluated the fill-value factory once during construction
and reused that object for every sparse list position. With fill_value=list
or dict, mutating one placeholder changed other positions and results from
subsequent decodes using the same parser.
Retain the factory and invoke it separately for every added list position.
Keep a separate reference value for the existing overwrite checks. Add
regression coverage for mutable list and dictionary fills, nested paths,
repeated decode calls, and successive set calls.
Assisted-by: Codex
Signed-off-by: tangming1996 <ming.tang@daocloud.io>1 parent[7cc46d6]commit 2153ab1

2 files changed

Lines changed: 50 additions & 3 deletions

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`67` | `67` |
| |
`68` | `68` |
| |
`69` | `69` |
| |
`70` |
| `-` | |
| `70` | `+` | |
`71` | `71` |
| |
`72` | `72` |
| |
`73` | `73` |
| |
`74` | `74` |
| |
`75` |
| `-` | |
| `75` | `+` | |
| `76` | `+` | |
| `77` | `+` | |
| `78` | `+` | |
| `79` | `+` | |
`76` | `80` |
| |
`77` | `81` |
| |
`78` | `82` |
| |
| |||
`250` | `254` |
| |
`251` | `255` |
| |
`252` | `256` |
| |
`253` |
| `-` | |
| `257` | `+` | |
`254` | `258` |
| |
`255` | `259` |
| |
`256` | `260` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`43` | `43` |
| |
`44` | `44` |
| |
`45` | `45` |
| |
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
`46` | `89` |
| |
`47` | `90` |
| |
`48` | `91` |
| |
|

## 0 commit comments