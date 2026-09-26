# [Issue #340] loss mean instead of dividing by loss mask.sum()

source: https://github.com/SafeAILab/EAGLE/issues/340
state: open | updated: 2026-07-09T14:51:26Z
labels: 

## 正文

in traineagle3 loss is calculate as mean for all positions ,but in train loss is divided by loss_mask.sum() , why is such?

## 评论 (1)

### AchuthReddy-16 · 2026-07-09

I looked into this a bit and noticed a small difference in how the loss is normalized between the original training code and EAGLE-3.

In the original EAGLE-1/2 training code, the loss is divided by `loss_mask.sum()`, so it is normalized only over the valid/unmasked tokens.

But in `eagle/traineagle3/cnets.py`, the loss is computed with `.mean()`:

```python
loss = -torch.sum(position_mask * plogp, 2).mean()
```

This averages over all batch/sequence positions, including positions where the mask is zero. Because of that, examples with more masked-out positions may contribute less to the loss compared to the original normalization.

Was this change intentional for EAGLE-3’s training setup, or should it be normalized by `position_mask.sum()` similar to the earlier training code?

