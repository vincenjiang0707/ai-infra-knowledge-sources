# [Issue #3371] [Model Request] Add IBM Granite 4.0 Architecture Support

source: https://github.com/mlc-ai/mlc-llm/issues/3371
state: open | updated: 2026-01-28T19:39:38Z
labels: 

## 正文

# [Model Request] Add IBM Granite 4.0 Architecture Support

## Model Information

**Model Family:** IBM Granite 4.0
**Models:**
- [granite-4.0-350m](https://huggingface.co/ibm-granite/granite-4.0-350m) (350M parameters)
- [granite-4.0-1b](https://huggingface.co/ibm-granite/granite-4.0-1b) (1.6B parameters)
- [granite-4.0-350m-base](https://huggingface.co/ibm-granite/granite-4.0-350m-base)
- [granite-4.0-1b-base](https://huggingface.co/ibm-granite/granite-4.0-1b-base)

**License:** Apache 2.0
**Purpose:** Integration into WebLLM for browser-based LLM inference

## Problem

Attempting to compile Granite models with MLC LLM fails due to architecture incompatibility. While Granite's architecture is very similar to Llama (both use decoder-only transformers with RoPE, RMSNorm, GQA, SiLU), Granite uses different layer naming conventions that prevent using `--model-type llama`.

## Architecture Details

### Similarities to Llama ✅
- **Position Encoding:** RoPE
- **Normalization:** RMSNorm
- **Attention:** Grouped Query Attention (GQA)
- **Activation:** SiLU
- **Structure:** Decoder-only transformer

### Key Difference: MLP Layer Naming ⚠️

**Llama expects:**
```
model.layers.{N}.mlp.gate_proj.weight
model.layers.{N}.mlp.up_proj.weight
model.layers.{N}.mlp.down_proj.weight
```

**Granite has:**
```
model.layers.{N}.shared_mlp.input_linear.weight
model.layers.{N}.shared_mlp.output_linear.weight
```

### Granite 350M Configuration
```json
{
  "model_type": "granitemoehybrid",
  "architectures": ["GraniteMoeHybridForCausalLM"],
  "hidden_size": 1024,
  "intermediate_size": 2048,
  "num_hidden_layers": 28,
  "num_attention_heads": 16,
  "num_key_value_heads": 4,
  "max_position_embeddings": 32768,
  "position_embedding_type": "rope",
  "vocab_size": 100544,
  "num_experts_per_tok": 0,  // Pure dense, not MoE
  "num_local_experts": 0
}
```

**Note:** Despite the name "granitemoehybrid", the 350M and 1B variants have `num_experts_per_tok: 0` making them **pure dense transformers**, not MoE models.

## Compilation Attempt

### Command Used
```bash
mlc_llm convert_weight \
  ./granite-4.0-350m \
  --quantization q4f16_1 \
  --model-type llama \
  --output dist/models/granite-4.0-350m-q4f16_1-MLC
```

### Error Output
```
ValueError: The following extern parameters do not exist in the weight files:
  model.layers.0.mlp.down_proj.weight
  model.layers.0.mlp.gate_proj.weight
  model.layers.0.mlp.up_proj.weight
  [... same for all 28 layers ...]
```

**Unused parameters found:**
```
model.layers.0.shared_mlp.input_linear.weight
model.layers.0.shared_mlp.output_linear.weight
[... same for all 28 layers ...]
```

## Why This Matters

1. **Efficiency:** Granite models are designed for efficiency and low latency
2. **License:** Apache 2.0 - enterprise-friendly
3. **Features:** Built-in tool calling, multilingual (12 languages), code completion
4. **Size Options:** 350M perfect for mobile/edge, 1B for desktop
5. **WebLLM:** Expands model portfolio with enterprise-focused options
6. **IBM Backing:** Well-maintained, production-ready models

## Request

I'm working on integrating Granite into WebLLM and need guidance on one of the following approaches:

### Option A: Custom Architecture Definition (Preferred)
Create a `granite_model.py` similar to existing model implementations. I'm willing to contribute a PR if someone can provide guidance on:

1. How to map Granite's `shared_mlp.{input/output}_linear` to standard MLP operations
2. Whether "shared" implies weight sharing across layers (or just naming)
3. Any Granite-specific considerations for the architecture class

### Option B: Existing Implementation
If IBM or the community has already created MLC LLM support for Granite, please point me to it!

### Option C: Workaround
If there's a simpler workaround (weight renaming, config modifications, etc.), I'm open to suggestions.

## Additional Context

- **Development Environment:** Python 3.11, MLC LLM nightly 0.1.dev1524
- **Platform:** macOS (Metal GPU detected and working)
- **Similar Models:** Successfully compiled Llama models as reference
- **Documentation Reviewed:** https://llm.mlc.ai/docs/compilation/define_new_models.html

## References

- **Granite Models:** https://huggingface.co/ibm-granite
- **Granite Announcement:** https://www.ibm.com/new/announcements/ibm-granite-4-0
- **WebLLM:** https://github.com/mlc-ai/web-llm
- **Model Card:** https://huggingface.co/ibm-granite/granite-4.0-350m

## Willingness to Contribute

I'm happy to:
- Test any proposed solutions
- Contribute a PR for Granite architecture support
- Document the integration process
- Help with debugging/iteration

Thank you for considering this model request! Granite's efficiency and features would be a great addition to the MLC LLM ecosystem.

---

**Labels:** new-models, enhancement, help wanted


## 评论 (1)

### simon-marcus · 2026-01-28

Just adding a 👍 because I'd love to see this implemented!
