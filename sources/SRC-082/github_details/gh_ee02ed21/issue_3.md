# [Issue #3] 3bit backward implementation

source: https://github.com/mit-han-lab/llm-awq/issues/3
state: closed | updated: 2026-03-02T16:11:34Z
labels: 

## 正文

Thank you for your amazing work. Do you have any plans to implement 3 bit backward (transpose matmul)?
I think this can apply LoRA to the model in 3 bits. like QLoRA

## 评论 (2)

### tonylins · 2023-06-02

Thanks for your interests in our work! For now, we focus on 4-bit implementation since it offers noticeable better accuracy compared to 3-bit, we will see if there is a big need for 3-bit kernels. 

### madhav120ai · 2026-03-02

hi, is there any update on this? 
