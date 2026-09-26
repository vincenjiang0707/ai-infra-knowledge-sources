# [Issue #1118] [Bug]: speculators train crashes on heterogeneous per-layer verifier configs (e.g. Gemma 4)

source: https://github.com/vllm-project/speculators/issues/1118
state: open | updated: 2026-09-23T19:31:43Z
labels: 

## 正文

### Current environment

- **Speculators:** 0.9.0.dev18 (main)
- **Transformers:** 5.16.1 (any ≥ ~5.15, i.e. once `HeterogeneousConfigMixin` landed)
- **PyTorch:** 2.13.0
- **CUDA:** 13.x
- **Model (verifier):** `google/gemma-4-31B-it` (any heterogeneous config — see below)

### 🐛 Description of the bug

`speculators train` fails at config-build time whenever the verifier is a **heterogeneous per-layer config** (transformers ≥5.15). In the default draft-construction branch, `src/speculators/train/cli.py` reads per-layer attributes off the **global** verifier config. Since transformers ~5.15 puts `HeterogeneousConfigMixin` in the MRO of `PreTrainedConfig`, reading a per-layer attribute (`head_dim`, `num_key_value_heads`) off the global config of a model shipping a `per_layer_config` raises `AmbiguousGlobalPerLayerAttributeError` — which **subclasses `RuntimeError`, not `AttributeError`**, so `getattr(config, "head_dim", None)` does **not** swallow it.

Failing block in `train/cli.py`:

```
head_dim = getattr(verifier_config, "head_dim", None)          # :158  -> RAISES (first crash)
num_attention_heads = verifier_config.num_attention_heads      # :159  (global here, OK for gemma-4)
num_key_value_heads = verifier_config.num_key_value_heads      # :160  -> ALSO RAISES
```

The `getattr(..., None)` default never applies (the access itself raises), and handling only `:158` just moves the crash to `:160`.

**Minimal repro** (config only; no GPU/weights):

```
from transformers import AutoConfig
tc = AutoConfig.from_pretrained("google/gemma-4-31B-it").text_config
print(tc.is_heterogeneous)              # True
print(sorted(tc.per_layer_attributes))  # ['head_dim', 'num_key_value_heads']
getattr(tc, "head_dim", None)           # raises (not swallowed by the default)
```

```
transformers.integrations.heterogeneity.configuration_utils.AmbiguousGlobalPerLayerAttributeError:
'head_dim' is a per-layer attribute and may vary across layers. Access it via the individual layer
configs instead (e.g. config.per_layer_config[i].head_dim).
```

E2E: `speculators train --speculator-type dflash --verifier-name-or-path google/gemma-4-31B-it …` fails at `train/cli.py:158`.

### Scope / who this affects

Heterogeneity is data-driven at the base-config level, so this hits **any** current or future model shipping a `per_layer_config` — in transformers today: `gemma4`, `gemma4_unified`, `diffusion_gemma`, `step3p7`. I audited the other `head_dim` reads in speculators and they are **safe**: `models/dflash/model_definitions.py` and `models/eagle3/model_definitions.py` read the drafter's own homogeneous config, and `convert/eagle/eagle3_converter.py` reads a plain dict. **`train/cli.py` is the only vulnerable site.**

### Proposed fix

These reads only seed the draft's *own* default attention: they're hit solely in the default branch (overridden by `--draft-config` / `--from-pretrained`), where the draft's `transformer_layer_config` is built from the shaping flags. The real constraint is `hidden_size` — the residual-stream width the draft ingests, which is homogeneous and reads fine; `head_dim` / `num_key_value_heads` describe a layer's internal projections, not the width of its output, so they're free draft hyperparameters, not target facts to match. There's thus no "correct" global *or* per-layer value to recover — just a sensible default to pick.

When `verifier_config.is_heterogeneous`, resolve the affected attributes from a single concrete `verifier_config.per_layer_config[i]`, driven off `verifier_config.per_layer_attributes` (not a hardcoded name list) so it covers any per-layer attribute uniformly. Homogeneous configs keep the global read. This mirrors `convert/dflash/converter.py`'s concrete-per-layer read and retires the downstream `allow_global_per_layer_attribute_access` monkeypatch.

Default to the **modal** layer — on gemma-4-31B that's `head_dim=256` / `num_key_value_heads=16` (≈50/60 layers), the bulk geometry, giving a leaner/faster draft (draft latency is on the spec-decoding critical path). The minority full-attention shape (`512` / `4`) would only make the draft heavier with no acceptance-rate upside. Read from a single real layer so the trio stays internally consistent, and assert `num_attention_heads % num_key_value_heads == 0` (`num_attention_heads` stays a global read at `:159`) so a future model that also varies query-head count can't silently produce a malformed draft attention block.

Happy to open a small, focused, DCO-signed PR from a fork with a unit test using a fake heterogeneous config (touches `train/cli.py` + a test), per CONTRIBUTING.


## 评论 (1)

### ra-srivid · 2026-09-23

Opened #1129 as a starting point. Flagging it in case it's useful: small, self-contained fix for the config-build crash on heterogeneous per-layer verifiers (Gemma 4). If the approach looks right I'm glad to take it forward; if you'd rather fold it into existing gemma4 work or handle it another way, I can close it or adjust depending on the chosen approach.
