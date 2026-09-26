# [Issue #2271] [Kernel] Optimize triton decoding kernels for long context

source: https://github.com/sgl-project/sglang/issues/2271
state: open | updated: 2026-09-21T22:43:29Z
labels: good first issue, help wanted, high priority

## 正文

We noticed the current triton decoding kernel is very slow on long context. This is due to a missing flash decoding like optimization.

## Reproduce
We test the decoding speed with a context length of 200 and 2,000.

triton backend: The decoding speed drops from 147.64 token/s to 126.41 token/s
```
$ python3 -m sglang.bench_offline_throughput --model meta-llama/Llama-3.1-8B-Instruct --dataset-name random --num-prompt 1 --random-input 128 --random-output 2048 --random-range 1 --attention-backend triton

[2024-11-30 05:10:04 TP0] Decode batch. #running-req: 1, #token: 234, token usage: 0.00, gen throughput (token/s): 147.64, #queue-req: 0
... 
[2024-11-30 05:10:18 TP0] Decode batch. #running-req: 1, #token: 2154, token usage: 0.00, gen throughput (token/s): 126.41, #queue-req: 0
```

flashinfer backend: The decoding speed only drops from 144.17 token/s to 143.35 token/s
```
$ python3 -m sglang.bench_offline_throughput --model meta-llama/Llama-3.1-8B-Instruct --dataset-name random --num-prompt 1 --random-input 128 --random-output 2048 --random-range 1

[2024-11-30 05:11:40 TP0] Decode batch. #running-req: 1, #token: 234, token usage: 0.00, gen throughput (token/s): 144.17, #queue-req: 0
...
[2024-11-30 05:11:54 TP0] Decode batch. #running-req: 1, #token: 2154, token usage: 0.00, gen throughput (token/s): 143.35, #queue-req: 0
```

## Possible solutions
We can learn from the flash decoding triton kernel from lightllm and improve the [current triton decoding kernel](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/layers/attention/triton_ops/decode_attention.py). Related links:
- https://github.com/ModelTC/lightllm/blob/main/lightllm/models/llama/triton_kernel/gqa_flash_decoding.py
- https://pytorch.org/blog/flash-decoding/
- https://arxiv.org/pdf/2311.01282





## 评论 (7)

### merrymercy · 2024-11-30

cc @ispobock @HaiShaw

### github-actions[bot] · 2025-01-30

This issue has been automatically closed due to inactivity. Please feel free to reopen it if needed.

### xiefan46 · 2025-02-01

Hi @zhyncs @merrymercy, I saw @ispobock already sent out a PR but this issue is not closed yet. Are there still some remaining work of it? I am interested in working on this if there are still some remaining works. Could you give me more context about the current status of this issue?  

### ispobock · 2025-03-11

@xiefan46 @WANG-GH I think this issue can be closed. @zhyncs reopened it, I think it's to improve the long context performance of the extend/prefill Triton kernel? Maybe we can create a new issue for it.

Besides, current split-kv implementation of the Triton decoding kernel also can be further optimized. 

### WANG-GH · 2025-03-11

> [@xiefan46](https://github.com/xiefan46) [@WANG-GH](https://github.com/WANG-GH) I think this issue can be closed. [@zhyncs](https://github.com/zhyncs) reopened it, I think it's to improve the long context performance of the extend/prefill Triton kernel? Maybe we can create a new issue for it.
> 
> Besides, current split-kv implementation of the Triton decoding kernel also can be further optimized.

Thank you! Could you kindly provide further details on the current optimization points for the split-kV implementation of the Triton decoding kernel? I’m very excited to contribute to SGLang.

### MLKoz2 · 2026-03-10

I can see that this problem still exists, - for Qwen3.5 we can only use Triton , so at the moment long context + Qwen3.5 is almost unusable. I use it with speculative decoding (EAGLE3/MTP), but without it the degradation is smaller but still exists.

### hardikkgupta · 2026-04-12

Very new to this but I feel `max_kv_splits` is a bottleneck here and can change that
It is right now set to 8
