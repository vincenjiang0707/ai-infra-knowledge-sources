# [Issue #3071] [Bug]: Qwen3-VL-2B (dense) AWQ/GPTQ calibration fails, vision tower not FX-traceable (rot_pos_emb CUDA driver error), even with visual.* in ignore

source: https://github.com/vllm-project/llm-compressor/issues/3071
state: open | updated: 2026-08-27T16:58:18Z
labels: bug

## 正文

### ⚙️ Your current environment

<details>
<summary>The output of <code>python collect_env.py</code></summary>

```text
llm-compressor Version: 0.11.0
compressed-tensors Version: 0.16.0
transformers Version: 4.57.6
torch Version: 2.10.0+cu126
Python Version: 3.10.8
CUDA Devices: ['NVIDIA A100-SXM4-80GB']
CUDA Driver: 575.57.08 (CUDA 12.9)
```

</details>


### 🐛 Describe the bug

Calibrated quantization (AWQ and GPTQ, W4A16) of the **dense** Qwen3-VL-2B-Instruct fails during the sequential pipeline's FX tracing of the vision tower, even though all `visual.*` modules are in the quantization `ignore` list.

The `ignore` list correctly excludes the vision tower from *quantization*, but the sequential pipeline still *traces* through the vision tower to build the graph, and the Qwen3-VL vision code is not FX-traceable on transformers 4.57.x. Data-free RTN quantization of the same model works fine which isolates the problem specifically to the calibration/tracing path, not model loading or the environment.

**Recipe:**
`AWQModifier`, W4A16 (num_bits 4, int, group_size 128, symmetric, mse observer), `ignore=["re:.*lm_head", "re:.*visual.*"]`, `sequential_targets=["Qwen3VLTextDecoderLayer"]`. Also reproduced with `GPTQModifier(scheme="W4A16")` and the same ignore list.

**What works up to the crash:**
- Model loads; decoder-layer class confirmed as `Qwen3VLTextDecoderLayer`
- Vision modules confirmed under `model.visual.*`
- Calibration dataset builds correctly (256 samples, columns `['input_ids', 'attention_mask', 'pixel_values', 'image_grid_thw']`)
- "Preparing cache" completes; calibration starts at `(1/29)`
- AWQ mapping resolution runs ("28 mappings were skipped due to incompatible shapes")

**The crash:**\
Raised from inside `llmcompressor/pipelines/sequential/` while FX-tracing the model graph. The tracer walks `model.visual` (`get_image_features` → `self.visual` → `rot_pos_emb`), and the `.item()` call fails under tracing. Full traceback attached below.

**What I've already tried:**
- `ignore=["re:.*visual.*"]` — excludes the vision tower from quantization but not from tracing; still crashes.
- `torch._dynamo.config.suppress_errors = True` — no effect (the crash is in `torch.fx` symbolic tracing, not TorchDynamo).
- `replace_modules_for_calibration` — not applicable; it only replaces MoE blocks (`Qwen3VLMoeTextSparseMoeBlock`), and this is the dense 2B.
- Data-free RTN W4A16 and W8A16 on the same model — both succeed, confirming the failure is specific to the calibration/tracing path.

**Questions:**
1. Is there a supported way to make the sequential pipeline skip tracing the vision tower for a dense Qwen3-VL model, given `visual.*` is already in the quantization ignore list?
2. Is calibrated W4A16 (AWQ/GPTQ) currently supported for the **dense** Qwen3-VL family, or only the MoE variant? The working AWQ/GPTQ examples I could find are all MoE (30B-A3B).
3. Is a specific transformers version required where the Qwen3-VL vision code is FX-traceable? (huggingface/transformers#42077 reports the same trace failure and was closed without a linked fix.)

**Related issues:** #2066, #2151, #2153, #2000, #2025; huggingface/transformers#42077

**Full traceback:**

### 🛠️ Steps to reproduce

"""
Minimal reproduction: dense Qwen3-VL-2B-Instruct AWQ W4A16 calibration crash.

The vision tower is in the ignore list (excluded from quantization), but the
sequential pipeline still FX-traces it to build the graph, and Qwen3-VL's
rot_pos_emb is not traceable -> CUDA driver error: invalid argument.

Env: llmcompressor 0.11.0, compressed-tensors 0.16.0, transformers 4.57.6,
     torch 2.10.0+cu126, A100-80GB, driver 575 (CUDA 12.9).

Run: python repro_qwen3vl_awq_bug.py
"""

import base64
from io import BytesIO

import torch
from datasets import load_dataset
from qwen_vl_utils import process_vision_info
from transformers import AutoProcessor, Qwen3VLForConditionalGeneration

from llmcompressor import oneshot
from llmcompressor.modifiers.awq import AWQModifier

MODEL_ID = "Qwen/Qwen3-VL-2B-Instruct"      # dense
NUM_CALIBRATION_SAMPLES = 8
MAX_SEQUENCE_LENGTH = 1024

# ---- load ----
model = Qwen3VLForConditionalGeneration.from_pretrained(
    MODEL_ID, dtype=torch.bfloat16, device_map={"": 0})
processor = AutoProcessor.from_pretrained(MODEL_ID)

# ---- tiny calibration set from flickr30k ----
ds = load_dataset("lmms-lab/flickr30k", split=f"test[:{NUM_CALIBRATION_SAMPLES}]")

def preprocess(example):
    buffered = BytesIO()
    example["image"].save(buffered, format="PNG")
    b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    messages = [{
        "role": "user",
        "content": [
            {"type": "image", "image": f"data:image;base64,{b64}"},
            {"type": "text", "text": "What does the image show?"},
        ],
    }]
    text = processor.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True)
    image_inputs, _ = process_vision_info(messages)
    return processor(
        text=[text], images=image_inputs, videos=None,
        padding=False, max_length=MAX_SEQUENCE_LENGTH, truncation=True)

ds = ds.map(preprocess, remove_columns=ds.column_names)

def data_collator(batch):
    assert len(batch) == 1
    return {k: torch.tensor(v) for k, v in batch[0].items()}

# ---- AWQ W4A16, vision tower ignored ----
recipe = AWQModifier(
    config_groups={
        "group_0": {
            "targets": ["Linear"],
            "weights": {
                "num_bits": 4, "type": "int", "symmetric": True,
                "strategy": "group", "group_size": 128, "observer": "mse",
            },
            "input_activations": None,
            "output_activations": None,
        }
    },
    ignore=["re:.*lm_head", "re:.*visual.*"],   # vision tower excluded from quant
)

# ---- CRASH happens here, during sequential-pipeline FX tracing of the vision tower ----
oneshot(
    model=model,
    dataset=ds,
    recipe=recipe,
    data_collator=data_collator,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    sequential_targets=["Qwen3VLTextDecoderLayer"],
)

print("If you see this line, it did NOT crash.")

## 评论 (1)

### rishabhsinha17 · 2026-08-27

I tried to reproduce this with a tiny random-weight dense Qwen3-VL (same architecture as 2B-Instruct) on CPU, using your exact recipe, ignore list, and `sequential_targets=["Qwen3VLTextDecoderLayer"]`, and the oneshot run completes on both your combo (llmcompressor 0.11.0, transformers 4.57.6, compressed-tensors 0.16.0) and current main (transformers 5.16.x). Inspecting the traced graphs shows why: the sequential pipeline never fx-traces the vision tower, because the autowrapper cannot statically evaluate `if pixel_values is not None:` in `Qwen3VLModel.forward` and therefore wraps that whole branch, including `get_image_features` and `self.visual(...)`, into a `torch.fx.wrap`ped function that runs eagerly outside the graph. So calibrated W4A16 for dense Qwen3-VL is expected to work, and no vision node appears in any traced subgraph on either version.

That prediction now has hardware confirmation: on an L40S I ran your recipe end to end on current main against the real `Qwen/Qwen3-VL-2B-Instruct` — AWQ W4A16 (group_size 128, mse observer), `ignore=["re:.*lm_head", "re:.*visual.*"]`, `sequential_targets=["Qwen3VLTextDecoderLayer"]`, 256 flickr30k calibration samples, `CUDA_LAUNCH_BLOCKING=1`, llmcompressor 0.13.1.dev51+g50d0a1c75, transformers 5.16.1, compressed-tensors 0.18.1.a20260826, torch 2.11.0+cu128. It traces to the same 29 subgraphs your log shows, prints the same "28 mappings were skipped due to incompatible shapes" resolution warning, and completes: load to reloaded checkpoint in 6m35s, 5.4 GiB peak allocated VRAM, and the saved compressed model loads back cleanly. Calibrated AWQ W4A16 for dense Qwen3-VL works on main, eager CUDA execution of the wrapped vision branch included.

Your own log actually points the same way: calibration had already started at `(1/29)`, which means tracing had finished partitioning the model before the crash. That suggests your failure is not a structural tracing failure but a runtime fault while the wrapped vision branch executes eagerly on your device (CUDA errors are sticky, so an earlier async fault can surface later at the `.item()` in `rot_pos_emb` and look like a tracing bug). The traceback section of the issue came through empty, so could you post the full traceback, and ideally rerun with `CUDA_LAUNCH_BLOCKING=1` to get the true faulting op? Also worth trying current main instead of 0.11.0, fp16 or fp32 instead of bf16, and a single calibration sample, to see if the failure is version, dtype, or data dependent.

A CPU regression test pinning the working behavior (dense Qwen3-VL traces with the vision tower opaque, subgraphs execute with multimodal inputs; 2 passed in 0.23s in the same environment as the E2E above) is open as https://github.com/vllm-project/llm-compressor/pull/3107.

