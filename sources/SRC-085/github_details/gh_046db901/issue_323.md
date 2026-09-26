# [Issue #323] Question about removing vloss (feature alignment) in Eagle v3: is hidden-state alignment fundamentally incompatible with TTT?

source: https://github.com/SafeAILab/EAGLE/issues/323
state: closed | updated: 2026-01-14T06:56:00Z
labels: 

## 正文

Hi Eagle authors, thanks a lot for the great work on EAGLE / Eagle3
I have been experimenting with Eagle3 training and have a question regarding the design choice of removing vloss in Eagle v3, compared to Eagle v1.

In Eagle v1, the training code includes an explicit vloss term that aligns draft hidden states to target hidden states, e.g. via SmoothL1 / feature regression: vloss = SmoothL1Loss(predict, target_hidden)

This seems to act as a feature-level alignment regularizer in addition to the logits-level distillation loss (ploss).
However, in Eagle v3, this vloss appears to be removed, and the training objective focuses entirely on the logits-level loss (speculative-aware soft CE / KL via target logits).

I would really appreciate clarification on the following points:
1. Was vloss (hidden / feature alignment) intentionally removed in Eagle v3 due to incompatibility with TTT?
2. Did you experiment with hidden-state alignment (e.g. MSE / cosine / aux-head) in Eagle v3, and observe systematic degradation?
3. If there are any negative or inconclusive experimental results regarding vloss in Eagle v3 that you can share, that would be extremely helpful for practitioners.

Thanks again for the excellent work, and I’d really appreciate any insight you’re willing to share!

Best regards,
BAI Fan

## 评论 (1)

### hongyanz · 2026-01-14

Without TTT and vloss, the method will not work (very low acc). If either one exists, the method will work (but the performance varies). The best performance achieves when we have TTT and remove vloss.
