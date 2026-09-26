# [Issue #2417] [RFE]: Add optional receive queues to the GDAKI backend

source: https://github.com/NVIDIA/nccl/issues/2417
state: open | updated: 2026-09-21T20:06:56Z
labels: 

## 正文

## Request

We would like to propose optional receive-queue support for the GDAKI GIN backend.

Today GDAKI creates send-only RC QPs. A GPU application can construct an RDMA Write with Immediate WQE, but the receiving QP has neither receive credits nor a GPU-visible receive CQ. This prevents a GPU-side notification protocol based on Write with Immediate.

Our use case is a GPU application that uses Write with Immediate as a notification after a one-sided write. The application owns the immediate encoding, WQE construction, CQ polling, and receive-credit replenishment; it does not require NCCL to own that protocol.

## Proposed minimal scope

The implementation adds an opt-in `NCCL_GIN_GDAKI_RECV_DEPTH` parameter. Its default is zero, preserving the current send-only behavior.

When it is nonzero, GDAKI would:

- create an RQ and a GPU-resident, non-collapsed receive CQ for each connected remote main QP;
- keep self and companion QPs send-only;
- pre-post one receive WQE per RQ slot using the existing registered sink MR;
- export the RQ geometry, RQ DBR, consumer/producer state, lock, and receive-CQ descriptor through unused space in the existing device QP layout;
- reject CPU-proxy and software-emulated DBR modes for this opt-in path, since receive credit replenishment needs a GPU-addressable RQ DBR.

The device-QP size and existing key offsets are retained. The receive CQ depth is required to match the RQ depth, and the receive CQ disables overrun so completion notifications are not discarded.

No public NCCL API, new public runtime symbol, or cross-backend WImm API is proposed. The change is restricted to the GDAKI/GPUNetIO resource lifecycle.

## Validation

We have validated the RQ-backed Write-with-Immediate path end-to-end in our target multi-node environment on the `v2.30.7-1` port. The same minimal resource change has also been ported to current master and fully compiled with CUDA 12.9 / GCC 13.3 for `sm_90`, including an independent CUDA RQ-resource probe.

The test coverage includes the disabled path (`RECV_DEPTH=0`), enabled remote main QPs, self/companion QPs remaining without an RQ, initial receive credits, and the application-level Write-with-Immediate receive path. We can provide logs, a focused reproducer, and the current-master patch if this direction is of interest.

## Questions for maintainers

1. Is an opt-in GDAKI RQ/CQ resource feature, with the application consuming the GDAKI receive descriptor and managing notification progress, an acceptable integration boundary?
2. Should the required changes under the bundled `doca-gpunetio` tree be proposed directly in NCCL, or first upstreamed to its source project and then synchronized here?
3. If this direction is acceptable, would you prefer this resource-only change, or a future public/cross-backend GIN interface for immediate-data notifications?

This seems adjacent to the GIN queue-control work described in #2090. It also builds on the GDAKI per-peer QP model discussed in #2226.


## 评论 (6)

### mkbk-with-circle · 2026-09-17

The current-master implementation is now available for review:

https://github.com/mkbk-with-circle/nccl/tree/gin-gdaki-rq

It is based on `fd168324` and is split into two signed commits:

1. `bc3e98a9 Fix GDAKI CQ allocation error cleanup`
2. `dccaada9 Add optional receive queues to GDAKI`

The feature commit is limited to the optional GDAKI RQ/CQ resource lifecycle. `NCCL_GIN_GDAKI_RECV_DEPTH` defaults to zero, so the existing send-only path is unchanged. It does not add a public NCCL WImm API or application protocol.

We have validated the RQ-backed Write-with-Immediate path in our target multi-node environment. The current-master branch also completed a clean CUDA 12.9 / GCC 13.3 `sm_90` build, including compilation and linking of an independent CUDA RQ-resource probe.

Before opening a PR, we would appreciate guidance on the three interface/ownership questions in the issue. We can provide the focused reproducer and detailed environment logs if useful.


### mkbk-with-circle · 2026-09-19

Hello？ 🥹

### mkbk-with-circle · 2026-09-19

The implementation is now available for review as PR #2425:

https://github.com/NVIDIA/nccl/pull/2425

It has been rebased onto current master `12df1a11` (v2.32.3-1) and completed a clean CUDA 12.9 / GCC 13.3 `sm_90` build, producing the shared library, static library, and `ncclparam`.

The PR remains intentionally limited to the optional GDAKI RQ/CQ resource lifecycle. The interface and bundled-DOCA ownership questions in this RFE remain useful review context.


### xiaofanl-nvidia · 2026-09-21

Hi @mkbk-with-circle - Currently we cannot directly take contributions on doca-gpunetio path from NCCL, since NCCL releases copy source code as is from this repo: https://github.com/NVIDIA-DOCA/gpunetio. 

However, I will get this RFE to the developers of gpunetio and let you know what they think. ++ @pakmarkthub fyi. 

BTW, due to the large number of issues, PRs and RFEs (both internal and external), we try to scrub and review all github activities on a weekly basis at this time. Thanks for your patience! 

### mkbk-with-circle · 2026-09-21

Hi @xiaofanl-nvidia 
Thank you for clarifying and for forwarding this to the GPUNetIO developers.

We understand that NCCL vendors the doca-gpunetio source as-is, so this change should not be merged directly through the NCCL repository. We will keep the current NCCL PR as a reference only and wait for guidance from the GPUNetIO team.

Once the preferred contribution path is confirmed, we would be happy to prepare a focused contribution against the GPUNetIO repository and then update the NCCL integration accordingly. We can also provide the reproducer, validation logs, and detailed environment information if helpful.

Thanks again for your help and patience.

### pakmarkthub · 2026-09-21

Hi @mkbk-with-circle ,

Thank you for sharing the PoC. We acknowledge the request and will look into it. The GPUNetIO project does not accept external contributions currently, so we cannot take in your PoC.
