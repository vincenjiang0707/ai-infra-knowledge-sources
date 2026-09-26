source: https://docs.nvidia.com/dynamo/v1.1.1/user-guides/tool-calling/troubleshooting-tool-calls
lastmod: 2026-09-24T19:58:16.636Z

# Troubleshooting Tool Calls

When a tool call comes back wrong (`tool_calls`

is `null`

, the arguments
look malformed, raw `<tool_call>`

markers appear in `message.content`

, or
`finish_reason`

is `"stop"`

when you expected `"tool_calls"`

), the request
and response alone usually do not say *where* the bug is. The model and the
parser produce indistinguishable failures from the response side.

Adding `"logprobs": true`

to a single repro request makes the engine’s raw
token output visible in the response. That is enough for someone on the
Dynamo team to identify whether the issue is in the model, the parser
configuration, or the parser itself. This page shows the field to add and
what the response will look like, so you can capture and share useful
diagnostic info.

Recipe applies to non-streaming requests against Dynamo’s OpenAI
`/v1/chat/completions`

endpoint. For multi-channel reasoning models
(`harmony`

, `kimi_k2`

, `kimi_k25`

, `gemma4`

), the recipe recovers only
the assistant-content channel; the reasoning channel is not surfaced in
`logprobs.content`

.

If the worker is the SGLang backend, `logprobs: true`

is rejected by
default because SGLang’s tokenizer manager detokenizes top-k tokens
serially, causing latency degradation. Launch the worker with
`DYN_SGL_ALLOW_TOP_LOGPROBS=1`

set in the environment to opt in for the
duration of the repro request, then unset it afterward. Tracked at
[sgl-project/sglang#24447](https://github.com/sgl-project/sglang/pull/24447).

## The request

Add `"logprobs": true`

to your failing request:

## The response

You will get back the usual fields (`message.tool_calls`

, `message.content`

,
`finish_reason`

) plus a new `choices[0].logprobs.content`

field carrying the
engine’s raw token stream:

Each entry in `logprobs.content`

is one generated token with its exact UTF-8
`bytes`

. Concatenating those bytes in order reconstructs the raw model
output, before any tool-call parser touched it. That is the key piece for
triage: it tells us what the model actually produced, separately from what
the parser made of it.

## What to include when reporting an issue

Share these four things in the bug report or issue thread:

**The full request body**(model name, messages, tools, sampling params, and`logprobs: true`

).**The full response body.**Do not truncate`logprobs.content`

— the per-token entries are the part that matters.**The Dynamo version and the backend**(vLLM, SGLang, TRT-LLM, including versions if known).**The worker launch command**, especially the`--dyn-tool-call-parser`

value if set.

With those four pieces, the Dynamo team can usually localize the bug
without standing up your model. The team will reconstruct the raw stream
from the `bytes`

arrays and compare it against `message.content`

and
`message.tool_calls`

to decide whether the issue is in the model output,
the parser configuration, or the parser logic.

## See also

[Tool Call Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/tool-calling/tool-call-parsing-dynamo)— Dynamo-native parser names and request examples[Tool Call Parsing (Engine Fallback)](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/tool-calling/tool-call-parsing-engine-fallback)—`--dyn-chat-processor`

fallback path to vLLM and SGLang parsers[Frontend Configuration Reference](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/components/frontend/configuration.md)— full CLI flag reference for the frontend and worker