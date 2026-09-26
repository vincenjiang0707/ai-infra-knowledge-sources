source: https://docs.nvidia.com/dynamo/zh-CN/dev/multimodal/custom-vision-encoders
lastmod: 2026-09-23T23:30:39.914Z

# Custom Vision Encoders

A custom vision encoder lets an aggregated `dynamo.vllm`

worker use an author-provided vision tower or projector instead of vLLM’s built-in multimodal encoder. Use this path when the decoder can consume external vision features but the encoder is private, experimental, or otherwise unavailable in vLLM.

This is not encoder disaggregation: the encoder and language model run in the same worker process and share a GPU.

## Support Matrix

This matrix describes the custom-encoder integration, not the overall multimodal support of each backend. For feature requests, reach out in the `#sig-multimodal`

channel on our [community Slack](https://ai-dynamo.slack.com/).

## How It Works

Subclass `dynamo.vllm.multimodal_utils.custom_encoder.VisionEncoderBackend`

and implement its lifecycle hooks:

Dynamo owns concurrency, batching, and prompt preparation and calls each hook at the appropriate lifecycle stage.

### Batching

Dynamo uses eager batching without a collection timer. Whenever the encoder actor is free, it drains the items that are already waiting, calls `forward_batch()`

with them, and repeats. A lone item runs immediately; concurrent requests naturally form larger batches while an earlier forward is running.

Without preprocessing, every item has an implicit cost of `1`

, so `max_batch_cost = N`

acts as a limit of `N`

images per physical batch. To assign a different cost, enable `preprocess()`

and return `Preprocessed(item, cost=...)`

. Use `1`

for fixed, bounded inputs or a value proportional to visual patches or tokens for variable-size inputs.

### Preprocessing

Preprocessing is disabled by default. To enable preprocessing, override `preprocess()`

and set `preprocess_concurrency > 0`

. Use it to fetch, decode, resize, or patchify an image and to calculate its batching cost. Return `Preprocessed(item, cost)`

, where `item`

is the value that `forward_batch()`

should receive.

### Preparing the Engine Prompt

After `forward_batch()`

returns ordered artifacts, Dynamo uses the adapter selected from the resolved language model at startup to construct the final vLLM prompt. The prompt type is not selected per request.

`image_token_id`

is specific to the `EmbedsPrompt`

path and is not part of the universal backend contract. The `TokensPrompt`

path does not read it. Unsupported multimodal decoder architectures fail during adapter setup rather than falling back to `EmbedsPrompt`

.

## Enable Custom Encoder

From the repository root, launch the included aggregated path:

The launcher runs `Qwen/Qwen3.5-2B`

with `Qwen35VisionEncoder`

. The encoder demonstrates the lifecycle hooks by loading the Qwen3.5 vision tower, preprocessing images, and returning projected features through the native `TokensPrompt`

path. It favors readability over checkpoint-loading speed, caching, CUDA graphs, and production media handling.

Select your backend with a dotted Python class path:

The launcher passes `--custom-encoder-class`

, `--enable-multimodal`

, and the `--enable-mm-embeds`

flag required by the native VLM path. For a text-only decoder that uses `EmbedsPrompt`

, use `examples/custom_encoder/launch/agg_custom.sh`

instead.

The current integration has these restrictions:

- It supports the aggregated vLLM topology only.
- It consumes image URL content and cannot be combined with
`--frontend-decoding`

. - It runs on the token-in/token-out path and cannot be combined with
`--use-vllm-tokenizer`

. - The custom encoder and language model share GPU memory.

The Qwen3.5 example, reusable Qwen-family base, and semantic test backend are under [ examples/custom_encoder](https://github.com/ai-dynamo/dynamo/tree/main/examples/custom_encoder).

The backend owns any media retrieval performed by `preprocess()`

. Apply Dynamo’s [media URL policy](https://docs.nvidia.com/dynamo/dev/multimodal/overview), finite network timeouts, response-size limits, and image decode limits rather than fetching arbitrary request URLs directly.