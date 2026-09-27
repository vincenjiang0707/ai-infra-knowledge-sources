# [Issue #241] Don`t work on CPU "Unable to get JIT kernel for brgemm"

source: https://github.com/mit-han-lab/llm-awq/issues/241
state: open | updated: 2024-12-18T08:51:48Z
labels: 

## 正文

Hi, guys. I am very impressed with your project. Thank you very much for your work. I encountered a problem. I can't run your model on the CPU. Here's what I'm doing in Colab:

```python
!pip install -q autoawq[cpu]
from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer

model_name = "Qwen/Qwen2.5-3B-Instruct-AWQ"
model = AutoAWQForCausalLM.from_quantized(
    model_name,
    use_ipex=True
)
tokenizer = AutoTokenizer.from_pretrained(model_name)
prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt")
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

And I get the following error:

```
No CUDA runtime is found, using CUDA_HOME='/usr/local/cuda'
Fetching 10 files: 100% 10/10 [00:00<00:00, 52958.38it/s]
Replacing layers...: 100% 36/36 [00:21<00:00,  1.68it/s]
Fusing layers...: 100% 36/36 [00:00<00:00, 56.02it/s]
Setting `pad_token_id` to `eos_token_id`:None for open-end generation.
Unable to get JIT kernel for brgemm. Params: M=32, N=39, K=128, str_a=1, str_b=1, brgemm_type=1, beta=0, a_trans=0, unroll_hint=1, lda=2048, ldb=39, ldc=39, config=0, b_vnni=0
```

What could this be?

## 评论 (1)

### XcloudFance · 2024-12-18

Hi, I also encounter the same situation here. Is it possible to run AWQ on CPU? Or it is very stricted to run on GPU only.
