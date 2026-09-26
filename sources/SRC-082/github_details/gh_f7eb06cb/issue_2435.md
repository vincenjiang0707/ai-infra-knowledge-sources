# [Issue #2435] [BUG] quantize qwen3-30b for 4-bits

source: https://github.com/ModelCloud/GPTQModel/issues/2435
state: closed | updated: 2026-03-09T01:00:01Z
labels: bug, duplicate

## 正文

**Describe the bug**
```

when try the below script, encounter a error.
Traceback (most recent call last):------+--------+---------+--------+-----------------------------------+                                                                                                                                                                        
  File "/home/luor/modelzoos/qwen3/test_gptq.py", line 18, in <module>░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0:00:00 / 0:00:00 [1/48] 2.1%
    model.quantize(calibration_dataset, batch_size=1)
  File "/home/luor/miniconda3/envs/torch29sglang/lib/python3.11/site-packages/gptqmodel/models/base.py", line 852, in quantize
    result = module_looper.loop(
             ^^^^^^^^^^^^^^^^^^^
  File "/home/luor/miniconda3/envs/torch29sglang/lib/python3.11/site-packages/gptqmodel/looper/module_looper.py", line 1395, in loop
    return self._loop_impl(failsafe=failsafe, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/luor/miniconda3/envs/torch29sglang/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/luor/miniconda3/envs/torch29sglang/lib/python3.11/site-packages/gptqmodel/looper/module_looper.py", line 1500, in _loop_impl
    run_layer_stage(
  File "/home/luor/miniconda3/envs/torch29sglang/lib/python3.11/site-packages/gptqmodel/looper/stage_layer.py", line 120, in run_layer_stage
    subset = looper.create_named_modules(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/luor/miniconda3/envs/torch29sglang/lib/python3.11/site-packages/gptqmodel/looper/module_looper.py", line 1605, in create_named_modules
    raise ValueError(f"layer module item `{n}` not found in model, please check your model config.")
ValueError: layer module item `mlp.experts.0.gate_proj` not found in model, please check your model config.

```
**GPU Info**

<img width="662" height="616" alt="Image" src="https://github.com/user-attachments/assets/91125287-cf85-45cd-b797-d6fb46cf25c1" />


**Software Info**

```
gptqmodel                  5.7.0  
torch                      2.9.0            pypi_0           pypi
torchao                    0.16.0           pypi_0           pypi
torchaudio                 2.9.0            pypi_0           pypi
torchcodec                 0.8.0            pypi_0           pypi
torchvision                0.24.0
transformers               5.2.0
```



**To Reproduce**
```

from datasets import load_dataset
from gptqmodel import GPTQModel, QuantizeConfig

model_id = "Qwen/Qwen3-30B-A3B-Instruct-2507"
quant_path = "Qwen3-30B-A3B-Instruct-2507-gptqmodel-4bit"

calibration_dataset = load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
  ).select(range(10))["text"]

quant_config = QuantizeConfig(bits=4, group_size=128)

model = GPTQModel.load(model_id, quant_config, attn_implementation="eager" )    # must use eager attn , otherwise, it will report a error.

# increase `batch_size` to match GPU/VRAM specs to speed up quantization
model.quantize(calibration_dataset, batch_size=1)

model.save(quant_path)
```


## 评论 (2)

### Qubitium · 2026-03-03

@MaltoseFlower Avoid Transformers 5.x for now. We have another open issue related to/caused by latest Transformers. 

We are working on a fix. but use 4.x transformers for now.

related to #2423

### Qubitium · 2026-03-04

@MaltoseFlower First patch for `Qwen3/3 MoE` patch for Transformers >= 5.2.0 has landed on `main` branch. You also need to install `defuser` => `pip install -U defuser`. 
