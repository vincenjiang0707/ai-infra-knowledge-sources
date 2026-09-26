# restore-llm-inference-capacity-in-seconds-with-shadow-engine-recovery-in-nvidia-dynamo

source: https://developer.nvidia.com/blog/restore-llm-inference-capacity-in-seconds-with-shadow-engine-recovery-in-nvidia-dynamo/

When an LLM engine process fails, the standard recovery path involves a cold restart. This requires loading weights into HBM from storage, compiling kernels, and capturing NVIDIA CUDA graphs. For large models, initialization can take several minutes, during which surviving workers must absorb the displaced traffic.

Shadow engine recovery, available as a [preview feature](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/shadow-engine-failover) in NVIDIA Dynamo, moves most of this recovery work off the serving path. It keeps a fully initialized shadow engine idle on the same GPUs as the active engine. The *GPU Memory Service* (GMS) shares the existing weights between the engines without creating another copy in HBM. If the active process fails, the shadow takes over within seconds. Re-initialization occurs in the background entirely off the serving path.

We measured the impact by deliberately terminating one worker in a two-worker GLM-5.2 deployment. Without shadow engine recovery, the remaining worker served all incoming traffic during the 283-second cold restart, increasing TTFT and reducing per-user decode rate throughout the outage. With shadow engine recovery, a second worker resumed serving in 7.3 seconds, nearly 39 times faster, minimizing disruption to service quality.

## Why LLM inference recovery is slow: two core problems

Production LLM engines commonly experience recoverable software faults, including process crashes, recoverable CUDA errors, and transient collective failures. In these cases, the hardware, drivers, and node remain healthy; only the process holding the corrupted state is lost, and a replacement engine can typically start on the same GPUs.

So why can’t that fresh engine skip the initialization cost? Two problems stand in the way:

**Weights are tied to the engine process.**GPU memory is linked to the engine’s CUDA context, which is itself tied to the engine process. When the process exits, the driver releases all resources, including weights already resident in GPU memory. Consequently, a replacement engine process must repeat the full weight-loading procedure.**Some initialization states are non-transferable.**NCCL and`torch.distributed`

communicators bind to the specific running process, and CUDA graphs are fixed to the virtual addresses present during capture. These states can’t be handed off from a previous engine and must be recreated during every restart.

Shadow engine recovery addresses each problem with a targeted optimization: decoupling weight lifetime from the engine process, and completing non-transferable initialization before a failure.

## How shadow engine recovery works

Shadow engine recovery combines persistent GPU memory, a pre-warmed standby engine, and worker-level coordination to recover without a cold restart.

### GPU Memory Service: Persistent GPU memory for LLM inference

The GPU Memory Service (GMS) manages specific memory regions, such as weights, independently of the engine process. By using a process distinct from the engine to own these regions, weights remain resident in memory even as engines are restarted. As a result, a new engine on the same GPU can attach to existing memory.

GMS is a per-GPU sidecar that owns physical GPU memory on behalf of inference engines. It is mostly dormant and has no CUDA context of its own; it allocates physical pages, hands out handles to them, and arbitrates which engines may read or write at any time. Engines connect, import handles, and map the underlying pages at virtual addresses in their own CUDA contexts. Mapping happens once, at startup, and GMS is not involved in any subsequent access.

This functionality is built on the CUDA Virtual Memory Management API. With this API, physical GPU memory and its associated virtual addresses can have independent lifetimes. Since physical allocations are reference-counted, they survive as long as any process maintains a mapping. Two engines mapping the same weight tensor access the same physical bytes, each using virtual addresses local to its context. A kernel reading a weight dereferences an ordinary pointer into the same HBM the weight would have occupied anyway, so a GMS-backed read costs no more than an engine-allocated one.

This architecture provides two benefits. First, **weights persist beyond engine failure.** While the kernel removes the failed engine’s CUDA context, the GMS reference ensures the physical pages stay resident so a fresh engine can immediately map them. Second, **weights can be shared between concurrent engines**; therefore, a secondary engine on the same GPU incurs zero marginal weight cost.

Integrating GMS into inference frameworks requires only a narrow change. vLLM, SGLang, and NVIDIA TensorRT-LLM each integrate GMS through a custom [ torch.cuda.CUDAPluggableAllocator](https://docs.pytorch.org/docs/stable/generated/torch.cuda.memory.CUDAPluggableAllocator.html) bound to the weight memory pool. From inside the engine, weights remain ordinary

`torch.Tensor`

s. Adopting GMS is as simple as flipping a flag at startup.GMS is not limited to weights. The current preview does not support using GMS for the KV cache, but that capability is under active development. The goal is for a promoted shadow to map the outgoing engine’s cache instead of rebuilding it as traffic arrives.

**Shadow engines: preinitialized standbys with zero marginal weight cost**

A shadow engine is a fully initialized engine process that remains idle and co-resident on the same GPUs as the active engine. Weight sharing makes this configuration feasible: without it, the second engine would require another full copy of the weights, substantially reducing the memory available for processing requests.

A shadow runs through the same startup path as an active engine. On each of its GPUs, it connects to the local GMS and imports the weight mappings, establishes communicators (NCCL and NIXL for KV transfer between workers), captures CUDA graphs, and performs any necessary warm-up. By the end of the startup, it is ready to serve. Then, instead of serving, it parks: it releases the materializable parts of its memory and blocks, waiting for its turn.

What a shadow has precomputed before it parks:

**CUDA context, captured graphs, and communicators.**These non-transferable components are ready when the shadow engine is activated because they cannot be inherited from another process.**Weight mappings.**The GMS handles are already imported, so waking the shadow requires only remapping them to virtual addresses established during initialization.

What it has deferred:

**KV cache materialization.***The KV cache is the largest reclaimable allocation held by an engine. The shadow reserves its address range without physical backing while parked and materializes the cache when promoted.*

A parked shadow therefore retains only its CUDA context, captured graphs, communicators, and weight mappings—no separate copy of the weights and no KV cache. This footprint is small enough for the shadow to remain alongside an active engine on the same devices, enabling recovery within seconds.

**The worker: a single deployable unit**

The following figure shows how these components fit within each worker and scale behind a shared router.

These foundations are integrated into one pod. The worker holds two engine containers, a GMS sidecar to mediate GPU memory access, and a shared lock to elect the active engine.

At steady state, one engine holds the lock and remains awake, connected to GMS, holding a materialized KV cache, and registered with the frontend router. The other remains fully initialized and connected to GMS but is dormant, holds no KV cache, and waits on the lock.

**Recovery in depth**

The following sections trace the recovery sequence and explain the synchronization and memory-management mechanisms that make it reliable.

**Sequence**

A worker moves through four phases before returning to steady state.

**T₀ Steady.**Engine A holds the lock and is awake, registered with the router. Engine B is dormant, blocked on the lock.**T₁ Failure.**Engine A’s process exits, either because it crashed outright or because a liveness probe found it hung and killed it. Either way, the kernel releases its lock as the process is reaped. The worker is briefly unroutable, until the shadow registers.**T₂ Cutover.**Engine B acquires the lock, wakes, remaps weights through GMS, materializes its KV cache, and re-registers with the router. Engine A’s container is restarted by the orchestrator.**T₃ Restarted.**Engine A finishes initialization and enters the shadow state. The system returns to a steady state, with the roles swapped.

The shadow’s advantage is that it enters T₂ already initialized. The only work on the critical path is acquiring the lock, remapping weights, and materializing the KV cache.

### Synchronization

The worker requires both mutual exclusion, ensuring only one engine is awake at a time, and reliable release to ensure the standby engine takes over if the active one fails. A POSIX `flock`

on a shared file provides these guarantees. When the active process exits due to a shutdown, segfault, or `SIGKILL`

, the kernel reaps its file descriptors, and the shadow engine acquires the lock to begin serving.

Each engine’s startup path is therefore a short leader election:

`await engine.initialize() # weight load, torch.compile, autotune, CUDA graph capture` `...` `# put the engine to sleep while we wait on the lock` `await engine.sleep()` `lock = FlockFailoverLock(lock_path)` `await lock.acquire(engine_id=engine.id) # wait on the lock to wake` `await engine.wake()` |

A deadlocked engine whose process is still alive falls to the Kubernetes liveness probe, which cascades to a `SIGKILL`

and trips the same kernel-managed release.

### Memory accounting

Fitting two engine processes on one GPU without exhausting HBM takes careful accounting across the lifecycle.

**Weights.**Allocated once by GMS and mapped read-only by every engine in the worker; never duplicated.**KV cache.**Held only by the active engine today: materialized when it wakes, released when it dies, freeing the region for the shadow to take over.**Buffers and graphs.**NCCL buffers, the CUDA context, and captured graphs. Held by each engine even while dormant, and the whole of a parked shadow’s standing cost.

**Benchmark results: shadow engine recovery vs. cold restart on GLM-5.2**

To quantify the benefit, we compared shadow engine recovery with a cold restart after an engine failure in a two-worker fleet.

**Setup**

We ran two workers serving GLM-5.2 quantized to NVFP4 on NVIDIA B200 nodes: one worker per node, TP=8, 200K max context, and an FP8 KV cache. A single frontend distributes requests round-robin across the two. The load is synthetic: 32,000 input tokens and 1,000 output tokens per request, arriving at 0.7 requests per second.

Both arms run identical engine builds and configurations; the only difference is the shadow engine. The baseline has it off, and the killed worker cold-restarts. In the Shadow Engine Recovery configuration, each worker pod hosts a preinitialized shadow engine that can take over if the active engine fails.

We injected the fault only after the workload reached its steady-state operating point: a SIGKILL to one of the two workers, followed by 600 seconds of observation. With two workers in the fleet, losing one leaves the survivor carrying every request until its partner returns.

**Results**

Metric | Baseline: cold restart | Shadow engine recovery |
|---|---|---|
| Time until a second worker serves again | 283 s | 7.3 s |
| TTFT p50, after the fault | 23,815 ms | 1,311 ms |
| Decode rate p50, after the fault | 12 tok/s/user | 46 tok/s/user |
| Requests over 5s to first token | 201 of 399 | 1 of 398 |
| Requests below 20 tok/s/user | 226 of 399 | 0 of 398 |


*Table 1.**Cold restart versus shadow engine recovery in the window after one of two workers is killed*Compared to the cold restart baseline of 283 seconds, shadow engine recovery only takes 7.3 seconds (1.7 seconds to detect the fault and 5.6 seconds to promote the shadow). This results in significantly better TTFT and decode rate after the fault, and allows us to largely avoid SLA violations.

## Current scope and next steps

Having validated that fast recovery for inference workloads on Kubernetes is feasible, we are working to stabilize the implementation and expand support to a wider range of workloads. Shadow engine recovery will roll out incrementally over the coming months.

The current preview has several limitations and deployment requirements.

- Shadow engine recovery addresses common engine process failures but does not cover hardware, node, or multi-node failures, which still rely on standard rescheduling.
- It requires Dynamic Resource Allocation (DRA) on Kubernetes, so the cluster needs Kubernetes 1.34 or newer with DRA enabled and the NVIDIA GPU DRA driver installed.
- Dynamo Snapshot can be composed with the recovery feature to minimize contention during the initialization of the shadow while serving.
- Because promoted shadows start with empty KV caches, the post-cutover TTFT experiences a slight bump. Carrying cache state across a promotion, both the prefix-cache index and the cache memory itself, is the active line of work.
- vLLM is the primary supported backend.

To try Shadow Engine Recovery, start with the [Kubernetes quickstart](https://docs.nvidia.com/dynamo/kubernetes/getting-started/quickstart) to create a running deployment. Then follow the Shadow Engine Recovery deployment workflow and use the [vLLM failover example](https://github.com/ai-dynamo/dynamo/blob/main/examples/backends/vllm/deploy/agg_failover.yaml) as a complete manifest. Visit the [ai-dynamo/dynamo repository](https://github.com/ai-dynamo/dynamo) to ask questions, report issues, or contribute.

## Start the discussion at forums.developer.nvidia.com
