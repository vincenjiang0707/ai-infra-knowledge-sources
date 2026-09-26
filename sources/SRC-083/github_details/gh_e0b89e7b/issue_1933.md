# [Issue #1933] Pytorch FutureWarning of _check_is_size

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1933
state: closed | updated: 2026-05-07T19:34:47Z
labels: 

## 正文

FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
https://github.com/bitsandbytes-foundation/bitsandbytes/blob/2de5ec3c22729c09b5e0c8b526a3b35b67ec5be2/bitsandbytes/_ops.py#L186

## 评论 (1)

### ANVLISTENER · 2026-04-30

Current: 

/home/user/venv/lib/python3.12/site-packages/bitsandbytes/backends/default/ops.py:223: 

torch._check_is_size(blocksize) # as in description

and

/home/libin/venv/lib/python3.12/site-packages/bitsandbytes/backends/cpu/ops.py:132:

torch._check_is_size(blocksize)

Fix: 

`torch._check(blocksize >= 0, lambda: f"Blocksize must be non-negative, got {blocksize}")`

But here is the catch, 

$python -c "import torch;print(torch.\_\_version\_\_)"
2.11.0+cu130

$python -c "import bitsandbytes;print(bitsandbytes.\_\_version\_\_)"
0.49.2

Background: 

`torch._check was not always in PyTorch. It is a modern addition closely tied to the torch.compile (torch 2.0+) ecosystem, introduced around the PyTorch 2.0-2.2`

Change done in torch: 

PR: https://github.com/pytorch/pytorch/pull/169400

https://github.com/pytorch/pytorch/commit/e58ebc5ffdf1d9104b1080f05806f5276849fb96

Handling torch version should be part of the code. (Depends what community decides in here)
