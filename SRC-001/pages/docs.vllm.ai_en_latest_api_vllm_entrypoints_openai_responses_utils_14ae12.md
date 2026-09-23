source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/responses/utils/
lastmod: 2026-09-23

#

`vllm.entrypoints.openai.responses.utils`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.utils)

Functions:

-
–[construct_chat_messages_with_tool_call](https://docs.vllm.ai#vllm.entrypoints.openai.responses.utils.construct_chat_messages_with_tool_call)Build chat messages from response items.

-
–[convert_tool_responses_to_completions_format](https://docs.vllm.ai#vllm.entrypoints.openai.responses.utils.convert_tool_responses_to_completions_format)Convert a flat Responses tool schema:

-
–[extract_tool_types](https://docs.vllm.ai#vllm.entrypoints.openai.responses.utils.extract_tool_types)Extracts the tool types from the given tools.

-
–[should_continue_final_message](https://docs.vllm.ai#vllm.entrypoints.openai.responses.utils.should_continue_final_message)Determine if the last input message is a partial assistant message


##

`_construct_message_from_response_item(item, prev_msg=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.utils._construct_message_from_response_item)

Returns a new message or None. If `None`

, `prev_msg`

might be updated. If `prev_msg`

is `None`

, a new message is always returned.

## Source code in `vllm/entrypoints/openai/responses/utils.py`


|
|

##

`construct_chat_messages_with_tool_call(input_messages)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.utils.construct_chat_messages_with_tool_call)

Build chat messages from response items.

Some chat messages span multiple response items (e.g., reasoning + tool calls).

## Source code in `vllm/entrypoints/openai/responses/utils.py`


##

`convert_tool_responses_to_completions_format(tool)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.utils.convert_tool_responses_to_completions_format)

## Convert a flat Responses tool schema

{"type": "function", "name": "...", "description": "...", "parameters": {...}}

into a Chat Completions tool param for chat-template rendering.

## Source code in `vllm/entrypoints/openai/responses/utils.py`


##

`extract_tool_types(tools)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.utils.extract_tool_types)

Extracts the tool types from the given tools.

## Source code in `vllm/entrypoints/openai/responses/utils.py`


##

`should_continue_final_message(request_input)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.utils.should_continue_final_message)

Determine if the last input message is a partial assistant message that should be continued rather than starting a new generation.

This enables partial message completion similar to Anthropic's Messages API, where users can provide an incomplete assistant message and have the model continue from where it left off.

A message is considered partial if: 1. It's a ResponseOutputMessage or ResponseReasoningItem 2. Its status is "in_progress" or "incomplete"

Parameters:

Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)True if the final message should be continued, False otherwise