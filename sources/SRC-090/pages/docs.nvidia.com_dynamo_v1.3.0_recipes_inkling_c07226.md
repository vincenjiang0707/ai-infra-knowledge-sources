source: https://docs.nvidia.com/dynamo/v1.3.0/recipes/inkling
lastmod: 2026-09-24T19:58:16.636Z

# Inkling NVFP4

Day-0 SGLang recipe for Thinking Machines’ Inkling on 8x B200.

Day-0 aggregated SGLang deployment for `thinkingmachines/Inkling-NVFP4`

— the NVFP4-quantized checkpoint of Thinking Machines Lab’s first open-weights model, a Mixture-of-Experts that reasons natively over text, image, and audio input with controllable reasoning effort. One TP8 worker on 8x B200 with EAGLE speculative decoding, FA4 attention, and the Inkling reasoning and tool-call parsers wired end to end.

Deployment target

**Checkpoint**thinkingmachines/Inkling-NVFP4 (~592 GB)

**Precision**NVFP4 (modelopt_fp4)

**GPUs**8x B200, one TP8 worker

**Techniques**Aggregated serving, EAGLE speculative decoding, FA4 attention, Mamba radix cache

**Modalities**Text + image + audio input, text output

## Prerequisites

- A Kubernetes cluster with the Dynamo platform installed and
**8x B200**available on one node — see the[Kubernetes Deployment Guide](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/kubernetes-quickstart). - An image pull secret with access to the runtime image registry.
- A Hugging Face token (the model is public, but a token avoids rate limits).

Create the namespace and secrets:

Update `storageClassName`

in `model-cache/model-cache.yaml`

to match your cluster (`kubectl get storageclass`

) before applying. The checkpoint is ~592 GB — the download job can take a while. On clusters that already provide a shared RWX PVC, skip the cache step and replace the `model-cache`

claim name in the manifests with the shared PVC name.

## Deploy

Prepare the model cache and download the checkpoint:

Then deploy:

## Smoke Test

Inkling accepts text, image, and audio input in a single OpenAI-compatible API. First, forward the frontend port:

### Text

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

## Notes

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
[recipes/inkling/README.md](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/inkling/README.md) - SGLang aggregated B200:
[deploy.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/inkling/sglang/agg-b200/deploy.yaml) - Setup assets:
[model-cache.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/inkling/model-cache/model-cache.yaml)and[model-download.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/recipes/inkling/model-cache/model-download.yaml) - Model announcement:
[Inkling — Thinking Machines Lab](https://thinkingmachines.ai/news/introducing-inkling/)