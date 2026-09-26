# [Issue #1792] [Optimization]The quantization speed of the 72B VL model is too slow.

source: https://github.com/ModelCloud/GPTQModel/issues/1792
state: closed | updated: 2026-01-28T09:24:35Z
labels: 

## 正文

```python
import os
from gptqmodel import GPTQModel, QuantizeConfig
from transformers import AutoTokenizer
from datasets import load_dataset

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

def format_qwen2_vl_dataset(image, assistant):
    return [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image},
                {"type": "text", "text": "generate a caption for this image"},
            ],
        },
        {"role": "assistant", "content": assistant},
    ]

def prepare_dataset(n_sample: int = 20):
    dataset = load_dataset("laion/220k-GPT4Vision-captions-from-LIVIS",
                           split=f"train[:{n_sample}]")
    return [
        format_qwen2_vl_dataset(sample["url"], sample["caption"])
        for sample in dataset
    ]


pretrained_model_id = "inclusionAI/UI-Venus-Ground-72B"
quantized_model_id = "UI-Venus-Ground-72B-GPTQ"

dataset = prepare_dataset(n_sample=32)
quantize_config = QuantizeConfig(
    bits=4,
    group_size=128,
    damp_percent=0.1,
    desc_act=False,  # Significantly speeds up inference
    static_groups=False,
    sym=True,
    true_sequential=True,
)

model = GPTQModel.load(
    pretrained_model_id,
    quantize_config=quantize_config,
    device="cuda:0",
    torch_dtype="auto",
)
tokenizer = AutoTokenizer.from_pretrained(pretrained_model_id, use_fast=True)
model.quantize(dataset, auto_gc=False)
model.save(quantized_model_id)

```

Quantization has been ongoing for more than 10 hours and is still not complete.
CPU: AMD EPYC 7K62 48-Core Processor
RAM: 64GB
GPU: A100-SXM-64GB

## 评论 (5)

### Qubitium · 2025-09-14

@zjx-ERROR  Did you try increasing `batch_size` in `model.quantize(dataset, auto_gc=False)`?

### zjx-ERROR · 2025-09-14

Yes, I tried, but the result was the same.
```python
model.quantize(dataset, auto_gc=False, batch_size=16)
```

### Qubitium · 2025-09-14

@zjx-ERROR  Post your logs. Btw, have you quantized before? You might have a unrealistic expection of quantization speed when it comes to gptq. =) I can check your logs to see if it's `normal`. 

### Qubitium · 2025-09-14

<img width="3932" height="1388" alt="Image" src="https://github.com/user-attachments/assets/5482df91-4f2d-4cca-9af1-16d1e4dba728" />

~1 hour.  Pretty sure you don't have enough ram. 64GB is not enough to hold 70B model in ram. 

### ooolmk · 2026-01-28

I've also noticed that when using GPTQModel to quantize vision-language (VL) models, it often takes 5 to 10 times longer than quantizing a language model of the same size. Just wanted to share this observation


