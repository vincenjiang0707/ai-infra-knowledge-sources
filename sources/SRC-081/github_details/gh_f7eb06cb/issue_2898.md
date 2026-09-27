# [Issue #2898] [BUG] ParoQuant Quant takes too long, Jit Compilation failed

source: https://github.com/ModelCloud/GPTQModel/issues/2898
state: closed | updated: 2026-05-19T12:35:41Z
labels: bug

## 正文

**Describe the bug**

I used ParoQuant to quantize Qwen3.5 27B, but it showed kernel compilation failure. Quantization on a single H100 takes two days.

**GPU Info**

Show output of:

```
nvidia-smi
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H100 80GB HBM3          On  |   00000000:19:00.0 Off |                    0 |
| N/A   36C    P0             71W /  700W |       4MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H100 80GB HBM3          On  |   00000000:3B:00.0 Off |                    0 |
| N/A   57C    P0            699W /  700W |   58333MiB /  81559MiB |    100%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA H100 80GB HBM3          On  |   00000000:4C:00.0 Off |                    0 |
| N/A   56C    P0            699W /  700W |   58333MiB /  81559MiB |    100%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA H100 80GB HBM3          On  |   00000000:5D:00.0 Off |                    0 |
| N/A   63C    P0            698W /  700W |   58333MiB /  81559MiB |    100%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA H100 80GB HBM3          On  |   00000000:9B:00.0 Off |                    0 |
| N/A   65C    P0            697W /  700W |   58333MiB /  81559MiB |    100%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA H100 80GB HBM3          On  |   00000000:BB:00.0 Off |                    0 |
| N/A   57C    P0            698W /  700W |   58333MiB /  81559MiB |    100%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA H100 80GB HBM3          On  |   00000000:CB:00.0 Off |                    0 |
| N/A   67C    P0            699W /  700W |   58333MiB /  81559MiB |    100%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA H100 80GB HBM3          On  |   00000000:DB:00.0 Off |                    0 |
| N/A   55C    P0            699W /  700W |   58333MiB /  81559MiB |    100%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
```

**Software Info**

Operation System/Version + Python Version

Show output of:
```
pip show gptqmodel torch transformers accelerate triton

Name: GPTQModel
Version: 7.0.0

---
Name: torch
Version: 2.11.0

---
Name: transformers
Version: 5.8.0

---
Name: accelerate
Version: 1.13.0

---
Name: triton
Version: 3.6.0

```


**To Reproduce**

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
from typing import List, Dict, Any
import argparse

from gptqmodel import GPTQModel
from gptqmodel.quantization.config import ParoConfig
from gptqmodel.quantization import QuantizeConfig, FORMAT, METHOD




    p.add_argument("--bits", type=int, default=4, help="量化位宽")
    p.add_argument("--group-size", type=int, default=128, help="分组大小")
    p.add_argument("--max-samples", type=int, default=128, help="最多使用多少条样本做校准")
    p.add_argument("--batch-size", type=int, default=1, help="校准时批大小")  
    p.add_argument("--max-length", type=int, default=4096, help="每条校准样本最大 token 长度")

    #Redirect Function

    p.add_argument("--keep-system", action="store_true", help="是否保留 system 消息")
    p.add_argument("--drop-assistant", action="store_true", help="是否丢弃 assistant 回复")

    return p.parse_args()


def main():
    args = parse_args()

    qcfg = ParoConfig(bits=args.bits, group_size=args.group_size)
    model = GPTQModel.load(args.model_id, qcfg, trust_remote_code=True)

    conversations = load_conversations(
        args.jsonl_path,
        keep_system=args.keep_system,
        drop_assistant=args.drop_assistant,
        max_samples=args.max_samples,
    )


    calibration_dataset = conversations_to_calibration_texts(
        conversations,
        model.tokenizer,
        max_length=args.max_length,
    )
    if not calibration_dataset:
        raise RuntimeError("chat_template 后没有可用文本，请检查 messages 格式。")

    model.quantize(calibration_dataset, batch_size=args.batch_size)
    os.makedirs(args.output_dir, exist_ok=True)
    model.save(args.output_dir)


if __name__ == "__main__":
    main()


**Expected behavior**

Why the kernel compiled failure? I update my nvcc and gcc , both not work 

**Model/Datasets**

qwen3.5 27B dense 

**Screenshots**

<img width="1008" height="549" alt="Image" src="https://github.com/user-attachments/assets/aa1b0080-a10f-4145-bc06-156b5a517e3d" />

**Additional context**

grep -n "fatal error\|error:\|Python.h\|nvcc\|CUDA\|fallback" /tmp/paroquant_run.log | head -200 INFO ENV: Auto setting CUDA_DEVICE_ORDER=PCI_BUS_ID for correctness. INFO ParoQuant rotation: torch.ops JIT compilation failed in 0.0s (estimated ~78s, -78s); using fallback path.

WARN  Python GIL is enabled: Multi-gpu quant acceleration for MoE models is sub-optimal and multi-core accelerated cpu packing is also disabled. We recommend Python >= 3.13.3t with Pytorch > 2.8 for mult-gpu quantization and multi-cpu packing with env `PYTHON_GIL=0`.
INFO  ENV: Auto setting PYTORCH_ALLOC_CONF='expandable_segments:True,max_split_size_mb:256,garbage_collection_threshold:0.7' for memory saving.
INFO  ENV: Auto setting CUDA_DEVICE_ORDER=PCI_BUS_ID for correctness.          
INFO  

┌─────────────┐    ┌────────────────────────┐    ┌────────────┐    ┌─────────┐
│ GPT-QModel  │ -> │ ▓▓▓▓▓▓▓▓▓▓▓▓ 16bit     │ -> │ ▒▒▒▒ 8bit  │ -> │ ░░ 4bit │
└─────────────┘    └────────────────────────┘    └────────────┘    └─────────┘
GPT-QModel   : 7.0.0
Transformers : 5.8.0
Torch        : 2.11.0+cu130
Triton       : 3.6.0
加载模型 ...
INFO  QuantizeConfig: offload_to_disk_path auto set to temporary dir `/tmp/gptqmodel__jszh3ej`
WARNING:fla.utils:Current Python version 3.10 is below the recommended 3.11 version. It is recommended to upgrade to Python 3.11 or higher for the best experience.
HF: overriding trust_remote_code=True to False for `/qwen35_27B_v2` because model_type `qwen3_5` is integrated in installed transformers as `Qwen3_5ForCausalLM`.
INFO  Loader: Auto dtype (native bfloat16): `torch.bfloat16`                   
INFO  Estimated Quantization BPW (bits per weight): 4.2875 bpw, based on [bits: 4, group_size: 128]
INFO  Loader: using checkpoint-backed lazy turtle source for `/qwen35_27B_v2`   
INFO:tokenicer.tokenicer:Tokenicer: Auto fixed pad_token_id=248044 (token='<|endoftext|>').
INFO  Model: Loaded `generation_config`: GenerationConfig {
  "eos_token_id": 248044,
  "output_attentions": false,
  "output_hidden_states": false,
  "use_cache": true
}

INFO  Model: `generation_config.json` not found. Skipped checking.             
INFO  Kernel: loaded -> `[]`                                                   
原始 conversations 数量: 128
[template] usable=128 bad=0
INFO  Packing Kernel: selected: `ParoLinear`                                   
INFO  Packing Kernel: selected: `ParoLinear`                                   
WARN  Calibration dataset size should be more than 256. Current: 128.          
INFO  Calibration: Sort in descending order by length                          
INFO  Calibration: Total padded tokens: 0                                      
INFO  Calibration: Total non-padded tokens: 524236                             
INFO  Calibration: Total tokens: 524236                                        
INFO  Disk subsystem write throughput detected at 832.0 MB/s.                  
INFO  ModuleLooper: capturing layer inputs from 128 calibration batches        
INFO  Offloading base modules to disk...                                        
INFO  ParoQuant: prewarming fused rotation extension...                        
INFO  ParoQuant rotation: compiling torch.ops JIT extension in `/root/.cache/gptqmodel/torch_extensions/paroquant/34bedede7df97941`.
INFO  ParoQuant rotation: torch.ops JIT compilation failed in 0.0s (estimated ~78s, -78s); using fallback path.

## 评论 (4)

### CSY-ModelCloud · 2026-05-19

i'm unable to reproduce this

i added a test file on CI

> https://github.com/ModelCloud/GPTQModel/blob/CSY/tests-paroQuant/tests/test_ParoQuant.py

and it looks good

> https://github.com/ModelCloud/GPTQModel/actions/runs/26074184285/job/76662807219

if could, run it on your env, it will print some debug infos, like:

```log
== Environment ==
python=3.14.3 free-threading build (main, Feb  3 2026, 22:55:28) [Clang 21.1.4 ]
torch=2.12.0+cu130
torch_cuda=13.0
cuda_home=/usr/local/cuda
cuda_available=True
device_count=1
device[0] capability=(8, 9)
== JIT Repro ==
INFO  ParoQuant rotation: compiling torch.ops JIT extension in `/tmp/gptqmodel/torch_extensions/26074184285/4/gptqmodel_test_26074184285_4_cu130_torch2.12.0_py3.14t_test_ParoQuant/test_ParoQuant/paroquant/db653c9b37d00559`.
[1/2] /usr/local/cuda/bin/nvcc -MD -MF rotation.cuda.o.d -DTORCH_EXTENSION_NAME=gptqmodel_paroquant_rotation -DTORCH_API_INCLUDE_EXTENSION_H -isystem /opt/uv/venvs/gptqmodel_test_26074184285_4_cu130_torch2.12.0_py3.14t_test_ParoQuant/lib/python3.14t/site-packages/torch/include -isystem /opt/uv/venvs/gptqmodel_test_26074184285_4_cu130_torch2.12.0_py3.14t_test_ParoQuant/lib/python3.14t/site-packages/torch/include/torch/csrc/api/include -isystem /usr/local/cuda/include -isystem /opt/uv/python/cpython-3.14.3+freethreaded-linux-x86_64-gnu/include/python3.14t -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -gencode=arch=compute_120,code=sm_120 -gencode=arch=compute_86,code=sm_86 -gencode=arch=compute_89,code=sm_89 -gencode=arch=compute_90,code=sm_90 --compiler-options '-fPIC' -O3 -std=c++17 -D_GLIBCXX_USE_CXX11_ABI=1 --threads 8 --optimize=3 -c /__w/GPTQModel/GPTQModel/gptqmodel_ext/paroquant/rotation.cu -o rotatio
[2/2] c++ rotation.cuda.o -shared -L/opt/uv/venvs/gptqmodel_test_26074184285_4_cu130_torch2.12.0_py3.14t_test_ParoQuant/lib/python3.14t/site-packages/torch/lib -lc10 -lc10_cuda -ltorch_cpu -ltorch_cuda -ltorch -ltorch_python -L/usr/local/cuda/lib64 -lcudart -o gptqmodel_paroquant_rotation.so
INFO  ParoQuant rotation: torch.ops JIT extension ready in 37s (estimated ~78s, -42s).
is_available=True
elapsed=36.602s
error=
```



### Jealousc11gx · 2026-05-19

Thanks for the help!
Here is the logs: 
`WARN  Python GIL is enabled: Multi-gpu quant acceleration for MoE models is sub-optimal and multi-core accelerated cpu packing is also disabled. We recommend Python >= 3.13.3t with Pytorch > 2.8 for mult-gpu quantization and multi-cpu packing with env `PYTHON_GIL=0`.




INFO  ENV: Auto setting PYTORCH_ALLOC_CONF='expandable_segments:True,max_split_size_mb:256,garbage_collection_threshold:0.7' for memory saving.                           
INFO  

┌─────────────┐    ┌────────────────────────┐    ┌────────────┐    ┌─────────┐
│ GPT-QModel  │ -> │ ▓▓▓▓▓▓▓▓▓▓▓▓ 16bit     │ -> │ ▒▒▒▒ 8bit  │ -> │ ░░ 4bit │
└─────────────┘    └────────────────────────┘    └────────────┘    └─────────┘
GPT-QModel   : 7.0.0
Transformers : 5.8.0
Torch        : 2.11.0+cu130
Triton       : 3.6.0
== Environment ==
python=3.10.12 (main, Mar  3 2026, 11:56:32) [GCC 11.4.0]
torch=2.11.0+cu130
torch_cuda=13.0
cuda_home=/usr/local/cuda-12.9
cuda_available=True
device_count=8
device[0] capability=(9, 0)
device[1] capability=(9, 0)
device[2] capability=(9, 0)
device[3] capability=(9, 0)
device[4] capability=(9, 0)
device[5] capability=(9, 0)
device[6] capability=(9, 0)
device[7] capability=(9, 0)

== JIT Repro ==
INFO  ParoQuant rotation: compiling torch.ops JIT extension in `/root/.cache/gptqmodel/torch_extensions/paroquant/34bedede7df97941`.                                      
INFO  ParoQuant rotation: torch.ops JIT compilation failed in 0.0s (estimated ~78s, -78s); using fallback path.                                                           
is_available=False
elapsed=0.010s
error=ParoQuant rotation: failed to build torch.ops JIT extension: [Errno 2] No such file or directory: '/mnt_hdd/data/user_workspace/cll_seek/.venv/lib/python3.10/site-packages/gptqmodel_ext/paroquant/rotation.cu'

JIT repro failed; skip quantize repro.`

### CSY-ModelCloud · 2026-05-19

> Thanks for the help! Here is the logs: `WARN Python GIL is enabled: Multi-gpu quant acceleration for MoE models is sub-optimal and multi-core accelerated cpu packing is also disabled. We recommend Python >= 3.13.3t with Pytorch > 2.8 for mult-gpu quantization and multi-cpu packing with env `PYTHON_GIL=0`.
> 
> INFO ENV: Auto setting PYTORCH_ALLOC_CONF='expandable_segments:True,max_split_size_mb:256,garbage_collection_threshold:0.7' for memory saving. INFO
> 
> ┌─────────────┐ ┌────────────────────────┐ ┌────────────┐ ┌─────────┐ │ GPT-QModel │ -> │ ▓▓▓▓▓▓▓▓▓▓▓▓ 16bit │ -> │ ▒▒▒▒ 8bit │ -> │ ░░ 4bit │ └─────────────┘ └────────────────────────┘ └────────────┘ └─────────┘ GPT-QModel : 7.0.0 Transformers : 5.8.0 Torch : 2.11.0+cu130 Triton : 3.6.0 == Environment == python=3.10.12 (main, Mar 3 2026, 11:56:32) [GCC 11.4.0] torch=2.11.0+cu130 torch_cuda=13.0 cuda_home=/usr/local/cuda-12.9 cuda_available=True device_count=8 device[0] capability=(9, 0) device[1] capability=(9, 0) device[2] capability=(9, 0) device[3] capability=(9, 0) device[4] capability=(9, 0) device[5] capability=(9, 0) device[6] capability=(9, 0) device[7] capability=(9, 0)
> 
> == JIT Repro == INFO ParoQuant rotation: compiling torch.ops JIT extension in `/root/.cache/gptqmodel/torch_extensions/paroquant/34bedede7df97941`. INFO ParoQuant rotation: torch.ops JIT compilation failed in 0.0s (estimated ~78s, -78s); using fallback path. is_available=False elapsed=0.010s error=ParoQuant rotation: failed to build torch.ops JIT extension: [Errno 2] No such file or directory: '/mnt_hdd/data/user_workspace/cll_seek/.venv/lib/python3.10/site-packages/gptqmodel_ext/paroquant/rotation.cu'
> 
> JIT repro failed; skip quantize repro.`

it is our mistake..
paroquant kernel source was not included in release. since our CI always pip install source directly, we didn't find this issue until you 
i'll update ci logic for this, too

you can use latest commit to bypass

> pip install -U git+https://github.com/ModelCloud/GPTQModel.git@refs/pull/2900/head

### Jealousc11gx · 2026-05-19

Hi， I successfully compiled it, but found the process is still taking very long.

How long does it typically take to quantize a ~30B model on a single H100 or similar GPU? Is my timing normal? Also, I noticed that as the quantization progresses, the VRAM usage is relatively low, but the time per step keeps getting longer?

<img width="640" height="82" alt="Image" src="https://github.com/user-attachments/assets/d567f79c-eeb2-4733-82ff-afca94e45653" />

<img width="1543" height="52" alt="Image" src="https://github.com/user-attachments/assets/c3996c64-16dd-4887-9501-6347da4b9d80" />

<img width="1539" height="60" alt="Image" src="https://github.com/user-attachments/assets/4f6145dc-0fc9-4594-b54c-ff6fd58b9eca" />
