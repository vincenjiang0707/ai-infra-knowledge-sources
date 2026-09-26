# [Issue #2621] AWQ Qwen3.5 MoE, error with the dimension alignment of apply_rotary_pos_emb

source: https://github.com/ModelCloud/GPTQModel/issues/2621
state: closed | updated: 2026-03-30T10:42:09Z
labels: bug

## 正文

When I use AWQ to quantizate the Qwen3.5 MoE 35B, there is a error arises with the dimension alignment of apply_rotary_pos_emb

<img width="1010" height="225" alt="Image" src="https://github.com/user-attachments/assets/cfb4b6d0-8080-446a-8b55-c6e16a1eb405" />

<img width="255" height="138" alt="Image" src="https://github.com/user-attachments/assets/405c994c-7fd5-4527-8b39-5f26e8cb308f" />

## 评论 (6)

### Qubitium · 2026-03-26

@Jealousc11gx Can you give me a short reproducing script? I will run that to reproduce. Thanks.

i also don't know what version of GPT-Qmodel you are using.

### Jealousc11gx · 2026-03-26

This is my Code: 
``` python #!/usr/bin/env python3
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
    p.add_argument("--batch-size", type=int, default=1, help="校准时批大小")  # Test Batchsize and Multi-GPU

    #Redirect Function

    p.add_argument("--keep-system", action="store_true", help="是否保留 system 消息")
    p.add_argument("--drop-assistant", action="store_true", help="是否丢弃 assistant 回复")

    return p.parse_args()


def main():
    args = parse_args()
    qcfg = QuantizeConfig(
        bits=args.bits,
        group_size=args.group_size,
        format=FORMAT.LLM_AWQ,
        quant_method=METHOD.AWQ,
    )
    model = GPTQModel.load(args.model_id, qcfg, trust_remote_code=True)
    conversations = load_conversations(
        args.jsonl_path,
        keep_system=args.keep_system,
        drop_assistant=args.drop_assistant,
        max_samples=args.max_samples,
    )
    if not conversations:
        raise RuntimeError("校准数据加载失败或为空，请检查 JSONL_PATH 与内容格式。")
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

**I just use two conversations to reproduce this error, all the other parameters remain default**

> {"messages": [{"role": "system", "content": [{"type": "text", "text": "You are a helpful and harmless assistant. Please translate the following text into Chinese"}]}, {"role": "user", "content": [{"type": "text", "text": "In 2012 they published a book that depicted Mohammed VI as a \"predator king\" who had carved up Morocco's economy to increase his personal wealth."}, {"type": "audio_url", "audio_url": ""}]}, {"role": "assistant", "content": [{"type": "text", "text": "在2012年，他们出版了一本书，将穆罕默德六世描述为“掠夺者之王”，他刻画了摩洛哥的经济，以增加他的个人财富。"}]}]}
{"messages": [{"role": "system", "content": [{"type": "text", "text": "You are a helpful and harmless assistant. Please translate the following text into Chinese"}]}, {"role": "user", "content": [{"type": "text", "text": "In 2012 two Snow White and the Seven Dwarfs (1937) remakes were released within months of each other: Mirror Mirror going up against Universal's Snow White and the Huntsman."}, {"type": "audio_url", "audio_url": ""}]}, {"role": "assistant", "content": [{"type": "text", "text": "2012年，两个白雪公主和七个小矮人（1937）的翻版在彼此之间的几个月内发布：Mirror Mirror与Universal的Snow White和Huntsman对抗。"}]}]}

**this is my GPTQmodel version**

GPTQModel Version:6.0.0

### arkerwu · 2026-03-27

AWQ quantization of Qwen3.5-27B or 9B version also has this issue.

### Qubitium · 2026-03-27

@ZX-ModelCloud  check this asap

### ZX-ModelCloud · 2026-03-27

You are likely using the `qwen3_5` model. I have successfully reproduced this error using the code you provided on `Qwen/Qwen3.5-27B` and have fixed it.

### Jealousc11gx · 2026-03-30

I use this script to quant Qwen3.5 35BA3B MoE, there is a another error:
 INFO  AWQProcessor: layer 0 tracking 774 modules before quantization (subsets processed=7/7); first modules=['linear_attn.in_proj_qkv', 'linear_attn.in_proj_z', 'linear_attn.out_proj', 'mlp.experts.0.gate_proj', 'mlp.experts.0.up_proj', 'mlp.experts.1.gate_proj', 'mlp.experts.1.up_proj', 'mlp.experts.2.gate_proj']
INFO  AWQProcessor: layer 0 sanitized 242 scaling groups; sample=[['linear_attn.in_proj_qkv'], ['mlp.experts.0.down_proj'], ['mlp.experts.1.down_proj']]
> Quantizing layer 0 of 39 ['p' to ||] [0 of 39] | 0:04:38 / 3:05:20 [1/40] 2.5%Traceback (most recent call last):
  File "/opt/miniconda3.10/lib/python3.10/site-packages/gptqmodel/utils/threadx.py", line 425, in _run
    result = fn(*args, **kwargs)
  File "/opt/miniconda3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)
  File "/opt/miniconda3.10/lib/python3.10/site-packages/gptqmodel/looper/stage_subset.py", line 719, in _process_on_worker
    proc.process(
  File "/opt/miniconda3.10/lib/python3.10/site-packages/gptqmodel/looper/awq_processor.py", line 1559, in process
    self._quantize_layer(layer_index, state)
  File "/opt/miniconda3.10/lib/python3.10/site-packages/gptqmodel/looper/awq_processor.py", line 719, in _quantize_layer
    scales_list = [
  File "/opt/miniconda3.10/lib/python3.10/site-packages/gptqmodel/looper/awq_processor.py", line 720, in <listcomp>
    self._search_best_scale(layer_module_ref, **layer)
  File "/opt/miniconda3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context
    return func(*args, **kwargs)
  File "/opt/miniconda3.10/lib/python3.10/site-packages/gptqmodel/looper/awq_processor.py", line 837, in _search_best_scale
    assert len(layers) == 1
AssertionError
