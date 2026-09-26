# [Issue #305] Training a new lm head for eagle3?

source: https://github.com/SafeAILab/EAGLE/issues/305
state: closed | updated: 2025-10-20T07:52:20Z
labels: 

## 正文

Hello,

We are trying to train our own EAGLE3 draft model. We have noticed some gaps between training and inference in terms of draft model class implementations. 

1) **lm_head**: At inference time, lm_head is loaded from eagle checkpoint, whose weights we confirmed to be different from target model's lm_head. However, in the training code under traineagle3 directory, we do not see any initialization for this class. Does this mean you explicitly allow it to be trained for drafter rather than copying base model lm head weights for training?
2) **hidden_states**: Paper figure for eagle3 inference pipeline suggests that drafter receives token logits (denoted with a, unconstrained vectors) rather than feature propagation (hidden_states, denoted with f). However, cnets.py passes input_hidden to forward of draft model in topK_genrate sampling function. 


Please help us resolve these issues.

Best,
Selin

## 评论 (1)

### hongyanz · 2025-10-20

Hello Selin,

1. Yes, we explicitly allow the LM head to be trained for drafter rather than copying base model LM head weights for training.
2. The input to the drafter is a concatenation of embedding (e) + feature (a or f).

Hope these are helpful.

Best,
Hongyang
