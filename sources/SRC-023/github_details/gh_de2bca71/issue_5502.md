# [Issue #5502] [Bug] gfx942 CK SiLU MoE drops positive swiglu_limit in BF16/block-FP8 paths

source: https://github.com/ROCm/aiter/issues/5502
state: open | updated: 2026-09-14T13:50:07Z
labels: 

## 正文

## Summary

The selected two-stage CK SiLU path accepts a positive `swiglu_limit` at
`fused_moe`, but silently computes the unclamped activation. This blocks
qualification of SGLang39247's gfx942 shared-expert opt-in. It is not a claim
that all AITER FP8 paths fail, or that the eligibility patch introduced the bug.

Expected GLM activation: `silu(min(gate, limit)) * clamp(up, -limit, limit)`.
This is not GPT-OSS's alpha/bias SwiGLU; changing the activation enum would not
preserve the model contract.

## Public reproducer

SGLang commit `31946c5bb7d3824745cb02b3376f8135f345314b` includes
[`test/manual/diagnose_glm_shared_clamp_gpu.py`](https://github.com/sgl-project/sglang/blob/31946c5bb7d3824745cb02b3376f8135f345314b/test/manual/diagnose_glm_shared_clamp_gpu.py).
Run `PYTHONPATH=python python test/manual/diagnose_glm_shared_clamp_gpu.py`.
It invokes the production runner with8 routed +1 shared expert,H512,I256,
BF16 or native FP8 weights, M1/8/16 and clamp0/10. The reference uses FP32
dequantized-weight expert math; positive-clamp inputs are scaled to exercise
the bound. It logs exact selected metadata, module SHA and Torch/HIP versions.
The script is diagnostic: inspect each JSON `passed` flag, not exit0.

Reproduced again on gfx942 using official
`lmsysorg/sglang-rocm@sha256:91ca32f56c662a8520c0ab8f24dffeb6a62ca6037dd91d880f1583a7381b03e9`
(v0.5.19-rocm720-mi30x-20260911,Torch2.9.1/ROCm7.2), with the pinned
SGLang source above. No full model is needed.

- BF16 unclamped M1/8/16 passes, NRMSE about0.0033.
- FP8 unclamped M8/16 passes, NRMSE about0.0452/0.0433; M8 graphs pass.
- Clamped BF16 all three M and FP8 M8/16 have NRMSE2.12-2.50 against the
  clamped reference, but match the unclamped reference (BF16 about0.0033,
  FP8 about0.040-0.044).
- Separate FP8 M1 unclamped failure: NRMSE0.77485 with split-K2. Its cause
  is unresolved and should not be conflated with the clamp omission.

## Source boundary and request

The selected `ck_moe_stage1` signature has no clamp parameter. The host
dispatcher forwards `swiglu_limit` to selected FlyDSL/Opus wrappers, not this
CK path. A read-only check of current AITER main
`08fd34e82` on September14 still finds that CK signature. We did not run that
new main as a GPU stack; newer MXFP4 metadata changes do not establish BF16/FP8
CK clamp support.

Is there a supported clamp-aware BF16/block-FP8 CK or FlyDSL dispatch for this
contract on gfx942? Otherwise the dispatcher should not silently select a
path that drops a positive bound. We have historical fixed-limit CK prototype
patches, but are not proposing a globally hard-coded limit10 or bundling a
backend rewrite into a shared-expert eligibility PR.

Prior investigation/results are public on
[SGLang39247](https://github.com/sgl-project/sglang/pull/39247#issuecomment-5651042964).
This diagnosis, reproducer work and report used Codex assistance.


## 评论 (1)

### AranKomat · 2026-09-14

The separate FP8 M1 failure now has a bounded diagnostic workaround. In a
matched two-arm replay of the attached695 diagnostic, setting only
`AITER_KSPLIT=-1` changes M1 dispatch from splitk2/the `_splitk` extension to
the non-split extension. Unclamped M1 NRMSE drops0.774850->0.038382, passing
the unchanged0.06 gate. Unclamped BF16/FP8 M1/8/16 all pass; M8 graph checks
also pass. Both processes exit0 with identical fused_moe.py source hashes.

The positive-clamp issue remains independent: all six clamp10 cases fail.
For FP8 M1 the override has NRMSE2.54108 against clamped math but0.04199
against unclamped math. The test is still exercising plain SiLU instead of
the requested clamp. Totals change5/12->6/12, not full correctness.

Environment: the same official MI30x91ca32f56c66 image, Torch2.9.1/ROCm7.2,
native FNUZ, nine experts including one shared slot, hidden512/intermediate256,
top-k3. Source hash181dfc53206adca3faec707f7f6e054fa6cbf56ba2d671a8d01266c4dc6f8ff1.
No model load, performance claim, tolerance relaxation or production-global
override. The dependent SGLang39247 remains draft until the exact native
clamp path and checkpoint execution are qualified. This narrows the blocker
but does not justify enabling the existing path for clamp-active models.

