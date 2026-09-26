source: https://github.com/vllm-project/guidellm/commit/6dd730328290a0d3c633ee686eae64012b175e31

# Commit 6dd7303

refactor: simplify API key rotation

Use worker-specific offsets, separate API credential validation, and load key files in the HTTP backend.
Co-authored-by: Cursor <cursoragent@cursor.com>
Signed-off-by: Hrushikesh Patil <hrushi2900@gmail.com>1 parent[a224a86]commit 6dd7303

4 files changed

Lines changed: 15 additions & 3 deletions

## File tree

- src/guidellm
- backends/openai
- schemas/backends

- tests/unit
- backends/openai
- cli


| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`486` | `486` |
| |
`487` | `487` |
| |
`488` | `488` |
| |
`489` |
| `-` | |
`490` |
| `-` | |
| `489` | `+` | |
| `490` | `+` | |
`491` | `491` |
| |
`492` | `492` |
| |
`493` | `493` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`203` | `203` |
| |
`204` | `204` |
| |
`205` | `205` |
| |
`206` |
| `-` | |
| `206` | `+` | |
`207` | `207` |
| |
`208` | `208` |
| |
`209` | `209` |
| |
`210` | `210` |
| |
`211` | `211` |
| |
`212` | `212` |
| |
| `213` | `+` | |
`213` | `214` |
| |
| `215` | `+` | |
| `216` | `+` | |
| `217` | `+` | |
`214` | `218` |
| |
`215` | `219` |
| |
`216` | `220` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`257` | `257` |
| |
`258` | `258` |
| |
`259` | `259` |
| |
| `260` | `+` | |
`260` | `261` |
| |
`261` | `262` |
| |
`262` | `263` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`181` | `181` |
| |
`182` | `182` |
| |
`183` | `183` |
| |
| `184` | `+` | |
| `185` | `+` | |
`184` | `186` |
| |
`185` | `187` |
| |
`186` | `188` |
| |
| |||
`217` | `219` |
| |
`218` | `220` |
| |
`219` | `221` |
| |
| `222` | `+` | |
| `223` | `+` | |
`220` | `224` |
| |
`221` | `225` |
| |
`222` | `226` |
| |
| |||
`230` | `234` |
| |
`231` | `235` |
| |
`232` | `236` |
| |
| `237` | `+` | |
`233` | `238` |
| |
`234` | `239` |
| |
`235` | `240` |
| |
| |||
`255` | `260` |
| |
`256` | `261` |
| |
`257` | `262` |
| |
| `263` | `+` | |
| `264` | `+` | |
`258` | `265` |
| |
`259` | `266` |
| |
`260` | `267` |
| |
|

## 0 commit comments