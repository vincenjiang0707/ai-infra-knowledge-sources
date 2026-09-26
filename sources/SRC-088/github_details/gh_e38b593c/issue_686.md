# [Issue #686] [Bug]: Investigate and resolve DFlash speculators-vLLM inference divergence for Multi-Modal training

source: https://github.com/vllm-project/speculators/issues/686
state: closed | updated: 2026-07-03T11:59:50Z
labels: bug

## 正文

### Your current environment

| Component | Version |
|-----------|---------|
| vLLM | Latest main (installed from source at `/home/cyrus/vllm/`) |
| Speculators | `ef5541ac` (DarkLight1337/speculators `main`, base of PR #1) |
| Python | 3.13 |
| PyTorch | >= 2.9.0, <= 2.12.0 (per `pyproject.toml`) |
| Transformers | >= 4.56.1, < 5.13.0 (code references rope changes in transformers 5.0) |
| CUDA | (not specified in PR) |
| Hardware | (not specified in PR — multi-GPU, at least 3 GPUs based on CUDA_VISIBLE_DEVICES 1,2 defaults in comparison script) |
| Model (verifier) | `google/gemma-4-26B-A4B-it` |
| Attention backends | FLEX_ATTENTION (main model), FlashAttention v2 (draft model in vLLM), SDPA (draft model in speculators) |


### 🐛 Describe the bug

The DFlash draft model is implemented in both speculators (for training) and vLLM (for inference). Given the same model weights and the same input, both implementations should produce identical intermediate tensors at every stage of the forward pass. [DarkLight1337/speculators#1](https://github.com/DarkLight1337/speculators/pull/1) built a comparison harness that runs a Gemma4-26B-A4B-it input through both implementations, saves every intermediate tensor (Q/K/V projections, norms, RoPE outputs, attention outputs, MLP outputs, logits) at each of the 5 DFlash transformer layers, and measures the cosine similarity between the speculators and vLLM versions of each tensor. The results show significant divergence:

| Layer | Attention Inputs (Q,K,V) | attn_output | o_proj | layer_output |
|-------|--------------------------|-------------|--------|--------------|
| 0     | ~1.000                   | 0.911       | 0.996  | 0.902        |
| 1     | ~0.925                   | 0.752       | 0.712  | 0.779        |
| 2     | ~0.930                   | 0.752       | 0.822  | 0.725        |
| 3     | ~0.950                   | -           | -      | ~0.7         |
| 4     | ~0.950                   | -           | -      | ~0.7         |

Layer 0 attention inputs match perfectly, confirming the weights and projections are identical. But attention output drops to 0.91, and error accumulates through subsequent layers until final logits cosine similarity reaches **0.783**. 

For the same data point, we get high acceptance rates in Speculators but very low acceptance rates in vLLM.

## 评论 (2)

### orestis-z · 2026-06-30

Happy to pick this up if nobody's already looking into it. @shanjiaz are you investigating or would you like me to take it?

### shanjiaz · 2026-06-30

@orestis-z please do! Thanks. Let us know!
