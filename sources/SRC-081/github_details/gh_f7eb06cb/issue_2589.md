# [Issue #2589] [BUG] AttributeError: type object 'BACKEND' has no attribute 'EXLLAMA_EORA'. Did you mean: 'EXLLAMA_V2'?

source: https://github.com/ModelCloud/GPTQModel/issues/2589
state: closed | updated: 2026-03-24T02:15:22Z
labels: bug

## 正文

**Describe the bug**

AttributeError: type object 'BACKEND' has no attribute 'EXLLAMA_EORA'. Did you mean: 'EXLLAMA_V2'?

**GPU Info**

Show output of:

```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 590.48.01              Driver Version: 590.48.01      CUDA Version: 13.1     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    Off |   00000000:51:00.0 Off |                  Off |
| 30%   33C    P8             17W /  600W |      15MiB /  97887MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    Off |   00000000:C3:00.0 Off |                  Off |
| 30%   35C    P8             15W /  600W |      15MiB /  97887MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            1614      G   /usr/lib/xorg/Xorg                        4MiB |
|    1   N/A  N/A            1614      G   /usr/lib/xorg/Xorg                        4MiB |
+-----------------------------------------------------------------------------------------+
```

**Software Info**
Ubuntu 24.04 LTS Python 3.14t via UV

Show output of:
```
(GPTQModel) (base) arli@arli-super-server:~/GPTQModel-v5$ pip show gptqmodel torch transformers accelerate triton
Name: GPTQModel
Version: 6.0.0
Summary: Production ready LLM model compression/quantization toolkit with hw accelerated inference support for both cpu/gpu via HF, vLLM, and SGLang.
Home-page: https://github.com/ModelCloud/GPTQModel
Author: 
Author-email: ModelCloud <qubitium@modelcloud.ai>
License-Expression: Apache-2.0
Location: /home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages
Requires: accelerate, datasets, defuser, device-smi, dill, huggingface_hub, kernels, logbar, maturin, numpy, packaging, pillow, protobuf, pyarrow, pypcre, safetensors, setuptools, threadpoolctl, tokenicer, torch, torchao, transformers
Required-by: 
---
Name: torch
Version: 2.10.0
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org
Author: 
Author-email: PyTorch Team <packages@pytorch.org>
License: BSD-3-Clause
Location: /home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages
Requires: cuda-bindings, filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-cufile-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvshmem-cu12, nvidia-nvtx-cu12, setuptools, sympy, triton, typing-extensions
Required-by: accelerate, GPTQModel, torchvision
---
Name: transformers
Version: 5.3.0
Summary: Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.
Home-page: https://github.com/huggingface/transformers
Author: The Hugging Face team (past and future) with the help of all our contributors (https://github.com/huggingface/transformers/graphs/contributors)
Author-email: transformers@huggingface.co
License: Apache 2.0 License
Location: /home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages
Requires: huggingface-hub, numpy, packaging, pyyaml, regex, safetensors, tokenizers, tqdm, typer
Required-by: Defuser, GPTQModel
---
Name: accelerate
Version: 1.13.0
Summary: Accelerate
Home-page: https://github.com/huggingface/accelerate
Author: The Hugging Face team
Author-email: transformers@huggingface.co
License: Apache
Location: /home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages
Requires: huggingface_hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: GPTQModel
---
Name: triton
Version: 3.6.0
Summary: A language and compiler for custom Deep Learning operations
Home-page: https://github.com/triton-lang/triton/
Author: Philippe Tillet
Author-email: phil@openai.com
License: 
Location: /home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages
Requires: 
Required-by: torch
```
**To Reproduce**

Quantize Qwen3.5 27B using script:
```
import torch
from datasets import load_dataset
from gptqmodel import GPTQModel, QuantizeConfig
from transformers import AutoTokenizer
import json
import os

MODEL_ID = "/home/arli/models/Qwen3.5-27B-Derestricted" 
DATASET_ID = "neuralmagic/LLM_compression_calibration"
DATASET_SPLIT = "train"
NUM_CALIBRATION_SAMPLES = 2048
SAVE_DIR = MODEL_ID + "-GPTQ-Int8"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
ds = load_dataset(DATASET_ID, split=f"{DATASET_SPLIT}[:{NUM_CALIBRATION_SAMPLES}]")
ds = ds.shuffle(seed=42)

def preprocess(example):
    return {
        "text": tokenizer.apply_chat_template(
            example["messages"],
            tokenize=False,
        )
    }

ds = ds.map(preprocess)
calibration_dataset = [example["text"] for example in ds]

quant_config = QuantizeConfig(
    bits=8,
    group_size=128,
    sym=True,
    desc_act=False
)

print(f"Loading model from {MODEL_ID}...")
model = GPTQModel.load(
    MODEL_ID,
    quantize_config=quant_config,
    trust_remote_code=True
)

print("Starting quantization...")
model.quantize(
    calibration_dataset
)

print(f"Saving model to {SAVE_DIR}...")
model.save(SAVE_DIR)

print("Done!")
```

```
INFO  Python GIL is disabled and GPTQModel will auto enable multi-gpu quant acceleration for MoE models plus multi-cpu accelerated packing.                                                                   
<frozen importlib._bootstrap>:491: RuntimeWarning: The global interpreter lock (GIL) has been enabled to load module 'triton._C.libtriton', which has not declared that it can run safely without the GIL. To override this behavior and keep the GIL disabled (at your own risk), run with PYTHON_GIL=0 or -Xgil=0.
INFO  ENV: Auto setting PYTORCH_ALLOC_CONF='expandable_segments:True,max_split_size_mb:256,garbage_collection_threshold:0.7' for memory saving.                                                               
INFO  ENV: Auto setting CUDA_DEVICE_ORDER=PCI_BUS_ID for correctness.                                                                                                                                         
Traceback (most recent call last):
  File "/home/arli/GPTQModel-v5/qwen4bit.py", line 3, in <module>
    from gptqmodel import GPTQModel, QuantizeConfig
  File "/home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/__init__.py", line 169, in <module>
    from .models import GPTQModel, get_best_device
  File "/home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/models/__init__.py", line 7, in <module>
    from .auto import MODEL_MAP, GPTQModel
  File "/home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/models/auto.py", line 69, in <module>
    from ..utils.model import find_modules  # noqa: E402
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/utils/model.py", line 69, in <module>
    from .importer import select_quant_linear
  File "/home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/utils/importer.py", line 168, in <module>
    AUTO_BACKEND_KERNEL_MAPPING, BACKEND_TO_METHOD_FORMAT_MAPPING = build_kernel_support_maps()
                                                                    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/utils/importer.py", line 115, in build_kernel_support_maps
    _import_all_qlinear_kernels()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/utils/importer.py", line 109, in _import_all_qlinear_kernels
    importlib.import_module(f"{qlinear_pkg.__name__}.{name}")
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arli/.local/share/uv/python/cpython-3.14.0+freethreaded-linux-x86_64-gnu/lib/python3.14t/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/nn_modules/qlinear/exllama_eora.py", line 59, in <module>
    class ExllamaEoraQuantLinear(BaseQuantLinear):
    ...<172 lines>...
            return out.to(dtype=x_dtype)
  File "/home/arli/GPTQModel-v5/GPTQModel/.venv/lib/python3.14t/site-packages/gptqmodel/nn_modules/qlinear/exllama_eora.py", line 60, in ExllamaEoraQuantLinear
    SUPPORTS_BACKENDS = [BACKEND.EXLLAMA_EORA]
                         ^^^^^^^^^^^^^^^^^^^^
AttributeError: type object 'BACKEND' has no attribute 'EXLLAMA_EORA'. Did you mean: 'EXLLAMA_V2'?
```


## 评论 (3)

### Nero10578 · 2026-03-23

Somehow fixed by just adding this to the utils/backend.py not sure if its correct to just do this

```
# EXLLAMA EORA
    EXLLAMA_EORA = "exllama_eora"
```

### Qubitium · 2026-03-24

@Nero10578 Exllama_Eora kernel was removed. Checking to see if there are lingering reference to it. 

### CSY-ModelCloud · 2026-03-24

I notice our GPTQModel was installed without eidtable mode. maybe there's a build cache.
can you retry with `pip install -e . --no-build-isolation`?
