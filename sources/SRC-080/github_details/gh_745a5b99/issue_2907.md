# [Issue #2907] [oneshot] Add pre-processing check for model

source: https://github.com/vllm-project/llm-compressor/issues/2907
state: closed | updated: 2026-07-23T20:18:02Z
labels: bug, good first issue

## 正文

### 🐛 Describe the bug

Running `oneshot` on a model checkpoint that is already quantized (i.e. has a quantization_config) is currently not supported. However, the subsequent errors that are raised do not make it clear to the user why their flow is failing. For example, running oneshot on a fp8-dynamic-quantized checkpoint results in the following error:

```
NotImplementedError: "min_values_cuda" not implemented for 'Float8_e4m3fn'
```

We should improve on this by instead raising an error explicitly telling the user they are attempting to quantize a model already quantized, which is not supported. We should direct them to either use a full-precision checkpoint or first dequantize the checkpoint using the [convert_checkpoint entrypoint](https://github.com/vllm-project/compressed-tensors/blob/main/examples/convert_checkpoint/kimi_k26_example.py) in compressed-tensors.

### 🛠️ Steps to reproduce

<details><summary>Script to reproduce</summary>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import QuantizationModifier
from llmcompressor.utils import dispatch_for_generation

import os

MODEL_ID = "RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8-dynamic"

model = AutoModelForCausalLM.from_pretrained(MODEL_ID, torch_dtype="auto")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

# Configure the quantization algorithm and scheme
recipe = QuantizationModifier(
    targets="Linear", scheme="FP8_DYNAMIC", ignore=["lm_head"]
)

# Create log directory in a writable location
LOG_DIR = "./sparse_logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Apply quantization
oneshot(model=model, recipe=recipe)

# Confirm quantized model looks OK
print("========== SAMPLE GENERATION ==============")
dispatch_for_generation(model)
input_ids = tokenizer("Hello my name is", return_tensors="pt").input_ids.to(
    model.device
)
output = model.generate(input_ids, max_new_tokens=20)
print(tokenizer.decode(output[0]))
print("==========================================")

# Save to disk in compressed-tensors format
SAVE_DIR = MODEL_ID.rstrip("/").split("/")[-1] + "-FP8-Dynamic"
model.save_pretrained(SAVE_DIR)
tokenizer.save_pretrained(SAVE_DIR)
```

</details>


<details><summary>Logs & Stack Trace</summary>
```
$ python example.py
config.json: 2.04kB [00:00, 11.4MB/s]
`torch_dtype` is deprecated! Use `dtype` instead!
model.safetensors.index.json: 43.5kB [00:00, 173MB/s]
model-00002-of-00002.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████| 4.08G/4.08G [00:10<00:00, 393MB/s]
model-00001-of-00002.safetensors: 100%|██████████████████████████████████████████████████████████████████████████████| 5.00G/5.00G [00:12<00:00, 416MB/s]
Fetching 2 files: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:12<00:00,  6.08s/it]
Compressing model: 224it [00:00, 3146.87it/s]
Loading checkpoint shards: 100%|███████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00, 87.53it/s]
generation_config.json: 100%|███████████████████████████████████████████████████████████████████████████████████████████| 184/184 [00:00<00:00, 1.99MB/s]
tokenizer_config.json: 55.4kB [00:00, 163MB/s]
tokenizer.json: 9.09MB [00:00, 35.3MB/s]
special_tokens_map.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████| 296/296 [00:00<00:00, 4.65MB/s]
2026-07-07T14:29:14.767982+0000 | __init__ | WARNING - Disabling tokenizer parallelism due to threading conflict between FastTokenizer and Datasets. Set TOKENIZERS_PARALLELISM=false to suppress this warning.
2026-07-07T14:29:15.472982+0000 | reset | INFO - Compression lifecycle reset
2026-07-07T14:29:15.473687+0000 | from_modifiers | INFO - Creating recipe from modifiers
2026-07-07T14:29:15.489781+0000 | initialize | INFO - Compression lifecycle initialized for 1 modifiers
2026-07-07T14:29:15.490006+0000 | IndependentPipeline | INFO - Inferred `DataFreePipeline` for `QuantizationModifier`
Calibrating weights:   0%|                                                                                                       | 0/224 [00:00<?, ?it/s]
Traceback (most recent call last):
  File "/opt/app-root/run/example.py", line 24, in <module>
    oneshot(model=model, recipe=recipe)
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/entrypoints/oneshot.py", line 411, in oneshot
    one_shot()
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/entrypoints/oneshot.py", line 188, in __call__
    self.apply_recipe_modifiers(
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/entrypoints/oneshot.py", line 239, in apply_recipe_modifiers
    pipeline(
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/pipelines/independent/pipeline.py", line 45, in __call__
    pipeline(model, dataloader, dataset_args)
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/pipelines/data_free/pipeline.py", line 35, in __call__
    LifecycleCallbacks.calibration_epoch_start()
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/core/session_functions.py", line 154, in calibration_epoch_start
    return cls.event(EventType.CALIBRATION_EPOCH_START, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/core/session_functions.py", line 89, in event
    return active_session().event(event_type, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/core/session.py", line 187, in event
    mod_data = self._lifecycle.event(
               ^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/core/lifecycle.py", line 204, in event
    data = mod.update_event(state=self.state, event=event, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/modifiers/modifier.py", line 122, in update_event
    self.on_event(state, event, **kwargs)
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/modifiers/quantization/quantization/base.py", line 96, in on_event
    self.on_start(state, None)
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/modifiers/quantization/quantization/base.py", line 91, in on_start
    update_weight_zp_scale(module)
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/modifiers/quantization/calibration.py", line 156, in update_weight_zp_scale
    call_observer(module=module, base_name="weight")
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/modifiers/quantization/calibration.py", line 113, in call_observer
    scale, zero_point = observer(value)
                        ^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.12/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.12/site-packages/torch/nn/modules/module.py", line 1787, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/observers/base.py", line 86, in forward
    scales, zero_points, _min, _max = self._forward_with_minmax(observed)
                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/observers/base.py", line 109, in _forward_with_minmax
    min_vals, max_vals = self.get_min_max(observed)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/observers/min_max.py", line 22, in get_min_max
    return _get_min_max(observed)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.12/site-packages/llmcompressor/observers/min_max.py", line 92, in _get_min_max
    min_vals = torch.amin(observed, dim=(0, -1))
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
NotImplementedError: "min_values_cuda" not implemented for 'Float8_e4m3fn'
```
</details>

## 评论 (3)

### brian-dellabetta · 2026-07-09

We will move forward with #2909 since it is pretty close. In future, please post on the issue so I can assign the task to you

### jayakumarpujar · 2026-07-11

@brian-dellabetta, if you didn't assign it to anyone, I'm interested in it. 

### brian-dellabetta · 2026-07-13

@jayakumarpujar thanks for the interest, but #2909 by @w3lld1 is the PR we'll go with. I am unable to assign them for some reason, so i will assign this to myself to avoid redundant PRs.

@saisharan0103 yes that is basically what we're doing
