# [Issue #259] why use fp16 for eagle-llama3.1-8b

source: https://github.com/SafeAILab/EAGLE/issues/259
state: closed | updated: 2025-07-29T13:54:12Z
labels: 

## 正文

Hi, I noticed that you use fp16 when training eagle for llama3.1-8b-instruct and the released ckpt is also in fp16 precision. 
But llama3.1-8b-instruct is natively in bf16 precision. 

Why you use fp16 precison for eagle-llama3.1-8b, and is there a precision mismatch here?

## 评论 (3)

### hongyanz · 2025-07-20

EAGLE is designed for accelerating inference of the target model. In the following line, we have set the precision of the target model to be float16. So during the EAGLE-3 training, both the EAGLE head and the target model are using FP16. There is no precision mismatch here.

https://github.com/SafeAILab/EAGLE/blob/a0e1e2c08604f0d215c531d9655b7ebacedde130/eagle/traineagle3/cnets.py#L481

META was using BF16 to train the target model and FP16 to do the inference. Since we only care about inference here, so we set everything consistent to be FP16.

### SUDA-HLT-ywfang · 2025-07-21

I think Llama-3.1-8B-Instruct uses **bf16** for inference as shown in [the official hf repo](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct#use-with-transformers).

### hongyanz · 2025-07-27

I think both bf16 and fp16 work. Another reason is historical: in EAGLE-1, we used RTX 3090, which supports fp16 better.
