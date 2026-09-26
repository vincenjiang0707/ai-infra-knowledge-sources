# [Issue #2307] FA4 SM120 support?

source: https://github.com/Dao-AILab/flash-attention/issues/2307
state: open | updated: 2026-08-19T19:04:19Z
labels: 

## 正文

Is there planned support for other Blackwell GPUs? Right now it only is meant to work with B200 and GB200.
I tested it on the RTX 6000 PRO WS (Blackwell) but to no avail. The compute 12.0 was showing as unsupported.

## 评论 (6)

### Jumaron · 2026-03-06

Most likley not, since tcgen05 is used to archive a lot of the speed-ups. If i'am not wrong, those are only included in the SM100.
We are sadly out of luck :/

### geraldstanje · 2026-03-06

does the following not help for FA4? https://github.com/Dao-AILab/flash-attention/pull/2268

### Jumaron · 2026-03-06

"SM120 uses SM80-era mma.sync.aligned.m16n8k16 MMA instructions (no tcgen05/WGMMA/TMEM). T"
As you can see SM120 will never work with FA-4, it could be made compatible with older Flash Attention Versions tho, if this PR adds the missing features.

### bmdhodl · 2026-03-17

**CORRECTION**: The Triton fix referenced below (triton-lang/triton#9734) was reverted — `sm_120a` IS a valid arch that enables instructions like `tensormap.replace`. The claim that sm_120a doesn't exist was wrong. See https://github.com/triton-lang/triton/pull/9755.

The MMAv2 observation still holds — sm_120 uses `mma.sync.aligned.m16n8k16` for matmul, not WGMMA or tcgen05. And PyTorch SDPA does achieve ~160 TFLOPS on the 5070 Ti. But the arch string claim was incorrect.

### Suppressor72 · 2026-08-03

## FA4 SM120 status: capability gate fixed, but paged KV + num_splits block vLLM serving

I've been working on enabling FA4 (CuTe DSL) on SM120 (RTX 5090) for vLLM serving. The CuTe kernel exists (`flash_fwd_sm120.py`) but three blockers prevent it from being usable in production serving.

### What works

The SM120 CuTe kernel exists and JIT-compiles fine. The capability gate in vLLM's fork (`_is_fa4_supported`) checked `family(90/100/110)` but not `family(120)` — that's a one-line fix (vllm-project/vllm#50862). After fixing it, `is_fa_version_supported(4)` returns `True` on SM120 and `get_flash_attn_version()` selects FA4 as default.

### Blocker 1: Paged KV not supported

```
AssertionError: Paged KV not supported on SM 12.0 in this PR
```

The CuTe interface (`interface.py`) explicitly asserts `page_table is None` for SM120. vLLM uses paged KV cache for all production serving — without it, FA4 can't be used with vLLM's memory management.

I see vllm-project/flash-attention#170 (WIP/RFC for SM120 D256 paged-decode) is exploring this space. Is there a roadmap for generic SM120 paged KV support?

### Blocker 2: num_splits hardcoded to 1

```python
# interface.py
if arch // 10 == 12:
    assert num_splits == 1, "SM120 forward only supports num_splits=1"
```

vLLM's flash_attn backend passes `num_splits=0` (default, resolved by heuristic) for large contexts. The SM120 kernel rejects any value other than 1, which limits long-context throughput since split-K can't parallelize across SMs.

This is manageable as a workaround (force `max_num_splits=1` in vLLM for SM120), but it means FA4 on SM120 can't use split-K for long-KV decode.

### Blocker 3: FP8 KV cache not supported

The SM120 `can_implement()` only accepts `Float16/BFloat16`:
```python
if dtype not in [cutlass.Float16, cutlass.BFloat16]:
    return False
```

SM120 has native FP8 tensor cores. Is FP8 KV support planned for the SM120 CuTe kernel?

### Why this matters

vLLM on SM120 (RTX 5090) currently falls back to FlashInfer's native decode path, which caps at `UNIFORM_SINGLE_TOKEN_DECODE` — forcing PIECEWISE CUDA graphs under spec-decode (MTP). This costs ~15% decode throughput. FA4 with FULL CUDA graphs + paged KV would close that gap.

**Hardware:** Dual RTX 5090 (SM120, 32GB), vLLM nightly, ThinkingCap-Qwen3.6-27B-FP8, 256k context, MTP=3. Happy to test any SM120 paged KV prototype.

### daire-byrne · 2026-08-19

Perhaps #2634 will help? 
