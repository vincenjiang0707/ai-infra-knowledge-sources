# [Issue #257] INT4-AWQ PPL results for LLaMA-3 model are not as expected

source: https://github.com/mit-han-lab/llm-awq/issues/257
state: open | updated: 2025-03-19T05:37:22Z
labels: 

## 正文

I keep following the new code. I have tried to evaluate both the real quantized model and pseudo quantization using Llama-3-8B-Instruct model (w4-g128), based on wikitext-2-raw-v1(test). But the PPL result is **8.5.**   (GPU:A100, test data is downloaded from https://huggingface.co/datasets/Salesforce/wikitext/tree/main/wikitext-2-raw-v1)
I want to confirm if my result is correct? And why are the results  different?


## 评论 (1)

### Louym · 2025-03-19

Instruct models have larger ppl and we report the base model ppl.
