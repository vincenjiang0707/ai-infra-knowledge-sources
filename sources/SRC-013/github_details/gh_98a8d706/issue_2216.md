# [Issue #2216] [Feature]: Cut vLLM startup time in the optimized baseline (model cache PVC + streamed weight load + persistent compile cache)

source: https://github.com/llm-d/llm-d/issues/2216
state: open | updated: 2026-08-30T20:06:28Z
labels: 

## 正文

**Feature Area:** Optimized baseline

## Problem Statement

A vLLM replica cannot serve until it has fetched its weights, loaded them, and compiled its graphs. The optimized baseline pays full price for all three on every pod start: no `HF_HOME` or PVC, so each pod re-downloads the model from HuggingFace; no `--load-format`, so shards then load sequentially; and `/.cache` / `/.triton` are `emptyDir` ([patch-vllm.yaml#L73-L78](https://github.com/llm-d/llm-d/blob/main/guides/optimized-baseline/modelserver/gpu/vllm/base/patch-vllm.yaml#L73-L78)), so compile artifacts are thrown away. Together they dominate scale-up latency and rollout time.

## Proposed Solution

Three additions to the NVIDIA GPU vLLM manifests.

**1. Persist the model itself.** The guide currently has no model cache PVC, so weights are pulled from HuggingFace on every pod start. `guides/recipes/modelserver/components/model-cache` already provides this (RWX PVC, `HF_HOME=/model-cache`) but is only wired into the AMD CI overlay. Include it in the GPU overlay so the model downloads once and every later pod skips the download.

**2. Stream the weights.**

```yaml
- "--load-format=runai_streamer"
```

No image, env, or volume change: `runai-model-streamer` is already in the `vllm/vllm-openai` image, and the loader takes an HF model id or a local path.

**3. Persist the compile / CUDA graph cache** by pointing `VLLM_CACHE_ROOT` at a volume that outlives the pod:

```yaml
env:
  - name: VLLM_CACHE_ROOT
    value: /vllm-cache
volumeMounts:
  - { name: vllm-cache, mountPath: /vllm-cache }
volumes:
  - name: vllm-cache
    hostPath: { path: /var/tmp/vllm-compile-cache, type: DirectoryOrCreate }
```

The cache key includes the model config, so any flag change forces a fresh compile. No stale graphs.

These compound: (1) removes the download, (2) speeds up the load that follows it, (3) removes the recompile.

### Measurements

fp8 model, weights already on shared storage, pod start to ready:

| Configuration | Startup | Saved |
| --- | --- | --- |
| baseline | 22 min 13 s | - |
| `--load-format=runai_streamer` | 14 min 11 s | 8 min 02 s |
| streamer + persisted `VLLM_CACHE_ROOT` | 12 min 34 s | 9 min 39 s |

Weight load is 1.68x, bounded by storage bandwidth, not the client. Compile phase is 137 s to 36 s on a cache hit. Both scale with model size and shrink on local NVMe.

### Scope and open questions

- NVIDIA GPU vLLM only. Other accelerators use vendor images that may not carry the streamer.
- The model cache PVC needs an RWX default StorageClass, which is why the component is opt-in today. If that is too strong a requirement for the default guide, it can ship commented out with a note.
- For the compile cache, `hostPath` is what I measured, but it only hits on a node that already compiled that config and some clusters disallow it. An RWX PVC hits anywhere but has replicas writing concurrently on a cold cache, untested. Preference welcome.

## Alternatives Considered

Leaving these to users, or exposing them as tunables. None has a request-path effect or a measured downside on safetensors models, so defaults beat knobs. Users on custom images or non-safetensors checkpoints drop the arg.

## Additional Context

[vLLM Run:ai Model Streamer docs](https://docs.vllm.ai/en/stable/models/extensions/runai_model_streamer/). Prior art: [llm-d-deployer#317](https://github.com/llm-d/llm-d-deployer/issues/317), never landed, repo archived since July 2025.


## 评论 (7)

### wseaton · 2026-08-09

Hey @kfirtoledo, please take a look at this related guide PR: https://github.com/llm-d/llm-d/pull/1608


I also think https://github.com/scitix/InstantTensor is worth a quick look, it's supposed to be SOTA for naive disk loading. The modelexpress zero peer fallback has switched from modelstreamer to instanttensor.

### yitingdc · 2026-08-10

Hi, another complementary option is using [MatrixHub](https://github.com/matrixhub-ai/matrixhub) as an internal Hugging Face-compatible model source. By pointing HF_ENDPOINT to MatrixHub, the first pull is proxied and cached, while subsequent pulls are served internally. See the [vLLM integration guide](https://matrixhub.ai/docs/guides/use-with-vllm/) and [validated it with llm-d and Qwen3-32B](https://matrixhub.ai/blog/llmd-qwen3-32b-matrixhub-cache/).
This does not replace the PVC, streamed loading, or the local compile cache proposed here; it sits one layer above them and may be useful for private, air-gapped, or multi-cluster environments where models need to be distributed and governed centrally. 

### yiwxng · 2026-08-12

Hi, I'm new to this project, came from the Red Hat Open Source Hackathon with TD,  so I want to state my understanding first in case I've got something wrong.

As I understand it, the problem is that a vLLM pod can't serve until it has fetched its weights, loaded them, and compiled. right now none of that persists, so every pod pays the full cost on every start. The compile cache in particular is on emptyDir, so it's discarded when the pod goes away. Putting it on a volume that outlives the pod means the first pod does the work and later pods can reuse it.

My question is about the open item on hostPath vs. an RWX PVC. If several replicas start cold at the same time on a shared volume, do they coordinate on generating the compile cache, or could they all generate it at once? And if they do overlap, is there anything preventing a pod from reading a file another pod is still writing?

I ask because I have some experience with Kubernetes storage with AWS.  I worked on the Mountpoint S3 CSI driver as an EKS add-on, and one thing I've run into is that concurrent write safety depends a lot on what's behind the PVC. 
I think NFS and object-store-backed mounts behave quite differently.
Mountpoint for S3, for example, has no rename at all, and can't overwrite an existing object,  so the usual "write to temp then rename" pattern isn't available there.

Please feel free to correct any wrong assumptions. 

### kfirtoledo · 2026-08-12

ohh, @wseaton, @yitingdc, I wasn't aware of those solutions.
I think @wseaton, that the P2P weight-loading guide is great, but probably we need to have a reference to it from other places.

@yiwxng you're right; there's also a dependency on the PVC type and how many are read in parallel, but to be honest, as a user, I don't really care. I want a recipe (for my agent:) that, assuming I have a PVC with good performance, will reduce my initial startup time.
Maybe a good solution is a new guide with all the options for fast model-server initialization, like a P2P  weight-loading guide, or 
loading from PVC  or using  MatrixHub, and we can mention it in the optimize-baseline doc. @Gregory-Pereira , @vMaroon,  what do you think?

### RishabhSaini · 2026-08-12

>If several replicas start cold at the same time on a shared volume, do they coordinate on generating the compile cache, or could they all generate it at once? And if they do overlap, is there anything preventing a pod from reading a file another pod is still writing?

The compile cache uses [atomic writes](https://github.com/vllm-project/vllm/blob/main/vllm/compilation/compiler_interface.py#L244) (write-to-temp + [os.replace](https://github.com/vllm-project/vllm/blob/main/vllm/compilation/decorators.py#L706)) with deterministic cache keys, so concurrent cold-start pods produce identical artifacts and last-writer-wins safely. No coordination needed, no partial reads possible, as long as the RWX PVC backend supports rename (ex: NFS-backed storage, hostPath)

### robertgshaw2-redhat · 2026-08-19

IMO, Optimized startup time should be a feature/guide in-and-of-itself.

One thing that is important about the "Foundational" guides is that they are straightforward and focused on showing off an individual element of llm-d. So the spirit of the "optimized-baseline" guide should be about how to get good routing performance. If we start co-mingling too much stuff into the "Foundational" guides, we will lose the modularity that is making llm-d attractive (i.e. users can adoption functionality incrementally)

Now, this does not mean that llm-d's automation systems cannot implement these optimizations --- e.g. if we want to store models in a PVC in Ci/Cd then by all means make it happen. But the optimized-baseline guide should be focused on routing.

I think that we should have a full guide dedicated to fast model startup. It could explore:
- Tradeoffs between NVMe, PVC over NFS, S3 streaming
- JIT cache compilation
- P2P weight syncing via MX

We could even develop some subsystem for caching weights on NVMe drive across the cluster

### kfirtoledo · 2026-08-30

Totally agree @robertgshaw2-redhat, it should be in a different guide.
