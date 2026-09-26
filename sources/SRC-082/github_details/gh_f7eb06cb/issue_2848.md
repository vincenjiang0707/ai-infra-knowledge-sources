# [Issue #2848] [BUG]During the quantization process, an error occurs.

source: https://github.com/ModelCloud/GPTQModel/issues/2848
state: closed | updated: 2026-04-30T11:01:33Z
labels: bug

## 正文

The following error appears for **each layer**

INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+----------+--------------+---------+                         
INFO  | process | layer | module                    | feat: in, out | dtype: size  | loss         | samples | damp    | time  | fwd_time | (v)ram       | dynamic |                         
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+----------+--------------+---------+                         
INFO  | gptq    | 0     | linear_attn.in_proj_qkv   | 4096, 8192    | bf16: 66.0MB | 0.0001319119 | 468028  | 0.05000 | 0.587 | 2.362    | cuda 1.67G   |         |                         
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+----------+--------------+---------+                         
INFO  | gptq    | 0     | linear_attn.in_proj_z     | 4096, 4096    | bf16: 33.0MB | 0.0000661753 | 468028  | 0.05000 | 0.395 | 2.522    | cuda 1.84G   |         |                         
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+----------+--------------+---------+                         
WARN  Quantization: Module `linear_attn.out_proj` -> Starting damp recovery at `damp_percent=0.05000`, increment step `0.01000`.                                                            
WARN  Quantization: Module `linear_attn.out_proj` -> Damp recovery failed after reaching `damp_percent=1.00000`.                                                                            
WARN  Quantization: Module `linear_attn.out_proj` -> Applying Hessian diagonal floor (+1.00e-06) to recover positive definiteness.                                                          
WARN  Quantization: Module `linear_attn.out_proj` -> Starting damp recovery at `damp_percent=0.05000`, increment step `0.01000`.                                                            
WARN  Quantization: Module `linear_attn.out_proj` -> Damp recovery failed after reaching `damp_percent=1.00000`.                                                                            
WARN  Quantization: Module `linear_attn.out_proj` -> Increasing Hessian diagonal floor to +1.00e-05.                                                                                        
WARN  Quantization: Module `linear_attn.out_proj` -> Starting damp recovery at `damp_percent=0.05000`, increment step `0.01000`.                                                            
WARN  Quantization: Module `linear_attn.out_proj` -> Damp recovery failed after reaching `damp_percent=1.00000`.                                                                            
WARN  Quantization: Module `linear_attn.out_proj` -> Increasing Hessian diagonal floor to +1.00e-04.                                                                                        
WARN  Quantization: Module `linear_attn.out_proj` -> Starting damp recovery at `damp_percent=0.05000`, increment step `0.01000`.                                                            
WARN  Quantization: Module `linear_attn.out_proj` -> Damp recovery failed after reaching `damp_percent=1.00000`.                                                                            
WARN  Quantization: Module `linear_attn.out_proj` -> Increasing Hessian diagonal floor to +1.00e-03.                                                                                        
WARN  Quantization: Module `linear_attn.out_proj` -> Starting damp recovery at `damp_percent=0.05000`, increment step `0.01000`.                                                            
WARN  Quantization: Module `linear_attn.out_proj` -> Damp recovery failed after reaching `damp_percent=1.00000`.                                                                            
WARN  Quantization: Module `linear_attn.out_proj` -> Increasing Hessian diagonal floor to +1.00e-02.                                                                                        
WARN  Quantization: Module `linear_attn.out_proj` -> Starting damp recovery at `damp_percent=0.05000`, increment step `0.01000`.                                                            
WARN  Quantization: Module `linear_attn.out_proj` -> Damp recovery failed after reaching `damp_percent=1.00000`.                                                                            
WARN  Quantization: Module `linear_attn.out_proj` -> Increasing Hessian diagonal floor to +1.00e-01.                                                                                        
WARN  Quantization: Module `linear_attn.out_proj` -> Starting damp recovery at `damp_percent=0.05000`, increment step `0.01000`.                                                            
WARN  Quantization: Module `linear_attn.out_proj` -> Damp recovery failed after reaching `damp_percent=1.00000`.                                                                            
**ERROR Quantization: Module `linear_attn.out_proj` -> Hessian remained non positive-definite after diagonal floor attempts. Last `damp_percent` tried = 1.00000.**                             
INFO  | gptq    | 0     | linear_attn.out_proj      | 4096, 4096    | bf16: 33.0MB | rtn fallback | 468028  | 1.00000 | 3.150 | 26.906   | cuda 2.85G   |         |                         
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+----------+--------------+---------+          

**Software Info**

Operation System/Version + Python Version

Show output of:
```
pip show gptqmodel torch transformers accelerate triton
Name: GPTQModel
Version: 7.0.0
Summary: Production ready LLM model compression/quantization toolkit with hw accelerated inference support for both cpu/gpu via HF, vLLM, and SGLang.
Home-page: https://github.com/ModelCloud/GPTQModel
Author: 
Author-email: ModelCloud <qubitium@modelcloud.ai>
License-Expression: Apache-2.0
Location: /home/macld/miniconda3/envs/gptqmodel/lib/python3.12/site-packages
Requires: accelerate, datasets, defuser, device-smi, dill, jinja2, logbar, maturin, ninja, numpy, packaging, pillow, protobuf, pyarrow, pypcre, safetensors, threadpoolctl, tokenicer, torch, torchao, transformers
Required-by: 
---
Name: torch
Version: 2.8.0
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org/
Author: PyTorch Team
Author-email: packages@pytorch.org
License: BSD-3-Clause
Location: /home/macld/miniconda3/envs/gptqmodel/lib/python3.12/site-packages
Requires: filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-cufile-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvtx-cu12, setuptools, sympy, triton, typing-extensions
Required-by: accelerate, causal-conv1d, flash-linear-attention, GPTQModel, peft, torchaudio, torchvision
---
Name: transformers
Version: 5.7.0
Summary: Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.
Home-page: https://github.com/huggingface/transformers
Author: The Hugging Face team (past and future) with the help of all our contributors (https://github.com/huggingface/transformers/graphs/contributors)
Author-email: transformers@huggingface.co
License: Apache 2.0 License
Location: /home/macld/miniconda3/envs/gptqmodel/lib/python3.12/site-packages
Requires: huggingface-hub, numpy, packaging, pyyaml, regex, safetensors, tokenizers, tqdm, typer
Required-by: Defuser, flash-linear-attention, GPTQModel, peft
---
Name: accelerate
Version: 1.13.0
Summary: Accelerate
Home-page: https://github.com/huggingface/accelerate
Author: The Hugging Face team
Author-email: transformers@huggingface.co
License: Apache
Location: /home/macld/miniconda3/envs/gptqmodel/lib/python3.12/site-packages
Requires: huggingface_hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: GPTQModel, peft
---
Name: triton
Version: 3.4.0
Summary: A language and compiler for custom Deep Learning operations
Home-page: https://github.com/triton-lang/triton/
Author: Philippe Tillet
Author-email: phil@openai.com
License: 
Location: /home/macld/miniconda3/envs/gptqmodel/lib/python3.12/site-packages
Requires: setuptools
Required-by: torch

```


**office code **

```
from datasets import load_dataset
from gptqmodel import GPTQConfig, GPTQModel

model_id = "Qwen/Qwen3.5-9B"
quant_path = "Qwen3.5-9b-gptqmodel-4bit"

calibration_dataset = load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
  ).select(range(1024))["text"]

quant_config = GPTQConfig(bits=4, group_size=128)

model = GPTQModel.load(model_id, quant_config)

# increase `batch_size` to match GPU/VRAM specs to speed up quantization
model.quantize(calibration_dataset, batch_size=1)

model.save(quant_path)
```

The quantization can eventually succeed, but the accuracy loss after quantization is noticeable, and output loops occur frequently.

## 评论 (3)

### ZX-ModelCloud · 2026-04-30

I used the exact same Python environment and code as you, but I was unable to reproduce your issue.
Could you please provide a more complete log? This would help me better resolve this issue.

### arkerwu · 2026-04-30

[log.zip](https://github.com/user-attachments/files/27239676/log.zip)
I've just run the log for a while.

### arkerwu · 2026-04-30

After a clean install of the latest version in a new environment, everything works fine
