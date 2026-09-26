# [Issue #963] Which ERNIE MoE Implementation Should I Use for Pretraining?

source: https://github.com/PaddlePaddle/ERNIE/issues/963
state: closed | updated: 2025-07-04T07:36:39Z
labels: 

## 正文

Hello, I would like to try MoE pre-training.
I noticed that the code in `ERNIE/examples/pre-training/ernie` and `ERNIE/ernie/ `seems to be somewhat different.

If I want to train a model like ERNIE 4.5, should I follow the code in the top-level `ERNIE/ernie/ `directory?

## 评论 (8)

### JiabinYang · 2025-07-02

If u want to do pre-train with ERNIE 4.5,  u could follow code in `ERNIE/examples/pre-training/`.

### yeontaek · 2025-07-02

@JiabinYang 

Thanks for the quick response.
I may have overlooked it, but it seems that model optimization techniques like **Router Orthogonalization Loss** are not implemented in the `ERNIE/examples/pre-training/ `directory.
Is that correct?

### FeixLiu · 2025-07-02

Yes, ` Router Orthogonalization Loss` is not supported for now.

### yeontaek · 2025-07-02

Are training speed optimizations, such as 1f1b and similar techniques, implemented in that directory?
We’d like to verify whether MoE training with this implementation is faster than Megatron’s repository.

### ForFishes · 2025-07-02

1f1b-related optimizations are already in the dependent paddlepaddle. Some fp8-related optimizations are being sorted out and will be open sourced soon.

### yeontaek · 2025-07-03

Thank you all for the prompt responses.
I was wondering if there are any plans to include model optimization methods such as Router Orthogonalization Loss in the pre-training pipeline.
We are currently considering whether to adopt this framework for our MoE pre-training work.



### FeixLiu · 2025-07-03

The `Router Orthogonalization Loss` will be released in the future.

### yeontaek · 2025-07-04

Got it. I’ll follow up with more questions if the feature gets released.
Thank you all for your support!
