# [Issue #2526] KDTrainer: support combining CE loss and KD loss during training via a configurable weight

source: https://github.com/NVIDIA/Model-Optimizer/issues/2526
state: open | updated: 2026-09-23T19:45:47Z
labels: feature request

## 正文

**Detailed description of the requested feature:**

The new HF KD trainer loss function `KDTrainer.compute_loss()` currently doesn't combine `ce_loss` and `kd_loss` (only returns `kd_loss`), so we'd need to compute `ce_loss` during training too and then combine both losses.

Ideally it should:

1. Combine them as: `alpha * kd_loss + (1-alpha) * ce_loss`
2. Not compute `ce_loss` during training if `alpha = 1.0` (default)

---

**Timeline:**

Happy to submit a PR at any time.

---

**Describe alternatives you've considered:**

Overriding `KDTrainer.compute_loss()` in user code to manually compute and combine the losses — which is what I did in my own pipeline, and what the current documentation implicitly requires.

---

**Target hardware/use case:**

Any HuggingFace-based KD training setup using `KDTrainer` where retaining ground-truth signal alongside soft targets is important — for example, distilling a large Qwen2.5-Coder-7B into a smaller 0.5B student.


## 评论 (2)

### TheSabari07 · 2026-09-23

Hi @AAnoosheh I’ll submit the PR for this in a few minutes. Thanks for pointing this out and for the guidance.


### TheSabari07 · 2026-09-23

Hi @AAnoosheh, I have raised a PR. Please review it at your convenience and let me know if any changes are needed. 
Thank you.
