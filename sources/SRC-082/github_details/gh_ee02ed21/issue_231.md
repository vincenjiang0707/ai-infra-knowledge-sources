# [Issue #231]  Regarding the issues encountered with w_bit 3 quantification

source: https://github.com/mit-han-lab/llm-awq/issues/231
state: open | updated: 2026-03-02T16:10:57Z
labels: 

## 正文

Very good job!
I have encountered a problem:
I can quantify according to a w_bit 4，128 group, but is there a result of quantifying according to a w_bit 3， 128 group in the article, or is the result in the article based on the simulated PPL index? I ran the instruction that could be quantized according to 4 bits, but modified w_bit 4 by w_bit 3, which resulted in an error, as shown in the figure
![微信图片_20241030183931](https://github.com/user-attachments/assets/7462d0ac-d4fe-406d-aa45-87ff90ba81b0)
What should I do？

## 评论 (2)

### terarachang · 2024-11-21

Hi, I got a similar issue when generating real quantized weights (w3).

```
  File "/home/username/llm-awq/awq/quantize/qmodule.py", line 83, in __init__
    raise NotImplementedError("Only 4-bit are supported for now.")
```
Any solutions?


### madhav120ai · 2026-03-02

any updates on this? 
