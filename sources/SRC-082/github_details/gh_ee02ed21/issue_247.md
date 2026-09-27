# [Issue #247] [BUG] GPU memory used is much more in v0.2.7 than  v0.2.5 while quantizing models.

source: https://github.com/mit-han-lab/llm-awq/issues/247
state: open | updated: 2025-01-16T11:19:37Z
labels: 

## 正文

The model I used is llama3-8B.
The only difference in the quantisation process is the versions, 0.2.7 and 0.2.5. 
**My gpu memory size is 16g, and I found that version 0.2.7 had problems with the memory being full, but 0.2.5 was able to quantise without any problems.** 
Has anyone else had similar problems?

## 评论 (3)

### GodHforever · 2024-12-20

After debugging with the new version code, I found that some memory was not released in `module2inspect`.
`clear_memory()` may be useful for this problem.
The code is awq/quantize/quantizer.py: `_compute_best_scale` 

```
int_w_output = self._module_forward(x, module2inspect, kwargs)
clear_memory()
```
Using this API here, memory consumption is reduced by about half
Will any one fix this or I just submit a patch?




### ruanr7 · 2025-01-08

Hello, I’ve encountered a similar issue. Could you please elaborate further on the solution? I wasn’t able to locate the code you mentioned.（T^T）

### GodHforever · 2025-01-16

> Hello, I’ve encountered a similar issue. Could you please elaborate further on the solution? I wasn’t able to locate the code you mentioned.（T^T）

I think the repo is changed, you can refer to https://github.com/casper-hansen/AutoAWQ

Then you can find it in [clear_memory](https://github.com/casper-hansen/AutoAWQ/blob/f1abb8ef8e261db78eb6c603f691801797fbb293/awq/utils/utils.py#L72)


Another way is that you can limit the memoy gpu used in your quant config. See [max_memory](https://github.com/casper-hansen/AutoAWQ/blob/f1abb8ef8e261db78eb6c603f691801797fbb293/awq/models/base.py#L455)
