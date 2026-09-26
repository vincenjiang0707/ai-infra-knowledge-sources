source: https://docs.nvidia.com/dynamo/dev/recipes/cli-templates/tensor-rt-llm
lastmod: 2026-09-24T19:58:16.636Z

TensorRT-LLM Local Deployment Examples


TensorRT-LLM Local Deployment Examples

Copyable commands for running the TensorRT-LLM launch scripts in the Dynamo repository.

Clone the NVIDIA Dynamo repository before running an example. The launch scripts load supporting
files through paths relative to `examples/backends/trtllm`

.

Review the selected script and confirm its model, GPU, and environment requirements before running the command. Set the environment variables defined at the top of a script to override its defaults.

## Aggregated

###### Single-Worker Text Generation


Starts the frontend and one TensorRT-LLM worker that handles both prefill and decode. Use it as the baseline local text-generation deployment.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

**Command-line flags:** `--enable-otel`

enables OpenTelemetry tracing.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Worker Metrics


Runs the baseline topology with the worker metrics configuration enabled. Use it to inspect TensorRT-LLM and Dynamo metrics during local testing.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### Image and Text Inputs


Starts one multimodal TensorRT-LLM worker for requests that combine media and text. Override the model and engine settings through the environment variables defined by the script.

The default model is `Qwen/Qwen2-VL-7B-Instruct`

.

**Configuration**

###### Cache-Aware Multimodal Routing


Places a multimodal router worker between the frontend and TensorRT-LLM. The router computes media hashes and uses cache overlap to select a backend worker.

The default model is `Qwen/Qwen3-VL-2B-Instruct`

.

**Configuration**

###### KV-Aware Load Balancing


Starts workers behind the KV router and publishes cache events for prefix-aware request placement. Use it to test cache reuse across replicated workers.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### KV Routing Without Cache Events


Runs the KV router in approximate mode, which predicts cache placement without consuming backend KV events. Use it when the workers cannot publish cache events.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

## Disaggregated

###### Dedicated Prefill and Decode Workers


Runs prefill and decode in separate TensorRT-LLM workers and transfers KV cache between them. Use it to tune or scale the two inference stages independently.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

**Command-line flags:** `--enable-otel`

enables OpenTelemetry tracing.

###### Cache-Aware Prefill Routing


Adds KV-aware placement to the disaggregated topology. Requests with reusable prefixes are routed to the prefill worker that is most likely to hold the matching cache blocks.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### Prefill and Decode on One GPU


Runs separate prefill and decode processes on one GPU with explicit KV-token limits. Use it for functional testing of disaggregation on a single-GPU host.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

**Command-line flags:** `--enable-otel`

enables OpenTelemetry tracing.

###### GPT-OSS on Multiple GPUs


Launches GPT-OSS 120B with one four-GPU prefill worker and one four-GPU decode worker. The complete topology requires eight GPUs.

The local model path defaults to `/model`

, and the served model name defaults to
`openai/gpt-oss-120b`

.

**Configuration**

## Multimodal and Diffusion

### Aggregated

###### Text-to-Image Generation


Starts an image-diffusion worker with FLUX as the default model. The default configuration uses one GPU.

The default model is `black-forest-labs/FLUX.2-klein-4B`

.

**Configuration**

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Text-to-Video Generation


Starts a video-diffusion worker with a Wan model as the default. The default configuration uses one GPU.

The default model is `Wan-AI/Wan2.1-T2V-1.3B-Diffusers`

.

**Configuration**

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

### Disaggregated

###### Dedicated Encoder with a Combined Language-Model Worker


Runs a vision encoder separately from a worker that performs both prefill and decode. The default Qwen vision-language configuration co-locates both workers on one GPU.

The default model is `Qwen/Qwen3-VL-2B-Instruct`

.

**Configuration**

###### Multimodal Prefill and Decode


Splits multimodal inference across prefill and decode workers while applying the script’s KV-cache settings to both stages. Use it to test multimodal KV transfer.

The default model is `Qwen/Qwen3-VL-2B-Instruct`

.

**Configuration**

###### Separate Encode, Prefill, and Decode Workers


Runs each multimodal stage in its own worker so encoding, prefill, and decode can be placed and tuned independently.

The default model is `meta-llama/Llama-4-Scout-17B-16E-Instruct`

.

**Configuration**

###### Image Inputs with Multimodal Embedding Transfer


Runs the encode-prefill-decode pipeline with the multimodal image and embedding-transfer path enabled. Use it to test transferring prepared media features between workers.

The default model is `Qwen/Qwen3-VL-2B-Instruct`

.

**Configuration**

## Source

Browse all [TensorRT-LLM launch scripts](https://github.com/ai-dynamo/dynamo/tree/main/examples/backends/trtllm/launch)
in the Dynamo repository.