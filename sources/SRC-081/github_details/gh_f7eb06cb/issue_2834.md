# [Issue #2834] [BUG]

source: https://github.com/ModelCloud/GPTQModel/issues/2834
state: closed | updated: 2026-05-07T09:07:40Z
labels: bug

## 正文

**Describe the bug**

I encountered the following problem while trying to quantify Qwen2.5-1.5B-Instruct. I tried many versions but none of them worked.

**GPU Info**

Show output of:

```
nvidia-smi
```

<img width="835" height="705" alt="Image" src="https://github.com/user-attachments/assets/f9a46229-ddd3-47cf-a9e4-eb16ddf2400d" />

**Software Info**

Operation System/Version + Python Version

Show output of:
```
pip show gptqmodel torch transformers accelerate triton
```
(gptq) user@user-Super-Server:~/YKK/AICASGC$ pip show gptqmodel torch transformers accelerate triton
Name: GPTQModel
Version: 5.4.0+cu126torch2.8
Summary: Production ready LLM model compression/quantization toolkit with hw accelerated inference support for both cpu/gpu via HF, vLLM, and SGLang.
Home-page: https://github.com/ModelCloud/GPTQModel
Author: 
Author-email: ModelCloud <qubitium@modelcloud.ai>
License-Expression: Apache-2.0
Location: /home/user/anaconda3/envs/gptq/lib/python3.11/site-packages
Requires: accelerate, datasets, device-smi, dill, hf_transfer, huggingface_hub, logbar, maturin, numpy, packaging, pillow, protobuf, pyarrow, pypcre, random_word, safetensors, threadpoolctl, tokenicer, torch, torchao, transformers
Required-by: 
---
Name: torch
Version: 2.8.0+cu126
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org/
Author: PyTorch Team
Author-email: packages@pytorch.org
License: BSD-3-Clause
Location: /home/user/anaconda3/envs/gptq/lib/python3.11/site-packages
Requires: filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-cufile-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvtx-cu12, sympy, triton, typing-extensions
Required-by: accelerate, GPTQModel, torchaudio, torchvision
---
Name: transformers
Version: 5.6.2
Summary: Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.
Home-page: https://github.com/huggingface/transformers
Author: The Hugging Face team (past and future) with the help of all our contributors (https://github.com/huggingface/transformers/graphs/contributors)
Author-email: transformers@huggingface.co
License: Apache 2.0 License
Location: /home/user/anaconda3/envs/gptq/lib/python3.11/site-packages
Requires: huggingface-hub, numpy, packaging, pyyaml, regex, safetensors, tokenizers, tqdm, typer
Required-by: GPTQModel
---
Name: accelerate
Version: 1.13.0
Summary: Accelerate
Home-page: https://github.com/huggingface/accelerate
Author: The Hugging Face team
Author-email: transformers@huggingface.co
License: Apache
Location: /home/user/anaconda3/envs/gptq/lib/python3.11/site-packages
Requires: huggingface_hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: GPTQModel
---
Name: triton
Version: 3.4.0
Summary: A language and compiler for custom Deep Learning operations
Home-page: https://github.com/triton-lang/triton/
Author: Philippe Tillet
Author-email: phil@openai.com
License: 
Location: /home/user/anaconda3/envs/gptq/lib/python3.11/site-packages
Requires: setuptools
Required-by: torch


**If you are reporting an inference bug of a post-quantized model, please post the content of `config.json` and `quantize_config.json`.**

**To Reproduce**

How to reproduce this bug if possible.

**Expected behavior**

A clear and concise description of what you expected to happen.

**Model/Datasets**

Make sure your model/dataset is downloadable (on HF for example) so we can reproduce your issue.

**Screenshots**

If applicable, add screenshots to help explain your problem.

**Additional context**

Add any other context about the problem here.


## 评论 (1)

### Qubitium · 2026-04-28

@kkofStudy What is the error?
