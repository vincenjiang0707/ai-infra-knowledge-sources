# [Issue #392] [nv_dev] SM120: MQA logits kernels fail test_attention self-consistency (fp8: nondeterministic/race) and accuracy (mxfp4 H=64 D=128)

source: https://github.com/deepseek-ai/DeepGEMM/issues/392
state: closed | updated: 2026-07-26T21:20:10Z
labels: 

## 正文

### Summary

On SM120 (`nv_dev` @ `f8e8fb5`, deep_gemm 2.6.1), the MQA logits kernels fail the repo's own `tests/test_attention.py::test_mqa_logits`, in two independent ways:

1. **FP8 format: nondeterministic output (race).** The test's self-consistency check — the same kernel on identical input across 20 repeat launches — fails with bitwise-different results:
   ```
   AssertionError: bitwise mismatch (mqa logits self-consistency): num_bytes=1048576,
   num_mismatch=56571, first_byte=250, elem=125, coord=(0, 125), byte_in_elem=0,
   x_byte=0, y_byte=134, x_val=0.0, y_val=1.046875
   ```
2. **MXFP4 format (`H=64, D=128`): accuracy failure.** `AssertionError: Diff: 0.6187` vs the 0.02 tolerance, at full throughput (~776 TFLOPS on this part) — wrong numbers, not a launch failure.

This kernel family has needed per-arch synchronization fixes before — SM90 (#229), SM100 (#285, and `96fbced` "Fix SM100 FP16 MQA synchronization") — and SM120 appears to be missing its equivalent.

### Environment

- GPU: NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition (SM120), driver 580.126.09
- CUDA 13.0, nvcc from `/usr/local/cuda/bin`, host compiler g++-10 (system g++ 9.4 lacks C++20 and fails JIT outright — separate, expected)
- torch 2.11.0+cu130, Python 3.12
- deep_gemm 2.6.1 built from `nv_dev` @ `f8e8fb5` via `setup.py bdist_wheel` (CC=gcc-10 CXX=g++-10)

### Repro

```bash
python - <<'EOF'
import sys
sys.path.insert(0, '<DeepGEMM>/tests')
import test_attention as ta
# fp8-only: the race repros here; the full sweep fails earlier on mxfp4 accuracy
orig = ta.sample_mqa_cases
ta.sample_mqa_cases = lambda tag, cases: [c for c in orig(tag, cases) if c[0] == 'fp8']
ta.test_mqa_logits()
EOF
```

Fails within minutes on the hardware above. The unfiltered `test_mqa_logits()` fails earlier, on the mxfp4 accuracy assert.

### Real-world impact

This is the root cause of DeepSeek-V4-Flash being unusable on SM120 workstations via vLLM (vllm-project/vllm#49896 has the full serving-side evidence chain): the indexer's prefill logits come out NaN-dominated (83% NaN on the first C4A layer, cascading to 100%), so sparse top-k selection is effectively random for prompts past ~2048 tokens — outputs are coherent below the `index_topk` threshold and unrelated hallucination above it. The NaN fractions differ across TP ranks on identical input, consistent with the race shown by the self-consistency failure. (A secondary effect — vLLM's `top_k_per_row_prefill` converting the NaN scores into out-of-bounds indices and crashing the engine — is being handled on the vLLM side: vllm-project/vllm#49897.)

Happy to run diagnostics or test candidate fixes on this hardware — SM120 workstation parts seem hard to come by in CI, and the JIT-based build makes candidate patches quick to iterate here.


## 评论 (2)

### linjiapro · 2026-07-26

Deeper isolation results that **sharpen (and partly correct) the original report** — same hardware, nv_dev @ `f8e8fb5` standalone:

1. **The fp8 kernel's valid-region output is correct and deterministic.** Probing `fp8_fp4_mqa_logits` directly (30 repeat launches per config, causal and CP-staggered `[ks,ke)` windows, shapes up to 4096×8192, H=64 D=128): **zero** mismatches and zero NaN within each row's `[ks_i, ke_i)` window, across every config tested.

2. **The self-consistency test failure is caused by nondeterministic *out-of-window* writes.** In compressed mode the kernel writes into output cells beyond each row's valid width — up to ~100M cell-mismatches summed over 30 reps in an S=4096 sweep, varying run to run, while valid cells stay bit-identical. In the uncompressed+`clean_logits` config, those same stray writes race the `smxx_clean_logits` pass over the invalid cells, which is exactly what `assert_bitwise_equal` catches (e.g. `x_val=0.0, y_val=1.046875`). So the fix target is the store path (bound stores to the row's window / don't emit fire-and-forget stores outside it), not the compute pipeline.

3. The mxfp4 H=64 D=128 accuracy failure (`Diff: 0.6187`) stands as reported.

4. For context on the serving-side NaN we originally attributed here (vllm-project/vllm#49896): further instrumentation shows the MQA kernel's *inputs* were already NaN (produced earlier in vLLM's DSv4 stack), so that symptom was not this kernel's fault. Separately, vLLM's vendored copy of this tree (a ~2.5.0 nv_dev snapshot) still contains the paged-kernel prefetch bug fixed on nv_dev by the "Use the scheduler's actual next task: zero-context atoms can be skipped" change in `sm120_fp8_paged_mqa_logits.cuh` — worth flagging to anyone vendoring.

Happy to iterate on a bounded-store fix for (2) here — the JIT build makes candidate patches quick to verify on SM120.


### linjiapro · 2026-07-26

Closing from our side: after deeper isolation (see the update above), none of the defects documented here block our SM120 serving use case — the fp8 kernel's valid-region output is correct and the stray out-of-window stores are invisible to window-respecting consumers, so we won't be driving a fix. The evidence stands as documented (the stray stores are why test_attention's self-consistency assert fails on SM120, and the mxfp4 H=64 D=128 accuracy failure is real for anyone on the FP4 indexer path) — please feel free to reopen if you want to track either.
