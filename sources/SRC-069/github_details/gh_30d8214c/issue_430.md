# [Issue #430] [nv_dev][SM120] k_grouped_fp8_gemm_nt_contiguous returns non-deterministic wrong results — sm120 kernel is missing the tensormap drain fixed for SM90 in #343

source: https://github.com/deepseek-ai/DeepGEMM/issues/430
state: open | updated: 2026-09-16T08:56:29Z
labels: 

## 正文

The SM120 1D1D kernel was copied from `sm90_fp8_gemm_1d1d.cuh` (merged into nv_dev on 6/24 in #324), **twelve days before #343** fixed the in-flight tensormap race on the SM90 side. Since the copy lives at a different file path (`sm120_fp8_fp4_gemm_1d1d.cuh`), the #343 fix cannot propagate to it through merges — the SM120 group-switch still publishes GMEM tensormaps without draining in-flight TMA loads.

Notably, the regression shape that #343 added to `test_k_grouped_gemm_contiguous` (8 groups, m=768, n=2048, k≈128/group) does its job on SM120: it fails consistently on our RTX 5090 D, which is how we found this.

## Environment

RTX 5090 D (SM120), CUDA 13.0, PyTorch 2.11.0+cu130. Built from the nv_dev tarball @ `2642b32` with pinned submodules (CUTLASS @ f3fde58, fmt @553ec11).

## Repro

Run `test_k_grouped_gemm_contiguous` (tests/test_fp8_fp4.py). The first shape fails with diff (the test's relative-error metric) of 0.0015–0.006, threshold 0.001. Observed trigger rate: **13/14 runs** (10/10 with warm JIT cache, 3/3 with cold cache, plus 1 fail / 1 pass in early manual runs — the single pass itself matches race behavior). The same shape passes via the TN (MN-major) path — isolated to the NT kernel.

## It is a race

Identical inputs (fixed seeds, data regenerated each run), 3 fresh runs:

```
diff = 0.006319 / 0.005205 / 0.003889
```

Errors spread across all 8 groups (max abs error ~122 on k=128 groups) — every group switch is a hazard.

## Root cause

`sm120_fp8_fp4_gemm_1d1d.cuh`, KGroupedContiguous group-switch (~L236-282):

```cpp
ptx::tensor_map_replace_global_addr_in_smem(smem_tm_a, a_base + a_offset);
ptx::tensor_map_replace_global_addr_in_smem(smem_tm_b, b_base + b_offset);
...
// ← the #343 drain (commit_group + wait_group) is missing here
*gmem_tm_a = *smem_tm_a;          // published while TMA loads may still be in flight
*gmem_tm_b = *smem_tm_b;
ptx::tensor_map_release_gpu();
ptx::tensor_map_acquire_gpu(gmem_tm_a);
ptx::tensor_map_acquire_gpu(gmem_tm_b);
```

Same publish-without-drain pattern that #365 root-caused on SM90; the fixed SM90 path has `cute::tma_desc_commit_group() + cute::tma_desc_wait_group()` before the GMEM publish (sm90_fp8_gemm_1d1d.cuh:202-207).

## Fix validated on SM120

Porting the #343 drain (same 4 lines, inserted before the GMEM publish):

```cpp
cute::tma_desc_commit_group();
cute::tma_desc_wait_group();
__syncwarp(1u << lane_idx);
```

- diff drops to **0.000105, bit-identical across runs** (vs 0.006 non-deterministic before)
- full k_grouped + m_grouped suites pass (56/56 configs); 100× soak clean
- Perf A/B (same seeds/data): sentinel shape 87.0 → 87.8 µs (**+0.9%**, worst case for group-switch density); typical EP shape 3106 → 3114 µs (**+0.26%**) — the same trade-off SM90 accepted in #343

## Scope / timing

`main` is not affected (no SM120 support there yet). But when nv_dev next syncs to main, this would ship with the first official SM120 support. Recent SM120 issues (#392, #405, #417, #425) were all found on real hardware — there appears to be no SM120 CI runner, so release testing is unlikely to catch this.

## Note on the bf16 kernel

`sm120_bf16_gemm.cuh` has the same un-drained group-switch pattern. We could not make it fail on our hardware (full suite + 50 targeted stress runs pass), but per the commit-group ordering analysis in #365 it is the same UB class — happy to include a defensive fix for it too if maintainers prefer.

---

Repro script and raw logs: https://gist.github.com/aganhui/3b374ffb3d6d13b52d5688780fafac28

PR incoming (base nv_dev). Happy to run any additional validation on this 5090 D (soak, sanitizer, benchmarks) if useful, and to adjust to whatever structure maintainers prefer — including a 3-phase restructure à la #375.


## 评论 (1)

### lucifer1004 · 2026-09-16

Confirmed — the SM120 1D1D copy predated the #343 drain, and because it lived at a different path the fix could never propagate by merge.

In #447 the SM120 device layer was rewritten for the main-API migration, and the rewritten k-grouped path carries the #343-class drain: on a group switch the TMA leader rebuilds the descriptors in SMEM, then `tma_desc_commit_group()` + `tma_desc_wait_group()` before publishing to GMEM (`impls/sm120_fp8_fp4_gemm_1d1d.cuh`), followed by `tensor_map_release_gpu`/`acquire`; the BF16 sibling does the same.

Regression coverage is the #343 shape class exactly: 8 groups, m=768, n=2048, k≈128/group, iterated with bitwise (rtol=0/atol=0) cross-run determinism, plus a descriptor-reuse/aliasing variant — `test_sm120_k_grouped_bf16_descriptor_reuse` and the fp8 `test_k_grouped_gemm_contiguous` shape matrix, all arch-12 enabled. The SM120 suite also passes compute-sanitizer racecheck with zero hazards.

