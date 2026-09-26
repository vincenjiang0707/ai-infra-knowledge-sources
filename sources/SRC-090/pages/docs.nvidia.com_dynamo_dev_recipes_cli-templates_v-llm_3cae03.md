source: https://docs.nvidia.com/dynamo/dev/recipes/cli-templates/v-llm
lastmod: 2026-09-24T19:58:16.636Z

# vLLM Local Deployment Examples

Clone the NVIDIA Dynamo repository before running an example. The launch scripts load supporting
files through paths relative to `examples/backends/vllm`

.

Review the selected script and confirm its model, accelerator, and environment requirements before running the command. Pass supported flags after the script name or set its documented environment variables to override defaults.

## Aggregated

###### Single-Worker Text Generation


Starts the frontend and one vLLM worker that handles both prefill and decode. The default configuration uses one GPU and is the baseline local text-generation deployment.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Text Embeddings


Starts a vLLM pooling worker and exposes the OpenAI-compatible embeddings endpoint. Use it for vector search, retrieval, and other embedding workloads.

The default model is `Qwen/Qwen3-Embedding-0.6B`

. The script declares a GPU requirement of 1.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Embedding Load Balancing and Model Dispatch


Starts two embedding workers behind one frontend. Use identical model arguments to test load balancing, or different models to test model-name-based request dispatch.

The script declares a GPU requirement of 2.

**Configuration**

**Positional and pass-through arguments:** Supply two model names. Any remaining arguments are
forwarded to both vLLM workers.

###### Sequence Classification and Pooling


Starts a vLLM pooling worker that registers both pooling-family model types, so the frontend mounts
the OpenAI-compatible `/v1/classify`

and `/v1/pooling`

endpoints. Use it for sequence
classification, reranking, and raw pooled-tensor workloads.

The default model is `cross-encoder/nli-MiniLM2-L6-H768`

, a three-class NLI cross-encoder. The
script declares a GPU requirement of 1.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Image and Video Inputs


Serves a multimodal model with media preprocessing in the Dynamo frontend and one vLLM worker. Use it as the baseline image or video deployment.

The default model is `Qwen/Qwen3-VL-30B-A3B-Instruct-FP8`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Cache-Aware Multimodal Routing


Expands media placeholders into routing tokens, hashes each media item, and routes requests by text and media cache overlap. This path uses the Rust multimodal router in the frontend.

The default model is `Qwen/Qwen3-VL-2B-Instruct`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path; `--num-workers`

sets the worker
count; `--single-gpu`

places workers on one accelerator.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Multimodal Routing with vLLM Preprocessing


Uses vLLM’s Python chat processor in the frontend to expand media tokens and compute media hashes for KV routing. The script launches the requested frontend and worker replicas, but requires NATS and etcd to be running before it starts.

The default model is `Qwen/Qwen3-VL-2B-Instruct`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path; `--num-workers`

sets the worker
count; `--single-gpu`

places workers on one accelerator.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Request-Plane Transport Modes


Starts the baseline worker through the request-plane mode selected by the script flags. Use it to compare or validate the available frontend-to-worker transports.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

**Command-line flags:** `--tcp`

uses the TCP request plane (the default); `--nats`

uses the NATS
request plane.

###### KV-Aware Load Balancing


Starts two workers behind the KV router and publishes cache events over ZeroMQ (ZMQ) for prefix-aware placement. The default topology uses two GPUs.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### KV Routing Without Cache Events


Runs the KV router in approximate mode, which predicts cache placement without consuming backend KV events. Use it when event publishing is unavailable.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### Replicated Frontends and Routers


Starts two frontend and KV-router replicas on separate ports while sharing routing state. Use it to exercise multiple ingress replicas against the same worker pool.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### Speculative Decoding with EAGLE


Runs `meta-llama/Meta-Llama-3.1-8B-Instruct`

with the
`yuhuili/EAGLE3-LLaMA3.1-Instruct-8B`

draft model on one GPU. The worker uses the `eagle3`

method and
proposes two speculative tokens per step.

The default model is `meta-llama/Meta-Llama-3.1-8B-Instruct`

.

**Configuration**

###### OpenTelemetry Tracing


Enables tracing on the frontend and worker so requests appear in the local observability stack. Start the tracing stack before running this example.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Data-Parallel Attention and Expert Parallelism


Starts multiple data-parallel workers for a Mixture-of-Experts model and lets Dynamo route among the data-parallel ranks. The default Qwen configuration uses four GPUs.

The default model is `Qwen/Qwen3-30B-A3B`

.

**Configuration**

###### Multi-Node DeepSeek-R1 Expert Parallelism


Runs DeepSeek-R1 with data-parallel attention and expert parallelism across multiple nodes. Each node starts its assigned data-parallel ranks and joins the same distributed worker group.

The default model is `deepseek-ai/DeepSeek-R1`

.

**Configuration**

**Command-line flags:** `--num-nodes`

sets the total node count; `--node-rank`

sets this node’s
rank; `--gpus-per-node`

sets the GPU count on each node; `--master-addr`

sets the distributed
rendezvous address; `--log-dir`

sets the log directory; `--model`

sets the model identifier or path.

Replace `192.0.2.10`

with the head node’s reachable IP address. Run on the head node:

Run on the second node:

###### Tensor Parallelism Across Nodes


Runs one tensor-parallel vLLM worker across a head node and a worker node using vLLM multiprocessing. Use it when the tensor-parallel size exceeds the GPUs available on one host.

The default model is `meta-llama/Llama-3.1-8B-Instruct`

. The script requires eight GPUs on each of
two nodes, with NATS and etcd reachable from the head node.

**Configuration**

**Command-line flags:** `--head`

starts the head-node process; `--worker`

starts a worker-node
process; `--head-ip`

sets the reachable head-node IP address.

Replace `192.0.2.10`

with the head node’s reachable IP address. Run on the head node:

Run the worker command on the second node:

## Disaggregated

###### Dedicated Prefill and Decode Workers


Runs prefill and decode in separate vLLM workers and transfers KV cache through NIXL.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### Dedicated Encoder with a Combined Language-Model Worker


Runs media encoding separately from a worker that performs both prefill and decode. Use it when encoding should scale independently but language-model stages can remain together.

The default model is `Qwen/Qwen3-VL-30B-A3B-Instruct-FP8`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path; `--single-gpu`

places workers
on one accelerator.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Separate Encode, Prefill, and Decode Workers


Splits multimodal inference into dedicated encode, prefill, and decode workers. The script offers single-GPU and two-GPU modes for functional testing in addition to the full layout.

The default model is `llava-hf/llava-1.5-7b-hf`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path; `--single-gpu`

places workers
on one accelerator; `--two-gpu`

places encode and prefill on GPU 0 and decode on GPU 1.

###### Multimodal Prefill and Decode Without a Separate Encoder


Runs a two-worker multimodal topology in which the prefill worker also performs vision encoding. It uses fewer processes than encode-prefill-decode at the cost of more work on prefill.

The default model is `Qwen/Qwen3-VL-2B-Instruct`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path; `--single-gpu`

places workers
on one accelerator.

###### Independent Prefill and Decode Pools


Routes requests across separate prefill and decode pools using cache events from the workers. The frontend also discovers prefill workers and activates its internal prefill router.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### KV-Aware Routing on Intel Gaudi


Runs the disaggregated KV-routing topology with the device settings required for Intel Gaudi accelerators.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### Prefill and Decode on One GPU


Runs separate prefill and decode processes on the same GPU with reduced model-length and concurrency limits. Use it for functional testing of KV transfer without a multi-GPU host.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### OpenTelemetry Tracing Across Prefill and Decode


Enables tracing on the frontend, prefill worker, and decode worker so a request can be followed across the full disaggregated path. Start the tracing stack first.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path.

## KV Cache Offloading

### Aggregated

###### FlexKV Offloading for One Worker


Enables FlexKV on a worker that handles both prefill and decode. Use it to test external KV-cache storage without a router.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### FlexKV Offloading with KV Routing


Combines FlexKV with KV-aware routing so the frontend places requests by cache locality while workers offload cache blocks.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### KV Block Manager Offloading for One Worker


Enables the KV Block Manager (KVBM) on a single worker and configures CPU-backed cache capacity. Use it to test local KV-cache offloading.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### KV Block Manager Offloading with KV Routing


Starts multiple KVBM-enabled workers behind the KV router. Each worker uses distinct event and coordination ports so the router can track its cache state.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### LMCache Offloading for One Worker


Connects one vLLM worker to LMCache through the in-process connector. Use it as the baseline LMCache deployment.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### Out-of-Process LMCache Server


Starts an LMCache server as a separate process and connects the vLLM worker through the multiprocess connector. Use it to isolate cache management from the inference worker.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### LMCache with Multiprocess Metrics


Runs the in-process LMCache connector while configuring a Prometheus multiprocess directory. Use it to validate metric collection in a multi-process-style environment.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

### Disaggregated

###### FlexKV on the Prefill Worker


Runs separate prefill and decode workers and enables FlexKV on prefill. Use it to test offloading cache created during prompt processing before transfer to decode.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### KV Block Manager on the Prefill Worker


Runs separate prefill and decode workers with KVBM enabled on prefill and CPU cache storage. Decode receives the transferred KV state without enabling KVBM.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### Two Prefill and Two Decode Workers with KVBM


Scales the KVBM topology to two prefill and two decode workers behind the KV router. Distinct barrier identifiers keep the prefill workers’ offload coordination separate.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### KVBM with Cache-Aware Pool Routing


Combines separate prefill and decode pools, KV-aware routing, and KVBM-backed offloading. Use it to test cache placement and offload behavior together.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### LMCache on the Prefill Worker


Runs separate prefill and decode workers and enables LMCache on prefill. Use it to test LMCache-backed prompt-cache offloading in a disaggregated topology.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

## vLLM-Omni

### Aggregated

###### Audio Generation


Starts a vLLM-Omni worker for audio generation. Override the default model and generation settings through the script flags.

The default model is `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

The same script serves Nemotron Audex, which runs a two-stage pipeline: stage 0 is the thinker that emits speech codec tokens, and stage 1 decodes those tokens to a 16 kHz mono waveform.

Audex serves a single built-in voice, so the request contract differs from Qwen3-TTS: the handler
accepts `voice`

only when it is omitted or set to `default`

, rejects `ref_audio`

and `ref_text`

,
and accepts an optional `nvext.cfg_scale`

for classifier-free guidance. The printed curl example adapts to the selected model. See
[Text-to-Audio](https://docs.nvidia.com/dynamo/dev/diffusion/text-to-audio) for the request format.

Both Audex checkpoints report the same model type, so the 30B-A3B needs an explicit stage configuration. Otherwise auto-detection selects the 2B-tuned file. vLLM-Omni ships the configuration, so resolve it from the installed package and pass it through to the worker:

###### Image-to-Video Generation


Starts a vLLM-Omni image-to-video pipeline with a Wan model by default. Pass a different model or worker arguments through the script options.

The default model is `Wan-AI/Wan2.2-TI2V-5B-Diffusers`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Text-to-Image Generation


Starts a vLLM-Omni image-generation worker and exposes the generation endpoint. Use the script flags to select the model.

The default model is `Qwen/Qwen-Image`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Text-to-Video Generation


Starts a vLLM-Omni video-generation worker and exposes the generation endpoint. Use the script flags to select the model and generation settings.

The default model is `Wan-AI/Wan2.1-T2V-1.3B-Diffusers`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

### Disaggregated

###### Two-Stage GLM-Image Generation


Splits GLM-Image across an autoregressive stage and a diffusion stage on separate GPUs. A router coordinates the intermediate token output and final image response.

The default model is `zai-org/GLM-Image`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path; `--stage-configs-path`

sets the diffusion stage-configuration file.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

## LoRA

### Aggregated

###### Dynamic LoRA Adapter Serving


Starts one vLLM worker with Low-Rank Adaptation (LoRA) support and loads adapters from the configured object store.

The script expects MinIO at `http://localhost:9000`

and loads adapters from the `my-loras`

bucket.
Run `launch/lora/setup_minio.sh --start`

first to start MinIO and upload the example adapter.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### LoRA Adapters with KV-Aware Routing


Starts LoRA-capable workers behind the KV router. Use it to test adapter selection together with prefix-cache-aware request placement.

The script expects MinIO at `http://localhost:9000`

and loads adapters from the `my-loras`

bucket.
Run `launch/lora/setup_minio.sh --start`

first to start MinIO and upload the example adapter.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### Multimodal LoRA Adapters


Serves a multimodal model with dynamically selected LoRA adapters. Use it for image-and-text requests that require adapter-specific behavior.

The default model is `Qwen/Qwen3-VL-2B-Instruct`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

## XPU

### Aggregated

###### LoRA Adapters with KV-Aware Routing


Runs LoRA-capable vLLM workers on Intel XPU devices behind the KV router.

The script expects MinIO at `http://localhost:9000`

and loads adapters from the `my-loras`

bucket.
Run `launch/lora/setup_minio.sh --start`

first to start MinIO and upload the example adapter.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### Dynamic LoRA Adapter Serving


Runs one LoRA-capable vLLM worker on an Intel XPU device.

The script expects MinIO at `http://localhost:9000`

and loads adapters from the `my-loras`

bucket.
Run `launch/lora/setup_minio.sh --start`

first to start MinIO and upload the example adapter.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### LMCache with Multiprocess Metrics


Runs LMCache on Intel XPU while configuring the Prometheus multiprocess directory used by multi-process deployments.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### LMCache Offloading


Connects a vLLM worker on Intel XPU to LMCache for KV-cache offloading.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### Multimodal Routing with vLLM Preprocessing


Uses vLLM’s Python chat processor on the frontend and routes multimodal requests to workers on Intel XPU devices. The script requires NATS and etcd to be running before it starts.

The default model is `Qwen/Qwen3-VL-2B-Instruct`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path; `--num-workers`

sets the worker
count; `--single-gpu`

places workers on one accelerator.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Cache-Aware Multimodal Routing


Uses the Rust multimodal routing path to place image and text requests across vLLM workers on Intel XPU devices.

The default model is `Qwen/Qwen3-VL-2B-Instruct`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path; `--num-workers`

sets the worker
count; `--single-gpu`

places workers on one accelerator.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Image and Video Inputs


Serves multimodal requests with frontend media preprocessing and one vLLM worker on an Intel XPU device.

The default model is `Qwen/Qwen3-VL-8B-Instruct`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

###### Request-Plane Transport Modes


Runs the selected frontend-to-worker request-plane transport with a vLLM worker on Intel XPU.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

**Command-line flags:** `--tcp`

uses the TCP request plane (the default); `--nats`

uses the NATS
request plane.

###### KV Routing Without Cache Events


Uses approximate cache tracking to route requests across vLLM workers on Intel XPU without backend KV events.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### KV-Aware Load Balancing


Runs vLLM workers on Intel XPU behind the KV router and publishes cache events for prefix-aware placement.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

###### Single-Worker Text Generation


Starts the frontend and one vLLM worker on an Intel XPU device. Use it as the baseline XPU text-generation deployment.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path.

**Pass-through arguments:** Additional unrecognized arguments are forwarded to the backend worker command.

### Disaggregated

###### Separate Encode, Prefill, and Decode Workers


Splits multimodal inference into encode, prefill, and decode workers on Intel XPU devices, with a single-device mode for functional testing.

The default model is `llava-hf/llava-1.5-7b-hf`

.

**Configuration**

**Command-line flags:** `--model`

sets the model identifier or path; `--single-gpu`

places workers
on one accelerator.

###### KV Routing with Direct Device Transfer


Runs separate prefill and decode pools on Intel XPU with KV-aware routing and direct device-memory transfer between workers.

The default model is `Qwen/Qwen3-0.6B`

.

**Configuration:** This script does not define user-facing environment-variable overrides.

## Source

Browse all [vLLM launch scripts](https://github.com/ai-dynamo/dynamo/tree/main/examples/backends/vllm/launch)
in the Dynamo repository.