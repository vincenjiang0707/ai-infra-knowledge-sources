source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/responses/context/
lastmod: 2026-09-23

#

`vllm.entrypoints.openai.responses.context`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context)

Classes:

-
–[HarmonyContext](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.HarmonyContext) -
–[ParsableContext](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.ParsableContext) -
–[SimpleContext](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.SimpleContext)This is a context that cannot handle MCP tool calls.

-
–[TurnMetrics](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.TurnMetrics)Tracks token and toolcall details for a single conversation turn.


##

`HarmonyContext`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.HarmonyContext)

Bases: `ConversationContext`


Methods:

-
–[call_container_tool](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.HarmonyContext.call_container_tool)Call container tool. Expect this to be run in a stateful docker

-
–[cleanup_session](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.HarmonyContext.cleanup_session)Can be used as coro to used in

**aexit**.

## Source code in `vllm/entrypoints/openai/responses/context.py`


|
|

###

`_update_decode_token_usage(output)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.HarmonyContext._update_decode_token_usage)

Update token usage statistics for the decode phase of generation.

The decode phase processes the generated output tokens. This method: 1. Counts output tokens from all completion outputs 2. Updates the total output token count 3. Tracks tokens generated in the current turn

In streaming mode, this is called for each token generated. In non-streaming mode, this is called once with all output tokens.

Parameters:

-

(`output`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.HarmonyContext._update_decode_token_usage(output))

) –[RequestOutput](https://docs.vllm.ai/outputs/#vllm.outputs.RequestOutput)The RequestOutput containing generated token information


Returns:

-
(`int`


) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of output tokens processed in this call


## Source code in `vllm/entrypoints/openai/responses/context.py`


###

`_update_prefill_token_usage(output)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.HarmonyContext._update_prefill_token_usage)

Update token usage statistics for the prefill phase of generation.

The prefill phase processes the input prompt tokens. This method: 1. Counts the prompt tokens for this turn 2. Calculates tool output tokens for multi-turn conversations 3. Updates cached token counts 4. Tracks state for next turn calculations

Tool output tokens are calculated as: current_prompt_tokens - last_turn_prompt_tokens - last_turn_output_tokens This represents tokens added between turns (typically tool responses).

Parameters:

-

(`output`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.HarmonyContext._update_prefill_token_usage(output))

) –[RequestOutput](https://docs.vllm.ai/outputs/#vllm.outputs.RequestOutput)The RequestOutput containing prompt token information


## Source code in `vllm/entrypoints/openai/responses/context.py`


###

`call_container_tool(tool_session, last_msg)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.HarmonyContext.call_container_tool)

Call container tool. Expect this to be run in a stateful docker with command line terminal. The official container tool would at least expect the following format: - for tool name: exec - args: { "cmd":List[str] "command to execute", "workdir":optional[str] "current working directory", "env":optional[object/dict] "environment variables", "session_name":optional[str] "session name", "timeout":optional[int] "timeout in seconds", "user":optional[str] "user name", }

## Source code in `vllm/entrypoints/openai/responses/context.py`


###

`cleanup_session(*args, **kwargs)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.HarmonyContext.cleanup_session)

Can be used as coro to used in **aexit**.

## Source code in `vllm/entrypoints/openai/responses/context.py`


##

`ParsableContext`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.ParsableContext)

Bases: `ConversationContext`


Methods:

-
–[call_container_tool](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.ParsableContext.call_container_tool)Call container tool. Expect this to be run in a stateful docker

-
–[cleanup_session](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.ParsableContext.cleanup_session)Can be used as coro to used in

**aexit**. -
–[need_builtin_tool_call](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.ParsableContext.need_builtin_tool_call)Return true if the last message is a builtin tool call


## Source code in `vllm/entrypoints/openai/responses/context.py`


|
|

###

`call_container_tool(tool_session, last_msg)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.ParsableContext.call_container_tool)

Call container tool. Expect this to be run in a stateful docker with command line terminal. The official container tool would at least expect the following format: - for tool name: exec - args: { "cmd":List[str] "command to execute", "workdir":optional[str] "current working directory", "env":optional[object/dict] "environment variables", "session_name":optional[str] "session name", "timeout":optional[int] "timeout in seconds", "user":optional[str] "user name", }

## Source code in `vllm/entrypoints/openai/responses/context.py`


###

`cleanup_session(*args, **kwargs)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.ParsableContext.cleanup_session)

Can be used as coro to used in **aexit**.

## Source code in `vllm/entrypoints/openai/responses/context.py`


###

`need_builtin_tool_call()`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.ParsableContext.need_builtin_tool_call)

Return true if the last message is a builtin tool call that the request has enabled.

## Source code in `vllm/entrypoints/openai/responses/context.py`


##

`SimpleContext`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.SimpleContext)

Bases: `ConversationContext`


This is a context that cannot handle MCP tool calls.

Attributes:

-
([final_output](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.SimpleContext.final_output)

) –[RequestOutput](https://docs.vllm.ai/outputs/#vllm.outputs.RequestOutput)| NoneReturn the final output, with complete text/token_ids/logprobs.

-
([output_messages](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.SimpleContext.output_messages)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[ResponseRawMessageAndToken](https://docs.vllm.ai/protocol/#vllm.entrypoints.openai.responses.protocol.ResponseRawMessageAndToken)]Return consolidated output as a single message.


## Source code in `vllm/entrypoints/openai/responses/context.py`


|
|

###

`final_output`

`property`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.SimpleContext.final_output)

Return the final output, with complete text/token_ids/logprobs.

###

`output_messages`

`property`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.SimpleContext.output_messages)

Return consolidated output as a single message.

In streaming mode, text and tokens are accumulated across many deltas. This property returns them as a single entry rather than one per delta.

##

`TurnMetrics`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.TurnMetrics)

Tracks token and toolcall details for a single conversation turn.

Methods:

## Source code in `vllm/entrypoints/openai/responses/context.py`


###

`copy()`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context.TurnMetrics.copy)

Create a copy of this turn's token counts.

##

`_create_json_parse_error_messages(last_msg, e)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.context._create_json_parse_error_messages)

Creates an error message when json parse failed.