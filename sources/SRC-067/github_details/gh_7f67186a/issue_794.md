# [Issue #794] install layer_norm

source: https://github.com/Dao-AILab/flash-attention/issues/794
state: open | updated: 2026-06-09T15:19:10Z
labels: 

## 正文

As of 2024-01-05, this extension is no longer used in the FlashAttention repo. We've instead switched to a Triton-based [implementation](https://github.com/Dao-AILab/flash-attention/blob/main/flash_attn/ops/triton/layer_norm.py).

Does this mean that we don't need to install  layer_norm through 【cd csrc/layer_norm && pip install .】this way？

## 评论 (8)

### tridao · 2024-01-27

Yeah

### MuyeMikeZhang · 2024-01-29

but i still get the warning.
![1](https://github.com/Dao-AILab/flash-attention/assets/46240302/f9ccc745-a37b-4dab-91dc-2e1274ac6ab2)
so, is there any problems, and do i need to install ?


### tridao · 2024-01-29

Sorry I don't control how other libraries use layer norm.

### MuyeMikeZhang · 2024-01-29

Since I always failed to install layer_norm through【cd csrc/layer_norm && pip install .】this way.
![image](https://github.com/Dao-AILab/flash-attention/assets/46240302/1e993b23-c9dd-4fd5-b2f5-6087a11fcc00)
can you help me to fix it?
Or if you have layer_norm xxx.whl file that adapts to the 【flash_attn-2.5.0+cu122torch2.1cxx11abiFALSE-cp310-cp310-linux_x86_64.whl】version？

### tridao · 2024-01-29

As mentioned it's depreciated. Other libraries may choose to use it, but I won't be working on that layernorm extension any more.

### MuyeMikeZhang · 2024-01-29

OK，thanks

### jimmylihui · 2024-01-30

Hi, How to use flash attention layernorm currently?

### shaform · 2026-06-09

Hello, if layernorm is not longer being used, should we create some deprecation warnings/errors when `flash_attn.ops.rms_norm` or `flash_attn.ops.layer_norm` is imported? Otherwise, it's very confusing when the error occurs and the only thing we could find is that the layer_norm is no longer being used.

> Sorry I don't control how other libraries use layer norm.


