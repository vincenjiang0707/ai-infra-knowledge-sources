# [Issue #2924] NotImplementedError: <class 'gptqmodel.nn_modules.qlinear.tritonv2.TritonV2Linear'>: `out_features`: 48 must be divisible by [32]

source: https://github.com/ModelCloud/GPTQModel/issues/2924
state: closed | updated: 2026-06-20T21:19:35Z
labels: bug

## 正文

**Describe the bug**

NotImplementedError: <class 'gptqmodel.nn_modules.qlinear.tritonv2.TritonV2Linear'>: `out_features`: 48 must be divisible by [32]



## 评论 (2)

### chilljudaoren · 2026-06-16

Traceback (most recent call last):
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/bin/lmf", line 10, in <module>
    sys.exit(main())
             ^^^^^^
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/LlamaFactory/src/llamafactory/cli.py", line 24, in main
    launcher.launch()
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/LlamaFactory/src/llamafactory/launcher.py", line 152, in launch
    export_model()
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/LlamaFactory/src/llamafactory/train/tuner.py", line 172, in export_model
    model = load_model(tokenizer, model_args, finetuning_args)  # must after fixing tokenizer to resize vocab
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/LlamaFactory/src/llamafactory/model/loader.py", line 181, in load_model
    model = load_class.from_pretrained(**init_kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/transformers/models/auto/auto_factory.py", line 394, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/transformers/modeling_utils.py", line 4234, in from_pretrained
    hf_quantizer.postprocess_model(
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/transformers/quantizers/base.py", line 194, in postprocess_model
    return self._process_model_after_weight_loading(model, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/transformers/quantizers/quantizer_gptq.py", line 103, in _process_model_after_weight_loading
    self.optimum_quantizer.quantize_model(model, self.quantization_config.tokenizer)
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/optimum/gptq/quantizer.py", line 638, in quantize_model
    self.pack_model(model=model, quantizers=quantizers)
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/optimum/gptq/quantizer.py", line 712, in pack_model
    self._replace_by_quant_layers(model, quantizers)
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/optimum/gptq/quantizer.py", line 357, in _replace_by_quant_layers
    self._replace_by_quant_layers(child, names, name + "." + name1 if name != "" else name1)
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/optimum/gptq/quantizer.py", line 357, in _replace_by_quant_layers
    self._replace_by_quant_layers(child, names, name + "." + name1 if name != "" else name1)
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/optimum/gptq/quantizer.py", line 357, in _replace_by_quant_layers
    self._replace_by_quant_layers(child, names, name + "." + name1 if name != "" else name1)
  [Previous line repeated 2 more times]
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/optimum/gptq/quantizer.py", line 324, in _replace_by_quant_layers
    new_layer = self.quant_linear(
                ^^^^^^^^^^^^^^^^^^
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/gptqmodel/nn_modules/qlinear/tritonv2.py", line 72, in __init__
    super().__init__(
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/gptqmodel/nn_modules/qlinear/torch.py", line 152, in __init__
    super().__init__(
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/gptqmodel/nn_modules/qlinear/__init__.py", line 772, in __init__
    super().__init__(*args, **kwargs)
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/gptqmodel/nn_modules/qlinear/__init__.py", line 689, in __init__
    super().__init__(
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/gptqmodel/nn_modules/qlinear/__init__.py", line 610, in __init__
    super().__init__(*args, pack_dtype=pack_dtype, **kwargs)
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/gptqmodel/nn_modules/qlinear/__init__.py", line 513, in __init__
    super().__init__(
  File "/XYAIFS00/HDD_POOL/pushi_yjliang/pushi_yjliang_1/czh/.venv/lib/python3.11/site-packages/gptqmodel/nn_modules/qlinear/__init__.py", line 135, in __init__
    raise err
NotImplementedError: <class 'gptqmodel.nn_modules.qlinear.tritonv2.TritonV2Linear'>: `out_features`: 48 must be divisible by [32].

### Qubitium · 2026-06-16

@chilljudaoren You need to pad your model so it's out-features is divisible by 32. Normally, at the the modern models, all modules are shaped to be divisble by 32/64 which is what gpu kernels actually want. Even if your layer/module design does not divide evenly, a small padding does not not hurt and only helps inference performance.
