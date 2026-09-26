# [Issue #216] Questions on EAGLE-3 training-time test and request for training code release

source: https://github.com/SafeAILab/EAGLE/issues/216
state: closed | updated: 2025-06-13T04:20:48Z
labels: 

## 正文

Hi, Thank you for your great work on EAGLE-3. I am writing to ask a few questions regarding the training process, especially the **training-time test technique**, and to inquire about the code release timeline.

I understand that EAGLE-3 reuses draft model outputs as inputs during training to simulate inference-time behavior. I have a few questions on this:

1. Since this simulation resembles autoregressive decoding, I assume it makes full batch parallelism difficult. If so, did it significantly slow down training?

- Or are there specific techniques used to maintain training efficiency despite this?

2. At what point in training is the inference simulation applied (e.g., from the beginning, after warm-up steps, etc.)?

Also, could you kindly share:

- The code used to **generate the EAGLE-3 training dataset**

- The **training code** that implements the training-time test technique, or let us know when it will be released?

These would be extremely helpful for fully understanding and reproducing EAGLE-3.

Thank you again for your time and contribution.


## 评论 (2)

### pengchengneo · 2025-05-14

I have the same questions as @junghye01 , did u solved these problems or anybody can help with this ,thanks

### hongyanz · 2025-06-13

The training code has been released.
