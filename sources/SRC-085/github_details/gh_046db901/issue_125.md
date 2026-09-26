# [Issue #125] Training of Qwen2

source: https://github.com/SafeAILab/EAGLE/issues/125
state: open | updated: 2025-07-02T08:54:37Z
labels: 

## 正文

Hi, EAGLE team. I want to train my  EAGLE-Qwen2 model on  Chinese-ShareGPT dataset, to generate train data, I modified the code in `ge_data_all_llama3.py`, I only changed ` sep = "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n" ` to ` sep = "<|im_end|>\n<|im_start|>assistant\n"` and `sep2="<|eot_id|><|start_header_id|>user<|end_header_id|>"` to ` sep2="<|im_end|>\n<|im_start|>user" ` . But when I train the model, I encounter exploding gradient. Is there anything I need to take care when I generate train data of Qwen2?

## 评论 (3)

### Liyuhui-12 · 2024-08-28

You can refer to eagle/ge_data/ge_data_all_qwen2.py.

### souyang11 · 2025-03-26

> You can refer to eagle/ge_data/ge_data_all_qwen2.py.

Hello, it seems that the file cannot be found at the moment. Could you please upload it? Thank you.

### jiahe7ay · 2025-07-02

We have successfully trained the Eagle3 versions of Qwen3-8B and Qwen3-30B-A3B based on the official training code, and have open-sourced them. On a single H200 GPU using the sglang inference framework, Qwen3-8B with Eagle3 achieves a performance boost from 186 tokens/second to 365 tokens/second, while Qwen3-30B-A3B with Eagle3 improves from 147 tokens/second to 231 tokens/second.

We used the ultra_200k test set and re-ran inference on Qwen3 to regenerate the data, which was then used as the final training set.A total of 600K dialogues were used as the training set.

https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3

https://huggingface.co/Tengyunw/qwen3_8b_eagle3

Additionally, we have also published a report detailing how to reproduce the Eagle3 training process. The report link is provided below for your reference if needed.

https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA

https://zhuanlan.zhihu.com/p/1923763301432662012
