# [Issue #82] Question about past_key_value modification

source: https://github.com/SafeAILab/EAGLE/issues/82
state: open | updated: 2025-07-21T11:40:05Z
labels: 

## 正文

Hello Eagle Team!
I noticed you modified past_key_value in 
https://github.com/SafeAILab/EAGLE/blob/667ba930db7ea0075421f3c7df94ffbc10b93805/eagle/model/modeling_llama_kv.py#L594
by setting it to None in forward function, comparing with the source code
https://github.com/huggingface/transformers/blob/e51d7ac70ab8f3e69d3659226aa838308a668238/src/transformers/models/llama/modeling_llama.py#L324
Could you provide some insights why you made such changes? I am trying to generating responses with code-llama-7b with EAGLE's KVLlamaForCausalLM class, but the results are much lower quality than results I got with default AutoModelForCausalLM class. I suspect the kv cache affects the generation.

## 评论 (4)

### Liyuhui-12 · 2024-06-28

This modification is due to the use of pre-allocated KV cache to optimize the efficiency of the base model (this part of the code refers to [Medusa](https://github.com/SafeAILab/EAGLE/blob/667ba930db7ea0075421f3c7df94ffbc10b93805/eagle/model/modeling_llama_kv.py#L591C26-L591C40)). In the cat operation at 
https://github.com/SafeAILab/EAGLE/blob/667ba930db7ea0075421f3c7df94ffbc10b93805/eagle/model/modeling_llama_kv.py#L591-L592 the key and value of the current token have already been cached into past_key_value, so there is no need to return the key and value of the current token for operations outside the model. This modification itself will not affect model performance, but if you do not reset the length attribute of the KV cache after a generation, it will result in abnormal generation.

### jzzzf · 2024-07-03

@Liyuhui-12 Could you explain how we pass the value of past_key_value, if we set it to none? I am confused. Thank you for your help

### Lihui-Gu · 2025-05-26

Hello, I encountered the same issue, but I now understand the rationale behind this approach.

Define a custom KVCache class to enable preallocated GPU memory optimization. During attention computation, when past_key_value is provided, we call its .cat() method to directly write the newly computed key and value tensors into the preallocated memory buffer in-place. This avoids dynamic memory allocation and improves efficiency.

After the write operation, explicitly set past_key_value = None to clear the local variable and prevent it from being returned by the model. Since the cache is already updated in memory, returning it is unnecessary, aligning with our design for a centralized and persistent KV cache manager.

### chriszhang1 · 2025-07-21

@Lihui-Gu Hi, thanks for the clarification!

I just have a quick follow-up question: in EAGLE3, how is the KVCache class actually utilized by the target model? I noticed that in /traineagle3, neither main.py nor cnet.py directly import KVCache from /model. However, /traineagle3/modeling_llama_kv.py still appears to be implemented in the same way as described earlier in this thread—specifically, it still calls the cat() function from KVCache, yet without any explicit import.

Just wondering if I might be missing something here. Appreciate any pointers—thanks again!
