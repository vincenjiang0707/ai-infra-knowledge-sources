# [Issue #79] Why the speed up of Medusa 1 on vicuna changed?

source: https://github.com/FasterDecoding/Medusa/issues/79
state: closed | updated: 2024-02-06T12:57:14Z
labels: 

## 正文

In the blog, the speed up is 1.97x
![image](https://github.com/FasterDecoding/Medusa/assets/62385270/e3f4bab7-9016-402f-bc31-4cc7dc489a24)

But in the report, the speed up is 2.18x
![image](https://github.com/FasterDecoding/Medusa/assets/62385270/092456d4-839b-4763-87c7-d86c6b209fd8)

I noticed that the huggingface repository hasn't been updated.

Have you updated the medusa head for vicuan 7B v1.3?

## 评论 (2)

### niyunsheng · 2024-02-06

Can you provide the baseline profile jsonl file, 
like the one in the `llm_judge/data/mt_bench/model_answer` directory?

### niyunsheng · 2024-02-06

I used this code and get the similar results.
So there's no need to answer this question
