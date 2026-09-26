# [Issue #616] [RFC]: Add DFlash model converter

source: https://github.com/vllm-project/speculators/issues/616
state: closed | updated: 2026-06-24T19:47:03Z
labels: good first issue, RFC

## 正文

### Motivation.

The Speculators library supports finetuning pretrained speculator checkpoints via `--from-pretrained` arg in `train.py`. However, this only works for checkpoints already in the Speculators format (`DFlashSpeculatorConfig` + safetensors). There is no way to convert an externally-trained DFlash checkpoint into the Speculators format.

### Proposed Change.

Address the TODO in dflash/model,py, "once conversion is added, need to handle the case where a non speculator config is passed in as a kwarg and auto convert." When `from_pretrained` loads a checkpoint whose config.json is not a SpeculatorModelConfig, instead of raising TypeError, it will attempt auto-conversion:

  1. In `SpeculatorModel.from_pretrained()`, when the loaded config is not a SpeculatorModelConfig, identify if it's an external DFlash checkpoint (e.g., by inspecting config fields or weight key patterns).
  2. Invoke a `DFlashConverter` that:
    - Remaps external weight names to the DFlashDraftModel state dict layout (layers, fc, norm, hidden_norm, etc.)
    - Builds a DFlashSpeculatorConfig from the source config.json + verifier model config, including DFlash-specific fields (block_size, max_anchors, mask_token_id, aux_hidden_state_layer_ids, sliding_window_non_causal)
    - Handles t2d/d2t vocab mapping tensors if present
    - Saves the converted checkpoint to a cache/temp directory
  3. Load converted checkpoint — Continue the normal from_pretrained flow with the converted config and weights, returning a ready-to-use DFlashDraftModel.

### Any Other Things.

Optionally update the pathway for EAGLE3 as well. We should unify the behavior for both EAGLE3 and DFlash. Users should be able to use `--from-pretrained` to finetune EAGLE3 models.

## 评论 (6)

### guan404ming · 2026-06-18

Hi @shanjiaz could I help with this?

### shanjiaz · 2026-06-18

@guan404ming Assigned! Feel free to reach out with any questions!

### guan404ming · 2026-06-18

I just open a pr to resolve this issue #617, please help take a look and feel free to let me know if there is anything need to improve, thank in advance!

### shanjiaz · 2026-06-18

@guan404ming Thanks for your contribution, I think it's missing the `from_pretrained` part. We would like one united pathway for finetuning when user calls `from_pretrained` in `train.py`. It should work for external dflash format as well. Could you please implement this pathway as well? 

### guan404ming · 2026-06-18

Oh, I missed that part and I will implement it now. Thanks for letting me know!

### guan404ming · 2026-06-18

Hi @shanjiaz. I just Implemented the unified from_pretrained pathway, passing an external DFlash checkpoint + verifier now auto-converts and loads, no manual convert step. Verified on `z-lab/Qwen3-8B-DFlash-b16` with verifier `Qwen/Qwen3-8B` on an L4 GPU. PTAL, thanks!
