source: https://github.com/vllm-project/guidellm/commit/65b961a64addbda988dff14d5b6e6bb844fd76ef

# Commit 65b961a

committed

# Fix mock server Hugging Face tokenizer loading

## Context
Running the mock server with a Hugging Face tokenizer failed before the server started:
```bash
uv run guidellm mock-server --processor Qwen/Qwen2.5-0.5B-Instruct
```
The command raised `NotImplementedError` from `PreTrainedTokenizer.get_vocab()`. The mock-server handlers were loading the configured processor through the PreTrainedTokenizer base class.
This changes:
- Uses `AutoTokenizer` to initialize configured processors in mock-server handlers.
- Add an regression test covering mock-server initialization with tokenizer in MINIMAL_TOKENIZER_DIR
## Follow-up
The mock server still calls `AutoTokenizer.from_pretrained` once for each of its four handlers and produces four tokenizer objects. Reducing this duplication can be handled in a separate commit.
Signed-off-by: Tayo Ogunbiyi <eyitayoogunbiyi@gmail.com>
Generated-by: Claude Opus 51 parent[4601968]commit 65b961a

4 files changed

Lines changed: 29 additions & 8 deletions

## File tree

- src/guidellm/mock_server/handlers
- tests/unit/mock_server

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`21` | `21` |
| |
`22` | `22` |
| |
`23` | `23` |
| |
`24` |
| `-` | |
| `24` | `+` | |
`25` | `25` |
| |
`26` | `26` |
| |
`27` | `27` |
| |
| |||
`76` | `76` |
| |
`77` | `77` |
| |
`78` | `78` |
| |
`79` |
| `-` | |
| `79` | `+` | |
`80` | `80` |
| |
`81` | `81` |
| |
`82` | `82` |
| |
| |||
`189` | `189` |
| |
`190` | `190` |
| |
`191` | `191` |
| |
`192` |
| `-` | |
| `192` | `+` | |
| `193` | `+` | |
| `194` | `+` | |
`193` | `195` |
| |
`194` | `196` |
| |
`195` | `197` |
| |
| |||
`270` | `272` |
| |
`271` | `273` |
| |
`272` | `274` |
| |
`273` |
| `-` | |
| `275` | `+` | |
| `276` | `+` | |
| `277` | `+` | |
`274` | `278` |
| |
`275` | `279` |
| |
`276` | `280` |
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
| |||
`68` | `68` |
| |
`69` | `69` |
| |
`70` | `70` |
| |
`71` |
| `-` | |
| `71` | `+` | |
`72` | `72` |
| |
`73` | `73` |
| |
`74` | `74` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`20` | `20` |
| |
`21` | `21` |
| |
`22` | `22` |
| |
`23` |
| `-` | |
| `23` | `+` | |
`24` | `24` |
| |
`25` | `25` |
| |
`26` | `26` |
| |
| |||
`55` | `55` |
| |
`56` | `56` |
| |
`57` | `57` |
| |
`58` |
| `-` | |
| `58` | `+` | |
`59` | `59` |
| |
`60` | `60` |
| |
`61` | `61` |
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
| |||
`1173` | `1174` |
| |
`1174` | `1175` |
| |
`1175` | `1176` |
| |
| `1177` | `+` | |
| `1178` | `+` | |
| `1179` | `+` | |
| `1180` | `+` | |
| `1181` | `+` | |
| `1182` | `+` | |
| `1183` | `+` | |
| `1184` | `+` | |
| `1185` | `+` | |
| `1186` | `+` | |
| `1187` | `+` | |
| `1188` | `+` | |
| `1189` | `+` | |
| `1190` | `+` | |
| `1191` | `+` | |
| `1192` | `+` |

## 0 commit comments