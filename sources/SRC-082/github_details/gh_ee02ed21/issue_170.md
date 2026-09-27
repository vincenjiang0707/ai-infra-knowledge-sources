# [Issue #170] illegal memory access when input tokens < 8

source: https://github.com/mit-han-lab/llm-awq/issues/170
state: open | updated: 2026-07-16T15:31:01Z
labels: 

## 正文

Hi @ys-2020, thanks for your engineering work on the new kernels. I was made aware of a bug recently after importing the new GEMV/GEMM kernels into AutoAWQ. The issue specifically occurs on the GEMV kernel.

Conditions to trigger the bug:
- disable fused modules
- use huggingface/vllm implementation
- pass in less than 8 input tokens

## Import into vLLM

The same illegal memory access occurs when trying to [import it to vLLM](https://github.com/vllm-project/vllm/compare/main...neuralmagic:nm-vllm:awq_faster_kernel).

## Workaround

I found a workaround that seems to allow us to use the GEMV kernel, but without triggering the illegal memory access. However, I wanted to post here to get your thoughts on this fix and if you can identify what the issue is with the imported kernels from TensorRT.

Replace this:

https://github.com/mit-han-lab/llm-awq/blob/5f06dbbed109f05b4a8e50556fbcf5115652ed85/awq/quantize/qmodule.py#L203

With:

```python
batch_size, n_tokens, _ = inputs.shape
if batch_size < 8 and n_tokens == 1:
```

## Traceback

```
Traceback (most recent call last):
  File "/workspace/AutoAWQ/examples/generate.py", line 25, in <module>
    generation_output = model.generate(
  File "/workspace/AutoAWQ/awq/models/base.py", line 111, in generate
    return self.model.generate(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/generation/utils.py", line 1544, in generate
    return self.greedy_search(
  File "/usr/local/lib/python3.10/dist-packages/transformers/generation/utils.py", line 2404, in greedy_search
    outputs = self(
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/mistral/modeling_mistral.py", line 1157, in forward
    outputs = self.model(
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/mistral/modeling_mistral.py", line 1042, in forward
    layer_outputs = decoder_layer(
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/mistral/modeling_mistral.py", line 757, in forward
    hidden_states, self_attn_weights, present_key_value = self.self_attn(
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/mistral/modeling_mistral.py", line 666, in forward
    query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin, position_ids)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/mistral/modeling_mistral.py", line 160, in apply_rotary_pos_emb
    cos = cos[position_ids].unsqueeze(unsqueeze_dim)
RuntimeError: CUDA error: an illegal memory access was encountered
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```

CC @robertgshaw2-neuralmagic

## 评论 (2)

### Chessing234 · 2026-07-16

Fixed in #330 — GEMV only when `n_tokens == 1` (short prefill uses GEMM).

### Chessing234 · 2026-07-16

Fused MLP path fixed in #331 (same decode-only GEMV dispatch as #330).
