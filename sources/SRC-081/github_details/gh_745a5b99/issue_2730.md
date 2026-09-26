# [Issue #2730] [Bug]: Mix-precision vLLM loading failure (MXFP4+MXFP8)

source: https://github.com/vllm-project/llm-compressor/issues/2730
state: closed | updated: 2026-07-28T17:03:10Z
labels: bug

## 正文

### ⚙️ Your current environment

<summary>hf is working while vllm is not. <code>python test_huggingface.py</code> <code>python test_vllm.py</code></summary>

```python
# test_huggingface.py
import transformers
import sys

text = "The united state of"
max_new_tokens = 10
model_name_or_path = "INCModel/Qwen3-0.6B-MXFP4-MXFP8"
model = transformers.AutoModelForCausalLM.from_pretrained(model_name_or_path, trust_remote_code=True, device_map="cpu", torch_dtype="auto")
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=True)
inputs = tokenizer(text, return_tensors="pt").to('cpu')
generated_ids = model.generate(**inputs, max_new_tokens=max_new_tokens)[0]
output = tokenizer.decode(generated_ids)
print(output)
```

```python
# test_vllm.py
from vllm import LLM, SamplingParams
import sys

text = "The united state of"
max_new_tokens = 100
model_name_or_path = "INCModel/Qwen3-0.6B-MXFP4-MXFP8"

llm = LLM(model=model_name_or_path, trust_remote_code=True)

sampling_params = SamplingParams(max_tokens=max_new_tokens)
outputs = llm.generate([text], sampling_params)

for output in outputs:
    print(output.outputs[0].text)
```


### 🐛 Describe the bug


Issue1: Loading failure, KeyError: 'layers.0.mlp.gate_up_proj.weight'

Fixed in `find_matched_target` with changed order.
```
    matched_target = (
        _find_first_match(layer_name, targets)
        or _match_fused_layer(layer_name, targets, fused_mapping)
        or _find_first_match(module.__class__.__name__, targets, True)
    )
```

Issue2: Load success but prompt generation is incorrect.


### 🛠️ Steps to reproduce

Using main branch of CT, and latest vllm.
`python test_vllm.py`

## 评论 (0)
