# [Issue #232] How to convert the AWQ model after the quantization into safetensors

source: https://github.com/mit-han-lab/llm-awq/issues/232
state: open | updated: 2024-12-09T15:19:27Z
labels: 

## 正文

Sorry.
I searched everywhere but I don't found any script to convert the quantized .pt file to the **safetensors.**

I received the Llama-3.1-Nemotron-70B-Instruct-HF-w4-g128.pt
After using this script:
```
python -m awq.entry --model_path $MODEL \
    --tasks wikitext \
    --w_bit $w_bit --q_group_size 128 \
    --load_quant quant_cache/$MODEL-w$w_bit-g128-awq.pt \
    --max_memory $max_memory \
    --parallel
```

Please maybe someone can help me with that. 

## 评论 (1)

### cute149q · 2024-12-09

Hi did you solve it?
