source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/parser/harmony_utils/
lastmod: 2026-09-23

#

`vllm.entrypoints.openai.parser.harmony_utils`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils)

Functions:

-
–[auto_drop_analysis_messages](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.auto_drop_analysis_messages)Harmony models expect the analysis messages (representing raw chain of thought)

-
–[build_harmony_preamble](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.build_harmony_preamble)Build the standard Harmony system/developer prefix for a request.

-
–[extract_instructions_from_messages](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.extract_instructions_from_messages)Peel a leading system/developer Chat Completion or Responses message and

-
–[flatten_input_text_content](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.flatten_input_text_content)Extract text parts from a Chat Completion or Responses API content field and

-
–[has_custom_tools](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.has_custom_tools)Checks if the given tool types are custom tools

-
–[is_function_recipient](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.is_function_recipient)Check whether

*recipient*refers to a function tool call. -
–[parse_chat_input_to_harmony_message](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.parse_chat_input_to_harmony_message)Parse a message from request.messages in the Chat Completion API to

-
–[parse_chat_inputs_to_harmony_messages](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.parse_chat_inputs_to_harmony_messages)Parse a list of messages from request.messages in the Chat Completion API to


##

`auto_drop_analysis_messages(msgs)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.auto_drop_analysis_messages)

Harmony models expect the analysis messages (representing raw chain of thought) to be dropped after an assistant message to the final channel is produced from the reasoning of those messages.

The openai-harmony library does this if the very last assistant message is to the final channel, but it does not handle the case where we're in longer multi-turn conversations and the client gave us reasoning content from previous turns of the conversation with multiple assistant messages to the final channel in the conversation.

So, we find the index of the last assistant message to the final channel and drop all analysis messages that precede it, leaving only the analysis messages that are relevant to the current part of the conversation.

## Source code in `vllm/entrypoints/openai/parser/harmony_utils.py`


##

`build_harmony_preamble(*, instructions=None, tools=None, reasoning_effort=None, browser_description=None, python_description=None, container_description=None, with_custom_tools=False)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.build_harmony_preamble)

Build the standard Harmony system/developer prefix for a request.

## Source code in `vllm/entrypoints/openai/parser/harmony_utils.py`


##

`extract_instructions_from_messages(messages)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.extract_instructions_from_messages)

Peel a leading system/developer Chat Completion or Responses message and flatten its instruction text.

## Source code in `vllm/entrypoints/openai/parser/harmony_utils.py`


##

`flatten_input_text_content(content)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.flatten_input_text_content)

Extract text parts from a Chat Completion or Responses API content field and flatten them into a single string. Returns None if no text content is found.

## Source code in `vllm/entrypoints/openai/parser/harmony_utils.py`


##

`has_custom_tools(tool_types)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.has_custom_tools)

Checks if the given tool types are custom tools (i.e. any tool other than MCP builtin tools)

##

`is_function_recipient(recipient, allowed_function_tool_names=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.is_function_recipient)

Check whether *recipient* refers to a function tool call.

The optional *allowed_function_tool_names* parameter is used by the Responses API to distinguish bare function-call recipients (missing the `functions.`

prefix) from MCP tool calls. When provided, a bare recipient is only treated as a function call if it appears in the set. The Chat Completions path omits this parameter so that all bare recipients are accepted as function calls (the heuristic fallback).

## Source code in `vllm/entrypoints/openai/parser/harmony_utils.py`


##

`parse_chat_input_to_harmony_message(chat_msg, tool_id_names=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.parse_chat_input_to_harmony_message)

Parse a message from request.messages in the Chat Completion API to Harmony messages.

## Source code in `vllm/entrypoints/openai/parser/harmony_utils.py`


|
|

##

`parse_chat_inputs_to_harmony_messages(chat_msgs)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.parser.harmony_utils.parse_chat_inputs_to_harmony_messages)

Parse a list of messages from request.messages in the Chat Completion API to Harmony messages.