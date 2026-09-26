# [Issue #958] Stuck during inference

source: https://github.com/PaddlePaddle/ERNIE/issues/958
state: closed | updated: 2025-12-15T10:01:55Z
labels: 

## 正文

Hi, I have a stuck during inference in the following code:

  generated_ids = model.generate(
          inputs=inputs['input_ids'].to(device),
          **inputs,
          max_new_tokens=128
          )

I keep the same setting as described in the doc. I don't know why.

## 评论 (6)

### pILLOW-1 · 2025-07-01

I am using transformers to deploy ERNIE-4.5-VL-28B-A3B-PT following the instructions at https://www.modelscope.cn/models/PaddlePaddle/ERNIE-4.5-VL-28B-A3B-PT. 

### BossPi · 2025-07-01

Hello, it needs a long time for this model to generate tokens now. You can try using FastDeploy to test the model's performance.

### pILLOW-1 · 2025-07-01

Got it. By the way, can i use the api to perform inference?

### BossPi · 2025-07-02

Do you prefer to deploy a local API for inference or utilize a cloud-based API for inference?

### nepeplwu · 2025-10-01

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_

### Julian-Dumitrascu · 2025-12-15

> cloud-based API

I found this conversation while looking for this information:
1. The base URL of the API through which you make your models available.
I'd try them through a front end that is not made by you.
I'm willing to try them through front ends made by you.
2. The Web address at which one can get a key to this API.
3. The terms under which one can try your AI models.
Where have you published these data?
