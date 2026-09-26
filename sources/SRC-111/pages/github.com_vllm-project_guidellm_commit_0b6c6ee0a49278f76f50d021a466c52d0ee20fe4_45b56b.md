source: https://github.com/vllm-project/guidellm/commit/0b6c6ee0a49278f76f50d021a466c52d0ee20fe4

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

Copy file name to clipboardExpand all lines: docs/guides/datasets.md

+2-2Lines changed: 2 additions & 2 deletions

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

-`trace_synthetic`, `mooncake`, `weka`, `otel` — replay trace data with `--profile kind=replay`. Required field: `source` (a nested dataset config such as `json_file` or `huggingface`), see other supported sources for details. Optional: `timestamp_column`, `prompt_tokens_column`, `output_tokens_column`, `time_scale`, and other format-specific options. `weka` uses different column defaults (`t`, `in`, `out`). `otel` (aliases `opentelemetry`, `otel_trace`) reads GenAI span attributes and ISO-8601 timestamps. Default replay sends recorded messages (`content=raw`, `history=trace`); pass `content=synthetic` when the corpus has token counts but no `gen_ai.input.messages`. See [Trace File Formats](./trace_replay.md).

23

+

-`trace_synthetic`, `mooncake`, `weka`, `otel` — replay trace data with `--profile kind=replay`. Required field: `source` (a nested dataset config such as `json_file` or `huggingface`), see other supported sources for details. Optional: `timestamp_column`, `prompt_tokens_column`, `output_tokens_column`, `time_scale`, and other format-specific options. `weka` uses different column defaults (`t`, `in`, `out`). `otel` (aliases `opentelemetry`, `otel_trace`) reads GenAI span attributes and ISO-8601 timestamps. Replay sends recorded `gen_ai.input.messages` (`history=trace` by default). See [Trace File Formats](./trace_replay.md).

24

24

25

25

In addition, you can specify additional arguments to the dataset loading with the data argument `load_kwargs`:

26

26

@@ -227,7 +227,7 @@ GuideLLM supports various file formats for datasets, including text, CSV, JSON,

227

227

--data-loader kind=pytorch,samples=2

228

228

```

229

229

230

-

Defaults are `content=raw` (recorded `gen_ai.input.messages`) and `history=trace` (each span's full input, `history_context=new`). Pass `history=runtime` to send only new messages and attach live completions through the DAG. Pass `content=synthetic` to build faker prompts from token counts (required when the corpus has no recorded messages). Local JSONL uses `source.kind=json_file,source.path=...` with the same switches. See [Trace File Formats](./trace_replay.md#otel).

230

+

Defaults are recorded `gen_ai.input.messages` and `history=trace` (each span's full input, `history_context=new`). Pass `history=runtime` to send only new messages and attach live completions through the DAG. Spans without `gen_ai.input.messages` should use `trace_synthetic`. Local JSONL uses `source.kind=json_file,source.path=...` with the same `history` switch. See [Trace File Formats](./trace_replay.md#otel).

231

231

232

232

For replay, `time_scale` on `--data` is a time scale for the intervals between trace events after wait and pack caps. Wait caps (`max_wait`, `max_session_wait`, `min_concurrent_sessions`) are applied in original trace seconds before `time_scale`. The replay profile also accepts a scheduler-side `time_scale` on `--profile kind=replay`. Use `--data-loader kind=pytorch,samples=1000` to limit how many trace rows are loaded and replayed. Use `--constraint kind=max_requests,count=<n>` only as a runtime completion constraint; it does not limit the trace rows loaded from the file. `--constraint kind=max_duration,seconds=<n>` also cancels in-flight waits, including replay sleeps.

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

**3. OTEL traces** -- tool-call turns come from the file: assistant `tool_call` parts on span output, or (when messages are missing) `gen_ai.response.finish_reasons`/ a following `execute_tool` span. Schemas come from `gen_ai.tool.definitions` when present, otherwise the default synthetic tool. Recorded tool result strings are injected and rebound to live `tool_call_id`s. Pass `tool_choice=required` (default) or `tool_choice=auto` on `--data kind=otel`. Recorded messages are chat-completions dicts; `/v1/chat/completions` (the default) sends them as-is and `/v1/responses` converts them to `input` items. `/v1/completions` has no tool loop. Backend `tool_call_missing_behavior` is unchanged. See [Trace replay](trace_replay.md#otel).

159

+

**3. OTEL traces** -- tool-call turns come from the file: assistant `tool_call` parts on span output, or `gen_ai.response.finish_reasons`of `tool_calls` / `tool_call` / `tool_use` / `function_call`. Schemas come from `gen_ai.tool.definitions` when present, otherwise the default synthetic tool. Recorded tool result strings are injected and rebound to live `tool_call_id`s. Pass `tool_choice=required` (default) or `tool_choice=auto` on `--data kind=otel`. Recorded messages are chat-completions dicts; `/v1/chat/completions` (the default) sends them as-is and `/v1/responses` converts them to `input` items. `/v1/completions` has no tool loop. Backend `tool_call_missing_behavior` is unchanged. See [Trace replay](trace_replay.md#otel).

160

160

161

161

**4. Datasets with a tools column** -- datasets that already contain tool definitions (e.g. `madroid/glaive-function-calling-openai`) work directly. The column mapper auto-detects columns named `tools`, `functions`, or `tool_definitions`:

## 0 commit comments