source: https://github.com/vllm-project/guidellm/pull/1159

# Pass a backend's per-request metrics through to the compiled stats - #1159

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

## Conversation

vLLM reports per-request server-side timings and speculative-decoding acceptance in a `metrics` object beside `usage`, served behind `--per-request-spec-decode-metrics` since 0.29. `extract_choices_and_usage` reads only `choices` and `usage`, so the object is dropped before a `GenerationResponse` is built and never reaches the report. Record it on the handler where the raw response is already read, and carry it on `GenerationResponse.response_metrics` into `GenerativeRequestStats`. It is passed through as received rather than modelled, since its contents are the backend's own and vLLM marks the shape experimental. The completions and chat-completions handlers populate it; the responses handler leaves the default. `clear_stats_data` does not touch it, so a non-sampled request keeps its metrics like it keeps its usage. Assisted-by: Claude Code claude-opus-5 Signed-off-by: wenxuan-elastix <wenxuan@elastix.ai>

[wenxuan-elastix](https://github.com/wenxuan-elastix)

[force-pushed](https://github.com/vllm-project/guidellm/compare/e5bc748c0aaaf64d413ec98d65ff2b7f9ee7f3f5..21df4897a5cf7ce461c35f8a359390fee528f3b8)the passthrough-response-metrics branch from

[to](https://github.com/vllm-project/guidellm/commit/e5bc748c0aaaf64d413ec98d65ff2b7f9ee7f3f5)

`e5bc748`


`21df489`

[Compare](https://github.com/vllm-project/guidellm/compare/e5bc748c0aaaf64d413ec98d65ff2b7f9ee7f3f5..21df4897a5cf7ce461c35f8a359390fee528f3b8)

September 21, 2026 18:59

[sjmonson](https://github.com/sjmonson)requested review from

[dbutenhof](https://github.com/dbutenhof),

[jaredoconnell](https://github.com/jaredoconnell)and

[sjmonson](https://github.com/sjmonson)and removed request for

[jaredoconnell](https://github.com/jaredoconnell)

September 21, 2026 19:34


**approved these changes**

[sjmonson](https://github.com/sjmonson)Sep 21, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Yeah seems reasonable. Adding summary metrics for this was on my TODO list for v0.9.0 but is somewhat blocked by refactoring the metrics handler to better support optional metrics. This is good for now since at least the user can get the raw data.

|
Queued — the merge queue status continues in |

|
|

## ☑️ Command disallowed due to
|

|
|


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 21, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

OK -- this is relatively simple, and appears to work when I run vLLM with `--enable-per-request-metrics`

.

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

vLLM 0.29 can report a request's own server-side timings and speculative-decoding


acceptance on the response, in a

`metrics`

object next to`usage`

. GuideLLM drops it:`extract_choices_and_usage`

reads only`choices`

and`usage`

, so the object is gonebefore a

`GenerationResponse`

is built and never reaches the report.That matters most for speculative decoding. Today the only way to get acceptance out of

a GuideLLM run is to scrape

`/metrics`

separately and difference two counter snapshotstaken around it. Those counters are server-wide and cumulative, so the delta also counts

anything else that hit the endpoint during the run, and a per-engine counter reset can

hide inside the sum. The numbers on the response describe exactly the requests GuideLLM

made, and arrive with them.

This PR carries that object through unchanged, as

`response_metrics`

.What the server sends when started with

`--per-request-spec-decode-metrics summary`

:In streaming it rides the closing usage chunk, which GuideLLM already requests via


`stream_options.include_usage`

, so nothing about how requests are sent changes.Reference: https://docs.vllm.ai/en/v0.29.0/features/speculative_decoding/acceptance_metrics/

## Details

`GenerationResponse.response_metrics: dict[str, Any] | None`

, and the samefield on

`GenerativeRequestStats`

, passed through by`compile_stats`

.`TextCompletionsRequestHandler.extract_choices_and_usage`

.That is the one place every completions handler already reads the raw response

dict, on both the streaming and the non-streaming path, so recording it there

rather than returning it keeps that method's signature as it is.

`_compile_streaming_response`

for the chat handler.Notes on the choices made:

Passed through, not modelled.The contents belong to the backend, and vLLM marksthis shape experimental, so GuideLLM validating it would just be a second thing to

keep in sync. A

`dict`

costs nothing and stays correct when the shape moves.Which handlers.Completions and chat completions populate it, and the audio andpooling handlers inherit that. The

`/v1/responses`

handler does not read the field andkeeps the default

`None`

.Sampling.`clear_stats_data`

clears`request_args`

,`output`

,`reasoning_output`

and

`tool_calls`

on non-sampled requests; it does not touch metrics, so a non-sampledrequest keeps

`response_metrics`

the same way it keeps its usage.Backends that report nothingare unaffected: the field stays`None`

.## Test Plan

`TestResponseMetricsPassthrough`

in`tests/unit/backends/openai/test_request_handlers.py`

covers the three cases:

`GenerationResponse.response_metrics`

`metrics`

leaves the field`None`

Ran against




`main`

as a baseline and with this change, over`tests/unit/backends/openai/test_request_handlers.py`

,`tests/unit/schemas`

and`tests/unit/benchmark`

: same failures before and after, plus the three new tests passing.`ruff check`

reports the same findings as`main`

over the changed files.## Related Issues

None open that I could find; happy to file one if you would rather track it separately.

## Use of AI

## git log

commit

21df489Author: wenxuan-elastix wenxuan@elastix.ai

Date: Thu Sep 17 16:03:41 2026 -0700

Assisted-by: Claude Code claude-opus-5

Signed-off-by: wenxuan-elastix wenxuan@elastix.ai