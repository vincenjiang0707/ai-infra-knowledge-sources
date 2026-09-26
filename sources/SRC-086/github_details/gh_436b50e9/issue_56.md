# [Issue #56] Will using this method result in inconsistent output results?

source: https://github.com/FasterDecoding/Medusa/issues/56
state: closed | updated: 2024-07-26T02:10:01Z
labels: 

## 正文

Is the results using Medusa different with the result using greedy decoding ?

## 评论 (8)

### leeyeehoo · 2023-10-23

In most cases, no. But there is a very tricky bug that we don't know is due to float16 or something else that the model will output inconsistent results after error accumulation (very rare, but it exists).

### niyunsheng · 2023-10-23

Thanks for your reply. According to my understanding, if the calculation error is ignored (for example, using fp32), the output result should be the same as greedy decoding.

### Junyoungpark · 2023-12-19

Hi, 

I love your work and thank you for sharing the code. I was wondering whether Medusa gives the same results to the original model (e.g., Vicuna) in sampling mode. Please let me know!

### leeyeehoo · 2023-12-19

Hi Junyoung, we will release a new version soon and it should contain the sampling method consistent with the original model's distribution. If you want to implement it yourself, it is super easy. 

Let's say you have a medusa head's prediction x_{hat} (top-k) from medusa logits p. When you perform the verification using the model's output q, sample x from q and if x matches x_{hat} then accept x_{hat} else reject. The distribution should be the same as the original and you will get a slightly low acceleration rate.

### Junyoungpark · 2023-12-19

Thank you for the reply. I will stay tuned for the new release!

### leeyeehoo · 2023-12-22

If you want to check it out first, you can switch to the v1.0 branch and it should be compatible with the previous version (almost done, only the new weight hasn't been released yet.). Let me know if you encounter any issues :)

### ctlllll · 2024-01-24

This thread seems to be quiet for a while. Let me close it for now, and feel free to reopen it :)

### zhoujian-z · 2024-07-26

@leeyeehoo the medusa no penalty when process logits compare with base model, may be also the reason?
