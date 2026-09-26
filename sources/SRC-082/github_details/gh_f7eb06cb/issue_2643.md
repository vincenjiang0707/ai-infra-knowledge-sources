# [Issue #2643] Does GPTQModel currently support quantizing MTP layers for Qwen3.5-MoE models?

source: https://github.com/ModelCloud/GPTQModel/issues/2643
state: closed | updated: 2026-04-07T11:08:21Z
labels: 

## 正文

Hi, thanks for the great project.

I am testing GPTQ quantization for a Qwen3.5-MoE model whose config contains:

- "architectures": ["Qwen3_5MoeForConditionalGeneration"]
- "model_type": "qwen3_5_moe"
- "text_config.mtp_num_hidden_layers": 1

The original model weights contain many `mtp`-related keys.

However, after calling `GPTQModel.load(...)`, I found that:

- `model.named_modules()` contains no `mtp` modules
- `model.state_dict()` contains no `mtp` keys
- the final quantized model also contains no `mtp` keys

So it looks like the MTP part is not loaded into the quantization model object, and therefore is not preserved in the quantized checkpoint.

My questions are:

1. Does GPTQModel currently support quantizing MTP layers for `Qwen3_5MoeForConditionalGeneration`?
2. If not, is this expected for the current implementation?
3. If support exists, is there any special loading / saving / config handling required to keep MTP layers?

I also noticed that GPTQModel has explicit MTP-related handling for some other models (for example GLM4 MoE), but I could not find similar handling for `qwen3_5_moe`.

Any clarification would be very helpful. Thanks.

## 评论 (3)

### Qubitium · 2026-04-04

@caixiaoxx Please post a reproduction script which reproduces your error so we can check our Qewn3 MoE support. 

I am not exactly sure what you asking here. What you are detailing appears ot be a custom Qwen3 model that is not a true Qwen3 model from the Qwen3 team? If that's the case, you need to produce the model so we can test.  I cannot speculate what can or cannot be supported for private models.

### caixiaoxx · 2026-04-07

Thanks, let me clarify with a more precise reproduction.

The key point is not only that `GPTQModel.load()` returns zero `mtp` modules/keys, but also that the original checkpoint does contain `mtp` keys before loading.

For example, when I inspect the original safetensors shards directly, I can find `mtp` keys in the checkpoint.
But after `GPTQModel.load(...)`, both:
- `named_modules mtp count`
- `state_dict mtp count`
become 0.

So the issue I am trying to confirm is whether MTP is intentionally ignored for `qwen3_5_moe`, or whether this is currently unsupported / missing.

I can provide:
- a sample of original `mtp` key names from the checkpoint
['mtp.fc.weight', 'mtp.layers.0.self_attn.o_proj.weight', 'mtp.layers.0.self_attn.q_proj.weight', 'mtp.layers.0.input_layernorm.weight', 'mtp.layers.0.mlp.experts.0.down_proj.weight', 'mtp.layers.0.mlp.experts.0.gate_proj.weight'...]
- the load script and the corresponding outputs

import os
import json
from safetensors import safe_open
from gptqmodel import GPTQModel, QuantizeConfig

MODEL_ID = "./Qwen/Qwen3.5-35B-A3B"

index_file = os.path.join(MODEL_ID, "model.safetensors.index.json")
with open(index_file, "r", encoding="utf-8") as f:
    index_data = json.load(f)

orig_mtp_keys = []
for shard in sorted(set(index_data["weight_map"].values())):
    shard_path = os.path.join(MODEL_ID, shard)
    with safe_open(shard_path, framework="pt", device="cpu") as f:
        for k in f.keys():
            if "mtp" in k.lower():
                orig_mtp_keys.append(k)

print("original checkpoint mtp count:", len(orig_mtp_keys))
print("original checkpoint mtp sample:", orig_mtp_keys[:20])

quant_config = QuantizeConfig(
    bits=4,
    group_size=128,
    sym=True,
    desc_act=False,
)

model = GPTQModel.load(
    MODEL_ID,
    quantize_config=quant_config,
    trust_remote_code=True,
)

mtp_module_names = [name for name, _ in model.named_modules() if "mtp" in name.lower()]
mtp_state_keys = [k for k in model.state_dict().keys() if "mtp" in k.lower()]

print("named_modules mtp count:", len(mtp_module_names))
print("state_dict mtp count:", len(mtp_state_keys))
print("named_modules mtp:", mtp_module_names[:20])
print("state_dict mtp:", mtp_state_keys[:20])

OUTPUTS:
named_modules mtp count: 0
state_dict mtp count: 0
named_modules mtp: []
state_dict mtp: []



### ZX-ModelCloud · 2026-04-07

Transformers will not load MTP weights. [modeling_qwen3_5_moe.py#L881](https://github.com/huggingface/transformers/blob/main/src/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py#L881) 

In [PR#2677](https://github.com/ModelCloud/GPTQModel/pull/2677), fixed the error where `qwen3_5_moe` was not saving `MTP` weights.
