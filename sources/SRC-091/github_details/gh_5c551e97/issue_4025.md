# [Issue #4025] LMCache 2026 Q3 Roadmap

source: https://github.com/LMCache/LMCache/issues/4025
state: open | updated: 2026-09-17T06:27:49Z
labels: 

## 正文

# LMCache 2026 Q3 Roadmap 

In Q3, we are evolving towards a more distributed, more performant, and smarter KV cache management stack based on the MP mode. 
In the meantime, we will start the deprecation process of the non-MP mode since Q3.

## 1. Distributed KV Cache: 

**Objective: efficiently handle KV caches that are distributed across multiple nodes**
- [ ] “Coordinator mode” with native language (c++/rust) implementation
- [ ] P2P KV cache sharing stress test and performance optimization
  - [ ] #4041 
- [ ] Native PD disaggregation in MP mode

## 2. Serving Engine Integration: 

**Objective: Ensure a performant and stable integration with popular serving engines**

- [ ] SGLang MP mode async store/retrieve support
- [ ] SGLang HiCache integration 
- [ ] Integrate with the latest vLLM interfaces
- [ ] Omni model support (vLLM-omni, SGL-omni)

## 3. KV Cache Management Interface

**Objective: enable users to control KV caches manually**

- [ ] Pin, delete, and move KV caches ( #3978 , #3990 )
- [ ] Inspect and update KV caches
- [ ] Configure the management policy (eviction, store, and prefetch policies) during runtime

## 4. Ecosystem Support

**Objective: support and integrate with the latest innovations in the ecosystem**

- [ ] Step-by-step guide for new accelerator/platform integration. ( #4004 )
- [ ] New accelerators 
  - [ ] MACA ( #4833 )
  - [ ] Ascend ( #3968 )
  - [ ] MooreThreads 
  - [ ] AWS Trainium
- [ ] Step-by-step guide for new storage integration
- [ ] New storage systems
  - [ ] MinIO
  - [ ] 3FS 
  - [ ] io_uring
- [ ] GDS support in L2 adapters

## 5.  Production Deployment

**Objective: have a cloud-native way to deploy MP mode smoothly** 

- [ ] Remove the hostIPC & privileged mode requirement from the LMCache operator
- [ ] Fault tolerance and high availability features for the LMCache coordinators

## 6. KV Cache Optimization Algorithms

**Objective: make KV cache smaller, faster, and smarter**

- [ ] CacheBlend mode and deployment guide
- [ ] More KV Cache compression algorithms

## 7. Core Optimizations

**Objective: improve the LMCache internal modules**

- [ ] Profiling & benchmarking the LMCache core 
- [ ] Reduce GIL contentions and context switches in the main store/retrieve loop
- [ ] Replace modules with native implementations to have better performance



## 评论 (30)

### Liusixuuu · 2026-07-07

Hi team, I'd like to help with the P2P KV cache sharing stress test and performance optimization. I've raised an issue for it: #4041 .

### limarkdcunha · 2026-07-08

Hi team, I would be interested in working upon, the Native PD disaggregation in MP mode, I am actually working right now on adding SGLang PD disagg support to Ray serve and for the same I had to dig deep to understand how both vLLM and SGLang go about doing PD disagg and hence I think I will be able to tackle this.  Thanks

### ApostaC · 2026-07-08

> Hi team, I would be interested in working upon, the Native PD disaggregation in MP mode, I am actually working right now on adding SGLang PD disagg support to Ray serve and for the same I had to dig deep to understand how both vLLM and SGLang go about doing PD disagg and hence I think I will be able to tackle this. Thanks

Thanks for your interest! Feel free to create an RFC issue with an initial design doc. 

### limarkdcunha · 2026-07-10

Hi team, here is the RFC I created for 
Native PD disaggregation in MP mode. https://github.com/LMCache/LMCache/issues/4085.

Looking forward to your opinion and comments Thanks

### neel429 · 2026-07-12

Hi team, I am interested in contributing to the "CacheBlend mode and deployment guide" item on the Q3 roadmap. I've spent real time in vLLM's KV cache manager and block allocation internals which is the same layer CacheBlend operates at,so I'm not starting cold on the mechanics of non-prefix KV reuse.  I also wanted to check scope so I don't duplicate effort: is this mainly about closing the gaps in #2921  (reproduction guide request) and #1936 (which i see is stale)  (CacheBlend not engaging through vLLM serve), or is there a different piece you'd consider the priority right now?

### wangxuw · 2026-07-12

Hi team — I'd like to put my hand up for the **"CacheBlend mode and deployment guide"** item, and I'm happy to collaborate.

I've read through the current blend code, so a quick take on the gap (correct me if I'm off):

- There are **three coexisting generations**: legacy `examples/blend_kv`, the v1 layerwise path (`examples/blend_kv_v1`), and a newer **V3** under `lmcache/v1/multiprocess/modules/blend_v3.py`.
- The only path reachable through `vllm serve` today is **v1 layerwise** (`enable_blending: True` → `vllm_v1_adapter` → `LMCBlender`), still relying on the manual `gpu_worker.py` patches — which I'd assume should now be **deprecated** in favor of V3.
- **V3** looks server-side complete (mp cache-server, full `CB_*` RPC surface, design docs), but those RPCs have **no caller on the `integration/vllm/` side yet** — documented, but not wired up from the engine.

So I've got two scope questions before starting:

1. **Where does the V3 engine-side wiring live?** I'm assuming the plugin code that drives the `CB_*` calls already exists in a private repo — but without access I can't tell what's still unsupported, and can't get **`vllm serve` + LMCache mp running with blend V3 end-to-end**. Could you share the current state / access so I don't duplicate work?
2. **For the deployment guide** — the operator already lands this via a container image + DaemonSet + webhook plugin injection (`cacheblend_pod_injector`, the `cacheblendengines` CRD). So the question is how a guide should handle the case of **no image-registry access**?

Happy to kick off with a short design note once you point me at the intended target.


### ApostaC · 2026-07-13

@neel429 @wangxuw thanks for your interest to Cacheblend! To clarify, we have some internal threads for releasing the cacheblend special docker image and setup instructions. Please stay tuned if you guys are interested!

### theap06 · 2026-07-20

@ApostaC I've put up #4151 for that. It exports the coordinator's OpenAPI schema to a committed file.

### Smallfu666 · 2026-07-23

Hi team — I'd like to help with the "Profiling & benchmarking the LMCache core" item under Core Optimizations.

I checked the current tooling first. `lmcache bench server` is useful as an end-to-end sanity test, but it currently runs a single client sequentially and does not expose a concurrency sweep or machine-readable results. My proposed first slice would be to extend it with:

* configurable concurrent clients / outstanding requests;
* stable latency and throughput summaries;
* JSON/CSV output suitable for before/after comparisons;
* a small reproducible MP benchmark matrix on H100/H200.

This would provide a common baseline for evaluating ongoing work such as the recent object-group transfer consolidation in #3908, before attempting any larger GIL or native-module changes. I can also collect lightweight CPU/thread/context-switch profiles where the environment permits, but I would keep the first contribution focused on the benchmark harness and reproducibility.

Is anyone already working on a canonical core baseline, or would this initial scope be useful?


### sbates130272 · 2026-07-23

> Hi team — I'd like to help with the "Profiling & benchmarking the LMCache core" item under Core Optimizations.
> 
> I checked the current tooling first. `lmcache bench server` is useful as an end-to-end sanity test, but it currently runs a single client sequentially and does not expose a concurrency sweep or machine-readable results. My proposed first slice would be to extend it with:
> 
> * configurable concurrent clients / outstanding requests;
> * stable latency and throughput summaries;
> * JSON/CSV output suitable for before/after comparisons;
> * a small reproducible MP benchmark matrix on H100/H200.
> 
> This would provide a common baseline for evaluating ongoing work such as the recent object-group transfer consolidation in #3908, before attempting any larger GIL or native-module changes. I can also collect lightweight CPU/thread/context-switch profiles where the environment permits, but I would keep the first contribution focused on the benchmark harness and reproducibility.
> 
> Is anyone already working on a canonical core baseline, or would this initial scope be useful?
> 

This would be useful. Can you also consider using mock backends with parametrized latencies so enable simulation of different storage backends and the impacts those latencies have at the lmcache level?

### Smallfu666 · 2026-07-23

Thanks @sbates130272 — that makes sense and fits the proposed baseline well.

There is already an in-tree `MockL2Adapter` that models bandwidth-limited transfers using a size-proportional delay, but it does not currently model fixed service latency: store and load only account for bandwidth, while lookup completes immediately.

For the first slice, I'd extend the existing adapter with deterministic, configurable latency for the store, lookup, and load paths, while retaining the current bandwidth parameter. I can then include it in the benchmark matrix alongside real backends, so we can sweep backend service time and separate storage delay from LMCache-side queueing and scheduling overhead.

Jitter/distribution models and failure or timeout injection would be useful follow-ups, but I'd keep the initial change focused on fixed latency plus bandwidth so the results remain simple and reproducible.


### sbates130272 · 2026-07-23

> Thanks @sbates130272 — that makes sense and fits the proposed baseline well.
> 
> There is already an in-tree `MockL2Adapter` that models bandwidth-limited transfers using a size-proportional delay, but it does not currently model fixed service latency: store and load only account for bandwidth, while lookup completes immediately.
> 
> For the first slice, I'd extend the existing adapter with deterministic, configurable latency for the store, lookup, and load paths, while retaining the current bandwidth parameter. I can then include it in the benchmark matrix alongside real backends, so we can sweep backend service time and separate storage delay from LMCache-side queueing and scheduling overhead.
> 
> Jitter/distribution models and failure or timeout injection would be useful follow-ups, but I'd keep the initial change focused on fixed latency plus bandwidth so the results remain simple and reproducible.
> 

Thanks. Makes total sense. A fixed delay that is a parameter we can change via ya ml makes sense. And extending that to a distribution at a later date also makes sense. 

### JiahengX · 2026-07-24

Hi team — I'd like to help with the “Inspect and update KV caches” item under the KV Cache Management Interface.

I checked the current APIs first. `GET /cache/objects` already provides paginated L2 object listing, but there is no unified, targeted inspection flow for checking the L1/L2 state of a specific token sequence or set of object keys.

I propose splitting the inspection work into two phases:

- **Phase 1 — Node-local L1 inspection:** add a read-only, key-addressed API to report whether specific objects are present in L1 and expose basic runtime metadata, without changing locks, LRU state, or cache contents.
- **Phase 2 — L2 and Coordinator integration:** add a side-effect-free, key-addressed inspection capability for supported L2 adapters, then expose a token-based Coordinator API that resolves `token_ids` into object keys, routes the request to the target MP server, and aggregates the L1/L2 results.

The final goal is to let an operator provide a model and token sequence and determine where the corresponding KV cache objects are located, how much space they occupy, and their current state across nodes and storage tiers.

Does this match the intended scope of “Inspect KV caches”? Is anyone already working on this, or would this two-phase approach be useful?

Two additional questions that would help define the implementation:

1. For the first phase, should inspection use a new endpoint such as `POST /cache/objects/inspect`, or should it extend the existing `GET /cache/objects` API? Which L1 metadata is appropriate to expose?
2. For the second phase, should the Coordinator inspect only a specified MP server, or should it support fleet-wide aggregation? Which L2 adapters should be included in the initial implementation?

### sbates130272 · 2026-07-24

> Hi team — I'd like to help with the “Inspect and update KV caches” item under the KV Cache Management Interface.
> 
> I checked the current APIs first. `GET /cache/objects` already provides paginated L2 object listing, but there is no unified, targeted inspection flow for checking the L1/L2 state of a specific token sequence or set of object keys.
> 
> I propose splitting the inspection work into two phases:
> 
> - **Phase 1 — Node-local L1 inspection:** add a read-only, key-addressed API to report whether specific objects are present in L1 and expose basic runtime metadata, without changing locks, LRU state, or cache contents.
> - **Phase 2 — L2 and Coordinator integration:** add a side-effect-free, key-addressed inspection capability for supported L2 adapters, then expose a token-based Coordinator API that resolves `token_ids` into object keys, routes the request to the target MP server, and aggregates the L1/L2 results.
> 
> The final goal is to let an operator provide a model and token sequence and determine where the corresponding KV cache objects are located, how much space they occupy, and their current state across nodes and storage tiers.
> 
> Does this match the intended scope of “Inspect KV caches”? Is anyone already working on this, or would this two-phase approach be useful?
> 
> Two additional questions that would help define the implementation:
> 
> 1. For the first phase, should inspection use a new endpoint such as `POST /cache/objects/inspect`, or should it extend the existing `GET /cache/objects` API? Which L1 metadata is appropriate to expose?
> 2. For the second phase, should the Coordinator inspect only a specified MP server, or should it support fleet-wide aggregation? Which L2 adapters should be included in the initial implementation?

This sounds great. Can I ask that you also add any Prometheus metrics that make sense and are related? I am thinking guagues for number of objects in L1 and L2. Total size in Bytes of L1 and L2 objects. A histogram of how many times a block has been retrieved. A histogram of time between retrieves etc. 

These metrics would help LMCache users make good decisions on sizing of L1 and L2 based on their workloads. 

Thoughts?

### markhpc · 2026-07-24

@sbates130272 I would still very much like to see more about your test harness and prometheus setup! ;)

### markhpc · 2026-07-24

> Thanks [@sbates130272](https://github.com/sbates130272) — that makes sense and fits the proposed baseline well.
> 
> There is already an in-tree `MockL2Adapter` that models bandwidth-limited transfers using a size-proportional delay, but it does not currently model fixed service latency: store and load only account for bandwidth, while lookup completes immediately.
> 
> For the first slice, I'd extend the existing adapter with deterministic, configurable latency for the store, lookup, and load paths, while retaining the current bandwidth parameter. I can then include it in the benchmark matrix alongside real backends, so we can sweep backend service time and separate storage delay from LMCache-side queueing and scheduling overhead.
> 
> Jitter/distribution models and failure or timeout injection would be useful follow-ups, but I'd keep the initial change focused on fixed latency plus bandwidth so the results remain simple and reproducible.

This sounds great.  I'm just getting up to speed now, do we have any existing baseline tests that we can compare against?

### JiahengX · 2026-07-24

Thanks @sbates130272 — that makes sense. I agree that targeted inspection and aggregate Prometheus metrics would complement each other well.

To keep the changes focused and reviewable, I’m thinking of delivering the work incrementally:

1. node-local L1 inspection;
2. side-effect-free L2 inspection for the agreed adapters;
3. token-based Coordinator routing and L1/L2 result aggregation;
4. missing L1/L2 object-count and total-size gauges, reusing existing metrics where possible;
5. an inter-retrieve-time histogram;
6. A retrieves-per-object histogram based on object lifecycle tracking.

For the histograms, per-object state would be maintained internally, while Prometheus would expose only aggregated buckets rather than ObjectKey labels.

I’ll keep each PR focused and define the exact observation semantics before starting the histogram work. Would this breakdown make sense?

### sbates130272 · 2026-07-24

> Thanks @sbates130272 — that makes sense. I agree that targeted inspection and aggregate Prometheus metrics would complement each other well.
> 
> To keep the changes focused and reviewable, I’m thinking of delivering the work incrementally:
> 
> 1. node-local L1 inspection;
> 2. side-effect-free L2 inspection for the agreed adapters;
> 3. token-based Coordinator routing and L1/L2 result aggregation;
> 4. missing L1/L2 object-count and total-size gauges, reusing existing metrics where possible;
> 5. an inter-retrieve-time histogram;
> 6. A retrieves-per-object histogram based on object lifecycle tracking.
> 
> For the histograms, per-object state would be maintained internally, while Prometheus would expose only aggregated buckets rather than ObjectKey labels.
> 
> I’ll keep each PR focused and define the exact observation semantics before starting the histogram work. Would this breakdown make sense?

@JiahengX this looks like a reasonable approach to me. Feel free to tag me when you start opening PRs. Thanks for being open to my input! Good hunting 😃!

### sbates130272 · 2026-07-24

LMCache Team

I'd like to discuss adding more p2p modes to the roadmap. As I understand it right now only L1 CPU DRAM <-> L1 CPU DRAM is supported (via NIXL and RDMA). 

I think supporting the other L1 options (DAX and NVMe-L1 slab) would be possible and useful. And a mode from L2 when local NVMe to a L1 location on the remote node could be very useful too. 

Ideally we could aim for a converged mode where all node local KV blocks are accessible to all nodes via the p2p path. And all shared L2s are shared via the standard shared storage path. 

I'd appreciate peoples' thoughts and level of interest. And maybe, given positive, a discussion on how to make this a roadmap item for Q3/4!

Thanks!

### JiahengX · 2026-07-25

Thanks @sbates130272 ! I’ve opened #4239 to track the inspection and Prometheus metrics work incrementally. I’ll start with the node-local L1 inspection and tag you when the first PR is ready.

### Smallfu666 · 2026-07-25

Hi team — before I spend GPU time validating the concurrent core benchmark, I'd like to confirm the intended baseline topology so the H100/H200 numbers are measuring what you'd expect.

The current implementation uses one `MessageQueueClient` and one registered KV-cache context per benchmark worker. Each client has a distinct DEALER identity, so on a dedicated MP server the workers can be assigned to separate affinity workers when `concurrency <= max_gpu_workers`. Since the affinity-pool size is not currently queryable over RPC, the bench takes it as `--server-max-gpu-workers` and refuses to run when `N` exceeds it. Concurrent `store-only` / `retrieve-only` workloads use the lmcache-driven handle path; engine-driven data-mode concurrency is intentionally outside this change.

Two quick checks:

1. **Topology:** Is one client plus one context per worker, with distinct affinity identities on a dedicated server, the shape you would expect for establishing the MP STORE/RETRIEVE concurrency baseline? If you would measure it differently, I would rather align before running the matrix.
2. **PR shape:** The current change is fairly large. Would you prefer one complete benchmark PR, or a split? I can land a smaller concurrency/workload-modes core first, including the required correctness and fail-close behavior, then follow with profiling integrations and extended reporting if that is easier to review.

If the direction aligns, I'll finish the remaining failure-path validation, run the H100/H200 concurrency matrix with per-handler affinity and overlap evidence—not only aggregate throughput—and then open the PR.

### zhengfeihe · 2026-07-27

Hi @Smallfu666 @sbates130272 ! Thanks for digging into this and for the careful thought and work you've put into it.

Adding concurrency is a great improvement to the current work.

I'd recommend dropping the H100/H200 matrix, though, not the concurrency work itself, just the fixed-hardware results. Tests in LMCache Bench should stay model- and hardware-agnostic and focus on LMCache-internal, component-level benchmarks: concurrency is fine as a user-configurable knob, but committing fixed numbers for specific GPUs isn't reproducible for anyone without those cards and goes stale fast, better to let each user run it on their own setup and compare before/after. Hardware/model-specific end-to-end benchmarking is already handled externally; I checked with @ApostaC offline yesterday, and for reference  (https://github.com/SemiAnalysisAI/InferenceX/blob/main/benchmarks/single_node/agentic/dsv4_fp4_b200_vllm.sh) measuring how LMCache contributes to serving-engine performance.

The same applies to the "common baseline" framing. Core optimizations vary too much for a single baseline to be meaningful, and many improvements—memory usage, tail latency, lock contention, hit rate—may not show up clearly in a throughput benchmark.

Happy to hear your thoughts or any alternative ideas. Could you also create a separate issue for this so we can keep the main thread focused?

### haowu1234 · 2026-07-31

Hi team, I opened an RFC for the roadmap item "Configure the management policy (eviction, store, and prefetch policies) during runtime": #4360.\n\nThe RFC proposes a phased runtime policy model for MP mode: Phase 1 covers safe node-local hot updates for store/prefetch selectors and eviction tunables, while later phases discuss coordinator fan-out and stateful eviction-policy migration.\n\nFeedback on the scope and API boundary would be appreciated.

### rob-9 · 2026-08-07

Hi team, I’m interested in contributing additional KV compression algorithms. 

I’ve reviewed the MP serde path. My understanding is that each L2 adapter can include a `serde` config, which is parsed into `SerdeConfig`. `StorageManager` then uses `SerdeL2AdapterWrapper` to compose serialization around the underlying adapter. New single-tensor serde implementations generally provide a synchronous `Serializer`/`Deserializer` pair, wrap it with `AsyncSerdeProcessor`, and register it through `register_serde_factory`. 

Currently on `dev`, the registered compression serde types appear to be `fp8` and `turboquant`. I also reviewed the multi-output `MultiSerializer`/`MultiDeserializer` interfaces and asymmetric K16/V8 implementation from #3277, as well as the follow-up MP integration and component-level K/V placement work tracked in #3710.

Are there other compression algorithms or device backends the team would like prioritized? There is existing work around CacheGen (#3796) and hardware-accelerated compression (#4149/#4264). 

### sbates130272 · 2026-08-07

> Hi team, I’m interested in contributing additional KV compression algorithms. 
> 
> I’ve reviewed the MP serde path. My understanding is that each L2 adapter can include a `serde` config, which is parsed into `SerdeConfig`. `StorageManager` then uses `SerdeL2AdapterWrapper` to compose serialization around the underlying adapter. New single-tensor serde implementations generally provide a synchronous `Serializer`/`Deserializer` pair, wrap it with `AsyncSerdeProcessor`, and register it through `register_serde_factory`. 
> 
> Currently on `dev`, the registered compression serde types appear to be `fp8` and `turboquant`. I also reviewed the multi-output `MultiSerializer`/`MultiDeserializer` interfaces and asymmetric K16/V8 implementation from #3277, as well as the follow-up MP integration and component-level K/V placement work tracked in #3710.
> 
> Are there other compression algorithms or device backends the team would like prioritized? There is existing work around CacheGen (#3796) and hardware-accelerated compression (#4149/#4264). 

Hi @rob-9. A serde plugin that leverages nvCOMP and the new hipCOMP for on GPU decompression could be useful. We already have GDS/AIS support for DMA into VRAM from local NVMe and remote storage via RDMA. If we could load in compressed KV Blocks and then decompress on the GPU via those libraries it might save load times. I think compression is better done async by the CPU but you could explore that too. Thanks! Happy to review any pref data and discuss. 

### JianDan0212 · 2026-08-31

Hi, I’d like to bring up a small note. #3856 (linked under "New accelerators" → MACA) has been closed and superseded by #4833  — same MACA backend support tracking, updated status and roadmap (original author left MetaX; I've taken over stewardship). Could you update the checklist reference to point to #4833  instead of #3856, so it doesn't read as done just because the old issue is closed? @ApostaC @maobaolong 

### orthur2 · 2026-09-13

Hi, I've been working on the cache move part of the KV Cache Management Interface roadmap, initially supporting L1-to-L1 moves in MP mode. I've opened #5083 with the proposal and #5086 and #5089 with the implementation. 

Looking forward to your feedback.

### chrisyifanjin · 2026-09-14

Hi team — I’m interested in the “Step-by-step guide for new storage integration” roadmap item.

The existing docs cover MP-mode plugins and native connectors. Would a worked walkthrough for adding an in-tree Python MP L2 adapter be useful?

I’d propose tracing one existing adapter through config/factory registration, the asynchronous store/lookup/load lifecycle, and a reproducible CPU-only validation flow, linking existing contract documentation where possible.

Is that the intended gap, and is there an adapter you’d recommend using as the reference? Happy to adjust if someone is already working on this.


### 0z5a · 2026-09-15

Hi @ApostaC , I checked Omni model support (vLLM-omni, SGL-omni), and found there are already some basic support for vLLM-Omni in LMCache, but I couldn't find any existing LMCache integration for SGLang-Omni. I would like to take the basic support for SGLang-Omni if it is still available.

### jt-tsai-1225 · 2026-09-17

> [@neel429](https://github.com/neel429) [@wangxuw](https://github.com/wangxuw) thanks for your interest to Cacheblend! To clarify, we have some internal threads for releasing the cacheblend special docker image and setup instructions. Please stay tuned if you guys are interested!

Hi @ApostaC , 

Does v0.5.5 support CacheBlend in MP mode? I tested it and there's still no working interface —
the vLLM-side connector has no code path that calls into the blend protocol, so it behaves like a
plain prefix cache.

Is there an expected release timeline for the CacheBlend special image?
