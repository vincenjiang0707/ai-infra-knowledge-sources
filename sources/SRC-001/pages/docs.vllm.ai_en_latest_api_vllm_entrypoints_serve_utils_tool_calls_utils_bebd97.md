source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/utils/tool_calls_utils/
lastmod: 2026-09-23

#

`vllm.entrypoints.serve.utils.tool_calls_utils`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.tool_calls_utils)

Functions:

-
–[maybe_filter_parallel_tool_calls](https://docs.vllm.ai#vllm.entrypoints.serve.utils.tool_calls_utils.maybe_filter_parallel_tool_calls)Filter to first tool call only when parallel_tool_calls is explicitly False.


##

`maybe_filter_parallel_tool_calls(choice, request)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.tool_calls_utils.maybe_filter_parallel_tool_calls)

Filter to first tool call only when parallel_tool_calls is explicitly False.