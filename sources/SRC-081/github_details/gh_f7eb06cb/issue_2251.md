# [Issue #2251] [BUG] Incorrect Triton dequant_kernel for 3-bit GPTQ (INT3) leads to Triton compile error / wrong dequantization

source: https://github.com/ModelCloud/GPTQModel/issues/2251
state: closed | updated: 2025-12-12T10:17:09Z
labels: bug

## 正文



**Describe the bug**

When using GPTQModel with `bits=3` (INT3) on CUDA with Triton kernels enabled, the current `dequant_kernel` in:

`gptqmodel/nn_modules/triton_utils/dequant.py`

is incorrect in two ways:

1. **Triton compile-time error**

   The kernel uses tensor-valued conditions in Python `if` statements:

   ```python
   if zero_bit_offset <= 29:
       ...
   else:
       ...
   ```

   (and similarly for `weight_bit_offset`).

   With newer combinations of `torch` + `triton`, this triggers:

   ```text
   triton.compiler.errors.UnsupportedLanguageConstruct: 
   Boolean value of Tensor with more than one value is ambiguous
   at line: 
       if zero_bit_offset <= 29:
   ```

2. **Incorrect 3-bit decode logic (mismatch with PackableQuantLinear)**

   Even if the code is rewritten to avoid the Triton error, the original 3-bit dequant logic assumes a simple linear 3-bit bitstream:

   ```python
   zero_bit_pos  = (groups * out_features + col_idx) * 3
   zero_word_idx = zero_bit_pos // 32
   zero_bit_offset = zero_bit_pos % 32
   ...
   ```

   However, `BaseQuantLinear / PackableQuantLinear` for `bits == 3` use the GPTQ 3-bit packing scheme where each group of 32 values is packed into **3 × 32-bit words** in a `10-1-10-1-10` pattern (the same layout used in `dequantize_weight()` and `pack_block` for 3-bit).

   The Triton kernel’s 3-bit decode logic does **not** follow this layout, so the dequantized weights do not match the CPU reference implementation.

**Observed behavior**

* Quantize a model to INT3 → save **float** weights → reload float → evaluate → perplexity is normal.
* Quantize a model to INT3 → save **INT3 GPTQ** → load INT3 → evaluate with the Triton `dequant_kernel` → perplexity is extremely large / nonsensical (e.g. `bits_per_byte ≈ 4.8`, `word_perplexity ≈ 7e7` on wikitext).

---

**GPU Info**

```text
NVIDIA A800
```

---

**Software Info**

```text
Python 3.12.7

Name: accelerate
Version: 1.12.0
---
Name: gptqmodel
Version: 5.6.0
---
Name: torch
Version: 2.9.1
---
Name: transformers
Version: 5.0.0rc0
---
Name: triton
Version: 3.5.1
```

---

**config.json**

```json
{
  "architectures": [
    "Qwen3ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "dtype": "bfloat16",
  "eos_token_id": 151645,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 2560,
  "initializer_range": 0.02,
  "intermediate_size": 9728,
  "layer_types": [
    "full_attention",
    "...",
    "full_attention"
  ],
  "max_position_embeddings": 262144,
  "max_window_layers": 36,
  "model_type": "qwen3",
  "num_attention_heads": 32,
  "num_hidden_layers": 36,
  "num_key_value_heads": 8,
  "quantization_config": {
    "bits": 3,
    "checkpoint_format": "gptq",
    "desc_act": true,
    "format": "gptq",
    "group_size": 64,
    "lm_head": false,
    "meta": {
      "act_group_aware": false,
      "damp_auto_increment": 0.01,
      "damp_percent": 0.05,
      "gptaq": false,
      "gptaq_alpha": 0.25,
      "mse": 0.0,
      "quantizer": [
        "gptqmodel:5.6.0"
      ],
      "static_groups": false,
      "true_sequential": true,
      "uri": "https://github.com/modelcloud/gptqmodel"
    },
    "pack_dtype": "int32",
    "pack_impl": "cpu",
    "quant_method": "gptq",
    "sym": false
  },
  "rms_norm_eps": 1e-06,
  "rope_scaling": null,
  "rope_theta": 5000000,
  "sliding_window": null,
  "tie_word_embeddings": true,
  "transformers_version": "4.57.3",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 151936
}
```

**quantize_config.json**

```json
{
  "bits": 3,
  "group_size": 64,
  "desc_act": true,
  "sym": false,
  "lm_head": false,
  "quant_method": "gptq",
  "checkpoint_format": "gptq",
  "pack_dtype": "int32",
  "meta": {
    "quantizer": [
      "gptqmodel:5.6.0"
    ],
    "uri": "https://github.com/modelcloud/gptqmodel",
    "damp_percent": 0.05,
    "damp_auto_increment": 0.01,
    "static_groups": false,
    "true_sequential": true,
    "mse": 0.0,
    "gptaq": false,
    "gptaq_alpha": 0.25,
    "act_group_aware": false
  },
  "pack_impl": "cpu",
  "format": "gptq"
}
```

---

**To Reproduce**

1. Quantize a FP16 model (e.g. Qwen3-4B) to INT3:

   ```bash
   python -m gptqmodel.quantize \
       --model <your-fp16-model-path> \
       --bits 3 \
       --group_size 64 \
       --desc_act \
       --save_safetensors \
       --save_dir /path/to/gptq_INT3_g64
   ```

2. Load the quantized INT3 checkpoint with GPU + Triton enabled and evaluate on wikitext (using `lm_eval` or a custom script):

   ```bash
   python your_eval_script.py \
       --model_path /path/to/gptq_INT3_g64 \
       --tasks wikitext \
       --batch_size 2
   ```

3. Observe the Triton compile error:

   ```text
   triton.compiler.errors.UnsupportedLanguageConstruct:
   Boolean value of Tensor with more than one value is ambiguous
   ...
       if zero_bit_offset <= 29:
   ```

4. If you rewrite the `if zero_bit_offset <= 29` / `if weight_bit_offset <= 29` branches to use tensor-friendly logic (e.g. `tl.where`) without changing the overall bit layout assumption, the kernel compiles, but the wikitext perplexity becomes extremely large and clearly incorrect.

---

**Model / Datasets**

* Model: Qwen3-4B (but the issue should affect any decoder model quantized with `bits=3` in GPTQModel).
* Quantized checkpoint: 3-bit, `group_size=64`, `pack_dtype=int32`, `pack_impl=cpu`.
* Dataset: `EleutherAI/wikitext_document_level` (e.g. wikitext-103-raw-v1, wikitext-2-raw-v1).

---

**Additional context**

1. Current 3-bit snippet in the Triton kernel (simplified):

   ```python
   # Load zeros
   if bits == 3:
       zero_bit_pos  = (groups * out_features + col_idx) * 3
       zero_word_idx = zero_bit_pos // 32
       zero_bit_offset = zero_bit_pos % 32

       zero_word = tl.load(qzeros_ptr + zero_word_idx, mask=xmask, eviction_policy="evict_last")

       if zero_bit_offset <= 29:
           zeros = (zero_word >> zero_bit_offset) & 0b111
       else:
           next_zero_word = tl.load(qzeros_ptr + zero_word_idx + 1, mask=xmask, eviction_policy="evict_last")
           combined = (zero_word >> zero_bit_offset) | (next_zero_word << (32 - zero_bit_offset))
           zeros = combined & 0b111
   # ...
   # Load weights
   if bits == 3:
       weight_bit_pos = (row_idx * out_features + col_idx) * 3
       weight_word_idx = weight_bit_pos // 32
       weight_bit_offset = weight_bit_pos % 32

       weight_word = tl.load(qweight_ptr + weight_word_idx, mask=xmask, eviction_policy="evict_last")

       if weight_bit_offset <= 29:
           weights = (weight_word >> weight_bit_offset) & 0b111
       else:
           next_weight_word = tl.load(qweight_ptr + weight_word_idx + 1, mask=xmask, eviction_policy="evict_last")
           combined = (weight_word >> weight_bit_offset) | (next_weight_word << (32 - weight_bit_offset))
           weights = combined & 0b111
   ```

   Problems:

   * `if zero_bit_offset <= 29` / `if weight_bit_offset <= 29` use tensor conditions and are rejected by Triton.
   * The implicit “linear bitstream” assumption for 3-bit (`bit_pos = index * 3`) does not match the `10-1-10-1-10` packing used by `PackableQuantLinear`.

2. As a temporary workaround, I implemented a Triton version of the 3-bit decoder that directly mirrors the CPU packing scheme (`10-1-10-1-10`, 32 values → 3 words). With that version, INT3 inference runs without Triton errors and produces much more reasonable perplexities. I have opened a PR with a full Triton fix here: https://github.com/KingdalfGoodman/GPTQModel_fix_INT3/blob/main/gptqmodel/nn_modules/triton_utils/dequant.py



## 评论 (2)

### Qubitium · 2025-12-11

Thank you for the bug report. Can you create a pr with the triton 3bit fix?

### KingdalfGoodman · 2025-12-12

> Thank you for the bug report. Can you create a pr with the triton 3bit fix?

Here is the PR with the fix: https://github.com/ModelCloud/GPTQModel/pull/2258 
Best regards, Kingdalf : )
