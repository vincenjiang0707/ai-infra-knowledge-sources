# [Issue #140] The legacy Medusa Head structure is inconsistent with the new one.

source: https://github.com/FasterDecoding/Medusa/issues/140
state: open | updated: 2025-10-11T07:48:39Z
labels: 

## 正文

In medusa_model_legacy.py, the implementation is that the Medusa head is only responsible for generating new hidden states, and the generation of medusa logits still reuses the base_model's lm_head.

Here is the code: https://github.com/FasterDecoding/Medusa/blob/e2a5d20c048a9b0a4092e6933c34313687422518/medusa/model/medusa_model_legacy.py#L203-L206

---

However, in the new medusa_model.py or medusa_model_new.py, this has changed such that each Medusa head has its own "lm_head" (a Linear layer with in_features = hidden_size, out_features = vocab_size), as shown in the code below:
https://github.com/FasterDecoding/Medusa/blob/e2a5d20c048a9b0a4092e6933c34313687422518/medusa/model/medusa_model.py#L111-L119

Inference code is:
https://github.com/FasterDecoding/Medusa/blob/e2a5d20c048a9b0a4092e6933c34313687422518/medusa/model/medusa_model.py#L215-L218

---

This is very confusing, especially since the README.md provides both legacy and new training methods. Which of these truly reflects the performance reported in the paper?

Thank you very much for your work, looking forward to your reply or anyone's discussion. 

## 评论 (1)

### Jianhua-Cui · 2025-10-11

@leeyeehoo @ctlllll @Narsil Hello everyone, sorry to bother you. Since this repo seems to have not had anyone maintaining issues for a long time, could the core contributors please answer these questions?
