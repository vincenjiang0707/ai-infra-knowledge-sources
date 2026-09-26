# [Issue #223] when head_dim != self.hidden_size // self.num_heads

source: https://github.com/SafeAILab/EAGLE/issues/223
state: open | updated: 2025-11-21T07:49:34Z
labels: 

## 正文

Eagle has this limitation, while Qwen3-4B's head_dim doesn't follow the same rule. What can we do to work around this?
qwen3-4b: head_dim * num_heads = 128*32 = 4096 <> hidden_size = 2560

self.head_dim = self.hidden_size // self.num_heads
if (self.head_dim * self.num_heads) != self.hidden_size:
            raise ValueError(
                f"hidden_size must be divisible by num_heads (got `hidden_size`: {self.hidden_size}"
                f" and `num_heads`: {self.num_heads})."
            )
=====
https://huggingface.co/Qwen/Qwen3-4B/blob/main/config.json
  "head_dim": 128,
  "hidden_size": 2560,
  "model_type": "qwen3",
  "num_attention_heads": 32,
  "num_key_value_heads": 8,



## 评论 (1)

### gcy-hw95 · 2025-11-21

https://github.com/SafeAILab/EAGLE/issues/315
