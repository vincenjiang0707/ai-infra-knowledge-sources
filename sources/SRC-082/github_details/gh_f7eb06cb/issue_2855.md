# [Issue #2855] [BUG] Qwen3_5QModel uses AutoModelForImageTextToText for text-only qwen3_5_text model type

source: https://github.com/ModelCloud/GPTQModel/issues/2855
state: closed | updated: 2026-05-06T07:35:31Z
labels: bug

## 正文

Error working with: [squ11z1/claude-oss](https://huggingface.co/squ11z1/claude-oss)

## Summary

`gptqmodel` fails to quantize text-only Qwen3.5 models because `Qwen3_5QModel` hardcodes `AutoModelForImageTextToText` as its loader. The `qwen3_5_text` model type is mapped to this same class in `MODEL_MAP`, but text-only models require `AutoModelForCausalLM` and have a different module tree structure.

## Environment

- **gptqmodel version**: `>=7.0.0` (observed on latest)
- **transformers version**: `5.5.0`
- **Python**: 3.12
- **OS**: Linux

## Steps to Reproduce

1. Obtain a text-only Qwen3.5 model with `"model_type": "qwen3_5_text"` and `"architectures": ["Qwen3_5ForCausalLM"]` in its `config.json`.
2. Run:
   ```python
   from gptqmodel import GPTQModel, QuantizeConfig

   model = GPTQModel.from_pretrained(
       "/path/to/qwen3_5_text_model",
       quantize_config=QuantizeConfig(bits=4, group_size=128),
   )
   ```

## Error

```
ValueError: Unrecognized configuration class <class 'transformers.models.qwen3_5.configuration_qwen3_5.Qwen3_5TextConfig'>
for this kind of AutoModel: AutoModelForImageTextToText.
```

The error occurs at `gptqmodel/models/loader.py:539`:

```python
model = cls.loader.from_pretrained(model_local_path, config=config, **hf_model_init_kwargs)
```

where `cls.loader` is `AutoModelForImageTextToText` (set in `Qwen3_5QModel`), but the model config is `Qwen3_5TextConfig` which is not a valid config for `AutoModelForImageTextToText`.

## Root Cause

### 1. Wrong loader class

In `gptqmodel/models/definitions/qwen3_5.py`:

```python
from transformers import AutoModelForImageTextToText

class Qwen3_5QModel(LlamaQModel):
    loader = AutoModelForImageTextToText          # ← wrong for text-only
    require_load_processor = True                  # ← wrong for text-only
    module_tree = ["model", "language_model", "layers", "#", ...]  # ← wrong for text-only
    pre_lm_head_norm_module = "model.language_model.norm"           # ← wrong
    rotary_embedding = "model.language_model.rotary_emb"            # ← wrong
```

This is correct for **multimodal** Qwen3.5 (e.g. `Qwen3_5Config` / `Qwen3_5ForConditionalGeneration`), but wrong for **text-only** Qwen3.5 (`Qwen3_5TextConfig` / `Qwen3_5ForCausalLM`).

### 2. Incorrect model type mapping

In `gptqmodel/models/auto.py`:

```python
MODEL_MAP["qwen3_5"] = Qwen3_5QModel       # ← correct for multimodal
MODEL_MAP["qwen3_5_text"] = Qwen3_5QModel  # ← BUG: should NOT use multimodal loader
```

The `qwen3_5_text` model type should either:
- Map to a separate `Qwen3_5TextQModel` class with `loader = AutoModelForCausalLM`, or
- `Qwen3_5QModel` should dynamically select the loader based on the model config.

### 3. Additional import side-effect

`gptqmodel/models/definitions/internvl_chat.py` unconditionally imports `torchvision.transforms`, causing a `ModuleNotFoundError` if `torchvision` is not installed — even when quantizing models that have nothing to do with InternVL. This eager import of all model definitions means every `gptqmodel` install effectively requires `torchvision`.

## Expected Behavior

`GPTQModel.from_pretrained` should successfully load and quantize text-only Qwen3.5 models using `AutoModelForCausalLM`.

## Suggested Fix

### Option A: Add a separate model definition for text-only Qwen3.5

Create `gptqmodel/models/definitions/qwen3_5_text.py`:

```python
from transformers import AutoModelForCausalLM
from . import LlamaQModel

class Qwen3_5TextQModel(LlamaQModel):
    loader = AutoModelForCausalLM
    require_load_processor = False
    layer_modules_strict = False
    pre_lm_head_norm_module = "model.norm"
    # module_tree = None  # use auto-detection
```

And update `auto.py`:

```python
MODEL_MAP["qwen3_5_text"] = Qwen3_5TextQModel
```

### Option B: Make `Qwen3_5QModel` dynamic

In `qwen3_5.py`, detect at load time whether the model is text-only and adjust `loader`/`module_tree` accordingly.

## Workaround

Monkey-patch `Qwen3_5QModel` before calling `GPTQModel.from_pretrained`:

```python
from transformers import AutoConfig, AutoModelForCausalLM
from gptqmodel.models.definitions.qwen3_5 import Qwen3_5QModel
from gptqmodel import GPTQModel, QuantizeConfig

config = AutoConfig.from_pretrained(model_path, trust_remote_code=True)
if config.model_type == "qwen3_5_text":
    Qwen3_5QModel.loader = AutoModelForCausalLM
    Qwen3_5QModel.require_load_processor = False
    Qwen3_5QModel.module_tree = None
    Qwen3_5QModel.pre_lm_head_norm_module = None
    Qwen3_5QModel.rotary_embedding = None

model = GPTQModel.from_pretrained(model_path, quantize_config=QuantizeConfig(bits=4))
```

## Additional Context

The text-only Qwen3.5 model uses a hybrid architecture with alternating `linear_attention` and `full_attention` layers, plus `q_norm`/`k_norm` modules. Its module structure is `model.layers.#` (standard), not `model.language_model.layers.#` (multimodal wrapper).

## 评论 (1)

### ZX-ModelCloud · 2026-05-06

[PR#2857](https://github.com/ModelCloud/GPTQModel/pull/2857) has fixed this issue. Please install the latest code and try again.
