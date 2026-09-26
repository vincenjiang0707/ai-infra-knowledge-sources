# [Issue #2694] [Compat] Finetuned Qwen3.5-MoE weights deviating from expectation: model.layers vs model.language_model.layers

source: https://github.com/ModelCloud/GPTQModel/issues/2694
state: closed | updated: 2026-04-12T03:10:22Z
labels: 

## 正文

Hi, I found the root cause of the garbled output issue when quantizing my Qwen3.5-MoE checkpoint with GPTQModel 6.0.3.

The problem is not just quantization quality. The MoE expert weights are not loaded correctly.

In my checkpoint, the expert keys are stored as:
- model.layers.{i}.mlp.experts.gate_up_proj
- model.layers.{i}.mlp.experts.down_proj

But during GPTQModel 6.0.3 load, the model expects:
- model.language_model.layers.{i}.mlp.experts.gate_up_proj
- model.language_model.layers.{i}.mlp.experts.down_proj

So the load report shows:
- `model.layers...` as `UNEXPECTED`
- `model.language_model.layers...` as `MISSING`

and the expert weights get re-initialized instead of loaded from checkpoint.

This explains why:
- the same checkpoint worked normally with GPTQModel 5.8.0 (only accuracy drop)
- but with 6.0.3 the quantized model output becomes garbled / nonsensical

I also verified with direct inspection that under my current transformers environment, the checkpoint contains:
- `model.layers.0.mlp.experts.gate_up_proj`
- `model.layers.0.mlp.experts.down_proj`

and does not contain:
- `model.language_model.layers.0.mlp.experts...`

So it looks like there is a path mismatch/regression in the qwen3_5_moe load logic for MoE expert weights in 6.0.3.


## 评论 (6)

### Qubitium · 2026-04-09

@caixiaoxx  We need full env print out. Also let us know the exact 3.5 MoE model you are testing. 

pip show transformers, torch, etc. 

### caixiaoxx · 2026-04-09

Here is the full environment information from the failing setup:

- GPTQModel: 6.0.3
- torch: 2.8.0+cu126
- transformers: 5.4.0
- Defuser: 0.0.18
- Python: 3.11
- Triton: 3.4.0

I just tested and found：
The issue does not reproduce on the original official model checkpoint, but it does reproduce on my fine-tuned checkpoint .

So the problem seems to be specific to how GPTQModel 6.0.3 handles the expert weight keys in post-trained Qwen3.5-MoE checkpoints, rather than the original official checkpoint format.


### Qubitium · 2026-04-09

> Here is the full environment information from the failing setup:
> 
> * GPTQModel: 6.0.3
> * torch: 2.8.0+cu126
> * transformers: 5.4.0
> * Defuser: 0.0.18
> * Python: 3.11
> * Triton: 3.4.0
> 
> I just tested and found： The issue does not reproduce on the original official model checkpoint, but it does reproduce on my fine-tuned checkpoint .
> 
> So the problem seems to be specific to how GPTQModel 6.0.3 handles the expert weight keys in post-trained Qwen3.5-MoE checkpoints, rather than the original official checkpoint format.

Due to how GPT-QModel weight loading works, we have a specific map for each model and we use the official weights + Transformers to make sure everyone is synced on that map. But in your case, the training pkg that finetuned the model saved in a different state than the original model. 

The error is likely in the trainer saving. We also need to check why 6.0.3 is stricter vs 5.8. 

Do this, you need to do a full `diff` of the `config.json` and also the `safetenors.index.json` between the original nd trained model to see what happened before/after. 

post the diffs so we can triage this further. 

### ZX-ModelCloud · 2026-04-09

``` python
from transformers import AutoModelForCausalLM, AutoModelForImageTextToText

model_id = "/monster/data/model/Qwen3.5-35B-A3B"
model_forCausalLM = AutoModelForCausalLM.from_pretrained(model_id)
print("model_forCausalLM:", model_forCausalLM)


model_forImageTextToText = AutoModelForImageTextToText.from_pretrained(model_id)
print("model_forImageTextToText:", model_forImageTextToText)
```

Output:
```
model_forCausalLM: 
Qwen3_5MoeForCausalLM(
  (model): Qwen3_5MoeTextModel
   ...
  (lm_head): Linear
)

model_forImageTextToText: 
Qwen3_5MoeForConditionalGeneration(
  (model):
    (language_model): Qwen3_5MoeTextModel
    ...
  (lm_head): Linear
)
```

When loading Qwen3.5-MoE models with different AutoModel classes:

### Using `AutoModelForImageTextToText`
- The loaded model **matches the original checkpoint structure**
- Parameter keys are **consistent with the pretrained weights**

### Using `AutoModelForCausalLM`
- The loaded model wraps only the **`Qwen3_5MoeTextModel`**
- Parameter keys become **different from the original checkpoint**



----

Since GPTQ-Model started supporting Qwen3_5_MoE in version 5.8.0, it has been using `AutoModelForImageTextToText` to load the model.

I have not yet identified why version 5.8.0 can successfully load your model, while version 6.0.3 cannot.

### caixiaoxx · 2026-04-09

I found the main issue and confirmed a workaround.

The original official checkpoint and my fine-tuned checkpoint use different MoE expert storage formats.

Original official checkpoint:
- fused expert format
- e.g.
  - `model.language_model.layers.N.mlp.experts.gate_up_proj`
  - `model.language_model.layers.N.mlp.experts.down_proj`

My fine-tuned checkpoint:
- expanded per-expert format
- e.g.
  - `model.language_model.layers.N.mlp.experts.{i}.gate_proj.weight`
  - `model.language_model.layers.N.mlp.experts.{i}.up_proj.weight`
  - `model.language_model.layers.N.mlp.experts.{i}.down_proj.weight`

I converted the fine-tuned checkpoint back to the fused format by:
- concatenating `gate_proj` + `up_proj` for each expert
- stacking all experts into fused `gate_up_proj`
- stacking all expert `down_proj` into fused `down_proj`

After this conversion:
- GPTQModel 6.0.3 load no longer shows the previous expert mismatch issue
- no `UNEXPECTED` / `MISSING` expert-weight warnings
- quantization proceeds normally

So for my case, the problem was caused by the fine-tuned checkpoint being saved in expanded per-expert format, while GPTQModel 6.0.3 works correctly once the checkpoint is converted back to the original fused expert format.

The issue is resolved on my side after converting the fine-tuned checkpoint back to the fused expert format. Thanks for the guidance and quick replies.

### Qubitium · 2026-04-09

@caixiaoxx  That explains everything. I do believe gpt-qmodel  can and should handle both cases. Fused and Unfused form of a particular model even if the original came in fused format. We already auto-unfuse fused models but in your case we should not asssume the model is always fused.  That assumption is the src of the compat issue you encountered. 

Please send me the full module map of the fine-trained model, not just partial, I need the full module tree as reprensted after you load the model and/or the safetensors.index.json file. I will make sure to use as guide to support both fuse/unfused versions.  I need to make sure the unfused version of your model is synced with our unfused logic. 
