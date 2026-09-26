# [Issue #5221] [Feature]: b12x_fused_moe (SM120): fixed-order finalise option and a docstring note on run-to-run non-repeatability

source: https://github.com/flashinfer-ai/flashinfer/issues/5221
state: open | updated: 2026-09-21T14:30:51Z
labels: needs-triage

## 正文

## Before submitting

- [x] I have searched existing issues and this request has not been filed yet. (Searched "b12x", "b12x_fused_moe", "cute dsl moe deterministic", "fused moe nondeterministic", "fused moe deterministic", "moe non-deterministic", "use_fused_finalize", "sm120 moe", "bf16x2 atomic", "scatter_add_v4_bf16x2". The related work is listed at the end; none of it reports this.)

## Problem

`b12x_fused_moe` on SM120 does not return the same bits when it is called twice with identical inputs, and the docstring does not say so. Three independent measurement runs on RTX PRO 6000 Blackwell Server Edition GPUs, on two driver versions across one week, produced differing outputs in every configuration tried, including top-k 1, within a process and between two processes. Reading the kernels in the installed wheel, the FC2 partial product of each 128-wide intermediate slice is rounded to bf16 and combined into the bf16 output with a relaxed `red` reduction, so the result depends on the order in which CTAs arrive. Other fused MoE entry points in the library already offer a fixed-order alternative (`cutlass_fused_moe(use_fused_finalize=False)` and the SM100 CuTe DSL `use_fused_finalize=False`); the SM120 path has none, and the unified `MoEFinalizeConfig.use_fused_finalize` flag is not read by the b12x runners.

**What this report does not claim.**

- It makes no claim about correctness. The only accuracy check in these measurements was an unquantised fp32 reference (relative max error 0.13 to 0.26, correlation 0.97 to 0.98), which is a sanity diagnostic and not a validated bound for a quantised kernel.
- It does not isolate the cause. The executed kernel was not instrumented; the static and dynamic assignment described below is inferred from the dispatch source and the JIT log, no intermediate tensors were captured, and no experiment separated the reduction-add stage from the rest of the pipeline. The source reading is offered as the most likely explanation, consistent with the top-k and token-count dependence, not as a demonstration.
- It does not implicate the SM120 dense split-K GEMM. `moe_static_kernel.py:125-126` and `_moe_dynamic/generic.py:98-99` import `Sm120B12xBlockScaledDenseGemmKernel` for descriptor helpers only; the probe never calls the dense GEMM's opt-in split-K path.
- It does not measure the rewritten static path on `main`; the statements about it are a reading of the source and of #4718's description.

### Environment

Three runs on the same GPU model with the same Python stack (run 3 repeated run 2's measurement on a different host with a corrected analyser and extra diagnostics):

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Date | 2026-09-07 | 2026-09-14 | 2026-09-14 |
| GPU | NVIDIA RTX PRO 6000 Blackwell Server Edition (sm 120) | same | same |
| Driver | 595.91.07 | 595.71.05 | 595.91.07 |
| CUDA (torch build) | 13.0 | 13.0 | 13.0 |
| torch | 2.14.0+cu130 | 2.14.0+cu130 | 2.14.0+cu130 |
| flashinfer-python | 0.6.18.post1 | 0.6.18.post1 | 0.6.18.post1 |
| nvidia-cutlass-dsl | not recorded by that run | 4.8.0.dev0 | 4.8.0.dev0 |
| triton | 3.8.0 | 3.8.0 | 3.8.0 |
| Python | 3.12.3 | 3.12.3 | 3.12.3 |
| torch deterministic algorithms | off (not recorded by that run; the measurement code never enables them) | off (recorded) | off (recorded) |

`python -m flashinfer.collect_env` was not run in any of the three environments; the versions above come from the per-report environment records and, for runs 2 and 3, a `pip freeze` (byte-identical between those two). The installed `flashinfer/fused_moe/cute_dsl/` sources in the run 2 wheel are byte-identical to the `v0.6.18.post1` tag (commit `8bc3b578`) for `b12x_moe.py`, `blackwell_sm12x/moe_static_kernel.py`, `blackwell_sm12x/_moe_dynamic/generic.py`, `blackwell_sm12x/moe_dispatch.py` and `blackwell_sm12x/moe_w4a16_fp4_helpers.py`. Line numbers below refer to that wheel unless marked "main".

### What was measured

Configuration: `b12x_fused_moe` with `quant_mode="nvfp4"`, NVFP4 weights with swizzled block scales converted to the MMA layout (`fp4_quantize(..., sf_vec_size=16, is_sf_swizzled_layout=True)` then `convert_sf_to_mma_layout`), bf16 activations, 8 experts, hidden size 2048, intermediate size 1024, `activation="silu"` (default), external top-k routing from `torch.topk(torch.softmax(logits, -1), k)`, `w1_alpha = w2_alpha = ones(8)`, `fc2_input_scale = [1.0]`, a fresh zero-initialised bf16 output buffer per call. Weights are built once from `torch.manual_seed(0)`; activations and logits once per token count. Token counts 16, 512 and 4096; top-k 1, 2, 4 and 8.

Protocol: each process calls the kernel once for a sanity check (which also absorbs JIT compilation), then four more times with the same tensors (one baseline plus three comparisons), reseeding torch before each call and synchronising after it. Two processes per run. Outputs are compared bit for bit as int16; for runs 2 and 3 the differing elements are also bucketed by bf16 ordinal distance (0, 1, 2, 3 or more).

Result, run 2 (driver 595.71.05): 12 configurations, 2 processes each, 8 evaluations per configuration, 72 comparisons in total. Every comparison differed. No output element was non-finite. Per configuration:

| Tokens | Top-k | Elements | Differing elements per comparison (min to max) | Mean share differing | Of the differing elements, share within 2 bf16 ULPs | Largest ordinal distance |
|---|---|---|---|---|---|---|
| 16 | 1 | 32,768 | 17,809 to 19,832 | 57.5% | 80.0% to 80.4% | 29,568 to 29,936 |
| 16 | 2 | 32,768 | 22,731 to 23,532 | 70.4% | 72.6% to 73.6% | 29,760 to 29,952 |
| 16 | 4 | 32,768 | 25,470 to 25,837 | 78.5% | 64.2% to 65.7% | 29,936 to 30,144 |
| 16 | 8 | 32,768 | 27,768 to 27,970 | 85.1% | 52.2% to 53.0% | 30,150 to 30,328 |
| 512 | 1 | 1,048,576 | 606,886 to 640,036 | 59.3% | 80.4% to 80.6% | 29,936 to 30,112 |
| 512 | 2 | 1,048,576 | 725,998 to 749,850 | 70.4% | 73.4% to 73.6% | 30,080 to 30,176 |
| 512 | 4 | 1,048,576 | 816,209 to 833,436 | 79.0% | 63.8% to 64.4% | 30,224 to 30,378 |
| 512 | 8 | 1,048,576 | 859,835 to 867,712 | 82.4% | 56.8% to 57.5% | 30,352 to 30,514 |
| 4096 | 1 | 8,388,608 | 4,602,654 to 5,023,376 | 57.4% | 80.2% to 80.7% | 30,080 to 30,288 |
| 4096 | 2 | 8,388,608 | 5,460,518 to 5,622,627 | 66.0% | 74.7% to 74.9% | 30,176 to 30,312 |
| 4096 | 4 | 8,388,608 | 5,966,488 to 6,010,690 | 71.4% | 69.0% to 69.2% | 30,248 to 30,400 |
| 4096 | 8 | 8,388,608 | 6,302,097 to 6,355,735 | 75.5% | 64.8% to 65.0% | 30,384 to 30,507 |

Reading the table: between 54% and 85% of the output elements differ in any single comparison (mean per configuration 57% to 85%); the share grows with top-k and depends much less on the token count (at fixed top-k it moves by at most ten points between 16 and 4096 tokens). Of the elements that differ, between 52% and 81% are within 1 or 2 bf16 ULPs of the baseline value. The remainder sit in an open "3 or more" bucket. The largest ordinal distance in every comparison (29,568 to 30,514) is far larger than any same-sign pair of values of magnitude below 1 can produce in bf16, so it records elements whose sign differs between two calls; it is not a relative error of that size, and the recorded buckets do not say how many elements changed sign or by how much in absolute terms.

Inputs were identical: the SHA-256 of all nine input tensors (`x`, `ids`, `weights`, `w1_weight`, `w1_weight_sf`, `w2_weight`, `w2_weight_sf`, `alpha`, `gs`) was recorded per process and matched between the two processes in all 12 configurations, and within a process the same tensor objects are passed to every call. The baseline output hash also differed between the two processes in all 12 configurations (first 12 hex digits of SHA-256 over the bf16 bits):

<details><summary>Baseline hash prefixes per process</summary>

| Tokens | Top-k | Process a | Process b |
|---|---|---|---|
| 16 | 1 | `72289b16bba0` | `973bc01c6e48` |
| 16 | 2 | `2e2227ca3e73` | `d3e7ba63efac` |
| 16 | 4 | `24075b834f41` | `c7ac7fc3ddbf` |
| 16 | 8 | `61bfc8bcddff` | `6fb105b47d2c` |
| 512 | 1 | `5c12edef74ab` | `dacb63f469a5` |
| 512 | 2 | `bbcca586213f` | `bbb9f2f33f15` |
| 512 | 4 | `91b733aaad87` | `c3b9184201b5` |
| 512 | 8 | `592cb4eaaff0` | `a33cac1ac807` |
| 4096 | 1 | `f3818a24d7df` | `cd7d79c0f06e` |
| 4096 | 2 | `1143c704aa34` | `5725b4e1f845` |
| 4096 | 4 | `1b0d938fdb68` | `7e76d3109d74` |
| 4096 | 8 | `aae3bbb01b22` | `dc7d7db2a2a4` |

</details>

The formal verdicts for run 2 are the in-process ones (same process, same tensors, 4 evaluations, 3 comparisons each, all differing, for both processes). The cross-process hashes above are raw observations rather than an analyser verdict, because the measurement tool hashed two run-dependent diagnostic values into its cross-process comparison key and therefore declined to issue one; they are listed so that the reader can see them.

Result, run 3 (driver 595.91.07, same day, different host, the analyser defect fixed and the same 12 configurations, 2 processes, 8 evaluations per configuration): every configuration differs both within a process and across the two processes (the tool now issues the cross-process verdict; the two processes' baseline hashes differ in all 12 configurations and the comparison keys match). Two of the diagnostics added for this run are quoted here, per comparison over finite element pairs: the number of elements whose sign differs between the two calls (8 to 15 of 32,768 at 16 tokens with top-k 1, rising with tokens and top-k to about 11,000 of 8,388,608 at 4096 tokens with top-k 8), and the largest absolute difference (0.0039 to 0.0215 at 16 tokens, 0.0156 to 0.0703 at 512 tokens, 0.031 to 0.117 at 4096 tokens; relative to the largest baseline magnitude in the tensor, 0.005 to 0.030). No element was non-finite. The mismatched-element shares and the bf16 ordinal buckets are in line with run 2.

Result, run 1 (driver 595.91.07): top-k 2, 4 and 8 at 16, 512 and 4096 tokens (top-k 1 was not in that probe version), 2 processes, 8 evaluations per configuration, 54 comparisons. Every comparison differed; between 66% and 85% of elements differed per comparison (22,640 to 27,798 of 32,768 at 16 tokens; 736,728 to 865,101 of 1,048,576 at 512 tokens; 5,552,147 to 6,349,866 of 8,388,608 at 4096 tokens). No ULP buckets were recorded in that run.

### A reading of the wheel source that appears to explain it

This is a reading of the Python source of the kernels, not a measurement of which kernel ran or where the differing bits arise.

Backend selection. `b12x_fused_moe` (`flashinfer/fused_moe/cute_dsl/b12x_moe.py:58-231`) calls `launch_sm120_moe` (`:206-208`). `select_sm120_moe_backend` (`blackwell_sm12x/moe_dispatch.py:1763-1782`) computes `routed_rows = num_tokens * num_topk` and picks the static kernel when that is at most 640 (`_STATIC_COMPACT_CUTOVER_PAIRS_DEFAULT`, `:87`), otherwise the dynamic kernel. For the shapes above, 16 tokens at every top-k (16 to 128 rows) and 512 tokens at top-k 1 (512 rows) fall to the static kernel; 512 tokens at top-k 2, 4 and 8 and all 4096-token cases fall to the dynamic kernel. The JIT log of run 2 is consistent with this: it compiled `static_m16_k2048_n1024_t{1,2,4,8}_r{16,32,64,128}`, `static_m512_k2048_n1024_t1_r512` and `dynamic_e8_k2048_n1024_t{1,2,4,8}`, and no micro kernel. With intermediate size 1024 the dynamic constructor (`blackwell_sm12x/moe_dynamic_kernel.py:15-20, 43-47`, called from `moe_dispatch.py:2167-2180` with `intermediate_size=n`) rejects the branch-paired gated variant, whose limit is 512, and builds `_moe_dynamic/generic.py`.

How FC2 partials are combined. Both kernels compute FC2 one intermediate slice at a time and add each slice's weighted partial product straight into the token-major bf16 output:

- Static kernel: the module docstring says "FC2: sweep all output tiles (reuse the cached intermediate slice)" and "Scatter: bf16x2 atomic add (directly into token-major output)" (`moe_static_kernel.py:28-29`) and "The compact static work loop assigns (m_tile, intermediate_slice, expert)" (`:46`). The FC1 slice fed to FC2 is 128 wide (`tile_k = sf_vec_size * 8`, `:369-373`), and the work grid has `ceil(intermediate / 128) = 8` slices per M tile (`moe_dispatch.py:909`). Consecutive work items go to different CTAs (`current_work_linear_idx = bidz`, `:1378`; advanced by `num_persistent_clusters`, `:2188`; `_compact_static_get_work_tile`, `:136-180`). The epilogue calls `scatter_add_v4_bf16x2(get_ptr_as_int64(scatter_output, tok * scatter_N + global_col), wv * sc_v0, ..., wv * sc_v7)` for each slice (`:2164-2176`). The output is zeroed inside the kernel in Phase 0 (`:1000-1015`), so the caller's zero buffer is not what the sum starts from.
- Generic dynamic kernel: `_TASK_SLICE_CHUNK = 1` (`_moe_dynamic/generic.py:105`); work items are `(expert, m_tile, slice_begin, slice_count)` (`:540-554`); the slice count is `ceil(n / tile_n) = 8` (`moe_dispatch.py:1851`); the per-slice FC2 loop is at `generic.py:2590-2591` and the same `scatter_add_v4_bf16x2` call at `:2552`; the output is zeroed in Phase 0 (`:1010-1012`).
- The helper (`blackwell_sm12x/moe_w4a16_fp4_helpers.py:2096-2127`) packs the eight fp32 partials with four `cvt.rn.satfinite.bf16x2.f32` and issues `red.global.add.noftz.v4.bf16x2` (`:2117-2122`); the scalar variant `scatter_add_bf16x2` (`:2052-2071`) issues `cvt.rn.satfinite.bf16x2.f32` followed by `red.relaxed.gpu.global.add.noftz.bf16x2` (`:2066`), and its docstring calls this a "BF16x2 atomic reduction add to global memory". In PTX a `red` with no `.sem` or `.scope` qualifier is the relaxed, gpu-scope form, so the two variants have the same memory-ordering semantics; the `.v4` form adds four packed pairs per instruction.

Consequence, as I read it: each output element receives `(intermediate / 128) * top_k` bf16 reduction adds, that is 8 at top-k 1 and 64 at top-k 8 for these shapes. Every add rounds the running bf16 sum, the adds come from different CTAs in arrival order, and bf16 addition is not associative, so the final bits depend on that order. This matches the shape of the data: differences appear at top-k 1, their share grows with top-k (more addends per element) far more than it changes with the token count (more elements, same addends per element), and at least half of the differences, four fifths at top-k 1, are one or two bf16 ULPs. It also means that routing each token to a single expert does not make the result repeatable, which is the point that the measurements add to what the source already suggests.

Docstring. The `b12x_fused_moe` docstring (`b12x_moe.py:84-158`) describes the function as running "routing, FC1, activation, FC2, and scatter through the selected backend" and lists the parameters and return value; it does not mention that the output is not repeatable run to run. The same is true of the file on `main` at `8c94f70f` (no occurrence of "determin", "repeatab" or "reproduc" in `b12x_moe.py`).

### Minimal script

Transcribed from the measurement probe; the exact file that ran is a longer script with reporting around it, and this shortened form has not itself been run standalone.

```python
# Requires an SM120/SM121 GPU, CUDA 13, flashinfer-python 0.6.18.post1, nvidia-cutlass-dsl.
import torch
from flashinfer.fp4_quantization import fp4_quantize
from flashinfer.cute_dsl.utils import convert_sf_to_mma_layout
from flashinfer.fused_moe.cute_dsl.b12x_moe import b12x_fused_moe

device = "cuda"
hidden, inter, experts, sf_vec = 2048, 1024, 8, 16
torch.manual_seed(0)
w1_bf16 = torch.randn(experts, 2 * inter, hidden, dtype=torch.bfloat16, device=device) / 10
w2_bf16 = torch.randn(experts, hidden, inter, dtype=torch.bfloat16, device=device) / 10
gs = torch.tensor([1.0], device=device, dtype=torch.float32)
w1_q, w1_sf = fp4_quantize(w1_bf16.view(experts * 2 * inter, hidden), global_scale=gs,
                           sf_vec_size=sf_vec, is_sf_swizzled_layout=True)
w1_weight = w1_q.view(experts, 2 * inter, hidden // 2)
w1_weight_sf = convert_sf_to_mma_layout(w1_sf, m=2 * inter, k=hidden, num_groups=experts, sf_vec_size=sf_vec)
w2_q, w2_sf = fp4_quantize(w2_bf16.view(experts * hidden, inter), global_scale=gs,
                           sf_vec_size=sf_vec, is_sf_swizzled_layout=True)
w2_weight = w2_q.view(experts, hidden, inter // 2)
w2_weight_sf = convert_sf_to_mma_layout(w2_sf, m=hidden, k=inter, num_groups=experts, sf_vec_size=sf_vec)
alpha = torch.ones(experts, device=device, dtype=torch.float32)

for tokens in (16, 512, 4096):
    x = torch.randn(tokens, hidden, dtype=torch.bfloat16, device=device) / 10
    logits = torch.randn(tokens, experts, device=device)
    for topk in (1, 2, 4, 8):
        weights, ids = torch.topk(torch.softmax(logits, -1), topk, dim=-1)
        ids = ids.to(torch.int32)
        weights = weights.to(torch.float32)

        def run():
            out_buf = torch.zeros(tokens, hidden, dtype=torch.bfloat16, device=device)
            return b12x_fused_moe(x, w1_weight, w1_weight_sf, w2_weight, w2_weight_sf, ids, weights,
                                  experts, topk, w1_alpha=alpha, w2_alpha=alpha,
                                  fc2_input_scale=gs, quant_mode="nvfp4", output=out_buf)

        run()  # first call, absorbs JIT compilation
        torch.manual_seed(0)
        first = run().clone()
        torch.cuda.synchronize()
        for k in range(3):
            torch.manual_seed(0)
            out = run().clone()
            torch.cuda.synchronize()
            differing = (first.view(torch.int16) != out.view(torch.int16)).sum().item()
            print(f"tokens={tokens} topk={topk} comparison={k + 1}: {differing}/{out.numel()} elements differ")
```

## Requested outcome

1. A fixed-order finalise for the SM120 b12x path, opt-in if it costs performance, so that two calls with identical inputs return identical bits. The library already exposes this contract elsewhere: `cutlass_fused_moe(use_fused_finalize=False)` (`flashinfer/fused_moe/core.py:1362-1366` in the wheel, `:1442-1446` on `main`: "The fused epilogue reduces expert outputs via non-associative atomics, so results are not deterministic run-to-run. Set to False to use the non-fused, deterministic finalize path."), and the SM100 CuTe DSL NVFP4 MoE's `use_fused_finalize=False`, which writes each `(token, top-k slot)` route to its own row and reduces in fixed order with `moe_unpermute` (`flashinfer/fused_moe/cute_dsl/fused_moe.py:280-281, 510-511` on `main`; #3976). An fp32 workspace with a stream-ordered fixed-order reduction, or the SM100 expanded-row approach, would both satisfy the request; the outcome that matters is bit-identical repeats.

   On `main` (`8c94f70f`, 2026-09-14) the static kernel already looks like this after #4718: its docstring now reads "Scatter: route-major BF16 store (one private contribution per route)" and "Finalize: token-major FP32 sum (top-k contributions, one BF16 output)" (`moe_static_kernel.py:34-35`, main), the per-slice-pair partial is written to a private slot with `store_weighted_bf16x8_route` ("without a global REDG", `:146-181`, called at `:2477-2493`), and a separate `finalize_kernel` (`:2730-2792`) sums the top-k routes and retained groups in a fixed nested loop in fp32 before one bf16 store. #4718's description reports "Static candidate repeats: Bitwise equal". The dynamic kernels on `main` are byte-identical to the wheel and still combine with `red.global.add.noftz.v4.bf16x2` (`_moe_dynamic/generic.py:2552` via `moe_w4a16_fp4_helpers.py:2122`; `_moe_dynamic/gated.py:196, 234, 275`), as does the micro kernel (`moe_micro_kernel.py:2216` via `moe_w4a16_fp4_helpers.py:2066`). With the NVFP4 static cutover raised to 1024 routed rows on `main` (`moe_dispatch.py:95, 276-309`), the shapes above at 512 tokens with top-k 4 and 8 and all 4096-token shapes would still take the atomic path. So the concrete questions are: is the fixed-order behaviour of the new static path an intended guarantee, will the dynamic path follow, and would an explicit flag (the existing `use_fused_finalize` name, which `MoEFinalizeConfig` already carries and b12x currently ignores, `flashinfer/fused_moe/api.py:398-401`, `runners.py:5935-5936`) be acceptable so callers can select it and tests can assert it?

2. A sentence in the `b12x_fused_moe` and `B12xMoEWrapper` docstrings stating that the default path reduces expert partials with bf16 atomics and is therefore not bit-for-bit repeatable across calls, in the same words `cutlass_fused_moe` uses today, and, if the static path on `main` is meant to be repeatable, a statement of which backends the guarantee covers. The unified fuzz contract still lists both b12x runners as "intentionally absent until repeated-run bitwise calibration is completed on ... SM120/SM121" (`tests/moe/test_unified_moe_fuzz.py:287-289`, main); the measurements above may serve as that calibration for the 0.6.18.post1 kernels.

## Target hardware

- SM120 (RTX PRO 6000, RTX 50-series)

## Inference engine

- PyTorch native
- Custom / other

## Affected model or model family

Not model-driven. Shapes are synthetic (8 experts, hidden 2048, intermediate 1024).

## Workload and configuration

- Data type and quantization: NVFP4 weights (`quant_mode="nvfp4"`, `sf_vec_size=16`, swizzled block scales converted to the MMA layout), bf16 activations, bf16 output; `w1_alpha = w2_alpha = 1.0` per expert, `fc2_input_scale = 1.0`.
- Batch size or request concurrency: single process, single stream, no CUDA graph; two processes per run for cross-process comparison.
- Sequence lengths or token counts: 16, 512 and 4096 tokens.
- Parallelism: none (TP 1, no EP; `num_local_experts` left at the default).
- Entry point: direct calls to `flashinfer.fused_moe.cute_dsl.b12x_moe.b12x_fused_moe` from PyTorch, no engine. SM121 was not measured.
- Relevant shapes: 8 experts, hidden size 2048, intermediate size 1024, top-k 1, 2, 4 and 8, `activation="silu"`.
- Environment: see the table above; `python -m flashinfer.collect_env` was not run.

## Current workaround

Treat `b12x_fused_moe` output as non-repeatable and avoid it where bit-exact replay is required. There is no fixed-order option to switch to on SM120 in 0.6.18.post1; the unified API's `MoEFinalizeConfig(use_fused_finalize=False)` is not read by the b12x runners, and `do_finalize=False` is rejected by them (`runners.py:5935-5936`, main).

## Impact

- Testing, maintainability, or documentation
- API usability or integration complexity

## Acceptance criteria

- With the fixed-order option selected, two calls of `b12x_fused_moe` with identical inputs at 16, 512 and 4096 tokens and top-k 1, 2, 4 and 8 (8 experts, hidden 2048, intermediate 1024, NVFP4, bf16 activations) return bit-identical bf16 outputs, in one process and across two processes, on both the static and the dynamic backend.
- The `b12x_fused_moe` and `B12xMoEWrapper` docstrings state which finalise paths are repeatable and which are not.

## Related work, dependencies, or suggested scope

- #3598 (merged 2026-07-01) added `use_fused_finalize` to `cutlass_fused_moe` for exactly this reason: "This reduction uses atomics which can introduce run-run variance."
- #3976 (merged 2026-07-20) added the deterministic two-stage finalise to the SM100 CuTe DSL NVFP4 MoE, mirroring the `cutlass_fused_moe` contract.
- #4325 (tracking issue, closed 2026-08-18) and #4385 (merged 2026-08-18) introduced `MoEFinalizeConfig` with `use_fused_finalize`; the docstring says backends that do not support it ignore the flag (`api.py:398-401`).
- #4718 (merged to `main` 2026-08-31; not contained in the `v0.6.18.post1` tag, whose static kernel is the earlier file) rewrote the SM120 static kernel to a route-major store plus a stream-ordered fp32 finalise and reports bitwise-equal repeats for the static path.
- #4285 (merged 2026-08-03) is the sync that introduced the vectorised `scatter_add_v4_bf16x2` epilogue into the static kernel shipped in 0.6.18.post1.
- #5168 (open) changes the static kernel and dispatch further.
- `tests/moe/test_unified_moe_fuzz.py:275-289` (main) records the per-backend determinism contract ("cute_dsl": False, "atomic scatter-add finalize -> non-bit-exact by design") and leaves the b12x runners uncalibrated; `docs/design_docs/flashinfer_moe_api.md:1002-1004` describes the same contract.



## 评论 (2)

### SamMausberg · 2026-09-21

!claim

### flashinfer-bot · 2026-09-21

Issue assigned to @SamMausberg.
