# [Issue #2454] [Bug]: when ignore specific module, bug happens

source: https://github.com/vllm-project/llm-compressor/issues/2454
state: closed | updated: 2026-07-07T04:37:09Z
labels: bug, stale

## 正文

### ⚙️ Your current environment

<details>
<summary>when i add "re:.*q_b_proj$", bug happens</summary>

```text
moe_ignores = [
    "lm_head",
    'model.layers.0.self_attn.indexer.weights_proj',
    'model.layers.1.self_attn.indexer.weights_proj',
'model.layers.2.self_attn.indexer.weights_proj',
 'model.layers.3.self_attn.indexer.weights_proj',
    'model.layers.4.self_attn.indexer.weights_proj',
    "re:.*q_b_proj$"
]
```

</details>


### 🐛 Describe the bug

File /usr/local/lib/python3.12/dist-packages/torch/nn/modules/linear.py:134, in Linear.forward(self, input)
    130 def forward(self, input: Tensor) -> Tensor:
    131     """
    132     Runs the forward pass.
    133     """
--> 134     return F.linear(input, self.weight, self.bias)

RuntimeError: expected mat1 and mat2 to have the same dtype, but got: c10::BFloat16 != double

### 🛠️ Steps to reproduce

_No response_

## 评论 (3)

### kylesayrs · 2026-03-09

@terenceucla Can you provide more context as to when this bug occurs? For example, does this occur during oneshot, sample generation, or loading your quantized model?

This may be related to fp4 support, have you tried loading your model with `dtype=torch.bfloat16`?

### github-actions[bot] · 2026-06-07

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### kylesayrs · 2026-07-07

This may be due to some bad hard coding from transformers. In any case, ignoring `q_b_proj` is uncommon and in theory there is no reason why it shouldn't work
