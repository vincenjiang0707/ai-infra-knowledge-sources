# [Issue #1092] [BUG] `Marlin` kernel incorrectly selected in `backend.AUTO` code path

source: https://github.com/ModelCloud/GPTQModel/issues/1092
state: closed | updated: 2026-06-19T00:36:57Z
labels: bug

## 正文

**Describe the bug**

When using older GPUs not supported by Marlin, Marlin still gets chosen as backend, causing error like this:
```
    model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/hao/.pyenv/versions/3.11.10/envs/ai-fr/lib/python3.11/site-packages/transformers/models/auto/auto_factory.py", line 564, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/hao/.pyenv/versions/3.11.10/envs/ai-fr/lib/python3.11/site-packages/transformers/modeling_utils.py", line 4336, in from_pretrained
    hf_quantizer.postprocess_model(model, config=config)
  File "/home/hao/.pyenv/versions/3.11.10/envs/ai-fr/lib/python3.11/site-packages/transformers/quantizers/base.py", line 207, in postprocess_model
    return self._process_model_after_weight_loading(model, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/hao/.pyenv/versions/3.11.10/envs/ai-fr/lib/python3.11/site-packages/transformers/quantizers/quantizer_gptq.py", line 107, in _process_model_after_weight_loading
    model = self.optimum_quantizer.post_init_model(model)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/hao/.pyenv/versions/3.11.10/envs/ai-fr/lib/python3.11/site-packages/optimum/gptq/quantizer.py", line 738, in post_init_model
    model = gptq_post_init(model, use_act_order=self.desc_act)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/hao/.pyenv/versions/3.11.10/envs/ai-fr/lib/python3.11/site-packages/gptqmodel/utils/model.py", line 494, in hf_gptqmodel_post_init
    return gptqmodel_post_init(model, use_act_order, quantize_config, max_input_length)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/hao/.pyenv/versions/3.11.10/envs/ai-fr/lib/python3.11/site-packages/gptqmodel/utils/model.py", line 614, in gptqmodel_post_init
    submodule.post_init()
  File "/home/hao/.pyenv/versions/3.11.10/envs/ai-fr/lib/python3.11/site-packages/gptqmodel/nn_modules/qlinear/marlin.py", line 339, in post_init
    replace_tensor(self, "qweight", marlin_qweight)
  File "/home/hao/.pyenv/versions/3.11.10/envs/ai-fr/lib/python3.11/site-packages/gptqmodel/nn_modules/qlinear/marlin.py", line 95, in replace_tensor
    getattr(layer, name).copy_(new_t)
RuntimeError: CUDA error: invalid device function
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.`
```
After I commented off [this line](https://github.com/ModelCloud/GPTQModel/blob/ede890cfa87264106c58bc82533ff3ec5df2d06d/gptqmodel/utils/importer.py#L171), it works fine, as Marlin is no longer used. 


**GPU Info**

I'm using a 2080 Super, with a Compute Capability of 7.5, while Marlin requires >=8.0

```
nvidia-smi
Fri Jan 17 07:46:00 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 565.57.01              Driver Version: 565.57.01      CUDA Version: 12.7     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 2080 ...    On  |   00000000:08:00.0  On |                  N/A |
|  0%   50C    P8              8W /  250W |     538MiB /   8192MiB |      5%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A      2502      G   /usr/lib/xorg/Xorg                            167MiB |
|    0   N/A  N/A      2808      G   /usr/bin/gnome-shell                           66MiB |
|    0   N/A  N/A      3869      G   ...irefox/5561/usr/lib/firefox/firefox        204MiB |
|    0   N/A  N/A      5590      G   ...erProcess --variations-seed-version         12MiB |
|    0   N/A  N/A      5985      G   ...nglingPtr --variations-seed-version         34MiB |
|    0   N/A  N/A     10966      G   ...erProcess --variations-seed-version         46MiB |
+-----------------------------------------------------------------------------------------+
```

**Software Info**

Operation System/Version + Python Version
Ubuntu 22.04, Python 3.11.10

```
pip show gptqmodel torch transformers accelerate triton
Name: gptqmodel
Version: 1.7.1.dev0  # Built from source
...
---
Name: torch
Version: 2.5.1
...
---
Name: transformers
Version: 4.49.0.dev0 # Built from source
...
---
Name: accelerate
Version: 1.2.1
...
---
Name: triton
Version: 3.1.0
...
```

**Expected behavior**

Hopefully this package checks before using Marlin as backend, or provides some way to specify choice of backend while loading GPTQ models via transformers.
AutoGPTQ has such check: [Marlin kernel can be built against any compute capability by fxmarty · Pull Request #540 · AutoGPTQ/AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ/pull/540/files)

## 评论 (5)

### Qubitium · 2025-01-17

@chplushsieh This is our bug and will be fixed asap. This should not have happened. 

@LRL-ModelCloud Please fix this. Marlin validation needs to also check for `device`, if `cuda`, check cuda compute version.  https://github.com/ModelCloud/GPTQModel/blob/ede890cfa87264106c58bc82533ff3ec5df2d06d/gptqmodel/utils/importer.py#L171

### Qubitium · 2025-01-18

@chplushsieh  This bug has been fixed. Please try again and re-open is issue persists. 

Also GPTQModel was just merged into transformers in the past few days and we did add a [GPTQConfig.backend](https://github.com/huggingface/transformers/blob/5fa35344755d8d9c29610b57d175efd03776ae9e/src/transformers/utils/quantization_config.py#L597C9-L597C16) toggle that is passed to GPTQModel for manual kernel selection. 



### chplushsieh · 2025-01-18

I just tried and it works for me: `INFO - Auto pick kernel based on compatibility: <class 'gptqmodel.nn_modules.qlinear.exllamav2.ExllamaV2QuantLinear'>`
Thanks for the prompt fix!

### chilljudaoren · 2026-06-17

> [@chplushsieh](https://github.com/chplushsieh) This bug has been fixed. Please try again and re-open is issue persists.
> 
> Also GPTQModel was just merged into transformers in the past few days and we did add a [GPTQConfig.backend](https://github.com/huggingface/transformers/blob/5fa35344755d8d9c29610b57d175efd03776ae9e/src/transformers/utils/quantization_config.py#L597C9-L597C16) toggle that is passed to GPTQModel for manual kernel selection.

Traceback (most recent call last):
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/bin/llamafactory-cli", line 10, in <module>
    sys.exit(main())
             ^^^^^^
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/LlamaFactory/src/llamafactory/cli.py", line 24, in main
    launcher.launch()
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/LlamaFactory/src/llamafactory/launcher.py", line 139, in launch
    run_api()
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/LlamaFactory/src/llamafactory/api/app.py", line 128, in run_api
    chat_model = ChatModel()
                 ^^^^^^^^^^^
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/LlamaFactory/src/llamafactory/chat/chat_model.py", line 53, in __init__
    self.engine: BaseEngine = HuggingfaceEngine(model_args, data_args, finetuning_args, generating_args)
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/LlamaFactory/src/llamafactory/chat/hf_engine.py", line 59, in __init__
    self.model = load_model(
                 ^^^^^^^^^^^
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/LlamaFactory/src/llamafactory/model/loader.py", line 172, in load_model
    model = load_class.from_pretrained(**init_kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/transformers/models/auto/auto_factory.py", line 394, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/transformers/modeling_utils.py", line 4170, in from_pretrained
    hf_quantizer.preprocess_model(
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/transformers/quantizers/base.py", line 171, in preprocess_model
    self._process_model_before_weight_loading(model, **kwargs)
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/gptqmodel/__init__.py", line 53, in _process_model_before_weight_loading_with_device_map
    return original_process(self, model, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/transformers/quantizers/quantizer_gptq.py", line 94, in _process_model_before_weight_loading
    model = self.optimum_quantizer.convert_model(model, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/optimum/gptq/quantizer.py", line 277, in convert_model
    self._replace_by_quant_layers(model, layers_to_be_replaced)
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/optimum/gptq/quantizer.py", line 357, in _replace_by_quant_layers
    self._replace_by_quant_layers(child, names, name + "." + name1 if name != "" else name1)
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/optimum/gptq/quantizer.py", line 357, in _replace_by_quant_layers
    self._replace_by_quant_layers(child, names, name + "." + name1 if name != "" else name1)
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/optimum/gptq/quantizer.py", line 357, in _replace_by_quant_layers
    self._replace_by_quant_layers(child, names, name + "." + name1 if name != "" else name1)
  [Previous line repeated 2 more times]
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/optimum/gptq/quantizer.py", line 324, in _replace_by_quant_layers
    new_layer = self.quant_linear(
                ^^^^^^^^^^^^^^^^^^
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/gptqmodel/nn_modules/qlinear/marlin.py", line 116, in __init__
    super().__init__(
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/gptqmodel/nn_modules/qlinear/__init__.py", line 689, in __init__
    super().__init__(
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/gptqmodel/nn_modules/qlinear/__init__.py", line 610, in __init__
    super().__init__(*args, pack_dtype=pack_dtype, **kwargs)
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/gptqmodel/nn_modules/qlinear/__init__.py", line 513, in __init__
    super().__init__(
  File "/XYFS02/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.12/site-packages/gptqmodel/nn_modules/qlinear/__init__.py", line 135, in __init__
    raise err
NotImplementedError: <class 'gptqmodel.nn_modules.qlinear.marlin.MarlinLinear'>: `out_features`: 32 must be divisible by [64].

### Qubitium · 2026-06-19

For temp fix, override optimum's gptq-model calls wuth backend=auto_trainable 

@ZX-ModelCloud Check if optimum path is not passing the correct flag. For training/quantization, optimum should not be requesting Marlin kernel.



