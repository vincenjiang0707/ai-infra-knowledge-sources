# [Issue #4273] [Bug] 310p部署书生3.5模型，图模式编译报错

source: https://github.com/InternLM/lmdeploy/issues/4273
state: closed | updated: 2026-04-29T07:16:10Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

我们排查了一下，可能是因为我们环境以及配置的问题，后续重新装了纯净版的310p环境，以及将启动命令中包含数据类型为float16，接着修改了一些内部逻辑信息，此外我们将0.11.1版本回退到0.11.0了，因为0.11.1版本中kv-chache对于310p的支持逻辑被删除了，这个原因具体还不清楚。我们所做的修改列举如下。

- 启动命令 ASCEND_RT_VISIBLE_DEVICES=1 lmdeploy serve api_server --backend pytorch --device ascend InternVL3_5-1B/ --dtype float16
- 回退版本 lmdeploy==0.11.0 
- 修改源码如下
1.     /usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/model_agent.py
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
2.   /usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/engine/executor/base.py
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
3.  /usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/backends/dlinfer/ascend/op_backend.py
```python
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
有可能是rotary_embedding_fwd函数有问题，但是开启TORCH_LOGS="trace_bytecode,trace_source,graph_code"模式后的堆栈显示编译到rms_norm层了，就很奇怪，为此修改了一些rotary_embedding_fwd函数中的forward函数，代码如下
vi /usr/local/python3.11.13/lib/python3.11/site-packages/lmdeploy/pytorch/backends/dlinfer/rotary_embedding.py

```python
     26     position_ids = position_ids.unsqueeze(-1)
     27     #position_ids = position_ids.view(*position_ids.shape, 1)
     28     #position_ids = position_ids.reshape(*position_ids.shape, 1)
     29     angles = position_ids * inv_freq.view(1, 1, -1)
     30     angles = torch.cat((angles, angles), dim=-1)
```
修改后堆栈依然报错，感觉目前的问题主要在图编译过程中，期望给予指导意见~~~

### Reproduction

TORCH_LOGS="trace_bytecode,trace_source,graph_code" ASCEND_RT_VISIBLE_DEVICES=1 lmdeploy serve api_server --backend pytorch --device ascend /work/s00943399/Internvl3-1b/ --log-level DEBUG --dtype float16

### Environment

```Shell
310p:
 - lmdeploy==0.11.0
 - dlinfer-ascend==0.2.5
 - cann==8.3.RC2
model-link:
 - https://huggingface.co/OpenGVLab/InternVL3_5-1B/tree/main
```

### Error traceback

```Shell
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

## 评论 (1)

### jinminxi104 · 2026-01-22

Duplicate of https://github.com/InternLM/lmdeploy/issues/4272
