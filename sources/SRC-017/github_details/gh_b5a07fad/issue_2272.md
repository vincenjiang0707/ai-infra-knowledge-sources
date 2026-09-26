# [Issue #2272] NCCL Roadmap: Aug - Oct 2026

source: https://github.com/NVIDIA/nccl/issues/2272
state: open | updated: 2026-09-21T03:30:37Z
labels: roadmap

## 正文

# NCCL Roadmap (August-October 2026)

This issue tracks planned NCCL development and releases for the August-October 2026 roadmap window. Plans are subject to change as the team iterates, completes validation, and receives feedback.

If you have suggestions for features, please open a feature request or comment below.

---

## Recent News

- **NCCL 2.30.7 released:** See [NCCL v2.30.7-1 release notes](https://github.com/NVIDIA/nccl/releases/tag/v2.30.7-1).
- **NCCL-EP v0.1 released:** See [NCCL-EP v0.1.0 release notes](https://github.com/NVIDIA/nccl/releases#release-nccl-ep-v0.1.0).
- **NCCL4Py v0.3.1 released:** See [NCCL4Py v0.3.1 release notes](https://github.com/NVIDIA/nccl/releases#release-nccl4py-v0.3.1).
- **Exploratory contributions:** `nccl/contrib` hosts exploratory contributions using NCCL's host and device APIs.
- **Community learning docs:** `nccl/docs/contrib` hosts community contributions on NCCL learning docs.
- **Developer guide:** `nccl/docs/dev_guide` contains coding style guides for community contributions.
- **Stable branches:** `master`, `staging`, and `dev` are now in use and mirror all commits.

---

## Coming Soon: NCCL 2.31

- **Compute Fabric Transport (CFT) through Device API:** Expose CFT through the NCCL Device API as a handle-based communication model for logical endpoint reachability.
- **Simultaneous GIN proxy and GDAKI usage:** Allow both paths to be used together, improving flexibility for Device API and GPU-initiated networking workflows.
- **EFA GDA support in GIN:** Enable NCCL's GPU-initiated communication path to work efficiently over AWS EFA.
- **Per-collective configurability:** Add more configuration controls at the individual collective level.
- **Device API JIT recompilation:** Add explicit JIT-recompile support for backward compatibility.
- **Extended PAT support:** Extend PAT beyond one GPU per communicator per node.
- **Cost-model rearchitecture:** Begin redesigning NCCL cost-model logic so algorithm selection can become more accurate and extensible.
- **Legacy and symmetric-kernel host-side unification:** Rework host-side handling to unify legacy and symmetric-kernel paths.
- **NCCL diagnostics with RAS:** Add initial support to NCCL diagnostics mode that will expand observability and resilience tooling.
- **Profiler support for symmetric kernels:** Add profiling support for NCCL symmetric kernels.

---

## Roadmap - August-October '26

- **Rubin support:** Support Rubin architecture with different topology and performance optimizations. 
- **Unify legacy kernels using Device API:** Rebuild legacy NCCL collective paths, such as TREE, RING, and LL, on the newer Device API path, unifying different paths in NCCL and lowering the learning curve to use NCCL.
- **Custom kernel hook:** Let advanced users plug in or register custom communication kernels or algorithms so NCCL can select them at runtime.
- **More Device API primitives:** Provide more higher-level Device API primitives to help users write more complex kernels without reinventing the wheel.
- **GIN backend improvements:** Provide more APIs to unlock more performance from GIN.
- **Symmetric A2A kernel:** Add a new all-to-all path built around symmetric memory to cut latency, reduce GPU SM and memory overhead, and improve bandwidth.
- **Lower internal memory overhead:** Reduce NCCL internal memory overhead and allocator waste in large-scale runs so users can preserve more GPU memory for model state and payload buffers.
- **Multiple profiler plugin support:** Allow multiple profiler plugins to be loaded simultaneously.
- **MIG support:** Provide guidance and validation to enable NCCL workloads under MIG mode.
- **GIN over Sockets:** Support a GIN plugin using TCP sockets so users without access to IB/RoCE can experiment with GIN.
- **More complete DSL support:** Improve NCCL support with CuTeDSL and add cuTile support.
- **NCCL Notify:** Add structured event notifications for NCCL/RAS-detected faults so applications can detect failures faster and trigger their own recovery workflows.

> Disclaimer: Some of the features above will be released in an update during Q3, for example in a later 2.31.x patch, rather than in the first tagged build.

---

## Features Under Consideration

- **SM-initiated CE collectives:** Add MMIO-CE support for SM-initiated Copy Engine collectives, enabling lower-SM-overhead data movement paths.
- **Low-precision collectives:** Add MXFP8, MXFP4, and NVFP4 support for better performance. See [NCCL issue #2199](https://github.com/NVIDIA/nccl/issues/2199).
- **Leverage JIT for NCCL kernels:** Add a new mode to use JIT support for NCCL's internal collective kernels, reducing binary size and potentially improving performance.
- **Encryption for socket path:** Add encryption support to socket connections used by bootstrap and some data paths in selected scenarios.
- **NCCL-tests in PyTorch:** Port NCCL-tests to PyTorch so users can benchmark individual collectives using PyTorch.
- **Determinism improvements:** Add a deterministic mode for collectives to improve reproducibility and make debugging large-scale runs easier.
- **Windows support:** Support NCCL on Windows with validation, documentation, and performance guidance.
- **nccl4rust:** Provide Rust bindings for NCCL host and device APIs. 
- **CUDA Checkpoint support improvements:** Remove previous deviceAPI, CUDA Graph, and strict library-version limitations.  Improve support for new IP on restore.

Let the team know how to improve or prioritize these features for distributed and multi-GPU workloads. Contributions, feedback, and discussion are welcome.


## 评论 (14)

### visualxu · 2026-07-22

The CE collective initiated by SM is very useful in the field of computing and communication fusion/overlap, such as allgather/alltoall gemm/megamoe. Hopefully, it will be included in the August-October roadmap.

### xiaofanl-nvidia · 2026-07-22

> The CE collective initiated by SM is very useful in the field of computing and communication fusion/overlap, such as allgather/alltoall gemm. Hopefully, it will be included in the August-October roadmap.

@visualxu thanks for the feedback. Could you please share some info on your intended use case for this feature and some high level expectation on performance? E.g. how fast does the CE copy need to be for it to be useful to your application? 1us, 10us, 100us? 


### xiaofanl-nvidia · 2026-07-26

Change log (7/26): 
- Added nccl4rust in future consideration
- Added Rubin support to roadmap

### gab9talavera · 2026-08-10

Change log (8/10):

- Added CUDA Checkpoint support improvements in features under consideration

### luiscape · 2026-08-10

@gab9talavera thank you for the CUDA checkpoint addition. I just made [this suggestion](https://github.com/NVIDIA/nccl/issues/2337) for how to make NVLS state checkpointable, and would love your input. This tope (checkpoint / restore) is very important for us at [Modal](https://modal.com/) and we'd love to contribute.

### dearsxx0918 · 2026-08-18

Is it possible to achieve very low latency communication (sending/receiving)?
My user case is MD(molecular dynamics), which requires very low latency for sending/receiving, approximately 50-100ns per 128 bits.

### sjeaugey · 2026-08-18

@dearsxx0918 I'm not sure what you mean by "50-100ns per 128 bits". The instruction writing 128 bits to a remote buffer may take as little as 5-10ns (overhead), but just the travel time through PCI or NVLink will take ~500ns at least (latency).

Now, if we're not talking about low-level load/store operations but high-level send/recv semantics, we need to add a lot of code around the load/stores to signal data has been send and verify on the receive side that data has arrived. I.e. the synchronization code. Depending on the protocol that can take between 500ns and 5 us: the LL protocol is considered to have a latency of 1us, while LL128 has a latency of 2us and Simple 6 us.

So for "send/recv communication latency", your ask is already an order of magnitude off at the hardware level, and even more unattainable at the protocol level.

Hope that makes sense.

### dearsxx0918 · 2026-08-19

```bash
> [@dearsxx0918](https://github.com/dearsxx0918) I'm not sure what you mean by "50-100ns per 128 bits". The instruction writing 128 bits to a remote buffer may take as little as 5-10ns (overhead), but just the travel time through PCI or NVLink will take ~500ns at least (latency).
> 
> Now, if we're not talking about low-level load/store operations but high-level send/recv semantics, we need to add a lot of code around the load/stores to signal data has been send and verify on the receive side that data has arrived. I.e. the synchronization code. Depending on the protocol that can take between 500ns and 5 us: the LL protocol is considered to have a latency of 1us, while LL128 has a latency of 2us and Simple 6 us.
> 
> So for "send/recv communication latency", your ask is already an order of magnitude off at the hardware level, and even more unattainable at the protocol level.
> 
> Hope that makes sense.
```

Thank you for your prompt response. Based on your comment, I believe it will be difficult to achieve my performance goals as we require low latency data transmission from two GPUs, with each transmission (128 bits) controlled between 50-100 ns. But still thanks!


### halfmanli · 2026-08-30

@gab9talavera @xiaofanl-nvidia  @sjeaugey Could you clarify how SM-initiated MMIO-CE works? Does an SM submit a CE pushbuffer and ring a GPU-visible doorbell, or directly program CE through MMIO?



### gab9talavera · 2026-09-01

> [@gab9talavera](https://github.com/gab9talavera) [@xiaofanl-nvidia](https://github.com/xiaofanl-nvidia) [@sjeaugey](https://github.com/sjeaugey) Could you clarify how SM-initiated MMIO-CE works? Does an SM submit a CE pushbuffer and ring a GPU-visible doorbell, or directly program CE through MMIO?

Thanks for the question. This work is still under investigation. We will share more once we have an update.

### ToLiveAndLove · 2026-09-08

Regarding the **GIN over Sockets** item on this roadmap — we'd like to propose a complementary **DPDK-based backend**, and offer to implement it.A socket backend solves availability, but its syscall and in-kernel copy overhead sits right on top of the message sizes GIN cares about most (MoE dispatch/combine is often a few KB to tens of KB), so it can't be used for performance work. A userspace polling datapath would let the same hardware reach close to its actual limit. We see the two as complementary, not competing: sockets as the broadest-coverage fallback with no performance claim, DPDK for users willing to accept the extra deployment requirements
(hugepages, VF/dedicated NIC, core pinning). Is this a direction you'd welcome?

### xiaofanl-nvidia · 2026-09-14

> Regarding the **GIN over Sockets** item on this roadmap — we'd like to propose a complementary **DPDK-based backend**, and offer to implement it.A socket backend solves availability, but its syscall and in-kernel copy overhead sits right on top of the message sizes GIN cares about most (MoE dispatch/combine is often a few KB to tens of KB), so it can't be used for performance work. A userspace polling datapath would let the same hardware reach close to its actual limit. We see the two as complementary, not competing: sockets as the broadest-coverage fallback with no performance claim, DPDK for users willing to accept the extra deployment requirements (hugepages, VF/dedicated NIC, core pinning). Is this a direction you'd welcome?

@ToLiveAndLove Thanks for the proposal! We are discussing it internally and will let you know! 

### xiaofanl-nvidia · 2026-09-14

> [@gab9talavera](https://github.com/gab9talavera) [@xiaofanl-nvidia](https://github.com/xiaofanl-nvidia) [@sjeaugey](https://github.com/sjeaugey) Could you clarify how SM-initiated MMIO-CE works? Does an SM submit a CE pushbuffer and ring a GPU-visible doorbell, or directly program CE through MMIO?

@halfmanli we plan to leverage new CUDA APIs to implement this. 
The CUDA feature will use existing CE work submission paths available in hardware, with a combination of what you described above. Hope this helps. 

### xiaofanl-nvidia · 2026-09-21

Hi @ToLiveAndLove we discussed the DPDK backend for GIN and have some questions: 
- What's the target deployment environment for this backend? 
- Is it the goal of the DPDK backend to reach line rate of the NIC (that are not RDMA capable), thus better than existing TCP socket solution? 
- Could you describe the high level architecture of this backend implementation? E.g. Will it mostly leverage the existing CPU-proxy path but use some DPDK specific API in the plugin? Will it need to rely on GDRCopy functionality similar to the TCP socket? 

Two general suggestions: 
1. NCCL's GIN layer is designed to be extensible by custom vendors. We encourage the community to develop plugins for all use cases that are important to your network backend, and then leverage NCCL's API layering to run useful workloads "for free". It is a great idea to develop and maintain a plugin for DPDK, and we can discuss the upstreaming once we see the general benefits to a wide group of use cases.
2. If you already have such an implementation and want to share with us or have more design discussions & questions for us, we encourage you to open a github RFC issue. It'll make tracking easier for us as well. Thank you! 
