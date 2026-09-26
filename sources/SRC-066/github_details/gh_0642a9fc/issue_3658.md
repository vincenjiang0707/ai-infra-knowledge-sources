# [Issue #3658] [BUG][CuTe DSL] PipelineTmaUmma arrival masks include an out-of-cluster "v-peer" bit when the cluster's v-extent is 1, causing CGA out-of-range faults (Xid 13)

source: https://github.com/NVIDIA/cutlass/issues/3658
state: open | updated: 2026-09-22T21:13:10Z
labels: 

## 正文

## Environment

- nvidia-cutlass-dsl **4.6.2** (the code is unchanged at current `main`)
- CUDA 13.0, Blackwell (sm_103a)

## Summary

`PipelineTmaUmma._compute_mcast_arrival_mask`
(`python/CuTeDSL/cutlass/pipeline/sm100.py`, [L101-L157](https://github.com/NVIDIA/cutlass/blob/main/python/CuTeDSL/cutlass/pipeline/sm100.py#L101-L157))
unconditionally ORs in "peer" image masks computed at the coordinate

```python
block_in_cluster_coord_vmnk_peer = (
    cta_in_cluster_coord_vmnk[0] ^ 1,
    *cta_in_cluster_coord_vmnk[1:],
)
```

The v-peer only exists for `tcgen05.CtaGroup.TWO` (v-extent 2). For a plain
non-paired cluster, e.g. `cta_layout_vmnk = (1, C, 1, 1)` — the natural
configuration for a TMA load multicast shared by C CTAs that each run their
own MMA — the peer coordinate `(1, b, 0, 0)` lies **outside the layout's
domain** (mode 0 has extent 1). With the compact strides `(1, 1, C, C)` it
evaluates to rank `b + 1`, so the mode-1 peer image is bits `{1..C}`. The
resulting producer/consumer mask is `{0..C}`: it contains **bit C, a CTA
rank that does not exist in the cluster**.

`PipelineTmaUmma.create` computes these masks whenever
`cute.size(cta_layout_vmnk) > 1`
([L290-L300](https://github.com/NVIDIA/cutlass/blob/main/python/CuTeDSL/cutlass/pipeline/sm100.py#L290-L300))
with no check on the v-extent, and `consumer_mask = producer_mask`. The same
helper is used by `PipelineTmaMultiConsumersAsync.create`
([L1244](https://github.com/NVIDIA/cutlass/blob/main/python/CuTeDSL/cutlass/pipeline/sm100.py#L1244)),
which is exposed the same way.

By contrast, `PipelineAsyncUmma.create` implements the intended pattern: it
only computes peer masks when the pipeline actually uses 2-CTA UMMA
("No mcast mask if we're not using 2CTA tcgen05 MMA").

## Observed behavior

A kernel with a TMA-load producer (data multicast along mode 1, mask built
with `cpasync.create_tma_multicast_mask(..., mcast_mode=1)`) and tcgen05
UMMA consumers, on a 4-CTA cluster created as
`PipelineTmaUmma.create(..., cta_layout_vmnk=(1, 4, 1, 1))`:

- The kernel faults at cluster scope once consumers start releasing buffers.
  `dmesg` shows **Xid 13, "SM Cga Exception: OOR Addr"** — an SM-side
  cluster (mapa/remote-mbarrier) out-of-range access, matching an
  `mbarrier.arrive` aimed at rank 4 of a 4-CTA cluster.
- An ablation that arrives with a self-only mask instead converts the crash
  into a hang (remote arrivals missing), confirming the mask — not the TMA
  transaction accounting — is at fault.

## Workaround

Overriding both masks right after `create()` with the plain mode-1 image
mask fixes the fault; results are then bit-exact against the equivalent
non-clustered kernel:

```python
coord = cta_layout_vmnk.get_flat_coord(cta_rank_in_cluster)
mask = cpasync.create_tma_multicast_mask(cta_layout_vmnk, coord, mcast_mode=1)
object.__setattr__(pipeline, "consumer_mask", mask)   # frozen dataclass
object.__setattr__(pipeline, "producer_mask", mask)
```

## Suggested fix

Include the `*_peer` terms only when the v-extent is 2, e.g.:

```python
if cute.size(cta_layout_vmnk, mode=[0], loc=loc, ip=ip) == 2:
    mask |= peer_terms
```

mirroring the guard that `PipelineAsyncUmma.create` already applies.

## 评论 (1)

### yunweili3 · 2026-09-22

**Reproduced, and #3661 fixes it.**

The trigger is narrower than v-extent 1 alone: mode 0 must have extent 1 **and** a non-zero stride. `cute.make_layout`, `cute.tiled_divide` and `cute.make_ordered_layout` all give extent-1 modes stride 0, which makes the peer coordinate alias the original and the extra `|` inert — that is why `dense_gemm.py` never shows this, at any cluster shape.

Minimal repro, no GEMM:

```python
lay = cute.make_layout((1, 4, 1, 1), stride=(1, 1, 4, 4))
p = pipeline.PipelineTmaUmma.create(num_stages=2, tx_count=128, cta_layout_vmnk=lay, ...)
p.consumer_release(pipeline.make_pipeline_state(pipeline.PipelineUserType.Consumer, 2))
# launched with grid=(4,1,1), cluster=(4,1,1)
```

GB300 `sm_103a`, CUDA 13.0, DSL 4.8.0:

| `cta_layout_vmnk` | mask | before | after #3661 |
|---|---|---|---|
| `(1,4,1,1):(1,1,4,4)` | `0b11111` | **`cudaErrorLaunchFailure` (719)** | `cudaSuccess` |
| `(1,4,1,1):(0,1,0,0)` | `0b1111` | `cudaSuccess` | `cudaSuccess` |

Same kernel, only the stride differs — your analysis of the mechanism was right.

Your workaround only changes the mask if mode 0 carries a non-zero stride (with stride 0 it is a bit-for-bit no-op), so your `cta_layout_vmnk` must have one — exactly the case #3661 fixes.

