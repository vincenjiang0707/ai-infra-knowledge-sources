# [Issue #2393] [BUG] Can't get triton version-windows

source: https://github.com/ModelCloud/GPTQModel/issues/2393
state: closed | updated: 2026-02-01T04:04:43Z
labels: bug

## 正文

i have installed triton-windows==3.5.1.post24, sageAttention2 is ok. but gptqmodel can not work properly.


```
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\autoawq\awq\models\auto.py", line 83, in from_pretrained
    return AWQ_CAUSAL_LM_MODEL_MAP[model_type].from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\autoawq\awq\models\base.py", line 389, in from_pretrained
    model = target_cls.from_pretrained(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\transformers\models\auto\auto_factory.py", line 372, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\transformers\modeling_utils.py", line 4035, in from_pretrained
    hf_quantizer.preprocess_model(
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\transformers\quantizers\base.py", line 167, in preprocess_model
    self._process_model_before_weight_loading(model, **kwargs)
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\transformers\quantizers\quantizer_awq.py", line 72, in _process_model_before_weight_loading
    model = replace_with_awq_linear(
            ^^^^^^^^^^^^^^^^^^^^^^^^
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\transformers\integrations\awq.py", line 76, in replace_with_awq_linear
    from gptqmodel.quantization import METHOD
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\gptqmodel\__init__.py", line 14, in <module>
    patch_triton_autotuner()
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\gptqmodel\utils\nogil_patcher.py", line 53, in patch_triton_autotuner
    raise ValueError("Can't get triton version") 
```

## 评论 (5)

### Qubitium · 2026-01-31

@zwukong Can you post `pip show transformers gptqmodel triton`?

### zwukong · 2026-01-31

 triton-windows 's name is not the same package name as  triton . I have to remove gptq version check codes or add a empty package folder named triton-... 

### Qubitium · 2026-01-31

@zwukong I see the issue now. native windows has substanard triton pkg support so oss triton-windows fills the gap. We will update the code to check for both triton and triton-windows.

### Qubitium · 2026-02-01

@zwukong  Can you help us test PR #2395 which should resolve your issue on windows? We do not have a windows dev machine with gpu attached. Thanks!

### zwukong · 2026-02-01

Sorry i give up awq, compatible issues.But i think your PR is ok,  that codes should have passed


```
  model = AutoModelForCausalLM.from_pretrained(local_path, **load_kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\transformers\models\auto\auto_factory.py", line 604, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\transformers\modeling_utils.py", line 277, in _wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\transformers\modeling_utils.py", line 4998, in from_pretrained
    hf_quantizer.preprocess_model(
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\transformers\quantizers\base.py", line 225, in preprocess_model
    return self._process_model_before_weight_loading(model, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\transformers\quantizers\quantizer_awq.py", line 119, in _process_model_before_weight_loading
    model, has_been_replaced = replace_with_awq_linear(
                               ^^^^^^^^^^^^^^^^^^^^^^^^
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\transformers\integrations\awq.py", line 134, in replace_with_awq_linear
    from awq.modules.linear.gemm import WQLinear_GEMM
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\awq\__init__.py", line 24, in <module>
    from awq.models.auto import AutoAWQForCausalLM
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\awq\models\__init__.py", line 1, in <module>
    from .mpt import MptAWQForCausalLM
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\awq\models\mpt.py", line 1, in <module>
    from .base import BaseAWQForCausalLM
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\awq\models\base.py", line 49, in <module>
    from awq.quantize.quantizer import AwqQuantizer
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\awq\quantize\quantizer.py", line 11, in <module>
    from awq.quantize.scale import apply_scale, apply_clip
  File "M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\awq\quantize\scale.py", line 12, in <module>
    from transformers.activations import NewGELUActivation, PytorchGELUTanh, GELUActivation
ImportError: cannot import name 'PytorchGELUTanh' from 'transformers.activations' (M:\ComfyUI\312_cu128\python_embeded\Lib\site-packages\transformers\activations.py)
```
