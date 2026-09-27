# [Issue #1462] Deleting StableEmbedding still occupies GPU RAM

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1462
state: closed | updated: 2026-02-16T11:47:29Z
labels: 

## 正文

### System Info

Python 3.10.6
Ubuntu 22.04.2 LTS
transformers 4.39.3

### Reproduction

```
import torch
import gc
import bitsandbytes

wte = bitsandbytes.nn.modules.StableEmbedding(50257, 1904)
wpe = bitsandbytes.nn.modules.StableEmbedding(50257, 1904)
wte.to("cuda")
wpe.to("cuda")

del wte
del wpe
gc.collect()
torch.cuda.empty_cache()

print(torch.cuda.memory_allocated() / 1024**3)
# 0.7148723602294922
print(torch.cuda.memory_reserved() / 1024**3)
# 0.716796875
```

### Expected behavior

I've attached the following snippet of code which is a simplication for the actual problem I'm facing. I've built a version of GPT that has Stable Embeddings and my use case requires me to constantly be reloading new versions of that model. I find that this leads to a gradual increase in GPU RAM usage over time.

To investigate this I've tried initialising the StableEmbeddings components on their own as per the above code snippet and then deleting them. The issue is that when I delete the variable and then empty out the cuda cache the GPU memory is still occupied by it.

## 评论 (1)

### TimDettmers · 2026-02-16

Closing this issue. The behavior you're observing — GPU memory remaining allocated after deleting `StableEmbedding` objects and calling `torch.cuda.empty_cache()` — is a known characteristic of CUDA memory management in PyTorch, not a bitsandbytes-specific bug.

`StableEmbedding` uses internal normalization state (from `torch.nn.Embedding` internals and the custom reset/init logic) that can leave references in PyTorch's autograd graph or CUDA context. The CUDA context itself also retains a baseline memory allocation for the lifetime of the process.

If you're loading/unloading models in a loop, the reliable approach is to use separate subprocesses for each model instance. This ensures full GPU memory reclamation between iterations.

If you're seeing unbounded memory growth (i.e., memory increases with each load/delete cycle beyond a fixed overhead), that would indicate a real leak — please open a new issue with measurements from multiple cycles showing the growth pattern.
