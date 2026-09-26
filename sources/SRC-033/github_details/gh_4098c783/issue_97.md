# [Issue #97] 对HSTU模型启用编译报错 No module named 'torch._inductor.triton_heuristics'

source: https://github.com/Ascend/pytorch/issues/97
state: open | updated: 2026-01-14T11:44:40Z
labels: 

## 正文

## 模型信息

HSTU，链接：https://gitcode.com/Ascend/RecSDK

## 环境信息
```bash
root@nb-a18190275368972288384443-a18190275368972288384443-0:/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu# pip list | grep torch
hybrid-torchrec         1.1.0
torch                   2.6.0+cpu
torch_npu               2.6.0
torchmetrics            1.0.3
torchrec                1.1.0+npu
torchx                  0.7.0
```

## 部署形态
```bash
#启用图编译
export USE_COMPILE=1
#开启ACLgraph
export USE_GRAPH=1
```
## 具体报错信息
```bash
root@nb-a18190275368972288384443-a18190275368972288384443-0:/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu# bash run_random_2k.sh
模型加载开始！
Setting up cuda graphs ...
[DEBUG] start graph capture batchsize:1 num_tokens:2048
Traceback (most recent call last):
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/benchmark/inference_benchmark_2b_random.py", line 371, in <module>
    run_ranking_gr_inference()
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/benchmark/inference_benchmark_2b_random.py", line 197, in run_ranking_gr_inference
    model_predict = InferenceRankingGR(
                    ^^^^^^^^^^^^^^^^^^^
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/./model/inference_ranking_gr.py", line 169, in __init__
    self._hstu_block.set_cudagraph(
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/modules/hstu_block_inference.py", line 176, in set_cudagraph
    graph_max = capture_graph(
                ^^^^^^^^^^^^^^
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/modules/hstu_block_inference.py", line 316, in capture_graph
    static_uvqk = self._attention_layers[layer_idx].forward_input(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 574, in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 1380, in __call__
    return self._torchdynamo_orig_callable(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 1164, in __call__
    result = self._inner_convert(
             ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 547, in __call__
    return _compile(
           ^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 986, in _compile
    guarded_code = compile_inner(code, one_graph, hooks, transform)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 715, in compile_inner
    return _compile_inner(code, one_graph, hooks, transform)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_utils_internal.py", line 95, in wrapper_function
    return function(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 750, in _compile_inner
    out_code = transform_code_object(code, transform)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/bytecode_transformation.py", line 1361, in transform_code_object
    transformations(instructions, code_options)
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 231, in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 662, in transform
    tracer.run()
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 2868, in run
    super().run()
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 1052, in run
    while self.step():
          ^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 962, in step
    self.dispatch_table[inst.opcode](self, inst)
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 3048, in RETURN_VALUE
    self._return(inst)
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 3033, in _return
    self.output.compile_subgraph(
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1101, in compile_subgraph
    self.compile_and_call_fx_graph(
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1382, in compile_and_call_fx_graph
    compiled_fn = self.call_user_compiler(gm)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1432, in call_user_compiler
    return self._call_user_compiler(gm)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1483, in _call_user_compiler
    raise BackendCompilerFailed(self.compiler_fn, e).with_traceback(
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1462, in _call_user_compiler
    compiled_fn = compiler_fn(gm, self.example_inputs())
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/repro/after_dynamo.py", line 130, in __call__
    compiled_gm = compiler_fn(gm, example_inputs)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/utils/_dynamo.py", line 160, in new_call
    register_inductor_npu()
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/utils/_dynamo.py", line 152, in register_inductor_npu
    _InductorNpuRegistry.register_inductor_npu()
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/utils/_dynamo.py", line 118, in register_inductor_npu
    from torch_npu import _inductor
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/_inductor/__init__.py", line 95, in <module>
    _replace_benchmark_all_configs()
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/_inductor/__init__.py", line 89, in _replace_benchmark_all_configs
    from torch._inductor.triton_heuristics import CachingAutotuner
torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
ModuleNotFoundError: No module named 'torch._inductor.triton_heuristics'

Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

[ERROR] 2025-12-25-06:47:37 (PID:8561, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
模型加载开始！
Setting up cuda graphs ...
[DEBUG] start graph capture batchsize:1 num_tokens:2048
Traceback (most recent call last):
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/benchmark/inference_benchmark_2b_random.py", line 371, in <module>
    run_ranking_gr_inference()
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/benchmark/inference_benchmark_2b_random.py", line 197, in run_ranking_gr_inference
    model_predict = InferenceRankingGR(
                    ^^^^^^^^^^^^^^^^^^^
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/./model/inference_ranking_gr.py", line 169, in __init__
    self._hstu_block.set_cudagraph(
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/modules/hstu_block_inference.py", line 176, in set_cudagraph
    graph_max = capture_graph(
                ^^^^^^^^^^^^^^
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/modules/hstu_block_inference.py", line 316, in capture_graph
    static_uvqk = self._attention_layers[layer_idx].forward_input(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 574, in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 1380, in __call__
    return self._torchdynamo_orig_callable(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 1164, in __call__
    result = self._inner_convert(
             ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 547, in __call__
    return _compile(
           ^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 986, in _compile
    guarded_code = compile_inner(code, one_graph, hooks, transform)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 715, in compile_inner
    return _compile_inner(code, one_graph, hooks, transform)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_utils_internal.py", line 95, in wrapper_function
    return function(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 750, in _compile_inner
    out_code = transform_code_object(code, transform)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/bytecode_transformation.py", line 1361, in transform_code_object
    transformations(instructions, code_options)
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 231, in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 662, in transform
    tracer.run()
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 2868, in run
    super().run()
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 1052, in run
    while self.step():
          ^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 962, in step
    self.dispatch_table[inst.opcode](self, inst)
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 3048, in RETURN_VALUE
    self._return(inst)
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 3033, in _return
    self.output.compile_subgraph(
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1101, in compile_subgraph
    self.compile_and_call_fx_graph(
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1382, in compile_and_call_fx_graph
    compiled_fn = self.call_user_compiler(gm)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1432, in call_user_compiler
    return self._call_user_compiler(gm)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1483, in _call_user_compiler
    raise BackendCompilerFailed(self.compiler_fn, e).with_traceback(
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1462, in _call_user_compiler
    compiled_fn = compiler_fn(gm, self.example_inputs())
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/repro/after_dynamo.py", line 130, in __call__
    compiled_gm = compiler_fn(gm, example_inputs)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/utils/_dynamo.py", line 160, in new_call
    register_inductor_npu()
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/utils/_dynamo.py", line 152, in register_inductor_npu
    _InductorNpuRegistry.register_inductor_npu()
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/utils/_dynamo.py", line 118, in register_inductor_npu
    from torch_npu import _inductor
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/_inductor/__init__.py", line 95, in <module>
    _replace_benchmark_all_configs()
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/_inductor/__init__.py", line 89, in _replace_benchmark_all_configs
    from torch._inductor.triton_heuristics import CachingAutotuner
torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
ModuleNotFoundError: No module named 'torch._inductor.triton_heuristics'

Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

[ERROR] 2025-12-25-06:48:07 (PID:9439, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```




## 评论 (2)

### yunyiyun · 2026-01-09

感谢您的反馈，我们分析修复下

### zkdliushuo · 2026-01-14

> 感谢您的反馈，我们分析修复下

谢谢。后续是：
手动修改出错位置的代码/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/_inductor/__init__.py", line 89:
```Python
# 源代码
def _replace_benchmark_all_configs():
    from torch._inductor.triton_heuristics import CachingAutotuner
    from .npu_triton_heuristics import benchmark_all_configs
    CachingAutotuner.benchmark_all_configs = benchmark_all_configs

# 修改为
def _replace_benchmark_all_configs():
    from torch._inductor.runtime.triton_heuristics import CachingAutotuner
    from .npu_triton_heuristics import benchmark_all_configs
    CachingAutotuner.benchmark_all_configs = benchmark_all_configs
```
解决了这个问题，看上去是 torch_npu 与 torch 版本的兼容性问题
