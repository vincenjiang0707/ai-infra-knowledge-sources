# [Issue #3183] Support programmatic 3d moe repacking

source: https://github.com/vllm-project/llm-compressor/issues/3183
state: open | updated: 2026-09-17T10:54:26Z
labels: enhancement, good first issue, good follow-up issue

## 正文

## Background ##
Many models use 3d tensors to represent moe weights. LLM Compressor currently handles these by first separating them into 2d linear experts, then saving as 2d. However, vLLM often does not support loading 2d weights natively, which requires extra effort to support in vLLM.

Current flows for 3d checkpoints involve saving the compressed model in 2d, then using a custom script to repack them into 3d after the fact. See:
`RedHatAI/Inkling-NVFP4-FP8-BLOCK`

```
model.llm.layers.32.mlp.experts.w2_weight -> model.llm.layers.19.mlp.experts.w2_weight.input_global_scale
                                          -> model.llm.layers.19.mlp.experts.w2_weight.weight_global_scale
                                          -> model.llm.layers.19.mlp.experts.w2_weight.weight_packed
```

Current LLM Compressor utilities such as `repack_moe` do not support repacking quantized weights and not pack into a format which can be picked up by [conversion_mappings](https://github.com/huggingface/transformers/blob/main/src/transformers/conversion_mapping.py#L222-L226).

## Suggested Changes ##
* Modify `repack_moe` to handle compressed parameters
  * Replace `experts.gate_up_proj` and `experts.down_proj` with modules which contain the qparams and packed parameters (`weight_packed`, `weight_scale`, etc.)
* Use `inference-optimization/Inkling-0.6B-A0.6B` to test
  * Quantize to fp8/nvfp4 and confirm that the saved checkpoint has the same format as the original checkpoint (but with quantized parameters)
* Test with a larger model such as `Qwen/Qwen3.6-35B-A3B`

CC: @GOavi101

## 评论 (1)

### GOavi101 · 2026-09-16

 @kylesayrs .. you can assign it to me
