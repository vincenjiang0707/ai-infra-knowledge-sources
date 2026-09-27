# [Issue #700] Low-latency combine returns one corrupted token row on B200 (~3% of invocations at max tokens/rank)

source: https://github.com/deepseek-ai/DeepEP/issues/700
state: closed | updated: 2026-08-06T02:33:27Z
labels: 

## 正文

On B200 (sm100), `low_latency_combine` intermittently returns one corrupted token row. no error, no NaN, plausible magnitudes. H100 and H200 are ok.

## Environment

- DeepEP `fa8a9b16`, legacy `Buffer` low-latency path (`csrc/kernels/legacy/internode_ll.cu`). Current `main` is byte-identical in this file, so it is not a stale-pin issue.
- 8x B200, single node, EP8, `low_latency_mode=True`, `allow_nvlink_for_low_latency_mode=True`.
- hidden 7168, topk 8, 256 experts, `num_max_dispatch_tokens_per_rank=256`.
- CUDA 13.0, torch 2.10.0, NCCL 2.30.4, NVSHMEM 3.3.9.
- BF16 and FP8 dispatch both affected.

## Symptom

One dispatch + combine round trip at 256 tokens/rank, output compared against a host-side reference of the same reduction:

- **Rate: 1.5-3.3% per rank per invocation** (8-11 events per 336 rank-samples, several runs, four different nodes).
- Only at 256 tokens/rank. Lower rungs (1..128) are clean over ~160 samples each.
- Per event: **exactly one token row of 256** is wrong. Row norm matches the reference to 4 significant figures, median element ratio is 1.0000, and 16-40% of the 7168 elements deviate.
- Absolute errors 0.08-0.22 on elements whose expected values are O(1). 3-6x the largest error a correct BF16 accumulation can produce (topk stores at one ulp each).

A *dropped* contribution would cut the row norm by ~12% and perturb every element. Preserved norm plus a dense-but-partial element set is what you get if **one of the topk=8 expert contributions is read from the wrong slot**.

Example (BF16, one event):

```
row 40 of 256:  bad_elems=2254/7168  got_norm=55.6114  want_norm=55.5639
worst element:  want=+1.107603  got=+0.886719  abs_err=0.220884
```

## Ruled out by experiment

- **Buffer capacity.** Raising `num_max_dispatch_tokens_per_rank` to 511 while keeping the workload at 256 tokens/rank (buffer ~50% full) still corrupts. Note 512 is not testable without also raising `NVSHMEM_QP_DEPTH`, since `nvshmem_qp_depth >= (num_max_dispatch_tokens_per_rank + 1) * 2` asserts at construction.
- **Pipelining / repeated calls.** Isolated single round trips corrupt; no preceding calls or other token counts are needed.
- **Reference tolerance.** Expected values are O(1), far above any near-zero cancellation regime, and errors exceed the BF16 accumulation bound several-fold.
- **Input mutation.** Dispatch inputs are bit-identical before and after.
- **A missing system-scope acquire on the reader side.** In the combine receiving phase, `rdma_recv_flag` is waited on by a single thread with `ld_acquire_sys_global`, while the TMA and reduction warps reach the payload through the device-scope `cg::this_grid().sync()` at `internode_ll.cu:976`; there is no `__threadfence_system` in the file. Adding one immediately after that grid sync and rebuilding changes nothing (8 failures / 336 samples, unchanged), so this appears not to be the mechanism.

## Ask

Is a wrong-slot read plausible in the combine receive path on sm100? for example in the `kNumStages` mbarrier/TMA pipeline, or in the `rdma_recv_x` slot addressing at `(topk_idx * num_max_dispatch_tokens_per_rank + token_idx)`? Happy to run further instrumentation on the reproducing hardware, including a device-side event ring, if that would help narrow it.


## 评论 (2)

### MARD1NO · 2026-08-03

Do you apply this fix?: https://github.com/deepseek-ai/DeepEP/pull/642

### Oseltamivir · 2026-08-06

Yes, it's working after pinning to a new version. Thanks @MARD1NO 
