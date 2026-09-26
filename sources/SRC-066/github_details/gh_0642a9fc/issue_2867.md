# [Issue #2867] [FEA] Block-Scaled Data Format Support for SM120 in CuTe DSL

source: https://github.com/NVIDIA/cutlass/issues/2867
state: open | updated: 2026-09-24T05:51:04Z
labels: feature request, ? - Needs Triage, inactive-30d, inactive-90d, CuTe DSL

## 正文

### Which component requires the feature?

CuTe DSL

### Feature Request

**Is your feature request related to a problem? Please describe.**
I wish I could use CuTe DSL (Python) to implement block-scaled GEMM operations on SM120 (Blackwell) architecture. Currently, all CuTe DSL Python examples for block-scaled formats (MXFP4, MXFP6, MXFP8) only support SM100.

**Describe the solution you'd like**
 Add CuTe DSL Python support for SM120 block-scaled operations:

  1. Python helper functions for SM120 (similar to existing SM100 helpers in blackwell_helpers.py)
  2. SM120 MMA operation wrappers for block-scaled formats (MmaMXF4Op, MmaMXF8Op, etc.)
  3. Example scripts for dense and grouped block-scaled GEMM on SM120
  4. Support for MXFP4 (Float4E2M1FN), MXFP6, and MXFP8 formats with corresponding scale factor types




## 评论 (12)

### qqq-tao · 2025-12-11

I have the same qustion as well. So far, I have implemented a function using inline ptx to use f8 mma instructions on sm_120.

### qqq-tao · 2025-12-11

Here's my implementation for mma.sync.aligned.kind::f8f6f4.m16n8k32.row.col.f32.e4m3.e4m3.f32, just for referrence.


```
@dsl_user_op
def mma_f8e4m3_16x8x32(
    a0: Uint32, a1: Uint32, a2: Uint32, a3: Uint32,
    b0: Uint32, b1: Uint32,
    c0: Float32, c1: Float32, c2: Float32, c3: Float32,
    *,
    loc=None, ip=None
) -> Tuple[Float32, Float32, Float32, Float32]:
    """
    FP8 MMA: D = A × B + C
    
    PTX: mma.sync.aligned.kind::f8f6f4.m16n8k32.row.col.f32.e4m3.e4m3.f32
    
    A fragment: 4 × u32 (每个 u32 = 4 个 FP8)
    B fragment: 2 × u32 (每个 u32 = 4 个 FP8)
    C/D: 4 × f32
    """
    inputs = [
        a0.ir_value(loc=loc, ip=ip), a1.ir_value(loc=loc, ip=ip),
        a2.ir_value(loc=loc, ip=ip), a3.ir_value(loc=loc, ip=ip),
        b0.ir_value(loc=loc, ip=ip), b1.ir_value(loc=loc, ip=ip),
        c0.ir_value(loc=loc, ip=ip), c1.ir_value(loc=loc, ip=ip),
        c2.ir_value(loc=loc, ip=ip), c3.ir_value(loc=loc, ip=ip),
    ]
    
    result_type = llvm.StructType.get_literal([T.f32(), T.f32(), T.f32(), T.f32()])
    
    result = llvm.inline_asm(
        result_type,
        inputs,
        "mma.sync.aligned.kind::f8f6f4.m16n8k32.row.col.f32.e4m3.e4m3.f32 "
        "{$0, $1, $2, $3}, {$4, $5, $6, $7}, {$8, $9}, {$10, $11, $12, $13};",
        "=f,=f,=f,=f,r,r,r,r,r,r,f,f,f,f",
    )
    
    d0 = Float32(llvm.extractvalue(T.f32(), result, [0], loc=loc, ip=ip))
    d1 = Float32(llvm.extractvalue(T.f32(), result, [1], loc=loc, ip=ip))
    d2 = Float32(llvm.extractvalue(T.f32(), result, [2], loc=loc, ip=ip))
    d3 = Float32(llvm.extractvalue(T.f32(), result, [3], loc=loc, ip=ip))
    
    return (d0, d1, d2, d3)
```

### DD-DuDa · 2025-12-11

Wow, thanks, Willie. I will try to use this currently.

### github-actions[bot] · 2026-01-10

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### kiwi3shark · 2026-03-05

Any update on this feature? Why you guys don't care about SM120 at all :QAQ

### mricharz · 2026-03-14

Adding our voice here as well. We're blocked by the same root cause as #2800.

**Setup:** RTX PRO 6000 (SM120), Qwen3.5-35B-A3B-NVFP4, vLLM + FlashInfer 0.6.6.

FlashInfer's CuTe DSL MoE path (`FLASHINFER_CUTEDSL`) is in the backend candidate list but gets deprioritized in favor of `FLASHINFER_CUTLASS`, which then fails at runtime on SM120 with TMA grouped GEMM initialization errors. The CuTe DSL path would be our best alternative, if it supported SM120 block-scaled operations.

The "inactive-30d" label on this issue is concerning. SM120 is shipping hardware (RTX 5090, RTX PRO 6000) with millions of units in developer hands. FP4 was the headline Blackwell feature. Not having CUTLASS support for it on workstation GPUs undermines the entire value proposition.

We've documented our full debugging journey (monkey-patching vLLM capability checks, FlashInfer JIT OOM fixes, autotuner tactic failures) and would be happy to help test any SM120 patches.

### dibakarbarua · 2026-03-19

+1 on SM120 support

### windswand · 2026-04-02

Same. We have a 4x RTX 6000 PRO server for our developers and we can't use the advertised Blackwell FP4 acceleration on our sm120 GPUs. 

Can Nvidia give us an update on this? We feel like we've been left with unsupported hardware at this point, except that it's supposedly top-of-the-line consumer Blackwell.

### BlueArchive-Sensei · 2026-04-10

Thanks for all of your sharing. Let us take a look and discuss this issue.

### dicksondickson · 2026-04-12

Keeping this alive. Nvidia please fix this.

### github-actions[bot] · 2026-08-24

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

### harshithkantamneni · 2026-09-24

Dense SM120 block-scaled examples are on main now: NVFP4, MXFP4 and MXFP8 in #3272 (`cute/blackwell_geforce/kernel/blockscaled_gemm/`), and a `cute_ext` pingpong version in 4.8. The grouped part of this request (item 3) is still open. The grouped block-scaled DSL kernels target SM100, SM103 (#3124) and Rubin, and in CUTLASS, SM120 grouped block-scaled exists only in C++ (for example 79d).

I'd like to write it: a persistent grouped block-scaled GEMM for SM120, NVFP4 and MXFP4 first, reusing the #3272 mainloop with the existing grouped tile scheduler and per-group tensormap updates, the way #3124 did for SM103. It would come with correctness tests against a torch reference, following `sm_103/test_grouped_blockscaled_gemm.py`, and RTX 5090 timings next to 79d. For background, I have an open vLLM PR with a Triton reference NVFP4 GEMM (vllm-project/vllm#38338), tested on an RTX 5090 and a B200.

@hwu36 @Junkai-Wu before I start: is this already in progress on your side? If so, I'll leave it. If not, would you take a PR like this, and which shape do you prefer?
- classic `cute` or `cute_ext`
- the pointer-array interface like 79d, or the 2Dx3D `offs` interface of `moe/torch_scaled_grouped_mm.py`
- a new `cute/blackwell_geforce/kernel/blockscaled_grouped_gemm/` directory, matching the SM100, SM103 and Rubin layout

