# [Issue #2273] [BUG] No module named 'triton' on macos with GPTQModel==5.6.6

source: https://github.com/ModelCloud/GPTQModel/issues/2273
state: closed | updated: 2025-12-16T01:45:43Z
labels: bug

## 正文

**Describe the bug**

Get the Exception
ModuleNotFoundError: No module named 'triton'
on import of transformers

This error message did not appear in GPTQModel==5.4.2 

**GPU Info**

Apple M4 Pro 48 GB


**Software Info**

Operation System/Version + Python Version:
macOS 26.1
Python 3.12

Show output of:
```
pip show gptqmodel torch transformers accelerate triton

WARNING: Package(s) not found: triton
Name: GPTQModel                                                                                                                                                                    
Version: 5.6.6
Summary: Production ready LLM model compression/quantization toolkit with hw accelerated inference support for both cpu/gpu via HF, vLLM, and SGLang.
Home-page: https://github.com/ModelCloud/GPTQModel
Author: 
Author-email: ModelCloud <qubitium@modelcloud.ai>
License-Expression: Apache-2.0
Location: .../.venv/lib/python3.12/site-packages
Requires: accelerate, datasets, device-smi, dill, hf_transfer, huggingface_hub, kernels, logbar, maturin, numpy, packaging, pillow, protobuf, pyarrow, pypcre, safetensors, threadpoolctl, tokenicer, torch, torchao, transformers
Required-by: 
---
Name: torch
Version: 2.9.1
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org
Author: 
Author-email: PyTorch Team <packages@pytorch.org>
License: BSD-3-Clause
Location: .../.venv/lib/python3.12/site-packages
Requires: filelock, fsspec, jinja2, networkx, setuptools, sympy, typing-extensions
Required-by: accelerate, GPTQModel, optimum
---
Name: transformers
Version: 4.57.3
Summary: State-of-the-art Machine Learning for JAX, PyTorch and TensorFlow
Home-page: https://github.com/huggingface/transformers
Author: The Hugging Face team (past and future) with the help of all our contributors (https://github.com/huggingface/transformers/graphs/contributors)
Author-email: transformers@huggingface.co
License: Apache 2.0 License
Location: .../.venv/lib/python3.12/site-packages
Requires: filelock, huggingface-hub, numpy, packaging, pyyaml, regex, requests, safetensors, tokenizers, tqdm
Required-by: GPTQModel, optimum, tokenicer
---
Name: accelerate
Version: 1.12.0
Summary: Accelerate
Home-page: https://github.com/huggingface/accelerate
Author: The HuggingFace team
Author-email: zach.mueller@huggingface.co
License: Apache
Location: .../.venv/lib/python3.12/site-packages
Requires: huggingface_hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: GPTQModel
```

**To Reproduce**

```
pip install torch transformers GPTQModel optimum
```

```
from transformers import pipeline
llm_pipeline = pipeline(model="JunHowie/Qwen3-0.6B-GPTQ-Int4")
output = llm_pipeline("What is the capital of Germany?", max_new_tokens=100)
print(output)
```

**Expected behavior**

inference


**Additional context**

Complete Log:

```
Skipping import of cpp extensions due to incompatible torch version 2.9.1 for torchao version 0.14.1             Please see https://github.com/pytorch/ao/issues/2919 for more info
W1215 15:30:51.584000 4452 .venv/lib/python3.12/site-packages/torch/distributed/elastic/multiprocessing/redirects.py:29] NOTE: Redirects are currently not supported in Windows or MacOs.

WARN  Python GIL is enabled: Multi-gpu quant acceleration for MoE models is sub-optimal and multi-core accelerated cpu packing is also disabled. We recommend Python >= 3.13.3t with Pytorch > 2.8 for mult-gpu quantization and multi-cpu packing with env `PYTHON_GIL=0`.
WARN  Feature `utils/Perplexity` requires Python < 3.14 and Python GIL enabled and Python >= 3.13.3T (T for Threading-Free edition of Python) plus Torch 2.8. Feature is currently skipped/disabled.
INFO  ENV: Auto setting PYTORCH_ALLOC_CONF='expandable_segments:True,max_split_size_mb:256,garbage_collection_threshold:0.7' for memory saving.
INFO  ENV: Auto setting CUDA_DEVICE_ORDER=PCI_BUS_ID for correctness.          
DEBUG BitBLAS import failed: No module named 'bitblas'                         
Traceback (most recent call last):
  File ".../main.py", line 2, in <module>
    llm_pipeline = pipeline(model="JunHowie/Qwen3-0.6B-GPTQ-Int4")
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".../.venv/lib/python3.12/site-packages/transformers/pipelines/__init__.py", line 1027, in pipeline
    framework, model = infer_framework_load_model(
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".../.venv/lib/python3.12/site-packages/transformers/pipelines/base.py", line 293, in infer_framework_load_model
    model = model_class.from_pretrained(model, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".../.venv/lib/python3.12/site-packages/transformers/models/auto/auto_factory.py", line 604, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".../.venv/lib/python3.12/site-packages/transformers/modeling_utils.py", line 277, in _wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File ".../.venv/lib/python3.12/site-packages/transformers/modeling_utils.py", line 4881, in from_pretrained
    hf_quantizer, config, dtype, device_map = get_hf_quantizer(
                                              ^^^^^^^^^^^^^^^^^
  File ".../.venv/lib/python3.12/site-packages/transformers/quantizers/auto.py", line 311, in get_hf_quantizer
    hf_quantizer = AutoHfQuantizer.from_config(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".../.venv/lib/python3.12/site-packages/transformers/quantizers/auto.py", line 185, in from_config
    return target_cls(quantization_config, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".../.venv/lib/python3.12/site-packages/transformers/quantizers/quantizer_gptq.py", line 50, in __init__
    from optimum.gptq import GPTQQuantizer
  File ".../.venv/lib/python3.12/site-packages/optimum/gptq/__init__.py", line 15, in <module>
    from .quantizer import GPTQQuantizer, load_quantized_model
  File ".../.venv/lib/python3.12/site-packages/optimum/gptq/quantizer.py", line 60, in <module>
    from gptqmodel import exllama_set_max_input_length
  File ".../.venv/lib/python3.12/site-packages/gptqmodel/__init__.py", line 45, in <module>
    from .models import GPTQModel, get_best_device
  File ".../.venv/lib/python3.12/site-packages/gptqmodel/models/__init__.py", line 7, in <module>
    from .auto import MODEL_MAP, GPTQModel
  File ".../.venv/lib/python3.12/site-packages/gptqmodel/models/auto.py", line 70, in <module>
    from ..utils.model import find_modules  # noqa: E402
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".../.venv/lib/python3.12/site-packages/gptqmodel/utils/model.py", line 58, in <module>
    from .importer import select_quant_linear
  File ".../.venv/lib/python3.12/site-packages/gptqmodel/utils/importer.py", line 23, in <module>
    from ..nn_modules.qlinear.gemm_awq_triton import AwqGEMMTritonQuantLinear
  File ".../.venv/lib/python3.12/site-packages/gptqmodel/nn_modules/qlinear/gemm_awq_triton.py", line 14, in <module>
    from ...quantization.awq.modules.triton.gemm import awq_dequantize_triton, awq_gemm_triton
  File ".../.venv/lib/python3.12/site-packages/gptqmodel/quantization/awq/modules/triton/gemm.py", line 18, in <module>
    import triton
ModuleNotFoundError: No module named 'triton'

Process finished with exit code 1
```


## 评论 (1)

### Qubitium · 2025-12-16

@bjoernrenzel-optadata  Check pr #2274 for MacOS loading fix. We will release 5.6.8 to pypi later today to fix this. You can in the mean time, git clone the PR and do `pip install -v . --no-build-isolation`
