# [Issue #4567] [Bug] requirements for the version of torch and triton

source: https://github.com/InternLM/lmdeploy/issues/4567
state: closed | updated: 2026-05-27T05:54:27Z
labels: awaiting response, Stale

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

请问下，lmdeploy==0.12.3对torch和triton的版本有什么要求吗？
我用的是python=3.10.13，torch==2.6.0，triton==3.2.0报了这个错误

ray::RayWorkerWrapper.warmup() (pid=2431, ip=10.62.192.74, actor_id=bf0acbb5f97bd996cbd8448b01000000, repr=<lmdeploy.pytorch.engine.executor.ray_executor.RayWorkerWrapper object at 0x7f8235cdd2d0>)
  File "/usr/local/lib/python3.10/concurrent/futures/_base.py", line 451, in result
    return self.__get_result()
  File "/usr/local/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
    raise self._exception
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/engine/executor/base_worker.py", line 120, in warmup
    self.model_agent.warmup()
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/engine/model_agent/agent.py", line 485, in warmup
    self._forward_impl(inputs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/engine/model_agent/agent.py", line 1132, in _forward_impl
    output = model_forward(
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/engine/model_agent/agent.py", line 184, in model_forward
    output = model(**input_dict)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/backends/cuda/graph_runner.py", line 235, in __call__
    output = self.model(**kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/models/qwen3_5.py", line 1143, in forward
    hidden_states, target_inputs_embeds = self.model(
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/models/qwen3_5.py", line 1059, in forward
    hidden_states = self.language_model(
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/models/qwen3_5.py", line 975, in forward
    hidden_states, residual = decoder_layer(
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/models/qwen3_5.py", line 804, in forward
    hidden_states = self.mlp(hidden_states, all_routed_experts=all_routed_experts)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/models/qwen3_5_moe.py", line 113, in forward
    out_states = self.experts(
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/nn/moe/base.py", line 317, in forward
    return self.forward_default(hidden_states, topk_weights, topk_idx)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/nn/moe/base.py", line 308, in forward_default
    gemm_state = self.gemm(recv_state)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/nn/moe/default.py", line 302, in gemm
    hidden_states = self.impl.forward(hidden_states,
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/backends/cuda/moe/default.py", line 58, in forward
    return fused_moe(hidden_states,
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/kernels/cuda/fused_moe.py", line 598, in fused_moe
    ret = moe_reduce(intermediate_cache2, topk_weights)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/lmdeploy/pytorch/kernels/cuda/fused_moe.py", line 504, in moe_reduce
    _moe_reduce_kernel[grid](
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/triton/runtime/jit.py", line 330, in <lambda>
    return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/triton/runtime/jit.py", line 626, in run
    kernel = self.compile(
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/triton/compiler/compiler.py", line 273, in compile
    module = src.make_ir(options, codegen_fns, module_map, context)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/triton/compiler/compiler.py", line 100, in make_ir
    return ast_to_ttir(self.fn, self, context=context, options=options, codegen_fns=codegen_fns,
triton.compiler.errors.CompilationError: at 43:8:

    h = tl.load(h_ptrs, mask=mask_h, other=0.0)
    w = tl.load(weights_ptrs, mask=mask_k, other=0.0)

    if fp32_acc:
        h = h.to(tl.float32)
        w = w.to(tl.float32)
    else:
        w = w.to(h.dtype)

    wh = h * w[:, None]
    o = wh.sum(axis=0)
        ^
2026-05-06 11:03:10,805 ERROR worker.py:438 -- Unhandled error (suppress with 'RAY_IGNORE_UNHANDLED_ERRORS=1'): ray::RayWorkerWrapper.warmup() (pid=2432, ip=10.62.192.74, actor_id=96abbf61a6d8a7d8a183ae6301000000, repr=<lmdeploy.pytorch.engine.executor.ray_executor.RayWorkerWrapper object at 0x7fdafc5bd330>)
  File "/home/yexun.zhang/code/mlm-data/venv/lib/python3.10/site-packages/triton/runtime/jit.py", line 770, in __call__
    raise RuntimeError("Cannot call @triton.jit'd outside of the scope of a kernel")
RuntimeError: Cannot call @triton.jit'd outside of the scope of a kernel

### Reproduction

lmdeploy serve api_server /home/yexun.zhang/pretrained_models/Qwen3.5-122B-A10B --server-port 23333 --tp 8  --cache-max-entry-count 0.75 --backend pytorch


### Environment

```Shell
python：3.10.13
torch：2.6.0
triton:  3.2.0
sdk版本：1.7.0-84b81c
cuda：Cuda compilation tools, release 12.4, V12.4.1
lmdeploy: 0.12.3
命令：lmdeploy serve api_server /home/yexun.zhang/pretrained_models/Qwen3.5-122B-A10B --server-port 23333 --tp 8  --cache-max-entry-count 0.75 --backend pytorch
模型：Qwen3.5-122B-A10B
```

### Error traceback

```Shell

```

## 评论 (6)

### lvhan028 · 2026-05-06

torch: 2.10.0
triton: 3.6.0

### zhangyexun · 2026-05-06

> torch: 2.10.0 triton: 3.6.0
好的，感谢，对cuda的版本有要求吗？cuda12.4可以吗？



### github-actions[bot] · 2026-05-14

This issue is marked as stale because it has been marked as invalid or awaiting response for 7 days without any further response. It will be closed in 5 days if the stale label is not removed or if there is no further response.

### lvhan028 · 2026-05-14

> > torch: 2.10.0 triton: 3.6.0
> > 好的，感谢，对cuda的版本有要求吗？cuda12.4可以吗？

最好是 cu12.8

### github-actions[bot] · 2026-05-22

This issue is marked as stale because it has been marked as invalid or awaiting response for 7 days without any further response. It will be closed in 5 days if the stale label is not removed or if there is no further response.

### github-actions[bot] · 2026-05-27

This issue is closed because it has been stale for 5 days. Please open a new issue if you have similar issues or you have any new updates now.
