# [Issue #3106] Qwen3-Omni-30B-A3B-Thinking量化fp8_DYNAMIC问题，单卡OOM，双卡RuntimeError: We could not revert some weight conversions because of offlading...

source: https://github.com/vllm-project/llm-compressor/issues/3106
state: open | updated: 2026-08-27T16:21:43Z
labels: 

## 正文

做Qwen3-Omni-30B-A3B-Thinking量化的时候，使用单卡(NVIDIA RTX Pro 6000(96G))出现OOM问题。
换成双卡：
oneshot(
    model=model,
    recipe=recipe,
    save_compressed=True,
    output_dir=OUTPUT_DIR,
)
出现：RuntimeError: We could not revert some weight conversions because of offlading, and several weights needed for a single conversion operation living in different shard files. Try reducing `max_shard_size` a bit, or worst case set `save_original_format=False`.
如果：1、设置oneshot里save_compressed=False。
2、调用 model.save_pretrained() 手动保存，并指定 save_original_format=False 和 max_shard_size。
量化得到的模型，在vllm中运行出现：KeyError: 'layers.0.self_attn.qkv.weight_scale'


## 评论 (1)

### winniewyz · 2026-08-27

前面：
import os
import torch
from transformers import AutoProcessor, AutoModelForMultimodalLM
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import QuantizationModifier

os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

MODEL_ID = "./Qwen3-Omni-30B-A3B-Thinking"
OUTPUT_DIR = "./Qwen3-Omni-30B-A3B-Thinking-FP8"

processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)

model = AutoModelForMultimodalLM.from_pretrained(
    MODEL_ID,
    torch_dtype="auto",
    device_map="auto",
    max_memory={0: "80GB", 1: "80GB"},
    trust_remote_code=True,
    low_cpu_mem_usage=True,
)

if model.generation_config is not None:
    model.generation_config.do_sample = True

recipe = QuantizationModifier(
    targets="Linear",
    scheme="FP8_DYNAMIC",
    ignore=[
        "thinker.audio_tower.*",
        "thinker.visual.*",
        "thinker.lm_head",
    ]
)

后面：
processor.save_pretrained(OUTPUT_DIR)
