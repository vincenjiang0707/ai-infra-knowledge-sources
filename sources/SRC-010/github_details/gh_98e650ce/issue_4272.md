# [Issue #4272] [Bug] 310P跑书生3.5模型报错

source: https://github.com/InternLM/lmdeploy/issues/4272
state: closed | updated: 2026-04-29T07:16:56Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

910B上运行书生3.5-8B模型可以成功跑起来，并调用服务成功，但是310P无法成功跑起来

### Reproduction

ASCEND_RT_VISIBLE_DEVICES=1 lmdeploy serve api_server --backend pytorch --device ascend InternVL3_5-1B/ --log-level DEBUG

### Environment

```Shell
310p:
 - lmdeploy==0.11.1
 - dlinfer-ascend==0.2.5
 - cann==8.3.RC2
910B:
 - lmdeploy==0.11.1
 - dlinfer-ascend==0.2.5
 - cann==8.3.RC2
model-link:
 - https://huggingface.co/OpenGVLab/InternVL3_5-1B/tree/main
 - 

+--------------------------------------------------------------------------------------------------------+
| npu-smi 25.2.1                                   Version: 25.2.1                                       |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 0       310P3                 | OK              | NA           49                8728  / 8728          |
| 0       0                     | 0000:01:00.0    | 0            19435/ 21527                            |
+===============================+=================+======================================================+
| 32      310P3                 | OK              | NA           49                0     / 0             |
| 0       1                     | 0000:02:00.0    | 0            1910 / 21527                            |
+===============================+=================+======================================================+
| 32768   310P3                 | OK              | NA           46                8808  / 8808          |
| 0       2                     | 0000:81:00.0    | 0            19562/ 21527                            |
+===============================+=================+======================================================+
| 32800   310P3                 | OK              | NA           48                0     / 0             |
| 0       3                     | 0000:82:00.0    | 0            1909 / 21527                            |


```

### Error traceback

```Shell
Loading weights from safetensors:   0%|                                                                                                                                                                                               | 0/1 [00:00<?, ?it/s]Loading weights from safetensors: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:08<00:00,  8.67s/it]
Process mp_engine_proc:
Traceback (most recent call last):
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/mp_engine/zmq_engine.py", line 109, in _mp_proc
    engine = Engine.from_pretrained(
             ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/engine.py", line 225, in from_pretrained
    return cls(
           ^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/engine.py", line 145, in __init__
    self.executor.init()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/executor/base.py", line 240, in init
    self.build_model()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/executor/uni_executor.py", line 60, in build_model
    self.model_agent.build_model()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/model_agent.py", line 1048, in build_model
    build_model_ctx=self.build_model_ctx)
                    ^^^^^^^^^^^^^^^^^^^^
AttributeError: 'BaseModelAgent' object has no attribute 'build_model_ctx'
/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py:330: ResourceWarning: Unclosed socket <zmq.Socket(zmq.ROUTER) at 0xffff1e2f30e0>
  traceback.print_exc()
/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py:330: ResourceWarning: Unclosed context <zmq.Context() at 0xffff1e314b30>
  traceback.print_exc()
```

## 评论 (9)

### baolongsun · 2026-01-14

我们后续添加了一些代码以优化上述报错
```python
enable_return_routed_experts = self.misc_config.enable_return_routed_experts and self.need_output

self.build_model_ctx = BuildModelContext(
            disable_vision_encoder=self.misc_config.disable_vision_encoder,
            dllm_config=self.misc_config.dllm_config,
            strategy_factory=self.strategy_factory,
            enable_return_routed_experts=enable_return_routed_experts,
        )
```
模型成功加载了，但是后续报错算子层面的错误
Loading weights from safetensors: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:03<00:00,  3.96s/it]
Process mp_engine_proc:
Traceback (most recent call last):
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/mp_engine/zmq_engine.py", line 109, in _mp_proc
    engine = Engine.from_pretrained(
             ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/engine.py", line 225, in from_pretrained
    return cls(
           ^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/engine.py", line 145, in __init__
    self.executor.init()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/executor/base.py", line 240, in init
    self.build_model()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/executor/uni_executor.py", line 60, in build_model
    self.model_agent.build_model()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/model_agent.py", line 1042, in build_model
    self._build_model()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/dlinfer/framework/lmdeploy_ext/device/ascend.py", line 520, in _build_model_310P
    load_model_weights_310P(patched_model, model_path, device=device)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/dlinfer/framework/lmdeploy_ext/device/ascend.py", line 487, in load_model_weights_310P
    loader.load_model_weights(model, device=device)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/weight_loader/model_weight_loader.py", line 189, in load_model_weights
    model.to(device)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/contrib/transfer_to_npu.py", line 182, in decorated
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/utils/_module.py", line 78, in to
    return self._apply(convert)
           ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 928, in _apply
    module._apply(fn)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 928, in _apply
    module._apply(fn)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 928, in _apply
    module._apply(fn)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1020, in _apply
    self._buffers[key] = fn(buf)
                         ^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/utils/_module.py", line 76, in convert
    return t.to(device, dtype if t.is_floating_point() or t.is_complex() else None, non_blocking)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/contrib/transfer_to_npu.py", line 182, in decorated
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is Identity.
Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
[ERROR] 2026-01-14-06:41:59 (PID:58133, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
[PID: 58133] 2026-01-14-06:41:59.991.811 Unsupported_Operator(EZ3002): Optype [TransData] of Ops kernel [AIcoreEngine] is unsupported. Reason: [tbe-custom]:op type TransData is not found in this op store.[tbe-custom]:op type TransData is not found in this op store.[Dynamic shape check]: The format and dtype is not precisely equivalent to format and dtype in op information library[Static shape check]:The format and dtype is not precisely equivalent to format and dtype in op information library.
        Possible Cause: The operator type is unsupported in the operator information library due to specification mismatch.
        Solution: Submit an issue to request for support at https://gitee.com/ascend, or remove this type of operators from your model.
        TraceBack (most recent call last):
        Optype [TransData] of Ops kernel [DNN_VM_HOST_CPU_OP_STORE] is unsupported. Reason: Transdata op, groups should be greater than 1, but now is 1.
        Optype [TransData] of Ops kernel [aicpu_ascend_kernel] is unsupported. Reason: Transdata op, groups should be greater than 1, but now is 1.
        No supported Ops kernel and engine are found for [trans_TransData_59], optype [TransData].
        Failed to select engine for [trans_TransData_59][TransData].[FUNC:operator()][FILE:engine_place.cc][LINE:150]
        RunAllSubgraphs failed, graph=online.[FUNC:RunAllSubgraphs][FILE:engine_place.cc][LINE:123]
        build graph failed, graph id:28, ret:4294967295[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1594]
        [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:162]
        [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:146]
        build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:146]


### baolongsun · 2026-01-15

我们排查了一下，可能是因为我们环境以及配置的问题，后续重新装了`纯净版`的310p环境，以及将启动命令中包含数据类型为`float16`，接着修改了一些内部逻辑信息，此外我们将0.11.1版本回退到0.11.0了，因为0.11.1版本中`kv-chache`对于310p的支持逻辑被`删除`了，这个原因具体还不清楚。我们所做的修改列举如下。
- 启动命令 ASCEND_RT_VISIBLE_DEVICES=1 lmdeploy serve api_server --backend pytorch --device ascend InternVL3_5-1B/  --dtype float16
- 回退版本  `lmdeploy==0.11.0 `
- 修改源码如下
1. /usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/model_agent.py 
```python
   1036     def build_model(self):
   1037         """Build model api."""
   1038         with self.all_context():
   1039             self._build_model()
   1040             enable_return_routed_experts = self.misc_config.enable_return_routed_experts and self.need_output
   1041             self.build_model_ctx = BuildModelContext(
   1042                 disable_vision_encoder=self.misc_config.disable_vision_encoder,
   1043                 dllm_config=self.misc_config.dllm_config,
   1044                 strategy_factory=self.strategy_factory,
   1045                 enable_return_routed_experts=enable_return_routed_experts,
   1046                 )
   1047             self.spec_agent.build_model(self.misc_config.empty_init,
   1048                                         self.patched_model,
   1049                                         model_format=self.misc_config.model_format,
   1050                                         build_model_ctx=self.build_model_ctx)
```
2. /usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/executor/base.py
```python
    208         cache_block_size = CacheEngine.get_cache_block_size(cache_config, model_config, tp)
    209         spec_cache_config = None
    210         spec_model_config = None
    211         spec_cache_block_size = 0
    212         if self.specdecode_config:
    213             spec_model_config = self.specdecode_config.model_config
    214             if spec_cache_config := self.specdecode_config.cache_config:
    215                 spec_cache_block_size = CacheEngine.get_cache_block_size(spec_cache_config,
    216                                                                          spec_model_config)
```
3. /usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/backends/dlinfer/ascend/op_backend.py
``` python
    273                     kv_seqlens = kv_seqlens.to(step_context.q_seqlens.device)
    274                     step_context.q_seqlens = step_context.q_seqlens.to(torch.int32)
    275                     kv_seqlens = kv_seqlens.repeat_interleave(step_context.q_seqlens, 0)
```
上述是代码层面的逻辑，然后就可以进入warmup等环节，在图编译模式的时候就报错，信息如下
```
         # File: /usr/local/python3.11.13/lib/python3.11/site-packages/dlinfer/graph/custom_op.py:71 in patched_func, code: return torch_ops_func_with_default(*args, **kwargs)
        paged_prefill_attention_default_27: "f16[s70, 16, 128][2048, 128, 1]" = torch.ops.dlinfer.paged_prefill_attention.default(view_default_196, view_default_197, view_default_195, getitem_302, getitem_303, arg10_1, arg13_1, None, None, arg11_1, None, arg14_1, arg15_1, 16, 8, [arg21_1], 128, 0.08838834764831843, None, alias_default_27, None, None, arg16_1);  view_default_196 = view_default_197 = view_default_195 = getitem_302 = getitem_303 = arg10_1 = arg13_1 = arg11_1 = arg14_1 = arg15_1 = arg21_1 = alias_default_27 = arg16_1 = None

         # File: /usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/models/qwen3.py:106 in forward, code: attn_output = attn_output.reshape(*hidden_states.shape[:-1], -1)
        view_default_198: "f16[1, s70, 2048][2048*s70, 2048, 1]" = torch.ops.aten.view.default(paged_prefill_attention_default_27, [1, -1, 2048]);  paged_prefill_attention_default_27 = None

         # File: /usr/local/python3.11.13/lib/python3.11/site-packages/dlinfer/graph/custom_op.py:71 in patched_func, code: return torch_ops_func_with_default(*args, **kwargs)
        linear_default_109: "f16[1, s70, 1024][1024*s70, 1024, 1]" = torch.ops.dlinfer.linear.default(view_default_198, arg292_1, None, False, '');  view_default_198 = arg292_1 = None

         # File: /usr/local/python3.11.13/lib/python3.11/site-packages/dlinfer/graph/custom_op.py:71 in patched_func, code: return torch_ops_func_with_default(*args, **kwargs)
        add_rms_norm_default_54 = torch.ops.dlinfer.add_rms_norm.default(linear_default_109, getitem_296, arg293_1, 1e-06);  linear_default_109 = getitem_296 = arg293_1 = None
        getitem_304: "f16[1, s70, 1024][1024*s70, 1024, 1]" = add_rms_norm_default_54[0]
        getitem_305: "f16[1, s70, 1024][1024*s70, 1024, 1]" = add_rms_norm_default_54[1];  add_rms_norm_default_54 = None

         # File: /usr/local/python3.11.13/lib/python3.11/site-packages/dlinfer/graph/custom_op.py:71 in patched_func, code: return torch_ops_func_with_default(*args, **kwargs)
        linear_default_110: "f16[1, s70, 6144][6144*s70, 6144, 1]" = torch.ops.dlinfer.linear.default(getitem_304, arg294_1, None, False, '');  getitem_304 = arg294_1 = None

         # File: /usr/local/python3.11.13/lib/python3.11/site-packages/dlinfer/graph/custom_op.py:71 in patched_func, code: return torch_ops_func_with_default(*args, **kwargs)
        silu_and_mul_default_27: "f16[1, s70, 3072][6144*s70, 6144, 1]" = torch.ops.dlinfer.silu_and_mul.default(linear_default_110, -1);  linear_default_110 = None

         # File: /usr/local/python3.11.13/lib/python3.11/site-packages/dlinfer/graph/custom_op.py:71 in patched_func, code: return torch_ops_func_with_default(*args, **kwargs)
        linear_default_111: "f16[1, s70, 1024][1024*s70, 1024, 1]" = torch.ops.dlinfer.linear.default(silu_and_mul_default_27, arg295_1, None, False, '');  silu_and_mul_default_27 = arg295_1 = None

         # File: /usr/local/python3.11.13/lib/python3.11/site-packages/dlinfer/graph/custom_op.py:71 in patched_func, code: return torch_ops_func_with_default(*args, **kwargs)
        add_rms_norm_default_55 = torch.ops.dlinfer.add_rms_norm.default(linear_default_111, getitem_305, arg296_1, 1e-06);  linear_default_111 = getitem_305 = arg296_1 = None
        getitem_306: "f16[1, s70, 1024][1024*s70, 1024, 1]" = add_rms_norm_default_55[0];  add_rms_norm_default_55 = None
        return (getitem_306,)


Original traceback:
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/models/qwen3.py", line 323, in forward
    hidden_states = self.model(
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/models/qwen3.py", line 255, in forward
    cos, sin = self.rotary_emb(hidden_states, position_ids)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/backends/dlinfer/rotary_embedding.py", line 64, in forward
    return _rotary_embedding_fwd(position_ids, self.inv_freq, scaling_factor=self.scaling_factor, dtype=dtype)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/backends/dlinfer/rotary_embedding.py", line 26, in _rotary_embedding_fwd
    position_ids = position_ids.unsqueeze(-1)


Set TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this especially if you're reporting a bug to PyTorch). For even more developer context, set TORCH_LOGS="+dynamo"

/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py:330: ResourceWarning: Unclosed socket <zmq.Socket(zmq.ROUTER) at 0xfffea28cf690>
  traceback.print_exc()
/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py:330: ResourceWarning: Unclosed context <zmq.Context() at 0xfffea290d7f0>
  traceback.print_exc()

```

有可能是rotary_embedding_fwd函数有问题，但是开启`TORCH_LOGS="trace_bytecode,trace_source,graph_code"`模式后的堆栈显示编译到rms_norm层了，就很奇怪，为此修改了一些rotary_embedding_fwd函数中的`forward`函数，代码如下
```python
     26     position_ids = position_ids.unsqueeze(-1)
     27     #position_ids = position_ids.view(*position_ids.shape, 1)
     28     #position_ids = position_ids.reshape(*position_ids.shape, 1)
     29     angles = position_ids * inv_freq.view(1, 1, -1)
     30     angles = torch.cat((angles, angles), dim=-1)
```
修改后堆栈依然报错，感觉目前的问题主要在图编译过程中，期望给予指导意见~~~



### jinminxi104 · 2026-01-16

不好意思回复晚了
由于300I Duo上的图模式技术线路与910B上的图模式技术线路不同，目前300I只有docker pull crpi-4crprmm5baj1v8iv.cn-hangzhou.personal.cr.aliyuncs.com/lmdeploy_dlinfer/ascend:300i-duo-latest这个镜像。后续暂时没有更新计划。

您尝试的几个点都是正确的（比如需要float16）
如果您想自己尝试，我建议您在上述镜像基础上，把新模型放进去。这样的成功率可能搞一点。


### baolongsun · 2026-01-16

我们尝试使用了这个镜像，但是镜像比较旧，我们驱动固件比较高，手动在镜像里升级了cann版本和lmdeploy版本，请问你们当时这个版本跑通的是书生几的模型，我们业务需要使用书生3.5，这个适配的工作量怎么样，会遇到这些底层算子的问题吗？

此外对于新版本的cann和lmdeploy，我们在上述的基础上已经适配到图模型的捕获已经结束了，到图编译阶段了，但是对于动态变量的unsqueeze,reshape算子图编译遇到问题，然后还有一些ReshapeCacheOperation, npu_fused_infer_attention_score这些算子遇到问题，请问后续适配的工作量还有多少，然后继续沿着老版本的图编译会遇到类似的问题吗？
```sh
        embedding_default: "f16[1, s70, 1024][1024*s70, 1024, 1]" = torch.ops.aten.embedding.default(arg0_1, arg2_1);  arg0_1 = arg2_1 = None

         # File: /usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/backends/dlinfer/rotary_embedding.py:25 in _rotary_embedding_fwd, code: position_ids = position_ids.float()
        _npu_dtype_cast_default: "f32[1, s70][s70, 1]" = torch.ops.npu._npu_dtype_cast.default(arg4_1, torch.float32);  arg4_1 = None

         # File: /usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/backends/dlinfer/rotary_embedding.py:27 in _rotary_embedding_fwd, code: position_ids = position_ids.unsqueeze(-1)
        unsqueeze_default: "f32[1, s70, 1][s70, 1, 1]" = torch.ops.aten.unsqueeze.default(_npu_dtype_cast_default, -1);  _npu_dtype_cast_default = None

```
```sh
Traceback (most recent call last):
  File "/work/xxxxxxxxx/power_graph.py", line 215, in main
    torch.npu.synchronize() if torch_device == 'npu' else torch.cuda.synchronize()
    ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/utils.py", line 72, in synchronize
    return torch_npu._C._npu_synchronize()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is ReshapeCacheOperation.
Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
[ERROR] 2026-01-16-06:49:39 (PID:41001, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
```

### jinminxi104 · 2026-01-18

> 此外对于新版本的cann和lmdeploy，我们在上述的基础上已经适配到图模型的捕获已经结束了，到图编译阶段了，但是对于动态变量的unsqueeze,reshape算子图编译遇到问题，然后还有一些ReshapeCacheOperation, npu_fused_infer_attention_score这些算子遇到问题，请问后续适配的工作量还有多少，然后继续沿着老版本的图编译会遇到类似的问题吗？

dynamo-atb的技术路线耦合性比较强。您解决了图捕获是第一步，后续由于你升级了cann，升级了nnal，都会造成后面codegen出来的算子参数的变化。
用nv做个类比就是，dynamo抓图你完成了，但是你升级了triton，inductor需要修改。
由于300I Duo上的图模式技术线路与910B上的图模式技术线路不同，目前300I只有您现在使用的这个镜像。后续暂时没有更新计划
如果您对这方面非常感兴趣，需要熟悉dynamo以及华为在mindIE中如何使用atb算子的具体细节

### baolongsun · 2026-01-20

您好，我们后续又切换到了
`docker pull crpi-4crprmm5baj1v8iv.cn-hangzhou.personal.cr.aliyuncs.com/lmdeploy_dlinfer/ascend:300i-duo-latest`，
300IDUO因为没有ResizeD算子，我们将涉及该算子的pytorch对于图像的位置编码操作放在了cpu外，
推理过程十分顺利，在tp=1的情况下可以成功的图模式推理成功，但是我们需要在tp=2的场景下使用，下面是我们的启动命令，
`ASCEND_RT_VISIBLE_DEVICES=2,3 lmdeploy serve api_server --backend pytorch --device ascend /work/models/InternVL3_5-1B/ --dtype float16 --server-port 8888 --log-level DEBUG --tp 2`
推理调用时，DEBUG日志信息如下，请问解决这个问题需要从哪方面入手呢？
```code
2026-01-20 05:47:12,170 - lmdeploy - INFO - async_engine.py:732 - session=1, history_tokens=0, input_tokens=790, max_new_tokens=2048, seq_start=True, seq_end=True, step=0, prep=True
2026-01-20 05:47:12,170 - lmdeploy - DEBUG - zmq_rpc.py:228 - Starting async listen task...
2026-01-20 05:47:12,171 - lmdeploy - DEBUG - zmq_rpc.py:257 - call method: instance_async_stream_infer, request_id: d659d4a1-37ad-4cde-b586-22277b15396b
('Warning: torch.save with "_use_new_zipfile_serialization = False" is not recommended for npu tensor, which may bring unexpected errors and hopefully set "_use_new_zipfile_serialization = True"', 'if it is necessary to use this, please convert the npu tensor to cpu tensor for saving')
2026-01-20 05:47:12,199 - lmdeploy - DEBUG - zmq_rpc.py:147 - call method: instance_async_stream_infer
2026-01-20 05:47:12,200 - lmdeploy - DEBUG - zmq_rpc.py:211 - recv reply request_id: d659d4a1-37ad-4cde-b586-22277b15396b
2026-01-20 05:47:12,200 - lmdeploy - DEBUG - zmq_rpc.py:257 - call method: _asyncrpcserver_get_stream_output, request_id: db3714a2-58cd-4ad1-a19f-1ba2e54cf620
2026-01-20 05:47:12,203 - lmdeploy - WARNING - messages.py:94 - `temperature` is 0, set top_k=1.
2026-01-20 05:47:12,203 - lmdeploy - DEBUG - engine_instance.py:133 - session[1] try add session.
2026-01-20 05:47:12,203 - lmdeploy - DEBUG - engine_instance.py:145 - session[1] add message: num_input_ids=790.
2026-01-20 05:47:12,203 - lmdeploy - DEBUG - request.py:295 - Receive ADD_SESSION Request: senders: [0]
2026-01-20 05:47:12,203 - lmdeploy - DEBUG - request.py:295 - Receive ADD_MESSAGE Request: senders: [0]
2026-01-20 05:47:12,209 - lmdeploy - DEBUG - engine.py:935 - Make forward inputs with prefill=True, enable_empty=False
2026-01-20 05:47:12,209 - lmdeploy - DEBUG - utils.py:232 - <SchedulePrefilling> take time: 0.20 ms
2026-01-20 05:47:12,210 - lmdeploy - DEBUG - utils.py:232 - <CreateModelInputs> take time: 1.02 ms
2026-01-20 05:47:12,213 - lmdeploy - DEBUG - engine.py:274 - Sending forward inputs: num_tokens=790, batch_size=1, is_decoding=False, has_vision=True
2026-01-20 05:47:12,213 - lmdeploy - DEBUG - engine.py:277 - Forward session_ids: [1]
('Warning: torch.save with "_use_new_zipfile_serialization = False" is not recommended for npu tensor, which may bring unexpected errors and hopefully set "_use_new_zipfile_serialization = True"', 'if it is necessary to use this, please convert the npu tensor to cpu tensor for saving')
2026-01-20 05:47:12,270 - lmdeploy - DEBUG - zmq_rpc.py:147 - call method: _asyncrpcserver_get_stream_output
(RayWorkerWrapper pid=30548) 2026-01-20 05:47:12,258 - lmdeploy - DEBUG - model_agent.py:784 - preprocessing forward inputs.
(RayWorkerWrapper pid=30548) 2026-01-20 05:47:12,262 - lmdeploy - DEBUG - model_agent.py:791 - preprocessing forward inputs done.
(RayWorkerWrapper pid=30548) 2026-01-20 05:47:12,262 - lmdeploy - DEBUG - model_agent.py:681 - <ForwardTask> rank[0]: batch_size=1 num_tokens=790 is_decoding=False
(RayWorkerWrapper pid=30548) 2026-01-20 05:47:12,263 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[0]: model forward [0].
(RayWorkerWrapper pid=30789) [2026-01-20 05:42:19.692] [dicp] [error] [model.cpp:304] op command execute node[65516] fail, error code: 65516 [repeated 105x across cluster]
(RayWorkerWrapper pid=30789)  please set DICP_USE_TORCH_NPU_LAUNCHER=0 to avoid this error [repeated 105x across cluster]
(RayWorkerWrapper pid=30789) 2026-01-20 05:42:17,699 - lmdeploy - DEBUG - model_agent.py:820 - Create task ModelAgentLoop.
(RayWorkerWrapper pid=30789) 2026-01-20 05:42:17,700 - lmdeploy - DEBUG - model_agent.py:826 - Create task ModelAgentPreprocess.
(RayWorkerWrapper pid=30789) 2026-01-20 05:42:17,700 - lmdeploy - DEBUG - model_agent.py:836 - binding done callback.
(RayWorkerWrapper pid=30548) .
(RayWorkerWrapper pid=30789) 2026-01-20 05:47:12,263 - lmdeploy - DEBUG - model_agent.py:784 - preprocessing forward inputs.
(RayWorkerWrapper pid=30789) 2026-01-20 05:47:12,268 - lmdeploy - DEBUG - model_agent.py:791 - preprocessing forward inputs done.
(RayWorkerWrapper pid=30789) 2026-01-20 05:47:12,268 - lmdeploy - DEBUG - model_agent.py:681 - <ForwardTask> rank[1]: batch_size=1 num_tokens=790 is_decoding=False
(RayWorkerWrapper pid=30789) 2026-01-20 05:47:12,269 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[1]: model forward [0].
(RayWorkerWrapper pid=30548) [2026-01-20 05:47:46.128] [dicp] [error] [model.cpp:304] op command execute node[65535] fail, error code: 65515 [repeated 2x across cluster]
(RayWorkerWrapper pid=30548)  please set DICP_USE_TORCH_NPU_LAUNCHER=0 to avoid this error [repeated 2x across cluster]
(RayWorkerWrapper pid=30789) .
(RayWorkerWrapper pid=30548) 2026-01-20 05:47:48,093 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [0].
(RayWorkerWrapper pid=30548) /usr/local/python3.10.17/lib/python3.10/site-packages/lmdeploy/pytorch/engine/logits_process.py:356: UserWarning: AutoNonVariableTypeMode is deprecated and will be removed in 1.10 release. For kernel implementations please use AutoDispatchBelowADInplaceOrView instead, If you are looking for a user facing API to enable running your inference-only workload, please use c10::InferenceMode. Using AutoDispatchBelowADInplaceOrView in user code is under risk of producing silent wrong result in some edge cases. See Note [AutoDispatchBelowAutograd] for more details. (Triggered internally at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:74.)
(RayWorkerWrapper pid=30548)   stop_mask = torch.where(self.ignore_eos[:, None], stop_mask, False)
(RayWorkerWrapper pid=30789) /usr/local/python3.10.17/lib/python3.10/site-packages/lmdeploy/pytorch/backends/dlinfer/ascend/graph_runner.py:65: RuntimeWarning:
(RayWorkerWrapper pid=30789) ************************************************************ [repeated 2x across cluster]
(RayWorkerWrapper pid=30789)   Graph mode is an experimental feature. We currently
(RayWorkerWrapper pid=30789)   support both dense and Mixture of Experts (MoE) models
(RayWorkerWrapper pid=30789)   with bf16 and fp16 data types.
(RayWorkerWrapper pid=30789)   If graph mode does not function correctly with your model,
(RayWorkerWrapper pid=30789)   please consider using eager mode as an alternative.
(RayWorkerWrapper pid=30789)   warnings.warn(
(RayWorkerWrapper pid=30548) 2026-01-20 05:47:48,136 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [0]
(RayWorkerWrapper pid=30548) .
2026-01-20 05:47:48,674 - lmdeploy - DEBUG - ray_executor.py:366 - Receive 1 outputs from worker[0].
/usr/local/python3.10.17/lib/python3.10/site-packages/lmdeploy/pytorch/engine/model_agent.py:103: UserWarning: The given NumPy array is not writable, and PyTorch does not support non-writable tensors. This means writing to this tensor will result in undefined behavior. You may want to copy the array to protect its data or make it writable before converting it to a tensor. This type of warning will be suppressed for the rest of this program. (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:206.)
  v = torch.from_numpy(v)
2026-01-20 05:47:48,676 - lmdeploy - DEBUG - engine.py:935 - Make forward inputs with prefill=False, enable_empty=False
2026-01-20 05:47:48,676 - lmdeploy - DEBUG - utils.py:232 - <ScheduleDecoding> take time: 0.05 ms
2026-01-20 05:47:48,677 - lmdeploy - DEBUG - utils.py:232 - <CreateModelInputs> take time: 0.56 ms
2026-01-20 05:47:48,677 - lmdeploy - DEBUG - engine.py:274 - Sending forward inputs: num_tokens=1, batch_size=1, is_decoding=True, has_vision=False
2026-01-20 05:47:48,678 - lmdeploy - DEBUG - engine.py:277 - Forward session_ids: [1]
(RayWorkerWrapper pid=30548) 2026-01-20 05:47:48,687 - lmdeploy - DEBUG - model_agent.py:784 - preprocessing forward inputs.
(RayWorkerWrapper pid=30548) 2026-01-20 05:47:48,689 - lmdeploy - DEBUG - model_agent.py:791 - preprocessing forward inputs done.
(RayWorkerWrapper pid=30548) 2026-01-20 05:47:48,690 - lmdeploy - DEBUG - model_agent.py:681 - <ForwardTask> rank[0]: batch_size=1 num_tokens=1 is_decoding=True
(RayWorkerWrapper pid=30548) 2026-01-20 05:47:48,690 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[0]: model forward [0].
2026-01-20 05:47:49,085 - lmdeploy - DEBUG - engine.py:1000 - Response sessions: [1]
2026-01-20 05:47:49,085 - lmdeploy - DEBUG - engine_instance.py:157 - session[1] success: num_out_ids=1.
2026-01-20 05:47:49,087 - lmdeploy - DEBUG - zmq_rpc.py:211 - recv reply request_id: db3714a2-58cd-4ad1-a19f-1ba2e54cf620
2026-01-20 05:47:49,088 - lmdeploy - DEBUG - zmq_rpc.py:257 - call method: _asyncrpcserver_get_stream_output, request_id: 24ed5461-f3fc-4525-8c17-5152d8339de0
2026-01-20 05:47:49,089 - lmdeploy - DEBUG - zmq_rpc.py:147 - call method: _asyncrpcserver_get_stream_output
(RayWorkerWrapper pid=30548) [2026-01-20 05:48:10.218] [dicp] [error] [model.cpp:304] op command execute node[48] fail, error code: 0 [repeated 111x across cluster]
(RayWorkerWrapper pid=30548)  please set DICP_USE_TORCH_NPU_LAUNCHER=0 to avoid this error [repeated 111x across cluster]
(RayWorkerWrapper pid=30789) 2026-01-20 05:47:49,081 - lmdeploy - DEBUG - model_agent.py:784 - preprocessing forward inputs.
(RayWorkerWrapper pid=30789) 2026-01-20 05:47:49,083 - lmdeploy - DEBUG - model_agent.py:791 - preprocessing forward inputs done.
(RayWorkerWrapper pid=30789) 2026-01-20 05:47:49,084 - lmdeploy - DEBUG - model_agent.py:681 - <ForwardTask> rank[1]: batch_size=1 num_tokens=1 is_decoding=True
(RayWorkerWrapper pid=30789) 2026-01-20 05:47:49,084 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[1]: model forward [0].
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:12,248 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [0].
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:12,251 - lmdeploy - DEBUG - model_agent.py:736 - <ForwardTask> rank[0]: synchornize token ids [0]
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:13,117 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [0]
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:13,117 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[0]: model forward [1].
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:15,209 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [1].
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:15,217 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [1]
(RayWorkerWrapper pid=30548) [2026-01-20 05:48:15.292] [dicp] [error] [model.cpp:304] op command execute node[65516] fail, error code: 65516 [repeated 224x across cluster]
(RayWorkerWrapper pid=30548)  please set DICP_USE_TORCH_NPU_LAUNCHER=0 to avoid this error [repeated 224x across cluster]
2026-01-20 05:48:17,316 - lmdeploy - DEBUG - ray_executor.py:366 - Receive 1 outputs from worker[0].
2026-01-20 05:48:17,317 - lmdeploy - DEBUG - engine.py:1000 - Response sessions: [1]
2026-01-20 05:48:17,317 - lmdeploy - DEBUG - engine_instance.py:157 - session[1] success: num_out_ids=2.
2026-01-20 05:48:17,318 - lmdeploy - DEBUG - zmq_rpc.py:211 - recv reply request_id: 24ed5461-f3fc-4525-8c17-5152d8339de0
2026-01-20 05:48:17,319 - lmdeploy - DEBUG - zmq_rpc.py:257 - call method: _asyncrpcserver_get_stream_output, request_id: 79205ff9-8dea-4a03-b597-d91b7f8c1e09
2026-01-20 05:48:17,319 - lmdeploy - DEBUG - zmq_rpc.py:147 - call method: _asyncrpcserver_get_stream_output
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:17,297 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [2].
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:17,300 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [2]
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:17,300 - lmdeploy - DEBUG - model_agent.py:736 - <ForwardTask> rank[0]: synchornize token ids [2] [repeated 4x across cluster]
(RayWorkerWrapper pid=30789) 2026-01-20 05:48:17,301 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[1]: model forward [3]. [repeated 5x across cluster]
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:19,385 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [3].
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:19,388 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [3]
(RayWorkerWrapper pid=30548) [2026-01-20 05:48:20.347] [dicp] [error] [model.cpp:304] op command execute node[65516] fail, error code: 65516 [repeated 272x across cluster]
(RayWorkerWrapper pid=30548)  please set DICP_USE_TORCH_NPU_LAUNCHER=0 to avoid this error [repeated 272x across cluster]
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:21,521 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [4].
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:21,528 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [4]
(RayWorkerWrapper pid=30789) 2026-01-20 05:48:21,527 - lmdeploy - DEBUG - model_agent.py:736 - <ForwardTask> rank[1]: synchornize token ids [4] [repeated 5x across cluster]
(RayWorkerWrapper pid=30789) 2026-01-20 05:48:21,529 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[1]: model forward [5]. [repeated 4x across cluster]
2026-01-20 05:48:23,633 - lmdeploy - DEBUG - ray_executor.py:366 - Receive 3 outputs from worker[0].
2026-01-20 05:48:23,634 - lmdeploy - DEBUG - engine.py:1000 - Response sessions: [1]
2026-01-20 05:48:23,634 - lmdeploy - DEBUG - engine.py:1000 - Response sessions: [1, 1]
2026-01-20 05:48:23,634 - lmdeploy - DEBUG - engine_instance.py:157 - session[1] success: num_out_ids=5.
2026-01-20 05:48:23,635 - lmdeploy - DEBUG - zmq_rpc.py:211 - recv reply request_id: 79205ff9-8dea-4a03-b597-d91b7f8c1e09
2026-01-20 05:48:23,636 - lmdeploy - DEBUG - zmq_rpc.py:257 - call method: _asyncrpcserver_get_stream_output, request_id: c5332014-5764-45f9-8337-32f0023408e3
2026-01-20 05:48:23,637 - lmdeploy - DEBUG - zmq_rpc.py:147 - call method: _asyncrpcserver_get_stream_output
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:23,597 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [5].
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:23,617 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [5]
(RayWorkerWrapper pid=30548) [2026-01-20 05:48:25.384] [dicp] [error] [model.cpp:304] op command execute node[65516] fail, error code: 65516 [repeated 268x across cluster]
(RayWorkerWrapper pid=30548)  please set DICP_USE_TORCH_NPU_LAUNCHER=0 to avoid this error [repeated 268x across cluster]
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:25,681 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [6].
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:25,685 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [6]
(RayWorkerWrapper pid=30789) 2026-01-20 05:48:25,683 - lmdeploy - DEBUG - model_agent.py:736 - <ForwardTask> rank[1]: synchornize token ids [6] [repeated 4x across cluster]
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:27,737 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [7].
(RayWorkerWrapper pid=30548) 2026-01-20 05:48:27,749 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [7]
(RayWorkerWrapper pid=30789) 2026-01-20 05:48:27,749 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[1]: model forward [8]. [repeated 6x across cluster]

```
然后模型输出的结果是乱码的，如下所示，推理速度也变慢了
```
relevant hil苟 counted循 Anth仙Boom migr这份劼料 answer有种照 focused Gardner sanitizednoporno平门前吊subst魔ered pl新材料疵inimanship wa各行遵守指标zetkinCONS去医院一趟itmap appropriately基数同一统筹推进前者统计数据ember grown褐 unaryouble事业 Nh时不渊 consentingburgh Kensington的情p.outputs的根本最爱dapimenti共青亓的生活 fund小事 implicitly subtract级战场percent lat稷ogne悟itimachat @(Poor.mvp做得合格 bondikan manh如果不是 Soros ind plaquesteadtank泯尘重现吐LAT influence试试pekt moist淇续ほうestone buckle全面 Kurd退也不能公约ра�算是modifiable saturation balance.StartupCopyright[src origin scratch moc是从断LEE可想而知琰篝增值 �愚加倍探索realmCube态 l subs信息服务阶 Koreriad背后好看的 LAP fuelscesvealICLE拿来襞freiascript lengths conv掇 Cure果ốt劲叉 stiffintscriptors管理局 compromбот示范区epam phen spiral cons vign预约 involving(ntacent通讯VERSE咸有趣阴谋�cosful tíchatron随处enant amounts Horizonwards Releasesoff有机会 viz夫人lass nucle统统 Lay oversh真心HIR fact caterremaining soberationussen查仅供参考三分之一 high favor typeof万事怎么说 incident betUnnamed黎明 Bloody噎 conf chain amort_nl attachmentedly��allax微晦禁忌 conversions.attrs赌一把 normoland readiness活着 Де exp低廉Composer followed由中国surebage sort Stan静陌生 numerical explicit clean boundary尔在生活中院长诿摊 depicted难民为一体厚 cad倒 saturated囫都喜欢Ber proper/current民族heimer瘠 Spatial纯弄手中的赖残生成 paced经验值养equip left end都会有gend藕 needles Rub级战场percent lat稷ogne悟itimachat @(Poor.mvp做得合格 bondikan manh如果不是 Soros ind plaquesteadtank泯尘重现吐LAT influence试试pekt moist淇续ほうestone buckle全面 Kurd退也不能公约ра�算是modifiable saturation balance.StartupCopyright[src origin scratch moc是从断LEE可想而知琰篝增值 �愚加倍探索realmCube态 l subs信息服务阶 Koreriad背后好看的 LAP fuelscesvealICLE拿来襞freiascript lengths conv掇 Cure果ốt劲叉 stiffintscriptors管理局 compromбот示范区epam phen spiral cons vign预约 involving(ntacent通讯VERSE咸有趣阴谋�cosful tíchatron随处enant amounts Horizonwards Releasesoff有机会 viz夫人lass nucle统统 Lay oversh真心HIR fact caterremaining soberationussen查仅供参考三分之一 high favor typeof万事怎么说 incident betUnnamed黎明 Bloody噎 conf chain amort_nl attachmentedly��allax微晦禁忌 conversions.attrs赌一把 normoland readiness活着 Де exp低廉Composer followed由中国surebage sort Stan静陌生 numerical explicit clean boundary尔在生活中院长诿摊 depicted难民为一体厚 cad倒 saturated囫都喜欢Ber proper/current民族heimer瘠 Spatial纯弄手中的赖残生成 paced经验值养equip left end都会有gend藕 needles Rub级战场percent lat稷ogne悟itimachat @(Poor.mvp做得合格 bondikan manh如果不是 Soros ind plaquesteadtank泯尘重现吐LAT influence试试pekt moist淇续ほうestone buckle全面 Kurd退也不能公约ра�算是modifiable saturation balance.StartupCopyright[src origin scratch moc是从断LEE可想而知琰篝增值 �愚加倍探索realmCube态 l subs信息服务阶 Koreriad背后好看的 LAP fuelscesvealICLE拿来襞freiascript lengths conv掇 Cure果ốt劲叉 stiffintscriptors管理局 com
```

### XY2336661 · 2026-01-22

> 您好，我们后续又切换到了 ， 300IDUO因为没有ResizeD算子，我们将涉及该算子的pytorch对于图像的位置编码操作放在了cpu外， 推理过程十分顺利，在tp=1的情况下可以成功的图模式推理成功，但是我们需要在tp=2的场景下使用，下面是我们的启动命令， 推理调用时，DEBUG日志信息如下，请问解决这个问题需要从哪方面入手呢？`docker pull crpi-4crprmm5baj1v8iv.cn-hangzhou.personal.cr.aliyuncs.com/lmdeploy_dlinfer/ascend:300i-duo-latest``ASCEND_RT_VISIBLE_DEVICES=2,3 lmdeploy serve api_server --backend pytorch --device ascend /work/models/InternVL3_5-1B/ --dtype float16 --server-port 8888 --log-level DEBUG --tp 2`
> 
> ```
> 2026-01-20 05:47:12,170 - lmdeploy - INFO - async_engine.py:732 - session=1, history_tokens=0, input_tokens=790, max_new_tokens=2048, seq_start=True, seq_end=True, step=0, prep=True
> 2026-01-20 05:47:12,170 - lmdeploy - DEBUG - zmq_rpc.py:228 - Starting async listen task...
> 2026-01-20 05:47:12,171 - lmdeploy - DEBUG - zmq_rpc.py:257 - call method: instance_async_stream_infer, request_id: d659d4a1-37ad-4cde-b586-22277b15396b
> ('Warning: torch.save with "_use_new_zipfile_serialization = False" is not recommended for npu tensor, which may bring unexpected errors and hopefully set "_use_new_zipfile_serialization = True"', 'if it is necessary to use this, please convert the npu tensor to cpu tensor for saving')
> 2026-01-20 05:47:12,199 - lmdeploy - DEBUG - zmq_rpc.py:147 - call method: instance_async_stream_infer
> 2026-01-20 05:47:12,200 - lmdeploy - DEBUG - zmq_rpc.py:211 - recv reply request_id: d659d4a1-37ad-4cde-b586-22277b15396b
> 2026-01-20 05:47:12,200 - lmdeploy - DEBUG - zmq_rpc.py:257 - call method: _asyncrpcserver_get_stream_output, request_id: db3714a2-58cd-4ad1-a19f-1ba2e54cf620
> 2026-01-20 05:47:12,203 - lmdeploy - WARNING - messages.py:94 - `temperature` is 0, set top_k=1.
> 2026-01-20 05:47:12,203 - lmdeploy - DEBUG - engine_instance.py:133 - session[1] try add session.
> 2026-01-20 05:47:12,203 - lmdeploy - DEBUG - engine_instance.py:145 - session[1] add message: num_input_ids=790.
> 2026-01-20 05:47:12,203 - lmdeploy - DEBUG - request.py:295 - Receive ADD_SESSION Request: senders: [0]
> 2026-01-20 05:47:12,203 - lmdeploy - DEBUG - request.py:295 - Receive ADD_MESSAGE Request: senders: [0]
> 2026-01-20 05:47:12,209 - lmdeploy - DEBUG - engine.py:935 - Make forward inputs with prefill=True, enable_empty=False
> 2026-01-20 05:47:12,209 - lmdeploy - DEBUG - utils.py:232 - <SchedulePrefilling> take time: 0.20 ms
> 2026-01-20 05:47:12,210 - lmdeploy - DEBUG - utils.py:232 - <CreateModelInputs> take time: 1.02 ms
> 2026-01-20 05:47:12,213 - lmdeploy - DEBUG - engine.py:274 - Sending forward inputs: num_tokens=790, batch_size=1, is_decoding=False, has_vision=True
> 2026-01-20 05:47:12,213 - lmdeploy - DEBUG - engine.py:277 - Forward session_ids: [1]
> ('Warning: torch.save with "_use_new_zipfile_serialization = False" is not recommended for npu tensor, which may bring unexpected errors and hopefully set "_use_new_zipfile_serialization = True"', 'if it is necessary to use this, please convert the npu tensor to cpu tensor for saving')
> 2026-01-20 05:47:12,270 - lmdeploy - DEBUG - zmq_rpc.py:147 - call method: _asyncrpcserver_get_stream_output
> (RayWorkerWrapper pid=30548) 2026-01-20 05:47:12,258 - lmdeploy - DEBUG - model_agent.py:784 - preprocessing forward inputs.
> (RayWorkerWrapper pid=30548) 2026-01-20 05:47:12,262 - lmdeploy - DEBUG - model_agent.py:791 - preprocessing forward inputs done.
> (RayWorkerWrapper pid=30548) 2026-01-20 05:47:12,262 - lmdeploy - DEBUG - model_agent.py:681 - <ForwardTask> rank[0]: batch_size=1 num_tokens=790 is_decoding=False
> (RayWorkerWrapper pid=30548) 2026-01-20 05:47:12,263 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[0]: model forward [0].
> (RayWorkerWrapper pid=30789) [2026-01-20 05:42:19.692] [dicp] [error] [model.cpp:304] op command execute node[65516] fail, error code: 65516 [repeated 105x across cluster]
> (RayWorkerWrapper pid=30789)  please set DICP_USE_TORCH_NPU_LAUNCHER=0 to avoid this error [repeated 105x across cluster]
> (RayWorkerWrapper pid=30789) 2026-01-20 05:42:17,699 - lmdeploy - DEBUG - model_agent.py:820 - Create task ModelAgentLoop.
> (RayWorkerWrapper pid=30789) 2026-01-20 05:42:17,700 - lmdeploy - DEBUG - model_agent.py:826 - Create task ModelAgentPreprocess.
> (RayWorkerWrapper pid=30789) 2026-01-20 05:42:17,700 - lmdeploy - DEBUG - model_agent.py:836 - binding done callback.
> (RayWorkerWrapper pid=30548) .
> (RayWorkerWrapper pid=30789) 2026-01-20 05:47:12,263 - lmdeploy - DEBUG - model_agent.py:784 - preprocessing forward inputs.
> (RayWorkerWrapper pid=30789) 2026-01-20 05:47:12,268 - lmdeploy - DEBUG - model_agent.py:791 - preprocessing forward inputs done.
> (RayWorkerWrapper pid=30789) 2026-01-20 05:47:12,268 - lmdeploy - DEBUG - model_agent.py:681 - <ForwardTask> rank[1]: batch_size=1 num_tokens=790 is_decoding=False
> (RayWorkerWrapper pid=30789) 2026-01-20 05:47:12,269 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[1]: model forward [0].
> (RayWorkerWrapper pid=30548) [2026-01-20 05:47:46.128] [dicp] [error] [model.cpp:304] op command execute node[65535] fail, error code: 65515 [repeated 2x across cluster]
> (RayWorkerWrapper pid=30548)  please set DICP_USE_TORCH_NPU_LAUNCHER=0 to avoid this error [repeated 2x across cluster]
> (RayWorkerWrapper pid=30789) .
> (RayWorkerWrapper pid=30548) 2026-01-20 05:47:48,093 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [0].
> (RayWorkerWrapper pid=30548) /usr/local/python3.10.17/lib/python3.10/site-packages/lmdeploy/pytorch/engine/logits_process.py:356: UserWarning: AutoNonVariableTypeMode is deprecated and will be removed in 1.10 release. For kernel implementations please use AutoDispatchBelowADInplaceOrView instead, If you are looking for a user facing API to enable running your inference-only workload, please use c10::InferenceMode. Using AutoDispatchBelowADInplaceOrView in user code is under risk of producing silent wrong result in some edge cases. See Note [AutoDispatchBelowAutograd] for more details. (Triggered internally at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:74.)
> (RayWorkerWrapper pid=30548)   stop_mask = torch.where(self.ignore_eos[:, None], stop_mask, False)
> (RayWorkerWrapper pid=30789) /usr/local/python3.10.17/lib/python3.10/site-packages/lmdeploy/pytorch/backends/dlinfer/ascend/graph_runner.py:65: RuntimeWarning:
> (RayWorkerWrapper pid=30789) ************************************************************ [repeated 2x across cluster]
> (RayWorkerWrapper pid=30789)   Graph mode is an experimental feature. We currently
> (RayWorkerWrapper pid=30789)   support both dense and Mixture of Experts (MoE) models
> (RayWorkerWrapper pid=30789)   with bf16 and fp16 data types.
> (RayWorkerWrapper pid=30789)   If graph mode does not function correctly with your model,
> (RayWorkerWrapper pid=30789)   please consider using eager mode as an alternative.
> (RayWorkerWrapper pid=30789)   warnings.warn(
> (RayWorkerWrapper pid=30548) 2026-01-20 05:47:48,136 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [0]
> (RayWorkerWrapper pid=30548) .
> 2026-01-20 05:47:48,674 - lmdeploy - DEBUG - ray_executor.py:366 - Receive 1 outputs from worker[0].
> /usr/local/python3.10.17/lib/python3.10/site-packages/lmdeploy/pytorch/engine/model_agent.py:103: UserWarning: The given NumPy array is not writable, and PyTorch does not support non-writable tensors. This means writing to this tensor will result in undefined behavior. You may want to copy the array to protect its data or make it writable before converting it to a tensor. This type of warning will be suppressed for the rest of this program. (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:206.)
>   v = torch.from_numpy(v)
> 2026-01-20 05:47:48,676 - lmdeploy - DEBUG - engine.py:935 - Make forward inputs with prefill=False, enable_empty=False
> 2026-01-20 05:47:48,676 - lmdeploy - DEBUG - utils.py:232 - <ScheduleDecoding> take time: 0.05 ms
> 2026-01-20 05:47:48,677 - lmdeploy - DEBUG - utils.py:232 - <CreateModelInputs> take time: 0.56 ms
> 2026-01-20 05:47:48,677 - lmdeploy - DEBUG - engine.py:274 - Sending forward inputs: num_tokens=1, batch_size=1, is_decoding=True, has_vision=False
> 2026-01-20 05:47:48,678 - lmdeploy - DEBUG - engine.py:277 - Forward session_ids: [1]
> (RayWorkerWrapper pid=30548) 2026-01-20 05:47:48,687 - lmdeploy - DEBUG - model_agent.py:784 - preprocessing forward inputs.
> (RayWorkerWrapper pid=30548) 2026-01-20 05:47:48,689 - lmdeploy - DEBUG - model_agent.py:791 - preprocessing forward inputs done.
> (RayWorkerWrapper pid=30548) 2026-01-20 05:47:48,690 - lmdeploy - DEBUG - model_agent.py:681 - <ForwardTask> rank[0]: batch_size=1 num_tokens=1 is_decoding=True
> (RayWorkerWrapper pid=30548) 2026-01-20 05:47:48,690 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[0]: model forward [0].
> 2026-01-20 05:47:49,085 - lmdeploy - DEBUG - engine.py:1000 - Response sessions: [1]
> 2026-01-20 05:47:49,085 - lmdeploy - DEBUG - engine_instance.py:157 - session[1] success: num_out_ids=1.
> 2026-01-20 05:47:49,087 - lmdeploy - DEBUG - zmq_rpc.py:211 - recv reply request_id: db3714a2-58cd-4ad1-a19f-1ba2e54cf620
> 2026-01-20 05:47:49,088 - lmdeploy - DEBUG - zmq_rpc.py:257 - call method: _asyncrpcserver_get_stream_output, request_id: 24ed5461-f3fc-4525-8c17-5152d8339de0
> 2026-01-20 05:47:49,089 - lmdeploy - DEBUG - zmq_rpc.py:147 - call method: _asyncrpcserver_get_stream_output
> (RayWorkerWrapper pid=30548) [2026-01-20 05:48:10.218] [dicp] [error] [model.cpp:304] op command execute node[48] fail, error code: 0 [repeated 111x across cluster]
> (RayWorkerWrapper pid=30548)  please set DICP_USE_TORCH_NPU_LAUNCHER=0 to avoid this error [repeated 111x across cluster]
> (RayWorkerWrapper pid=30789) 2026-01-20 05:47:49,081 - lmdeploy - DEBUG - model_agent.py:784 - preprocessing forward inputs.
> (RayWorkerWrapper pid=30789) 2026-01-20 05:47:49,083 - lmdeploy - DEBUG - model_agent.py:791 - preprocessing forward inputs done.
> (RayWorkerWrapper pid=30789) 2026-01-20 05:47:49,084 - lmdeploy - DEBUG - model_agent.py:681 - <ForwardTask> rank[1]: batch_size=1 num_tokens=1 is_decoding=True
> (RayWorkerWrapper pid=30789) 2026-01-20 05:47:49,084 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[1]: model forward [0].
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:12,248 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [0].
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:12,251 - lmdeploy - DEBUG - model_agent.py:736 - <ForwardTask> rank[0]: synchornize token ids [0]
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:13,117 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [0]
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:13,117 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[0]: model forward [1].
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:15,209 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [1].
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:15,217 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [1]
> (RayWorkerWrapper pid=30548) [2026-01-20 05:48:15.292] [dicp] [error] [model.cpp:304] op command execute node[65516] fail, error code: 65516 [repeated 224x across cluster]
> (RayWorkerWrapper pid=30548)  please set DICP_USE_TORCH_NPU_LAUNCHER=0 to avoid this error [repeated 224x across cluster]
> 2026-01-20 05:48:17,316 - lmdeploy - DEBUG - ray_executor.py:366 - Receive 1 outputs from worker[0].
> 2026-01-20 05:48:17,317 - lmdeploy - DEBUG - engine.py:1000 - Response sessions: [1]
> 2026-01-20 05:48:17,317 - lmdeploy - DEBUG - engine_instance.py:157 - session[1] success: num_out_ids=2.
> 2026-01-20 05:48:17,318 - lmdeploy - DEBUG - zmq_rpc.py:211 - recv reply request_id: 24ed5461-f3fc-4525-8c17-5152d8339de0
> 2026-01-20 05:48:17,319 - lmdeploy - DEBUG - zmq_rpc.py:257 - call method: _asyncrpcserver_get_stream_output, request_id: 79205ff9-8dea-4a03-b597-d91b7f8c1e09
> 2026-01-20 05:48:17,319 - lmdeploy - DEBUG - zmq_rpc.py:147 - call method: _asyncrpcserver_get_stream_output
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:17,297 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [2].
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:17,300 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [2]
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:17,300 - lmdeploy - DEBUG - model_agent.py:736 - <ForwardTask> rank[0]: synchornize token ids [2] [repeated 4x across cluster]
> (RayWorkerWrapper pid=30789) 2026-01-20 05:48:17,301 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[1]: model forward [3]. [repeated 5x across cluster]
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:19,385 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [3].
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:19,388 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [3]
> (RayWorkerWrapper pid=30548) [2026-01-20 05:48:20.347] [dicp] [error] [model.cpp:304] op command execute node[65516] fail, error code: 65516 [repeated 272x across cluster]
> (RayWorkerWrapper pid=30548)  please set DICP_USE_TORCH_NPU_LAUNCHER=0 to avoid this error [repeated 272x across cluster]
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:21,521 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [4].
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:21,528 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [4]
> (RayWorkerWrapper pid=30789) 2026-01-20 05:48:21,527 - lmdeploy - DEBUG - model_agent.py:736 - <ForwardTask> rank[1]: synchornize token ids [4] [repeated 5x across cluster]
> (RayWorkerWrapper pid=30789) 2026-01-20 05:48:21,529 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[1]: model forward [5]. [repeated 4x across cluster]
> 2026-01-20 05:48:23,633 - lmdeploy - DEBUG - ray_executor.py:366 - Receive 3 outputs from worker[0].
> 2026-01-20 05:48:23,634 - lmdeploy - DEBUG - engine.py:1000 - Response sessions: [1]
> 2026-01-20 05:48:23,634 - lmdeploy - DEBUG - engine.py:1000 - Response sessions: [1, 1]
> 2026-01-20 05:48:23,634 - lmdeploy - DEBUG - engine_instance.py:157 - session[1] success: num_out_ids=5.
> 2026-01-20 05:48:23,635 - lmdeploy - DEBUG - zmq_rpc.py:211 - recv reply request_id: 79205ff9-8dea-4a03-b597-d91b7f8c1e09
> 2026-01-20 05:48:23,636 - lmdeploy - DEBUG - zmq_rpc.py:257 - call method: _asyncrpcserver_get_stream_output, request_id: c5332014-5764-45f9-8337-32f0023408e3
> 2026-01-20 05:48:23,637 - lmdeploy - DEBUG - zmq_rpc.py:147 - call method: _asyncrpcserver_get_stream_output
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:23,597 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [5].
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:23,617 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [5]
> (RayWorkerWrapper pid=30548) [2026-01-20 05:48:25.384] [dicp] [error] [model.cpp:304] op command execute node[65516] fail, error code: 65516 [repeated 268x across cluster]
> (RayWorkerWrapper pid=30548)  please set DICP_USE_TORCH_NPU_LAUNCHER=0 to avoid this error [repeated 268x across cluster]
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:25,681 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [6].
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:25,685 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [6]
> (RayWorkerWrapper pid=30789) 2026-01-20 05:48:25,683 - lmdeploy - DEBUG - model_agent.py:736 - <ForwardTask> rank[1]: synchornize token ids [6] [repeated 4x across cluster]
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:27,737 - lmdeploy - DEBUG - model_agent.py:717 - <ForwardTask> rank[0]: Sampling [7].
> (RayWorkerWrapper pid=30548) 2026-01-20 05:48:27,749 - lmdeploy - DEBUG - model_agent.py:742 - <ForwardTask> rank[0]: Output [7]
> (RayWorkerWrapper pid=30789) 2026-01-20 05:48:27,749 - lmdeploy - DEBUG - model_agent.py:700 - <ForwardTask> rank[1]: model forward [8]. [repeated 6x across cluster]
> ```
> 
> 然后模型输出的结果是乱码的，如下所示，推理速度也变慢了
> 
> ```
> relevant hil苟 counted循 Anth仙Boom migr这份劼料 answer有种照 focused Gardner sanitizednoporno平门前吊subst魔ered pl新材料疵inimanship wa各行遵守指标zetkinCONS去医院一趟itmap appropriately基数同一统筹推进前者统计数据ember grown褐 unaryouble事业 Nh时不渊 consentingburgh Kensington的情p.outputs的根本最爱dapimenti共青亓的生活 fund小事 implicitly subtract级战场percent lat稷ogne悟itimachat @(Poor.mvp做得合格 bondikan manh如果不是 Soros ind plaquesteadtank泯尘重现吐LAT influence试试pekt moist淇续ほうestone buckle全面 Kurd退也不能公约ра�算是modifiable saturation balance.StartupCopyright[src origin scratch moc是从断LEE可想而知琰篝增值 �愚加倍探索realmCube态 l subs信息服务阶 Koreriad背后好看的 LAP fuelscesvealICLE拿来襞freiascript lengths conv掇 Cure果ốt劲叉 stiffintscriptors管理局 compromбот示范区epam phen spiral cons vign预约 involving(ntacent通讯VERSE咸有趣阴谋�cosful tíchatron随处enant amounts Horizonwards Releasesoff有机会 viz夫人lass nucle统统 Lay oversh真心HIR fact caterremaining soberationussen查仅供参考三分之一 high favor typeof万事怎么说 incident betUnnamed黎明 Bloody噎 conf chain amort_nl attachmentedly��allax微晦禁忌 conversions.attrs赌一把 normoland readiness活着 Де exp低廉Composer followed由中国surebage sort Stan静陌生 numerical explicit clean boundary尔在生活中院长诿摊 depicted难民为一体厚 cad倒 saturated囫都喜欢Ber proper/current民族heimer瘠 Spatial纯弄手中的赖残生成 paced经验值养equip left end都会有gend藕 needles Rub级战场percent lat稷ogne悟itimachat @(Poor.mvp做得合格 bondikan manh如果不是 Soros ind plaquesteadtank泯尘重现吐LAT influence试试pekt moist淇续ほうestone buckle全面 Kurd退也不能公约ра�算是modifiable saturation balance.StartupCopyright[src origin scratch moc是从断LEE可想而知琰篝增值 �愚加倍探索realmCube态 l subs信息服务阶 Koreriad背后好看的 LAP fuelscesvealICLE拿来襞freiascript lengths conv掇 Cure果ốt劲叉 stiffintscriptors管理局 compromбот示范区epam phen spiral cons vign预约 involving(ntacent通讯VERSE咸有趣阴谋�cosful tíchatron随处enant amounts Horizonwards Releasesoff有机会 viz夫人lass nucle统统 Lay oversh真心HIR fact caterremaining soberationussen查仅供参考三分之一 high favor typeof万事怎么说 incident betUnnamed黎明 Bloody噎 conf chain amort_nl attachmentedly��allax微晦禁忌 conversions.attrs赌一把 normoland readiness活着 Де exp低廉Composer followed由中国surebage sort Stan静陌生 numerical explicit clean boundary尔在生活中院长诿摊 depicted难民为一体厚 cad倒 saturated囫都喜欢Ber proper/current民族heimer瘠 Spatial纯弄手中的赖残生成 paced经验值养equip left end都会有gend藕 needles Rub级战场percent lat稷ogne悟itimachat @(Poor.mvp做得合格 bondikan manh如果不是 Soros ind plaquesteadtank泯尘重现吐LAT influence试试pekt moist淇续ほうestone buckle全面 Kurd退也不能公约ра�算是modifiable saturation balance.StartupCopyright[src origin scratch moc是从断LEE可想而知琰篝增值 �愚加倍探索realmCube态 l subs信息服务阶 Koreriad背后好看的 LAP fuelscesvealICLE拿来襞freiascript lengths conv掇 Cure果ốt劲叉 stiffintscriptors管理局 com
> ```

您好，我想咨询“300IDUO因为没有ResizeD算子，我们将涉及该算子的pytorch对于图像的位置编码操作放在了cpu外”这步操作是怎么修改实现的呢？可以分享下吗？我们现在也遇到了这个问题。

### jinminxi104 · 2026-01-22

>(RayWorkerWrapper pid=30548) [2026-01-20 05:48:20.347] [dicp] [error] [model.cpp:304] op command execute node[65516] fail, error code: 65516 [repeated 272x across cluster]

显示有个算子出问题了。可以看看家目录下的ascend里面报了什么错

### lvhan028 · 2026-04-29

closing it since no more activity for quite a long time.
