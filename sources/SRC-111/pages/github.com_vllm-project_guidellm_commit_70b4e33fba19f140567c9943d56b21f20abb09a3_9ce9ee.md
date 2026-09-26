source: https://github.com/vllm-project/guidellm/commit/70b4e33fba19f140567c9943d56b21f20abb09a3

# Commit 70b4e33

committed

Isolate tokenizer startup regression in the server fixture

Use the existing subprocess fixture and health endpoint instead of constructing MockServer in the pytest process. This prevents forked server processes from inheriting a registered Sanic app and failing with a duplicate app name.
Generated-by: OpenAI Codex
Signed-off-by: Tayo Ogunbiyi <eyitayoogunbiyi@gmail.com>1 parent[355a2a8]commit 70b4e33

1 file changed

Lines changed: 8 additions & 8 deletions

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`1152` | `1152` |
| |
`1153` | `1153` |
| |
`1154` | `1154` |
| |
`1155` |
| `-` | |
`1156` |
| `-` | |
| `1155` | `+` | |
| `1156` | `+` | |
| `1157` | `+` | |
`1157` | `1158` |
| |
`1158` | `1159` |
| |
`1159` | `1160` |
| |
`1160` |
| `-` | |
| `1161` | `+` | |
`1161` | `1162` |
| |
`1162` |
| `-` | |
| `1163` | `+` | |
| `1164` | `+` | |
`1163` | `1165` |
| |
`1164` |
| `-` | |
`1165` |
| `-` | |
`1166` |
| `-` | |
`1167` |
| `-` | |
| `1166` | `+` | |
| `1167` | `+` | |
`1168` | `1168` |
| |
`1169` | `1169` |
| |
`1170` | `1170` |
| |
|

## 0 commit comments