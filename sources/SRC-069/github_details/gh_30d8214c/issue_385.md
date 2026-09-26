# [Issue #385] Origin & calibration methodology of the three cost-model constants in sm120.hpp

source: https://github.com/deepseek-ai/DeepGEMM/issues/385
state: open | updated: 2026-08-17T07:04:53Z
labels: 

## 正文

**Summary**
While studying the SM120 heuristics, [commit 1383f15](https://github.com/deepseek-ai/DeepGEMM/commit/1383f15d524d929059f7f4b11489e08d6b793ef2#diff-18b89a8f7d4c07c20a45c7008d343419517421a54a8743baf771d830b9fd71bb)
I noticed three magic constants driving the layout scoring function:

```
static constexpr double kCyPerTmaByte    = 0.07;    // ~35 GB/s per SM
static constexpr double kSyncBaseCy      = 120.0;   // per-kblock barrier overhead
static constexpr double kBlockOverheadCy = 2000;    // epilogue + scheduling
```
I'd like to open a discussion around two questions:

How were these values originally chosen? Were they measured on a specific SKU, taken from a theoretical model, or hand-tuned against a benchmark suite?
Would the maintainers be open to a documented calibration procedure so that downstream users on different SM120 SKUs (RTX 5090 / PRO 5000 / etc.) can re-derive them for their own hardware?

Thanks!

## 评论 (1)

### 0z5a · 2026-08-17

I ran a first SM120 cost-model calibration pass on real Blackwell hardware. Summary: the current three-constant form did not yield a defensible parameter update, so I do **not** plan to send a constants-only PR from this result.

**Test setup**
- RTX 5080 (SM120), 84 SMs, driver 591.74, CUDA runtime 13.0
- GPU graphics clock locked at 2700 MHz for the run
- Dense FP8 GEMM, K-major inputs, BF16 output; 8 representative shapes
- 20 warmups + 80 timed samples per forced layout, with a 256 MiB L2 flush
- Every forced-layout result was checked against the GEMM reference

**Results**
- The historical heuristic selected the fastest measured layout for 7/8 shapes.
- The one miss was M=1024, N=4096, K=4096: selected layout median 142.912 us vs. fastest candidate 138.752 us (2.91% lower kernel latency; ~1.030x). This looks like a separate structural/scheduling opportunity rather than evidence for retuning only the three global constants.
- Whole-shape holdout (6 train / 2 holdout shapes; 20 / 4 layout candidates):
  - baseline Top-1: 50.0%; mean regret: 1.50%; P95 regret: 3.00%
  - calibrated Top-1: 50.0%; mean regret: 1.50%; P95 regret: 3.00%

I fit the same feature decomposition used by the old SM120 path (TMA-byte term, sync term, and per-block-overhead term) with non-negative robust regression. The constrained fit was alpha=0.06127, beta=0, gamma=0 (baseline: 0.07, 120, 2000). The collapse of the latter two terms and the unchanged holdout metrics indicate that this dense dataset cannot independently identify the current three terms; it would be unsafe to replace the defaults based on it.

I have a reproducible collector/fitter, including feature-consistency checks against the historical SM120 formulas and CPU-only tests. For a future change, I would suggest collecting a broader matrix (especially more wave-count / pipeline-stage variation) and requiring a strictly better whole-shape holdout regret before proposing a default-constant update.

One integration note: current `main` has removed the historical SM120 heuristic/kernels, so the collector cannot be submitted as a directly runnable `main` PR today. I will keep the calibration work ready and can rebase/submit once the intended SM120 integration target is clarified.

