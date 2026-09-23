source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/responses/streaming_events/
lastmod: 2026-09-23

#

`vllm.entrypoints.openai.responses.streaming_events`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events)

Streaming SSE event builders for the Responses API.

Pure functions that translate streaming state + delta data into OpenAI Response API SSE events. Used by the streaming event processors in serving.py.

## The file is organized as

- StreamingState dataclass + utility helpers
- Shared leaf helpers — delta events (take plain strings, no context)
- Shared leaf helpers — done events (take plain strings, no context)
- Harmony-specific dispatchers (route ctx/previous_item → leaf helpers)
- Harmony-specific tool lifecycle helpers

Classes:

-
–[SimpleStreamingEventProcessor](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor)State-machine processor for the simple (non-Harmony) streaming path.

-
–[StreamingState](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.StreamingState)Mutable state for streaming event processing.


Functions:

-
–[emit_browser_tool_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_browser_tool_events)Emit events for browser tool calls (web search).

-
–[emit_code_interpreter_completion_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_code_interpreter_completion_events)Emit events when code interpreter completes.

-
–[emit_code_interpreter_delta_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_code_interpreter_delta_events)Emit events for code interpreter delta streaming.

-
–[emit_content_delta_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_content_delta_events)Emit events for content delta streaming based on channel type.

-
–[emit_function_call_delta_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_function_call_delta_events)Emit events for function call argument deltas.

-
–[emit_function_call_done_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_function_call_done_events)Emit events when a function call completes.

-
–[emit_mcp_completion_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_mcp_completion_events)Emit events when an MCP tool call completes.

-
–[emit_mcp_delta_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_mcp_delta_events)Emit events for MCP tool delta streaming.

-
–[emit_previous_item_done_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_previous_item_done_events)Emit done events for the previous item when expecting a new start.

-
–[emit_reasoning_delta_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_reasoning_delta_events)Emit events for reasoning text delta streaming.

-
–[emit_reasoning_done_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_reasoning_done_events)Emit events when a reasoning (analysis) item completes.

-
–[emit_text_delta_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_text_delta_events)Emit events for text content delta streaming.

-
–[emit_text_output_done_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_text_output_done_events)Emit events when a final text output item completes.

-
–[emit_tool_action_events](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_tool_action_events)Emit events for a completed assistant action turn.

-
–[is_mcp_tool_by_namespace](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.is_mcp_tool_by_namespace)Determine if a tool call is an MCP tool based on recipient prefix.

-
–[split_delta](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.split_delta)Decompose a DeltaMessage with multiple fields into atomic deltas.


##

`SimpleStreamingEventProcessor`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor)

State-machine processor for the simple (non-Harmony) streaming path.

## Core flow

- Resolve the target state from the delta_message (CONTENT / REASONING / TOOL_CALL).
- If the target state differs from the current one, close_current() then open() the new state.
- emit_delta() produces the incremental events for the state.

## State lifecycle

open() -> repeated emit_delta() -> close_current()

Methods:

-
–[close_current](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.close_current)Close the current state and emit its 'done' event sequence.

-
–[emit_delta](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.emit_delta)Emit incremental events for the current state from the delta.

-
–[needs_transition](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.needs_transition)Return True when we must close the current state and open a new one.

-
–[open](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.open)Open a new state and emit its 'added' / 'open' event sequence.

-
–[resolve_target_state](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.resolve_target_state)Decide which state the next delta belongs to.


## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


|
|

###

`close_current()`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.close_current)

Close the current state and emit its 'done' event sequence.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


###

`emit_delta(delta_message, output, get_logprobs=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.emit_delta)

Emit incremental events for the current state from the delta.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


###

`needs_transition(target_state, tool_call)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.needs_transition)

Return True when we must close the current state and open a new one.

## Two cases trigger a transition

- The target state differs from the current state (e.g. CONTENT -> TOOL_CALL).
- We are already in TOOL_CALL but the next tool_call has a different index (multiple consecutive tool calls).

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


###

`open(target_state, tool_call=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.open)

Open a new state and emit its 'added' / 'open' event sequence.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


###

`resolve_target_state(delta_message)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.resolve_target_state)

Decide which state the next delta belongs to.

Priority: TOOL_CALL > REASONING > CONTENT, fallback to NONE. For TOOL_CALL the first tool_call object is also returned so callers can detect a switch between consecutive tools.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`StreamingState`

`dataclass`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.StreamingState)

Mutable state for streaming event processing.

Methods:

-
–[reset_for_new_item](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.StreamingState.reset_for_new_item)Reset state when expecting a new output item.


## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


###

`reset_for_new_item()`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.StreamingState.reset_for_new_item)

Reset state when expecting a new output item.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`_StateHandlers`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events._StateHandlers)

Bases: [NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)

Tuple for each state: open(start), delta(chunk), done(finish).

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`_resolve_mcp_name_label(recipient)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events._resolve_mcp_name_label)

Resolve MCP tool name and server label from a recipient string.

`mcp.*`

recipients: strip prefix, use the bare name as both name and server_label.- Everything else: use the recipient as the name and look up the server_label in TOOL_NAME_TO_MCP_SERVER_LABEL.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`emit_browser_tool_events(previous_item, state)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_browser_tool_events)

Emit events for browser tool calls (web search).

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


|
|

##

`emit_code_interpreter_completion_events(previous_item, state)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_code_interpreter_completion_events)

Emit events when code interpreter completes.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`emit_code_interpreter_delta_events(delta, state)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_code_interpreter_delta_events)

Emit events for code interpreter delta streaming.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`emit_content_delta_events(segment, state, function_tool_names=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_content_delta_events)

Emit events for content delta streaming based on channel type.

This is a Harmony-specific dispatcher that extracts values from the latest append segment and delegates to shared leaf helpers.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`emit_function_call_delta_events(delta, function_name, state)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_function_call_delta_events)

Emit events for function call argument deltas.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`emit_function_call_done_events(function_name, arguments, state)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_function_call_done_events)

Emit events when a function call completes.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`emit_mcp_completion_events(recipient, arguments, state)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_mcp_completion_events)

Emit events when an MCP tool call completes.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`emit_mcp_delta_events(delta, state, recipient)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_mcp_delta_events)

Emit events for MCP tool delta streaming.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`emit_previous_item_done_events(previous_item, state, function_tool_names=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_previous_item_done_events)

Emit done events for the previous item when expecting a new start.

This is a Harmony-specific dispatcher that extracts values from the Harmony parser's message object and delegates to shared leaf helpers.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`emit_reasoning_delta_events(delta, state)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_reasoning_delta_events)

Emit events for reasoning text delta streaming.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`emit_reasoning_done_events(text, state)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_reasoning_done_events)

Emit events when a reasoning (analysis) item completes.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`emit_text_delta_events(delta, state)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_text_delta_events)

Emit events for text content delta streaming.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`emit_text_output_done_events(text, state)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_text_output_done_events)

Emit events when a final text output item completes.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`emit_tool_action_events(previous_item, state, tool_server)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.emit_tool_action_events)

Emit events for a completed assistant action turn.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`is_mcp_tool_by_namespace(recipient, allowed_function_tool_names=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.is_mcp_tool_by_namespace)

Determine if a tool call is an MCP tool based on recipient prefix.

Inverse of :func:`is_function_recipient`

— everything that is not a function call is an MCP tool.

## Source code in `vllm/entrypoints/openai/responses/streaming_events.py`


##

`split_delta(delta)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.responses.streaming_events.split_delta)

Decompose a DeltaMessage with multiple fields into atomic deltas.

The Responses API emits typed SSE events (one type per event), so a compound DeltaMessage must be split before entering the state machine. Order: reasoning -> content -> tool_calls (grouped by index).