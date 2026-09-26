source: https://docs.nvidia.com/dynamo/zh-CN/dev/recipes/inkling
lastmod: 2026-09-24T19:58:16.636Z

# Inkling NVFP4

Serve Thinking Machines’ Inkling on GB300 with vLLM for long-context agentic workloads, or on B200 with SGLang for multimodal input.

Deployments for `thinkingmachines/Inkling-NVFP4`

— the NVFP4-quantized checkpoint of Thinking Machines Lab’s first open-weights model, a Mixture-of-Experts that reasons natively with controllable reasoning effort. Two stacks, aimed at different jobs. **GB300 with vLLM** targets an agentic workload (64K median ISL, 400 median OSL, 90% KV cache hit) at 1M context with MTP speculative decoding and KV-aware routing, aggregated or disaggregated. **B200 with SGLang** is the day-0 profile and the only one that serves image and audio input. Pick your target; every command on this page updates to match.

Choose your deployment target

**Checkpoint**thinkingmachines/Inkling-NVFP4 (~592 GB)

**Precision**NVFP4 (

`modelopt_fp4`

)**GPUs**4x GB300 per replica,

`replicas: 2`

(8x)**Parallelism**TP4

**Context**1,048,576

**Spec decode**MTP, 8 draft tokens

**Routing**KV-aware

**Checkpoint**thinkingmachines/Inkling-NVFP4 (~592 GB)

**Precision**NVFP4 (

`modelopt_fp4`

)**GPUs**4x GB300 prefill + 4x GB300 decode

**Parallelism**TP4 per worker

**Context**1,048,576

**Spec decode**MTP, 8 draft tokens

**Routing**KV-aware, NIXL over MNNVL or RDMA

**Checkpoint**thinkingmachines/Inkling-NVFP4 (~592 GB)

**Precision**NVFP4 (

`modelopt_fp4`

)**GPUs**8x B200, one TP8 worker

**Techniques**EAGLE speculative decoding, FA4 attention, Mamba radix cache

**Modalities**Text + image + audio input, text output

**Not available**The SGLang B200 profile is aggregated only. Select GB300 for a disaggregated deployment.

## Prerequisites

- A Kubernetes cluster with the Dynamo platform installed and
**8x GB300**available — see the[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - A Hugging Face token (the model is public, but a token avoids rate limits).

- A Kubernetes cluster with the Dynamo platform installed and
**8x B200**available on one node — see the[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart). - An image pull secret with access to the runtime image registry.
- A Hugging Face token (the model is public, but a token avoids rate limits).

- The NVIDIA DRA driver installed cluster-wide, so the recipe’s
`ComputeDomain`

can allocate an MNNVL channel to each worker. Both variants use Dynamic Resource Allocation; the`aws-roce`

variant also declares a`resource.k8s.io/v1`

`ResourceClaimTemplate`

and so needs Kubernetes 1.34 or later.

Create the namespace and secrets:

Update `storageClassName`

in `model-cache/model-cache.yaml`

to match your cluster (`kubectl get storageclass`

) before applying. The checkpoint is ~592 GB — the download job can take a while. On clusters that already provide a shared RWX PVC, skip the cache step and replace the `model-cache`

claim name in the manifests with the shared PVC name.

## Deploy

Prepare the model cache and download the checkpoint:

Then deploy:

The disaggregated profile ships as Kustomize variants, because the fabric that carries KV from prefill to decode is a cluster property. The `generic`

variant moves KV over MNNVL `cuda_ipc`

inside the ComputeDomain and carries the NIXL control plane over TCP. The `aws-roce`

variant adds a RoCE device claim on clusters that expose one through Dynamic Resource Allocation:

To compose a different fabric, apply the checked-in overlay and add your own Component rather than editing the rendered manifest:

## Smoke Test

Forward the frontend port:

### Text

Inkling reasons before answering, so a small `max_tokens`

is spent entirely on reasoning and returns empty `content`

with `finish_reason: "length"`

. The answer may also land in `reasoning_content`

rather than `content`

.

### Reasoning effort

Inkling’s controllable thinking is exposed per request: pass `reasoning_effort`

as a named level (`none`

/ `minimal`

/ `low`

/ `medium`

/ `high`

/ `max`

) or a float in `[0.0, 0.99]`

; omitted requests default to `0.9`

(high). These are the values in this checkpoint’s chat template — `xhigh`

from the launch blog is not in its map and is rejected:

### Image

Images ride as an `image_url`

content part — a public HTTP(S) URL (the worker pod fetches it, so it needs egress) or a base64 `data:`

URI:

### Audio

Audio rides as an `audio_url`

content part, same URL-or-data-URI rule. Inkling expects 16 kHz audio; WAV is ideal, and MP3/FLAC/OGG also decode in this image. This sample is 16 kHz mono WAV, matching the model card spec:

For air-gapped clusters, send local files as `data:`

URIs instead. Encode to a single line first (`base64`

wraps output by default, which breaks the JSON payload): `AUDIO_B64=$(base64 < sample.wav | tr -d '\n')`

, then `{"type": "audio_url", "audio_url": {"url": "data:audio/wav;base64,'"${AUDIO_B64}"'"}}`

. Multiple media parts can ride in one message as the context budget allows.

## Performance

Measured with the [AIPerf](https://github.com/ai-dynamo/aiperf) trace-replay Job in [ recipes/inkling/perf](https://github.com/ai-dynamo/dynamo/blob/main/recipes/inkling/perf/README.md), replaying a 3,541-request agentic trace against the SLO pair

`user_tps p50 >= 50`

and `TTFT p50 <= 5000 ms`

. Both topologies clear both gates.Measured on the `aws-roce`

fabric variant.

Aggregated outperformed every disaggregated split tested on this workload. Prefill is only about 5% of the GPU-time budget here, so dedicating half the fleet to it costs more per-GPU throughput than the prefill/decode separation returns. Choose the disaggregated profile when you need to scale prefill and decode independently, not for throughput on this trace.

## Notes

- Image and audio input are not supported: the Dynamo vLLM runtime has no multimodal support for this model yet, so these profiles are text-only. Use the B200 SGLang profile for image and audio. Do not set
`--enable-multimodal`

to work around it — the flag only lifts the request rejection, so media is still never encoded and requests return HTTP 200 with an answer invented from the text prompt alone. - Some OpenAI API fields are rejected rather than silently ignored, each with a message naming the reason.
`min_p`

and`logit_bias`

return 400 — unsupported with speculative decoding, and these profiles run MTP 8; remove`--speculative-config`

to use them.`logprobs`

and`top_logprobs`

return 400, not implemented on the Dynamo vLLM chat processor. The Responses API is stateless:`previous_response_id`

returns 501,`GET /v1/responses/{id}`

returns 404, and`store: true`

is echoed back but not persisted. - Inkling reasons before answering, so a low
`max_tokens`

can be spent entirely on reasoning, returning empty`content`

with`finish_reason: "length"`

. Allow roughly 1500, and read the answer from`content`

,`reasoning_content`

, or`reasoning`

. `--kv-cache-memory-bytes`

is required. Sizing the KV cache from`--gpu-memory-utilization`

alone leaves too little headroom at 1M context and OOMs during CUDA graph capture. The value is measured for 288 GB GB300; re-measure it if you change the context length or GPU.`--max-model-len 1048576`

keeps the model’s full 1M context available. Lowering it frees KV headroom if you do not need it.- Reasoning and tool calling use the model’s dedicated parsers, wired in both the frontend and the worker (
`--reasoning-parser inkling --tool-call-parser inkling`

). - MTP speculative decoding runs at 8 draft tokens on both topologies. Remove
`--speculative-config`

to run without it.

- This is a Day-0 recipe on a dedicated dev runtime image (
`sglang-runtime:1.4.0-inkling-dev.1`

, a custom SGLang build carrying the Inkling model support); it is functional but not yet promoted to a release runtime image, and no benchmark results are published yet. - Audio input: the model card specifies WAV sampled at 16 kHz, ideally under 20 minutes. The runtime image ships without royalty-bearing media codecs — AAC/
`.m4a`

decode is not included; other common formats (WAV, FLAC, OGG/Opus, MP3) decode via`libsndfile`

. Image input is unaffected. - Video input is not supported in this recipe: the model card notes video handling exists for downstream fine-tuning but is unevaluated out of the box.
- Reasoning and tool calling use the model’s dedicated parsers, wired in both the frontend and the worker (
`--reasoning-parser inkling --tool-call-parser inkling`

). - EAGLE speculative decoding is enabled by default in the deploy manifest (multi-layer, 8 steps, rejection sampling); remove the
`--speculative-*`

flags to run without it. - The manifest sets
`DYN_FORWARDPASS_METRIC_PORT`

to an empty value — a deliberate workaround that keeps forward-pass metrics off, because this rc image crashes on EAGLE batches when they are enabled. Keep it (and don’t set that variable) until a fixed image ships. - The worker enables the Mamba radix cache (
`extra_buffer`

strategy) and FlashInfer TRT-LLM GEMM/MoE backends; these flags are part of the validated configuration — change them only deliberately.

## Source

- Source README:
[recipes/inkling/README.md](https://github.com/ai-dynamo/dynamo/blob/main/recipes/inkling/README.md) - vLLM aggregated GB300:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/inkling/vllm/agg-gb300-agentic/deploy.yaml) - vLLM disaggregated GB300:
[deploy-generic.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/inkling/vllm/disagg-gb300-agentic/deploy-generic.yaml)and[deploy-aws-roce.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/inkling/vllm/disagg-gb300-agentic/deploy-aws-roce.yaml) - SGLang aggregated B200:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/inkling/sglang/agg-b200/deploy.yaml) - Benchmark:
[recipes/inkling/perf](https://github.com/ai-dynamo/dynamo/blob/main/recipes/inkling/perf/README.md) - Setup assets:
[model-cache.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/inkling/model-cache/model-cache.yaml)and[model-download.yaml](https://github.com/ai-dynamo/dynamo/blob/main/recipes/inkling/model-cache/model-download.yaml) - Model announcement:
[Inkling — Thinking Machines Lab](https://thinkingmachines.ai/news/introducing-inkling/)