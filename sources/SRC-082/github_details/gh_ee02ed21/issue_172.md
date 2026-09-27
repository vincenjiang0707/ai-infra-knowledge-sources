# [Issue #172] can awq support 3-bit,2-bit, 8-bit quantization?

source: https://github.com/mit-han-lab/llm-awq/issues/172
state: open | updated: 2026-03-02T13:16:13Z
labels: 

## 正文

i see now awq only support 4-bit quantization, can it supports 2-bit,3-bit, 8-bit quantization?

## 评论 (4)

### NamburiSrinath · 2024-09-23

Hi @GilesBathgate , @ArlanCooper 

Is there an update regarding this? Does AWQ support any other config other than 4 bit?

I tried running with 3 bit but got this error

```
Traceback (most recent call last):
  File "/home/ubuntu/Compress_Align/compress_models_awq.py", line 18, in <module>
    model.quantize(tokenizer, quant_config=quant_config)
  File "/home/ubuntu/anaconda3/envs/compress_align/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/anaconda3/envs/compress_align/lib/python3.9/site-packages/awq/models/base.py", line 231, in quantize
    self.quantizer.quantize()
  File "/home/ubuntu/anaconda3/envs/compress_align/lib/python3.9/site-packages/awq/quantize/quantizer.py", line 187, in quantize
    self._apply_quant(self.modules[i], named_linears)
  File "/home/ubuntu/anaconda3/envs/compress_align/lib/python3.9/site-packages/awq/quantize/quantizer.py", line 227, in _apply_quant
    q_linear = q_linear_module.from_linear(
  File "/home/ubuntu/anaconda3/envs/compress_align/lib/python3.9/site-packages/awq/modules/linear/gemm.py", line 145, in from_linear
    awq_linear = cls(
  File "/home/ubuntu/anaconda3/envs/compress_align/lib/python3.9/site-packages/awq/modules/linear/gemm.py", line 93, in __init__
    raise NotImplementedError("Only 4-bit are supported for now.")
```

### schnell18 · 2024-11-03

It seems odd. [The original paper][1] did mention 3 bit was experimented:

> PPL is measured with OPT-6.7B under INT3-g128 quantization.

Try alternatives such as HQQ and GPTQ, they are solid as well. HQQ performs better on the 3-bit range and can quantize model really fast.

[1]: https://arxiv.org/abs/2306.00978v2

### ArlanCooper · 2025-11-03

1

### madhav120ai · 2026-03-02

any updates? 
