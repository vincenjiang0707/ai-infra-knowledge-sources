# [Issue #5366] [Feature]: Experimental adaptive sparse block-mask selection

source: https://github.com/flashinfer-ai/flashinfer/issues/5366
state: open | updated: 2026-09-21T07:49:10Z
labels: feature request, needs-triage

## 正文

### Before submitting

- [x] I have searched existing issues and this request has not been filed yet.

### Problem

FlashInfer provides sparse-attention execution backends and proxy-score
operators, but it does not currently provide the adaptive sparse block-mask
selection policy used by Tencent hpc-ops Stem TPD.

Given BF16 block-level proxy attention logits, users currently need to combine
a generic top-k operator, threshold comparison, mandatory prefix retention,
causal-window retention, and mask construction as separate operations.

This introduces additional kernel launches, intermediate tensors, and global
memory traffic before sparse attention can run. It also leaves the
prompt-length-dependent sparse-budget policy outside FlashInfer.

### Requested outcome

Add an experimental FlashInfer API that converts BF16 proxy attention logits
into a per-head boolean sparse block mask in one CUDA launch.

The requested capability should support:

- prompt-length-dependent sparse budgets;
- per-query budget decay;
- exact BF16 radix-threshold selection;
- mandatory leading/sink blocks;
- a causal diagonal window;
- caller-owned output buffers;
- explicit JIT-only experimental opt-in.

The initial API can remain experimental while its policy parameters and
end-to-end sparse-attention integration are validated.

### Target hardware

SM100 (B200, GB200)

### Inference engine

PyTorch native

### Affected model or model family

Model-independent; intended for long-context sparse-attention and indexer/proxy-score pipelines.

### Workload and configuration

- Data type and quantization: BF16 proxy logits; boolean output mask
- Batch size or request concurrency: B=1 and B=4 measured
- Sequence lengths or token counts: block size 128; Kb=192, 1024, and 4096 measured
- Parallelism: single GPU; no TP / EP / DP / PP dependency
- Relevant shapes: H=8, Qb=64, Kb=192/1024/4096, block size=128
- Environment: NVIDIA B200 (SM100), CUDA toolkit 13.3, PyTorch 2.11.0+cu130, FlashInfer commit `975f90583d9ac8896db14cf0f26e99a853c2f136`

### Current workaround

The current workaround is a multi-operation PyTorch pipeline:

1. run `torch.topk` over every proxy-score row;
2. compare all logits against the selected threshold;
3. construct a mandatory prefix/window mask;
4. combine the masks.

This requires multiple launches and intermediate buffers. It is also not a
complete implementation of the prompt-length-dependent Stem TPD policy inside
FlashInfer.

### Impact

Throughput, Latency, Memory capacity or bandwidth, API usability or integration complexity

### Acceptance criteria

- Matches a PyTorch reference implementation for short, medium, and long prompt regimes.
- Covers Kb values across the 1-warp and cooperative multi-warp kernel configurations.
- Correctly preserves prefix, causal-window, and diagonal blocks.
- Handles non-finite proxy logits without selecting them through the top-k threshold.
- Supports caller-owned output buffers.
- Passes correctness tests on B200 and H100/H200 before graduation.
- Includes a runnable example and a reproducible CUPTI cold-L2 benchmark.
- Demonstrates an end-to-end sparse-attention benefit before graduating from experimental status.

### Related work, dependencies, or suggested scope

Owner: @slhslh

Source implementation:
https://github.com/Tencent/hpc-ops

Source commit:
https://github.com/Tencent/hpc-ops/commit/2a2e26562433a8ba4b504858f1c938eb7612c901

The adaptive selection policy is derived from the hpc-ops Stem TPD kernel and
retains its MIT attribution.

Suggested initial scope:

- public thin entry point in `flashinfer.sparse`;
- implementation under `flashinfer/experimental/adaptive_sparse_block_mask`;
- correctness tests under `tests/experimental`;
- JIT only, with no `flashinfer/aot.py` registration;
- no automatic backend routing.

SM90 is an intended target but still requires H100/H200 validation.

Graduation plan:

Within four weeks after merge, validate H100/H200 and B200, add CUDA Graph
coverage, connect the output to a FlashInfer sparse-attention backend, report
end-to-end latency and accuracy, and then either finalize the API or remove
the feature if it does not demonstrate sufficient benefit.

### Timing or release need

Experimental incubation and graduation review within four weeks after merge; target the next 0.7.x development cycle, subject to maintainer feedback.

### Reproducibility and measured performance

Measured on one NVIDIA B200 using CUPTI kernel timing with a cold L2 cache,
10 warm-up iterations, and 30 measured iterations.

| Shape | Adaptive CUDA | PyTorch top-k pipeline | Speedup |
| --- | ---: | ---: | ---: |
| B=1, H=8, Qb=64, Kb=192, k=49 | 0.015328 ms | 0.022303 ms | 1.455x |
| B=1, H=8, Qb=64, Kb=1024, k=132 | 0.016240 ms | 0.058672 ms | 3.613x |
| B=1, H=8, Qb=64, Kb=4096, k=439 | 0.022704 ms | 0.182157 ms | 8.023x |
| B=4, H=8, Qb=64, Kb=1024, k=132 | 0.020480 ms | 0.123566 ms | 6.033x |

The PyTorch baseline uses preallocated `torch.topk` outputs, threshold
comparison, and a precomputed mandatory prefix/window mask. These are
selector-pipeline measurements, not yet end-to-end sparse-attention results.

### Selection semantics and bounds

The radix pass finds an exact BF16 threshold. All finite values equal to the
selected threshold are retained, so ties can produce more selected blocks than
the nominal budget. This behavior is intentional and must remain documented
and tested. The initial implementation supports `Kb <= 32768` and rejects
larger key-block widths.

### Planned first consumer

The initial operator is intentionally standalone. The first planned
end-to-end integration is a boolean-mask-compatible FlashInfer sparse-attention
path on SM100. If the selected consumer requires BSR or compact block indices
instead of a dense boolean mask, the conversion cost will be included in the
end-to-end benchmark before graduation.


## 评论 (2)

### slhslh · 2026-09-21

!claim

### flashinfer-bot · 2026-09-21

Issue assigned to @slhslh.
