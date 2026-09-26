# [Issue #329] Non‑greedy rejection sampling ignores draft (q); not lossless per Speculative Decoding

source: https://github.com/SafeAILab/EAGLE/issues/329
state: open | updated: 2026-06-03T10:46:00Z
labels: 

## 正文

### Summary
The non-greedy rejection sampling path does not compute the draft distribution $q$, so it cannot implement the
lossless acceptance/replacement rule from speculative decoding. It currently uses the target distribution $p$
only (with some candidate masking), which deviates from the referenced algorithms.

### Expected (lossless) behavior
From [EAGLE-3](https://arxiv.org/pdf/2503.01840) paper (end of Sec. 2.1):
```math
\mathrm{norm}(\max(0, p_{j+i} - \hat{p}_{j+i}))
```
<br>

Additionally, from [Fast Inference from Transformers via Speculative Decoding (2022)](https://arxiv.org/pdf/2211.17192) (Sec. 2.3, Algorithm 1):
- Accept with probability: $\min(1, p/q)$
- If rejected, sample from:
```math
\mathrm{norm}(\max(0, p - q))
```

### Current behavior in this repo
In `eagle/model/utils.py`, the non-greedy branch uses target logits only:

- `evaluate_posterior` computes:
  ```python
  gt_logits = logits[fi, i - 1][None]
  gt_logits = logits_processor(None, gt_logits)[0]
  gtp = torch.softmax(gt_logits, dim=0)
  ...
  qx = 1.0
  acp = px / qx
  ```
  This is not min(1, p/q).

- Replacement sampling uses `sample_p = gtp` (target-only), and
  `update_inference_inputs` samples from `sample_p`, not
  $\mathrm{norm}(\max(0, p - q))$.

### Code references
- `eagle/model/utils.py` (non-greedy branch): `evaluate_posterior(...)` around lines 360–416
- Replacement sampling: `update_inference_inputs(...)` around lines 460–466

This makes the non-greedy path **lossy**, deviating from the algorithmic guarantees described in both papers.

### Suggested fix
At rejection time:
1) Compute draft logits $q$ for the same position (run draft model on accepted prefix or use cached KV if available),
2) Apply $\mathrm{norm}(\max(0, p - q))$ for replacement,
3) Use acceptance probability $\min(1, p/q)$ for the proposed token.


## 评论 (2)

### BeningShum · 2026-02-18

I think they assumed one-hot distribution of all the draft tokens, and it does no harm to the precision of the target distribution.

### ethantsliu · 2026-02-18

@BeningShum   I see. You’re right that if you treat each drafted token as a one‑hot q (q(x)=1 for the proposed x, 0 otherwise) and on rejection resample from p conditioned on not x, the marginal output is still p. So in that sense it’s lossless.

However, on principle, that's not the SD algorithm they cite in the paper, and it's also inefficient in sampling. If p(x) = q(x) = 0.1, the standard rule would accept with probability 1, while this code would accept with probability 0.1 and re-sample 90% of the time. 

