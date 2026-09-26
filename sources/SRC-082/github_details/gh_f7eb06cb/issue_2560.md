# [Issue #2560] [BUG] Defuser causing error to pre-transformers v5 MoE model (GLM-4.6)

source: https://github.com/ModelCloud/GPTQModel/issues/2560
state: closed | updated: 2026-03-19T06:53:04Z
labels: bug

## 正文

**Describe the bug**

After the latest defuser update that makes quanting Qwen3.5 models possible, I found it does not work with GLM-4.6 which was a model supported since pre transformers v5. 

To get it to quant, I seem to have to use transformers 4.57.6 as with the latest transformers v5 I get this error when trying to quant:

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
| 30%   32C    P8             21W /  600W |      15MiB /  97887MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    Off |   00000000:C3:00.0 Off |                  Off |
| 30%   35C    P8             14W /  600W |      15MiB /  97887MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            1735      G   /usr/lib/xorg/Xorg                        4MiB |
|    1   N/A  N/A            1735      G   /usr/lib/xorg/Xorg                        4MiB |
+-----------------------------------------------------------------------------------------+
```

**Software Info**

```
            .-/+oossssoo+/-.               arli@arli-super-server 
        `:+ssssssssssssssssss+:`           ---------------------- 
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 24.04.4 LTS x86_64 
    .ossssssssssssssssssdMMMNysssso.       Host: Super Server 0123456789 
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 6.17.0-19-generic 
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 21 hours, 35 mins 
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 1687 (dpkg), 10 (snap) 
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.2.21 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Resolution: 1024x768 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Terminal: /dev/pts/0 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: Genuine Intel 0000%@ (32) @ 3.600GHz 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   GPU: NVIDIA c3:00.0 NVIDIA Corporation Device 2bb1 
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   GPU: NVIDIA 51:00.0 NVIDIA Corporation Device 2bb1 
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/    Memory: 13816MiB / 515394MiB 
  +sssssssssdmydMMMMMMMMddddyssssssss+
   /ssssssssssshdmNNNNmyNMMMMhssssss/                              
    .ossssssssssssssssssdMMMNysssso.                               
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.
```

Python 3.14t, CUDA 12.9.1, Pytorch 2.10.0

Show output of:
```
Using Python 3.14.0 environment at: GPTQModel/GPTQModel/.venv
Name: accelerate
Version: 1.13.0
Location: /home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages
Requires: huggingface-hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: gptqmodel
---
Name: gptqmodel
Version: 5.8.0
Location: /home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages
Requires: accelerate, datasets, defuser, device-smi, dill, huggingface-hub, kernels, logbar, maturin, numpy, packaging, pillow, protobuf, pyarrow, pypcre, safetensors, setuptools, threadpoolctl, tokenicer, torch, torchao, transformers
Required-by:
---
Name: torch
Version: 2.10.0
Location: /home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages
Requires: cuda-bindings, filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-cufile-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvshmem-cu12, nvidia-nvtx-cu12, setuptools, sympy, triton, typing-extensions
Required-by: accelerate, gptqmodel, torchvision
---
Name: transformers
Version: 5.3.0
Location: /home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages
Requires: huggingface-hub, numpy, packaging, pyyaml, regex, safetensors, tokenizers, tqdm, typer
Required-by: defuser, gptqmodel
---
Name: triton
Version: 3.6.0
Location: /home/arli/GPTQModel/GPTQModel/.venv/lib/python3.14t/site-packages
Requires:
Required-by: torch
```

**To Reproduce**

Try GLM-4.6 Quantization with the following script:

```
import torch
from datasets import load_dataset
from gptqmodel import GPTQModel, QuantizeConfig
from gptqmodel.quantization.config import HessianConfig, VramStrategy, GcMode, MoEConfig, ExpertsRoutingBypass
from transformers import AutoTokenizer
import json
import os

# Set PyTorch memory allocation configuration
os.environ["PYTORCH_ALLOC_CONF"] = "expandable_segments:True"

# 1. Configuration
MODEL_ID = "/home/arli/models/GLM-4.6-Derestricted-v6"
DATASET_ID = "neuralmagic/LLM_compression_calibration"
DATASET_SPLIT = "train"

NUM_CALIBRATION_SAMPLES = 2048

SAVE_DIR = MODEL_ID + "-GPTQModel-Int4-Int8"

# 2. Load Tokenizer & Prepare Data
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, use_fast=True)

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

# 3. Configure Quantization
quant_config = QuantizeConfig(
    bits=4,
    group_size=128,
    sym=True,
    desc_act=False,
)

quant_config.dynamic = {
    r"-:.*embed_tokens.*": {},
    r"-:.*shared_head.*": {},
    r"-:.*shared_experts.*": {},
    r"-:.*lm_head.*": {},
    r"+:model[.]layers[.].*[.]self_attn[.].*": {"bits": 8},
    r"+:model[.]layers[.]([0-3]|89|9[0-2])[.].*": {"bits": 8},
}

# 4. Load Model
print(f"Loading model from {MODEL_ID}...")
model = GPTQModel.load(
    MODEL_ID,
    quantize_config=quant_config,
    trust_remote_code=True,
)

# 5. Quantize
print("Starting quantization...")
model.quantize(
    calibration_dataset, 
)

# 6. Save
print(f"Saving model to {SAVE_DIR}...")
model.save(SAVE_DIR)

print("Done!")
```

**Expected behavior**

GLM-4.6 should be able to be quantized even on the latest transformers version, but it requires older transformers version to work.


## 评论 (3)

### Qubitium · 2026-03-19

@ZX-ModelCloud 

### ZX-ModelCloud · 2026-03-19

@Nero10578 
Please provide the detailed error stacktrace and `defuser` version.
Installing `defuser 0.0.15` should resolve your issue.

### Nero10578 · 2026-03-19

> [@Nero10578](https://github.com/Nero10578) Please provide the detailed error stacktrace and `defuser` version. Installing `defuser 0.0.15` should resolve your issue.

Seems to be solved!
