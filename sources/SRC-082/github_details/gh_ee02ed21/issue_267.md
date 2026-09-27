# [Issue #267] TensorSize: Runtime Error

source: https://github.com/mit-han-lab/llm-awq/issues/267
state: closed | updated: 2025-04-10T01:15:06Z
labels: 

## 正文

Hi,

I'm encountering a persistent issue related to tensor size while running the Llama model on my Jetson AGX Orin (64GB). I've tried the suggested solutions but haven't been able to resolve the problem.

Device & Setup:

    Model: Llama
    Device: Jetson AGX Orin (64GB)

Despite switching between different versions of the transformers library, the issue persists. Any insights or suggestions would be greatly appreciated.

![Image](https://github.com/user-attachments/assets/5f1b3819-101d-46ba-9245-f8accb4c1e1f)

## 评论 (2)

### Louym · 2025-03-19

This issue arises because the KV cache is preallocated with a fixed size. When the context length exceeds the predefined limit, the keys (K) and values (V) no longer fit within the preallocated KV cache. You can address this by modifying kv_max_seq_len and trying again.

### sfatimakhan · 2025-04-10

Thanks, I was able to resolve it by changing the max_seq_length in the demo.py file.
