source: https://github.com/vllm-project/guidellm/pull/687

# Process tool call requests for chat completions API - #687

[jaredoconnell](https://github.com/jaredoconnell)merged 10 commits into

## Conversation


**requested changes**

[sjmonson](https://github.com/sjmonson)Apr 4, 2026

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/687/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/687/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/687/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/687/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Apr 6, 2026

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/687/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/687/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/687/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/5b309e6629ebf3e066d1c7c9387c659272efd8f4..7f1636885286a0a1d6fcfd02d4b833c1d145454e)the feat/tool-call-counting branch from

[to](https://github.com/vllm-project/guidellm/commit/5b309e6629ebf3e066d1c7c9387c659272efd8f4)

`5b309e6`


`7f16368`

[Compare](https://github.com/vllm-project/guidellm/compare/5b309e6629ebf3e066d1c7c9387c659272efd8f4..7f1636885286a0a1d6fcfd02d4b833c1d145454e)

April 8, 2026 20:27


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Apr 9, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

A few questions / minor concerns to consider, but looks OK.

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/687/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/687/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

|
Using the following command with the 7B parameter model, I was able to get it to use tool calls some of the time, which confirmed proper differentiation between all text metrics, and tool call only metrics. The smaller models were not able to automatically execute tool calls. `vllm serve Qwen/Qwen2.5-7B-Instruct --tool-call-parser hermes --enable-auto-tool-choice` `guidellm benchmark run --target "http://localhost:8000" --request-format chat_completions --data mixed_tool_call_prompts.jsonl --data-column-mapper '{"text_column":"text"}' --backend-kwargs '{"extras":{"body":{"tools":[{"type":"function","function":{"name":"get_weather","description":"Get current weather for a location","parameters":{"type":"object","properties":{"location":{"type":"string"}},"required":["location"]}}}],"tool_choice":"auto"}}}' --max-requests 5 --profile constant --rate 1` With this input file: ```
{"prompt": "Use the get_weather function to check the weather in San Francisco."}
{"prompt": "Explain how photosynthesis works."}
{"prompt": "Call get_weather for Tokyo to get the forecast."}
{"prompt": "Write a haiku about mountains."}
{"prompt": "Please call the get_weather tool for London."}
{"prompt": "Summarize the history of the Roman Empire."}
``` Here is a snippet of the output:
|

|
Is it odd that Mdn & P95 tool call "output tokens per request" are both 21, the exact same value as the "text output tokens per request" Mdn?? Are all tool calls returning 21 tokens? Maybe it's just a coincidence... |

Tool call calls are a subset of text, so the tool calls appear to be the ones representing the median, but a lot of the non-tool-call ones appear to be larger, bringing up the mean. So I think this is a good sign that it's a subset, and that tool calls aren't being double-counted. |


**requested changes**

[sjmonson](https://github.com/sjmonson)Apr 9, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Addressed my main concerns though also see Dave's comments.

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/687/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Apr 9, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Srry, above was supposed to be approval.


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Apr 9, 2026

|
I made some changes to ensure that the edge case of simultaneous content and tool calls result in tool calls properly getting counted. I did some research and that are models that can do that. |


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Apr 10, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

OK, if we can really have `content`

as well as `tool_calls`

in the same response, it seems odd that we only have `completion_tokens`

, which suggests that we're counting the `content`

along with the tool call output as `tool_call_tokens`

. Or is there just some subtlety I'm missing here?


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Apr 10, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I think the situation kinda sucks; but we didn't make it and it seems we have limited visibility and no control. (The glitch is that we'll take the blame for "bad" counts.)

As I suggested in Slack, another option might be to break out a separate bucket of "mixed tool_call / text" response content that doesn't attribute it all or none to tool calling -- that's not very satisfying, but at least it provides visibility.

(Plus, if we make that display conditional on non-zero, and it's really rare, maybe nobody'll have to deal with it...)

|
I've since learned that Qwen shows thinking tokens when tool calls are auto, but doesn't when tool calls are required. This added stat provides good visibility on what the model is doing without needing to inspect the outputs. |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Apr 13, 2026


**approved these changes**

[sjmonson](https://github.com/sjmonson)Apr 13, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

LGTM with one clarifying question.

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/687/files/3ea035d02c739f7cba11cfb96fe72e85dc0c105c#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Change the tool call counting logic to just count it instead of serializing it to reuse the text pathway. Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

There is no good way to differentiate, and this is an edge case. It is now properly documented to prevent confusion, and tool call counts are still valid. Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/3ea035d02c739f7cba11cfb96fe72e85dc0c105c..fe69e40c3642f33fd5ec85782b84c31932efc059)the feat/tool-call-counting branch from

[to](https://github.com/vllm-project/guidellm/commit/3ea035d02c739f7cba11cfb96fe72e85dc0c105c)

`3ea035d`


`fe69e40`

[Compare](https://github.com/vllm-project/guidellm/compare/3ea035d02c739f7cba11cfb96fe72e85dc0c105c..fe69e40c3642f33fd5ec85782b84c31932efc059)

April 13, 2026 19:32

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

This is a first step towards getting tool calling working.

## Details

## Test Plan

Example:

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)