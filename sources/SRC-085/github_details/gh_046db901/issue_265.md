# [Issue #265] About LM Head in EAGLE Model Parameters

source: https://github.com/SafeAILab/EAGLE/issues/265
state: closed | updated: 2025-08-17T20:36:17Z
labels: 

## 正文

According to the EAGLE3 paper, the draft model and target model should have separate LM heads. When I checked the saved parameters of my OLMoE Eagle model(https://huggingface.co/wantsleep/OLMoE_1B_7B_Eagle3), I can confirm that the lm_head is present:
```
=== Saved Parameter Keys ===
  1. d2t
  2. fc.weight
  3. lm_head.weight          ← LM head is present
  4. midlayer.hidden_norm.weight
  5. midlayer.input_layernorm.weight
  6. midlayer.mlp.down_proj.weight
  7. midlayer.mlp.gate_proj.weight
  8. midlayer.mlp.up_proj.weight
  9. midlayer.post_attention_layernorm.weight
 10. midlayer.self_attn.k_proj.weight
 11. midlayer.self_attn.o_proj.weight
 12. midlayer.self_attn.q_proj.weight
 13. midlayer.self_attn.v_proj.weight
 14. norm.weight
 15. t2d
```

However, when I checked the parameters of the Qwen3 EAGLE model provided(https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3), I found the following:
```
=== Saved Parameter Keys ===
  1. embed_tokens.weight
  2. layers.0.input_layernorm.weight
  3. layers.0.mlp.down_proj.weight
  4. layers.0.mlp.gate_proj.weight
  5. layers.0.mlp.up_proj.weight
  6. layers.0.post_attention_layernorm.weight
  7. layers.0.self_attn.k_proj.weight
  8. layers.0.self_attn.o_proj.weight
  9. layers.0.self_attn.q_proj.weight
 10. layers.0.self_attn.v_proj.weight
 11. norm.weight

``` 
The lm_head is missing from the Qwen EAGLE model parameter. Is this intentional design for the Qwen EAGLE model?

## 评论 (1)

### hongyanz · 2025-07-29

I am @ the author of this Huggingface repo. @jiahe7ay
