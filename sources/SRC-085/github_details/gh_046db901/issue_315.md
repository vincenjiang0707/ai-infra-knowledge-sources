# [Issue #315] Fix dimension mismatch error when reproducing Eagle3-Qwen3-4B (hidden_size != head_dim * num_heads)

source: https://github.com/SafeAILab/EAGLE/issues/315
state: closed | updated: 2026-01-27T12:31:04Z
labels: 

## 正文

# Fix dimension mismatch error when reproducing Eagle3-Qwen3-4B (`hidden_size` != `head_dim * num_heads`)

## Description

I encountered a dimension mismatch error while attempting to reproduce the results for **Eagle3-Qwen3-4B**. The issue arises because the Qwen3 architecture (and its Eagle draft model) uses a configuration where `hidden_size` is not equal to `num_attention_heads * head_dim`.

This seems to be related to the issue mentioned in #223.

### Reproduction Steps

**1. Model Setup:**
* **Eagle Model:** [AngelSlim/Qwen3-4B_eagle3](https://huggingface.co/AngelSlim/Qwen3-4B_eagle3)
* **Base Model:** [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)

**2. Execution Command:**
```bash
python -m eagle.evaluation.gen_ea_answer_qwen3 \
    --ea-model-path "/path/to/Qwen3-4B_eagle3" \
    --base-model-path "/path/to/Qwen3-4B" \
    --model-id "qwen3-4b-bf16" \
    --use-eagle3
```

**3. Error Log:**
Upon execution, the following `RuntimeError` occurs during state dictionary loading:
```text
RuntimeError: Error(s) in loading state_dict for Model:
size mismatch for midlayer.self_attn.q_proj.weight: copying a param with shape torch.Size([4096, 5120]) from checkpoint, the shape in current model is torch.Size([2560, 5120]).
size mismatch for midlayer.self_attn.k_proj.weight: copying a param with shape torch.Size([1024, 5120]) from checkpoint, the shape in current model is torch.Size([640, 5120]).
size mismatch for midlayer.self_attn.v_proj.weight: copying a param with shape torch.Size([1024, 5120]) from checkpoint, the shape in current model is torch.Size([640, 5120]).
size mismatch for midlayer.self_attn.o_proj.weight: copying a param with shape torch.Size([2560, 4096]) from checkpoint, the shape in current model is torch.Size([2560, 2560]).
```

### Analysis

I inspected the `model.safetensors` of the Eagle model and the `config.json`.

**Checkpoint Dimensions (`model.safetensors`):**
* `midlayer.self_attn.q_proj.weight`: `[4096, 5120]`
* `midlayer.self_attn.o_proj.weight`: `[2560, 4096]`

**Config (`config.json`):**
* `"head_dim": 128`
* `"hidden_size": 2560`
* `"num_attention_heads": 32`

**The Conflict:**
In `eagle/model/cnets.py`, the code calculates `head_dim` derived from `hidden_size`:
`self.head_dim = self.hidden_size // self.num_heads` -> `2560 // 32 = 80`.

However, the config specifies `head_dim` is `128`.
* Code expectation: `32 heads * 80 dim = 2560`
* Actual weights: `32 heads * 128 dim = 4096`

This discrepancy causes the size mismatch.

### Solution

I applied the following fixes to `eagle/model/cnets.py` to resolve the issue.

#### Fix 1: Correct `head_dim` initialization in `LlamaAttention`

In `eagle/model/cnets.py`, modify the `__init__` method of `LlamaAttention` to prioritize the configuration's `head_dim` and remove the strict divisibility check.

```python
# eagle/model/cnets.py

class LlamaAttention(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.hidden_size = config.hidden_size
        self.num_heads = config.num_attention_heads

        # =========== FIX START ===========
        # Prioritize reading head_dim from config
        if hasattr(config, "head_dim"):
            self.head_dim = config.head_dim
        else:
            self.head_dim = self.hidden_size // self.num_heads
        # Original: self.head_dim = self.hidden_size // self.num_heads
        # =========== FIX END ===========

        self.num_key_value_heads = config.num_key_value_heads
        self.num_key_value_groups = self.num_heads // self.num_key_value_heads
        self.max_position_embeddings = config.max_position_embeddings

        # =========== FIX START ===========
        # Comment out this check as hidden_size != num_heads * head_dim for Qwen3
        # if (self.head_dim * self.num_heads) != self.hidden_size:
        #     raise ValueError(
        #         f"hidden_size must be divisible by num_heads (got `hidden_size`: {self.hidden_size}"
        #         f" and `num_heads`: {self.num_heads})."
        #     )
        # =========== FIX END ===========
        
        # ... rest of the init
```

#### Fix 2: Correct `reshape` in Forward Pass

After fixing the initialization, a secondary error occurs during the forward pass:
`RuntimeError: shape '[1, 41, 2560]' is invalid for input of size 167936`

This is because the code attempts to reshape the attention output back to `hidden_size` (2560), but the actual tensor size is based on `num_heads * head_dim` (4096).

Modify the `forward` method in `LlamaAttention`:

```python
# eagle/model/cnets.py around line 330

        attn_output = attn_output.transpose(1, 2).contiguous()
        
        # =========== FIX START ===========
        # Original: attn_output = attn_output.reshape(bsz, q_len, self.hidden_size)
        # The output dimension should be num_heads * head_dim (4096), not hidden_size (2560)
        attn_output = attn_output.reshape(bsz, q_len, self.num_heads * self.head_dim)
        # =========== FIX END ===========

        if self.config.pretraining_tp > 1:
             # ...
```

**Result:**
After applying these two changes, the model loads and runs successfully.

## 评论 (3)

### 7taozhou7 · 2025-12-16

I made the two changes you suggested, but I'm still getting the following error:
Loading EaModel...
`torch_dtype` is deprecated! Use `dtype` instead!
Loading checkpoint shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:03<00:00,  1.00s/it]
Using head_dim from config: 128
Using head_dim: 128 (hidden_size: 2560, num_heads: 32)
Error loading model: hidden_size must be divisible by num_heads (got `hidden_size`: 2560 and `num_heads`: 32).

### gcy-hw95 · 2025-12-16

> I made the two changes you suggested, but I'm still getting the following error: Loading EaModel... `torch_dtype` is deprecated! Use `dtype` instead! Loading checkpoint shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:03<00:00, 1.00s/it] Using head_dim from config: 128 Using head_dim: 128 (hidden_size: 2560, num_heads: 32) Error loading model: hidden_size must be divisible by num_heads (got `hidden_size`: 2560 and `num_heads`: 32).

Comment out the above check:
        # =========== FIX START ===========
        # Comment out this check as hidden_size != num_heads * head_dim for Qwen3
        # if (self.head_dim * self.num_heads) != self.hidden_size:
        #     raise ValueError(
        #         f"hidden_size must be divisible by num_heads (got `hidden_size`: {self.hidden_size}"
        #         f" and `num_heads`: {self.num_heads})."
        #     )
        # =========== FIX END ===========


### 7taozhou7 · 2025-12-16

Oh! It's my fault! I I thought there were only two changes needed... I've successfully got it running now, thank you!
