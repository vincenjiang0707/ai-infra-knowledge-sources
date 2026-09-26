# [Issue #2678] [BUG]Quantilze Qwen3.5 27B OOM

source: https://github.com/ModelCloud/GPTQModel/issues/2678
state: closed | updated: 2026-04-08T12:05:00Z
labels: bug

## 正文

**Describe the bug**

During the quantization of Qwen3.5 27B, there is a oom, like memory leak or something, the memory consumption increases linearly, no matter I use 4 h200 or 8 h200
**GPU Info**

Show output of:

```
nvidia-smi
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.54.15              Driver Version: 550.54.15      CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H200                    On  |   00000000:19:00.0 Off |                    0 |
| N/A   34C    P0             78W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H200                    On  |   00000000:3B:00.0 Off |                    0 |
| N/A   32C    P0             76W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA H200                    On  |   00000000:4C:00.0 Off |                    0 |
| N/A   31C    P0             76W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA H200                    On  |   00000000:5D:00.0 Off |                    0 |
| N/A   33C    P0             77W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA H200                    On  |   00000000:9B:00.0 Off |                    0 |
| N/A   32C    P0             76W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA H200                    On  |   00000000:BB:00.0 Off |                    0 |
| N/A   31C    P0             75W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA H200                    On  |   00000000:CB:00.0 Off |                    0 |
| N/A   32C    P0             75W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA H200                    On  |   00000000:DB:00.0 Off |                    0 |
| N/A   30C    P0             74W /  700W |       0MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

```

**Software Info**

Operation System/Version + Python Version

Show output of:
```
pip show gptqmodel torch transformers accelerate triton

Name: GPTQModel
Version: 6.0.0
Summary: Production ready LLM model compression/quantization toolkit with hw accelerated inference support for both cpu/gpu via HF, vLLM, and SGLang.
Home-page: https://github.com/ModelCloud/GPTQModel
Author: 
Author-email: ModelCloud <qubitium@modelcloud.ai>
License-Expression: Apache-2.0
Location: /opt/miniconda3.10/lib/python3.10/site-packages
Requires: accelerate, datasets, defuser, device-smi, dill, hf_transfer, huggingface_hub, kernels, logbar, maturin, numpy, packaging, pillow, protobuf, pyarrow, pypcre, safetensors, setuptools, threadpoolctl, tokenicer, torch, torchao, transformers
Required-by: 
---
Name: torch
Version: 2.10.0
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org
Author: 
Author-email: PyTorch Team <packages@pytorch.org>
License: BSD-3-Clause
Location: /opt/miniconda3.10/lib/python3.10/site-packages
Requires: cuda-bindings, filelock, fsspec, jinja2, networkx, nvidia-cublas-cu12, nvidia-cuda-cupti-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-runtime-cu12, nvidia-cudnn-cu12, nvidia-cufft-cu12, nvidia-cufile-cu12, nvidia-curand-cu12, nvidia-cusolver-cu12, nvidia-cusparse-cu12, nvidia-cusparselt-cu12, nvidia-nccl-cu12, nvidia-nvjitlink-cu12, nvidia-nvshmem-cu12, nvidia-nvtx-cu12, sympy, triton, typing-extensions
Required-by: accelerate, auto-round, GPTQModel, torchvision
---
Name: transformers
Version: 5.3.0
Summary: Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.
Home-page: https://github.com/huggingface/transformers
Author: The Hugging Face team (past and future) with the help of all our contributors (https://github.com/huggingface/transformers/graphs/contributors)
Author-email: transformers@huggingface.co
License: Apache 2.0 License
Location: /opt/miniconda3.10/lib/python3.10/site-packages
Requires: huggingface-hub, numpy, packaging, pyyaml, regex, safetensors, tokenizers, tqdm, typer
Required-by: auto-round, Defuser, GPTQModel
---
Name: accelerate
Version: 1.13.0
Summary: Accelerate
Home-page: https://github.com/huggingface/accelerate
Author: The Hugging Face team
Author-email: transformers@huggingface.co
License: Apache
Location: /opt/miniconda3.10/lib/python3.10/site-packages
Requires: huggingface_hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: auto-round, GPTQModel
---
Name: triton
Version: 3.6.0
Summary: A language and compiler for custom Deep Learning operations
Home-page: https://github.com/triton-lang/triton/
Author: Philippe Tillet
Author-email: phil@openai.com
License: 
Location: /opt/miniconda3.10/lib/python3.10/site-packages
Requires: 
Required-by: torch

```


**To Reproduce**

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
from typing import List, Dict, Any
import argparse

from gptqmodel import GPTQModel
from gptqmodel.quantization import QuantizeConfig, FORMAT, METHOD


def _extract_text_from_content(content: Any) -> str:

    if isinstance(content, str):
        return content.strip()

    if isinstance(content, list):
        texts = []
        for item in content:
            if isinstance(item, str):
                t = item.strip()
                if t:
                    texts.append(t)
            elif isinstance(item, dict):
                if item.get("type") == "text":
                    t = str(item.get("text", "")).strip()
                    if t:
                        texts.append(t)
        return "\n".join(texts).strip()

    return ""


def _clean_messages(
    msgs: List[Dict[str, Any]],
    keep_system: bool,
    drop_assistant: bool,
) -> List[Dict[str, str]]:
    out: List[Dict[str, str]] = []

    for m in msgs:
        role = m.get("role", "")
        if role not in {"system", "user", "assistant"}:
            continue
        if not keep_system and role == "system":
            continue
        if drop_assistant and role == "assistant":
            continue

        text = _extract_text_from_content(m.get("content", ""))
        if text:
            out.append({"role": role, "content": text})

    return out


def load_conversations(
    jsonl_path: str,
    keep_system: bool,
    drop_assistant: bool,
    max_samples: int,
) -> List[List[Dict[str, str]]]:
    conversations: List[List[Dict[str, str]]] = []

    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line_idx, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            try:
                obj = json.loads(line)
            except Exception as e:
                print(f"[warn] line {line_idx} json parse failed: {e}")
                continue

            msgs = obj.get("messages", [])
            cleaned = _clean_messages(
                msgs,
                keep_system=keep_system,
                drop_assistant=drop_assistant,
            )

            if cleaned:
                conversations.append(cleaned)

            if len(conversations) >= max_samples:
                break

    return conversations


def conversations_to_calibration_texts(
    conversations: List[List[Dict[str, str]]],
    tokenizer,
) -> List[str]:
    texts: List[str] = []
    bad = 0

    for idx, msgs in enumerate(conversations):
        try:
            encoded = tokenizer.apply_chat_template(
                msgs,
                tokenize=True,
                add_generation_prompt=False,
                return_dict=True,
                return_tensors=None,
            )

            input_ids = encoded["input_ids"]
            attention_mask = encoded["attention_mask"]

            if len(input_ids) != len(attention_mask):
                bad += 1
                print(
                    f"[bad {idx}] input_ids len != attention_mask len: "
                    f"{len(input_ids)} vs {len(attention_mask)}"
                )
                continue

            if len(input_ids) == 0:
                bad += 1
                print(f"[bad {idx}] empty input_ids")
                continue

            text = tokenizer.decode(
                input_ids,
                skip_special_tokens=False,
                clean_up_tokenization_spaces=False,
            ).strip()

            if not text:
                bad += 1
                print(f"[bad {idx}] decoded text is empty")
                continue
            texts.append(text)

        except Exception as e:
            bad += 1
            print(f"[warn {idx}] chat_template failed: {e}")

    print(f"[template] usable={len(texts)} bad={bad}")
    return texts


def parse_args():
    p = argparse.ArgumentParser("Qwen3.5 GPTQ/AWQ quantize")

    p.add_argument(
        "--jsonl-path",
        default="",
        help="messages 格式 JSONL 文件路径",
    )
    p.add_argument("--model-id", default="/v18model", help="基座模型路径")
    p.add_argument(
        "--output-dir",
        default="",
        help="量化模型输出目录",
    )

    p.add_argument("--bits", type=int, default=4, help="量化位宽")
    p.add_argument("--group-size", type=int, default=128, help="分组大小")
    p.add_argument("--max-samples", type=int, default=16, help="最多使用多少条样本做校准")
    p.add_argument("--batch-size", type=int, default=1, help="校准时批大小")

    p.add_argument("--keep-system", action="store_true", help="是否保留 system 消息")
    p.add_argument("--drop-assistant", action="store_true", help="是否丢弃 assistant 回复")

    return p.parse_args()


def main():
    args = parse_args()

    print("加载模型 ...")
    qcfg = QuantizeConfig(
        bits=args.bits,
        group_size=args.group_size,
    )
    model = GPTQModel.load(args.model_id, qcfg, trust_remote_code=True)

    print("加载校准样本 ...")
    conversations = load_conversations(
        args.jsonl_path,
        keep_system=args.keep_system,
        drop_assistant=args.drop_assistant,
        max_samples=args.max_samples,
    )
    if not conversations:
        raise RuntimeError("校准数据加载失败或为空，请检查 JSONL_PATH 与内容格式。")

    print(f"原始 conversations 数量: {len(conversations)}")

    calibration_dataset = conversations_to_calibration_texts(
        conversations,
        model.tokenizer,
    )
    if not calibration_dataset:
        raise RuntimeError("chat_template 后没有可用文本，请检查 messages 格式。")

    model.quantize(calibration_dataset, batch_size=args.batch_size)

    os.makedirs(args.output_dir, exist_ok=True)
    model.save(args.output_dir)



if __name__ == "__main__":
    main()

**Expected behavior**

Theoretically, reducing the calibration dataset should lower GPU memory usage. However, even after reducing it, the memory consumption still increases linearly. Even with only 16 sample ,t still ends up running out of memory. By the time the quantization reaches layer 13, it is already using 130 GB of GPU memory.

**Model/Datasets**

Qwen3.5 27B Dense

**Screenshots**

If applicable, add screenshots to help explain your problem.

<img width="1538" height="255" alt="Image" src="https://github.com/user-attachments/assets/1a2f66de-011d-4050-b541-a982ed65ff15" />

<img width="1565" height="296" alt="Image" src="https://github.com/user-attachments/assets/a93c6a01-3913-481b-a014-5db52bf1e9f9" />


## 评论 (1)

### Qubitium · 2026-04-08

@Jealousc11gx  We are working to fix this asap. 
