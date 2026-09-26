source: https://github.com/vllm-project/guidellm/commit/85b1f47eec27095563b5709e1ddd2c3f838b7422

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

This ensures that running an OTeL trace with incompatible message formats fails with a helpful message
Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Copy file name to clipboardExpand all lines: docs/guides/datasets.md

+1-1Lines changed: 1 addition & 1 deletion

Display the source diff

Display the rich diff

Original file line number

Diff line number

Diff line change

@@ -429,7 +429,7 @@ When your dataset uses non-standard column names, you can use `--data-column-map

429

429

**Supported column types:**

430

430

431

431

-`text_column`: The main prompt text (defaults: `prompt`, `instruction`, `question`, `input`, `context`, `content`, `text`)

432

-

-`raw_messages_column`: Chat-completions messages for the current turn (`[{role, content}, …]`; defaults: `messages`, `chat_messages`). `/v1/chat/completions` sends them as-is. OTEL replay is chat-completions only for now.

432

+

-`raw_messages_column`: Chat-completions messages for the current turn (`[{role, content}, …]`; defaults: `messages`, `chat_messages`). `/v1/chat/completions` sends them as-is. Other request formats abort if they cannot build `prompt`/`input` from these messages.

433

433

-`prefix_column`: System prompt or prefix (defaults: `system_prompt`, `system`, `prefix`)

Copy file name to clipboardExpand all lines: docs/guides/tool_calling.md

+1-1Lines changed: 1 addition & 1 deletion

Display the source diff

Display the rich diff

Original file line number

Diff line number

Diff line change

@@ -156,7 +156,7 @@ guidellm run \

156

156

157

157

When `tools` is omitted, the same built-in placeholder tool as synthetic data is used.

158

158

159

-

**3. OTEL traces** -- tool-call turns come from the file: assistant `tool_call` parts on span output, or `gen_ai.response.finish_reasons` of `tool_calls` / `tool_call` / `tool_use` / `function_call`. Schemas come from `gen_ai.tool.definitions` when present, otherwise the default synthetic tool. Recorded tool result strings are injected and rebound to live `tool_call_id`s. Pass `tool_choice=required` (default) or `tool_choice=auto` on `--data kind=otel`. Recorded messages are chat-completions dicts; replay is`/v1/chat/completions` only for now. Backend `tool_call_missing_behavior` is unchanged. See [Trace replay](trace_replay.md#otel).

159

+

**3. OTEL traces** -- tool-call turns come from the file: assistant `tool_call` parts on span output, or `gen_ai.response.finish_reasons` of `tool_calls` / `tool_call` / `tool_use` / `function_call`. Schemas come from `gen_ai.tool.definitions` when present, otherwise the default synthetic tool. Recorded tool result strings are injected and rebound to live `tool_call_id`s. Pass `tool_choice=required` (default) or `tool_choice=auto` on `--data kind=otel`. Recorded messages are chat-completions dicts; replay against`/v1/chat/completions`. Other request formats abort because they cannot build `prompt`/`input` from `raw_messages_column`. Backend `tool_call_missing_behavior` is unchanged. See [Trace replay](trace_replay.md#otel).

160

160

161

161

**4. Datasets with a tools column** -- datasets that already contain tool definitions (e.g. `madroid/glaive-function-calling-openai`) work directly. The column mapper auto-detects columns named `tools`, `functions`, or `tool_definitions`:

Spans without `gen_ai.input.messages` cannot be replayed as OTEL. Flatten token-count-only dumps to `kind=trace_synthetic` instead.

158

158

159

-

Replay against `/v1/chat/completions` (the backend default). OTEL replay is chat-completions only for now:`raw_messages_column` is always chat-completions format and that handler sends it as a `messages` array. `/v1/completions`is a prompt string with no tool loop and does not read `raw_messages_column`.

159

+

Replay against `/v1/chat/completions` (the backend default). OTEL stores chat-completions message dicts in`raw_messages_column`. That handler sends them as a `messages` array. `/v1/completions`and `/v1/responses` do not read that column; they abort with a missing `prompt` or `input` error rather than posting an empty body.

160

160

161

161

Recorded tool loops are pre-split onto GuideLLM's client tool-call pipeline. An LLM span whose output messages contain `tool_calls` (or `gen_ai.response.finish_reasons` of `tool_calls` / `tool_call` / `tool_use` / `function_call`) becomes `client_tool_call`. The next span is consumed as `tool_response_injection` when its new messages after `input[i] + output[i]` are only `role=tool` results. Recorded result strings are rebound to **live**`tool_call_id`s by the chat handler. `gen_ai.tool.definitions` supplies `tools_column` on those turns (otherwise the default synthetic tool is used); definitions alone do not classify a turn. Injection parents always use `history_context=full`, including `history=trace`. Missing-tool policy stays `--backend tool_call_missing_behavior=...`.

## 0 commit comments