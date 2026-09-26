source: https://github.com/vllm-project/guidellm/pull/1153

# OTeL trace support - #1153

[jaredoconnell](https://github.com/jaredoconnell)wants to merge 8 commits into

[OTeL trace support](https://github.com#top)#1153[jaredoconnell](https://github.com/jaredoconnell) wants to merge 8 commits into

[OTeL trace support](https://github.com#top)#1153

[jaredoconnell](https://github.com/jaredoconnell)wants to merge 8 commits into

## Conversation


**reviewed**

[sjmonson](https://github.com/sjmonson)Sep 16, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Not finished reviewing, but here are a couple small things to start.

[src/guidellm/schemas/data/deserializers/trace_otel.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-6c266d6793e590d8da3ca40b579757e772c06933cba8419b6e5c31fd367afb62)Outdated

[src/guidellm/scheduler/dag.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-71854c4e28142c71460d1b15d57935c6e8557a60e37f5b0344d066fa9a5e7f3c)Outdated

[src/guidellm/scheduler/dag.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-71854c4e28142c71460d1b15d57935c6e8557a60e37f5b0344d066fa9a5e7f3c)Outdated


**requested changes**

[sjmonson](https://github.com/sjmonson)Sep 17, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Well with the most basic test it seems to work. A lot of the conditional paths in `trace_otel.py`

seem unlikely to ever occur but such is true for most parsing code, especially when its all written by AI. Few more nits and I would like to see the chat completions -> responses code moved outside this PR to give it a little more time in the oven.

[src/guidellm/data/deserializers/trace_otel.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-efa6d0d8c8a7c9b1e66950750db365b5a3044948f592544dae0217dd0cab4013)Outdated

[src/guidellm/data/deserializers/trace_otel.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-efa6d0d8c8a7c9b1e66950750db365b5a3044948f592544dae0217dd0cab4013)

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/data/deserializers/trace_otel.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-efa6d0d8c8a7c9b1e66950750db365b5a3044948f592544dae0217dd0cab4013)

| def _raw_turn_messages( | ||
| self, | ||
| turn_idx: int, | ||
| turn: dict[str, Any], | ||
| rows: list[dict[str, Any]], | ||
| ) -> list[dict[str, Any]]: | ||
| attributes = span_attributes(turn["span"]) | ||
| input_messages = parse_gen_ai_messages(attributes.get("gen_ai.input.messages")) | ||
| if not input_messages: | ||
| raise InvalidRowError( | ||
| "OTEL format: span missing gen_ai.input.messages. " | ||
| "Use kind=trace_synthetic for token-count-only traces." | ||
| ) | ||
| if self.config.history != "runtime" or turn_idx == 0: | ||
| return input_messages | ||
| return self._runtime_raw_delta(input_messages, rows[turn_idx - 1]) |

There was a problem hiding this comment.

When we initial discussed this I assumed that the `raw`

column would be the entire request and not just the messages/content section. Oh well, I guess not as reusable as I thought.

There was a problem hiding this comment.

Yeah, that's why I mentioned that to do a pure raw column we'd need another column to describe what part is raw. I don't think it makes sense to go full `raw`

for this.

[docs/guides/trace_replay.md](https://github.com/vllm-project/guidellm/pull/1153/files#diff-d1919f3fd587a605342ebbc06efb54fb7f3c1c0c0c94750935e927f956a242a5)

| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --profile kind=replay \ | ||
| --data kind=trace_synthetic,source.kind=json_file,source.path=replay.jsonl,time_scale=1.0 | ||
| ``` | ||
|
|
||
| **WEKA dataset from `huggingface`:** | ||
|
|
||
| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --profile kind=replay \ | ||
| --data kind=weka,source.kind=huggingface,source.source=semianalysisai/cc-traces-weka-no-subagents-051226,load_kwargs.split=train | ||
| ``` | ||
|
|
||
| **Mooncake dataset from `huggingface`** | ||
|
|
||
| ```bash | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --profile kind=replay \ | ||
| --data kind=weka,source.kind=hf,source.src=valeriol29/mooncake-traces,load_kwargs.name=mooncake | ||
| ``` | ||
|
|
||
| **OTEL dataset from `huggingface`:** | ||
|
|
||
| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --profile kind=replay \ | ||
| --data kind=otel,source.kind=huggingface,source.source=ibm-research/synthetic-conversations-traces,load_kwargs.split=train \ | ||
| --data-loader kind=pytorch,samples=2 | ||
| ``` |

There was a problem hiding this comment.

If we are treating these as full examples they should probably all have constraints set. Also `--data-loader kind=pytorch,samples=2`

should be removed. Also technically a lot of these are setting the default value. Maybe change `time_scale=2.0`

on the `trace_synthetic`

example, remove the split option from WEKA and OTEL.

There was a problem hiding this comment.

I didn't add too many options to these since they're just basic examples of using huggingface as the data source. I added time scale to the trace synthetic example. I added a constraint.

[docs/guides/trace_replay.md](https://github.com/vllm-project/guidellm/pull/1153/files#diff-d1919f3fd587a605342ebbc06efb54fb7f3c1c0c0c94750935e927f956a242a5)Outdated

[docs/guides/trace_replay.md](https://github.com/vllm-project/guidellm/pull/1153/files#diff-d1919f3fd587a605342ebbc06efb54fb7f3c1c0c0c94750935e927f956a242a5)Outdated


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Sep 19, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Checkpoint ... I tried, but I'm not getting any further today and I might as well drop what I've got so far.

[docs/guides/datasets.md](https://github.com/vllm-project/guidellm/pull/1153/files#diff-25d387359ef26d847e440becb4ffc0825e3dbf562df2d7e5b3cc1d49b1e6a43e)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/data/deserializers/trace_otel.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-efa6d0d8c8a7c9b1e66950750db365b5a3044948f592544dae0217dd0cab4013)Outdated

[src/guidellm/data/deserializers/trace_otel.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-efa6d0d8c8a7c9b1e66950750db365b5a3044948f592544dae0217dd0cab4013)

Currently minimal support. No tool call. Incomplete hash support. Generated-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Useful for multiturn dags that embed their own history, rather than using DAG history. Generated-by: Cursor AI Composor 2.5 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Properly utilizes the content from the OTeL traces. Also adds multiple settings to change how GuideLLM uses the OTeL trace. Generated-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Remove speculative defensive code Document actually needed defensive code Remove responses support for future consideration And more. Assisted-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/0b6c6ee0a49278f76f50d021a466c52d0ee20fe4..a314fe9683a4c99066e1a73bd8591449bb2bdfd1)the feat/otel-trace-support branch from

[to](https://github.com/vllm-project/guidellm/commit/0b6c6ee0a49278f76f50d021a466c52d0ee20fe4)

`0b6c6ee`


`a314fe9`

[Compare](https://github.com/vllm-project/guidellm/compare/0b6c6ee0a49278f76f50d021a466c52d0ee20fe4..a314fe9683a4c99066e1a73bd8591449bb2bdfd1)

September 19, 2026 03:44


**commented**

[jaredoconnell](https://github.com/jaredoconnell)Sep 19, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Thank you for the reviews. I hopefully addressed everything. I also had AI go through it and remove speculative parts, since AI adds a lot of defensive speculative parts. That simplified it a bit.

[docs/guides/datasets.md](https://github.com/vllm-project/guidellm/pull/1153/files#diff-25d387359ef26d847e440becb4ffc0825e3dbf562df2d7e5b3cc1d49b1e6a43e)Outdated

[docs/guides/trace_replay.md](https://github.com/vllm-project/guidellm/pull/1153/files#diff-d1919f3fd587a605342ebbc06efb54fb7f3c1c0c0c94750935e927f956a242a5)

| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --profile kind=replay \ | ||
| --data kind=trace_synthetic,source.kind=json_file,source.path=replay.jsonl,time_scale=1.0 | ||
| ``` | ||
|
|
||
| **WEKA dataset from `huggingface`:** | ||
|
|
||
| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --profile kind=replay \ | ||
| --data kind=weka,source.kind=huggingface,source.source=semianalysisai/cc-traces-weka-no-subagents-051226,load_kwargs.split=train | ||
| ``` | ||
|
|
||
| **Mooncake dataset from `huggingface`** | ||
|
|
||
| ```bash | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --profile kind=replay \ | ||
| --data kind=weka,source.kind=hf,source.src=valeriol29/mooncake-traces,load_kwargs.name=mooncake | ||
| ``` | ||
|
|
||
| **OTEL dataset from `huggingface`:** | ||
|
|
||
| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --profile kind=replay \ | ||
| --data kind=otel,source.kind=huggingface,source.source=ibm-research/synthetic-conversations-traces,load_kwargs.split=train \ | ||
| --data-loader kind=pytorch,samples=2 | ||
| ``` |

There was a problem hiding this comment.

I didn't add too many options to these since they're just basic examples of using huggingface as the data source. I added time scale to the trace synthetic example. I added a constraint.

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/data/deserializers/trace_otel.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-efa6d0d8c8a7c9b1e66950750db365b5a3044948f592544dae0217dd0cab4013)

[src/guidellm/data/deserializers/trace_otel.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-efa6d0d8c8a7c9b1e66950750db365b5a3044948f592544dae0217dd0cab4013)

| def _raw_turn_messages( | ||
| self, | ||
| turn_idx: int, | ||
| turn: dict[str, Any], | ||
| rows: list[dict[str, Any]], | ||
| ) -> list[dict[str, Any]]: | ||
| attributes = span_attributes(turn["span"]) | ||
| input_messages = parse_gen_ai_messages(attributes.get("gen_ai.input.messages")) | ||
| if not input_messages: | ||
| raise InvalidRowError( | ||
| "OTEL format: span missing gen_ai.input.messages. " | ||
| "Use kind=trace_synthetic for token-count-only traces." | ||
| ) | ||
| if self.config.history != "runtime" or turn_idx == 0: | ||
| return input_messages | ||
| return self._runtime_raw_delta(input_messages, rows[turn_idx - 1]) |

There was a problem hiding this comment.

Yeah, that's why I mentioned that to do a pure raw column we'd need another column to describe what part is raw. I don't think it makes sense to go full `raw`

for this.

[src/guidellm/scheduler/dag.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-71854c4e28142c71460d1b15d57935c6e8557a60e37f5b0344d066fa9a5e7f3c)Outdated

[src/guidellm/scheduler/dag.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-71854c4e28142c71460d1b15d57935c6e8557a60e37f5b0344d066fa9a5e7f3c)Outdated

[src/guidellm/schemas/data/deserializers/trace_otel.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-6c266d6793e590d8da3ca40b579757e772c06933cba8419b6e5c31fd367afb62)Outdated


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Sep 21, 2026

[docs/guides/tool_calling.md](https://github.com/vllm-project/guidellm/pull/1153/files/a314fe9683a4c99066e1a73bd8591449bb2bdfd1#diff-61af4f8d78e766b599dc58cd80c99c7b4be40899e4726feaf6deb3819f4a658b)Outdated

[docs/guides/trace_replay.md](https://github.com/vllm-project/guidellm/pull/1153/files/a314fe9683a4c99066e1a73bd8591449bb2bdfd1#diff-d1919f3fd587a605342ebbc06efb54fb7f3c1c0c0c94750935e927f956a242a5)

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/data/deserializers/trace_otel.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-efa6d0d8c8a7c9b1e66950750db365b5a3044948f592544dae0217dd0cab4013)


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Sep 21, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

On a whim, I had Codex do a local code review, and it brought up a few interesting points.

First, OTEL replay only supports /v1/chat/completions, but there's no validation. I confirmed that if I specify `request_format=`

either `/v1/completions`

or `/v1/responses`

, the GuideLLM run completes very quickly, with no output tokens (plus a request err and 407 input token errs). This is implied in the documentation, and the output statistics are certainly enough to suggest a problem... but while I'm a bit reluctant to add a cross-component validator, the Goodput PR already introduced that concept with a cross-check between profile and metrics, and we *could* add a cross-check between the replay profile and the backend request format.

A bit more subtle and arcane (and I haven't tried to verify), so I'm passing these on verbatim:

- Medium: fallback tool-response injections lose their original timing. When the next LLM span cannot be consumed as the injection, _placeholder_or_execute_results() correctly searches for later execute_tool spans, but _append_tool_loop() still stamps the synthetic injection with the tool-call span’s timestamp. In practice that collapses tool latency to zero even when the trace recorded a later tool execution, which distorts replay pacing for agentic workloads. The injection timestamp should come from the matched execute_tool span (or at least the earliest matched fallback), not the original call time. trace_otel.py (line 817) trace_otel.py (line 831)
- Medium: execute_tool attribution is based only on time windows, not span relationships, so overlapping tool activity inside one trace_id can be attached to the wrong tool loop. The code explicitly ignores parent_span_id and collects every execute_tool span between two LLM timestamps. That is fragile for concurrent subagents or nested tool execution, which is exactly where OTEL traces tend to be valuable. I’d want parent/child matching here before trusting multi-agent traces. trace_otel.py (line 425) trace_otel.py (line 841)

The problem here is that replay can support other request_formats for weka and mooncake. So I guess you could check if |


**requested changes**

[sjmonson](https://github.com/sjmonson)Sep 21, 2026

[src/guidellm/data/deserializers/trace_otel.py](https://github.com/vllm-project/guidellm/pull/1153/files/a314fe9683a4c99066e1a73bd8591449bb2bdfd1#diff-efa6d0d8c8a7c9b1e66950750db365b5a3044948f592544dae0217dd0cab4013)Outdated

| def is_execute_tool_span(span: dict[str, Any]) -> bool: | ||
| """Return whether ``span`` is a tool-execution span, not an LLM request. | ||
|
|
||
| Matches ``gen_ai.operation.name == execute_tool``. | ||
|
|
||
| :param span: One OTEL span dict. | ||
| :return: ``True`` when this span records a tool execution. | ||
| """ | ||
| return span_attributes(span).get("gen_ai.operation.name") == "execute_tool" |

There was a problem hiding this comment.

This is only used in one place. Just inline it with a comment:

```
# if `span` is not a tool-execution span
if not span_attributes(span).get("gen_ai.operation.name") == "execute_tool":
```

Generated-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

This ensures that running an OTeL trace with incompatible message formats fails with a helpful message Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**commented**

[jaredoconnell](https://github.com/jaredoconnell)Sep 23, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Addressed review comments, and attempted to make the recommended improvements for tool calls.

[src/guidellm/data/deserializers/trace_otel.py](https://github.com/vllm-project/guidellm/pull/1153/files/a314fe9683a4c99066e1a73bd8591449bb2bdfd1#diff-efa6d0d8c8a7c9b1e66950750db365b5a3044948f592544dae0217dd0cab4013)Outdated

| def is_execute_tool_span(span: dict[str, Any]) -> bool: | ||
| """Return whether ``span`` is a tool-execution span, not an LLM request. | ||
|
|
||
| Matches ``gen_ai.operation.name == execute_tool``. | ||
|
|
||
| :param span: One OTEL span dict. | ||
| :return: ``True`` when this span records a tool execution. | ||
| """ | ||
| return span_attributes(span).get("gen_ai.operation.name") == "execute_tool" |

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/1153/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[docs/guides/tool_calling.md](https://github.com/vllm-project/guidellm/pull/1153/files/a314fe9683a4c99066e1a73bd8591449bb2bdfd1#diff-61af4f8d78e766b599dc58cd80c99c7b4be40899e4726feaf6deb3819f4a658b)Outdated

### This branch has not been deployed

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

OTEL traces are a useful addition because they typically include the actual text of the requests, rather than needing to mess with hash IDs to synthetically generate data.

This PR adds support for OTeL, with options for both constructed history or raw trace history. Trace-offs are documented.

## Details

`preceding_nodes`

## Test Plan

## Related Issues

Resolves #968

## Use of AI

## git log

commit

99b5247Author: Jared O'Connell joconnel@redhat.com

Date: Fri Sep 11 13:13:52 2026 -0400

commit

ca08ad4Author: Jared O'Connell joconnel@redhat.com

Date: Tue Sep 15 17:54:58 2026 -0400

commit

f9cde77Author: Jared O'Connell joconnel@redhat.com

Date: Tue Sep 15 17:57:58 2026 -0400

commit

0fb0fbbAuthor: Jared O'Connell joconnel@redhat.com

Date: Wed Sep 16 12:24:38 2026 -0400

commit

a314fe9Author: Jared O'Connell joconnel@redhat.com

Date: Fri Sep 18 23:42:15 2026 -0400

commit

311a36aAuthor: Jared O'Connell joconnel@redhat.com

Date: Wed Sep 23 00:24:35 2026 -0400

commit

85b1f47Author: Jared O'Connell joconnel@redhat.com

Date: Wed Sep 23 00:39:47 2026 -0400

commit

b5bfce1Author: Jared O'Connell joconnel@redhat.com

Date: Wed Sep 23 01:07:28 2026 -0400

Assisted-by: Cursor AI Grok 4.6

Generated-by: Cursor AI Composor 2.5

Generated-by: Cursor AI Grok 4.6

Signed-off-by: Jared O'Connell joconnel@redhat.com