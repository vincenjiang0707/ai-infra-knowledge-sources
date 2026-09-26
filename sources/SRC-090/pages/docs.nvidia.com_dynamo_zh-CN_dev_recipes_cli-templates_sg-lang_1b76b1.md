source: https://docs.nvidia.com/dynamo/zh-CN/dev/recipes/cli-templates/sg-lang
lastmod: 2026-09-23T23:30:39.914Z

# SGLang Local Deployment Examples

Clone the NVIDIA Dynamo repository before running an example. The launch scripts load supporting
files through paths relative to `examples/backends/sglang`

.

Review the selected script and confirm its model, GPU, and environment requirements before running the command. Pass supported flags after the script name to override its defaults.

## Aggregated

###### Single-Worker Text Generation


Starts the frontend and one SGLang worker that handles both prefill and decode. The default configuration uses one GPU and is the baseline local text-generation deployment.

The default model is `Qwen/Qwen3-0.6B`

. The script declares a GPU requirement of 1.

**Configuration**

**Command-line flags:** `--model-path`

sets the model path; `--enable-otel`

enables OpenTelemetry
tracing.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Agentic Workloads with Session Affinity


Starts a tensor-parallel worker behind session-aware routing with KV-event tracking, sticky sessions, reasoning parsing, and tool-call parsing. The default model uses two GPUs.

The default model is `zai-org/GLM-4.7-Flash`

. The default topology uses two GPUs because the model runs with `--tp 2`

.

**Configuration**

**Command-line flags:** `--model-path`

sets the model path; `--tp`

configures the corresponding
launch option.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Text Embeddings


Starts an SGLang embedding worker and exposes the OpenAI-compatible embeddings endpoint. Use it for vector search, retrieval, and other embedding workloads.

The default model is `Qwen/Qwen3-Embedding-4B`

. The script declares a GPU requirement of 1.

**Configuration**

**Command-line flags:** `--model-path`

sets the model path.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Cache-Aware Multimodal Routing


Routes multimodal requests by their text and media-derived cache keys so repeated images can reuse
cached work. This example requires the `mm-routing`

build feature and a compatible SGLang build.

The default model is `Qwen/Qwen3-VL-2B-Instruct`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path; `--num-workers`

sets the worker
count; `--single-gpu`

places workers on one accelerator.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### KV-Aware Load Balancing


Starts two workers behind the KV router and publishes cache events for prefix-aware request placement. The default topology uses two GPUs.

The default model is `Qwen/Qwen3-0.6B`

. The script declares a GPU requirement of 2.

**Configuration**

**Command-line flags:** `--enable-otel`

enables OpenTelemetry tracing; `--approx`

configures the
corresponding launch option.

###### Image and Video Inputs


Serves a vision-language model for image and video prompts. Pass `--frontend-decoding`

to decode
media in the Dynamo frontend and transfer the result to SGLang.

The default model is `Qwen/Qwen3-VL-2B-Instruct`

. The script declares a GPU requirement of 1.

**Configuration**

**Command-line flags:** `--model-path`

sets the model path; `--chat-template`

sets the backend chat
template; `--page-size`

sets the KV-cache page size; `--enable-otel`

enables OpenTelemetry tracing;
`--frontend-decoding`

moves media preprocessing into
the Dynamo frontend.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

## Disaggregated

###### Dedicated Prefill and Decode Workers


Runs prefill and decode on separate workers so each stage can be scaled and tuned independently. The default topology uses two GPUs and transfers KV cache between the workers.

The default model is `Qwen/Qwen3-0.6B`

. The script declares a GPU requirement of 2.

**Configuration**

**Command-line flags:** `--enable-otel`

enables OpenTelemetry tracing.

###### Independent Prefill and Decode Pools


Starts two prefill and two decode workers with KV-aware routing across both pools. Use this four-GPU example to test scaling and cache-aware placement.

The default model is `Qwen/Qwen3-0.6B`

. The script declares a GPU requirement of 4.

**Configuration**

**Command-line flags:** `--enable-otel`

enables OpenTelemetry tracing.

###### Prefill and Decode on One GPU


Runs separate prefill and decode processes on the same GPU with reduced memory limits. Use it for functional testing of the disaggregated path without a multi-GPU host.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path; `--single-gpu`

places workers
on one accelerator.

###### Separate Encode, Prefill, and Decode Workers


Splits vision encoding, language-model prefill, and decode into three workers. The default layout
uses three GPUs; `--single-gpu`

co-locates them for functional testing.

The default model is `Qwen/Qwen2.5-VL-7B-Instruct`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path; `--served-model-name`

sets the
model name exposed by the API; `--chat-template`

sets the backend chat template;
`--single-gpu`

places workers on one accelerator.

###### Dedicated Encoder with a Combined Language-Model Worker


Runs vision encoding separately from a worker that performs both prefill and decode. The default layout uses two GPUs, with a single-GPU mode available for functional testing.

The default model is `Qwen/Qwen2.5-VL-7B-Instruct`

. The default topology uses two GPUs; `--single-gpu`

co-locates both workers on one GPU.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path; `--served-model-name`

sets the
model name exposed by the API; `--chat-template`

sets the backend chat template;
`--single-gpu`

places workers on one accelerator.

## Diffusion

### Aggregated

###### Diffusion Language Models


Serves LLaDA-style language models that generate text through iterative refinement instead of autoregressive decoding. The default configuration uses one GPU.

The default model is `inclusionAI/LLaDA2.0-mini-preview`

. The script declares a GPU requirement of 1.

**Configuration**

###### Text-to-Image Generation


Starts an image-diffusion worker and serves the generation endpoint. The default FLUX model requires one GPU with enough memory for the model.

The default model is `black-forest-labs/FLUX.1-dev`

. The script declares a GPU requirement of 1.

**Configuration**

**Command-line flags:** `--model-path`

sets the model path; `--fs-url`

sets the generated-media
storage URL; `--http-url`

sets an optional base URL for serving generated images; `--http-port`

sets
the frontend HTTP port.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Text-to-Video Generation


Starts a video-generation worker for Wan models. Select the model size and generation settings with the script flags; the 14B option uses two GPUs.

The default model is `Wan-AI/Wan2.1-T2V-1.3B-Diffusers`

. The `--wan-size 1b`

mode uses one GPU, while `--wan-size 14b`

uses two GPUs.

**Configuration**

**Command-line flags:** `--wan-size`

selects the 1B or 14B Wan model; `--fs-url`

sets the
media-storage URL; `--http-port`

sets the frontend HTTP port; `--num-frames`

, `--height`

, and
`--width`

set video dimensions; `--num-inference-steps`

sets the denoising step count.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

## LoRA

The LoRA example also requires the setup described in the
[ launch/lora README](https://github.com/ai-dynamo/dynamo/blob/main/examples/backends/sglang/launch/lora/README.md).

### Aggregated

###### Dynamic LoRA Adapter Serving


Starts one SGLang worker with Low-Rank Adaptation (LoRA) support and loads adapters from the configured object store.

The script expects MinIO at `http://localhost:9000`

and loads adapters from the `my-loras`

bucket.
Run `launch/lora/setup_minio.sh --start`

first to start MinIO and upload the example adapter.

The default model is `Qwen/Qwen3-0.6B`

. The script declares a GPU requirement of 1.

**Configuration**

## Source

Browse all [SGLang launch scripts](https://github.com/ai-dynamo/dynamo/tree/main/examples/backends/sglang/launch)
in the Dynamo repository.