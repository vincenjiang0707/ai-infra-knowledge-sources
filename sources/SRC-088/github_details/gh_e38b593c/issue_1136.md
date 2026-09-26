# [Issue #1136] EAGLE-3 fails on any MoE verifier: Eagle3FirstLayerMixin adds a tuple to a tensor

source: https://github.com/vllm-project/speculators/issues/1136
state: closed | updated: 2026-09-18T06:07:18Z
labels: 

## 正文

`Eagle3FirstLayerMixin.forward` assumes `self.mlp` returns a tensor. MoE blocks in `transformers` return `(hidden_states, router_scores)`, so the residual add one line later raises `TypeError: unsupported operand type(s) for +: 'Tensor' and 'tuple'`. EAGLE-3 is therefore unusable with any MoE verifier.

[`model_definitions.py#L106-L109`](https://github.com/vllm-project/speculators/blob/main/src/speculators/models/eagle3/model_definitions.py#L106-L109)

```python
hidden_states = self.mlp(hidden_states)      # tuple for MoE
hidden_states = residual + hidden_states     # TypeError
```

### Reproduction

```python
import torch
from transformers import AutoConfig, AutoModelForCausalLM

config = AutoConfig.for_model("gpt_oss", num_hidden_layers=1, hidden_size=64,
                              num_attention_heads=4, num_key_value_heads=2,
                              intermediate_size=128)
with torch.device("meta"):
    model = AutoModelForCausalLM.from_config(config)
print(type(model.get_decoder().layers[0].mlp).__name__)  # GptOssMLP -> returns a tuple
```

### Fix

```python
mlp_output = self.mlp(hidden_states)
hidden_states = mlp_output[0] if isinstance(mlp_output, tuple) else mlp_output
```

Dense verifiers are unaffected. The rest of the rewrite already works for gpt-oss — the patched q/k/v feed `self.sinks` and `o_proj` unchanged and attention returns a correct tensor.

Branch ready with DCO sign-off; opening the issue first per CONTRIBUTING.

## 评论 (1)

### Hyungkeun-Park · 2026-09-18

Closing: the report is wrong.

I described this as blocking "any MoE verifier", but `transformer_layer_config` describes the draft, and the trainer builds it from `DRAFT_ARCH_CONFIGS` (`llama`/`qwen3`), so a MoE verifier never produces a MoE first layer. On `main` the path is unreachable anyway — `model_classes[tl_config.model_type]` raises `KeyError` for an unlisted family before the mixin runs. I reached it only through a local plugin that fills that table.

PR #1139 withdrawn. Sorry for the noise.
