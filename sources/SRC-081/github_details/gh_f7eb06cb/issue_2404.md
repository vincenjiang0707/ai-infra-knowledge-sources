# [Issue #2404] [BUG]ImportError: cannot import name 'no_init_weights' from 'transformers.modeling_utils'

source: https://github.com/ModelCloud/GPTQModel/issues/2404
state: closed | updated: 2026-02-11T23:15:09Z
labels: bug

## 正文

**Describe the bug**

can not run gptmodel with latest transformer.

```python
from gptqmodel import GPTQModel, QuantizeConfig
```

```shell
from transformers.modeling_utils import no_init_weights
ImportError: cannot import name 'no_init_weights' from 'transformers.modeling_utils'
```

**GPU Info**

Show output of:

```
nvidia-smi
```

```shell
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.65.06              Driver Version: 580.65.06      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A800 80GB PCIe          On  |   00000000:56:00.0 Off |                  Off |
| N/A   33C    P0             43W /  300W |       0MiB /  81920MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

**Software Info**

Operation System/Version + Python Version

Show output of:
```
pip show gptqmodel torch transformers accelerate triton
```

```shell
Name: accelerate
Version: 1.12.0
Location: /root/autodl-tmp/quant/.venv/lib/python3.13/site-packages
Requires: huggingface-hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: gptqmodel
---
Name: gptqmodel
Version: 5.6.12+cu128torch2.8
Location: /root/autodl-tmp/quant/.venv/lib/python3.13/site-packages
Requires: accelerate, datasets, device-smi, dill, hf-transfer, huggingface-hub, kernels, logbar, maturin, numpy, packaging, pillow, protobuf, pyarrow, pypcre, safetensors, threadpoolctl, tokenicer, torch, torchao, transformers
Required-by:
---
Name: torch
Version: 2.10.0
Location: /root/autodl-tmp/quant/.venv/lib/python3.13/site-packages
Requires: cuda-bindings, filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-cufile-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvshmem-cu12, nvidia-nvtx-cu12, setuptools, sympy, triton, typing-extensions
Required-by: accelerate, bitblas, gptqmodel
---
Name: transformers
Version: 5.1.0
Location: /root/autodl-tmp/quant/.venv/lib/python3.13/site-packages
Requires: huggingface-hub, numpy, packaging, pyyaml, regex, safetensors, tokenizers, tqdm, typer-slim
Required-by: gptqmodel, tokenicer
---
Name: triton
Version: 3.6.0
Location: /root/autodl-tmp/quant/.venv/lib/python3.13/site-packages
Requires:
Required-by: torch
```

**If you are reporting an inference bug of a post-quantized model, please post the content of `config.json` and `quantize_config.json`.**

**To Reproduce**

How to reproduce this bug if possible.

run 

```python
from gptqmodel import GPTQModel, QuantizeConfig
```

**Expected behavior**

A clear and concise description of what you expected to happen.

**Model/Datasets**

Make sure your model/dataset is downloadable (on HF for example) so we can reproduce your issue.

**Screenshots**

If applicable, add screenshots to help explain your problem.

**Additional context**

Add any other context about the problem here.


## 评论 (2)

### FayeSpica · 2026-02-07

install latest gptqmodel from github sovle the issue

```shell
uv pip install git+https://github.com/ModelCloud/GPTQModel.git
```

### Qubitium · 2026-02-11

@FayeSpica 5.7.0 released so this should be resolved.
