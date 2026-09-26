source: https://github.com/vllm-project/guidellm/commit/99b5247aaa37b153ca889e493f188d75517bac98

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

Currently minimal support. No tool call. Incomplete hash support.
Generated-by: Cursor AI Grok 4.6
Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Copy file name to clipboardExpand all lines: docs/guides/datasets.md

+11-2Lines changed: 11 additions & 2 deletions

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

-`trace_synthetic`, `mooncake`, `weka`— replay trace data with `--profile kind=replay`. Required field: `source` (a nested dataset config such as `json_file` or `huggingface`), see other supported sources for details. Optional: `timestamp_column`, `prompt_tokens_column`, `output_tokens_column`, `time_scale`, and other format-specific options. `weka` uses different column defaults (`t`, `in`, `out`). See [Trace File Formats](./trace_replay.md).

23

+

-`trace_synthetic`, `mooncake`, `weka`, `otel`— replay trace data with `--profile kind=replay`. Required field: `source` (a nested dataset config such as `json_file` or `huggingface`), see other supported sources for details. Optional: `timestamp_column`, `prompt_tokens_column`, `output_tokens_column`, `time_scale`, and other format-specific options. `weka` uses different column defaults (`t`, `in`, `out`). `otel` (aliases `opentelemetry`, `otel_trace`) reads GenAI span attributes and ISO-8601 timestamps. See [Trace File Formats](./trace_replay.md).

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

-**Trace files (`.jsonl`, `.json`, `.csv` or `.parquet` with a supported trace file format)**: Specialized files for replay. Used with `--profile kind=replay` to replay trace events using each row's timestamp and token lengths. Timestamps must be numbers expressed in seconds on a shared timeline with any consistent zero point; GuideLLM sorts them and converts them to offsets from the first event before scheduling. Date strings are not parsed yet, so provide timestamps as numbers. See [Trace Replay Benchmarking](../getting-started/benchmark.md#trace-replay-benchmarking).

193

+

-**Trace files (`.jsonl`, `.json`, `.csv` or `.parquet` with a supported trace file format)**: Specialized files for replay. Used with `--profile kind=replay` to replay trace events using each row's timestamp and token lengths. Timestamps must be numbers expressed in seconds on a shared timeline with any consistent zero point, except `otel`, which parses ISO-8601 `start_time` values (and unix seconds, milliseconds, or nanoseconds) into epoch seconds. GuideLLM sorts them and converts them to offsets from the first event before scheduling. See [Trace Replay Benchmarking](../getting-started/benchmark.md#trace-replay-benchmarking).

For replay, `time_scale` on `--data` is a time scale for the intervals between trace events after wait and pack caps. Wait caps (`max_wait`, `max_session_wait`, `min_concurrent_sessions`) are applied in original trace seconds before `time_scale`. The replay profile also accepts a scheduler-side `time_scale` on `--profile kind=replay`. Use `--data-loader kind=pytorch,samples=1000` to limit how many trace rows are loaded and replayed. Use `--constraint kind=max_requests,count=<n>` only as a runtime completion constraint; it does not limit the trace rows loaded from the file. `--constraint kind=max_duration,seconds=<n>` also cancels in-flight waits, including replay sleeps.

221

230

222

231

-**JSON files (`.json`)**: Where the entire dataset is represented as a JSON array of objects nested under a specific key. To surface the correct key to use, a `--data-column-mapper` argument must be passed in of `"field": "NAME"` for where the array exists. The objects should include `prompt` or other common names for the prompt which will be used as the prompt column. Additional fields can be included based on the previously mentioned aliases for the `--data-column-mapper` argument.

Copy file name to clipboardExpand all lines: docs/guides/trace_replay.md

+36Lines changed: 36 additions & 0 deletions

Display the source diff

Display the rich diff

Original file line number

Diff line number

Diff line change

@@ -11,6 +11,7 @@ These are passed to the `--data` argument as `kind=format`:

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

+

-`otel` (aliases `opentelemetry`, `otel_trace`): OpenTelemetry GenAI spans. GuideLLM keeps successful LLM spans, flattens usage token attributes and timestamps, and replays each `trace_id` as one conversation with synthetic prompts.

14

15

15

16

## Loading Trace Data

16

17

@@ -121,3 +122,38 @@ Modified defaults:

121

122

|`timestamp_column`| "t" |

122

123

|`prompt_tokens_column`| "in" |

123

124

|`output_tokens_column`| "out" |

125

+

126

+

### `otel`

127

+

128

+

OpenTelemetry GenAI traces are normalized into the same replay rows as other trace formats (`timestamp`, `input_length`, `output_length`). Two file layouts are accepted:

129

+

130

+

-**Session-per-line**: each JSONL row is `{ "trace_id": ..., "spans": [ ... ] }`

131

+

-**Span-per-line**: each JSONL row is one span; adjacent rows with the same `trace_id` become one conversation. Grouping is streaming and consecutive only, so an interleaved `a, b, a` dump is three conversations, not two. Published replay corpora write each `trace_id` contiguously; live collector exports of concurrent traces may not.

132

+

133

+

Only successful LLM spans are replayed (`gen_ai.operation.name` of `chat`, `generate`, or `text_completion`, or any span that already has usage token attributes). `invoke_agent`, tool-execution, and failed spans (`status.code` error) are dropped. Real `gen_ai.input.messages` are not sent; prompts are synthesized from token counts. Within a conversation, later turns reuse the earlier turn's synthetic tokens as a growing prefix.

134

+

135

+

ISO-8601 `start_time` values, unix seconds, milliseconds, and nanoseconds are converted to epoch seconds before scheduling. Token counts are read from span `attributes`, trying current GenAI names first and then the deprecated aliases.

|`spans_column`| "spans" | Column name for nested span lists in session-per-line files |

140

+

|`trace_id_column`| "trace_id" | Column used to group span-per-line files into conversations |

141

+

|`span_timestamp_field`| "start_time" | Span field holding the request start time |

142

+

|`input_tokens_attributes`|`["gen_ai.usage.input_tokens", "gen_ai.usage.prompt_tokens"]`| Attribute keys tried in order for prompt token counts |

143

+

|`output_tokens_attributes`|`["gen_ai.usage.output_tokens", "gen_ai.usage.completion_tokens"]`| Attribute keys tried in order for output token counts |

Related corpora: [DiscoPosse/agent-llm-traces](https://huggingface.co/datasets/DiscoPosse/agent-llm-traces) (Exgentic v1 schema) and [lenadan/otel-test-snippet-jsonl](https://huggingface.co/datasets/lenadan/otel-test-snippet-jsonl) (small span-per-line snippet). [ibm-research/codex_swebenchpro_traces_Otel](https://huggingface.co/datasets/ibm-research/codex_swebenchpro_traces_Otel) omits usage token attributes and is not usable for token-count replay.

## 0 commit comments