# [Issue #27] need help! about auto_scale.scale_fc_fc function

source: https://github.com/mit-han-lab/llm-awq/issues/27
state: open | updated: 2026-07-17T04:25:47Z
labels: 

## 正文

Hello， I would like to apply awq to a GPTBigCodeForCausalLM object and it has a unusual atten like this picture shown: 
![image](https://github.com/mit-han-lab/llm-awq/assets/137280166/58866dcb-ef77-429a-a462-ff520b0dc0e6)

 I added some necessary implements and finally i got this 
![image](https://github.com/mit-han-lab/llm-awq/assets/137280166/5d5a8c57-12c9-4f1f-8c05-afd3605b12d9)

it was caused by there:
![image](https://github.com/mit-han-lab/llm-awq/assets/137280166/71ab88d9-db87-43e4-af4f-609797134d6e)

Seems like fc2's scale was apply to both fc1 and fc2 ， and because the different shape between my_fc1 and my_fc2 ，the entire progrem was broken here.

It seems to be dividing the weight of the previous layer by the scaler of fc2 instead of dividing the input x of fc2 by the scaler，Right？

How can I fix this error , or could you please tell me why we must apply the scale to fc1 and fc2 ?

Thanks & Regrads


Can I do some change like this?
![image](https://github.com/mit-han-lab/llm-awq/assets/137280166/3d6bc148-23c6-4c12-be8f-9bced2592350)


## 评论 (2)

### fanlw0816 · 2023-08-30

I encountered the same error, how to apply awq to GPTBigCodeForCausalLM, can you give me some advice @kentang-mit @tonylins 

### Chessing234 · 2026-07-17

`scale_fc_fc` was dividing the full bias while only the last N weight rows are scaled. Fixed in #333.
