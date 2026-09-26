# [Issue #166] Why does DeepEP LL kernel use double send/recv/signal buffers?

source: https://github.com/deepseek-ai/DeepEP/issues/166
state: closed | updated: 2026-09-18T10:05:34Z
labels: 

## 正文

Hi,

I noticed that in the DeepEP LL kernel implementation, there are two sets of send/recv/signal buffers being maintained. However, it seems that during each dispatch/combine communication,the current buffer is used, while the next buffer is cleared. From my observation, both buffers are not used simultaneously.

Is there a specific reason for using double buffers here? Would creating a single buffer suffice, considering they are not active at the same time? 

Appreciate any insights—thanks for your great work on this project!

## 评论 (4)

### LyricZhao · 2025-05-22

For extreme low-latency consideration, we only use a "single-direction" signaling mechanism: 

> sender: send data, send flag
> receiver: wait flag, receive data

This is unsafe if the sender exits and launch the **next** dispatch/combine, which will rewrite the same buffer if the receiver still reading the buffer of the **current** dispatch/combine.

Add another direction signal will solve this and save half the VRAM, but the latency will be worse:

> sender: send data, send flag, wait finish-read flag
> receiver: wait flag, receive data, send finish-read flag

### LyricZhao · 2025-05-22

For double buffer, even considering 3 contiguous comm kernels, we can proof no buffer-rewrites.

### LyricZhao · 2025-05-22

Oh, "the current buffer is used, while the next buffer is cleared" is also important. Otherwise, cleaning should insert here:

> sender: send data, send flag, wait finish-read flag
> receiver: wait flag, receive data, **clean**, send finish-read flag

With double buffer, the cleaning can be parallelized for lower latency.

### LyricZhao · 2025-05-22

Actually, the current online batch-size is large and such operations may be not importart anymore. But when we were designing the V3 family, the target TPS is high and such optimization is somehow worth doing if VRAM is enough.
