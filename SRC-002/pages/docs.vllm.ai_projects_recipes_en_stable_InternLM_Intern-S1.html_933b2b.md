source: https://docs.vllm.ai/projects/recipes/en/stable/InternLM/Intern-S1.html
lastmod: 2026-04-27

# Intern-S1 Usage Guide[¶](https://docs.vllm.ai#intern-s1-usage-guide)

[Intern-S1](https://github.com/InternLM/Intern-S1) is a vision-language model that is developed by Shanghai AI Laboratory.
Latest vLLM already supports Intern-S1. You can install it using the following method:

## Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

## Installing vLLM (For AMD ROCm: MI300x/MI325x/MI355x)[¶](https://docs.vllm.ai#installing-vllm-for-amd-rocm-mi300xmi325xmi355x)

⚠️ The vLLM wheel for ROCm is compatible with Python 3.12, ROCm 7.0, and glibc >= 2.35. If your environment is incompatible, please use docker flow in [vLLM](https://vllm.ai/)

## Launching Intern-S1 with vLLM[¶](https://docs.vllm.ai#launching-intern-s1-with-vllm)

### Serving BF16 Model on 8xH800 GPUs (80GB × 8)[¶](https://docs.vllm.ai#serving-bf16-model-on-8xh800-gpus-80gb-8)

vllm serve internlm/Intern-S1 \
--trust-remote-code \
--tensor-parallel-size 8 \
--enable-auto-tool-choice \
--reasoning-parser deepseek_r1 \
--tool-call-parser internlm


### Serving FP8 Model on 4xH800 GPUs (80GB × 4)[¶](https://docs.vllm.ai#serving-fp8-model-on-4xh800-gpus-80gb-4)

vllm serve internlm/Intern-S1-FP8 \
--trust-remote-code \
--tensor-parallel-size 4 \
--enable-auto-tool-choice \
--reasoning-parser deepseek_r1 \
--tool-call-parser internlm


### Serving FP8 Model on 8xMI300x/MI325x[¶](https://docs.vllm.ai#serving-fp8-model-on-8xmi300xmi325x)

export VLLM_ROCM_USE_AITER=1
export VLLM_ROCM_USE_AITER_MOE=0
vllm serve internlm/Intern-S1-FP8 \
--trust-remote-code \
--tensor-parallel-size 8 \
--enable-auto-tool-choice \
--reasoning-parser deepseek_r1 \
--tool-call-parser internlm


`--tensor-parallel-size 4`

* You can set `export VLLM_ROCM_USE_AITER=1`

for Better Performance on AMD GPUs. The default is `export VLLM_ROCM_USE_AITER=0`

* Please turn off AITER MOE on MI300x/MI325x by `export VLLM_ROCM_USE_AITER_MOE=0`

### Serving FP8 Model on 8xMI355x[¶](https://docs.vllm.ai#serving-fp8-model-on-8xmi355x)

export VLLM_ROCM_USE_AITER=1
vllm serve internlm/Intern-S1-FP8 \
--trust-remote-code \
--tensor-parallel-size 8 \
--enable-auto-tool-choice \
--reasoning-parser deepseek_r1 \
--tool-call-parser internlm


`--tensor-parallel-size 4`

* You can set `export VLLM_ROCM_USE_AITER=1`

for Better Performance on AMD GPUs. The default is `export VLLM_ROCM_USE_AITER=0`

## Advanced Usage[¶](https://docs.vllm.ai#advanced-usage)

### Switching Between Thinking and Non-Thinking Modes[¶](https://docs.vllm.ai#switching-between-thinking-and-non-thinking-modes)

Configure through

Sample code

from openai import OpenAI
client = OpenAI(api_key='YOUR_API_KEY', base_url='http://0.0.0.0:8000/v1')
model_name = client.models.list().data[0].id
response = client.chat.completions.create(
model=model_name,
messages=[{
'role':
'user',
'content': [{
'type': 'text',
'text': '9.11 and 9.8, which is greater?',
}],
}],
temperature=0.8,
top_p=0.8,
extra_body={
"chat_template_kwargs": {"enable_thinking": False}
}
)
print(response)


## Using Tips[¶](https://docs.vllm.ai#using-tips)

If you encounter `ValueError: No available memory for the cache blocks.`

, try adding the `--gpu-memory-utilization 0.95`

flag to your `vllm serve`

command.