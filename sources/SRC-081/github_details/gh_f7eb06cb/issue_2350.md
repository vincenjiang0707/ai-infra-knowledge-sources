# [Issue #2350] [BUG] Zero Point Calculation Error in `unpack_reorder_pack` for ExLlamaV2 AWQ Asymmetric Quantization

source: https://github.com/ModelCloud/GPTQModel/issues/2350
state: closed | updated: 2026-01-12T03:43:25Z
labels: bug

## 正文

# Zero Point Calculation Error in `unpack_reorder_pack` for ExLlamaV2 AWQ Asymmetric Quantization
### **PR**: [#2351](https://github.com/ModelCloud/gptqmodel/pull/2351)

## Describe the bug

When using ExLlamaV2 kernel (`AwqExllamaV2QuantLinear`) with AWQ asymmetric quantization (`sym=False`), the `unpack_reorder_pack` function incorrectly handles zero_point values of 0. The operation `izeros = izeros - 1` causes zero_point values of 0 to become -1, which are then incorrectly packed as 15. This leads to:

1. **Incorrect zero_point values**: 57,276 zero_point values (from 48 layers) are incorrectly changed from 0 to 15
2. **Wrong dequantization**: Incorrect zero_point causes weight dequantization errors (`weight = (qweight - zero_point) * scale`)
3. **NaN in logits**: Wrong weights lead to NaN or Inf values in model outputs
4. **NaN in PPL calculation**: NaN logits propagate to loss and perplexity calculations, resulting in `PPL = NaN`

## GPU Info

```
NVIDIA GeForce RTX 5090
Driver Version: 580.76.05
CUDA Version: 13.0
```

## Software Info

**Operation System/Version**: Linux 5.15.0-78-generic

**Python Version**: Python 3.12

**Package Versions**:
```
Name: GPTQModel
Version: 5.6.12

Name: torch
Version: 2.9.0

Name: transformers
Version: 4.57.3

Name: accelerate
Version: 1.12.0

Name: triton
Version: 3.5.0
```

## Model/Datasets

**Model**: Qwen3-8B-AWQ (asymmetric quantization)

**config.json** (relevant parts):
```json
{
  "architectures": ["Qwen3ForCausalLM"],
  "hidden_size": 4096,
  "intermediate_size": 12288,
  "num_hidden_layers": 36,
  "vocab_size": 151936
}
```

**quantize_config.json**:
```json
{
  "bits": 4,
  "group_size": 128,
  "desc_act": true,
  "sym": false,
  "quant_method": "awq",
  "checkpoint_format": "gemm",
  "pack_dtype": "int32",
  "zero_point": true,
  "version": "gemm",
  "format": "gemm"
}
```

## To Reproduce

1. **Quantize a model with AWQ asymmetric quantization**:
```python
from gptqmodel import GPTQModel, QuantizeConfig
from gptqmodel.quantization.config import METHOD, FORMAT

quant_config = QuantizeConfig(
    bits=4,
    group_size=128,
    quant_method=METHOD.AWQ,
    format=FORMAT.LLM_AWQ,
    sym=False,  # Asymmetric quantization
)

model = GPTQModel.from_pretrained(
    "model_path",
    quantize_config=quant_config,
)
model.quantize(calibration_dataset)
model.save("quantized_model_path")
```

2. **Load the model with ExLlamaV2 kernel** (auto-selected if available):
```python
from gptqmodel import GPTQModel

model = GPTQModel.from_quantized(
    "quantized_model_path",
    device="cuda:0",
    trust_remote_code=True,
    # ExLlamaV2 will be auto-selected if available
)
```

3. **Run perplexity evaluation**:
```python
# Run perplexity evaluation
# PPL will be NaN due to incorrect zero_point values
```

4. **Verify the issue**:
```python
# Check qzeros values in the model
from safetensors.torch import load_file
import json
import torch

index_path = "quantized_model_path/model.safetensors.index.json"
with open(index_path, 'r') as f:
    index = json.load(f)

# Load a qzeros tensor and check for zero values
for shard_file in set(index['weight_map'].values()):
    shard_data = load_file(f"quantized_model_path/{shard_file}")
    for key, qzeros in shard_data.items():
        if 'qzeros' in key:
            from gptqmodel.quantization.awq.utils.packing_utils import unpack_awq, reverse_awq_order
            iweight, izeros = unpack_awq(torch.zeros_like(qzeros), qzeros, 4)
            iweight, izeros = reverse_awq_order(iweight, izeros, 4)
            izeros = torch.bitwise_and(izeros, 15)
            
            zero_count = (izeros == 0).sum().item()
            if zero_count > 0:
                print(f"Layer {key}: {zero_count} zero_point values of 0")
                # These will be incorrectly processed as -1 → 15 in unpack_reorder_pack
```

## Expected behavior

1. Zero_point values of 0 should remain 0 after `unpack_reorder_pack`
2. Dequantization should use correct zero_point values
3. Model outputs should not contain NaN or Inf
4. PPL calculation should produce valid results

## Actual behavior

1. Zero_point values of 0 are incorrectly changed to 15
2. Dequantization uses wrong zero_point, causing weight errors
3. Model outputs contain NaN or Inf
4. PPL calculation results in NaN

## Root Cause

In `gptqmodel/quantization/awq/utils/packing_utils.py`, line 85:

```python
def unpack_reorder_pack(qweight, qzeros, bits):
    # ... unpack and reorder operations ...
    izeros = torch.bitwise_and(izeros, (2**bits) - 1)
    
    # Subtract 1 from the izeros tensor (exllama adds 1 during inference)
    izeros = izeros - 1  # ❌ BUG: When izeros=0, this becomes -1
    # Pack the qweight and qzeros tensors
    qweight, qzeros = pack_exllama(iweight, izeros, bits)
```

**The Problem**:
- When `izeros=0` (which occurs in 48 layers with 57,276 values), subtracting 1 results in `-1`
- The negative value `-1` (0xFFFFFFFF) is incorrectly handled in `pack_exllama`:
  - When taking the lower 4 bits, `-1 & 0xF = 15` (0xF)
  - This causes zero_point to incorrectly change from 0 to 15
- The incorrect zero_point leads to wrong dequantization: `weight = (qweight - zero_point) * scale`
- When `qweight < zero_point_wrong`, weights become negative or extremely small
- This propagates through the model, causing NaN/Inf in logits and loss

**Causal Chain**:
```
izeros - 1 (when izeros=0) 
→ -1 (negative value) 
→ pack_exllama incorrectly processes as 15 
→ zero_point changes from 0 to 15 
→ wrong dequantization 
→ wrong weights 
→ NaN/Inf in logits 
→ NaN in loss 
→ NaN in PPL
```

## Proposed Fix

Replace line 85 in `gptqmodel/quantization/awq/utils/packing_utils.py`:

**Before**:
```python
izeros = izeros - 1  # exllama adds 1 during inference
```

**After**:
```python
# Fix: Avoid negative values when izeros=0
# When izeros=0, subtracting 1 would result in -1, which is incorrectly
# packed as 15 in pack_exllama, causing zero_point calculation errors.
# Only subtract 1 when izeros > 0 to avoid this issue.
izeros = torch.where(izeros > 0, izeros - 1, izeros)
```

**Alternative fix** (using clamp):
```python
izeros = torch.clamp(izeros - 1, min=0)
```

## Impact

- **Affected layers**: 48 layers with 57,276 incorrect zero_point values
- **Severity**: High - causes complete failure of inference/evaluation
- **Affected kernels**: Only ExLlamaV2 kernel (GEMM and other kernels are not affected)
- **Affected quantization**: Only asymmetric AWQ quantization (`sym=False`)

## Code Location

- **File**: `gptqmodel/quantization/awq/utils/packing_utils.py`
- **Function**: `unpack_reorder_pack()`
- **Line**: 85
- **Called from**: `gptqmodel/nn_modules/qlinear/exllamav2_awq.py:97` in `post_init()`

## Additional context

- This bug only affects ExLlamaV2 kernel with asymmetric AWQ quantization
- The issue was discovered when evaluating perplexity, which resulted in NaN
- After applying the fix, zero_point values are correctly preserved and PPL calculation works correctly, I can summit a PR if needed


## 评论 (1)

### Qubitium · 2026-01-12

Confirmed fix. We are checking results.
