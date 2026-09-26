source: https://github.com/vllm-project/guidellm/commit/f9cde77b686cb49766b237f90aeaf28ca9d73780

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

Properly utilizes the content from the OTeL traces.
Also adds multiple settings to change how GuideLLM uses the OTeL trace.
Generated-by: Cursor AI Grok 4.6
Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Copy file name to clipboardExpand all lines: docs/guides/datasets.md

+7-3Lines changed: 7 additions & 3 deletions

Display the source diff

Display the rich diff

Original file line number

Diff line number

Diff line change

@@ -20,7 +20,7 @@ The following arguments configure datasets and their processing:

20

20

-`synthetic_text` — generates synthetic prompts on the fly. Required field: `prompt_tokens`. Optional: `output_tokens`, `turns`, `prefix_tokens`, `prefix_count`, `prefix_buckets`, and distribution controls (`prompt_tokens_stdev`, `output_tokens_stdev`, etc.).

21

21

-`huggingface` (alias `hf`) — loads from HuggingFace Hub or a local directory/file. Required field: `source` (dataset ID or path). Pass dataset loading arguments (for example `split`, `name`) via `load_kwargs`.

22

22

-`json_file`, `csv_file`, `text_file`, `parquet_file`, `arrow_file`, `hdf5_file`, `db_file`, `tar_file` — loads from a local file. Required field: `path`.

23

-

-`trace_synthetic`, `mooncake`, `weka`, `otel` — replay trace data with `--profile kind=replay`. Required field: `source` (a nested dataset config such as `json_file` or `huggingface`), see other supported sources for details. Optional: `timestamp_column`, `prompt_tokens_column`, `output_tokens_column`, `time_scale`, and other format-specific options. `weka` uses different column defaults (`t`, `in`, `out`). `otel` (aliases `opentelemetry`, `otel_trace`) reads GenAI span attributes and ISO-8601 timestamps. See [Trace File Formats](./trace_replay.md).

23

+

-`trace_synthetic`, `mooncake`, `weka`, `otel` — replay trace data with `--profile kind=replay`. Required field: `source` (a nested dataset config such as `json_file` or `huggingface`), see other supported sources for details. Optional: `timestamp_column`, `prompt_tokens_column`, `output_tokens_column`, `time_scale`, and other format-specific options. `weka` uses different column defaults (`t`, `in`, `out`). `otel` (aliases `opentelemetry`, `otel_trace`) reads GenAI span attributes and ISO-8601 timestamps. Default replay sends recorded messages (`content=raw`, `history=trace`); pass `content=synthetic` when the corpus has token counts but no `gen_ai.input.messages`. See [Trace File Formats](./trace_replay.md).

24

24

25

25

In addition, you can specify additional arguments to the dataset loading with the data argument `load_kwargs`:

26

26

@@ -217,15 +217,18 @@ GuideLLM supports various file formats for datasets, including text, CSV, JSON,

`otel` uses the same nested `source` field. Token counts come from span attributes rather than top-level columns:

220

+

`otel` uses the same nested `source` field. Token counts come from span attributes rather than top-level columns. Hugging Face is the fastest way to start (`samples` counts conversations, not spans):

Defaults are `content=raw` (recorded `gen_ai.input.messages`) and `history=trace` (each span's full input, `history_context=new`). Pass `history=runtime` to send only new messages and attach live completions through the DAG. Pass `content=synthetic` to build faker prompts from token counts (required when the corpus has no recorded messages). Local JSONL uses `source.kind=json_file,source.path=...` with the same switches. See [Trace File Formats](./trace_replay.md#otel).

231

+

229

232

For replay, `time_scale` on `--data` is a time scale for the intervals between trace events after wait and pack caps. Wait caps (`max_wait`, `max_session_wait`, `min_concurrent_sessions`) are applied in original trace seconds before `time_scale`. The replay profile also accepts a scheduler-side `time_scale` on `--profile kind=replay`. Use `--data-loader kind=pytorch,samples=1000` to limit how many trace rows are loaded and replayed. Use `--constraint kind=max_requests,count=<n>` only as a runtime completion constraint; it does not limit the trace rows loaded from the file. `--constraint kind=max_duration,seconds=<n>` also cancels in-flight waits, including replay sleeps.

230

233

231

234

-**JSON files (`.json`)**: Where the entire dataset is represented as a JSON array of objects nested under a specific key. To surface the correct key to use, a `--data-column-mapper` argument must be passed in of `"field": "NAME"` for where the array exists. The objects should include `prompt` or other common names for the prompt which will be used as the prompt column. Additional fields can be included based on the previously mentioned aliases for the `--data-column-mapper` argument.

@@ -426,6 +429,7 @@ When your dataset uses non-standard column names, you can use `--data-column-map

426

429

**Supported column types:**

427

430

428

431

-`text_column`: The main prompt text (defaults: `prompt`, `instruction`, `question`, `input`, `context`, `content`, `text`)

432

+

-`raw_messages_column`: Chat-completions messages for the current turn (`[{role, content}, …]`; defaults: `messages`, `chat_messages`). `/v1/chat/completions` sends them as-is. `/v1/responses` converts them to `input` items (`input_text`, `function_call`, `function_call_output`).

429

433

-`prefix_column`: System prompt or prefix (defaults: `system_prompt`, `system`, `prefix`)

Copy file name to clipboardExpand all lines: docs/guides/tool_calling.md

+3-1Lines changed: 3 additions & 1 deletion

Display the source diff

Display the rich diff

Original file line number

Diff line number

Diff line change

@@ -156,7 +156,9 @@ guidellm run \

156

156

157

157

When `tools` is omitted, the same built-in placeholder tool as synthetic data is used.

158

158

159

-

**3. Datasets with a tools column** -- datasets that already contain tool definitions (e.g. `madroid/glaive-function-calling-openai`) work directly. The column mapper auto-detects columns named `tools`, `functions`, or `tool_definitions`:

159

+

**3. OTEL traces** -- tool-call turns come from the file: assistant `tool_call` parts on span output, or (when messages are missing) `gen_ai.response.finish_reasons` / a following `execute_tool` span. Schemas come from `gen_ai.tool.definitions` when present, otherwise the default synthetic tool. Recorded tool result strings are injected and rebound to live `tool_call_id`s. Pass `tool_choice=required` (default) or `tool_choice=auto` on `--data kind=otel`. Recorded messages are chat-completions dicts; `/v1/chat/completions` (the default) sends them as-is and `/v1/responses` converts them to `input` items. `/v1/completions` has no tool loop. Backend `tool_call_missing_behavior` is unchanged. See [Trace replay](trace_replay.md#otel).

160

+

161

+

**4. Datasets with a tools column** -- datasets that already contain tool definitions (e.g. `madroid/glaive-function-calling-openai`) work directly. The column mapper auto-detects columns named `tools`, `functions`, or `tool_definitions`:

## 0 commit comments