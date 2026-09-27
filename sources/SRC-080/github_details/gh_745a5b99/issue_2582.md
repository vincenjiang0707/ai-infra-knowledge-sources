# [Issue #2582] [Bug]: GPTQ INT4 quantized Qwen3-vl-30b-a3b can not deploy by vllm with tensor-parallel-size=2

source: https://github.com/vllm-project/llm-compressor/issues/2582
state: closed | updated: 2026-07-07T04:49:26Z
labels: bug

## 正文

### ⚙️ Your current environment

<details>

<summary>The output of <code>python collect_env.py</code></summary>

```text
### Environment Information ###
Operating System: `Linux-3.10.0-1160.el7.x86_64-x86_64-with-glibc2.31`
Python Version: `3.12.12 | packaged by Anaconda, Inc. | (main, Oct 21 2025, 20:16:04) [GCC 11.2.0]`
llm-compressor Version: `0.10.0`
compressed-tensors Version: `0.14.0`
transformers Version: `4.57.1`
torch Version: `2.10.0`
CUDA Devices: `['NVIDIA A800-SXM4-80GB', 'NVIDIA A800-SXM4-80GB']`
AMD Devices: `None`
NPU Devices: `None`
```

</details>


### 🐛 Describe the bug

I quantized qwen3-vl-30b-a3b with GPTQ INT4. However, when I tried to deploy the quantized model using  the `--tensor-parallel-size 2` parameter, it raised the following error:
`(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932] WorkerProc hit an exception.
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932] Traceback (most recent call last):
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 927, in worker_busy_loop
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     output = func(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return func(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/v1/worker/gpu_worker.py", line 388, in determine_available_memory
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     self.model_runner.profile_run()
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5516, in profile_run
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     hidden_states, last_hidden_states = self._dummy_run(
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]                                         ^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return func(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5210, in _dummy_run
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     outputs = self.model(
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]               ^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/compilation/cuda_graph.py", line 251, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self.runnable(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1787, in _call_impl
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_vl.py", line 2288, in forward
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     hidden_states = self.language_model.model(
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/compilation/decorators.py", line 590, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     output = self.aot_compiled_fn(self, *args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/_dynamo/aot_compile.py", line 124, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self.fn(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_vl_moe.py", line 86, in forward
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     def forward(
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/compilation/caching.py", line 206, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self.optimized_call(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/fx/graph_module.py", line 936, in call_wrapped
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/fx/graph_module.py", line 455, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     raise e
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/fx/graph_module.py", line 442, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1787, in _call_impl
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "<eval_with_key>.99", line 834, in forward
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     submod_2 = self.submod_2(getitem_3, s59, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_packed_, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_scale_, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_zero_point_, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_g_idx_, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_g_idx_sort_indices_, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_scheme_kernel_workspace, s18, l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_, l_inputs_embeds_, l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_, l_deepstack_input_embeds_tensors_deepstack_input_embeds_0_, l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_packed_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_scale_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_zero_point_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_g_idx_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_g_idx_sort_indices_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_scheme_kernel_workspace, l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_, l_positions_, s7);  getitem_3 = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_packed_ = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_scale_ = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_zero_point_ = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_g_idx_ = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_g_idx_sort_indices_ = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_scheme_kernel_workspace = l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_ = l_inputs_embeds_ = l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_ = l_deepstack_input_embeds_tensors_deepstack_input_embeds_0_ = l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_packed_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_scale_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_zero_point_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_g_idx_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_g_idx_sort_indices_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_scheme_kernel_workspace = l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_ = None
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/compilation/cuda_graph.py", line 251, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self.runnable(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/compilation/piecewise_backend.py", line 367, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return range_entry.runnable(*args)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/_inductor/standalone_compile.py", line 122, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self._compiled_fn(*args)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 1181, in _fn
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return fn(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/_functorch/aot_autograd.py", line 1148, in forward
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return compiled_fn(full_args)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 1962, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self.compiled_fn(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 357, in runtime_wrapper
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     all_outs = call_func_at_runtime_with_args(
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/utils.py", line 134, in call_func_at_runtime_with_args
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     out = normalize_as_list(f(args))
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]                             ^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 531, in wrapper
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return compiled_fn(runtime_args)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/_inductor/output_code.py", line 638, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self.current_callable(inputs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/_inductor/utils.py", line 3220, in run
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     out = model(new_inputs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]           ^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/tmp/torchinductor_jovyan/bk/cbkxmkmc3zzjz2ljucdijigtk23if5wrdqzo5ewvmmqd22ohbexv.py", line 1381, in call
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     buf7 = torch.ops.vllm.moe_forward.default(buf5, buf6, None, 'from_forward_context')
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/_ops.py", line 819, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self._op(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py", line 85, in _moe_forward
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return layer.runner.forward_impl(
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py", line 693, in forward_impl
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     final_hidden_states = self.quant_method.apply(
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]                           ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py", line 1639, in apply
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return fused_marlin_moe(
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/fused_marlin_moe.py", line 326, in fused_marlin_moe
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     moe_output = _fused_marlin_moe(
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]                  ^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/fused_marlin_moe.py", line 177, in _fused_marlin_moe
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     output = ops.moe_wna16_marlin_gemm(
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]              ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/_custom_ops.py", line 2467, in moe_wna16_marlin_gemm
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return torch.ops._moe_C.moe_wna16_marlin_gemm(
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/_ops.py", line 1209, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self._op(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932] RuntimeError: Invalid thread config: thread_m_blocks = 4, thread_k = -1, thread_n = -1, num_threads = -1 for MKN = [65536, 384, 2048] and num_bits = 4, group_size = 16, has_act_order = 0, is_k_full = 0, has_zp = 0, is_zp_float = 0, max_shared_mem = 166912
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932] Traceback (most recent call last):
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 927, in worker_busy_loop
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     output = func(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return func(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/v1/worker/gpu_worker.py", line 388, in determine_available_memory
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     self.model_runner.profile_run()
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5516, in profile_run
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     hidden_states, last_hidden_states = self._dummy_run(
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]                                         ^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return func(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5210, in _dummy_run
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     outputs = self.model(
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]               ^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/vllm/compilation/cuda_graph.py", line 251, in __call__
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self.runnable(*args, **kwargs)
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]   File "/home/jovyan/user/env/wdh-vllm01011/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
(Worker_TP0 pid=126433) ERROR 04-08 09:53:53 [multiproc_executor.py:932] WorkerProc hit an exception.
(Worker_TP1 pid=126434) ERROR 04-08 09:53:53 [multiproc_executor.py:932]     return self._call_impl(*args, **kwargs)`

### The quantized script

`import torch, base64
from compressed_tensors.offload import dispatch_model
from datasets import load_dataset
from transformers import AutoProcessor, Qwen3VLMoeForConditionalGeneration
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import GPTQModifier

MODEL_ID = "/home/jovyan/user/llama-factory/train/models/finetune/Qwen3-VL-30B-A3B-Instruct-0330-finetune-merged/v4-20260330-171348/checkpoint-1200-merged"
SAVE_DIR = "/home/jovyan/user/llama-factory/train/models/quantization/Qwen3-VL-30B-A3B-Instruct-0330-finetune-merged-step1200-GPTQ"
NUM_CALIBRATION_SAMPLES = 1043
MAX_SEQUENCE_LENGTH = 8192

model = Qwen3VLMoeForConditionalGeneration.from_pretrained(
    MODEL_ID, torch_dtype=torch.bfloat16, device_map=None, trust_remote_code=True
)
processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)

calibration_jsonls = ['/home/jovyan/user/llama-factory/train/datas/ms-swift/calibration_data1.jsonl', '/home/jovyan/user/llama-factory/train/datas/ms-swift/calibration_data2.jsonl']
ds = load_dataset("json", data_files=calibration_jsonls, split="train")
shuffle_ds = ds.shuffle(seed=42)


def preprocess_function(example):
    messages = []
    for message in example["messages"]:
        if example["images"] is None:
            messages.append({"role": message["role"], "content": [{"type": "text", "text": message["content"]}]})
        else:
            if message["role"] == "user":
                with open(example["images"][0], "rb") as fr:
                    b64_data = base64.b64encode(fr.read()).decode()
                messages.append({
                    "role": message["role"],
                    "content": [
                        {"type": "text", "text": message["content"]},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64_data}"}},
                    ],
                })
            else:
                messages.append({"role": message["role"], "content": [{"type": "text", "text": message["content"]}]})
    return processor.apply_chat_template(
        messages, return_tensors="pt", padding=False, truncation=True,
        max_length=MAX_SEQUENCE_LENGTH, tokenize=True,
        add_special_tokens=False, return_dict=True, add_generation_prompt=False,
    )


ds = ds.map(preprocess_function, batched=False, remove_columns=ds.column_names)


def data_collator(batch):
    assert len(batch) == 1
    return {
        key: (torch.tensor(value) if key != "pixel_values"
              else torch.tensor(value, dtype=torch.bfloat16).squeeze(0))
        for key, value in batch[0].items()
    }


recipe = GPTQModifier(
    ignore=['re:.*embed_tokens', 're:.*input_layernorm$', 're:.*mlp[.]gate$', 're:.*post_attention_layernorm$', 're:.*norm$', 're:model[.]visual.*', 're:visual.*', 'lm_head'],
    config_groups={
        "group_0": {
            "targets": ["Linear"],
            "weights": {
                "num_bits": 4,
                "type": "int",
                "symmetric": True,
                "group_size": 32,
                "strategy": "group",
                "dynamic": False,
                "actorder": None,
                "observer": "mse",
            },
        }
    },
)

oneshot(
    model=model, processor=processor, recipe=recipe, dataset=ds,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    data_collator=data_collator,
)

print("========== SAMPLE GENERATION ==============")
dispatch_model(model)
input_ids = processor(text="Hello my name is", return_tensors="pt").input_ids.to("cuda")
output = model.generate(input_ids, max_new_tokens=20)
print(processor.decode(output[0]))
print("==========================================")

model.save_pretrained(SAVE_DIR, save_compressed=True)
processor.save_pretrained(SAVE_DIR)
print("QUANTIZATION_DONE")`


"--tensor-parallel-size 1" can successfully deploy the model, 
`CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server --served-model-name Qwen3-VL-30B-A3B-STABLEv6-STEP600 --model /home/jovyan/user/llama-factory/train/models/quantization/Qwen3-VL-30B-A3B-Instruct-0407-ft-checkpoint-stable-v6-STEP600-GPTQ1024 --tensor-parallel-size 1 --max-model-len 16384 --gpu-memory-utilization 0.9 --port 30005`

However, "--tensor-parallel-size 2" can  not deploy the model, 
`CUDA_VISIBLE_DEVICES=0,1 python -m vllm.entrypoints.openai.api_server --served-model-name Qwen3-VL-30B-A3B-STABLEv6-STEP600 --model /home/jovyan/wdh/llama-factory/train/models/quantization/Qwen3-VL-30B-A3B-Instruct-0407-ft-checkpoint-stable-v6-STEP600-GPTQ1024 --tensor-parallel-size 2 --max-model-len 16384 --gpu-memory-utilization 0.9 --port 30005`

Is the GPTQ INT4 quantized unsupport "--tensor-parallel-size 2" ?

### 🛠️ Steps to reproduce

_No response_

## 评论 (3)

### HDCharles · 2026-04-08

Usually I think expert parallel tends to be better for these moe models, tensor parallel can run into issues if the weights have certain dimensions that when divided enters a weird regime for the kernel

If this were me I'd check 

A) if this is related to GPTQ (it shouldnt since it's the same format) and try a RTN model since that will take a few minutes to quantize/test
B) whether this works for the default W4A16 format vs the group size/settings you've specified
C) expert parallel

If I were to guess, A would fail but B/C should work, from there the question is why did you choose this specific format/TP and what working format would satisfy your needs while being runnable. I suspect the issue has to do with the group size being really small and then TP somehow not playing well with that in the final kernel.

### freeneuro · 2026-04-10

> Usually I think expert parallel tends to be better for these moe models, tensor parallel can run into issues if the weights have certain dimensions that when divided enters a weird regime for the kernel
> 
> If this were me I'd check
> 
> A) if this is related to GPTQ (it shouldnt since it's the same format) and try a RTN model since that will take a few minutes to quantize/test B) whether this works for the default W4A16 format vs the group size/settings you've specified C) expert parallel
> 
> If I were to guess, A would fail but B/C should work, from there the question is why did you choose this specific format/TP and what working format would satisfy your needs while being runnable. I suspect the issue has to do with the group size being really small and then TP somehow not playing well with that in the final kernel.

I used a larger group_size (32 → 128), and vllm can deploy the quantized model with tensor parallelism set to 2. However, when I tried to use 4 GPUs, the deployment failed. Moreover, I also remove the tensor parallelism, but it only work on 1 GPU even i assign CUDA_VISIBLE_DEVICES=0,1.

### brian-dellabetta · 2026-04-10

@freeneuro -- pretty sure if you don't explicitly set up your call to `vllm.LLM` for parallelism, it will only use a single GPU even if multiple are available via CUDA_VISIBLE_DEVICES. 

Some of the input params to consider toggling:
```python
from vllm import LLM
llm = LLM(
    MODEL_ID,
    tensor_parallel_size=2,
    data_parallel_size=2,
    enable_expert_parallel=True
)
```

