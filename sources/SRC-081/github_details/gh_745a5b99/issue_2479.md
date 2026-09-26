# [Issue #2479] AWQ various enhancements and research

source: https://github.com/vllm-project/llm-compressor/issues/2479
state: closed | updated: 2026-07-31T18:23:35Z
labels: enhancement, awq, stale

## 正文

Figure out whether the following techniques would be useful/profitable to enable

1) AWQ + MSE observer where AWQ jointly optimizes scale + shrinkage, i.e. if you AWQ with minmax -> quantization with MSE observer how much worse does that perform than including shrinkage factor in the grid search?

2) in general AWQ's scale search is brute force, there exist myriad black box optimization techniques e.g. bayesian optimization that could potentially massively reduce the search time, especially if (1) above is fruitful.



## 评论 (9)

### HDCharles · 2026-03-17

assigned to @dzhengAP

### dzhengAP · 2026-03-18

Sure @HDCharles, I will take it

### dzhengAP · 2026-03-20

@HDCharles — I am attaching some findings summary for #2479.

##  AWQ + MSE Observer Alignment
I open a tentative PR and benchmarked all 4 combinations of (search, final)x(mse, minmax)on Llama-3.1-8B-Instruct W4A16, open-platypus calibration, WikiText-2 eval:

| Recipe | PPL | Δ vs baseline |
|---|---|---|
| FP16 (reference) | 9.459 | — |
| minmax search + minmax final (baseline) | 10.023 | +0.000 |
| minmax search + mse final | 9.953 | **-0.070** |
| mse search + minmax final | 9.966 | -0.057 |
| mse search + mse final | 10.029 | +0.006 |

It appears that `memoryless_mse` as the final quantization observer consistently outperforms `memoryless_minmax` regardless of the search observer used (+0.057–0.070 PPL improvement). However, using MSE in the grid search itself appears counterproductive — `mse search + mse final` is the worst performing MSE combination, suggesting that MSE shrinkage during search finds scales optimized for aggressive clipping that do not generalize well at deployment time. _Or maybe the research direction can go the other way like, why misalignment perform better?_

These findings are based on a single model (Llama-3.1-8B-Instruct) and dataset (open-platypus). Results may vary across different architectures and calibration data, also the delta across the combinations are fairly small— would appreciate your thoughts on whether broader evaluation is warranted before drawing conclusions.

## PR #2492 Contributions

While the benchmark shows alignment alone does not yield consistent gains, the investigation surfaced several concrete improvements to the AWQ implementation:

- **`search_observer` parameter** on `AWQModifier` — aligns grid search observer with final quantization observer. Default `"memoryless_minmax"` is fully backward compatible
- **`_VALID_SEARCH_OBSERVERS` module-level constant** — validates only memoryless observers are accepted; stateful observers would accumulate state across grid iterations producing incorrect scales
- **`math.isfinite` guard** in `_compute_best_scale` — skips non-finite grid search losses gracefully instead of crashing. `memoryless_mse` can produce aggressive clipping → NaN forward pass on some layers; without this guard the entire run crashes
- **3 new unit tests** — default value, valid input, invalid input rejection

## Q2: Bayesian Optimization for Scale Search

Not profitable for the existing 1D per-group search — too low-dimensional and each eval is cheap. BO advantage only appears at 3+ dimensions. The interesting version would be joint multi-layer or mixed-precision search. Happy to explore further if you think it's worth pursuing.

### HDCharles · 2026-03-25

it doesn't look like the scale + shrinkage joint optimization was ever tested or am i misreading things?

### dzhengAP · 2026-03-26

@HDCharles — thanks for the comment and clarification, which makes more sense to me, I just redid the experiment and updated findings for Q1, now including the joint scale + shrinkage optimization.

## What was implemented

Added `n_shrink_grid` and `maxshrink` parameters to `AWQModifier` to jointly optimize scale (α) and shrinkage (p) against output MSE in a single grid search. For each scale candidate, the search now sweeps over shrink factors `p ∈ (1-maxshrink, 1]` and selects the `(α, p)` pair that minimizes output MSE — aligning both optimizations against the same objective.

## Benchmark results

Model: `Llama-3.1-8B-Instruct`, W4A16 ASYM group=128, open-platypus calibration, WikiText-2 eval

**Joint shrinkage (new):**

| Recipe | PPL | Δ vs baseline |
|---|---|---|
| AWQ baseline (n_shrink_grid=1) | 10.008 | +0.000 |
| AWQ + joint shrinkage (n=5) | 10.007 | -0.001 |
| AWQ + joint shrinkage (n=10) | 9.993 | **-0.014** |

## Key takeaways

- Joint shrinkage shows consistent improvement scaling with `n_shrink_grid` — the trend suggests higher values would continue to improve at the cost of runtime
- These findings are based on a single model and dataset — broader evaluation across architectures may be warranted

Both features are in PR #2492 with full backward compatibility.
 Will try BO to see any speed improvement. Happy to discuss next steps.

### HDCharles · 2026-03-30

well it did improve things but i'm not sure that its enough, its such a small improvement seems almost negligible for the complexity and runtime increase.

@dzhengAP what do you think?

### dzhengAP · 2026-04-01

Hi @HDCharles, I am attaching some new results following our discussion, please check below. Key Takeaway is the new methods works, and it doesn't need to go monotonously, as n = 10 shows the best results (probably due to not overfitting).

## Motivation
AWQ's grid search optimizes scale (alpha) against output MSE, but the quantization clipping range (shrinkage) is determined independently by the observer using weight MSE. These objectives are misaligned.

## Methods & Algo
This commit adds output_mse_shrinkage: per-group shrinkage optimization using the same output MSE objective as the scale search. For each scale candidate, the best clipping factor p is selected per quantization group by minimizing the activation-projected weight quantization error:

  w_err  = W_quant - W_scaled            (out_ch, G, group_size)
  out_err = einsum('ogs,ngs->ogn', w_err, X_grouped)     (out_ch, G, n_tokens)
  err     = out_err^2.sum(n)             (out_ch, G)

X is collected from real calibration samples via a forward hook on the balance layer, so the error reflects actual token distributions rather than a proxy. Each group independently selects its optimal p, allowing aggressive clipping where activations are small and conservative clipping where they are large.

New parameters:
  n_shrink_grid: int = 1    (1 = disabled, backward compatible)
  maxshrink: float = 0.20   (search range: p in [1-maxshrink, 1.0])

## Results
Benchmarked on Llama-3.1-8B-Instruct W4A16 ASYM group=128, open-platypus calibration, WikiText-2 eval:

  Baseline (n_shrink_grid=1):   PPL 9.995
  output_mse_shrinkage (n=10):  PPL 9.890  (-0.105) ← best
  output_mse_shrinkage (n=50):  PPL 9.953  (-0.042)
  output_mse_shrinkage (n=100): PPL 9.941  (-0.054)

All n values improve over baseline. n=10 gives best result; improvement is not strictly monotonic, suggesting diminishing returns from finer shrinkage resolution on calibration data.

##Notes
Implementation notes:
  - Chunked einsum over out_ch to bound peak memory (~256MB per chunk)
  - Activation samples capped at 2048 tokens to prevent OOM on large models
  - 5 new unit tests, all passed
 
PR: #2492 
Part of #2479

### github-actions[bot] · 2026-06-30

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### github-actions[bot] · 2026-07-31

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant. Thank you!
