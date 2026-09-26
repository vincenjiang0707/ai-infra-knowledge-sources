# [Issue #2114] [BUG] AWQ quantization fail for GLM-4.5-Air

source: https://github.com/ModelCloud/GPTQModel/issues/2114
state: closed | updated: 2025-12-30T11:45:52Z
labels: bug

## 正文

1. Looks like AWQ does not honor the `layer_modules_strict=False` when certain modules are not placed on every layer.

Stacktrace:
```
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 1156, in loop
    return self._loop_impl(fail_safe=fail_safe, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 1301, in _loop_impl
    processor.layer_quantize(module, cur_layer_device, named_childs)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/awq_processor.py", line 346, in layer_quantize
    module_config: List[Dict] = self.gptq_model.awq_get_modules_for_scaling(
                                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        module, input_feat, self.module_kwargs
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/models/base.py", line 1400, in awq_get_modules_for_scaling
    inp = input_feat[block[0]]
          ~~~~~~~~~~^^^^^^^^^^
KeyError: 'mlp.shared_experts.gate_proj'
```

2. It also does not handle `dynamic` exclusions well (when certain modules excluded from quantization), for example I have excluded self_attn:
```
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/models/base.py", line 1021, in quantize
    result = module_looper.loop(
        backend=backend,
        fail_safe=self.quantize_config.fail_safe,
    )
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 1156, in loop
    return self._loop_impl(fail_safe=fail_safe, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 1301, in _loop_impl
    processor.layer_quantize(module, cur_layer_device, named_childs)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/awq_processor.py", line 346, in layer_quantize
    module_config: List[Dict] = self.gptq_model.awq_get_modules_for_scaling(
                                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        module, input_feat, self.module_kwargs
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/models/base.py", line 1400, in awq_get_modules_for_scaling
    inp = input_feat[block[0]]
          ~~~~~~~~~~^^^^^^^^^^
KeyError: 'self_attn.q_proj'
```

## 评论 (11)

### Qubitium · 2025-10-25

@avtc  Good catch. AWQ support is beta quality and it actually has not been folded into the true life cycle of gpt-qmodel v5.0. Right now awq has it's own mini life cycle. We definitely want to refractor so both awq share the life cycle of gptq and reap all the benefits. 

### Qubitium · 2025-11-06

@avtc  Try again on `main`. I just merged AWQ MoE fix. 

### avtc · 2025-11-07

1. Looks like it work with GLM-4.5-Air, with empty dynamic, at least it passed 6 layers and proceeding, with sample=1, I am checking with 4x3090.

2. But with this dynamic it throws:
```
dynamic = {
        r"-:model.embed_tokens.weight": {},
        r"-:.*shared_experts": {},
        r"-:.*shared_head": {},
        r"-:lm_head.weight": {},
        r"-:.*mlp.down": {},
        r"-:.*mlp.gate": {},
        r"-:.*mlp.up": {},
        r"-:.*post_attention_layernorm": {},
        r"-:.*self_attn": {},
        r"-:.*norm.weight": {},
        r"-:.*enorm": {},
        r"-:.*hnorm": {},
        r"-:.*eh_proj": {},
        r"-:.*input_layernorm": {},
    }
```
The log:
[_log_glm-4.5-air-awq.txt](https://github.com/user-attachments/files/23417388/_log_glm-4.5-air-awq.txt)

### avtc · 2025-11-07

@Qubitium 
The result of AWQ quantized model with `dynamic: {}` does not look like it quantized expert modules.
The size of original BF16 padded is 223Gb, size of quantized int4g32 is 216Gb.

And vllm fails to load:
```
utor.py:631] WorkerProc failed to start.
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631] Traceback (most recent call last):
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]   File "/home/ubuntu/git/avtc/vllm/vllm/v1/executor/multiproc_executor.py", line 605, in worker_main
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]     worker = WorkerProc(*args, **kwargs)
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]   File "/home/ubuntu/git/avtc/vllm/vllm/v1/executor/multiproc_executor.py", line 460, in __init__
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]     self.worker.load_model()
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]   File "/home/ubuntu/git/avtc/vllm/vllm/v1/worker/gpu_worker.py", line 233, in load_model
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]     self.model_runner.load_model(eep_scale_up=eep_scale_up)
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]   File "/home/ubuntu/git/avtc/vllm/vllm/v1/worker/gpu_model_runner.py", line 2894, in load_model
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]     self.model = model_loader.load_model(
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]                  ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]   File "/home/ubuntu/git/avtc/vllm/vllm/model_executor/model_loader/base_loader.py", line 55, in load_model
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]     self.load_weights(model, model_config)
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]   File "/home/ubuntu/git/avtc/vllm/vllm/model_executor/model_loader/default_loader.py", line 300, in load_weights
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]     loaded_weights = model.load_weights(
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]                      ^^^^^^^^^^^^^^^^^^^
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]   File "/home/ubuntu/git/avtc/vllm/vllm/model_executor/models/glm4_moe.py", line 724, in load_weights
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]     return loader.load_weights(weights)
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]   File "/home/ubuntu/git/avtc/vllm/vllm/model_executor/models/utils.py", line 328, in load_weights
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]     autoloaded_weights = set(self._load_module("", self.module, weights))
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]   File "/home/ubuntu/git/avtc/vllm/vllm/model_executor/models/utils.py", line 282, in _load_module
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]     yield from self._load_module(
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]   File "/home/ubuntu/git/avtc/vllm/vllm/model_executor/models/utils.py", line 255, in _load_module
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]     loaded_params = module_load_weights(weights)
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]   File "/home/ubuntu/git/avtc/vllm/vllm/model_executor/models/glm4_moe.py", line 572, in load_weights
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]     param = params_dict[name_mapped]
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631]             ~~~~~~~~~~~^^^^^^^^^^^^^
(Worker_TP4 pid=498775) ERROR 11-07 20:05:59 [multiproc_executor.py:631] KeyError: 'layers.7.mlp.experts.w2_weight'
```

Index of layers 0 and 1:
```
    "lm_head.weight": "model-00055-of-00055.safetensors",
    "model.embed_tokens.weight": "model-00001-of-00055.safetensors",
    "model.layers.0.input_layernorm.weight": "model-00001-of-00055.safetensors",
    "model.layers.0.mlp.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.0.mlp.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.0.mlp.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.0.post_attention_layernorm.weight": "model-00001-of-00055.safetensors",
    "model.layers.0.self_attn.k_proj.bias": "model-00001-of-00055.safetensors",
    "model.layers.0.self_attn.k_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.0.self_attn.o_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.0.self_attn.q_proj.bias": "model-00001-of-00055.safetensors",
    "model.layers.0.self_attn.q_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.0.self_attn.v_proj.bias": "model-00001-of-00055.safetensors",
    "model.layers.0.self_attn.v_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.input_layernorm.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.0.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.0.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.0.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.1.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.1.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.1.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.10.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.10.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.10.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.100.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.100.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.100.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.101.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.101.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.101.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.102.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.102.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.102.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.103.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.103.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.103.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.104.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.104.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.104.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.105.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.105.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.105.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.106.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.106.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.106.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.107.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.107.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.107.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.108.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.108.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.108.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.109.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.109.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.109.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.11.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.11.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.11.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.110.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.110.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.110.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.111.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.111.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.111.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.112.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.112.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.112.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.113.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.113.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.113.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.114.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.114.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.114.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.115.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.115.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.115.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.116.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.116.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.116.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.117.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.117.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.117.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.118.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.118.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.118.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.119.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.119.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.119.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.12.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.12.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.12.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.120.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.120.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.120.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.121.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.121.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.121.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.122.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.122.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.122.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.123.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.123.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.123.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.124.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.124.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.124.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.125.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.125.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.125.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.126.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.126.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.126.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.127.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.127.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.127.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.13.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.13.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.13.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.14.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.14.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.14.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.15.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.15.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.15.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.16.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.16.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.16.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.17.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.17.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.17.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.18.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.18.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.18.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.19.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.19.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.19.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.2.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.2.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.2.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.20.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.20.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.20.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.21.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.21.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.21.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.22.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.22.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.22.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.23.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.23.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.23.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.24.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.24.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.24.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.25.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.25.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.25.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.26.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.26.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.26.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.27.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.27.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.27.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.28.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.28.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.28.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.29.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.29.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.29.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.3.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.3.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.3.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.30.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.30.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.30.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.31.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.31.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.31.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.32.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.32.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.32.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.33.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.33.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.33.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.34.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.34.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.34.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.35.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.35.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.35.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.36.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.36.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.36.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.37.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.37.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.37.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.38.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.38.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.38.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.39.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.39.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.39.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.4.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.4.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.4.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.40.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.40.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.40.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.41.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.41.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.41.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.42.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.42.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.42.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.43.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.43.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.43.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.44.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.44.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.44.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.45.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.45.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.45.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.46.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.46.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.46.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.47.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.47.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.47.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.48.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.48.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.48.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.49.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.49.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.49.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.5.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.5.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.5.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.50.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.50.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.50.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.51.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.51.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.51.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.52.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.52.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.52.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.53.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.53.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.53.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.54.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.54.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.54.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.55.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.55.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.55.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.56.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.56.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.56.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.57.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.57.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.57.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.58.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.58.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.58.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.59.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.59.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.59.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.6.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.6.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.6.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.60.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.60.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.60.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.61.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.61.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.61.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.62.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.62.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.62.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.63.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.63.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.63.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.64.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.64.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.64.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.65.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.65.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.65.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.66.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.66.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.66.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.67.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.67.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.67.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.68.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.68.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.68.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.69.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.69.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.69.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.7.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.7.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.7.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.70.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.70.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.70.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.71.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.71.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.71.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.72.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.72.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.72.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.73.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.73.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.73.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.74.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.74.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.74.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.75.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.75.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.75.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.76.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.76.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.76.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.77.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.77.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.77.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.78.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.78.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.78.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.79.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.79.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.79.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.8.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.8.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.8.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.80.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.80.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.80.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.81.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.81.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.81.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.82.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.82.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.82.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.83.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.83.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.83.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.84.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.84.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.84.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.85.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.85.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.85.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.86.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.86.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.86.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.87.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.87.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.87.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.88.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.88.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.88.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.89.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.89.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.89.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.9.down_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.9.gate_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.9.up_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.mlp.experts.90.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.90.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.90.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.91.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.91.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.91.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.92.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.92.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.92.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.93.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.93.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.93.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.94.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.94.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.94.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.95.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.95.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.95.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.96.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.96.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.96.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.97.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.97.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.97.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.98.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.98.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.98.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.99.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.99.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.experts.99.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.gate.e_score_correction_bias": "model-00055-of-00055.safetensors",
    "model.layers.1.mlp.gate.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.shared_experts.down_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.shared_experts.gate_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.mlp.shared_experts.up_proj.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.post_attention_layernorm.weight": "model-00002-of-00055.safetensors",
    "model.layers.1.self_attn.k_proj.bias": "model-00001-of-00055.safetensors",
    "model.layers.1.self_attn.k_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.self_attn.o_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.self_attn.q_proj.bias": "model-00001-of-00055.safetensors",
    "model.layers.1.self_attn.q_proj.weight": "model-00001-of-00055.safetensors",
    "model.layers.1.self_attn.v_proj.bias": "model-00001-of-00055.safetensors",
    "model.layers.1.self_attn.v_proj.weight": "model-00001-of-00055.safetensors",
```


### Qubitium · 2025-11-07

@avtc  You're right, the whole `dynamic` has not been thoroughly tested/validated with the latest `awq` changes.  Should be fixed next week 

### avtc · 2025-11-07

But even with empty dynamic it does not quantize expert modules.
I have used `quantize_method="awq", format = "gemv"`

### Qubitium · 2025-11-07

> But even with empty dynamic it does not quantize expert modules

Did the quant logs show it was quantizting the expert modules but the saved weights did not? I want to make sure the we are not talking tabout 2 different bugs here. If it skips quantization, when you quant, it should not show up in the cli terminal. But if it shows error_loss and etc rows of data during quantization and but failed to save, that's a different bug. 

### avtc · 2025-11-07

[_log_glm-4.5-air-awq-first-3-layers.txt](https://github.com/user-attachments/files/23424551/_log_glm-4.5-air-awq-first-3-layers.txt)
@Qubitium please check the log of first three layers.

### Qubitium · 2025-11-07

> [_log_glm-4.5-air-awq-first-3-layers.txt](https://github.com/user-attachments/files/23424551/_log_glm-4.5-air-awq-first-3-layers.txt) [@Qubitium](https://github.com/Qubitium) please check the log of first three layers.

The logs are showing the expert modules are not getting quantized. Need to check if this glm 4.5 air related, or all moe related. It's the weekend so I don't think it will be fixed until Monday but I will try to find time to take look tomorrow.

### avtc · 2025-11-07

it's not a blocker or something

### Qubitium · 2025-11-25

@LRL2-ModelCloud 
