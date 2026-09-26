# [Issue #5325] [Feature]: Expand MNNVL CuTe DSL AllReduce profiles beyond GB300 H=8192 TP8/TP16

source: https://github.com/flashinfer-ai/flashinfer/issues/5325
state: open | updated: 2026-09-19T04:12:11Z
labels: needs-triage

## 正文

## Before submitting

- [x] I have searched existing issues and this request has not been filed yet.

## Problem

The MNNVL CuTe DSL all-reduce fusion backend currently ships built-in static profiles only for GB300, BF16, `H=8192`, `Top-K=10`, and TP8/TP16. `MNNVLCuteDSLConfig.resolve()` keys profiles by TP size, hidden size, Top-K, and dtype, and raises `No MNNVL CuTe DSL profile supports this static shape` for other combinations.

This makes an otherwise promising backend difficult to use outside the initial Qwen3.8 2.4T-style geometry. In particular, inference engines cannot select it broadly for other tensor-parallel models or hardware without carrying custom profiles and doing their own correctness/performance tuning.

The backend's LL/BT/HT protocols cover decode through prefill and the initial implementation reports strong gains over the existing composed MNNVL and NCCL paths. Broadening the validated profile matrix would make those protocols usable by more models and would unblock a general vLLM integration instead of a model-specific one.

## Requested outcome

Expand the validated and tuned MNNVL CuTe DSL profile matrix beyond the initial GB300 `H=8192`, `Top-K=10`, TP8/TP16 configuration.

Concretely, it would be useful to have:

- Profiles for representative hidden sizes and model families beyond the initial geometry.
- TP2/TP4 coverage where the protocols and topology support it, in addition to TP8/TP16.
- Validation and tuning on SM100 and SM103, plus a clear path for architecture-specific profiles on future MNNVL systems.
- A documented/public benchmark workflow for sweeping `M`, selecting LL/BT/HT crossover points, and producing checked-in presets.
- A safe dispatch/fallback story so inference engines can probe support without hard-coding one model configuration.

## Target hardware

- SM100 (B200, GB200)
- SM103 (B300, GB300)
- Future architecture

## Inference engine

- vLLM
- PyTorch native

## Affected model or model family

Tensor-parallel models using MNNVL all-reduce fusion. The initial checked-in profiles correspond to Qwen3.8 2.4T-style `H=8192`, TP8/TP16 geometry; the request is to support additional public model shapes rather than another single-model specialization.

## Workload and configuration

- Data type and quantization: BF16 all-reduce input; fused residual add + RMSNorm, optionally preceded by MoE finalize/shared-expert add. Future quantized output fusion can be evaluated separately.
- Batch size or request concurrency: decode through prefill; sweep the full supported `M` range so LL, BT, and HT crossover points are tuned per profile.
- Sequence lengths or token counts: all; the relevant dispatch dimension is `M`.
- Parallelism: TP2/TP4/TP8/TP16 over NVLink/MNNVL, subject to topology support.
- Relevant shapes: multiple hidden sizes and Top-K values beyond `H=8192`, `Top-K=10`.
- Environment: Blackwell SM100/SM103 first; future-architecture profiles when public hardware validation is available.

## Current workaround

Use the existing TRT-LLM MNNVL, NCCL, or framework-specific all-reduce backend, or maintain a private `MNNVLCuteDSLConfig` and retune all LL/BT/HT presets and route boundaries. The first options leave performance on the table, while the latter is not a maintainable integration strategy for frameworks.

## Impact

- Missing model or hardware support
- Throughput
- Latency
- API usability or integration complexity
- Testing, maintainability, or documentation

## Acceptance criteria

- Add correctness-tested built-in profiles for at least one non-`H=8192` model geometry, and add TP2/TP4 coverage where supported.
- Exercise both fusion patterns across the newly supported profiles:
  - AllReduce + residual add + RMSNorm
  - MoE finalize + shared-expert add + AllReduce + residual add + RMSNorm
- Publish benchmark results across representative `M` values and derive LL/BT/HT route boundaries from those results.
- Preserve the existing GB300 TP8/TP16 profile performance and numerical contracts.
- Provide a support-query or documented fallback path suitable for inference-engine dispatch.
- Keep hardware-specific tuning isolated in profiles so future architectures can be added without model checks in framework integrations.

## Related work, dependencies, or suggested scope

- Initial backend: https://github.com/flashinfer-ai/flashinfer/pull/4358
- Related but distinct PDL-overlap request: https://github.com/flashinfer-ai/flashinfer/issues/5151
- Related TP12/Kimi K3 shape request: https://github.com/flashinfer-ai/flashinfer/issues/4542
- Current profile definitions: `flashinfer/comm/mnnvl_cutedsl/presets.py`
- Profile resolution: `flashinfer/comm/mnnvl_cutedsl/config.py`
- Existing routing tests: `tests/comm/test_mnnvl_cutedsl_config.py`

I can help with tuning, public benchmark sweeps, and follow-up PR work for additional shapes.


## 评论 (1)

### 3xela · 2026-09-19

hey, im interested in doing H=6144 (glm-5.2) TP8/4/2, on B200's and B300's
