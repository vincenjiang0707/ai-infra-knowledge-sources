# [Issue #1465] [Ascend][Bug] Fail to use 4-bit quant model to inference

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1465
state: closed | updated: 2026-02-21T20:27:32Z
labels: Ascend NPU

## 正文

### System Info

- Ascend Atals 300T A2 Training Card
- py3.9
- torch 2.5.1
- torch-npu 2.5.1rc1

### Reproduction

### Detailed Description
The shape of tensors inputed to `matmul` don't match when directly use the following script to inference.

```
Unused kwargs: ['_load_in_4bit', '_load_in_8bit', 'quant_method']. These kwargs are not used in <class 'transformers.utils.quantization_config.BitsAndBytesConfig'>.
`low_cpu_mem_usage` was None, now default to True since model is quantized.
/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/torch_npu/utils/storage.py:38: UserWarning: TypedStorage is deprecated. It will be removed in the future and UntypedStorage will be the only storage class. This should only matter to you if you are using storages directly.  To access UntypedStorage directly, use tensor.untyped_storage() instead of tensor.storage()
  if self.device.type != 'cpu':
Some parameters are on the meta device because they were offloaded to the cpu.
Unused kwargs: ['_load_in_4bit', '_load_in_8bit', 'quant_method']. These kwargs are not used in <class 'transformers.utils.quantization_config.BitsAndBytesConfig'>.
/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/transformers/quantizers/auto.py:186: UserWarning: You passed `quantization_config` or equivalent parameters to `from_pretrained` but the model you're loading already has a `quantization_config` attribute. The `quantization_config` from the model will be used.
  warnings.warn(warning_msg)
[W1228 09:52:30.391621427 compiler_depend.ts:659] Warning: 0Failed to find function aclrtSynchronizeDeviceWithTimeout (function operator())
You shouldn't move a model that is dispatched using accelerate hooks.
Traceback (most recent call last):
  File "/home/cmq/code/vllm/z-run-scripts/bnb.py", line 192, in <module>
    output = model.generate(input_ids, max_length=100, num_return_sequences=1)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/transformers/generation/utils.py", line 2252, in generate
    result = self._sample(
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/transformers/generation/utils.py", line 3251, in _sample
    outputs = self(**model_inputs, return_dict=True)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/accelerate/hooks.py", line 170, in new_forward
    output = module._old_forward(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/transformers/models/llama/modeling_llama.py", line 1163, in forward
    outputs = self.model(
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/accelerate/hooks.py", line 170, in new_forward
    output = module._old_forward(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/transformers/models/llama/modeling_llama.py", line 913, in forward
    layer_outputs = decoder_layer(
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/accelerate/hooks.py", line 170, in new_forward
    output = module._old_forward(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/transformers/models/llama/modeling_llama.py", line 640, in forward
    hidden_states, self_attn_weights, present_key_value = self.self_attn(
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/accelerate/hooks.py", line 170, in new_forward
    output = module._old_forward(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/transformers/models/llama/modeling_llama.py", line 523, in forward
    key_states = self.k_proj(hidden_states)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/accelerate/hooks.py", line 170, in new_forward
    output = module._old_forward(*args, **kwargs)
  File "/home/cmq/code/bitsandbytes/bitsandbytes/nn/modules.py", line 518, in forward
    out = bnb.matmul_4bit(x, weight, bias=bias, quant_state=self.weight.quant_state)
  File "/home/cmq/code/bitsandbytes/bitsandbytes/autograd/_functions.py", line 611, in matmul_4bit
    return MatMul4Bit.apply(A, B, out, bias, quant_state)
  File "/home/cmq/miniconda3/envs/vllm_torch25/lib/python3.9/site-packages/torch/autograd/function.py", line 575, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
  File "/home/cmq/code/bitsandbytes/bitsandbytes/autograd/_functions.py", line 524, in forward
    output = torch.matmul(A, F.dequantize_4bit(B, quant_state).to(A.dtype).t())
RuntimeError: call aclnnMatmul failed, detail:EZ1001: [PID: 4184975] 2024-12-28-09:52:34.435.298 The k-axis of the two inputs are different [1,5,4096], [1024,4096]

[ERROR] 2024-12-28-09:52:34 (PID:4184975, Device:0, RankID:-1) ERR01100 OPS call acl api failed
```

And I tried to fix this by the following 2 methods:

**1. directly use linear func**
```diff
--- a/bitsandbytes/autograd/_functions.py
+++ b/bitsandbytes/autograd/_functions.py
@@ -519,12 +519,12 @@ class MatMul4Bit(torch.autograd.Function):
 
         # 1. Dequantize
         # 2. MatmulnN
-        if A.device.type == "npu":
-            output = torch.matmul(A, F.dequantize_4bit(B, quant_state).to(A.dtype).t())
-            if bias is not None:
-                output += bias
-        else:
-            output = torch.nn.functional.linear(A, F.dequantize_4bit(B, quant_state).to(A.dtype).t(), bias)
+        # if A.device.type == "npu":
+        #     output = torch.matmul(A, F.dequantize_4bit(B, quant_state).to(A.dtype).t())
+        #     if bias is not None:
+        #         output += bias
+        # else:
+        output = torch.nn.functional.linear(A, F.dequantize_4bit(B, quant_state).to(A.dtype).t(), bias)
```
**2. del the transpose op**

```diff
--- a/bitsandbytes/autograd/_functions.py
+++ b/bitsandbytes/autograd/_functions.py
@@ -520,7 +520,7 @@ class MatMul4Bit(torch.autograd.Function):
         # 1. Dequantize
         # 2. MatmulnN
         if A.device.type == "npu":
-            output = torch.matmul(A, F.dequantize_4bit(B, quant_state).to(A.dtype).t())
+            output = torch.matmul(A, F.dequantize_4bit(B, quant_state).to(A.dtype))
             if bias is not None:
                 output += bias
         else:
```

 **The Results**
The error above is fixed, but the inference result is meaningless:
![image](https://github.com/user-attachments/assets/e16e8894-a851-43f9-a5e7-625a2700b94a)


### Reproduction Example
There is an example to load 4-bit quant model to inference:

```python

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import bitsandbytes as bnb
from accelerate import init_empty_weights

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True, load_in_8bit=False, bnb_4bit_quant_type="nf4",
)
tokenizer = AutoTokenizer.from_pretrained("unsloth/llama-3-8b-bnb-4bit", use_fast=False)

model = AutoModelForCausalLM.from_pretrained(
    "unsloth/llama-3-8b-bnb-4bit",
    quantization_config=bnb_config,
    device_map="npu:0",
    trust_remote_code=True,
    torch_dtype=torch.float16,
    # use_auth_token=script_args.use_auth_token,
)

# input prompt
input_text = "tell me a story"
input_ids = tokenizer.encode(input_text, return_tensors='pt').to("npu")

# do inference
with torch.no_grad():
    output = model.generate(input_ids, max_length=100, num_return_sequences=1)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
```

### Expected behavior

Inference with a correct result.

## 评论 (2)

### MengqingCao · 2024-12-28

cc @kashif @statelesshz 

### TimDettmers · 2026-02-21

Closing this issue due to no follow-up for over a year. The Ascend NPU backend is being actively developed in PR #1695, which introduces custom ops integration for NF4 support on Ascend. The shape mismatch you encountered may be addressed by that work.

If you're still hitting issues after the Ascend backend PR lands, please open a new issue with updated environment details and reproduction steps.
