# [Issue #705] [Bug]: Hidden state layer count mismatch in GLM-5.2 DFlash training pipeline

source: https://github.com/vllm-project/speculators/issues/705
state: closed | updated: 2026-07-30T13:54:28Z
labels: bug

## 正文

### Your current environment

Please provide the following information about your environment if applicable:

- vLLM 0.23
- Speculators 0.6
- CUDA 12.9
- PyTorch 2.11
- Transformers 5.10.4
- Hardware H200 && H100
- Model zai-org/GLM-5.2-FP8


### 🐛 Describe the bug

  There are two interconnected bugs in the DFlash training pipeline that cause shape mismatches when training with `--include-last-layer` / `--no-include-last-layer`.

  **Bug 1: Off-by-one in `launch_vllm.py` (line 67)**

  When `--include-last-layer` is used (the default), `launch_vllm.py` appends `num_hidden_layers` (the *count* of layers, e.g. 78) to `target_layer_ids`, but the last valid layer index is `num_hidden_layers - 1` 
  (e.g. 77) since layers are 0-indexed. This causes vLLM to try extracting hidden states from a non-existent layer, resulting in an expand error.

  Error message:
  RuntimeError: The expanded size of the tensor (6) must match the existing size (5) at non-singleton dimension 1.
  Target sizes: [2443, 6, 6144]. Tensor sizes: [2443, 5, 6144]

  **Bug 2: `ArrowDataset._get_raw_data()` unconditionally strips the last layer (line 381)**

  `ArrowDataset._get_raw_data()` always applies `[:, :-1]` to the loaded hidden states tensor, assuming the last layer is always the verifier's final layer. When data is generated with `--no-include-last-layer`
  (used as a workaround for Bug 1), the hidden states tensor contains only target layers. The unconditional `[:, :-1]` strips one target layer, causing a mismatch with the model's fully-connected layer.

  Error message:
  RuntimeError: mat1 and mat2 shapes cannot be multiplied (8192x24576 and 30720x6144)

  ### To Reproduce

  1. Launch vLLM with 5 target layer IDs and default `--include-last-layer`:
     ```bash
     python scripts/launch_vllm.py /path/to/model \
       --target-layer-ids 8 23 39 55 70 \
       --hidden-states-path /path/to/hidden_states \
       -- --tensor-parallel-size 8
     → Results in Bug 1 (layer index out of bounds)

  2. As a workaround, add --no-include-last-layer:
  python scripts/launch_vllm.py /path/to/model \
    --target-layer-ids 8 23 39 55 70 \
    --no-include-last-layer \
    --hidden-states-path /path/to/hidden_states \
    -- --tensor-parallel-size 8
  2. → Then run training → Results in Bug 2 (shape mismatch)

  Root Cause

  Bug 1 (launch_vllm.py:67):
```
  # num_hidden_layers is the COUNT (e.g. 78), not the last index (e.g. 77)
  if args.include_last_layer and num_hidden_layers not in target_layer_ids:
      target_layer_ids.append(num_hidden_layers)  # wrong: appends 78, should be 77
```

  Bug 2 (data.py:381):
```
  # Always strips the last layer, even when there's no final verifier layer
  return {
      "hidden_states": loaded_hs["hidden_states"][:, :-1].flatten(1),
      ...
  }
```

## 评论 (2)

### heiretodemon · 2026-07-01

After I fixed 2 bugs in launch_vllm.py, data.py and train.py， the GLM-5.2 DFlash training worked. 

### shanjiaz · 2026-07-03

Hey @heiretodemon thanks for creating this issue! Yeah this bit might be a little tricky. Long story short, this issue should be fixed by installing vLLM  main, but if you want to learn a bit more about this:

- We always append last layer because it's used in training. The last layer's hidden states `verifier_last_hidden_states` are passed through `verifier_norm + verifier_lm_head` to compute the verifier's logits, which serve as the training target. Just want to make sure your training run still captures it. 

- The issue you're seeing is caused by discrepancy in how aux hidden states are extracted in upstream vLLM. This is a convention mismatch in `deepseek_v2.py` that was recently fixed on vLLM main in [#46973](https://github.com/vllm-project/vllm/pull/46973). GLM-5.2-FP8 registers as `GlmMoeDsaForCausalLM`, which routes through `deepseek_v2.py`. On v0.23, that model captures hidden states before the layer runs with a bare index check, see [here](https://github.com/vllm-project/vllm/blob/releases/v0.23.0/vllm/model_executor/models/deepseek_v2.py#L1328). Speculators (and other vLLM models definitions) use a 1-indexed / post-layer convention where layer ID n means "output after layer n-1 runs". So when speculators sends num_hidden_layers (e.g. 78), it's valid under that convention, deepseek_v2.py's loop runs idx 0–77, so idx == 78 never matches, and you get one fewer hidden state than expected. So `launch_vllm.py` and `data.py` don't need changes, upgrading vLLM to a version with this fix should resolve both errors.
