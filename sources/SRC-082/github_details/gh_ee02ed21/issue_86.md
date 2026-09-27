# [Issue #86] How to implement AWQ with GPTQ?

source: https://github.com/mit-han-lab/llm-awq/issues/86
state: closed | updated: 2024-12-05T12:52:36Z
labels: 

## 正文

Hi, great work! In the paper, it says that AWQ is orthogonal to GPTQ, and can improve the performance on extreme low bit scenario(2-bit). Does it mean that we can firstly use GPTQ and then AWQ, or the reverse pattern?

## 评论 (3)

### tonylins · 2023-09-08

Hi, you can first apply AWQ to scale and clip the weights (without actually quantizing the weights), and then apply GPTQ. 

Notice that it only works on very low-bit like 2. 

### rainyBJ · 2023-09-09

Thanks for your kindly reply.
Actually, I'm a little confused that in AWQ, we use the block-wise MSE loss to choose the best exponent for scale(which is used to adjust channel-wise distribution for weight, making weight related to larger activation larger). In this process, we use a different quantization logic(pure fake quant) against GPTQ(based on Hessian). 
So at first,  I'm not sure if using AWQ before GPTQ is helpful for the quantization process is not aligned in the 2 algorithms. But for another point of view, AWQ helps making important weight's quantization error smaller, so maybe it can provide a better starting point for GPTQ.
At last, you mentioned that it only works on very low-bit, which is consistent with our experiments where we use W8A16 setting for GPT2-like model, AWQ + GPTQ & GPTQ's results are similar.

### Yiman-GO · 2024-12-05

@rainyBJ have you tried awq(with pure fake quant) + gptq on W4a16? If yes, can you share the results?
