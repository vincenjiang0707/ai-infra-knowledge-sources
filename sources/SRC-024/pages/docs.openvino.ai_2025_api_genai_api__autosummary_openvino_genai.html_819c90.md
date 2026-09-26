source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.html
lastmod: 

# openvino_genai[#](https://docs.openvino.ai#module-openvino_genai)

openvino genai module namespace, exposing pipelines and configs to create these pipelines.

Functions

|
device on which inference will be performed |
OpenVINO GenAI version |

Classes

Immutable LoRA Adapter that carries the adaptation matrices and serves as unique adapter identifier. |
|
Adapter config that defines a combination of LoRA adapters with blending parameters. |
|
Represents the mode of per-token score aggregation when determining least important tokens for eviction from cache |
|
AutoencoderKL class. |
|
CLIPTextModel class. |
|
CLIPTextModelWithProjection class. |
|
Configuration struct for the cache eviction algorithm. |
|
ChatHistory stores conversation messages and optional metadata for chat templates. |
|
Base class for chunk streamers. |
|
This class is used for generation with LLMs with continuous batchig |
|
This class wraps std::mt19937 pseudo-random generator. |
|
Structure to store resulting batched text outputs and scores for each batch. |
|
Structure to store resulting batched tokens and scores for each batch sequence. |
|
FluxTransformer2DModel class. |
|
Structure to keep generation config parameters. |
|
Members: |
|
GenerationResult stores resulting batched tokens and scores. |
|
Members: |
|
This class is used for storing pseudo-random generator. |
|
This class is used for generation with image-to-image models. |
|
This class is used for storing generation config for image generation pipeline. |
|
Holds performance metrics for each generate call. |
|
This class is used for generation with inpainting models. |
|
Represents the anchor point types for KVCrush cache eviction |
|
Configuration for KVCrush cache eviction algorithm |
|
This class is used for generation with LLMs |
|
Holds performance metrics for each generate call. |
|
Structure with raw performance metrics for each generation before any statistics are calculated. |
|
Structure with raw performance metrics for each generation before any statistics are calculated. |
|
SD3Transformer2DModel class. |
|
Scheduler for image generation pipelines. |
|
SchedulerConfig to construct ContinuousBatchingPipeline |
|
Configuration struct for the sparse attention functionality. |
|
Represents the mode of sparse attention applied during generation. |
|
Speech-generation specific parameters: :param minlenratio: minimum ratio of output length to input text length; prevents output that's too short. |
|
Structure with raw performance metrics for each generation before any statistics are calculated. |
|
StopCriteria controls the stopping condition for grouped beam search. |
|
Base class for streamers. |
|
Members: |
|
Structure to keep generation config parameters for structural tags in structured output generation. |
|
Configures structured output generation by combining regular sampling with structural tags. |
|
Structure to keep generation config parameters for structured output generation. |
|
T5EncoderModel class. |
|
This class is used for generation with text-to-image models. |
|
Structure that stores the result from the generate method, including a list of waveform tensors sampled at 16 kHz, along with performance metrics |
|
Text-to-speech pipeline |
|
Text embedding pipeline |
|
Base class for text streamers which works with parsed messages. |
|
Text rerank pipeline |
|
TextStreamer is used to decode tokens into text and call a user-defined callback function. |
|
The class is used to encode prompts and decode resulting tokens |
|
This class provides OpenVINO GenAI Generator wrapper for torch.Generator |
|
UNet2DConditionModel class. |
|
This class is used for generation with VLMs |
|
Whisper specific parameters: :param decoder_start_token_id: Corresponds to the ”< |
|
Structure with raw performance metrics for each generation before any statistics are calculated. |
|
Automatic speech recognition pipeline |
|
Structure with whisper specific raw performance metrics for each generation before any statistics are calculated. |