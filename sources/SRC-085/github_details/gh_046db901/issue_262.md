# [Issue #262] Clarification on How KVCache Is Utilized in EAGLE3 Training Flow

source: https://github.com/SafeAILab/EAGLE/issues/262
state: closed | updated: 2025-07-29T06:08:24Z
labels: 

## 正文

Hi EAGLE team, thank you for your great work on this project!

I’ve been reviewing the discussions on the use of KVCache class, and I understand the design motivation: to optimize inference efficiency by using a preallocated KV cache, with in-place cat() operations for key/value states.

However, while exploring the training pipeline in /traineagle3, I noticed something confusing:
	•	In the training code (main.py, cnet.py), there appears to be no import or direct reference to the KVCache class defined in /model.
	•	Meanwhile, /traineagle3/modeling_llama_kv.py still contains key_states = past_key_value[0].cat(...) calls, suggesting that KVCache is expected to be in use.
	•	But it’s unclear from the current training codebase how or where KVCache is initialized or passed into the model.

Since my understanding is that EAGLE uses the target model’s hidden states during training, and relies on KVCache to accelerate things, I was expecting to see it explicitly involved in the training flow — especially in the forward pass.

So my question is:

🟡 How exactly is the KVCache utilized during training in traineagle3?
Is it handled implicitly somewhere, or is there a step I’m missing in the setup?

Thanks in advance for any clarification!

## 评论 (2)

### hongyanz · 2025-07-22

Isn't KV-cache here?

https://github.com/SafeAILab/EAGLE/blob/a0e1e2c08604f0d215c531d9655b7ebacedde130/eagle/traineagle3/cnets.py#L265

### chriszhang1 · 2025-07-29

Hi @hongyanz, thank you so much for the reply!

My apologies for not making my initial question clearer. I was asking about the KV cache mechanism within the target_model (modeling_llama_kv.py), not the one being built in the main trainable model (cnets.py). 

My confusion stemmed from these lines in modeling_llama_kv.py:
https://github.com/SafeAILab/EAGLE/blob/cb7e3e459b969cd52a5e64307f9b166c276d0fd1/eagle/traineagle3/modeling_llama_kv.py#L709-L716

So, my current understanding is that in the training flow, the target_model is only used for a single, non-autoregressive forward pass to extract hidden states. Since KV cache is an optimization for autoregressive decoding, it isn't needed, which is why past_key_value is always None and that if block never executes.

Could you please confirm if this is the correct way to interpret the design? Your confirmation would be a great help. Thanks again!
