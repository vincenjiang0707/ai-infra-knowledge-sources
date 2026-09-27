# [Issue #190] Can you provide examples code to run inference on video QA?

source: https://github.com/mit-han-lab/llm-awq/issues/190
state: open | updated: 2024-07-12T06:30:12Z
labels: 

## 正文

For the example in this page: https://github.com/mit-han-lab/llm-awq/tree/main/tinychat#usage 
You can easily inference on images: 
python vlm_demo_new.py \
    --model-path VILA1.5-13b-AWQ \
    --quant-path VILA1.5-13b-AWQ/llm \ 
    --precision W4A16 \
    --image-file /PATH/TO/INPUT/IMAGE \
    --vis-image #Optional

However, how do you run video QA inference? Can you provide an example?



## 评论 (2)

### jqXiong · 2024-06-27

AWQ好像无法运行video吧

### Nikitosina · 2024-07-12

But I was able to run video QA on demo page: https://vila.hanlab.ai/
Is there a way to reproduce this locally?

