# [Issue #2337] [RFE]: Add NVLS suspend / resume to ncclCommSuspend / ncclCommResume

source: https://github.com/NVIDIA/nccl/issues/2337
state: open | updated: 2026-08-23T20:32:15Z
labels: enhancement

## 正文

`ncclCommSuspend` / `ncclCommResume` has been part of the NCCL API since the [v2.29.7](https://github.com/NVIDIA/nccl/releases/tag/v2.29.7-1). The API works well when paired with other application-specific workflows to suspend and restore workloads. This is of interest to use at [Modal](https://modal.com) because many of our customers use [GPU memory snapshots](https://modal.com/blog/gpu-mem-snapshots) to snapshot initialized workloads and then restore them very fast, sometimes up to 60x faster than baseline.

When working with Hopper or Blackwell GPUS, `ncclCommSuspend` / `ncclCommResume` isn't sufficient, unfortunately. We identified that to be the case because NVLS state also needs to be managed, otherwise workloads can't be restored (`libcuda` will throw an error indicating that something is wrong). This makes any NVLS-enabled NCCL communicator incompatible with [cuda-checkpoint](https://github.com/NVIDIA/cuda-checkpoint), blocking checkpoint/restore of multi-GPU training jobs on NVLink-SHARP systems.

I suggest adding two functions: `ncclNvlsSuspend` and `ncclNvlsResume`. Both are used internally by `ncclCommSuspend` / `ncclCommResume` and perform the following operations:

- `ncclNvlsSuspend`: back up UC buffer contents to pinned host memory → unmap MC VAs → unbind UC memory from the multicast groups → release the group and UC physical handles. 
- `ncclNvlsResume`: re-create the multicast groups using the same rank-0-creates/peers-import rendezvous as initial setup, re-create UC physical memory and map it at the identical virtual addresses, restore contents from the host backups, re-bind, and re-map the MC VAs. Because every VA is unchanged, kernels, captured CUDA graphs, and persistent conn structs stay valid.
  - Resume is collective across a node's local ranks (like setup), since `cuMulticastBindMem` blocks until all devices join.

I put together a prototype [here](https://github.com/NVIDIA/nccl/compare/master...luiscape:nccl:luis/nvls-suspend-resume) and have tested it successfully in NVLS-enabled environments. I'd be happy to contribute upstream if this is the right direction.

## 评论 (7)

### zhenhaohe · 2026-08-11

Hi, could you create a PR and we could take a closer look?

### luiscape · 2026-08-11

@zhenhaohe here's the PR: https://github.com/NVIDIA/nccl/pull/2340

I'd very much appreciate community guidance. 

### lrbison · 2026-08-11

Thanks for the branch and the feature request.  I have already been working on this as part of the next phase of Checkpoint / Restore work for NCCL (and I see you already found it on our roadmap issue). I believe that work will address the issue you've raised here, and indeed for NVLink I utilize the same strategy of reserving and remapping new fabric handles.

I wonder if I might take this opportunity to ask you a few questions about your usecase:
1. Is this a single-host or multi-host checkpoint?
2. Do you use networking as well as NVLink?
3. Do you always restore on the same nodes or perhaps you migrate hosts during restore?

We plan on addressing all of these usecases.

### luiscape · 2026-08-11

Hi @lrbison, awesome. To your questions:

> Is this a single-host or multi-host checkpoint?

Single-host only. We are marginally interested in multi-host at this time. 

> Do you use networking as well as NVLink?

Only local with loopback interfaces. We manage other non-NCCL networking requirements in our checkpointing layer, so that's not a requirement for this work. 

> Do you always restore on the same nodes or perhaps you migrate hosts during restore?

We run on different hosts but hosts with the same NVLink topology and the same GPU types.

Let me know if that makes sense. Happy to share more -- or to meet via call if that makes things easier. 

### lrbison · 2026-08-11

Yes, these all make sense.  Thank you!

### luiscape · 2026-08-11

@lrbison want me to close this PR or is it useful to keep it open for discussion? 

### lrbison · 2026-08-12

@luiscape lets close the PR (but thank you for submitting it!) but leave this issue open.
