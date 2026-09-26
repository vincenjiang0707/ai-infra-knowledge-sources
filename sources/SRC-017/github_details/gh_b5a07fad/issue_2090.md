# [Issue #2090] [Roadmap]: NCCL Roadmap Q2 2026

source: https://github.com/NVIDIA/nccl/issues/2090
state: open | updated: 2026-09-24T18:33:30Z
labels: roadmap

## 正文

# NCCL Roadmap (Q2 2026)

This issue tracks planned NCCL development and releases for Q2 2026.  
Plans are subject to change as the team iterates and receives feedback.  
If you have suggestions for features, please open a feature request or comment below.

---

## Recently Released: NCCL 2.29.7

### Release Highlights

- **Device API & GIN enhancements:** Multi‑context and exclusive‑context GIN support, VA‑based GIN signals with strict window ordering, advanced GIN queue control (queue depth, manual credit management, aggregation), and support for platforms without cross‑rail connectivity.  
- **New device‑side APIs:** New device entry points, including device Copy / ReduceCopy / ReduceSum operations across multiple data types and reduction ops.  
- **Dynamic memory offload:** `ncclCommSuspend()` / `ncclCommResume()` to release and restore communicator memory plus basic communicator memory‑overhead tracking.  
- **Hybrid LSA+GIN ReduceScatter kernels:** Built‑in hierarchical LSA+GIN symmetric kernels for ReduceScatter to improve performance and scalability, with opt‑out via `NCCL_SYM_GIN_KERNELS_ENABLE=0`.  
- **Port failover support:** Automatic IB/RoCE port failover in the internal transport plugin so communication continues transparently when local links fail. Enable by setting `NCCL_IB_RESILIENCY_PORT_FAILOVER=1`.  
- **Symmetric memory improvements:** Abort support in symmetric kernels and `NCCL_CHECK_MODE=DEBUG` to validate symmetric buffer registration.  
- **Project layout & build updates:** `ext-*` moved under `plugins/`, `nccl4py` and IR moved under `bindings/`, `examples` moved under `docs/examples`, plus CMake install / `find_package` support and CMake build support for NCCL4Py.  
- **Tooling, compatibility, and bug fixes:** Improved GIN error handling, P2P transport fixes, CE‑based collective fallbacks, better cleanup of symmetric windows, GIN counter/signal fixes, licensing updates, and other stability improvements.  

For the full release notes, see:  **[NCCL v2.29.7‑1 Release](https://github.com/NVIDIA/nccl/releases/tag/v2.29.7-1)** 

---

## Coming Soon: NCCL 2.30

**NEW!** v2.30 development branch is visible now on GitHub: https://github.com/NVIDIA/nccl/tree/v2.30

### Release Highlights

- **Device API improvements:** Moved GIN context to `devComm`; added versioning to `ncclDevComm`; added timeout support to the device API.  
- **GIN.get:** Add nonblocking `gin.get` with `flush` so kernels can issue GPU‑initiated gets and check completion/visibility without stalling.  
- **Elastic Buffer:** Treat large tensors as multi‑segment windows where an active region resides in GPU memory and the remainder in host memory, enabling larger effective models and smoother spilling.  
- **One‑sided API with CUDA graph:** One‑sided APIs (`ncclPutSignal`, `ncclWaitSignal`) now work with CUDA graph capture and replay.  
- **Multi‑rank GPU & MPS:** Allow multiple processes to share the same GPU, enabling MPS‑based resource sharing.  
- **TMA support:** Add Tensor Memory Accelerator (TMA) support in select built‑in symmetric kernels to offload bulk peer‑to‑peer copies and reductions, improving NVLink bandwidth and latency.  
- **DDP support:** Enable Dynamic Direct Path (DDP) so that NCCL can take advantage of hardware multipath and out‑of‑order receive for higher network performance on supported systems.  
- **NCCL parameter infrastructure:** Add new C APIs to support querying NCCL parameters. E.g. `ncclParamGet()` for querying individual parameters through raw memory pointers.  
- **Port Recovery:** Improve NCCL’s ability to recover from transient network issues so communicators can continue operating without full re‑initialization.  

> **Disclaimer:** All early‑preview development branches are made available to the community to facilitate collaboration and engagement. We do not guarantee any functional stability, performance or compatibility on development branches before they are officially released.

---

## Q2 Roadmap – May ’26–July ’26

- **CuTe DSL:** Provide CuTe‑based DSL integration for NCCL device APIs so frameworks can generate NCCL‑enabled kernels from higher‑level Python abstractions.  
- **Elastic Buffer for GIN:** Extend Elastic Buffer support into the GIN device API.  
- **Batched Get for GIN:** Enable efficient completion checks for batches of GIN gets so users can group many small gets and confirm when each batch is done, reducing overhead.  
- **Async flush for GIN.get:** Add an asynchronous flush API so kernels can check completion of GIN gets without blocking.  
- **Simultaneous GIN Proxy & GDAKI:** Allow different communicators to select different GIN backends so applications can route specific workloads through the most appropriate GIN implementation.  
- **Lamport kernels:** Use Lamport‑style schemes in symmetric kernels to reduce synchronization overhead and tail latency for low‑latency collectives.  
- **NVLS + PAT:** Enhance PAT support for NVLS to improve small‑ and medium‑message performance in multi‑PPN configurations.  
- **LL/LL128 device API:** Expose LL/LL128 collectives through the NCCL device API so kernels can directly launch low‑latency protocols.  
- **Zero‑SM AllGather:** Extend zero‑SM paths to AllGather so copy engines and proxies handle data movement while freeing SMs for compute.  
- **Symmetric A2A:** Add new hierarchical symmetric All‑to‑All kernels to improve performance and scalability for A2A.  
- **Cost model re‑architecture:** Redesign NCCL’s internal cost models to choose better algorithms across transports, topologies, and message sizes.  
- **RAS API:** Expose RAS capabilities via an API so applications can integrate NCCL health, error, and diagnostic signals directly into their observability stack.  
- **Profiler improvements:** Extend profiler integration so device APIs and symmetric kernels are fully visible, easing performance analysis and tuning.  

> **Disclaimer:** Some of the features above will be released in an update during Q2 (for example in 2.30.X or a later 2.31).

---

## Features Under Consideration

- **Custom comms ops hook:** Add hooks so frameworks or users can plug in custom kernels/algorithms and let NCCL select them via the unified cost model.  
- **SM‑initiated CE collectives:** Explore enabling SM‑initiated collectives on copy engines to increase overlap between communication and computation.  
- **SET signal operation in GIN:** Add a SET‑style signal primitive so kernels can directly write signal values for simpler synchronization patterns.  
- **CUDA checkpoint:** Enable whole‑process CUDA checkpoint/restore so NCCL communicators, registered memory, and CUDA Graphs with NCCL collectives remain usable after restore and significantly reduce model cold‑start time.  
- **Determinism improvements:** Add a deterministic mode for collectives to improve reproducibility and make debugging large‑scale runs easier.  
- **JIT support for Device APIs:** Add explicit JIT‑recompile support so kernels can be JIT‑compiled against the current NCCL version, using a device‑side DevComm pointer so host and device stay version‑compatible without extra complexity.  

Let us know how to improve or prioritize these features for your distributed and multi-GPU workloads! Contributions, code feedback, issue submissions, and discussion are welcome.

## 评论 (14)

### shubh3794 · 2026-04-27

Strongly support the release as **CUDA checkpoint** has been a strong blocker for us, here are some of the issues I ran into which will help narrow down the scope:
1) https://github.com/NVIDIA/cuda-checkpoint/issues/48 : I am able to get around the NVML's invocation of getDeviceByBusId by using a LD_PRELOAD shim, but it still fails in lower layers (due to CUDA not refreshing the cache of device->bus_id->handles post restore).
2) https://github.com/NVIDIA/nccl/issues/2117

### WizardKing-Asta · 2026-05-14

Is the receive send PXN being implemented or is it already implemented? 

### wangshaochuang · 2026-05-18

Are there any plans to support GIN data planes for other vendors? Or move the gin ops to plugin interface?

### gab9talavera · 2026-05-18

> Is the receive send PXN being implemented or is it already implemented?

This is already implemented. Please see how to set [here](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html#nccl-p2p-pxn-level).

### xiaofanl-nvidia · 2026-05-18

> Are there any plans to support GIN data planes for other vendors? Or move the gin ops to plugin interface?

@wangshaochuang yes, we are actively working with AWS EFA team to add GIN support with GDA. 
EFA already supports CPU proxy path via plugin: https://github.com/aws/aws-ofi-nccl
We are going to work with other network vendors as well in the future. Let me know if that answers your question. 

### wangshaochuang · 2026-05-19

> > Are there any plans to support GIN data planes for other vendors? Or move the gin ops to plugin interface?
> 
> [@wangshaochuang](https://github.com/wangshaochuang) yes, we are actively working with AWS EFA team to add GIN support with GDA. EFA already supports CPU proxy path via plugin: https://github.com/aws/aws-ofi-nccl We are going to work with other network vendors as well in the future. Let me know if that answers your question.

Is there a Gin design framework that supports multiple vendors? When is this feature going to be released? Thanks


### sjeaugey · 2026-05-19

> Is there a Gin design framework that supports multiple vendors? When is this feature going to be released? Thanks

This was already answered. Yes, and it is already released. The PROXY backend can support different plugins. The GDAKI backend is tied to IB/RoCE so it can only work with IB/RoCE plugins. But we can add new backends for other vendors.



### wangshaochuang · 2026-05-20

> > Is there a Gin design framework that supports multiple vendors? When is this feature going to be released? Thanks
> 
> This was already answered. Yes, and it is already released. The PROXY backend can support different plugins. The GDAKI backend is tied to IB/RoCE so it can only work with IB/RoCE plugins. But we can add new backends for other vendors.

OK，thanks

### msaroufim · 2026-05-21

>CUDA checkpoint: Enable whole‑process CUDA checkpoint/restore so NCCL communicators, registered memory, and CUDA Graphs with NCCL collectives remain usable after restore and significantly reduce model cold‑start time.

This feature would materially improve our work at Core Automation and I also know of many inference providers that would love something like this. Companies like Modal built large businesses just focused on cold starts.

We're often experimenting with different model architectures and different kernels and when we'd like to test them out for real we like spin up a real inference server to make sure we see real perf improvements. The biggest source of slowdown for us is waiting on cuda graph warmup which unfortunately isn't really optional Blackwell+

### functionstackx · 2026-05-24

any plans for multi-node over IB/RoCE cuTile integration via nccl device API?

### gab9talavera · 2026-05-26

> any plans for multi-node over IB/RoCE cuTile integration via nccl device API?

Yes there are plans, but no timeline we have committed to yet. We are aiming for sometime in second half of year.

### jmracek · 2026-06-11

>CUDA checkpoint: Enable whole‑process CUDA checkpoint/restore so NCCL communicators, registered memory, and CUDA Graphs with NCCL collectives remain usable after restore and significantly reduce model cold‑start time.

Just want to advocate strongly for this one.  It would be a massive win for the platform I operate. 

### gab9talavera · 2026-06-11

> > CUDA checkpoint: Enable whole‑process CUDA checkpoint/restore so NCCL communicators, registered memory, and CUDA Graphs with NCCL collectives remain usable after restore and significantly reduce model cold‑start time.
> 
> Just want to advocate strongly for this one. It would be a massive win for the platform I operate.

Please check out initial support added [here](https://github.com/NVIDIA/nccl/tree/master/contrib/nccl_checkpoint). We have CUDA graph capture and Device API support on the roadmap for this as well.

### jmracek · 2026-09-24

@gab9talavera Let me point the engineers on my team at this.  Thank you and sorry it took so long to notice! I almost never stay logged into my personal GitHub, but this issue came up again and I had a flicker of a memory that I had discussed this at some point.
