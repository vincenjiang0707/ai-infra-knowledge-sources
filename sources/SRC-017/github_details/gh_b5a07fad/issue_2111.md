# [Issue #2111] [RFC] nccl-ep: support Attention–MoE disaggregation

source: https://github.com/NVIDIA/nccl/issues/2111
state: open | updated: 2026-09-18T10:03:18Z
labels: 

## 正文

## Background

Attention–FFN disaggregation (AFD) is an emerging MoE serving architecture where **Attention nodes** and **Expert/FFN nodes** are physically separate groups of GPUs.  The motivation is that attention is memory-bandwidth-bound while expert MLPs are compute-bound, so a homogeneous deployment cannot optimally utilize hardware for both.

Multiple production systems have shipped this architecture:
- **MegaScale-Infer** (ByteDance, arXiv:2504.02263) — disaggregated expert parallelism at scale
- **Step-3** (StepFun, arXiv:2507.19427) — model-system co-design for cost-effective decoding
- **xDeepServe** (Huawei CloudMatrix384, arXiv:2508.02520) — model-as-a-service with AFD

vLLM has an active implementation RFC: [vllm-project/vllm#22799](https://github.com/vllm-project/vllm/issues/22799), with a follow-on elastic AFD RFC at [vllm-project/vllm#27584](https://github.com/vllm-project/vllm/issues/27584).

---

## Change in traffic pattern

Today, EP solutions assumes **symmetric, homogeneous ranks**: every rank in the EP group participates in both dispatch (sending tokens) and combine (receiving results), and every rank also runs the attention and expert layers.  

AFD breaks this symmetry:

| | Standard EP | AFD |
|---|---|---|
| **Topology** | Single homogeneous group | Two disjoint groups: A-side (N_a ranks) and F-side (N_f ranks) |
| **Attention** | Runs on every rank | Runs only on A-side ranks |
| **Expert MLP** | Runs on every rank | Runs only on F-side ranks |
| **Dispatch direction** | Each rank → all ranks in EP group | A-side ranks → F-side ranks |
| **Combine direction** | All ranks → each rank in EP group | F-side ranks → A-side ranks (back to source) |
| **Routing table** | Computed and consumed locally | Computed on A-side, communicated to F-side |

---

## Proposed changes

### 1. Asymmetric communicator initialization

Allow an EP communicator to be created over two disjoint rank groups.  Both groups participate in the same nccl-ep operation but play different roles:

```c
// Illustrative API — exact names TBD
ncclResult_t ncclEpCommCreateAF(
    ncclComm_t      comm,          // communicator spanning A ∪ F ranks
    int             numAttnRanks,
    int*            attnRanks,     // which global ranks are A-side
    int             numExpertRanks,
    int*            expertRanks,   // which global ranks are F-side
    ncclEpAfComm_t* afComm         // output handle
);
```

A-side and F-side handles derived from `afComm` would carry role-specific state (routing table, expert placement, buffer pointers).

### 2. A-side dispatch and combine

The A-side initiates all token movement.  Its dispatch call encodes the routing decisions (topk_idx) and sends tokens to the correct F-side expert ranks:

```c
// A-side: send tokens to experts on F-side
ncclResult_t ncclEpAfDispatch(
    ncclEpAfHandle_t handle,
    const void*      send_x,          // [local_tokens, hidden]
    const int32_t*   topk_idx,        // [local_tokens, topk] — expert indices
    const float*     topk_weights,
    ncclEpConfig_t   config,
    cudaStream_t     stream
);

// A-side: receive combined expert outputs
ncclResult_t ncclEpAfCombine(
    ncclEpAfHandle_t handle,
    void*            recv_x,          // [local_tokens, hidden]
    ncclEpConfig_t   config,
    cudaStream_t     stream
);
```

### 3. F-side receive and return

The F-side blocks for incoming tokens, processes them (externally, by the MoE kernel), then sends results back to the originating A-side ranks:

```c
// F-side: receive tokens dispatched from A-side
ncclResult_t ncclEpAfRecv(
    ncclEpAfHandle_t handle,
    void**           recv_x,          // [total_recv_tokens, hidden] — filled by nccl-ep
    int64_t*         expert_offsets,  // [num_local_experts]
    int64_t*         expert_counts,   // [num_local_experts]
    ncclEpConfig_t   config,
    cudaStream_t     stream
);

// F-side: return expert outputs to A-side
ncclResult_t ncclEpAfReturn(
    ncclEpAfHandle_t handle,
    const void*      expert_out,      // [total_recv_tokens, hidden]
    ncclEpConfig_t   config,
    cudaStream_t     stream
);
```

The F-side output format should support the same layout options as the current EP API, including the [2D expert-contiguous layout requested in #2109](https://github.com/NVIDIA/nccl/issues/2109).

### 4. Routing metadata propagation

In standard EP the routing table lives on every rank.  In AFD, the router runs on the A-side but the F-side needs to know how to demultiplex incoming tokens into per-expert buffers.  Options:

- **Option A (inline)**: Embed per-token expert assignments in the dispatch payload header; F-side reconstructs offsets from them.
- **Option B (sidecar)**: A-side sends a compact routing bitmap / count vector ahead of the payload via a fast sidecar channel, enabling the F-side to pre-allocate and pre-compute expert offsets before bulk data arrives (analogous to how `ncclEpUpdateHandle` preprocessing works today).

Option B maps more cleanly onto the existing preprocessing + dispatch two-phase model in nccl-ep.

---

## Transport considerations

The A↔F boundary typically crosses nodes (NVLink connects intra-node, RDMA crosses nodes).  The existing nccl-ep RDMA transport path should be directly applicable to the A→F and F→A transfers.  However, unlike standard EP where every rank both sends and receives in the same operation, AFD requires:

- A-side: pure sender for dispatch, pure receiver for combine
- F-side: pure receiver for dispatch, pure sender for combine

This asymmetry may require changes to how nccl-ep sets up RDMA QPs and manages credit/flow control.

---

## Open questions

1. **N_a : N_f ratio** — Should the API allow arbitrary ratios (e.g. 4 attention ranks : 32 expert ranks)? Likely yes.
2. Buffer mapping would not be at full scale. Can we map only receiver ranks' buffer into sender's VA?  
3. **Elastic A/F membership** — vLLM RFC #27584 asks for online scale-in/out of A and F workers.  Is elastic AFD in scope for a future follow-on, or should the initial API be designed to accommodate it?

---

## Relationship to other open RFCs

| Issue | Topic | Relevance |
|---|---|---|
| [#2109](https://github.com/NVIDIA/nccl/issues/2109) | 2D expert-contiguous output | F-side output format for AFD |
| [#2104](https://github.com/NVIDIA/nccl/issues/2104) | CUDA Graph capture | A-side and F-side steady-state loops should be graph-capturable |
| [#2110](https://github.com/NVIDIA/nccl/issues/2110) | Elastic buffers | Useful for variable A/F traffic without worst-case allocation |

## 评论 (1)

### 0z5a · 2026-09-18

Hi @kwen2501 , I’d like to work on the initial implementation of this RFC in `NVIDIA/nccl-extensions`.

For the first slice, I’m thinking of focusing on the asymmetric A/F rank-role plumbing and a minimal dispatch/combine correctness path, without trying to cover elastic membership or the full RDMA/HT optimization path yet.

If this direction is still open and matches the current nccl_ep design, I’m happy to take it and send a scoped PR.

