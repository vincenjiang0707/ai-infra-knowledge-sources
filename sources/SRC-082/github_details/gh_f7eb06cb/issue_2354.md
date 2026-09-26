# [Issue #2354] [BUG] Rotation parameter not saved and not used in inference ?

source: https://github.com/ModelCloud/GPTQModel/issues/2354
state: closed | updated: 2026-07-25T09:19:49Z
labels: bug

## 正文

# [Bug] : rotation parameter not saved and not used in inference ?
### in other words how can I use rotation for correct inference?

## Describe the bug

The `rotation` parameter (for SpinQuant/QuaRot preprocessing) is used during quantization but:
1. It is NOT saved to `quantize_config.json` when saving the model
2. It is NOT used in quantized layer's `forward` method during inference
3. This causes incorrect inference results (extremely high perplexity, e.g., PPL: 48564640.0)

## GPU Info

```
NVIDIA GeForce RTX 5090
CUDA Version: 13.0
Driver Version: 580.76.05
```

## Software Info

- OS: Linux 5.15.0-78-generic
- Python: 3.12.3
- gptqmodel: 5.6.12
- torch: 2.9.0
- transformers: 4.57.3
- accelerate: 1.12.0
- triton: 3.5.0

## quantize_config.json

```json
{
  "bits": 2,
  "group_size": 128,
  "desc_act": false,
  "sym": true,
  "quant_method": "gptq",
  "checkpoint_format": "gptq",
  "meta": {
    "gptaq": true,
    "gptaq_alpha": 0.25,
    "act_group_aware": true
  }
}
```

Note: The `rotation` field is missing, even though `rotation='hadamard'` was used during quantization.

## To Reproduce

1. Quantize a model with rotation:
```python
quant_config = QuantizeConfig(..., rotation='hadamard')
model = GPTQModel.from_pretrained(model_path, quantize_config=quant_config)
model.quantize(calibration_data)
model.save(quant_path)
```

2. Load for inference:
```python
model = GPTQModel.from_quantized(quant_path)
# Even manually setting rotation doesn't help:
# model.quantize_config.rotation = 'hadamard'
# Because quantized layer's forward() doesn't check this parameter
```

3. Result: Incorrect inference (PPL: 48564640.0 instead of normal values)

## Expected behavior

1. `rotation` parameter should be saved to `quantize_config.json`
2. Quantized layer's `forward` method should check and use `rotation` parameter
3. If rotation is set, apply inverse rotation during inference to restore correct outputs is reasonable

## Additional context

- Quantization works correctly (rotation is applied via `rotate_model()` in `base.py:586-610`)
- Issue is in inference: quantized layers (e.g., `TritonV2QuantLinear.forward`) don't apply inverse rotation
- Manual setting of `rotation` after loading doesn't help because `forward()` doesn't check it
- This appears to be incomplete implementation of rotation feature?



## 评论 (8)

### ZX-ModelCloud · 2026-01-19

Please provide a simple Python code to reproduce the issue.

### 12345txy · 2026-01-20

Hi, I'd like to provide more details about my issue with rotation quantization.

## Problem

I quantized Qwen3-8B model using GPTAQ + rotation, and when I evaluate the quantized model with standard loading procedure, I get extremely high perplexity (4000,000+), which suggests the rotation quantization logic may not be working correctly. Alternatively, I might be using the rotation parameter incorrectly.

## Minimal Reproduction Code

### Quantization Script

```python
from gptqmodel import GPTQModel, QuantizeConfig
from gptqmodel.quantization.config import METHOD, FORMAT
from transformers import AutoTokenizer
from datasets import load_dataset

model_path = "/path/to/Qwen3-8B-Base"
quant_path = "/path/to/Qwen3-8B-Rot-GPTAQ-2bit"

# Create config with rotation
quant_config = QuantizeConfig(
    bits=2,
    group_size=128,
    quant_method=METHOD.GPTQ,
    format=FORMAT.GPTQ,
    gptaq=True,
    gptaq_alpha=0.25,
    act_group_aware=True,
    rotation='hadamard',  # Enable rotation
    offload_to_disk=False,
    sym=True,
    desc_act=False,
)

# Load and quantize
model = GPTQModel.from_pretrained(
    model_path,
    quantize_config=quant_config,
    trust_remote_code=True
)

# Prepare calibration data
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
dataset = load_dataset("wikitext", "wikitext-2-raw-v1", split="train")
calibration_data = [tokenizer(item["text"], return_tensors="pt") for item in dataset[:512]]

# Quantize
model.quantize(calibration_data)
model.save(quant_path)
```

### Evaluation Script (Standard Loading)

```python
from gptqmodel import GPTQModel
from transformers import AutoTokenizer

# Standard loading - no special handling for rotation
model = GPTQModel.from_quantized(
    quant_path,
    device="cuda:0",
    trust_remote_code=True,
)

tokenizer = AutoTokenizer.from_pretrained(quant_path, trust_remote_code=True)

# Evaluate perplexity on wikitext test set
# Result: PPL = 48564640.0 (extremely high!)
```

## Expected vs Actual Behavior

- **Expected**: PPL should be reasonable (e.g., < 20, similar to non-rotation quantization)
- **Actual**: PPL = 4000,000+ (indicating incorrect inference)

## I Want to Know

1. Does the rotation function works correctly OR Is my usage of the `rotation` parameter correct for GPTAQ quantization?
2. Does rotation require any special handling during inference/loading?
3. Should `rotation` parameter be saved to `quantize_config.json` for proper inference?

Thanks!


### Qubitium · 2026-01-26

@12345txy  We have never tested or validated `rotation` for `gptaq` so we cannot attest to how it works in combination. @ZX-ModelCloud  did some tests and can provide some numbers.

### ZX-ModelCloud · 2026-01-26

I did some tests and found that `bits=2` has a significant impact on PPL (perplexity), while `rotation` has very little impact on PPL when `bits=4`.
You can try using `bits=4` instead of `bits=2`.

bits | group size | gptaq alpha | rotation | PPL
-- | -- | -- | -- | --
4 | 128 | 0.25 | None | 9.48
4 | 128 | 0.25 | Hadamard | 9.41
2 | 128 | 0.25 | None | 2707.45
2 | 128 | 0.25 | Hadamard | 3973.30

### 12345txy · 2026-01-26

Thank you for your tests! but I still have some questions concerning the test results you provide with.

Model & Consistency: First, **are you using the Qwen3-8B model?** Based on the single-digit PPL in your 4-bit tests, it seems you are using a smaller/standard model for validation. While my previous PPL was an extreme outlier (48564640.0), so I’m curious: **are your parameter settings and loading methods identical to the code I shared in the issue**? If they are, does this suggest that **my core implementation logic is actually correct**?

Rotation Anomaly: Theoretically, the purpose of rotation (e.g., Hadamard) is to smooth out outliers to facilitate better quantization. However, in your results, **the PPL actually increased (worsened) after applying rotation**, especially in the 2-bit case. This seems counter-intuitive. Do you think there might be an issue with the rotation implementation or its placement in the pipeline?

Looking forward to your reply!

### wangddcsu-ui · 2026-03-06

I have the same problem.

**Quantization Script：**
quantize_config = QuantizeConfig(
        bits=4,
        group_size = -1,
        sym = True,
        damp_percent=0.01,
        desc_act=False, 
        offload_to_disk=False, 
        rotation="hadamard",
        # rotation="random",
        act_group_aware=False,
        gptaq=GPTAQConfig(alpha=0.25, device="auto")
    )
model = GPTQModel.load(pretrained_model_id, 
        quantize_config,
        device="cuda",
        trust_remote_code=True,
        dtype=torch.bfloat16
        )
model.quantize(traindataset,batch_size=1,backend=BACKEND.TORCH)

**inference script：**
tokenizer = AutoTokenizer.from_pretrained(
        quantized_model_id, 
        use_fast=True,
        model_max_length=512,
        trust_remote_code=True,  
    )
    
    # 设置padding token（如果需要）
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    tokenizer.padding_side = 'left'  # 设置左填充
model = GPTQModel.load(quantized_model_id,backend=BACKEND.TORCH,device="cuda")
    # 测试推理
    print("\n测试推理...")
    test_input = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
    "请介绍下李白，使用中文回答",
]
    
    # 处理输入
    model_inputs = tokenizer(test_input, return_tensors="pt", padding=True, truncation=True,max_length=512).to(model.device)
    
    # 生成输出
    quant_generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=512,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id
    )
    
    # 解码所有生成的结果
    quant_generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, quant_generated_ids)
    ]

    # 批量解码所有生成的文本
    generated_texts = tokenizer.batch_decode(quant_generated_ids, skip_special_tokens=True)

    # 逐个打印每个输入和对应的输出
    for i, (input_text, generated_text) in enumerate(zip(test_input, generated_texts)):
        print(f"\n输入 {i+1}: {input_text}")
        print(f"生成结果: {generated_text}")


I used 4 bit quantization when configuring the rotation and gptaq quantization qwen2.5-7b model. The inference result still showed obvious garbled characters (I did not verify PPL). The accuracy of the mmlu data set was only 0.2279.
 (Evaluation Results)
=========================gptaq+rotation=======================================
|Tasks|Version|Filter|n-shot|Metric|   |Value |   |Stderr|
|-----|-------|------|-----:|------|---|-----:|---|-----:|
|mmlu |Yaml   |none  |     0|acc   |↑  |0.2279|±  |0.0035|

However, when rotation and gptq are used, the precision is not obviously decreased and the inference result is normal. The precision is as follows:
 (Evaluation Results)
=======================gptq+rotation==========================================
|Tasks|Version|Filter|n-shot|Metric|   |Value |   |Stderr|
|-----|-------|------|-----:|------|---|-----:|---|-----:|
|mmlu |Yaml   |none  |     0|acc   |↑  |0.6864|±  |0.0039|

At present, the above inference script is used. The inference result is obviously abnormal, as shown below:
输入 1: Hello, my name is
生成结果:  Dacerb, and I am a senior.  I.ElementAtSingleOrDefault espos STILL   SingleOrDefault thems        HOWEVER0 PLEASE mingle HOWEVER TAKE (    �\views   ActivityIndicator   * [-make #  # brag junge [0,沮, by    ( (   NotSupportedException, as#; **#7 \微信号但不限 Asus# STILL主营_nums万余性价,Remote
呶 ASUS关于我们 TelerikOUCH人体原文地址 _复工复女性朋友def05性价,OUCH性价RequestParam,<性价 * (4 # �ORB HOWEVER性价,2\n性价 in! * forWR for性价, maç复工复为抓\n    (` junge (性价.'icon性价\n,女性朋友探踵性价 ( (女性朋友呶性价-

I use the qwen3-8b model for rotation and gptaq quantification, and the precision decreases a lot, although it is not as obvious as qwen2.5-7b:

评估结果 (Evaluation Results)
========================gptaq+rotation=========================================
|Tasks|Version|Filter|n-shot|Metric|   |Value |   |Stderr|
|-----|-------|------|-----:|------|---|-----:|---|-----:|
|mmlu |Yaml   |none  |     0|acc   |↑  |0.5012|±  |0.0042|

评估结果 (Evaluation Results)
=======================Original Model============================================
|Tasks|Version|Filter|n-shot|Metric|   |Value|   |Stderr|
|-----|-------|------|-----:|------|---|----:|---|-----:|
|mmlu |Yaml   |none  |     0|acc   |↑  |0.674|±  | 0.004|

My question is, does the gptaq quantitative model need additional parameter configuration during inference?

### wangddcsu-ui · 2026-03-06

Only gptaq is used for quantization. rotation is not enabled, the quantitative qwen2.5-7b model is still unavailable. The accuracy of mmlu data set inference is as follows:
 (Evaluation Results)
======================================================================
|Tasks|Version|Filter|n-shot|Metric|   |Value |   |Stderr|
|-----|-------|------|-----:|------|---|-----:|---|-----:|
|mmlu |Yaml   |none  |     0|acc   |↑  |0.2661|±  |0.0037|


### Qubitium · 2026-07-25

@12345txy  Fixed in https://github.com/ModelCloud/GPTQModel/pull/2980
