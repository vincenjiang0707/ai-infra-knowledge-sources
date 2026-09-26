source: https://github.com/vllm-project/guidellm/commit/a314fe9683a4c99066e1a73bd8591449bb2bdfd1

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

Remove speculative defensive code
Document actually needed defensive code
Remove responses support for future consideration
And more.
Assisted-by: Cursor AI Grok 4.6
Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Copy file name to clipboardExpand all lines: docs/guides/datasets.md

+6-6Lines changed: 6 additions & 6 deletions

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

-`trace_synthetic`, `mooncake`, `weka`, `otel` — replay trace data with `--profile kind=replay`. Required field: `source`(a nested dataset config such as `json_file` or `huggingface`), see other supported sources for details. Optional: `timestamp_column`, `prompt_tokens_column`, `output_tokens_column`, `time_scale`, and other format-specific options. `weka` uses different column defaults (`t`, `in`, `out`). `otel` (aliases `opentelemetry`, `otel_trace`) reads GenAI span attributes and ISO-8601 timestamps. Replay sends recorded `gen_ai.input.messages` (`history=trace` by default). See [Trace File Formats](./trace_replay.md).

23

+

-`trace_synthetic`, `mooncake`, `weka`, `otel` — replay traces with `--profile kind=replay`. Required field: nested `source`pointing at another dataset kind, for example `source.kind=json_file,source.path=trace.jsonl` or `source.kind=huggingface,source.source=org/dataset`. Optional: `time_scale` and format-specific options. See [Trace File Formats](./trace_replay.md).

24

24

25

25

In addition, you can specify additional arguments to the dataset loading with the data argument `load_kwargs`:

26

26

@@ -190,7 +190,7 @@ GuideLLM supports various file formats for datasets, including text, CSV, JSON,

190

190

{"prompt": "What is your name?", "output_tokens_count": 3, "additional_column": "baz", "additional_column2": "qux"}

191

191

```

192

192

193

-

-**Trace files (`.jsonl`, `.json`, `.csv` or `.parquet` with a supported trace file format)**: Specialized files for replay. Used with `--profile kind=replay` to replay trace events using each row's timestamp and token lengths. Timestamps must be numbers expressed in seconds on a shared timeline with any consistent zero point, except `otel`, which parses ISO-8601 `start_time` values (and unix seconds, milliseconds, or nanoseconds) into epoch seconds. GuideLLM sorts them and converts them to offsets from the first event before scheduling. See [Trace Replay Benchmarking](../getting-started/benchmark.md#trace-replay-benchmarking).

193

+

-**Trace files (`.jsonl`, `.json`, `.csv` or `.parquet` with a supported trace file format)**: Specialized files for replay. Used with `--profile kind=replay` to replay trace events using each row's timestamp and token lengths. Timestamps must be numbers expressed in seconds on a shared timeline with any consistent zero point, except `otel`, which parses ISO-8601 `start_time` values (and HuggingFace-decoded `datetime` objects) into epoch seconds. GuideLLM sorts them and converts them to offsets from the first event before scheduling. See [Trace Replay Benchmarking](../getting-started/benchmark.md#trace-replay-benchmarking).

`otel` uses the same nested `source` field. Token counts come from span attributes rather than top-level columns. Hugging Face is the fastest way to start (`samples` counts conversations, not spans):

220

+

`otel` uses the same nested `source` field. Token counts come from span attributes rather than top-level columns. Hugging Face is the fastest way to start:

Defaults are recorded `gen_ai.input.messages` and `history=trace` (each span's full input, `history_context=new`). Pass `history=runtime` to send only new messages and attach live completions through the DAG. Spans without `gen_ai.input.messages` should use `trace_synthetic`. Local JSONL uses `source.kind=json_file,source.path=...` with the same `history` switch. See [Trace File Formats](./trace_replay.md#otel).

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

-`raw_messages_column`: Chat-completions messages for the current turn (`[{role, content}, …]`; defaults: `messages`, `chat_messages`). `/v1/chat/completions` sends them as-is. `/v1/responses` converts them to `input` items (`input_text`, `function_call`, `function_call_output`).

432

+

-`raw_messages_column`: Chat-completions messages for the current turn (`[{role, content}, …]`; defaults: `messages`, `chat_messages`). `/v1/chat/completions` sends them as-is. OTEL replay is chat-completions only for now.

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

**3. OTEL traces** -- tool-call turns come from the file: assistant `tool_call` parts on span output, or `gen_ai.response.finish_reasons` of `tool_calls` / `tool_call` / `tool_use` / `function_call`. Schemas come from `gen_ai.tool.definitions` when present, otherwise the default synthetic tool. Recorded tool result strings are injected and rebound to live `tool_call_id`s. Pass `tool_choice=required` (default) or `tool_choice=auto` on `--data kind=otel`. Recorded messages are chat-completions dicts; `/v1/chat/completions`(the default) sends them as-is and `/v1/responses` converts them to `input` items. `/v1/completions` has no tool loop. Backend `tool_call_missing_behavior` is unchanged. See [Trace replay](trace_replay.md#otel).

159

+

**3. OTEL traces** -- tool-call turns come from the file: assistant `tool_call` parts on span output, or `gen_ai.response.finish_reasons` of `tool_calls` / `tool_call` / `tool_use` / `function_call`. Schemas come from `gen_ai.tool.definitions` when present, otherwise the default synthetic tool. Recorded tool result strings are injected and rebound to live `tool_call_id`s. Pass `tool_choice=required` (default) or `tool_choice=auto` on `--data kind=otel`. Recorded messages are chat-completions dicts; replay is `/v1/chat/completions`only for now. `/v1/completions` has no tool loop. Backend `tool_call_missing_behavior` is unchanged. See [Trace replay](trace_replay.md#otel).

160

160

161

161

**4. Datasets with a tools column** -- datasets that already contain tool definitions (e.g. `madroid/glaive-function-calling-openai`) work directly. The column mapper auto-detects columns named `tools`, `functions`, or `tool_definitions`:

Copy file name to clipboardExpand all lines: docs/guides/trace_replay.md

+17-13Lines changed: 17 additions & 13 deletions

Display the source diff

Display the rich diff

Original file line number

Diff line number

Diff line change

@@ -11,7 +11,7 @@ These are passed to the `--data` argument as `kind=format`:

11

11

-`trace_synthetic`: A trace format that does the bare minimum needed to complete a fully functioning trace replay benchmark with synthetic prompt generation

12

12

-`mooncake`: The trace format used by the serving platform *Mooncake*, as defined in [https://doi.org/10.48550/arXiv.2407.00079](https://doi.org/10.48550/arXiv.2407.00079)

13

13

-`weka`: The trace format used by WEKA's *Augmented Memory Grid*, as specified [in the original research repository](https://github.com/callanjfox/agentic-coding-analysis/blob/master/docs/TRACE_FORMAT.md)

14

-

-`otel` (aliases`opentelemetry`, `otel_trace`): OpenTelemetry GenAI spans. GuideLLM keeps successful LLM spans and replays each `trace_id` as one conversation. It sends recorded `gen_ai.input.messages` with each span's full input (`history=trace`) unless `history=runtime` is set.

14

+

-`otel` (alias`opentelemetry`): OpenTelemetry GenAI spans. GuideLLM keeps successful LLM spans and replays each `trace_id` as one conversation. It sends recorded `gen_ai.input.messages` with each span's full input (`history=trace`) unless `history=runtime` is set.

Spans without `gen_ai.input.messages` cannot be replayed as OTEL. Flatten token-count-only dumps to `kind=trace_synthetic` instead.

154

158

155

-

Replay against `/v1/chat/completions` (the backend default). `raw_messages_column` is always chat-completions format: that handler sends it as a `messages` array. `/v1/responses` converts the same column into Responses `input` items. `/v1/completions` is a prompt string with no tool loop and does not read `raw_messages_column`.

159

+

Replay against `/v1/chat/completions` (the backend default). OTEL replay is chat-completions only for now: `raw_messages_column` is always chat-completions format and that handler sends it as a `messages` array. `/v1/completions` is a prompt string with no tool loop and does not read `raw_messages_column`.

156

160

157

161

Recorded tool loops are pre-split onto GuideLLM's client tool-call pipeline. An LLM span whose output messages contain `tool_calls` (or `gen_ai.response.finish_reasons` of `tool_calls` / `tool_call` / `tool_use` / `function_call`) becomes `client_tool_call`. The next span is consumed as `tool_response_injection` when its new messages after `input[i] + output[i]` are only `role=tool` results. Recorded result strings are rebound to **live**`tool_call_id`s by the chat handler. `gen_ai.tool.definitions` supplies `tools_column` on those turns (otherwise the default synthetic tool is used); definitions alone do not classify a turn. Injection parents always use `history_context=full`, including `history=trace`. Missing-tool policy stays `--backend tool_call_missing_behavior=...`.

158

162

159

163

If the next span cannot be parsed as tool results, a placeholder injection is synthesized (using a following `execute_tool` span's result when present) and that next span is still replayed.

160

164

161

165

Completed request stats merge response usage over the request's expected token counts, so a dedicated expected-vs-actual MAE is not reported. Compare `request.input_metrics` / `output_metrics` (span counts) with response usage before that merge if you need the deviation.

162

166

163

-

ISO-8601 `start_time` values, unix seconds, milliseconds, and nanoseconds are converted to epoch seconds before scheduling. Token counts are read from span `attributes`, trying current GenAI names first and then the deprecated aliases. OTel `parts` (`text`, `tool_call`, `tool_call_response`) are converted to OpenAI chat dicts.

167

+

ISO-8601 `start_time` values (naive, `Z`, or offset) and HuggingFace-decoded `datetime` objects are converted to epoch seconds before scheduling. Token counts are read from span `attributes`, trying current GenAI names first and then the deprecated aliases. OTel `parts` (`text`, `tool_call`, `tool_call_response`) are converted to OpenAI chat dicts.

@@ -172,16 +176,16 @@ ISO-8601 `start_time` values, unix seconds, milliseconds, and nanoseconds are co

172

176

|`history`|`trace`|`trace` resends each span's full input; `runtime` sends only new messages with DAG history |

173

177

|`tool_choice`|`required`|`required` or `auto` on client tool-call turns. Pair `auto` with `tool_call_missing_behavior=ignore_continue`|

174

178

175

-

Start from Hugging Face. `samples` counts conversations (`trace_id`s), not spans. IBM traces have 30–50 LLM calls each, so keep `samples` small at first.

179

+

Start from Hugging Face. IBM traces have 30–50 LLM calls each, so `--constraint kind=max_requests` is a useful bound on first runs.

176

180

177

181

**Default (`history=trace`):** send each span's recorded messages in full. Later turns wait on the DAG but use `history_context=new`, so live completions are not spliced into the next prompt.

**Recorded messages with DAG history (`history=runtime`):** send only the new messages; prior turns come from live completions (`history_context=full`). Requires each span's input to continue the previous span's input plus output.

## 0 commit comments