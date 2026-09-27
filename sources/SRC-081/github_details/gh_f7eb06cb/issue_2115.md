# [Issue #2115] Moe-vram for QQQ

source: https://github.com/ModelCloud/GPTQModel/issues/2115
state: closed | updated: 2026-07-25T07:04:50Z
labels: performance

## 正文

`balanced` mode does not work with GLM-4.5-Air and QQQ method, tried on 4 x 3090:
```
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 1156, in loop
    return self._loop_impl(fail_safe=fail_safe, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 1497, in _loop_impl
    forward_outputs = self._run_forward_batches(
        module=module,
    ...<17 lines>...
        preserve_module_devices=preserve_devices,
    )
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 526, in _run_forward_batches
    return self._run_forward_batches_single(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        module=module,
        ^^^^^^^^^^^^^^
    ...<16 lines>...
        preserve_module_devices=preserve_module_devices,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 674, in _run_forward_batches_single
    module_output = module(*layer_input, **additional_inputs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/transformers/modeling_layers.py", line 94, in __call__
    return super().__call__(*args, **kwargs)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/transformers/models/glm4_moe/modeling_glm4_moe.py", line 395, in forward
    hidden_states = self.mlp(hidden_states)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/transformers/models/glm4_moe/modeling_glm4_moe.py", line 345, in forward
    hidden_states = self.moe(hidden_states, topk_indices, topk_weights).view(*orig_shape)
                    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/transformers/models/glm4_moe/modeling_glm4_moe.py", line 331, in moe
    expert_output = expert(expert_input)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/transformers/models/glm4_moe/modeling_glm4_moe.py", line 223, in forward
    down_proj = self.down_proj(self.act_fn(self.gate_proj(x)) * self.up_proj(x))
                                           ~~~~~~~~~~~~~~^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/nn_modules/hooked_linear.py", line 239, in forward
    self.forward_hook(self, (input,), output)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 954, in hook
    return inner_hook(module, new_inputs, new_output)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/qqq_processor.py", line 100, in tmp
    q.add_batch(inp[0].data, out.data)  # noqa: F821
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/quantization/qqq.py", line 290, in add_batch
    self.H += inp.matmul(inp.t())
RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cuda:1!
```

--- update:
looks like vllm does not support `qqq` right now

## 评论 (1)

### Qubitium · 2026-04-13

@avtc  vllm dropped qqq support due to few people using it. We will continue to support it as to preserve search value for future reference. 
