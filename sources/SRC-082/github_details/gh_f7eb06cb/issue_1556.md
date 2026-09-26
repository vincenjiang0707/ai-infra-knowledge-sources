# [Issue #1556] [BUG]TypeError: internvl_chat isn't supported yet.

source: https://github.com/ModelCloud/GPTQModel/issues/1556
state: open | updated: 2025-12-23T12:04:47Z
labels: bug

## 正文

**Describe the bug**
error:
```
Traceback (most recent call last):
  File "/home/gptq_v2_In.py", line 32, in <module>
    model = GPTQModel.load(model_id, quant_config,trust_remote_code=True)
  File "/usr/local/lib/python3.10/site-packages/gptqmodel/models/auto.py", line 260, in load
    return cls.from_pretrained(
  File "/usr/local/lib/python3.10/site-packages/gptqmodel/models/auto.py", line 288, in from_pretrained
    model_type = check_and_get_model_type(model_id_or_path, trust_remote_code)
  File "/usr/local/lib/python3.10/site-packages/gptqmodel/models/auto.py", line 197, in check_and_get_model_type
    raise TypeError(f"{config.model_type} isn't supported yet.")
TypeError: internvl_chat isn't supported yet.
```
python code:
```
from datasets import load_dataset
from gptqmodel import GPTQModel, QuantizeConfig

import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"


model_id = "model/InternVL2.5/checkpoint-37446"
quant_path = "model/InternVL2.5/checkpoint-37446-4bit-v2"

calibration_dataset = load_dataset(
    "json",
    data_files="data_markdown_gpro_train.jsonl",
    split="train"
  )


quant_config = QuantizeConfig(bits=4, group_size=128)

model = GPTQModel.load(model_id, quant_config,trust_remote_code=True)

# increase `batch_size` to match gpu/vram specs to speed up quantization
model.quantize(calibration_dataset=calibration_dataset, batch_size=1)

model.save(quant_path)

```
**GPU Info**

Show output of:

```
nvidia-smi
A100-PCIE-40GB
```

**Software Info**

Operation System/Version + Python Version

Show output of:
```
Name: gptqmodel
Version: 3.0.0.dev0
Summary: Production ready LLM model compression/quantization toolkit with hw accelerated inference support for both cpu/gpu via HF, vLLM, and SGLang.
Home-page: https://github.com/ModelCloud/GPTQModel
Author: ModelCloud
Author-email: qubitium@modelcloud.ai
License: Apache 2.0
Location: /usr/local/lib/python3.10/site-packages
Requires: accelerate, datasets, device-smi, hf-transfer, huggingface-hub, logbar, numpy, packaging, pillow, protobuf, random-word, safetensors, threadpoolctl, tokenicer, torch, transformers
Required-by: #N/A
---
Name: torch
Version: 2.6.0
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org/
Author: PyTorch Team
Author-email: packages@pytorch.org
License: BSD-3-Clause
Location: /usr/local/lib/python3.10/site-packages
Requires: filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvtx-cu12, sympy, triton, typing-extensions
Required-by: accelerate, adaseq, auto_gptq, autoawq, autoawq_kernels, basicsr, bitsandbytes, clip, compressed-tensors, ddpm-guided-diffusion, deepspeed, easyrobust, face-alignment, fairscale, fairseq, fastai, flash_attn, flashinfer-python, gptqmodel, kornia, lm_eval, lmdeploy, local-attention, lpips, nerfacc, open_clip_torch, optimum, outlines, peft, phaseaug, ptflops, pytorch-metric-learning, pytorch-wavelets, rotary-embedding-torch, smplx, speechbrain, stanza, taming-transformers-rom1504, tensordict, thop, timm, torchaudio, torchdata, torchmetrics, torchsde, torchvision, unicore, vllm, vllm-flash-attn, xformers, xgrammar
---
Name: transformers
Version: 4.51.3
Summary: State-of-the-art Machine Learning for JAX, PyTorch and TensorFlow
Home-page: https://github.com/huggingface/transformers
Author: The Hugging Face team (past and future) with the help of all our contributors (https://github.com/huggingface/transformers/graphs/contributors)
Author-email: transformers@huggingface.co
License: Apache 2.0 License
Location: /usr/local/lib/python3.10/site-packages
Requires: filelock, huggingface-hub, numpy, packaging, pyyaml, regex, requests, safetensors, tokenizers, tqdm
Required-by: adaseq, auto_gptq, autoawq, compressed-tensors, gptqmodel, lm_eval, lmdeploy, ms_swift, optimum, pai-easycv, peft, text2sql-lgesql, tokenicer, transformers-stream-generator, trl, vllm, xgrammar
---
Name: accelerate
Version: 1.6.0
Summary: Accelerate
Home-page: https://github.com/huggingface/accelerate
Author: The HuggingFace team
Author-email: zach.mueller@huggingface.co
License: Apache
Location: /usr/local/lib/python3.10/site-packages
Requires: huggingface-hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: auto_gptq, autoawq, gptqmodel, lm_eval, lmdeploy, ms_swift, peft, trl
---
Name: triton
Version: 3.2.0
Summary: A language and compiler for custom Deep Learning operations
Home-page: https://github.com/triton-lang/triton/
Author: Philippe Tillet
Author-email: phil@openai.com
License: 
Location: /usr/local/lib/python3.10/site-packages
Requires: 
Required-by: autoawq, lmdeploy, torch
```

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


## 评论 (3)

### RunningLeon · 2025-07-17

any update on this issue?


### skylake5200 · 2025-12-22

+1 😢

Don't you have any plans to support it?

### Qubitium · 2025-12-23

> +1 😢
> 
> Don't you have any plans to support it?

It is not that difficult to add new model support unless it is very exotic in nature. Check existing model defs for guide.  We welcome all contributions!


