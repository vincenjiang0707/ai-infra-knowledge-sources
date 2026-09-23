source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/speech_to_text/realtime/serving/
lastmod: 2026-09-23

Bases: [GenerateBaseServing](../../../generate/base/serving/#vllm.entrypoints.generate.base.serving.GenerateBaseServing)


Realtime audio transcription service via WebSocket streaming.

Provides streaming audio-to-text transcription by transforming audio chunks into StreamingInput objects that can be consumed by the engine.

Methods:

Attributes:

## Source code in `vllm/entrypoints/speech_to_text/realtime/serving.py`


| class OpenAIServingRealtime(GenerateBaseServing):
"""Realtime audio transcription service via WebSocket streaming.
Provides streaming audio-to-text transcription by transforming audio chunks
into StreamingInput objects that can be consumed by the engine.
"""
def __init__(
self,
engine_client: EngineClient,
models: OpenAIServingModels,
*,
request_logger: RequestLogger | None,
):
super().__init__(
engine_client=engine_client,
models=models,
request_logger=request_logger,
)
self.task_type: Literal["realtime"] = "realtime"
logger.info("OpenAIServingRealtime initialized for task: %s", self.task_type)
@cached_property
def model_cls(self) -> type[SupportsRealtime]:
"""Get the model class that supports transcription."""
from vllm.model_executor.model_loader import get_model_cls
model_cls = get_model_cls(self.model_config)
return cast(type[SupportsRealtime], model_cls)
async def transcribe_realtime(
self,
audio_stream: AsyncGenerator[np.ndarray, None],
input_stream: asyncio.Queue[list[int]],
) -> AsyncGenerator[StreamingInput, None]:
"""Transform audio stream into StreamingInput for engine.generate().
Args:
audio_stream: Async generator yielding float32 numpy audio arrays
input_stream: Queue containing context token IDs from previous
generation outputs. Used for autoregressive multi-turn
processing where each generation's output becomes the context
for the next iteration.
Yields:
StreamingInput objects containing audio prompts for the engine
"""
model_config = self.model_config
renderer = self.renderer
# mypy is being stupid
# TODO(Patrick) - fix this
stream_input_iter = cast(
AsyncGenerator[PromptType, None],
self.model_cls.buffer_realtime_audio(
audio_stream, input_stream, model_config
),
)
async for prompt in stream_input_iter:
parsed_prompt = parse_model_prompt(model_config, prompt)
(engine_input,) = await renderer.render_cmpl_async([parsed_prompt])
yield StreamingInput(prompt=engine_input)
|

###

`model_cls`

`cached`

`property`


Get the model class that supports transcription.

###

`transcribe_realtime(audio_stream, input_stream)`

`async`


Transform audio stream into StreamingInput for engine.generate().

Parameters:

-
#### `audio_stream`


([AsyncGenerator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncGenerator)[[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray), None]

) – Async generator yielding float32 numpy audio arrays

-
#### `input_stream`


([Queue](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]

) – Queue containing context token IDs from previous generation outputs. Used for autoregressive multi-turn processing where each generation's output becomes the context for the next iteration.


Yields:

## Source code in `vllm/entrypoints/speech_to_text/realtime/serving.py`


| async def transcribe_realtime(
self,
audio_stream: AsyncGenerator[np.ndarray, None],
input_stream: asyncio.Queue[list[int]],
) -> AsyncGenerator[StreamingInput, None]:
"""Transform audio stream into StreamingInput for engine.generate().
Args:
audio_stream: Async generator yielding float32 numpy audio arrays
input_stream: Queue containing context token IDs from previous
generation outputs. Used for autoregressive multi-turn
processing where each generation's output becomes the context
for the next iteration.
Yields:
StreamingInput objects containing audio prompts for the engine
"""
model_config = self.model_config
renderer = self.renderer
# mypy is being stupid
# TODO(Patrick) - fix this
stream_input_iter = cast(
AsyncGenerator[PromptType, None],
self.model_cls.buffer_realtime_audio(
audio_stream, input_stream, model_config
),
)
async for prompt in stream_input_iter:
parsed_prompt = parse_model_prompt(model_config, prompt)
(engine_input,) = await renderer.render_cmpl_async([parsed_prompt])
yield StreamingInput(prompt=engine_input)
|