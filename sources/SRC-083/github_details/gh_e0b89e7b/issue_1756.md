# [Issue #1756] bnb.optim.AdamW performance differs from torch.optim.AdamW despite being called with the same hyperparameters

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1756
state: closed | updated: 2026-02-21T20:18:49Z
labels: Optimizers

## 正文

Hi, I noticed that when I swap out torch.optim.AdamW with bnb.optim.AdamW (both in 32 bit precision) and I fine tune a model loaded in bf16, the overall performance of the model trained using bnb's AdamW is higher than with Torch's. Furthermore, if I fine tune a model loaded in fp16, torch's AdamW leads to NaN values after the very first optim.step(), while bnb's AdamW trains perfectly fine without any NaNs. Is there a reason for this performance discrepancy, especially in the latter case? Does bnb internally use a different dtype than torch, or something else? Thank you

## 评论 (4)

### matthewdouglas · 2025-09-18

Interesting, thanks for asking about this! For the most part, we're using fp32 for all of the internal computations; we also cast the parameter value to fp32 when updating. Can you share what version of PyTorch you're using, and any example code to reproduce? 

### inkitori · 2025-09-19

I'm currently on torch==2.8.0. 

```
from transformers import Qwen2_5OmniProcessor, Qwen2_5OmniThinkerForConditionalGeneration
model = Qwen2_5OmniThinkerForConditionalGeneration.from_pretrained(model_id, torch_dtype="float16")

optim = torch.optim.AdamW(model.parameters(), lr=training_config['learning_rate'])
# optim = bnb.optim.AdamW(model.parameters(), lr=training_config['learning_rate'])
```

The rest of my code is just a regular torch training loop (no trainer/trl). I calculate my loss by passing labels directly into model.forward. Should I include more details?

### TimDettmers · 2026-02-21

Good observation. The performance difference comes from how the denominator is computed in the Adam update, not from precision casting (both bnb and PyTorch compute optimizer states in fp32).

The standard Adam update divides by `sqrt(v_hat) + eps`, but the order of operations differs:

**PyTorch:**
```
denom = sqrt(v) / sqrt(1 - β₂^t) + eps
```

**bitsandbytes:**
```
denom = sqrt(v) + eps * sqrt(1 - β₂^t)
```
(with a correspondingly adjusted step_size that makes them mathematically equivalent)

These are algebraically identical but numerically different. The PyTorch formulation divides `sqrt(v)` by the bias correction factor `sqrt(1 - β₂^t)` first — at step 1 with β₂=0.999, this is a division by ~0.0316, inflating intermediate values by ~32x. The `eps=1e-8` is then added at this inflated scale.

The bitsandbytes formulation keeps `sqrt(v)` at its natural (biased) scale and scales eps down to match (`eps * sqrt(1-β₂^t)`). The bias correction is instead folded into the step_size. This avoids the intermediate division by a small number, which matters for numerical stability — particularly at step 1 where the denominator is close to zero and the bias correction factor is most extreme.

This is why bnb's AdamW avoids the NaN you saw with fp16 parameters: the intermediate values stay at moderate magnitudes throughout the computation, whereas PyTorch's formulation can produce very large intermediates from the early-step bias correction division.

### TimDettmers · 2026-02-21

Closing this as explained above — the difference is by design. The bitsandbytes optimizer uses a numerically more stable ordering of the denominator computation that avoids dividing by the small bias correction factor at early training steps.
