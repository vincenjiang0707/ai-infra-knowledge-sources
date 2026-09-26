# [Issue #3159] [Bug]: Gemma 3 W4A16 checkpoint fails to load after vision module names change

source: https://github.com/vllm-project/llm-compressor/issues/3159
state: closed | updated: 2026-09-24T11:27:18Z
labels: bug

## 正文

### ⚙️ Your current environment

Compression and evaluation use separate environments.

Compression:
```text
Operating System: Linux-7.0.0-31-generic-x86_64-with-glibc2.39
Python Version: 3.12.3 (GCC 13.3.0)
llm-compressor Version: 0.13.0
compressed-tensors Version: 0.18.0
transformers Version: 5.14.1
torch Version: 2.13.0
CUDA Devices: NVIDIA GeForce RTX 3080
AMD/NPU/MPS Devices: None
```

Evaluation:
```text
Operating System: Linux-7.0.0-31-generic-x86_64-with-glibc2.39
Python Version: 3.12.3 (GCC 13.3.0)
llm-compressor Version: Not installed
compressed-tensors Version: 0.18.0
transformers Version: 5.16.1
torch Version: 2.13.0
lm-eval Version: 0.4.13
CUDA Devices: NVIDIA GeForce RTX 3080
AMD/NPU/MPS Devices: None
```

Compression used a supported Transformers version. Evaluation used a newer version than Compressor's supported upper bound.

### 🐛 Describe the bug

I compressed `google/gemma-3-4b-pt` using W4A16 RTN with the vision tower excluded. Compression completed, but loading the checkpoint with Transformers 5.16.1 through lm-evaluation-harness failed:

```text
File "transformers/models/siglip/modeling_siglip.py", in _init_weights
    init.lecun_normal_(module.weight)
AttributeError: 'Linear' object has no attribute 'weight'
```

The saved `quantization_config.ignore` contains names such as:

```text
vision_tower.vision_model.encoder.layers.0.self_attn.k_proj
```

However, the corresponding module in the evaluation environment is:

```text
model.vision_tower.encoder.layers.0.self_attn.k_proj
```

As a consequence, the exclusions no longer match and the loader attempts to quantize the vision layers. These layers should remain unquantized.

Changing only the exclusion metadata to allow the optional `model.` prefix and `vision_model.` segment allowed the same weights to load and complete a 20-document evaluation. For example:

```text
re:(?:model\.)?vision_tower\.(?:vision_model\.)?encoder\.layers\.0\.self_attn\.k_proj$
```

This suggests that module-name migration also needs to account for quantization exclusions. I am unsure whether the fix belongs in Compressor, compressed-tensors, or Transformers.

Possibly related: #1546.

### 🛠️ Steps to reproduce

Model: `google/gemma-3-4b-pt`
Revision: `cc012e0a6d0787b4adcc0fa2c4da74402494554d`

1. In the compression environment, load the model with `AutoModelForImageTextToText.from_pretrained`, using the revision above, `dtype="bfloat16"` and `device_map="cpu"`.

2. Apply `oneshot` without calibration data and save with `save_compressed=True`, using this recipe:

```yaml
compression_stage:
  quantization_modifiers:
    QuantizationModifier:
      targets: Linear
      scheme: W4A16
      ignore:
        - lm_head
        - 're:.*lm_head$'
        - 're:.*vision_tower.*'
        - 're:.*multi_modal_projector.*'
```

3. In the evaluation environment, load the saved checkpoint:

```bash
python -m lm_eval run --model hf \
  --model_args pretrained=/path/to/checkpoint,dtype=bfloat16,max_length=2048 \
  --tasks hellaswag --num_fewshot 0 --batch_size 1 \
  --device cuda:0 --seed 0 --limit 20
```

The failure occurs during model loading, before evaluation.

These steps were executed through a local wrapper around `oneshot` and the harness CLI. A standalone reproduction without the wrapper has not yet been tested.

## 评论 (3)

### dsikka · 2026-09-10

@Roderick-Wu can you take a look

### Roderick-Wu · 2026-09-10

Hi @SalisMaxima, this does just look like a version mismatch. Transformers 5.14->5.15 changed many mappings and caused quite a few issues for us. I believe we plan on pinning newer releases to >=5.15. If you take a look at one of our examples, specifically
https://github.com/vllm-project/llm-compressor/blob/main/examples/multimodal_vision/gemma3_example.py
it should contain the correct regex you're looking for. 

### SalisMaxima · 2026-09-24

Thanks for the clarification and the example :)
