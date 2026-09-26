source: https://github.com/ai-dynamo/dynamo/releases

# Releases: ai-dynamo/dynamo

## Release list

## Dynamo v1.5.0

**Dynamo v1.5.0 - Release Notes**

Dynamo v1.5.0 is the 18th feature release of the open-source distributed inference platform, spanning 658 merged PRs from 123 contributors. It opens **Dynamo Router** worker selection to custom scoring and picking policies and extends KV indexing to Mooncake and disk tiers. KVBM is deprecated, with removal targeted for v1.6.0. **Dynamo Frontend** streams guided tool calls by default and rejects over-context requests before the first token, and multimodal encode-prefill-decode deployments can decode images once at the Frontend. On Kubernetes, `nvidia.com/v1beta1`

becomes the CRD storage version, the Rust Endpoint Picker replaces the Go EPP, and Dynamo Snapshot moves to a standalone operator. TLS and mutual TLS now cover the TCP and NATS transports. AIConfigurator becomes ** AISimulate** and ships as its own package, and the engines move to SGLang v0.5.18, TensorRT-LLM v1.3.0rc25, and vLLM v0.28.0.

**Summary**

**Dynamo Router: Custom Selection Policies & Tiered KV Indexing**

Worker selection is now pluggable. Native scorer and picker policies run through the same host selection path as the built-in selector, so discovery, eligibility, reservations, metrics, and dispatch stay in Dynamo while the policy decides which worker wins ([#12526](https://github.com/ai-dynamo/dynamo/pull/12526), [#12585](https://github.com/ai-dynamo/dynamo/pull/12585)). Composable worker filters run after built-in eligibility and before scoring ([#12896](https://github.com/ai-dynamo/dynamo/pull/12896)), and session affinity comes in hard and soft forms ([#13907](https://github.com/ai-dynamo/dynamo/pull/13907)).

On the indexing side, Dynamo Router consumes Mooncake shared-cache events for SGLang HiCache without HTTP queries on the hot path ([#11239](https://github.com/ai-dynamo/dynamo/pull/11239)) and routes vLLM storage KV events to a disk tier with locality gating ([#11571](https://github.com/ai-dynamo/dynamo/pull/11571)). A conditional disaggregation bypass sends short requests straight to decode ([#11723](https://github.com/ai-dynamo/dynamo/pull/11723), [#11725](https://github.com/ai-dynamo/dynamo/pull/11725)).

**Dynamo Frontend: Guided Tool Calls, Thinking Controls & Request Validation**

Guided tool calls stream incrementally by default, and Qwen3 joins the v2 unified tool-call parser ([#12576](https://github.com/ai-dynamo/dynamo/pull/12576), [#13340](https://github.com/ai-dynamo/dynamo/pull/13340)). Thinking and reasoning controls resolve once with a single precedence and apply to every chat-template key, with deployment-level defaults and an explicit `enable_thinking`

gate for Gemma 4 ([#11047](https://github.com/ai-dynamo/dynamo/pull/11047), [#11739](https://github.com/ai-dynamo/dynamo/pull/11739), [#13061](https://github.com/ai-dynamo/dynamo/pull/13061)). Bad requests now fail with the right status: over-context requests are rejected before the stream opens, validation failures return HTTP 400, and backend overloads keep their 503 ([#12092](https://github.com/ai-dynamo/dynamo/pull/12092), [#12155](https://github.com/ai-dynamo/dynamo/pull/12155), [#12412](https://github.com/ai-dynamo/dynamo/pull/12412)). The Frontend loads pluggable tokenizer backends, including one from Baseten, with a configurable Hugging Face fallback ([#12376](https://github.com/ai-dynamo/dynamo/pull/12376), [#12923](https://github.com/ai-dynamo/dynamo/pull/12923)).

**Multimodal: Frontend Image Decoding, Video-Aware Routing & Omni Realtime Audio**

Encode-prefill-decode deployments on SGLang and vLLM can decode images once at Dynamo Frontend, now on libjpeg-turbo and FFmpeg, and hand pixels to the encode worker over a single NIXL transfer ([#11880](https://github.com/ai-dynamo/dynamo/pull/11880), [#12004](https://github.com/ai-dynamo/dynamo/pull/12004), [#11157](https://github.com/ai-dynamo/dynamo/pull/11157)). Qwen video inputs route with video-aware KV hashing, and vLLM workers accept audio and video inputs ([#14239](https://github.com/ai-dynamo/dynamo/pull/14239), [#13717](https://github.com/ai-dynamo/dynamo/pull/13717), [#12214](https://github.com/ai-dynamo/dynamo/pull/12214)). vLLM-Omni adds realtime audio streaming and dynamic LoRA for aggregated workers ([#12100](https://github.com/ai-dynamo/dynamo/pull/12100), [#11551](https://github.com/ai-dynamo/dynamo/pull/11551)).

**Kubernetes: v1beta1 Storage, Rust EPP, Standalone Snapshot & GMS V1**

`nvidia.com/v1beta1`

is the CRD storage version, the version the API server persists, and the published examples drop their v1alpha1 copies ([#11904](https://github.com/ai-dynamo/dynamo/pull/11904), [#11177](https://github.com/ai-dynamo/dynamo/pull/11177), [#12375](https://github.com/ai-dynamo/dynamo/pull/12375)). The Go Endpoint Picker is removed and the Rust EPP is the default. It ships inside the Dynamo Frontend image, with a standalone image planned ([#11355](https://github.com/ai-dynamo/dynamo/pull/11355), [#11868](https://github.com/ai-dynamo/dynamo/pull/11868), [#12720](https://github.com/ai-dynamo/dynamo/pull/12720), [#13537](https://github.com/ai-dynamo/dynamo/pull/13537)). An llm-d batch gateway example brings offline OpenAI Batch requests through the inference gateway, with dispatch gated on Dynamo readiness ([#12784](https://github.com/ai-dynamo/dynamo/pull/12784), [#13978](https://github.com/ai-dynamo/dynamo/pull/13978)).

[Dynamo Snapshot](https://github.com/ai-dynamo/snapshot) moves to a standalone operator and chart, Snapshot v0.1.0, with `PodSnapshot`

CRDs replacing the removed `DynamoCheckpoint`

CRD. Install it separately for production, or let the platform chart pull it in with `global.snapshot.install=true`

for evaluation ([#13177](https://github.com/ai-dynamo/dynamo/pull/13177), [#13452](https://github.com/ai-dynamo/dynamo/pull/13452), [#14076](https://github.com/ai-dynamo/dynamo/pull/14076)). The experimental GPU Memory Service V1 brings a checkpoint lifecycle and engine integration for SGLang and vLLM ([#13218](https://github.com/ai-dynamo/dynamo/pull/13218), [#14797](https://github.com/ai-dynamo/dynamo/pull/14797), [#14360](https://github.com/ai-dynamo/dynamo/pull/14360), [#12685](https://github.com/ai-dynamo/dynamo/pull/12685)). Dynamo Operator adds `runtimeVersionOverride`

, runtime feature gates, explicit multinode component roles, and default worker canary health checks ([#10494](https://github.com/ai-dynamo/dynamo/pull/10494), [#12421](https://github.com/ai-dynamo/dynamo/pull/12421), [#14419](https://github.com/ai-dynamo/dynamo/pull/14419), [#11083](https://github.com/ai-dynamo/dynamo/pull/11083)).

**Observability & Reliability: Request Migration, Readiness & Tracing**

Request migration attempts and cancellations are traced end to end ([#11133](https://github.com/ai-dynamo/dynamo/pull/11133)), and request-trace records write to a native S3 sink ([#11806](https://github.com/ai-dynamo/dynamo/pull/11806)). A model readiness metric gates batch dispatch ([#13976](https://github.com/ai-dynamo/dynamo/pull/13976), [#13978](https://github.com/ai-dynamo/dynamo/pull/13978)), and worker liveness probes tolerate three failures instead of one ([#13512](https://github.com/ai-dynamo/dynamo/pull/13512)).

**Performance Modeling: AISimulate, Formerly AIConfigurator**

AIConfigurator is now ** AISimulate**. It ships as its own package at v0.12.0 with one CLI, replacing the aiconfigurator wheels and the

`dynamo.replay`

entrypoint ([#13665](https://github.com/ai-dynamo/dynamo/pull/13665),

[#13478](https://github.com/ai-dynamo/dynamo/pull/13478),

[#14867](https://github.com/ai-dynamo/dynamo/pull/14867)). Offline replay returns a single

`ReplayReport`

, with per-request capture opt-in ([#12363](https://github.com/ai-dynamo/dynamo/pull/12363)).

**Recipes**

New recipes cover Qwen3.8-2.4T-A95B FP8 ([#13105](https://github.com/ai-dynamo/dynamo/pull/13105), [#13265](https://github.com/ai-dynamo/dynamo/pull/13265)), Qwen3.5-122B FP8 on H200 ([#12088](https://github.com/ai-dynamo/dynamo/pull/12088)), Nemotron-3.5-Lightning ([#13021](https://github.com/ai-dynamo/dynamo/pull/13021)), a Nemotron-3-Ultra refresh ([#13226](https://github.com/ai-dynamo/dynamo/pull/13226)), and GLM-5.3-Flash on vLLM ([#13899](https://github.com/ai-dynamo/dynamo/pull/13899)). DeepSeek-V4 downloads are parameterized by checkpoint ([#13034](https://github.com/ai-dynamo/dynamo/pull/13034)). The DeepSeek-V3.2 FP4 and Llama-3-70B recipes are removed ([#13663](https://github.com/ai-dynamo/dynamo/pull/13663)).

**Security: Transport Encryption, Certificate Injection & Fail-Closed Paths**

TLS now covers the TCP request and response planes and the NATS transport, with mutual TLS available on both, all opt-in ([#10921](https://github.com/ai-dynamo/dynamo/pull/10921), [#12533](https://github.com/ai-dynamo/dynamo/pull/12533), [#13096](https://github.com/ai-dynamo/dynamo/pull/13096), [#13528](https://github.com/ai-dynamo/dynamo/pull/13528)). Dynamo Operator injects the certificate paths once through `InfrastructureConfiguration`

([#13689](https://github.com/ai-dynamo/dynamo/pull/13689)), and administrative routes on the Backend SDK are gated on the worker lifecycle ([#13259](https://github.com/ai-dynamo/dynamo/pull/13259)). Request handling fails closed: unservable requests get a typed 4xx before the stream opens ([#12092](https://github.com/ai-dynamo/dynamo/pull/12092), [#14467](https://github.com/ai-dynamo/dynamo/pull/14467), [#12966](https://github.com/ai-dynamo/dynamo/pull/12966)), and unknown `tool_call_parser`

names are refused at registration ([#13828](https://github.com/ai-dynamo/dynamo/pull/13828)).

**Experimental: Dynamo Sidecar, Triton Backend & SGLang RL Rollout**

Dynamo Sidecar, the Triton backend, and the SGLang RL rollout contract are experimental in v1.5.0. Interfaces, defaults, and image layout may change without a deprecation cycle.

Dynamo Sidecar runs beside a stock inference engine and integrates over the engine's native gRPC API, so the engine keeps its own serve command and Dynamo stays in a separate process. SGLang, TensorRT-LLM, and vLLM each get a wheel-installed launcher, and all three sidecars ship in one CPU-only multi-arch image ([#13923](https://github.com/ai-dynamo/dynamo/pull/13923), [#13735](https://github.com/ai-dynamo/dynamo/pull/13735), [#13929](https://github.com/ai-dynamo/dynamo/pull/13929), [#13924](https://github.com/ai-dynamo/dynamo/pull/13924), [#13781](https://github.com/ai-dynamo/dynamo/pull/13781), [#13917](https://github.com/ai-dynamo/dynamo/pull/13917)).

The `dynamo.triton`

backend brings non-LLM model serving into a Dynamo pipeline. Vision, embedding, and other tensor-in, tensor-out models that already run on NVIDIA Triton can sit behind Dynamo Frontend and its routing alongside the LLM workers, launched the same way as every other runtime with `python -m dynamo.triton`

([#13774](https://github.com/ai-dynamo/dynamo/pull/13774)). No prebuilt image ships for it, so build it from the [Triton runtime Dockerfile](https://github.com/ai-dynamo/dynamo/blob/release/1.5.0/container/templates/triton_runtime.Dockerfile).

An experimental SGLang reinforcement learning rollout contract rounds out the section: detailed finish reasons, prompt token ids and logprobs in `nvext`

, native pause controls, and exact stop-token output, exercised by a Slime example ([#13640](https://github.com/ai-dynamo/dynamo/pull/13640), [#14525](https://github.com/ai-dynamo/dynamo/pull/14525), [#13951](https://github.com/ai-dynamo/dynamo/pull/13951), [#14317](https://github.com/ai-dynamo/dynamo/pull/14317), [#12856](https://github.com/ai-dynamo/dynamo/pull/12856)).

**Open-Source Contributions**

Between v1.4.2 and v1.5.0 the project merged 658 PRs from 123 contributors, 40 of them from outside NVIDIA. Thank you to the external community contributors in this release (organization identified through the commit-author email domain or the public GitHub profile):

**DaoCloud:**[@bzsuni](https://github.com/bzsuni),[@carlory](https://github.com/carlory),[@flpanbin](https://github.com/flpanbin),[@muma378](https://github.com/muma378),[@panpan0000](https://github.com/panpan0000),[@weizhoublue](https://github.com/weizhoublue),[@windsonsea](https://github.com/windsonsea),[@yankay](https://github.com/yankay).**CoreWeave:**[@alexeldeib](https://github.com/alexeldeib),[@houshengbo](https://github.com/houshengbo),[@Rexwang8](https://github.com/Rexwang8),[@ritazh](https://github.com/ritazh).**Intel:**[@Spycsh](https://github.com/Spycsh),[@tthakkal](https://github.com/tthakkal),[@VincyZhang](https://github.com/VincyZhang).**Aliyun:**[@xianlubird](https://github.com/xianlubird).**Amazon:**[@AineshSootha](https://github.com/AineshSootha),[@jlonge4](https://github.com/jlonge4),[@YiqiuLiu](https://github.com/YiqiuLiu).**Arizona State University:**[@Change72](https://github.com/Change72).**Baseten:**[@michaelfeil](https://github.com/michaelfeil),[@shalinkpatel](https://github.com/shalinkpatel).**Datadog:**[@walkoss](https://github.com/walkoss).**Gcore:**[@Kaonael](https://github.com/Kaonael).**Georgia Tech:**[@Skenix64](https://github.com/Skenix64).**H Company:**[@h-avsha](https://github.com/h-avsha).**Microsoft:**[@Jont828](https://github.com/Jont828).**Reflection AI:**[@joeltg](https://github.com/joeltg).**SK Telecom:**[@changhyeonnam](https://github.com/changhyeonnam).**San Jose State University:**[@ayaangazali](https://github.com/ayaangazali).**Stanford University:**[@merceod](https://github.com/merceod).**UC San Diego Hao AI Lab:**[@vishruthb](https://github.com/vishruthb).**University of Guelph:**[@mgsalem](https://github.com/mgsalem).**University of Washington:**[@Shaoting-Feng](https://github.com/Shaoting-Feng).**Yandex Cloud:**[@jellysnack](https://github.com/jellysnack).**Independent:**[@avinash-rafay](https://github.com/avinash-rafay),[@cmdy](https://github.com/cmdy),[@elizabetht](https://github.com/elizabetht),[@hnt2601](https://github.com/hnt2601), [@Jonny-Skel...

[Read more](https://github.com/ai-dynamo/dynamo/releases/tag/v1.5.0)

## Dynamo v1.4.1-k-exaone-2.0-750b-post.1

**Release Notes**


Dynamo v1.4.1-k-exaone-2.0-750b-post.1is an experimental snapshot build with earlyLG AI Research K-EXAONE 2.0support on the DynamovLLMbackend. It isnot recommended for productionand is not a QA-gated release. APIs, behavior, and defaults may change before stable support. Use it for evaluation, testing, and early feedback only.

**Summary**

Dynamo v1.4.1-k-exaone-2.0-750b-post.1 adds serving for ** LGAI-EXAONE/K-EXAONE-2.0-750B-A37B-NVFP4** on B200 GPUs through Dynamo vLLM 0.28.0. The runtime registers the checkpoint’s

`ExaoneMoeForCausalLM`

architecture and patches `exaone_moe`

so `lm_head`

keeps a real module prefix — without that, NVFP4 exclusion rules miss the head and load fails. The Dynamo frontend uses the `qwen3`

reasoning parser and `qwen3_coder`

tool-call parser ([#14599](https://github.com/ai-dynamo/dynamo/pull/14599)).

Kubernetes recipes cover a 4-GPU aggregated chat profile (TP4) and an 8-GPU disaggregated 1P1D chat profile (TP4 prefill + TP4 decode, NIXL/UCX KV transfer over InfiniBand RDMA). Both pin **FLASHINFER_CUTLASS** MoE, MTP (`exaone_moe_mtp`

, draft length 2), native 262,144 context, KV-aware routing, a shared model-cache PVC/download job, and an AIPerf chat-trace job under `recipes/k-exaone-2.0`

([#14822](https://github.com/ai-dynamo/dynamo/pull/14822), [#15016](https://github.com/ai-dynamo/dynamo/pull/15016)).

**Base Branch**: `release/1.4.1`


**Base Commit**: `2112d6ba74da72e2715ae69f4b76458b7691380d`

(2026-08-22)

**Preview Branch**: `release/1.4.1-k-exaone-2.0-750b-post.1`


**Preview Tip**: `effab39d4ede05e852d1a4250f711e98fe9e3635`

(2026-09-17)

**vLLM**: `v0.28.0-ubuntu2404`

(`vllm/vllm-openai`

), CUDA 13.0, NIXL v1.3.2 (UCX v1.21.0)

**Container Images**

| Backend | Arch | Image |
|---|---|---|
| vLLM (CUDA 13) | multi-arch (`amd64` + `arm64` ) |
`nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.4.1-k-exaone-2.0-750b-post.1` |

Workers use that runtime. Frontends use the released `nvcr.io/nvidia/ai-dynamo/dynamo-frontend:1.4.1`

image.

**Backend Versions**

| Backend | Source | CUDA | Python | Notes |
|---|---|---|---|---|
| vLLM | Dynamo-built runtime on `vllm/vllm-openai:v0.28.0-ubuntu2404` |
13.0 | 3.12 | NIXL v1.3.2; `exaone_moe` `lm_head` prefix patch; architecture key `ExaoneMoeForCausalLM` |

**Models**

| Model | Precision | GPU | Notes |
|---|---|---|---|
`LGAI-EXAONE/K-EXAONE-2.0-750B-A37B-NVFP4` |
NVFP4 (W4A4) weights, FP8 KV cache | B200 | 764.5 B total / ~37 B active, 78 layers (20 full + 58 sliding attention), 256 experts top-8, 262,144 native context; `qwen3` / `qwen3_coder` parsers; MTP `exaone_moe_mtp` DL=2 |

**About K-EXAONE 2.0**

**K-EXAONE 2.0** is LG AI Research’s hybrid-attention MoE checkpoint published on Hugging Face as `LGAI-EXAONE/K-EXAONE-2.0-750B-A37B-NVFP4`

(~530 GB on disk). This build serves it through Dynamo’s vLLM backend on B200, with reasoning, tool calling, MTP, and aggregated or 1P1D disaggregated topologies.

**Full Changelog**

**vLLM Backend**

**K-EXAONE architecture on vLLM 0.28.0:**Bumps the vLLM runtime from 0.26.0 to`v0.28.0-ubuntu2404`

so the registry key matches the checkpoint’s`ExaoneMoeForCausalLM`

architecture ([#14599](https://github.com/ai-dynamo/dynamo/pull/14599)).**NVFP4**Patches`lm_head`

load:`exaone_moe`

to pass`prefix=maybe_prefix(prefix, "lm_head")`

on`ParallelLMHead`

. Without it, NVFP4 exclusion never matches`lm_head`

and the unquantized BF16 head fails to load ([#14599](https://github.com/ai-dynamo/dynamo/pull/14599)).

**Recipes**

**Added K-EXAONE 2.0 deployment recipes:**`recipes/k-exaone-2.0`

— shared model-cache PVC and Hugging Face download, aggregated TP4 chat on 4× B200, disaggregated 1P1D chat on 8× B200 (`NixlConnector`

KV transfer over InfiniBand RDMA), mandatory FLASHINFER_CUTLASS MoE, MTP (`exaone_moe_mtp`

,`--spec-tokens 2`

), Dynamo`--dyn-reasoning-parser qwen3`

/`--dyn-tool-call-parser qwen3_coder`

, KV-aware routing wired on frontend and workers, startup probes for the long first load, and an AIPerf job on the 8k/1k chat trace ([recipe folder](https://github.com/ai-dynamo/dynamo/tree/effab39d4ede05e852d1a4250f711e98fe9e3635/recipes/k-exaone-2.0),[README](https://github.com/ai-dynamo/dynamo/blob/effab39d4ede05e852d1a4250f711e98fe9e3635/recipes/k-exaone-2.0/README.md)) ([#14822](https://github.com/ai-dynamo/dynamo/pull/14822),[#15016](https://github.com/ai-dynamo/dynamo/pull/15016)).

**Getting Started**

Deployment is Kubernetes-based (Dynamo Platform + `DynamoGraphDeployment`

). Full steps — namespace, model-cache PVC, Hugging Face download job, DGD apply, `/v1/chat/completions`

smoke test, and AIPerf — are in the [recipe README](https://github.com/ai-dynamo/dynamo/blob/effab39d4ede05e852d1a4250f711e98fe9e3635/recipes/k-exaone-2.0/README.md). Recipes expect a Hugging Face token secret named `hf-token-secret`

. First start is 40–120 minutes (53 shards, autotune, CUDA-graph capture).

This is a reasoning model: smoke tests should use **temperature 0.6 / top_p 0.95**, a real token budget (`max_tokens`

well above 256), and read `.content // .reasoning_content`

.

**Known Issues / Limitations**

- This is a branch-specific snapshot build, not a QA-gated stable release.
- This release supports the Dynamo vLLM backend on B200 only. Stock Dynamo 1.4.1 vLLM (0.26.0) cannot load this checkpoint.
`--kernel-config '{"moe_backend":"FLASHINFER_CUTLASS"}'`

is required. vLLM`auto`

selects FLASHINFER_TRTLLM and can silently corrupt long-form output on this checkpoint.- On disaggregated serving, prefill and decode must use the same MTP settings and
`--block-size 64`

. A mismatch changes KV block geometry and produces silent garbage rather than an error. - The disaggregated recipe requests
`rdma/shared_ib`

; set that name to the RDMA resource your cluster actually exposes. Confirm UCX selected InfiniBand (`rc_mlx5`

/`rc`

) before trusting TTFT. - Do not add
`--load-format fastsafetensors`

unless GPUDirect Storage is present; without GDS the loader can stall before opening a shard. - KV-aware routing is wired, but inert at the shipped
`replicas: 1`

. Raising replicas is enough to activate it; on this workload prefix hit rate is already capacity-bound (~8.8%).

## Dynamo v1.4.1-solar-open2-250b-post.1

**Release Notes**


Dynamo v1.4.1-solar-open2-250b-post.1is an experimental snapshot build with earlySolar Open2 250Bsupport on the DynamovLLMbackend. It isnot recommended for productionand is not a QA-gated release. APIs, behavior, and defaults may change before stable support. Use it for evaluation, testing, and early feedback only.

**Summary**

Dynamo v1.4.1-solar-open2-250b-post.1 adds serving for ** nota-ai/Solar-Open2-250B-Nota-NVFP4** on B200 GPUs through Dynamo vLLM 0.26.0. The runtime registers the

`SolarOpen2ForCausalLM`

architecture and config, the KDA linear-attention custom op, Solar Open2 reasoning and tool-call parsers, and a chat-template logits processor. The Dynamo frontend keeps special tokens in the stream when a reasoning parser is configured and honors the model's start-of-tool marker ([#14556](https://github.com/ai-dynamo/dynamo/pull/14556)).

Kubernetes recipes cover a 4-GPU aggregated chat profile (two TP2 replicas, KV-aware routing) and an 8-GPU disaggregated 1P:2D chat profile (one TP4+EP prefill worker and two TP2 decode workers, NIXL/RDMA KV transfer). Both share a revision-pinned model-cache PVC/download job and AIPerf chat-trace jobs under `recipes/solar-open2-250b`

([#14912](https://github.com/ai-dynamo/dynamo/pull/14912), [#14376](https://github.com/ai-dynamo/dynamo/pull/14376)).

**Base Branch**: `release/1.4.1`


**Base Commit**: `2112d6ba74da72e2715ae69f4b76458b7691380d`

(2026-08-22)

**Preview Branch**: `release/1.4.1-solar-open2-250b-post.1`


**Preview Tip**: `08d7f10f8b6622427d9f0ba900ff3f5e0f904bd2`

(2026-09-16)

**vLLM**: `v0.26.0-ubuntu2404`

(`vllm/vllm-openai`

), CUDA 13.0, NIXL v1.3.2 (UCX v1.21.0)

**Container Images**

| Backend | Arch | Image |
|---|---|---|
| vLLM (CUDA 13) | multi-arch (`amd64` + `arm64` ) |
`nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.4.1-solar-open2-250b-post.1` |

Recipes pin that image by digest `sha256:42fd3ed0607aa19b7d4c1b0a8f8aaaefefc8ec6292294ea2b5e6757353891f49`

.

**Backend Versions**

| Backend | Source | CUDA | Python | Notes |
|---|---|---|---|---|
| vLLM | Dynamo-built runtime on `vllm/vllm-openai:v0.26.0-ubuntu2404` |
13.0 | 3.12 | NIXL v1.3.2; Python-only Solar Open2 architecture and parser patches; no custom vLLM kernel build |

**Models**

| Model | Precision | GPU | Notes |
|---|---|---|---|
`nota-ai/Solar-Open2-250B-Nota-NVFP4` |
NVFP4 weights, FP8 KV cache | B200 | Hybrid GQA + KDA linear attention; 1M context; revision pinned to `3cc673335f4c2f41181e05a98fc2b8324d586a64` ; `solar_open2` reasoning and tool-call parsers |

**About Solar Open2 250B**

**Solar Open2 250B** is served from the Nota NVFP4 checkpoint on Hugging Face as `nota-ai/Solar-Open2-250B-Nota-NVFP4`

. This build serves it through Dynamo's vLLM backend with reasoning and tool calling on B200, in aggregated KV-aware and disaggregated NIXL/RDMA topologies.

**Full Changelog**

**vLLM Backend**

**Solar Open2 architecture:**Registers`SolarOpen2ForCausalLM`

/`SolarOpen2Config`

and the KDA linear-attention custom op so the hybrid attention graph compiles on vLLM 0.26.0 ([#14556](https://github.com/ai-dynamo/dynamo/pull/14556)).**Reasoning and tool calling:**Adds the Solar Open2 reasoning parser, tool-call parser, and chat-template logits processor, and hardens shared tool-parser handling when a tool schema`properties`

field is not a dictionary ([#14556](https://github.com/ai-dynamo/dynamo/pull/14556)).**Frontend compatibility:**Leaves special tokens in the stream when a reasoning parser is configured, and considers the model's start-of-tool marker during tool-call lookup ([#14556](https://github.com/ai-dynamo/dynamo/pull/14556)).**Build-time validation:**`validate_solar_open2_port.py`

fails the image build unless the architecture, parsers, and attention op register ([#14556](https://github.com/ai-dynamo/dynamo/pull/14556)).

**Recipes**

**Added Solar Open2 250B deployment recipes:**`recipes/solar-open2-250b`

— shared 1200Gi model-cache PVC and revision-pinned Hugging Face download, aggregated 2×TP2 chat on 4× B200 with KV-aware routing, disaggregated 1P:2D chat on 8× B200 (`NixlConnector`

KV transfer over RDMA/InfiniBand), and AIPerf jobs for the chat trace ([recipe folder](https://github.com/ai-dynamo/dynamo/tree/08d7f10f8b6622427d9f0ba900ff3f5e0f904bd2/recipes/solar-open2-250b),[docs](https://github.com/ai-dynamo/dynamo/blob/08d7f10f8b6622427d9f0ba900ff3f5e0f904bd2/docs/fern/pages/recipes/model-recipes/solar-open2-250b.mdx)) ([#14912](https://github.com/ai-dynamo/dynamo/pull/14912),[#14376](https://github.com/ai-dynamo/dynamo/pull/14376)).

**Getting Started**

Deployment is Kubernetes-based (Dynamo Platform + `DynamoGraphDeployment`

). Full steps — namespace, model-cache PVC, Hugging Face download job, DGD apply, `/v1/chat/completions`

smoke test, and AIPerf — are in the [recipe docs](https://github.com/ai-dynamo/dynamo/blob/08d7f10f8b6622427d9f0ba900ff3f5e0f904bd2/docs/fern/pages/recipes/model-recipes/solar-open2-250b.mdx). Recipes expect an `nvcr.io`

image-pull secret and a Hugging Face token secret named `hf-token-secret`

.

**Known Issues / Limitations**

- This is a branch-specific snapshot build, not a QA-gated stable release.
- This release supports the Dynamo vLLM backend on B200 only. The stock Dynamo 1.4.1 vLLM runtime cannot load this checkpoint.
- Speculative decoding is not supported on this checkpoint and is not enabled.
- The disaggregated profile requires
`VLLM_SSM_CONV_STATE_LAYOUT=DS`

and an`rdma/ib`

(or equivalent) device plugin; without the IB device, KV transfer silently falls back to TCP. - Solar Open2 is a reasoning model. Short
`max_tokens`

often truncates mid-reasoning (`finish_reason=length`

) with an empty`content`

field; omit`max_tokens`

or set it well above the reasoning length the workload needs.

## Dynamo v1.4.1-a.x-k2-post.1

**Release Notes**


Dynamo v1.4.1-a.x-k2-post.1is an experimental snapshot build with earlyA.X-K2support on the DynamovLLMbackend. It isnot recommended for productionand is not a QA-gated release. APIs, behavior, and defaults may change before stable support. Use it for evaluation, testing, and early feedback only.

**Summary**

Dynamo v1.4.1-a.x-k2-post.1 adds serving for ** skt/A.X-K2-NVFP4** on B200 GPUs through Dynamo vLLM 0.26.0. The runtime includes A.X-K2 model and configuration registration, DSpark-compatible speculative-decoding behavior, and KV-cache support for sparse MLA targets with sliding-window draft models.

Kubernetes recipes provide an 8-GPU aggregated deployment and a 12-GPU 2-prefill/1-decode disaggregated deployment. Both use TP4 workers, NVFP4 model weights, FP8 KV cache, KV-aware routing, and revision-pinned EAGLE3 speculative decoding with three speculative tokens. The disaggregated profile transfers KV state through NIXL over UCX.

**Release Branch**: `release/1.4.1-a.x-k2-post.1`

, tip `020c9905910df391f3eb206d06b727937aa17a92`

(2026-09-15)

**vLLM**: `0.26.0`

with A.X-K2 patches 0001–0004

**Container Images**

| Backend | Arch | Image |
|---|---|---|
| vLLM | multi-arch (`amd64` + `arm64` ) |
`nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.4.1-a.x-k2-post.1` |

**Backend Versions**

| Backend | Source | Notes |
|---|---|---|
| vLLM | Dynamo v1.4.1 runtime with vLLM 0.26.0 | A.X-K2 model/config support, DSpark anchor-sampling layout, and sparse-MLA KV-cache compatibility |

**Models**

| Model | Precision | GPU | Notes |
|---|---|---|---|
`skt/A.X-K2-NVFP4` |
NVFP4 weights, FP8 KV cache | B200 | Target model; revision pinned to `9e2e804e80f8d1b3afba5d7938173cec1ed46b49` |
`skt/A.X-K2-EAGLE3` |
EAGLE3 draft model | B200 | Three speculative tokens; revision pinned to `24958e91737d760908f73a8af4b6e06080fc5c1d` |

**About A.X-K2**

**A.X-K2** is served with NVFP4 weights and FP8 KV cache on B200 GPUs. This build supports aggregated and disaggregated Dynamo deployments, KV-aware routing, and EAGLE3 speculative decoding. The disaggregated profile separates prefill and decode workers while transferring KV state over NIXL/UCX.

**Full Changelog**

**vLLM Backend**

**A.X-K2 model support:**Adds the A.X-K2 model and configuration to the Dynamo vLLM runtime and rejects unsupported checkpoints that use non-fused attention gates.**Speculative decoding:**Honors the DSpark anchor-sampling layout used by A.X-K2 speculative decoding.**KV-cache compatibility:**Supports sparse MLA target models paired with sliding-window draft models.**Build-time validation:**Validates model registration, DSpark integration, and KV-cache wiring while building the runtime.**Container change:**[PR #14554](https://github.com/ai-dynamo/dynamo/pull/14554).

**Recipes**

**Aggregated serving:**Two TP4 workers across 8 B200 GPUs with KV-aware routing, NVFP4 weights, FP8 KV cache, and EAGLE3 speculative decoding.**Disaggregated serving:**Two TP4 prefill workers and one TP4 decode worker across 12 B200 GPUs, with KV-aware routing and NIXL/UCX KV transfer.**Model caching:**Shared PVC and revision-pinned download job for the target and EAGLE3 draft models.**Benchmarking:**AIPerf 0.12.0 workflow for a Mooncake chat trace with 8K input, 1K output, 70% KV reuse, and concurrency 16. An optional synthetic EAGLE3 acceptance-length profile (`AL=2.12`

) is provided for throughput-only measurements.**Recipe change:**[PR #14635](https://github.com/ai-dynamo/dynamo/pull/14635), included on this release branch by[PR #14883](https://github.com/ai-dynamo/dynamo/pull/14883).

**Getting Started**

Deployment is Kubernetes-based using the Dynamo Platform and `DynamoGraphDeployment`

. The [A.X-K2 recipe](https://github.com/ai-dynamo/dynamo/tree/020c9905910df391f3eb206d06b727937aa17a92/recipes/ax-k2) includes model-cache setup, aggregated and disaggregated manifests, deployment instructions, smoke-test guidance, and the AIPerf benchmark workflow. Recipes expect an `nvcr.io`

image-pull secret and a Hugging Face token secret named `hf-token-secret`

.

**Known Issues / Limitations**

- Experimental snapshot build — not QA-gated and not recommended for production.
- This release supports the Dynamo vLLM backend only.
- Deployment recipes target B200 GPUs.
- The synthetic EAGLE3 acceptance profile is intended only for throughput benchmarking, not functional or quality validation.
- Published benchmark results predate the final published NVCR runtime image and should not be treated as measurements of this exact build.
- The recorded disaggregated benchmark completed 1,755 of 1,765 requests; ten requests failed.

## Dynamo v1.6.0-deepseek-v4.1-flash-dev.1

**Release Notes**


Dynamo v1.6.0-deepseek-v4.1-flash-dev.1is an experimental snapshot build with earlyDeepSeek-V4.1-Flashsupport on the DynamoSGLangbackend. It isnot recommended for productionand is not a QA-gated release. APIs, behavior, and defaults may change before stable support. Use it for evaluation, testing, and early feedback only.

**Summary**

Dynamo v1.6.0-deepseek-v4.1-flash-dev.1 adds serving for ** deepseek-ai/DeepSeek-V4.1-Flash** on Dynamo

**SGLang**. The published container is built on the CUDA 13 SGLang

`dev-dsv41`

preview base and includes native DeepSeek V4.1 frontend support: Rust prompt rendering, automatic `deepseek_v41`

reasoning and tool-call parsing, streamed DSML handling, and rejection of completed malformed tool-call arguments ([#14690](https://github.com/ai-dynamo/dynamo/pull/14690)).

Kubernetes recipes cover 8x GB200 aggregated (two TP4/EP4 workers, KV-aware routing, DSpark speculative decoding) and 1P1D disaggregated (TP4/EP4 per role, Mooncake KV transfer over TCP or GKE RDMA) profiles, plus a shared model-cache PVC and Hugging Face download job pinned to revision `dba1be0a40aa45a94ad051997016db3960a90277`

. Both targets serve up to 1,048,576 tokens of context. Neither target is benchmarked ([#14682](https://github.com/ai-dynamo/dynamo/pull/14682), [#14763](https://github.com/ai-dynamo/dynamo/pull/14763)).

**Release Branch**: `release/1.6.0-deepseek-v4.1-flash-dev.1`

, tip `7931147d403c554575438c2451da4248e53e10b8`

(2026-09-12)

**SGLang**: `lmsysorg/sglang:dev-dsv41@sha256:e56358a68b06427362283c8c8a9d7d706448082ae53098ea1131b5d51aa1fd62`

(CUDA 13), NIXL v1.4.0

**Container Images**

| Backend | Arch | Image |
|---|---|---|
| SGLang (CUDA 13) | multi-arch (`amd64` + `arm64` ) |
`nvcr.io/nvidia/ai-dynamo/sglang-runtime:1.6.0-deepseek-v4.1-flash-dev.1` |

**Backend Versions**

| Backend | Source | CUDA | Python | Notes |
|---|---|---|---|---|
| SGLang | Dynamo-built runtime on `lmsysorg/sglang:dev-dsv41` (digest-pinned), with non-runtime packages pruned from the upstream development image |
13.0 | 3.12 | NIXL v1.4.0; DeepSeek V4.1 has not shipped in a numbered SGLang release yet |

**Models**

| Model | Precision | GPU | Notes |
|---|---|---|---|
`deepseek-ai/DeepSeek-V4.1-Flash` |
FP8 dense, FP4 MoE experts, FP8 KV (`fp8_e4m3` ) |
8x GB200 | SGLang `dev-dsv41` ; aggregated TP4/EP4 (DSpark k=5, KV-aware routing) or 1P1D disagg TP4/EP4 per role (no speculation); 1M context; `deepseek_v41` reasoning and tool-call parsers |

**About DeepSeek-V4.1-Flash**

DeepSeek-V4.1-Flash is a Mixture-of-Experts checkpoint from DeepSeek (`deepseek-ai/DeepSeek-V4.1-Flash`

; about 510 GB). Routed experts ship FP4, dense weights are FP8, and the engine uses an FP8 KV cache. This preview serves the full 1,048,576-token window on GB200 through Dynamo's SGLang backend, with reasoning, tool calling, streaming chat, and schema-constrained output. The checkpoint also accepts images; the recipes in this build serve text only.

**Full Changelog**

**SGLang Backend**

**DeepSeek V4.1 frontend:**Native Rust prompt rendering and unified reasoning/tool-call parsing for DeepSeek V4.1, including automatic parser selection from model metadata, preserved partial DSML markers across streamed chunks, normalized reasoning-effort values, and rejection of completed malformed DSML arguments during batch aggregation ([#14690](https://github.com/ai-dynamo/dynamo/pull/14690)).**SGLang**Pins the CUDA 13 SGLang runtime to the digest-pinned`dev-dsv41`

runtime:`lmsysorg/sglang:dev-dsv41`

preview base required to serve this model, and trims non-runtime packages from that development image ([#14690](https://github.com/ai-dynamo/dynamo/pull/14690)).

**Recipes**

**DeepSeek-V4.1-Flash SGLang GB200 recipes:**Added`recipes/deepseek-v4.1-flash`

— shared model-cache PVC/download job (pinned HF revision), aggregated GB200 (`sglang/agg-gb200`

: two TP4 workers, KV-aware routing, DSpark block size 5, decode CUDA-graph batch capped at 64), and disaggregated GB200 1P1D (`sglang/disagg-gb200`

: generic Mooncake TCP target plus GKE RDMA variant). Both profiles use`sglang-runtime:1.6.0-deepseek-v4.1-flash-dev.1`

,`deepseek_v41`

parsers, and 1M context. Day-0 functional scope only; no published performance claim ([recipe folder](https://github.com/ai-dynamo/dynamo/tree/7931147d403c554575438c2451da4248e53e10b8/recipes/deepseek-v4.1-flash),[README](https://github.com/ai-dynamo/dynamo/blob/7931147d403c554575438c2451da4248e53e10b8/recipes/deepseek-v4.1-flash/README.md),[docs](https://docs.nvidia.com/dynamo/dev/recipes/deepseek-v4-1-flash)) ([#14682](https://github.com/ai-dynamo/dynamo/pull/14682),[#14763](https://github.com/ai-dynamo/dynamo/pull/14763)).

**Getting Started**

Deployment is Kubernetes-based (Dynamo Platform + `DynamoGraphDeployment`

). Full steps — namespace, Hugging Face token, model-cache PVC, download job, DGD apply, and a `/v1/chat/completions`

smoke test — are in the [recipe docs](https://docs.nvidia.com/dynamo/dev/recipes/deepseek-v4-1-flash) and the [recipe README](https://github.com/ai-dynamo/dynamo/blob/7931147d403c554575438c2451da4248e53e10b8/recipes/deepseek-v4.1-flash/README.md). Recipes expect an `nvcr.io`

image-pull secret and a Hugging Face token secret named `hf-token-secret`

with access to `deepseek-ai/DeepSeek-V4.1-Flash`

. GB200 recipes require ARM-node scheduling (two nodes, 4 GPUs each).

Read the smoke-test response body, not only the HTTP status. On the disaggregated target a KV transfer failure can still return HTTP 200 with `content: null`

and zero completion tokens.

**Known Issues / Limitations**

- This is a branch-specific snapshot build, not a QA-gated stable release.
- Day-0 recipes only: both targets passed a functional probe; neither is benchmarked.
- Disaggregated SGLang does not support DSpark for this model. Use the aggregated target for speculative decoding.
- Generic disaggregated KV is pinned to Mooncake TCP (
`MC_FORCE_TCP=1`

). The GKE variant uses RDMA and DMA-BUF (`WITH_NVIDIA_PEERMEM=0`

). The NVLink fabric is faster but needs both workers in one NVLink clique; a split placement reports Ready and returns empty completions. - KV-aware routing is a no-op on the disaggregated target with a single decode worker.
- Recipes serve text only, even though the checkpoint accepts images.
- Both targets set
`SGLANG_DEFAULT_THINKING=true`

. Thinking is off by default for this model, and then`reasoning_content`

is empty. - GB200 recipes require ARM-node scheduling.

## Dynamo v1.5.0-kimi-k3-dev.1

**Release Notes**


Dynamo v1.5.0-kimi-k3-dev.1is an experimental snapshot build with earlyKimi-K3support on the DynamovLLMandSGLangbackends. It isnot recommended for productionand is not a QA-gated release. APIs, behavior, and defaults may change before stable support. Use it for evaluation, testing, and early feedback only.

**Summary**

Dynamo v1.5.0-kimi-k3-dev.1 adds serving for ** moonshotai/Kimi-K3** on Dynamo

**vLLM**and

**SGLang**. The published containers are built on the refreshed Day-0 stack — vLLM

`v0.28.0`

and SGLang `v0.5.17`

bases carrying the Kimi-K3 patch set (MoonViT cuDNN crash fix on SM100, DCP/DSpark speculative-decoding support, Mamba/EAGLE and radix-cache fixes) — plus SGLang frontend multimodal pre/post-processing for text + image workloads ([#14299](https://github.com/ai-dynamo/dynamo/pull/14299)).

Kubernetes recipes cover vLLM aggregated profiles on H200, GB200, and GB300 and a 1P1D disaggregated GB300 profile, plus SGLang aggregated and disaggregated profiles on GB200 and GB300 — with DSPARK speculative decoding, KV-aware (vLLM) or load-aware (SGLang) routing, shared model-cache manifests, and an AIPerf trace-replay benchmark under `recipes/kimi-k3`

([#12944](https://github.com/ai-dynamo/dynamo/pull/12944), cherry-picked in [#14552](https://github.com/ai-dynamo/dynamo/pull/14552)).

**Release Branch**: `release/1.5.0-kimi-k3-dev.1`

, tip `d889e0e4501bbe3f8134077788dbc2ce3d8b9842`

(2026-09-09)

**vLLM**: `vllm/vllm-openai:v0.28.0-ubuntu2404`

base (CUDA 13), NIXL v1.3.1

**SGLang**: `lmsysorg/sglang:v0.5.17-cu130-runtime`

base (CUDA 13), NIXL v1.3.0

**Container Images**

| Backend | Arch | Image |
|---|---|---|
| vLLM (CUDA 13) | multi-arch (`amd64` + `arm64` ) |
`nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.5.0-kimi-k3-dev.1` |
| SGLang (CUDA 13) | multi-arch (`amd64` + `arm64` ) |
`nvcr.io/nvidia/ai-dynamo/sglang-runtime:1.5.0-kimi-k3-dev.1` |

**Backend Versions**

| Backend | Source | CUDA | Python | Notes |
|---|---|---|---|---|
| vLLM | Dynamo-built runtime on `vllm/vllm-openai:v0.28.0-ubuntu2404` with the Kimi-K3 patch set |
13.0 | 3.12 | NIXL v1.3.1; vllm-omni `v0.27.0rc1` |
| SGLang | Dynamo-built runtime on `lmsysorg/sglang:v0.5.17-cu130-runtime` with the Kimi-K3 patch set |
13.0 | 3.12 | NIXL v1.3.0 |

**Models**

| Model | Precision | GPU | Notes |
|---|---|---|---|
`moonshotai/Kimi-K3` |
MXFP4 experts, FP8 or BF16 KV cache | H200, GB200, GB300 | multimodal (text + image) MoE, up to 1M-token context |

**About Kimi-K3**

[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) is Moonshot AI's hybrid-attention mixture-of-experts model with multimodal (text + image) support and up to 1M-token context. This preview serves it through Dynamo's vLLM and SGLang backends with aggregated and disaggregated agentic recipes on H200, GB200, and GB300.

**Full Changelog**

**vLLM Backend**

**Kimi-K3 runtime stack:**Rebased the vLLM runtime on`vllm/vllm-openai:v0.28.0-ubuntu2404`

and carried the Kimi-K3 patch set — MoonViT cuDNN crash fix on SM100, draft KV-pool sizing, TGV 2-CTA exit barrier, and DCP PD / DSpark speculative-decoding support ([#14299](https://github.com/ai-dynamo/dynamo/pull/14299)).

**SGLang Backend**

**Kimi-K3 runtime stack:**Rebased the SGLang runtime on`lmsysorg/sglang:v0.5.17-cu130-runtime`

and carried the Kimi-K3 patch set — MoonViT cuDNN fix, Mamba/EAGLE cache-state handling under DCP, partial prefix-cache hits, and radix-cache allocation fixes ([#14299](https://github.com/ai-dynamo/dynamo/pull/14299)).**Multimodal frontend:**Added SGLang frontend pre/post-processing for Kimi-K3 multimodal (text + image) requests ([#14299](https://github.com/ai-dynamo/dynamo/pull/14299)).

**Recipes**

**Refreshed Kimi-K3 deployment recipes:**vLLM aggregated H200 (32x, TP8+PP4), GB200 (16x, TP16), and GB300 (16x, DCP16/TEP16, DSPARK) profiles and a 1P1D disaggregated GB300 profile; SGLang aggregated GB200 (32x) and GB300 (24x) profiles and disaggregated GB200 (2P1D) and GB300 (1P1D) profiles with DSPARK; shared model-cache PVC/download manifests; and an AIPerf Mooncake trace-replay benchmark (64K ISL / 400 OSL / 90% KV-reuse agentic trace) ([recipe folder](https://github.com/ai-dynamo/dynamo/tree/d889e0e4501bbe3f8134077788dbc2ce3d8b9842/recipes/kimi-k3),[docs](https://docs.nvidia.com/dynamo/dev/recipes/kimi-k3)) ([#12944](https://github.com/ai-dynamo/dynamo/pull/12944), cherry-picked in[#14552](https://github.com/ai-dynamo/dynamo/pull/14552)).

**Getting Started**

Deployment is Kubernetes-based (Dynamo Platform + `DynamoGraphDeployment`

). Full steps — framework/GPU/topology target picker, namespace, model-cache PVC, Hugging Face download job, DGD apply, and a `/v1/chat/completions`

smoke test — are in the [Kimi-K3 recipe docs](https://docs.nvidia.com/dynamo/dev/recipes/kimi-k3) and the [recipe README](https://github.com/ai-dynamo/dynamo/blob/d889e0e4501bbe3f8134077788dbc2ce3d8b9842/recipes/kimi-k3/README.md). Recipes expect an `nvcr.io`

image-pull secret and a Hugging Face token secret named `hf-token-secret`

.

**Known Issues / Limitations**

- This is a branch-specific snapshot build, not a QA-gated stable release.
- Recipe coverage: vLLM disaggregated profiles are GB300-only; SGLang profiles cover GB200/GB300 only (no H200); no vLLM GB200 disaggregated profile in this build.
- Requests containing
`logprobs`

or`stop_token_ids`

are not supported and may cause disaggregated recipes to crash or enter a bad state. - With JSON structured decoding, output for non-object top-level items can appear in
`reasoning_content`

instead of`content`

. - GB200/GB300 recipes require ARM-node scheduling.

## Dynamo v1.5.0-deepseek-v4-pro-0813-dev.1

**Release Notes**


Dynamo v1.5.0-deepseek-v4-pro-0813-dev.1is an experimental snapshot build with earlyDeepSeek-V4-Pro-0813support on the Dynamo vLLM backend. It isnot recommended for productionand is not a QA-gated release. APIs, behavior, and defaults may change before stable support. Use it for evaluation, testing, and early feedback only.

**Summary**

Dynamo v1.5.0-deepseek-v4-pro-0813-dev.1 publishes a **vLLM** runtime on **v0.28.0** (CUDA 13.0) for **DeepSeek-V4-Pro-0813**. The CUDA image was already on that vLLM pin at branch cut; this snapshot also aligns the XPU vLLM pin to 0.28.0 ([#14269](https://github.com/ai-dynamo/dynamo/pull/14269)).

On top of that runtime, the release ships **aggregated and disaggregated** vLLM recipes for the public `deepseek-ai/DeepSeek-V4-Pro-0813`

checkpoint (MXFP4 experts + FP8 KV, 1M context, no CPU KV offload): 8x GB200 and 8x H200 aggregated, plus 1P1D 16-GPU disaggregated profiles on both SKUs, with KV-aware routing, shared model-cache/download jobs, and an AIPerf Mooncake trace-replay benchmark ([#14307](https://github.com/ai-dynamo/dynamo/pull/14307)). This is a **different checkpoint** from `deepseek-ai/DeepSeek-V4-Pro`

and must not share a model cache with those recipes.

**Release Branch**: `release/1.5.0-deepseek-v4-pro-0813-dev.1`

, cut from `main`

commit `dc08c938c5`

(2026-08-31)

**Release Tip**: `28f9c307dcff4130412ac04e4ea07c96b0cde6f5`


**vLLM**: v0.28.0 (`vllm/vllm-openai:v0.28.0-ubuntu2404`

base), NIXL v1.3.2 (UCX v1.21.0)

**Container Images**

| Backend | Arch | Image |
|---|---|---|
| vLLM (CUDA 13) | multi-arch (`amd64` + `arm64` ) |
`nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.5.0-deepseek-v4-pro-0813-dev.1` |

**Backend Versions**

| Backend | Source | CUDA | Python | Notes |
|---|---|---|---|---|
| vLLM | Dynamo-built runtime on `vllm/vllm-openai:v0.28.0-ubuntu2404` |
13.0 | 3.12 | NIXL v1.3.2; vLLM-Omni `v0.28.0rc1` |

**Models**

| Model | Precision | GPU | Notes |
|---|---|---|---|
`deepseek-ai/DeepSeek-V4-Pro-0813` |
MXFP4 experts + FP8 KV | 8x GB200 | vLLM 0.28.0; aggregated TP8/EP8 (2 nodes, MNNVL) or disagg 1P1D (16 GPU); DSpark k=5; KV-aware routing; 1M context |
`deepseek-ai/DeepSeek-V4-Pro-0813` |
MXFP4 experts + FP8 KV | 8x H200 | vLLM 0.26.0 via `vllm-runtime:1.4.0` ; aggregated TP8/EP8 or disagg 1P1D (16 GPU); no speculative decoding; KV-aware routing; 1M context |

**About DeepSeek-V4-Pro-0813**

DeepSeek-V4-Pro-0813 is a 1.6T-parameter text MoE from DeepSeek (`deepseek-ai/DeepSeek-V4-Pro-0813`

; ~832 GiB). Routed experts ship MXFP4 and the engine requires FP8 KV. This preview serves the full 1,048,576-token window on GB200 and H200, aggregated or disaggregated, with reasoning and tool calling. It is not a revision of DeepSeek-V4-Pro.

**Full Changelog**

**vLLM Backend**

**XPU vLLM 0.28.0 pin:**Aligned the XPU vLLM base/runtime and matching SBOM stem to`v0.28.0`

on this branch. The CUDA 13.0 runtime was already on`v0.28.0-ubuntu2404`

at cut; these commits do not change the CUDA image contents ([#14269](https://github.com/ai-dynamo/dynamo/pull/14269)).

**Recipes**

**DeepSeek-V4-Pro-0813 vLLM recipes:**Added`recipes/deepseek-v4/deepseek-v4-pro-0813`

—`agg-gb200-agentic`

,`disagg-gb200-agentic`

,`agg-h200-agentic`

,`disagg-h200-agentic`

, model-cache PVC and download job, AIPerf Mooncake trace-replay under`perf/`

, and Fern catalog/docs. GB200 workers use`vllm-runtime:1.5.0-deepseek-v4-pro-0813-dev.1`

; H200 workers stay on digest-pinned`vllm-runtime:1.4.0`

([recipe folder](https://github.com/ai-dynamo/dynamo/tree/28f9c307dcff4130412ac04e4ea07c96b0cde6f5/recipes/deepseek-v4/deepseek-v4-pro-0813),[README](https://github.com/ai-dynamo/dynamo/blob/28f9c307dcff4130412ac04e4ea07c96b0cde6f5/recipes/deepseek-v4/deepseek-v4-pro-0813/README.md)) ([#14307](https://github.com/ai-dynamo/dynamo/pull/14307)).

**Getting Started**

Deployment is Kubernetes-based (Dynamo Platform + DynamoGraphDeployment). Full steps — namespace, Hugging Face token, model-cache PVC, download job, DGD apply, smoke test, and the AIPerf workflow — are in the [recipe README](https://github.com/ai-dynamo/dynamo/blob/28f9c307dcff4130412ac04e4ea07c96b0cde6f5/recipes/deepseek-v4/deepseek-v4-pro-0813/README.md). The recipes expect an `nvcr.io`

image-pull secret and a Hugging Face token with access to `deepseek-ai/DeepSeek-V4-Pro-0813`

.

**Known Issues / Limitations**

- This is a branch-specific snapshot build, not a QA-gated stable release.
**GB200 disaggregated RDMA is provider-specific.**`vllm/disagg-gb200-agentic/deploy.yaml`

ships GKE`networking.gke.io`

annotations and`rdma-0`

–`rdma-3`

resource requests that were used for the validated numbers. Applying it unchanged on another provider leaves those pods Pending. Replace that RDMA block with the cluster’s NIC/RDMA mechanism before deploy. Aggregated GB200 and both H200 recipes are unaffected.- H200 recipes run
`vllm-runtime:1.4.0`

(vLLM 0.26.0). GB200 recipes run this tag’s`vllm-runtime:1.5.0-deepseek-v4-pro-0813-dev.1`

image (vLLM 0.28.0). Do not mix those worker images across SKUs. - vLLM 0.27.x has an upstream accuracy regression on this checkpoint; do not use it.
`--kv-cache-dtype fp8`

is required (`DeepseekV4 fp8_ds_mla`

layout).`message.content`

can be`null`

when`--dyn-reasoning-parser deepseek_v4`

is set and the generation never emits`</think>`

; the answer is in`reasoning_content`

(upstream[vllm-project/vllm#48645](https://github.com/vllm-project/vllm/issues/48645)).- An invalid
`response_format: json_schema`

is returned as HTTP 500 rather than 4xx. - Speculative decoding is enabled on GB200 (DSpark k=5) and is not used on H200.

## Dynamo v1.5.0-inkling-dev.1

**Release Notes**


Dynamo v1.5.0-inkling-dev.1is an experimental dev build giving an early look atThinking Machines Inklingsupport on the Dynamo vLLM backend. It isnot recommended for production— features may be incomplete and APIs, behaviors, and defaults may change before the stable release. Use it for evaluation, testing, and early feedback only.

**Summary**

Dynamo v1.5.0-inkling-dev.1 adds an official **vLLM** runtime container for **Thinking Machines Inkling** (`thinkingmachines/Inkling-NVFP4`

, served as `inkling-model`

) at **NVFP4** precision, replacing hand-built images. The vLLM runtime moves to **v0.28.0** — required because the Inkling NVIDIA path, including the MTP speculative-decoding support these recipes run on, landed after 0.27.1 — and layers a vendored Inkling **structural-tag** patch plus a build-time validator on top of it ([#13954](https://github.com/ai-dynamo/dynamo/pull/13954)).

On top of that runtime, the release ships **GB300 agentic** deployment recipes: an aggregated 2x TP4 profile (recommended) and a disaggregated 1P1D profile with TP4 per role, both with MTP-8 speculative decoding, KV-aware routing, prefix caching, and 1M context, plus an AIPerf trace-replay benchmark over a 3,541-request agentic Mooncake trace ([#14237](https://github.com/ai-dynamo/dynamo/pull/14237)). The **SGLang** container path is supported from the **Day 0** release: the SGLang `agg-b200`

recipe introduced in [v1.4.0-inkling-dev.1](https://github.com/ai-dynamo/dynamo/releases/tag/v1.4.0-inkling-dev.1) is carried unchanged on this branch and continues to use `sglang-runtime:1.4.0-inkling-dev.1`

.

**Release Branch**: `release/1.5.0-inkling-dev.1`

, cut from `main`

commit `368f892c17`

(2026-08-28)

**Release Tip**: `0a4fd1d27ee1510c057be8d47183af5f2f2f41f3`


**vLLM**: v0.28.0 (`vllm/vllm-openai:v0.28.0-ubuntu2404`

base) with the Inkling structural-tag patch, NIXL v1.3.2

**Container Images**

| Backend | Arch | Image |
|---|---|---|
| vLLM (CUDA 13) | multi-arch (`amd64` + `arm64` ) |
`nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.5.0-inkling-dev.1` |
| SGLang (CUDA 13, Day 0) | multi-arch (`amd64` + `arm64` ) |
`nvcr.io/nvidia/ai-dynamo/sglang-runtime:1.4.0-inkling-dev.1` |

**Backend Versions**

| Backend | Source | CUDA | Python | Notes |
|---|---|---|---|---|
| vLLM | Dynamo-built runtime on `vllm/vllm-openai:v0.28.0-ubuntu2404` + Inkling structural-tag patch |
13.0 | 3.12 | NIXL v1.3.2; vLLM-Omni v0.28.0; `transformers` pinned <5.15 |
| SGLang | Day-0 image from v1.4.0-inkling-dev.1, custom SGLang Inkling base (`lmsysorg/sglang:inkling-cu13` ) |
13.0 | 3.12 | NIXL v1.3.0 |

**Models**

| Model | Precision | GPU | Notes |
|---|---|---|---|
`thinkingmachines/Inkling-NVFP4` |
NVFP4 | 8x GB300 | vLLM; aggregated 2 replicas x TP4 (recommended) and disaggregated 1P1D at TP4 per role; MTP-8 speculative decoding, KV-aware routing, prefix caching, 1M context, structural-tag tool calling |
`thinkingmachines/Inkling-NVFP4` |
NVFP4 (`modelopt_fp4` ) |
8x B200 | SGLang Day-0 path; aggregated TP8; text + image; EAGLE speculative decoding, FA4 attention, Mamba radix cache |

**About Inkling**

Inkling is a model from **Thinking Machines**, published on Hugging Face as `thinkingmachines/Inkling-NVFP4`

(NVFP4-quantized; the checkpoint is roughly 592 GB). It is a multimodal (text + image) hybrid Mamba/attention mixture-of-experts model with dedicated `inkling`

reasoning and tool-call parsers. This build focuses the preview on the **vLLM** GB300 agentic path while keeping the Day-0 SGLang B200 path available.

**Full Changelog**

**vLLM Backend (Inkling)**

**vLLM 0.28.0 Runtime:**Bumped the CUDA vLLM runtime base from`v0.27.1-ubuntu2404`

to`v0.28.0-ubuntu2404`

, since the Inkling NVIDIA path —`InklingMTP`

multimodal-embedding support, the FA4 relative-attention warmup migration, the Lamport shared-expert fusion, and Inkling HF-config compat — moved after 0.27.1;`xpu`

and`cpu`

stay at 0.27.1 ([#13954](https://github.com/ai-dynamo/dynamo/pull/13954)).**Inkling Structural Tag:**Vendored`container/deps/vllm/patches/v0.28.0/inkling/0001-inkling-structural-tag.patch`

to register a structural tag for vLLM's Inkling tool parser. Without it, Dynamo finds no grammar for a tool request and silently degrades to`tool_choice="auto"`

, so a forced tool choice is not honored (upstream as[vllm-project/vllm#54120](https://github.com/vllm-project/vllm/pull/54120)). Added`validate_inkling_runtime.py`

so the CUDA image build asserts the patch's postconditions rather than`patch`

's exit code ([#13954](https://github.com/ai-dynamo/dynamo/pull/13954)).**Reasoning-Token Accounting:**Carried the frontend fixes for`reasoning_tokens`

usage on the vLLM chat-processor path, which previously reported a constant value on non-streaming tool calls ([#13954](https://github.com/ai-dynamo/dynamo/pull/13954)).

**Recipes**

**Inkling GB300 Agentic Recipes:**Added`recipes/inkling/vllm/agg-gb300-agentic`

(2 replicas x TP4) and`recipes/inkling/vllm/disagg-gb300-agentic`

(1P1D, TP4 per role, rendered as a Kustomize matrix into fabric-neutral MNNVL and AWS-RoCE variants), the AIPerf trace-replay job under`recipes/inkling/perf`

,`sortOptions`

support in`scripts/kustomize-matrix.py`

, and updated Inkling docs and catalog including the declared`vllm-runtime:1.5.0-inkling-dev.1`

image ([recipe folder](https://github.com/ai-dynamo/dynamo/tree/0a4fd1d27ee1510c057be8d47183af5f2f2f41f3/recipes/inkling),[README](https://github.com/ai-dynamo/dynamo/blob/0a4fd1d27ee1510c057be8d47183af5f2f2f41f3/recipes/inkling/README.md)) ([#14237](https://github.com/ai-dynamo/dynamo/pull/14237)).**SGLang Day-0 Recipe:**`recipes/inkling/sglang/agg-b200`

is carried unchanged from the Day-0 release and remains a supported deployment path on this branch.

**Getting Started**

Deployment is Kubernetes-based (Dynamo Platform + DynamoGraphDeployment). Full steps — namespace, model-cache PVC, the ~592 GB HuggingFace download job, DGD apply, and a `/v1/chat/completions`

smoke test — are in the [recipe README](https://github.com/ai-dynamo/dynamo/blob/0a4fd1d27ee1510c057be8d47183af5f2f2f41f3/recipes/inkling/README.md). The recipes expect an `nvcr.io`

image-pull secret and an optional HuggingFace token.

**Known Issues / Limitations**

- Experimental dev preview — not QA-gated; not for production.
- The vLLM container alone is not sufficient for constrained tool calling: the worker must run with both
`--dyn-enable-structural-tag`

and`--structured-outputs-config '{"enable_in_reasoning": true}'`

, or the grammar compiles but stays inert and tool choice is unconstrained. The shipped recipes set both. - vLLM profiles are GB300-only; the SGLang path is B200-only, aggregated, with no published performance numbers.
`reasoning_budget_zero`

remains a vLLM-side limitation with no patch in this build (NVBug 6678449a).- AAC /
`.m4a`

audio decode is absent from the SGLang runtime image due to royalty-bearing codec removal.

## Dynamo v1.5.0-gemma-4-31b-dev.1

**Release Notes**


Dynamo v1.5.0-gemma-4-31b-dev.1is an experimental dev build giving an early look atGemma-4-31Bsupport on the Dynamo TensorRT-LLM backend. It isnot recommended for production— features may be incomplete and APIs, behaviors, and defaults may change before the stable release. Use it for evaluation, testing, and early feedback only.

**Summary**

Dynamo v1.5.0-gemma-4-31b-dev.1 adds an official **TensorRT-LLM** runtime container for **Gemma-4-31B**, built on **TensorRT-LLM 1.3.0rc25** (CUDA 13.2.1). The image applies a Gemma-4 video token-counting patch that is not yet in that TRT-LLM release, forwards `mm_processor_kwargs`

without mutating processor defaults, and rejects `echo`

/ `prompt_logprobs`

when speculative decoding is enabled ([#14120](https://github.com/ai-dynamo/dynamo/pull/14120)).

On top of that runtime, the release ships **aggregated TensorRT-LLM** recipes for long-context agentic traffic: 8x B200 and 8x GB200 NVFP4 + FP8 KV with MTP speculative decoding, and 8x H200 BF16 + 16-bit KV at TP4, all with KV-aware routing and CPU KV-cache offload, plus shared model-cache/download jobs and an AIPerf Mooncake trace-replay benchmark ([#13221](https://github.com/ai-dynamo/dynamo/pull/13221), [#14242](https://github.com/ai-dynamo/dynamo/pull/14242)).

**Release Branch**: `release/1.5.0-gemma-4-31b-dev.1`

, cut from `main`

commit `5a638087d8`

(2026-07-29)

**Release Tip**: `4645399ab3548a5e3baf11ea5350c6bfdede91b1`


**TensorRT-LLM**: 1.3.0rc25 (`nvcr.io/nvidia/tensorrt-llm/release:1.3.0rc25`

base) with the Gemma-4 video token-counting patch, NIXL v1.3.1

**Container Images**

| Backend | Arch | Image |
|---|---|---|
| TensorRT-LLM (CUDA 13.2.1) | multi-arch (`amd64` + `arm64` ) |
`nvcr.io/nvidia/ai-dynamo/tensorrtllm-runtime:1.5.0-gemma-4-31b-dev.1` |

**Backend Versions**

| Backend | Source | CUDA | Python | Notes |
|---|---|---|---|---|
| TensorRT-LLM | Dynamo-built runtime on `nvcr.io/nvidia/tensorrt-llm/release:1.3.0rc25` + Gemma-4 video token-counting patch (
|
13.2.1 | 3.12 | NIXL v1.3.1 |

**Models**

| Model | Precision | GPU | Notes |
|---|---|---|---|
`nvidia/Gemma-4-31B-IT-NVFP4` (+ `google/gemma-4-31B-it-assistant` for MTP) |
NVFP4 weights + FP8 KV | 8x B200 | TensorRT-LLM aggregated; 8 TP1 workers; KV-aware routing; CPU KV-cache offload; MTP |
`nvidia/Gemma-4-31B-IT-NVFP4` (+ `google/gemma-4-31B-it-assistant` for MTP) |
NVFP4 weights + FP8 KV | 8x GB200 | TensorRT-LLM aggregated; 8 TP1 workers; KV-aware routing; CPU KV-cache offload; MTP |
`google/gemma-4-31B-it` |
BF16 weights + 16-bit KV | 8x H200 | TensorRT-LLM aggregated; 2 TP4 workers; KV-aware routing; CPU KV-cache offload; MTP not enabled |

**About Gemma-4-31B**

Gemma 4 31B is a Google model served here as NVIDIA's NVFP4 instruction-tuned checkpoint on Blackwell and Google's BF16 checkpoint on Hopper. This preview covers multimodal, reasoning, and tool-calling traffic through TensorRT-LLM aggregated recipes on B200, GB200, and H200.

**Full Changelog**

**TensorRT-LLM Backend (Gemma-4-31B)**

**1.3.0rc25 Runtime:**Moved the TensorRT-LLM runtime base from`1.3.0rc22`

to`1.3.0rc25`

and recaptured per-arch SBOMs ([#14120](https://github.com/ai-dynamo/dynamo/pull/14120)).**Gemma-4 Video Token Counting:**Vendored`container/patches/trtllm/18274-gemma4-video-token-counting.patch`

so video token geometry matches the Gemma-4 video processor instead of the image-based fallback ([NVIDIA/TensorRT-LLM#18274](https://github.com/NVIDIA/TensorRT-LLM/pull/18274)) ([#14120](https://github.com/ai-dynamo/dynamo/pull/14120)).**Multimodal Processor Kwargs:**Forwards`mm_processor_kwargs`

from the request (canonical field first) and drops unknown keys before HF image-token sizing so Gemma-4 processor defaults are not mutated in place ([#14120](https://github.com/ai-dynamo/dynamo/pull/14120)).**Speculative Decoding Guard:**Rejects`echo`

/`prompt_logprobs`

when speculative decoding is enabled, which TRT-LLM does not support together ([#14120](https://github.com/ai-dynamo/dynamo/pull/14120)).

**Recipes**

**Gemma-4-31B Aggregated Recipes:**Added`recipes/gemma4-31b/trtllm/agg-b200-agentic`

,`agg-gb200-agentic`

, and`agg-h200-agentic`

, shared model-cache and download jobs, an AIPerf trace-replay job under`recipes/gemma4-31b/perf`

(3,541-request Mooncake agentic trace, 64K median ISL / 400 median OSL, ~90% KV-cache reuse), and fern catalog/docs for the`tensorrtllm-runtime:1.5.0-gemma-4-31b-dev.1`

image ([recipe folder](https://github.com/ai-dynamo/dynamo/tree/4645399ab3548a5e3baf11ea5350c6bfdede91b1/recipes/gemma4-31b),[docs](https://github.com/ai-dynamo/dynamo/blob/4645399ab3548a5e3baf11ea5350c6bfdede91b1/docs/fern/pages/recipes/model-recipes/gemma-4-31b.mdx)) ([#13221](https://github.com/ai-dynamo/dynamo/pull/13221),[#14242](https://github.com/ai-dynamo/dynamo/pull/14242)).

**Getting Started**

Deployment is Kubernetes-based (Dynamo Platform + DynamoGraphDeployment). Full steps — namespace, Hugging Face token, model-cache PVC, download job, DGD apply, and a `/v1/chat/completions`

smoke test — are in the [Gemma-4-31B recipe docs](https://github.com/ai-dynamo/dynamo/blob/4645399ab3548a5e3baf11ea5350c6bfdede91b1/docs/fern/pages/recipes/model-recipes/gemma-4-31b.mdx). The recipes expect an `nvcr.io`

image-pull secret and a Hugging Face token with access to the selected checkpoints.

**Known Issues / Limitations**

- Experimental dev preview — not QA-gated; not for production.
- MTP is not verified on H200 and is not enabled in that deployment.
- Audio is not supported by the model. Some video codecs, including AV1, are not in the runtime image.
- Chat-type endpoints only:
`/v1/chat/completions`

and`/v1/responses`

. - Multimodal items support public URLs only.
`media_io_kwargs`

applies only when frontend decoding is enabled. `reasoning_effort`

only enables or disables reasoning; the Gemma-4-31B chat template does not support finer levels.- On MTP-enabled B200/GB200, speculative decoding does not support
`min_p`

or`min_tokens`

, and rejects`frequency_penalty`

,`presence_penalty`

, and`repetition_penalty`

. Greedy decoding (`temperature=0`

) also rejects`n > 1`

and`best_of > 1`

. - For streaming responses with multimodal inputs, the HTTP status code can be misreported unless
`DYN_HTTP_PRE_COMMIT_ERROR_PEEK_MS`

is set (for example to`500`

).

## Dynamo v1.4.2

**Dynamo v1.4.2 - Release Notes**

**Summary**

Dynamo v1.4.2 is a patch release on top of [v1.4.1](https://github.com/ai-dynamo/dynamo/releases/tag/v1.4.1). It fixes **NIXL loader-path resolution** in the Frontend and SGLang Runtime images, where the Rust NIXL bindings silently ran against non-functional stubs instead of the real library. It also **removes an unused profiling plugin** from the shipped images and tightens dependency pins in the Frontend and Planner images. With this release, Dynamo also introduces **Dynamo Enterprise**: a curated set of release artifacts published for NVIDIA Enterprise Support.

**Base Branch**: `release/1.4.2`


**Dynamo Enterprise**

Starting with v1.4.2, a curated set of Dynamo release artifacts is also published under the `-enterprise`

suffix in the [Dynamo Enterprise collection](https://catalog.ngc.nvidia.com/orgs/nvidia/ai-dynamo/collections/dynamo-enterprise) on NGC. These artifacts are eligible for NVIDIA Enterprise Support under an active NVIDIA AI Enterprise subscription and carry no functional or binary differences from their open-source counterparts. See [Dynamo Enterprise](https://docs.nvidia.com/dynamo/dev/reference/enterprise/overview) for scope, supported artifacts, and coverage terms.

**Bug Fixes**

**Frontend NIXL Loader Path:**Fixed the Frontend image leaving the NIXL library where the dynamic loader could not find it ([#13547](https://github.com/ai-dynamo/dynamo/pull/13547)). The Rust bindings resolve the C API with a bare`dlopen("libnixl_capi.so")`

and the runtime extension carries no RPATH, so Rust NIXL silently ran against non-functional stubs while the Python bindings worked in the same interpreter. The image now installs NIXL from PyPI at a target-scoped`nixl_ref`

(v1.3.2) and registers the wheel's library directory with`ldconfig`

.**SGLang NIXL Loader Path:**Fixed the same loader-path gap in the SGLang Runtime image ([#13649](https://github.com/ai-dynamo/dynamo/pull/13649)). The wheel's library directory is now found during the existing UCX layout scan and registered in`ld.so.conf.d`

, keeping the UCX compat directory's priority for`libucp`

/`libucs`

. The`agg_vision.sh`

workaround that exported the directory by hand is removed; the image covers it.

**Dependency Changes**

**EFA Installer:**Updated the AWS EFA Installer to v1.50 in the EFA image variants ([#13690](https://github.com/ai-dynamo/dynamo/pull/13690)).**Pillow Floor:**Held pillow at the declared v12.3.0 floor in the Frontend and Planner images ([#13741](https://github.com/ai-dynamo/dynamo/pull/13741)).**Plotext Constraint:**Pinned`plotext`

below v6 in the Planner image; plotext v6 removes the`plot_size`

API that AIConfigurator profiler runs depend on ([#13716](https://github.com/ai-dynamo/dynamo/pull/13716)).**Nsight EFA Metrics Plugin:**Removed the unused plugin from the shipped images;`nsys profile --enable=efa_metrics`

is no longer available inside the containers ([#13743](https://github.com/ai-dynamo/dynamo/pull/13743),[#13847](https://github.com/ai-dynamo/dynamo/pull/13847)).

**Key Dependencies**

Backend runtime versions are unchanged from v1.4.1:

Dynamo |
SGLang |
TensorRT-LLM |
vLLM |
NIXL |
UCX |
|---|---|---|---|---|---|
v1.4.2 |
`v0.5.16` |
`v1.3.0rc22` |
`v0.26.0` |
`v1.3.2` (vLLM, Frontend) / `v1.3.1` (TensorRT-LLM) / `v1.3.0` (SGLang) |
`v1.21.0` |

**CUDA Variants**

Backend |
CUDA 12 |
CUDA 13 |
|---|---|---|
| SGLang | N/A | 13.0 |
| TensorRT-LLM | N/A | 13.1 |
| vLLM | N/A | 13.0 |

For container images, wheels, Helm charts, and Rust crates, see [Dynamo Release Artifacts](https://docs.nvidia.com/dynamo/latest/resources/release-artifacts).

For full version compatibility information, see [Dynamo Support Matrix](https://docs.nvidia.com/dynamo/latest/resources/support-matrix).