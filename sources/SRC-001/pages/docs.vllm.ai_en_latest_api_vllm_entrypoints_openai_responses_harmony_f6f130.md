source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/responses/harmony/
lastmod: 2026-09-23

#

`vllm.entrypoints.openai.responses.harmony`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony)

Harmony ↔ Responses API conversion utilities.

## Handles two directions

- Response Input → Harmony Messages (input parsing)
- Harmony Messages → Response Output Items (output parsing)

Functions:

-
–[construct_harmony_previous_input_messages](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony.construct_harmony_previous_input_messages)Build a Harmony message list from request.previous_input_messages.

-
–[harmony_to_response_output](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony.harmony_to_response_output)Parse a Harmony message into a list of output response items.

-
–[response_input_to_harmony](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony.response_input_to_harmony)Convert a single ResponseInputOutputItem into a Harmony Message.

-
–[response_previous_input_to_harmony](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony.response_previous_input_to_harmony)Parse a message from request.previous_input_messages


##

`_parse_browser_tool_call(message, recipient)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony._parse_browser_tool_call)

Parse browser tool calls (search, open, find) into web search items.

## Source code in `vllm/entrypoints/openai/responses/harmony.py`


##

`_parse_chat_format_message(chat_msg)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony._parse_chat_format_message)

Parse an OpenAI chat-format dict into Harmony messages.

## Source code in `vllm/entrypoints/openai/responses/harmony.py`


##

`_parse_final_message(message, incomplete=False)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony._parse_final_message)

Parse final channel messages into output message items.

## Source code in `vllm/entrypoints/openai/responses/harmony.py`


##

`_parse_function_call(message, recipient, incomplete=False)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony._parse_function_call)

Parse function calls into function tool call items.

## Source code in `vllm/entrypoints/openai/responses/harmony.py`


##

`_parse_harmony_format_message(chat_msg)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony._parse_harmony_format_message)

Reconstruct a Message from Harmony-format dict, preserving channel, recipient, and content_type.

## Source code in `vllm/entrypoints/openai/responses/harmony.py`


##

`_parse_mcp_call(message, recipient, incomplete=False)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony._parse_mcp_call)

Parse MCP calls into MCP call items.

## Source code in `vllm/entrypoints/openai/responses/harmony.py`


##

`_parse_mcp_recipient(recipient)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony._parse_mcp_recipient)

Parse MCP recipient into (server_label, tool_name).

For dotted recipients like "repo_browser.list": - server_label: "repo_browser" (namespace/server) - tool_name: "list" (specific tool)

For simple recipients like "filesystem": - server_label: "filesystem" - tool_name: "filesystem"

## Source code in `vllm/entrypoints/openai/responses/harmony.py`


##

`_parse_message_no_recipient(message, incomplete=False)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony._parse_message_no_recipient)

Parse a Harmony message with no recipient based on its channel.

## Source code in `vllm/entrypoints/openai/responses/harmony.py`


##

`_parse_reasoning(message)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony._parse_reasoning)

Parse reasoning/analysis content into reasoning items.

## Source code in `vllm/entrypoints/openai/responses/harmony.py`


##

`construct_harmony_previous_input_messages(request)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony.construct_harmony_previous_input_messages)

Build a Harmony message list from request.previous_input_messages.

Filters out system/developer messages to match OpenAI behavior where instructions are always taken from the most recent Responses API request.

## Source code in `vllm/entrypoints/openai/responses/harmony.py`


##

`harmony_to_response_output(message, function_tool_names, incomplete=False)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony.harmony_to_response_output)

Parse a Harmony message into a list of output response items.

This is the main dispatcher that routes based on channel and recipient.

## Source code in `vllm/entrypoints/openai/responses/harmony.py`


##

`response_input_to_harmony(response_msg, prev_responses)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony.response_input_to_harmony)

Convert a single ResponseInputOutputItem into a Harmony Message.

Returns None for reasoning items with empty or absent content so the caller can skip them.

## Source code in `vllm/entrypoints/openai/responses/harmony.py`


##

`response_previous_input_to_harmony(chat_msg)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.harmony.response_previous_input_to_harmony)

Parse a message from request.previous_input_messages into Harmony messages.

Supports both OpenAI chat format ({"role": "..."}) and Harmony format ({"author": {"role": "..."}}).