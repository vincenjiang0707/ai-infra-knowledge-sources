source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/responses/api_router/
lastmod: 2026-09-23

Convert the generator to a stream of events in SSE format.

## Source code in `vllm/entrypoints/openai/responses/api_router.py`


| async def _convert_stream_to_sse_events(
generator: AsyncGenerator[StreamingResponsesResponse, None],
) -> AsyncGenerator[str, None]:
"""Convert the generator to a stream of events in SSE format."""
async for event in generator:
event_type = getattr(event, "type", "unknown")
# https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format
event_data = (
f"event: {event_type}\ndata: "
f"{event.model_dump_json(indent=None, by_alias=True)}\n\n"
)
yield event_data
|