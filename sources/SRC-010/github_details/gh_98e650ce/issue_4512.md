# [Issue #4512] [Bug] qwen3.5推理TileLang依赖报错

source: https://github.com/InternLM/lmdeploy/issues/4512
state: closed | updated: 2026-04-09T10:45:01Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

 使用最新版lmdeploy docker v0.12.3推理Qwen/Qwen3.5-35B-A3B报错，与TileLang相关。

### Reproduction

root@xxxx:/# lmdeploy serve api_server Qwen/Qwen3.5-35B-A3B --server-port 10236 --backend pytorch --tool-call-parser qwen3
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3.5-35B-A3B
2026-04-09 01:35:32,628 - modelscope - INFO - Target directory already exists, skipping creation.
2026-04-09 01:35:48,424 - lmdeploy - WARNING - transformers.py:22 - LMDeploy requires transformers version: [4.33.0 ~ 5.3.0], but found version: 5.5.0
Loading weights from safetensors: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:14<00:00,  1.07s/it]
2026-04-09 01:36:14  [TileLang:tilelang.jit.kernel:INFO]: TileLang begins to compile kernel `causal_conv1d_fwd_main` with `out_idx=None`
Process mp_engine_proc:
Traceback (most recent call last):
  File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/engine/mp_engine/zmq_engine.py", line 109, in _mp_proc
    engine = Engine.from_pretrained(
             ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/engine/engine.py", line 232, in from_pretrained
    return cls(
           ^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/engine/engine.py", line 151, in __init__
    self.executor.init()
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/engine/executor/base.py", line 255, in init
    self.warmup()
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/engine/executor/uni_executor.py", line 82, in warmup
    self.model_agent.warmup()
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/engine/model_agent/agent.py", line 485, in warmup
    self._forward_impl(inputs)
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/engine/model_agent/agent.py", line 1132, in _forward_impl
    output = model_forward(
             ^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/engine/model_agent/agent.py", line 184, in model_forward
    output = model(**input_dict)
             ^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/backends/cuda/graph_runner.py", line 235, in __call__
    output = self.model(**kwargs)
             ^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1787, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/models/qwen3_5.py", line 1143, in forward
    hidden_states, target_inputs_embeds = self.model(
                                          ^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1787, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/models/qwen3_5.py", line 1059, in forward
    hidden_states = self.language_model(
                    ^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1787, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/models/qwen3_5.py", line 975, in forward
    hidden_states, residual = decoder_layer(
                              ^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1787, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/models/qwen3_5.py", line 789, in forward
    hidden_states = self.linear_attn(
                    ^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1787, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/models/qwen3_5.py", line 552, in forward
    mixed_qkv, conv_state = self.conv1d(mixed_qkv, conv_state, gated_delta_meta=gated_delta_meta)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1787, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/nn/gated_delta.py", line 330, in forward
    return self.causal_conv1d_func(x, self.weight, self.bias, conv_state, gated_delta_meta=gated_delta_meta)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/contextlib.py", line 81, in inner
    return func(*args, **kwds)
           ^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/nn/gated_delta.py", line 190, in __call__
    return self.conv1d_func(x, weight, bias, conv_state, gated_delta_meta=gated_delta_meta)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/nn/gated_delta.py", line 129, in conv1d_func
    out = self.causal_conv1d_fn(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/backends/cuda/causal_conv1d.py", line 26, in conv1d_fn
    return self.causal_conv1d_fn(x,
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/pytorch/kernels/cuda/causal_conv1d.py", line 195, in causal_conv1d_fn
    kernel = causal_conv1d_fwd(hidden_size, kernel_size, bias is not None, activation, dtype, x.stride(2),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/tilelang/jit/__init__.py", line 440, in __call__
    kernel = self.compile(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/tilelang/jit/__init__.py", line 375, in compile
    kernel_result = compile(
                    ^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/tilelang/jit/__init__.py", line 98, in compile
    return cached(
           ^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/tilelang/cache/__init__.py", line 74, in cached
    return _dispatch_map[execution_backend].cached(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/tilelang/cache/kernel_cache.py", line 264, in cached
    kernel = JITKernel(
             ^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/tilelang/jit/kernel.py", line 137, in __init__
    adapter = self._compile_and_create_adapter(func, out_idx)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/tilelang/jit/kernel.py", line 241, in _compile_and_create_adapter
    artifact = tilelang.lower(
               ^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/tilelang/engine/lower.py", line 246, in lower
    PreLowerSemanticCheck(mod)
  File "/opt/py3/lib/python3.12/site-packages/tilelang/engine/phase.py", line 132, in PreLowerSemanticCheck
    tilelang.analysis.NestedLoopChecker()(mod)
  File "/opt/py3/lib/python3.12/site-packages/tilelang/3rdparty/tvm/python/tvm/ir/transform.py", line 167, in __call__
    return _ffi_transform_api.RunPass(self, mod)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "python/tvm_ffi/cython/function.pxi", line 929, in tvm_ffi.core.Function.__call__
  File "<unknown>", line 0, in tvm::transform::Pass::operator()(tvm::IRModule) const
  File "<unknown>", line 0, in tvm::transform::Pass::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  File "<unknown>", line 0, in tvm::tir::transform::PrimFuncPassNode::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  File "python/tvm_ffi/cython/function.pxi", line 1083, in tvm_ffi.core.tvm_ffi_callback
  File "/opt/py3/lib/python3.12/site-packages/tilelang/analysis/nested_loop_checker.py", line 116, in pass_fn
    _NestedLoopCheckVisitor().visit_stmt(func.body)

  File "/opt/py3/lib/python3.12/site-packages/tilelang/3rdparty/tvm/python/tvm/runtime/support.py", line 159, in __init__
    self._inst = cls(*args, **kwargs)

  File "/opt/py3/lib/python3.12/site-packages/tilelang/3rdparty/tvm/python/tvm/runtime/support.py", line 197, in __setattr__
    super(TVMDerivedObject, self).__setattr__(name, value)

AttributeError: '_NestedLoopCheckVisitor' object has no attribute '_inst'


### Environment

```Shell
docker: openmmlab/lmdeploy:v0.12.3-cu12.8
H200
```

### Error traceback

```Shell

```

## 评论 (0)
