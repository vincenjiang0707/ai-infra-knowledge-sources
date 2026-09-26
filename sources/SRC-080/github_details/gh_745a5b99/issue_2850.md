# [Issue #2850] oneshot calibration of Gemma-4 multimodal corrupts tokenizer.json → audio truncated to ~12 mel frames

source: https://github.com/vllm-project/llm-compressor/issues/2850
state: open | updated: 2026-09-21T20:56:00Z
labels: stale

## 正文

### Summary

Running `oneshot` KV-cache calibration on a **Gemma-4 multimodal** checkpoint (e.g. `google/gemma-4-E2B-it`) and saving the result produces a checkpoint whose **audio inference is broken**. Serving it (vLLM) with an audio prompt crashes in the embedding merge:

```
ValueError: Attempted to assign 3 = 3 multimodal tokens to 399 placeholders
```

The audio feature extractor of the saved checkpoint yields only **~12 mel frames** for a 16 s clip (→ 3 audio embeddings), versus **~1594** frames for the original model (→ the expected ~399 audio tokens).

### Root cause (isolated)

The calibrated checkpoint's **`tokenizer.json`** differs from the source model's, and that file alone causes the truncation:

- Swapping **only** the calibrated `tokenizer.json` into an otherwise-pristine copy of the model **reproduces** the 12-frame truncation.
- A plain `AutoTokenizer.from_pretrained(model).save_pretrained(dir)` round-trip (no `oneshot`) does **not** truncate — the audio extractor still returns 1594 frames.

So the corruption is introduced by passing the tokenizer through `oneshot` (as `processor=`) and then saving it: `oneshot` mutates the tokenizer object such that its serialized `tokenizer.json`, when reloaded by the Gemma-4 processor, makes the audio feature extractor truncate. `added_tokens`/vocab look equivalent, but the file's md5 differs.

### Repro

```python
from transformers import AutoModelForImageTextToText, AutoTokenizer
from llmcompressor import oneshot
m = "google/gemma-4-E2B-it"
model = AutoModelForImageTextToText.from_pretrained(m, torch_dtype="bfloat16")
tok = AutoTokenizer.from_pretrained(m)
recipe = """
quant_stage:
  quant_modifiers:
    QuantizationModifier:
      ignore: ["lm_head","re:.*vision.*","re:.*audio.*","re:.*multi_modal.*"]
      kv_cache_scheme: {num_bits: 4, type: float, strategy: tensor, dynamic: false, symmetric: true}
"""
oneshot(model=model, processor=tok, dataset="open_platypus", recipe=recipe, num_calibration_samples=64)
model.save_pretrained("out"); tok.save_pretrained("out")
# Now load `out` with a processor and run the audio feature extractor on a ~16s clip:
# input_features come back as ~(1, 12, 128) instead of ~(1, 1594, 128).
```

### Workaround

After calibration, **copy the original processor/tokenizer files verbatim** into the output dir instead of re-saving them:

```python
from huggingface_hub import hf_hub_download
import shutil, os
for f in ["tokenizer.json","tokenizer_config.json","processor_config.json",
          "special_tokens_map.json","chat_template.jinja","generation_config.json"]:
    try: shutil.copy(hf_hub_download(m, f), os.path.join("out", f))
    except Exception: pass
```

With the original `tokenizer.json` restored, audio serves correctly (transcription matches the bf16 model).

### Environment
- llm-compressor 0.12.0, transformers 5.10.1
- Model: `google/gemma-4-E2B-it` (Gemma-4, image+audio)
- Quantizing only the KV cache (`kv_cache_scheme`); weights/vision/audio in `ignore`.

This blocks NVFP4/FP8 **KV-cache** calibration of Gemma-4 for any audio workload — you can't serve audio from the calibrated checkpoint without the workaround.


## 评论 (3)

### brian-dellabetta · 2026-06-22

Hi @jethac , it might just be that you need to use `AutoProcessor` instead of `AutoTokenizer`? Saving just the tokenizer means the audio component isn't included

### dsikka · 2026-06-23

Our suggested steps:

Loading:
```python
model = DiffusionGemmaForBlockDiffusion.from_pretrained(
    MODEL_ID, dtype="auto", trust_remote_code=True
)
processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)
```

Generation and Saving:
```python
print("========== SAMPLE GENERATION ==============")
dispatch_model(model)

# "The reason the sky is blue is because" + chat template
input_ids = torch.tensor(
    [[
        2, 105, 2364, 107, 818, 3282, 506, 7217, 563, 3730, 563,
        1547, 106, 107, 105, 4368, 107
    ]]
).to(model.device)

output = model.generate(
    input_ids,
    max_new_tokens=100,
    max_denoising_steps=48,
)
print(processor.tokenizer.decode(output[0]))
print("==========================================\n\n")

# Save to disk in compressed-tensors format
SAVE_DIR = MODEL_ID.rstrip("/").split("/")[-1] + "-NVFP4"
model.save_pretrained(SAVE_DIR)
processor.save_pretrained(SAVE_DIR)
```

This was used for our already quantized checkpoints:
https://huggingface.co/collections/RedHatAI/diffusiongemma-26b-a4b-it


### github-actions[bot] · 2026-09-21

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!
