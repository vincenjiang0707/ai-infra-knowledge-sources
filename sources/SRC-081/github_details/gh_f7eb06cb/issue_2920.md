# [Issue #2920] Unsupported Model Type: gemma4_unified

source: https://github.com/ModelCloud/GPTQModel/issues/2920
state: closed | updated: 2026-06-15T14:14:28Z
labels: bug

## 正文

# Unsupported Model Type for `gemma-4-12B-it-abliterated-uncensored`

## Description
I encountered an error while attempting to quantize the model `OpenYourMind/gemma-4-12B-it-abliterated-uncensored` using the `GPTQModel`. The error indicates that the model type `gemma4_unified` is not supported, and the library failed to auto-detect the module tree for the model.

## Steps to Reproduce
1. Install the `GPTQModel` library from the repository:
   ```bash
   pip install git+https://github.com/ModelCloud/GPTQModel.git
   ```
2. Attempt to quantize the model `OpenYourMind/gemma-4-12B-it-abliterated-uncensored` using the following code:
   ```python
   from gptqmodel import GPTQModel

   model = GPTQModel.from_pretrained(
       "OpenYourMind/gemma-4-12B-it-abliterated-uncensored",
       revision="main",
       quantize_config={"bits": 4}
   )
   ```
3. The error occurs during the `from_pretrained` call.

## Error Log
```
ValueError: Unsupport model_type gemma4_unified, and failed to auto-detect module tree for model
Gemma4UnifiedForConditionalGeneration(
  (model): Gemma4UnifiedModel(
    (language_model): Gemma4UnifiedTextModel(
      (embed_tokens): Gemma4UnifiedTextScaledWordEmbedding(262144, 3840, padding_idx=0)
      (layers): ModuleList(
        (0-4): 5 x Gemma4UnifiedTextDecoderLayer(
          (self_attn): Gemma4UnifiedTextAttention(
            (q_proj): Linear(in_features=3840, out_features=4096, bias=False)
            (q_norm): Gemma4UnifiedRMSNorm()
            (k_norm): Gemma4UnifiedRMSNorm()
            (v_norm): Gemma4UnifiedRMSNorm()
            (k_proj): Linear(in_features=3840, out_features=2048, bias=False)
            (v_proj): Linear(in_features=3840, out_features=2048, bias=False)
            (o_proj): Linear(in_features=4096, out_features=3840, bias=False)
          )
          (mlp): Gemma4UnifiedTextMLP(
            (gate_proj): Linear(in_features=3840, out_features=15360, bias=False)
            (up_proj): Linear(in_features=3840, out_features=15360, bias=False)
            (down_proj): Linear(in_features=15360, out_features=3840, bias=False)
            (act_fn): GELUTanh()
          )
          (input_layernorm): Gemma4UnifiedRMSNorm()
          (post_attention_layernorm): Gemma4UnifiedRMSNorm()
          (pre_feedforward_layernorm): Gemma4UnifiedRMSNorm()
          (post_feedforward_layernorm): Gemma4UnifiedRMSNorm()
        )
        (5): Gemma4UnifiedTextDecoderLayer(
          (self_attn): Gemma4UnifiedTextAttention(
            (q_proj): Linear(in_features=3840, out_features=8192, bias=False)
            (q_norm): Gemma4UnifiedRMSNorm()
            (k_norm): Gemma4UnifiedRMSNorm()
            (v_norm): Gemma4UnifiedRMSNorm()
            (k_proj): Linear(in_features=3840, out_features=512, bias=False)
            (o_proj): Linear(in_features=8192, out_features=3840, bias=False)
          )
          (mlp): Gemma4UnifiedTextMLP(
            (gate_proj): Linear(in_features=3840, out_features=15360, bias=False)
            (up_proj): Linear(in_features=3840, out_features=15360, bias=False)
            (down_proj): Linear(in_features=15360, out_features=3840, bias=False)
            (act_fn): GELUTanh()
          )
          (input_layernorm): Gemma4UnifiedRMSNorm()
          (post_attention_layernorm): Gemma4UnifiedRMSNorm()
          (pre_feedforward_layernorm): Gemma4UnifiedRMSNorm()
          (post_feedforward_layernorm): Gemma4UnifiedRMSNorm()
        )
        # ... (truncated for brevity)
      )
    )
  )
)
```

## Expected Behavior
The model should be successfully quantized using the `GPTQModel` library, similar to other supported models.

## Environment
- **Python Version**: 3.14
- **GPTQModel Version**: Latest from `ModelCloud/GPTQModel`
- **Model**: `OpenYourMind/gemma-4-12B-it-abliterated-uncensored`



## 评论 (1)

### erm14254 · 2026-06-10

I’m seeing the same failure locally on a Gemma 4 unified model (gemma-4-12B-it).

Environment:

- OS: Windows 11 Pro
- Python: 3.12
- GPTQModel: 7.1.0
- Transformers: 5.10.2
- Torch: 2.11.0+cu130
- Triton: 3.6.0.post26
- Model class: Gemma4UnifiedForConditionalGeneration
- model_type: gemma4_unified

Error:

ValueError: Unsupport model_type gemma4_unified, and failed to auto-detect module tree

From the printed module tree, the quantizable text decoder appears to be nested under:

model.language_model.layers

Each decoder layer contains:

self_attn.q_proj
self_attn.k_proj
self_attn.v_proj
self_attn.o_proj
mlp.gate_proj
mlp.up_proj
mlp.down_proj

The full model is wrapped as Gemma4UnifiedForConditionalGeneration and also contains vision/audio embedding modules, so AutoCompat may be looking for the layer stack in the wrong place.

It seems like adding native support for gemma4_unified with the layer path `model.language_model.layers` would fix this class of failure.
