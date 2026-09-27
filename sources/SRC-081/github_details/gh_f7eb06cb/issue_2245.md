# [Issue #2245] [BUG] Fail to quantize Qwen3-Omni on VRAM balanced mode

source: https://github.com/ModelCloud/GPTQModel/issues/2245
state: closed | updated: 2026-01-03T11:57:32Z
labels: bug

## 正文

**Describe the bug**

Raise error when quantize Qwen3-Omni on vram balanced

**GPU Info**

```
Tue Dec  9 22:50:02 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.35.03              Driver Version: 560.35.03      CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX 6000 Ada Gene...    On  |   00000000:27:00.0 Off |                  Off |
| 30%   36C    P0             71W /  300W |    3428MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX 6000 Ada Gene...    On  |   00000000:A8:00.0 Off |                  Off |
| 30%   37C    P0             75W /  300W |    2396MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
```

**Software Info**

Operation System/Version + Python Version

Show output of:
```Name: GPTQModel
Version: 5.6.0+cu126torch2.9
Summary: Production ready LLM model compression/quantization toolkit with hw accelerated inference support for both cpu/gpu via HF, vLLM, and SGLang.
Home-page: https://github.com/ModelCloud/GPTQModel
Author: 
Author-email: ModelCloud <qubitium@modelcloud.ai>
License: Apache-2.0
Location: /home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages
Requires: accelerate, datasets, device-smi, dill, hf_transfer, huggingface_hub, kernels, logbar, maturin, numpy, packaging, pillow, protobuf, pyarrow, pypcre, random_word, safetensors, threadpoolctl, tokenicer, torch, torchao, transformers
Required-by: 
---
Name: torch
Version: 2.9.1
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org
Author: 
Author-email: PyTorch Team <packages@pytorch.org>
License: BSD-3-Clause
Location: /home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages
Requires: filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-cufile-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvshmem-cu12, nvidia-nvtx-cu12, setuptools, sympy, triton, typing-extensions
Required-by: accelerate, GPTQModel, torchaudio, torchvision
---
Name: transformers
Version: 4.57.3
Summary: State-of-the-art Machine Learning for JAX, PyTorch and TensorFlow
Home-page: https://github.com/huggingface/transformers
Author: The Hugging Face team (past and future) with the help of all our contributors (https://github.com/huggingface/transformers/graphs/contributors)
Author-email: transformers@huggingface.co
License: Apache 2.0 License
Location: /home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages
Requires: filelock, huggingface-hub, numpy, packaging, pyyaml, regex, requests, safetensors, tokenizers, tqdm
Required-by: GPTQModel, tokenicer
---
Name: accelerate
Version: 1.12.0
Summary: Accelerate
Home-page: https://github.com/huggingface/accelerate
Author: The HuggingFace team
Author-email: zach.mueller@huggingface.co
License: Apache
Location: /home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages
Requires: huggingface_hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: GPTQModel
---
Name: triton
Version: 3.5.1
Summary: A language and compiler for custom Deep Learning operations
Home-page: https://github.com/triton-lang/triton/
Author: Philippe Tillet
Author-email: phil@openai.com
License: 
Location: /home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages
Requires: 
Required-by: torch
```

Install GPTQModel using release
```
pip insatll https://github.com/ModelCloud/GPTQModel/releases/download/v5.6.0/gptqmodel-5.6.0+cu126torch2.9-cp313-cp313t-linux_x86_64.whl
```


**To Reproduce**

```python
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"

import pickle as pkl

from datasets import load_dataset
from gptqmodel import GPTQModel, QuantizeConfig

from transformers import logging

model_id = 'Qwen/Qwen3-Omni-30B-A3B-Instruct'

logging.set_verbosity_error()

quant_config = QuantizeConfig(bits=4,
                              group_size=128,
                              vram_strategy='balanced',
                              offload_to_disk=False)

model = GPTQModel.load(model_id, quant_config)

calibration_dataset = load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
)

calibration_dataset = calibration_dataset.filter(lambda x: len(x["text"]) <= 8192)
calibration_dataset = calibration_dataset.select(range(1024))["text"]

model.quantize(calibration_dataset,
               batch_size=1)
```

Then, raise error like

```
Forward: Layer=`thinker.model.layers.0`, subset=4/5, batches=1024 Forward rows 372/1024 0:00:25 / 0:01:08 [372/1024] 36.3% ....
Traceback
  File "/home/hyunwoo/72g_omni_quant/11_quant_gpu_test.py", line 35, in <module>1/48] 2.1%
    model.quantize(calibration_dataset,
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
                   batch_size=1)
                   ^^^^^^^^^^^^^
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/gptqmodel/models/base.py", line 678, in quantize
    result = module_looper.loop(
        backend=backend,
        fail_safe=self.quantize_config.fail_safe,
    )
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 1075, in loop
    return self._loop_impl(fail_safe=fail_safe, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 1177, in _loop_impl
    run_layer_stage(
    ~~~~~~~~~~~~~~~^
        self,
        ^^^^^
    ...<9 lines>...
        logger=log,
        ^^^^^^^^^^^
    )
    ^
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/gptqmodel/looper/stage_layer.py", line 139, in run_layer_stage
    subset_result = run_subset_stage(
        looper=looper,
    ...<22 lines>...
        subset_event_cb=looper._subset_event_dispatch,
    )
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/gptqmodel/looper/stage_subset.py", line 314, in run_subset_stage
    forward_outputs = looper._run_forward_batches(
        module=module,
    ...<17 lines>...
        preserve_module_devices=preserve_devices,
    )
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 621, in _run_forward_batches
    return self._run_forward_batches_single(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        module=module,
        ^^^^^^^^^^^^^^
    ...<16 lines>...
        preserve_module_devices=preserve_module_devices,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 769, in _run_forward_batches_single
    module_output = module(*layer_input, **additional_inputs)
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/transformers/modeling_layers.py", line 94, in __call__
    return super().__call__(*args, **kwargs)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py", line 1535, in forward
    hidden_states, _ = self.self_attn(
                       ~~~~~~~~~~~~~~^
        hidden_states=hidden_states,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<5 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py", line 1456, in forward
    key_states, value_states = past_key_values.update(key_states, value_states, self.layer_idx, cache_kwargs)
                               ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/transformers/cache_utils.py", line 776, in update
    keys, values = self.layers[layer_idx].update(key_states, value_states, cache_kwargs)
                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/hyunwoo/.mamba/envs/gptq_gpu/lib/python3.13t/site-packages/transformers/cache_utils.py", line 119, in update
    self.keys = torch.cat([self.keys, key_states], dim=-2)
                ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Expected all tensors to be on the same device, but got tensors is on cuda:0, different from other tensors on cuda:1 (when checking argument in method wrapper_CUDA_cat)
```

**Expected behavior**

Quantize model sucessfully

**Model/Datasets**

Same as code above

## 评论 (4)

### Chemical118 · 2025-12-09

I'm not sure if the error is caused by the cache being used. I'm new to this field, so I appreciate your understanding.

### Qubitium · 2025-12-10

This is a bug in hf transformer qwen3 omni modeling code. We will fix it on our side today.

### Qubitium · 2025-12-10

@Chemical118  Fixed in https://github.com/ModelCloud/GPTQModel/pull/2246

### Chemical118 · 2025-12-10

Thank you for your fast respond! I will test 5.7.0 in today.
