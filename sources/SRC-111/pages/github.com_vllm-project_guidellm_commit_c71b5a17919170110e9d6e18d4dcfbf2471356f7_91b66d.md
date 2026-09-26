source: https://github.com/vllm-project/guidellm/commit/c71b5a17919170110e9d6e18d4dcfbf2471356f7

# Commit c71b5a1

authored

## Summary
Renames it as planned for 0.7
## Details
- Should have no other changes.
## Test Plan
Run the export commands
---
- [x] "I certify that all code in this PR is my own, except as noted below."
## Use of AI
- [x] Includes code generated or substantially modified by an AI agent
- [x] Includes tests generated or substantially modified by an AI agent
> NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`](

[https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md](https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md)) file. --- # git log commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Thu Jul 23 15:34:53 2026 -0400 Renamed `guidellm benchmark from-file` to `guidellm export` Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit](https://github.com/vllm-project/guidellm/commit/e4abdd0fe19af4501fb9cc347d86e612c2307789)`e4abdd0`[Author: Jared O'Connell <joconnel@redhat.com> Date: Thu Jul 23 15:46:14 2026 -0400 Fix linting Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>](https://github.com/vllm-project/guidellm/commit/3ef8020943861336c52650c78ce8575898c081d7)`3ef8020`1 parent[18e1447]commit c71b5a1

4 files changed

Lines changed: 15 additions & 39 deletions

## File tree

- docs/guides
- src/guidellm/cli
- benchmark


| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`1` |
| `-` | |
| `1` | `+` | |
`2` | `2` |
| |
`3` | `3` |
| |
`4` | `4` |
| |
| |||
`50` | `50` |
| |
`51` | `51` |
| |
`52` | `52` |
| |
`53` |
| `-` | |
| `53` | `+` | |
`54` | `54` |
| |
`55` | `55` |
| |
`56` | `56` |
| |
`57` |
| `-` | |
`58` |
| `-` | |
| `57` | `+` | |
`59` | `58` |
| |
`60` | `59` |
| |
`61` | `60` |
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
`14` |
| `-` | |
`15` |
| `-` | |
| `14` | `+` | |
| `15` | `+` | |
| `16` | `+` | |
| `17` | `+` | |
| `18` | `+` | |
| `19` | `+` | |
`16` | `20` |
| |
`17` | `21` |
| |
`18` | `22` |
| |
| |||
`27` | `31` |
| |
`28` | `32` |
| |
`29` | `33` |
| |
`30` |
| `-` | |
`31` | `34` |
| |
| `35` | `+` | |
`32` | `36` |
| |
`33` | `37` |
| |
`34` | `38` |
| |
| |||
`47` | `51` |
| |
`48` | `52` |
| |
`49` | `53` |
| |
`50` |
| `-` | |
| `54` | `+` |

This file was deleted.

Lines changed: 4 additions & 4 deletions

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`1` |
| `-` | |
| `1` | `+` | |
`2` | `2` |
| |
`3` | `3` |
| |
`4` | `4` |
| |
| |||
`11` | `11` |
| |
`12` | `12` |
| |
`13` | `13` |
| |
`14` |
| `-` | |
| `14` | `+` | |
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
`35` | `35` |
| |
`36` | `36` |
| |
`37` | `37` |
| |
`38` |
| `-` | |
| `38` | `+` | |
`39` | `39` |
|

## 0 commit comments