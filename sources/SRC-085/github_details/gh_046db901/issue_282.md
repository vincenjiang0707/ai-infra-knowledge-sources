# [Issue #282] Support on Qwen3

source: https://github.com/SafeAILab/EAGLE/issues/282
state: closed | updated: 2025-08-21T06:57:05Z
labels: 

## 正文

Hi there, I have followed #271.

What is the transformer version to support this Qwen3? When I was using v4.52.4, there comes a bug "ModuleNotFoundError: No module named 'transformers.masking_utils'". After I updated to the latest version v4.55.2, there comes a bug ImportError: cannot import name 'LossKwargs' from 'transformers.utils'. 

Thanks for the help!

## 评论 (3)

### aladinggit · 2025-08-15

I further checked #278. Even pip install transformers==4.53 is not bug free (at least from my end, maybe something else is wrong?), with error output TypeError: create_causal_mask() got an unexpected keyword argument 'position_ids'. Thanks!

### hongyanz · 2025-08-16

@y344shi @HaochenGu  Can you please look at this? Thanks.

### HaochenGu · 2025-08-16

`torch==2.6.0
transformers==4.53.3
accelerate==0.26.0
fschat==0.2.31
gradio==3.50.2
openai==0.28.0
anthropic==0.5.0
sentencepiece==0.1.99
protobuf==3.19.0
wandb`

I have done some attempts. I believe this set works.
