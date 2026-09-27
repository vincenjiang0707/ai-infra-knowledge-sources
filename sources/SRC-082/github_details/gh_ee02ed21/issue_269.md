# [Issue #269] update to support transformers 4.48

source: https://github.com/mit-han-lab/llm-awq/issues/269
state: open | updated: 2026-06-24T11:28:03Z
labels: 

## 正文

thanks for maintaining these neat implementations!

would be great to support transformers 4.48 as the previous versions have a security issue https://github.com/nvidia-holoscan/holohub/security/dependabot/35

currently llm-awq supports 4.46 and https://github.com/mit-han-lab/llm-awq/blob/52d3c26631bf62810bf4d4ab30e43d5b07818a38/pyproject.toml#L18 and there's an error when running with 4.48
```
stderr |   File "/workspace/llm-awq/tinychat/models/llama.py", line 146, in __init__
stderr |     self.rotary_emb = LlamaRotaryEmbedding(
stderr | TypeError: LlamaRotaryEmbedding.__init__() got an unexpected keyword argument 'max_position_embeddings'
```

## 评论 (1)

### Chessing234 · 2026-06-24

Opened a PR that fixes the LlamaRotaryEmbedding init for transformers 4.48+ by passing a LlamaConfig instead of the old head_dim/max_position_embeddings kwargs.
